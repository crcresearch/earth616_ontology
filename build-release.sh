#!/bin/bash

set -e

# Directory paths
SCRIPTS_DIR="./scripts"
RELEASE_DIR="./release/ontology"
LATEST_DIR="${RELEASE_DIR}/latest"
VERSION=$(grep -i versionInfo modules/core/metadata.ttl | sed 's/[^"]*"\([^"]*\).*/\1/')
VERSION_DIR="${RELEASE_DIR}/${VERSION}"

# Commands
MERGE_CMD="${SCRIPTS_DIR}/merge_ontology.py"
VALIDATE_CMD="${SCRIPTS_DIR}/validate_turtle.py"
WIDOCO_DOCKER_CMD="docker run -ti --rm -v $(pwd)/${VERSION_DIR}:/usr/local/widoco/in -v $(pwd)/${VERSION_DIR}:/usr/local/widoco/out/doc dgarijo/widoco"

# Files
FILES=$(cat tests/modules.txt | awk -F, '{print $2}')

# Ensure version directory exists
prepare_directory() {
    local dir=$1
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
    mkdir -p "$dir"
}

prepare_directory "$VERSION_DIR"
prepare_directory "$LATEST_DIR"

# Validate Turtle files for syntax errors
echo "Validating Turtle files for syntax errors"
$VALIDATE_CMD $FILES

# Merge ontology files
echo "Merging Ontology into Release ${VERSION}"
$MERGE_CMD "${VERSION_DIR}/merged.ttl" $FILES

# Run SHACL validation
echo "Running SHACL validation"
./tests/shacl/shacl-test.sh

# Run SPARQL Competency Questions validation
echo "Running SPARQL CQ validation"
./tests/sparql/sparql-test.sh

# Generate documentation with Widoco
echo "Generating Ontology Documentation via Widoco"
$WIDOCO_DOCKER_CMD -ontFile in/merged.ttl -outFolder out -rewriteAll -webVowl

# Copy to latest directory
echo "Updating latest directory"
cp -r "${VERSION_DIR}/." "${LATEST_DIR}"
