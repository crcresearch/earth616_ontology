#!/usr/bin/env bash
set -e
# If a Python virtualenv exists, activate it so python3 and rdflib are available
if [ -f ".venv/bin/activate" ]; then
    # shellcheck source=/dev/null
    . ".venv/bin/activate"
fi

# Usage:
#   build-release.sh [--mode=standard|oplax] [--docs=widoco|pylode]
#
#   --mode=oplax    include patterns imports (OPLaX mode); default: standard imports
#   --docs=widoco   generate HTML via Widoco container
#   --docs=pylode   generate HTML via pyLODE; default: pylode
#
# Parse options
MODE=standard
DOCS=pylode
for arg in "$@"; do
  case "$arg" in
    --mode=oplax) MODE=oplax ;; 
    --docs=widoco) DOCS=widoco ;; 
    --docs=pylode) DOCS=pylode ;; 
    *) echo "Unknown option: $arg"; exit 1 ;; 
  esac
done

# Directory paths
SCRIPTS_DIR="./scripts"
RELEASE_DIR="./release/ontology"
LATEST_DIR="${RELEASE_DIR}/latest"
VERSION=$(grep -i versionInfo modules/core/metadata.ttl | sed 's/[^"]*"\([^"]*\).*/\1/')
VERSION_DIR="${RELEASE_DIR}/${VERSION}"

# Directory paths for contexts and shapes
CONTEXTS_DIR="./contexts"
SHAPES_DIR="./shapes"
CONTEXTS_RELEASE_DIR="./release/contexts"
SHAPES_RELEASE_DIR="./release/shapes"

# Commands
MERGE_CMD="${SCRIPTS_DIR}/merge_ontology.py"
VALIDATE_CMD="${SCRIPTS_DIR}/validate_turtle.py"
WIDOCO_DOCKER_CMD="docker run -ti --rm -v $(pwd)/${VERSION_DIR}:/usr/local/widoco/in -v $(pwd)/${VERSION_DIR}:/usr/local/widoco/out/doc dgarijo/widoco"

# Files
FILES=$(cat tests/modules.txt | awk -F, '{print $2}')
# Module TTLs for pyLODE supermodel documentation
MODULE_TTLS="modules/core/*.ttl modules/scdocumentation/*.ttl modules/supplychain/*.ttl"

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

# Create version-specific directories for contexts and shapes
prepare_directory "${CONTEXTS_RELEASE_DIR}/${VERSION}"
prepare_directory "${CONTEXTS_RELEASE_DIR}/latest"
prepare_directory "${SHAPES_RELEASE_DIR}/shacl/${VERSION}"
prepare_directory "${SHAPES_RELEASE_DIR}/shacl/latest"

# Validate Turtle files for syntax errors
echo "Validating Turtle files for syntax errors"
$VALIDATE_CMD $FILES

# Merge ontology files
echo "Merging Ontology into Release ${VERSION}"
# Merge turtle modules into merged.ttl
$MERGE_CMD "${VERSION_DIR}/merged.ttl" $FILES

# Step 2: Build index ontology
echo "Building index ontology (mode=${MODE})"
if [ "$MODE" = oplax ]; then
  python3 scripts/build_index.py \
    --metadata modules/core/metadata.ttl \
    --modules modules \
    --patterns patterns \
    --out "${VERSION_DIR}/index.ttl"
else
  python3 scripts/build_index.py \
    --metadata modules/core/metadata.ttl \
    --modules modules \
    --out "${VERSION_DIR}/index.ttl"
fi

# If in OPLaX mode and using pyLODE, build a supermodel profile
if [ "$MODE" = oplax ] && [ "$DOCS" = pylode ]; then
  echo "Building pyLODE supermodel profile"
  python3 scripts/build_profile.py \
    --metadata modules/core/metadata.ttl \
    --modules-txt tests/modules.txt \
    --out "${VERSION_DIR}/index-profile.ttl"
fi

# Run SHACL validation
echo "Running SHACL validation"
# ./tests/shacl/shacl-test.sh

# Run SPARQL Competency Questions validation
# echo "Running SPARQL CQ validation"
# ./tests/sparql/sparql-test.sh
# Generate documentation
# Generate documentation
if [ "$DOCS" = widoco ]; then
  echo "Generating Ontology Documentation via Widoco"
  $WIDOCO_DOCKER_CMD -ontFile in/merged.ttl -outFolder out -rewriteAll -webVowl
elif [ "$DOCS" = pylode ]; then
  if [ "$MODE" = oplax ]; then
    echo "Generating supermodel documentation via pyLODE"
    pylode -p supermodel \
      -o "${VERSION_DIR}/index-supermodel.html" \
      "${VERSION_DIR}/index-profile.ttl" \
      "${VERSION_DIR}/index.ttl" \
      $MODULE_TTLS
  else
    echo "Generating Ontology Documentation via pyLODE"
    pylode "${VERSION_DIR}/index.ttl" -o "${VERSION_DIR}/index-en.html" -c false
    pylode "${VERSION_DIR}/merged.ttl" -o "${VERSION_DIR}/ontology-en.html" -c false
  fi
else
  echo "Unknown docs generator: ${DOCS}"; exit 1
fi

# Process JSON-LD contexts
echo "Processing JSON-LD contexts for release ${VERSION}"
# Copy all context files 
cp ${CONTEXTS_DIR}/*.jsonld "${CONTEXTS_RELEASE_DIR}/${VERSION}/"
# Also update the "latest" directory
cp ${CONTEXTS_DIR}/*.jsonld "${CONTEXTS_RELEASE_DIR}/latest/"

# Process SHACL shapes 
echo "Processing SHACL shapes for release ${VERSION}"
# Copy SHACL shape files
cp ${SHAPES_DIR}/*.jsonld "${SHAPES_RELEASE_DIR}/shacl/${VERSION}/"
# We no longer copy TTL files as they're replaced by JSON-LD
# cp ${SHAPES_DIR}/*.ttl "${SHAPES_RELEASE_DIR}/shacl/${VERSION}/"
# Copy to latest directory
cp ${SHAPES_DIR}/*.jsonld "${SHAPES_RELEASE_DIR}/shacl/latest/"
# cp ${SHAPES_DIR}/*.ttl "${SHAPES_RELEASE_DIR}/shacl/latest/"

# Update version information in context files
# This updates version references in the base context file
echo "Updating version information in context files"
sed -i.bak "s/\"version\": \"[0-9]\.[0-9]\.[0-9]\"/\"version\": \"${VERSION}\"/g" "${CONTEXTS_RELEASE_DIR}/${VERSION}/context-base.jsonld" && rm "${CONTEXTS_RELEASE_DIR}/${VERSION}/context-base.jsonld.bak"

# Copy to latest directory for ontology
echo "Updating latest directory"
cp -r "${VERSION_DIR}/." "${LATEST_DIR}"
