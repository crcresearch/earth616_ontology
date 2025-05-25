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
        
        # Process pattern templates
        if [ -d "${TEMPLATES_DIR}/patterns" ]; then
            echo "Processing pattern templates"
            prepare_directory "${RELEASE_DIR}/ontology/${VERSION}/patterns"
            prepare_directory "${RELEASE_DIR}/ontology/latest/patterns"
            
            find ${TEMPLATES_DIR}/patterns -name "*.ttl.template" | while read template; do
                base_name=$(basename "$template" .ttl.template)
                echo "Processing pattern template: $template -> patterns/${base_name}.ttl"
                
                # Generate Turtle files
                envsubst < "$template" > "${RELEASE_DIR}/ontology/${VERSION}/patterns/${base_name}.ttl"
                envsubst < "$template" > "${RELEASE_DIR}/ontology/latest/patterns/${base_name}.ttl"
                
                # Generate JSON-LD if riot is available
                if [ "$RIOT_AVAILABLE" = "true" ]; then
                    echo "  Converting pattern to JSON-LD: patterns/${base_name}.jsonld"
                    riot --output=jsonld "${RELEASE_DIR}/ontology/${VERSION}/patterns/${base_name}.ttl" > "${RELEASE_DIR}/ontology/${VERSION}/patterns/${base_name}.jsonld" 2>/dev/null || echo "    Warning: JSON-LD conversion failed for patterns/${base_name}.ttl"
                    riot --output=jsonld "${RELEASE_DIR}/ontology/latest/patterns/${base_name}.ttl" > "${RELEASE_DIR}/ontology/latest/patterns/${base_name}.jsonld" 2>/dev/null || true
                fi
            done
        fi
        
        # Merge ontology files (if merge script exists)
        if [ -f "${SCRIPTS_DIR}/merge_ontology.py" ]; then
            echo "Merging ontology modules"
            
            # For new template structure: include ontology base + modules, exclude profile and patterns
            if [ -f "${RELEASE_DIR}/ontology/${VERSION}/core/ontology.ttl" ]; then
                echo "Using new separated ontology/profile structure"
                # Include ontology.ttl and individual modules, but exclude profile.ttl and patterns
                FILES=$(find "${RELEASE_DIR}/ontology/${VERSION}" -name "*.ttl" \
                    -not -path "*/profile.ttl" \
                    -not -path "*/profile-new.ttl" \
                    -not -path "*/patterns/*.ttl" \
                    -not -path "*/pylode-config.ttl" | tr '\n' ' ')
            elif [ -f "${RELEASE_DIR}/ontology/${VERSION}/core/profile.ttl" ]; then
                echo "Using legacy PROF profile approach - excluding metadata.ttl"
                FILES=$(find "${RELEASE_DIR}/ontology/${VERSION}" -name "*.ttl" -not -path "*/metadata.ttl" | tr '\n' ' ')
            else
                FILES=$(find "${RELEASE_DIR}/ontology/${VERSION}" -name "*.ttl" | tr '\n' ' ')
            fi
            
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

# Generate PROF profile and pyLODE config (if ontology layer was built)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"ontology"* ]]; then
    echo "=== Generating PROF Profile and pyLODE Config ==="
    
    # Generate pyLODE config from template
    if [ -f "${TEMPLATES_DIR}/pylode-config.ttl.template" ]; then
        echo "Generating pyLODE config"
        envsubst < "${TEMPLATES_DIR}/pylode-config.ttl.template" > "${RELEASE_DIR}/ontology/${VERSION}/pylode-config.ttl"
        envsubst < "${TEMPLATES_DIR}/pylode-config.ttl.template" > "${RELEASE_DIR}/ontology/latest/pylode-config.ttl"
    fi
fi

