#!/usr/bin/env python

import sys
import json
from rdflib import Graph

def run_query(data_file, query_file, result_file):
    g = Graph()
    g.parse(data_file, format='turtle')

    with open(query_file, 'r') as qf:
        query = qf.read()

    results = g.query(query)
    results_json = results.serialize(format='json')

    with open(result_file, 'w') as rf:
        rf.write(results_json.decode('utf-8') if isinstance(results_json, bytes) else results_json)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: run_sparql_query.py <data_file> <query_file> <result_file>")
        sys.exit(1)
    
    data_file = sys.argv[1]
    query_file = sys.argv[2]
    result_file = sys.argv[3]
    
    run_query(data_file, query_file, result_file)