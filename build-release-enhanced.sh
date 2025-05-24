#!/usr/bin/env bash
set -e

# Enhanced build script with template support for URI resolution
# Usage:
#   build-release-enhanced.sh [--env=local|production] [--mode=standard|oplax] [--docs=widoco|pylode] [--layers=all|context,ontology,shapes,rules]

# Parse options
ENV=production
MODE=standard
DOCS=pylode
LAYERS=all

for arg in "$@"; do
  case "$arg" in
    --env=*)        ENV="${arg#*=}" ;;
    --mode=*)       MODE="${arg#*=}" ;; 
    --docs=*)       DOCS="${arg#*=}" ;; 
    --layers=*)     LAYERS="${arg#*=}" ;;
    *) echo "Unknown option: $arg"; exit 1 ;; 
  esac
done

echo "Building with environment: $ENV, mode: $MODE, docs: $DOCS, layers: $LAYERS"

# Load environment configuration
ENV_CONFIG="config/environments/${ENV}.yml"
if [ ! -f "$ENV_CONFIG" ]; then
    echo "Environment config not found: $ENV_CONFIG"
    exit 1
fi

# Extract environment variables from YAML (simple parsing)
export CONTEXT_BASE=$(grep "CONTEXT_BASE:" "$ENV_CONFIG" | cut -d'"' -f2)
export ONTOLOGY_BASE=$(grep "ONTOLOGY_BASE:" "$ENV_CONFIG" | cut -d'"' -f2)
export SHAPES_BASE=$(grep "SHAPES_BASE:" "$ENV_CONFIG" | cut -d'"' -f2)
export RULES_BASE=$(grep "RULES_BASE:" "$ENV_CONFIG" | cut -d'"' -f2)
export DATA_BASE=$(grep "DATA_BASE:" "$ENV_CONFIG" | cut -d'"' -f2)

echo "Using URI bases:"
echo "  Context: $CONTEXT_BASE"
echo "  Ontology: $ONTOLOGY_BASE"
echo "  Shapes: $SHAPES_BASE"
echo "  Rules: $RULES_BASE"

# Directory paths
SCRIPTS_DIR="./scripts"
RELEASE_DIR="./release"
VERSION=$(grep -i versionInfo modules/core/metadata.ttl | sed 's/[^"]*"\([^"]*\).*/\1/' || echo "0.1.4")

# Template directories
TEMPLATES_DIR="./templates"

# Ensure release directories exist
prepare_directory() {
    local dir=$1
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
    mkdir -p "$dir"
}

# Check if riot (Apache Jena) is available for format conversion
check_riot() {
    if ! command -v riot &> /dev/null; then
        echo "Warning: Apache Jena 'riot' command not found. Will skip JSON-LD generation."
        echo "Install with: brew install jena (macOS) or apt-get install jena (Ubuntu)"
        return 1
    fi
    return 0
}

RIOT_AVAILABLE=$(check_riot && echo "true" || echo "false")

