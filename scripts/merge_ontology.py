#!/usr/bin/env python

import sys
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager

def merge_ontologies(output_file, *input_files):
    g = Graph()
    
    # Set up namespace manager with consistent prefixes
    namespace_manager = NamespaceManager(g)
    
    # Collect all potential DSCDO namespace variations
    dscdo_namespaces = set()
    canonical_dscdo_namespace = None
    
    # Parse all input files and collect namespace info
    for input_file in input_files:
        temp_graph = Graph()
        temp_graph.parse(input_file, format='turtle')
        
        # Collect all earth616 namespace variations
        for prefix, namespace in temp_graph.namespace_manager.namespaces():
            if 'vocab.earth616' in str(namespace) and 'scdoc/ont' in str(namespace):
                dscdo_namespaces.add(str(namespace))
                # Prefer the version with trailing slash for consistency
                if canonical_dscdo_namespace is None or str(namespace).endswith('/'):
                    canonical_dscdo_namespace = str(namespace)
        
        # Add triples to main graph
        g += temp_graph
    
    # Ensure canonical namespace ends with slash for best practices
    if canonical_dscdo_namespace and not canonical_dscdo_namespace.endswith('/'):
        canonical_dscdo_namespace += '/'
    
    # Set up consistent namespace prefixes
    if canonical_dscdo_namespace:
        namespace_manager.bind('dscdo', canonical_dscdo_namespace, override=True)
        namespace_manager.bind('', canonical_dscdo_namespace, override=True)  # Default namespace
    
    # Bind other common namespaces with consistent prefixes
    namespace_manager.bind('owl', 'http://www.w3.org/2002/07/owl#', override=True)
    namespace_manager.bind('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', override=True)
    namespace_manager.bind('rdfs', 'http://www.w3.org/2000/01/rdf-schema#', override=True)
    namespace_manager.bind('xsd', 'http://www.w3.org/2001/XMLSchema#', override=True)
    namespace_manager.bind('skos', 'http://www.w3.org/2004/02/skos/core#', override=True)
    namespace_manager.bind('dcterms', 'http://purl.org/dc/terms/', override=True)
    namespace_manager.bind('prov', 'http://www.w3.org/ns/prov#', override=True)
    namespace_manager.bind('schema', 'http://schema.org/', override=True)
    namespace_manager.bind('time', 'http://www.w3.org/2006/time#', override=True)
    namespace_manager.bind('geo', 'http://www.opengis.net/ont/geosparql#', override=True)
    
    # Apply the namespace manager to the graph
    g.namespace_manager = namespace_manager
    
    # Serialize with the consistent prefixes
    # Note: rdflib may omit unused prefixes during serialization
    serialized_content = g.serialize(format='turtle')
    
    # Ensure dscdo prefix is included in the output even if not used in triples
    lines = serialized_content.split('\n')
    prefix_lines = []
    content_lines = []
    in_prefixes = True
    
    for line in lines:
        if in_prefixes and (line.startswith('@prefix') or line.startswith('@base') or line.strip() == ''):
            prefix_lines.append(line)
        else:
            in_prefixes = False
            content_lines.append(line)
    
    # Add dscdo prefix if not already present and we have a canonical namespace
    if canonical_dscdo_namespace:
        dscdo_prefix_line = f"@prefix dscdo: <{canonical_dscdo_namespace}> ."
        if not any('dscdo:' in line for line in prefix_lines):
            # Insert after the default namespace declaration
            insert_index = len(prefix_lines) - 1  # Before the empty line that separates prefixes from content
            prefix_lines.insert(insert_index, dscdo_prefix_line)
    
    # Reconstruct and write the file
    final_content = '\n'.join(prefix_lines + content_lines)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: merge_ontology.py <output_file> <input_file1> <input_file2> ...")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    merge_ontologies(output_file, *input_files)