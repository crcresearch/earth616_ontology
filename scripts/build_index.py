#!/usr/bin/env python3
"""
Build an index ontology (index.ttl) by merging project metadata and auto-discovered modules and patterns.
"""
import os
import sys
import argparse
from urllib.parse import urljoin

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL


def build_index_graph(metadata_path, modules_dir, patterns_dir=None):
    """
    Build an RDFLib Graph for the index ontology.
    - Loads metadata TTL (defines the owl:Ontology IRI).
    - Scans modules_dir for .ttl and .owl files, adds owl:imports for each.
    - Scans patterns_dir for .ttl files, adds owl:imports for each.
    Returns the populated Graph.
    """
    g = Graph()
    # Load metadata; assume Turtle serialization
    try:
        g.parse(metadata_path, format='turtle')
    except Exception as e:
        sys.stderr.write(f"Error parsing metadata '{metadata_path}': {e}\n")
        sys.exit(1)

    # Find the ontology IRI
    ontology_iris = list(g.subjects(predicate=RDF.type, object=OWL.Ontology))
    if not ontology_iris:
        sys.stderr.write("No owl:Ontology subject found in metadata file.\n")
        sys.exit(1)
    ontology_iri = ontology_iris[0]
    base_iri = str(ontology_iri)

    # Helper to add imports
    def add_imports(path_root, subpath_prefix, extensions):
        for root, _, files in os.walk(path_root):
            for fname in sorted(files):
                if not any(fname.lower().endswith(ext) for ext in extensions):
                    continue
                full = os.path.join(root, fname)
                rel = os.path.relpath(full, path_root).replace(os.path.sep, '/')
                rel_no_ext = os.path.splitext(rel)[0]
                import_iri = URIRef(urljoin(base_iri, f"{subpath_prefix}/{rel_no_ext}"))
                g.add((ontology_iri, OWL.imports, import_iri))

    # Add modules
    add_imports(modules_dir, 'modules', ['.ttl', '.owl'])
    # Add patterns if provided
    if patterns_dir:
        add_imports(patterns_dir, 'patterns', ['.ttl'])

    return g


def main():
    parser = argparse.ArgumentParser(
        description="Build index ontology (index.ttl) from metadata, modules, and patterns"
    )
    parser.add_argument('--metadata', '-m', required=True,
                        help='Path to core metadata TTL file')
    parser.add_argument('--modules', '-d', required=True,
                        help='Path to modules directory')
    parser.add_argument('--patterns', '-p', default=None,
                        help='Path to patterns directory (optional)')
    parser.add_argument('--out', '-o', required=True,
                        help='Output file path for index TTL')
    args = parser.parse_args()

    # Build graph
    graph = build_index_graph(args.metadata, args.modules, args.patterns)
    # Serialize to Turtle
    try:
        graph.serialize(destination=args.out, format='turtle')
        print(f"Index ontology written to {args.out}")
    except Exception as e:
        sys.stderr.write(f"Error writing index TTL to '{args.out}': {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()