# Process Layer 0: Contexts (JSON-LD only)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"context"* ]]; then
    echo "=== Building Layer 0: Contexts ==="
    
    prepare_directory "${RELEASE_DIR}/contexts/${VERSION}"
    prepare_directory "${RELEASE_DIR}/contexts/latest"
    
    if [ -d "${TEMPLATES_DIR}/contexts" ]; then
        for template in ${TEMPLATES_DIR}/contexts/*.jsonld.template; do
            if [ -f "$template" ]; then
                filename=$(basename "$template" .template)
                echo "Processing context template: $template -> $filename"
                
                # Process template with environment variables
                envsubst < "$template" > "${RELEASE_DIR}/contexts/${VERSION}/${filename}"
                envsubst < "$template" > "${RELEASE_DIR}/contexts/latest/${filename}"
            fi
        done
    else
        echo "Warning: No context templates found in ${TEMPLATES_DIR}/contexts"
    fi
fi

# Process Layer 1: Ontology (Turtle + JSON-LD)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"ontology"* ]]; then
    echo "=== Building Layer 1: Ontology ==="
    
    prepare_directory "${RELEASE_DIR}/ontology/${VERSION}"
    prepare_directory "${RELEASE_DIR}/ontology/latest"
    
    if [ -d "${TEMPLATES_DIR}/modules" ]; then
        # Process individual module templates
        find ${TEMPLATES_DIR}/modules -name "*.ttl.template" | while read template; do
            # Get relative path structure
            rel_path=$(echo "$template" | sed "s|${TEMPLATES_DIR}/modules/||" | sed 's|\.template$||')
            base_name=$(basename "$rel_path" .ttl)
            
            echo "Processing ontology template: $template -> $rel_path"
            
            # Create directory structure
            mkdir -p "${RELEASE_DIR}/ontology/${VERSION}/$(dirname "$rel_path")" 2>/dev/null || true
            mkdir -p "${RELEASE_DIR}/ontology/latest/$(dirname "$rel_path")" 2>/dev/null || true
            
            # Generate Turtle files
            envsubst < "$template" > "${RELEASE_DIR}/ontology/${VERSION}/${rel_path}"
            envsubst < "$template" > "${RELEASE_DIR}/ontology/latest/${rel_path}"
            
            # Generate JSON-LD if riot is available
            if [ "$RIOT_AVAILABLE" = "true" ]; then
                jsonld_path=$(echo "$rel_path" | sed 's|\.ttl$|.jsonld|')
                echo "  Converting to JSON-LD: $jsonld_path"
                
                riot --output=jsonld "${RELEASE_DIR}/ontology/${VERSION}/${rel_path}" > "${RELEASE_DIR}/ontology/${VERSION}/${jsonld_path}" 2>/dev/null || echo "    Warning: JSON-LD conversion failed for $rel_path"
                riot --output=jsonld "${RELEASE_DIR}/ontology/latest/${rel_path}" > "${RELEASE_DIR}/ontology/latest/${jsonld_path}" 2>/dev/null || true
            fi
        done
        
        # Merge ontology files (if merge script exists)
        if [ -f "${SCRIPTS_DIR}/merge_ontology.py" ]; then
            echo "Merging ontology modules"
            FILES=$(find "${RELEASE_DIR}/ontology/${VERSION}" -name "*.ttl" | tr '\n' ' ')
            if [ ! -z "$FILES" ]; then
                python3 "${SCRIPTS_DIR}/merge_ontology.py" "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" $FILES || echo "Warning: Merge failed"
                cp "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" "${RELEASE_DIR}/ontology/latest/merged.ttl" 2>/dev/null || true
            fi
        fi
    else
        echo "Warning: No ontology templates found in ${TEMPLATES_DIR}/modules"
    fi
fi

# Process Layer 2a: SHACL Shapes (Turtle + JSON-LD)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"shapes"* ]]; then
    echo "=== Building Layer 2a: SHACL Shapes ==="
    
    prepare_directory "${RELEASE_DIR}/shapes/shacl/${VERSION}"
    prepare_directory "${RELEASE_DIR}/shapes/shacl/latest"
    
    if [ -d "${TEMPLATES_DIR}/shapes" ]; then
        for template in ${TEMPLATES_DIR}/shapes/*.ttl.template; do
            if [ -f "$template" ]; then
                base_name=$(basename "$template" .ttl.template)
                echo "Processing shape template: $template -> $base_name"
                
                # Generate Turtle files
                envsubst < "$template" > "${RELEASE_DIR}/shapes/shacl/${VERSION}/${base_name}.ttl"
                envsubst < "$template" > "${RELEASE_DIR}/shapes/shacl/latest/${base_name}.ttl"
                
                # Generate JSON-LD if riot is available
                if [ "$RIOT_AVAILABLE" = "true" ]; then
                    echo "  Converting to JSON-LD: ${base_name}.jsonld"
                    riot --output=jsonld "${RELEASE_DIR}/shapes/shacl/${VERSION}/${base_name}.ttl" > "${RELEASE_DIR}/shapes/shacl/${VERSION}/${base_name}.jsonld" 2>/dev/null || echo "    Warning: JSON-LD conversion failed for ${base_name}.ttl"
                    riot --output=jsonld "${RELEASE_DIR}/shapes/shacl/latest/${base_name}.ttl" > "${RELEASE_DIR}/shapes/shacl/latest/${base_name}.jsonld" 2>/dev/null || true
                fi
            fi
        done
    else
        echo "Warning: No shape templates found in ${TEMPLATES_DIR}/shapes"
    fi
fi

# Process Layer 2b: SPARQL Rules (Turtle + JSON-LD)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"rules"* ]]; then
    echo "=== Building Layer 2b: SPARQL Rules ==="
    
    prepare_directory "${RELEASE_DIR}/rules/${VERSION}"
    prepare_directory "${RELEASE_DIR}/rules/latest"
    
    if [ -d "${TEMPLATES_DIR}/rules" ]; then
        for template in ${TEMPLATES_DIR}/rules/*.ttl.template; do
            if [ -f "$template" ]; then
                base_name=$(basename "$template" .ttl.template)
                echo "Processing rule template: $template -> $base_name"
                
                # Generate Turtle files
                envsubst < "$template" > "${RELEASE_DIR}/rules/${VERSION}/${base_name}.ttl"
                envsubst < "$template" > "${RELEASE_DIR}/rules/latest/${base_name}.ttl"
                
                # Generate JSON-LD if riot is available
                if [ "$RIOT_AVAILABLE" = "true" ]; then
                    echo "  Converting to JSON-LD: ${base_name}.jsonld"
                    riot --output=jsonld "${RELEASE_DIR}/rules/${VERSION}/${base_name}.ttl" > "${RELEASE_DIR}/rules/${VERSION}/${base_name}.jsonld" 2>/dev/null || echo "    Warning: JSON-LD conversion failed for ${base_name}.ttl"
                    riot --output=jsonld "${RELEASE_DIR}/rules/latest/${base_name}.ttl" > "${RELEASE_DIR}/rules/latest/${base_name}.jsonld" 2>/dev/null || true
                fi
            fi
        done
    else
        echo "Warning: No rule templates found in ${TEMPLATES_DIR}/rules"
    fi
fi

# Generate documentation (if ontology layer was built)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"ontology"* ]] && [ "$DOCS" = "pylode" ]; then
    echo "=== Generating Documentation ==="
    
    # Check if pylode is available
    if command -v pylode &> /dev/null; then
        # Generate documentation for merged ontology if it exists
        if [ -f "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" ]; then
            echo "Generating documentation via pyLODE"
            pylode "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" -o "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" -c false || echo "Warning: pyLODE documentation generation failed"
            cp "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" "${RELEASE_DIR}/ontology/latest/ontology-en.html" 2>/dev/null || true
        fi
        
        # Generate index documentation if index exists
        if [ -f "${RELEASE_DIR}/ontology/${VERSION}/index.ttl" ]; then
            pylode "${RELEASE_DIR}/ontology/${VERSION}/index.ttl" -o "${RELEASE_DIR}/ontology/${VERSION}/index-en.html" -c false || echo "Warning: Index documentation generation failed"
            cp "${RELEASE_DIR}/ontology/${VERSION}/index-en.html" "${RELEASE_DIR}/ontology/latest/index-en.html" 2>/dev/null || true
        fi
    else
        echo "Warning: pylode not found. Skipping documentation generation."
        echo "Install with: pip install pylode"
    fi
fi

echo "=== Build Complete ==="
echo "Environment: $ENV"
echo "Version: $VERSION"
echo "Layers processed: $LAYERS"
echo "Files generated in: ${RELEASE_DIR}/"

# If a Python virtualenv exists, activate it so python3 and rdflib are available
if [ -f ".venv/bin/activate" ]; then
    # shellcheck source=/dev/null
    . ".venv/bin/activate"
fi