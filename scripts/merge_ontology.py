#!/usr/bin/env python

import sys
from rdflib import Graph

def merge_ontologies(output_file, *input_files):
    g = Graph()
    for input_file in input_files:
        g.parse(input_file, format='turtle')
    g.serialize(destination=output_file, format='turtle')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: merge_ontology.py <output_file> <input_file1> <input_file2> ...")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    merge_ontologies(output_file, *input_files)