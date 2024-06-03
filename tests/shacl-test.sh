#!/bin/bash

# Directory containing SHACL shapes and sample data
SHACL_DIR="./tests/shacl"
SHAPES_DIR="${SHACL_DIR}/shapes"
SAMPLE_DATA_DIR="${SHACL_DIR}/sample-data"
REPORTS_DIR="${SHACL_DIR}/reports"

# Ensure reports directory exists
mkdir -p $REPORTS_DIR

# Run SHACL validation
for shape in ${SHAPES_DIR}/*.ttl; do
    for data in ${SAMPLE_DATA_DIR}/*.ttl; do
        echo "Validating $data against $shape"
        pyshacl -s $shape -d $data > ${REPORTS_DIR}/$(basename $data .ttl)_$(basename $shape .ttl)_report.txt
        if [ $? -ne 0 ]; then
            echo "SHACL validation failed for $data against $shape"
            exit 1
        fi
    done
done

echo "SHACL validation completed successfully."