# Generate documentation (if ontology layer was built)
if [[ "$LAYERS" == "all" || "$LAYERS" == *"ontology"* ]] && [ "$DOCS" = "pylode" ]; then
    echo "=== Generating Documentation ==="
    
    # Check if pylode is available
    if command -v pylode &> /dev/null; then
        
        # Generate supermodel documentation if PROF profile exists (OPLaX mode)
        if [ "$MODE" = "oplax" ] && [ -f "${RELEASE_DIR}/ontology/${VERSION}/core/profile.ttl" ]; then
            echo "Attempting pyLODE supermodel documentation"
            # For now, skip supermodel generation due to module URL resolution issues
            # TODO: Implement local web server or fix file:// URI handling in pylode
            echo "Supermodel generation temporarily disabled - modules need to be served via HTTP"
            echo "Generated traditional documentation instead"
        fi
        
        # Generate main ontology documentation
        if [ -f "${RELEASE_DIR}/ontology/${VERSION}/core/ontology.ttl" ]; then
            echo "Generating documentation from ontology.ttl (clean metadata)"
            pylode "${RELEASE_DIR}/ontology/${VERSION}/core/ontology.ttl" -o "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" -c false || echo "Warning: Ontology documentation generation failed"
            cp "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" "${RELEASE_DIR}/ontology/latest/ontology-en.html" 2>/dev/null || true
        elif [ -f "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" ]; then
            echo "Generating documentation from merged ontology (fallback)"
            pylode "${RELEASE_DIR}/ontology/${VERSION}/merged.ttl" -o "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" -c false || echo "Warning: pyLODE documentation generation failed"
            cp "${RELEASE_DIR}/ontology/${VERSION}/ontology-en.html" "${RELEASE_DIR}/ontology/latest/ontology-en.html" 2>/dev/null || true
        fi
        
        # Generate profile documentation
        if [ -f "${RELEASE_DIR}/ontology/${VERSION}/core/profile-new.ttl" ]; then
            echo "Generating profile documentation"
            pylode "${RELEASE_DIR}/ontology/${VERSION}/core/profile-new.ttl" -o "${RELEASE_DIR}/ontology/${VERSION}/profile-en.html" -c false || echo "Warning: Profile documentation generation failed"
            cp "${RELEASE_DIR}/ontology/${VERSION}/profile-en.html" "${RELEASE_DIR}/ontology/latest/profile-en.html" 2>/dev/null || true
        fi
        
        # Generate pattern documentation
        if [ -d "${RELEASE_DIR}/ontology/${VERSION}/patterns" ]; then
            echo "Generating pattern documentation"
            for pattern_file in "${RELEASE_DIR}/ontology/${VERSION}/patterns"/*.ttl; do
                if [ -f "$pattern_file" ]; then
                    pattern_name=$(basename "$pattern_file" .ttl)
                    echo "  Generating documentation for pattern: $pattern_name"
                    pylode "$pattern_file" -o "${RELEASE_DIR}/ontology/${VERSION}/patterns/${pattern_name}-en.html" -c false || echo "    Warning: Pattern documentation failed for $pattern_name"
                    cp "${RELEASE_DIR}/ontology/${VERSION}/patterns/${pattern_name}-en.html" "${RELEASE_DIR}/ontology/latest/patterns/${pattern_name}-en.html" 2>/dev/null || true
                fi
            done
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
echo ""
echo "URI Structure for Content Negotiation:"
echo "  Ontology: ${ONTOLOGY_BASE}/ (TTL/JSON-LD/HTML)"
echo "  Profile: ${ONTOLOGY_BASE}/profile/ (TTL/JSON-LD/HTML)"
echo "  Patterns: ${ONTOLOGY_BASE}/patterns/ (index + individual patterns)"
echo "  Modules: ${ONTOLOGY_BASE}/modules/{module}/ (TTL/JSON-LD/HTML)"

# If a Python virtualenv exists, activate it so python3 and rdflib are available
if [ -f ".venv/bin/activate" ]; then
    # shellcheck source=/dev/null
    . ".venv/bin/activate"
fi