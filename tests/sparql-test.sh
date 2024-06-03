#!/bin/bash

# Directory containing SPARQL queries and expected results
SPARQL_DIR="./tests/sparql"
QUERIES_DIR="${SPARQL_DIR}/queries"
EXPECTED_RESULTS_DIR="${SPARQL_DIR}/expected-results"
REPORTS_DIR="${SPARQL_DIR}/reports"
SCRIPTS_DIR="./scripts"

# Ensure reports directory exists
mkdir -p $REPORTS_DIR

# Temporary file to store query results
TEMP_RESULT=$(mktemp)

# Run SPARQL queries and compare results
for query in ${QUERIES_DIR}/*.rq; do
    expected_result="${EXPECTED_RESULTS_DIR}/$(basename $query .rq).json"
    echo "Running SPARQL query: $query"
    
    # Execute the SPARQL query using the Python script
    $SCRIPTS_DIR/run_sparql_query.py ./release/ontology/latest/merged.ttl $query $TEMP_RESULT
    
    # Compare the query result with the expected result
    diff $TEMP_RESULT $expected_result > ${REPORTS_DIR}/$(basename $query .rq)_report.txt
    if [ $? -ne 0 ]; then
        echo "SPARQL validation failed for query $query"
        echo "Differences found between actual result and expected result."
        exit 1
    fi
done

# Cleanup temporary file
rm $TEMP_RESULT

echo "SPARQL validation completed successfully."