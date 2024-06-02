#!/usr/bin/env python

import sys
from rdflib import Graph

def validate_turtle(file):
    g = Graph()
    try:
        g.parse(file, format='turtle')
        print(f"{file} is valid.")
    except Exception as e:
        print(f"Error in {file}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_turtle.py <file1> <file2> ...")
        sys.exit(1)
    for file in sys.argv[1:]:
        validate_turtle(file)