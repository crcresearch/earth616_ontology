#!/usr/bin/env python3
"""
Build a pyLODE supermodel profile TTL that declares each module as a lode:Module.
Reads the ontology IRI from modules/core/metadata.ttl and test module list from tests/modules.txt.
"""
import os
import sys
import argparse

from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL

PROF = Namespace("http://www.w3.org/ns/dx/prof/")
LODE = Namespace("http://purl.org/lode/config#")
DCTERMS = Namespace("http://purl.org/dc/terms/")

def read_ontology_iri(metadata_path):
    g = Graph()
    g.parse(metadata_path, format='turtle')
    for s in g.subjects(RDF.type, OWL.Ontology):
        return str(s)
    sys.stderr.write(f"Error: no owl:Ontology in {metadata_path}\n")
    sys.exit(1)

def build_profile(metadata_path, modules_txt, out_path):
    base_iri = read_ontology_iri(metadata_path)
    graph = Graph()
    graph.bind('prof', PROF)
    graph.bind('lode', LODE)
    graph.bind('dcterms', DCTERMS)
    graph.bind('rdfs', RDFS)

    # Build a single supermodel profile for the ontology
    ontology_iri = URIRef(base_iri)
    graph.add((ontology_iri, RDF.type, PROF.Profile))
    # For each module in tests/modules.txt, add a ResourceDescriptor
    from rdflib import BNode
    for line in open(modules_txt):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(',', 1)
        if len(parts) != 2:
            continue
        _, path = parts
        path = path.strip()
        rel = os.path.relpath(path, 'modules').replace(os.path.sep, '/')
        rel_no_ext = os.path.splitext(rel)[0]
        module_iri = URIRef(f"{base_iri}modules/{rel_no_ext}")
        desc = BNode()
        graph.add((ontology_iri, PROF.hasResource, desc))
        graph.add((desc, RDF.type, PROF.ResourceDescriptor))
        graph.add((desc, PROF.hasRole, LODE.config))
        graph.add((desc, DCTERMS['format'], Literal('text/turtle')))
        graph.add((desc, PROF.hasArtifact, module_iri))

    # Serialize profile TTL
    graph.serialize(destination=out_path, format='turtle')
    print(f"Supermodel profile written to {out_path}")

def main():
    p = argparse.ArgumentParser(description='Build pyLODE supermodel profile TTL')
    p.add_argument('--metadata', '-m', default='modules/core/metadata.ttl',
                   help='Path to core metadata TTL')
    p.add_argument('--modules-txt', '-t', default='tests/modules.txt',
                   help='Path to tests/modules.txt')
    p.add_argument('--out', '-o', required=True,
                   help='Output TTL file path')
    args = p.parse_args()
    build_profile(args.metadata, args.modules_txt, args.out)

if __name__ == '__main__':
    main()