# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains the Defense Supply Chain and Documentation Ontology (DSCDO), designed to standardize supply chain documentation in defense operations using Knowledge Graphs, ontologies, and AI technologies. The ontology is transitioning to adopt the CogitareLink four-layer model for improved LLM agent integration.

### GitHub Integration Breadcrumb

**Repository**: `crcresearch/earth616_ontology`  
**GitHub URL**: https://github.com/crcresearch/earth616_ontology  
**Issues URL**: https://github.com/crcresearch/earth616_ontology/issues  
**API URL**: https://api.github.com/repos/crcresearch/earth616_ontology  

This ontology follows **GitHub Issue-Driven Development** (ADR 06). Every ontology term is linked to a GitHub issue via `schema:source` property for full traceability and discussion provenance.

## Common Commands

### Installation
```bash
# Install Python dependencies using uv
pip install uv
uv install
```

### Build Release Artifacts
```bash
# Generate release artifacts using the enhanced template-based build
./build-release-enhanced.sh --env=local --layers=all

# For production release
./build-release-enhanced.sh --env=production --layers=all

# Build specific layers only
./build-release-enhanced.sh --env=local --layers=context,ontology,shapes
```

### Run Tests
```bash
# Run all tests
uv run pytest

# Run SHACL validation tests
./tests/shacl-test.sh

# Run SPARQL validation tests
./tests/sparql-test.sh

# Validate Turtle files syntax
python scripts/validate_turtle.py [file_paths]
```

## Architecture

### CogitareLink Four-Layer Model

The ontology follows the CogitareLink four-layer model with template-based development:

1. **Layer 0 (Context)**: Small (< 5KB) JSON-LD context files
   - **Templates**: `/templates/contexts/` (source templates with URI variables)
   - **Generated**: `/release/contexts/{version}/` (final context files)

2. **Layer 1 (Ontology)**: Modular ontology files with classes and properties
   - **Templates**: `/templates/modules/` (source templates with URI variables)
   - **Generated**: `/release/ontology/{version}/` (final ontology modules)

3. **Layer 2 (Shapes)**: SHACL validation shapes and rules
   - **Templates**: `/templates/shapes/` (source templates)  
   - **Generated**: `/release/shapes/{version}/` (final SHACL shapes)

4. **Layer 3 (Data)**: Instance data in JSON-LD format
   - **Location**: `/data/` (static data files and examples)

### Key Design Decisions (ADRs)

- **Separate Index vs. Merged Ontologies**: `/release/ontology/<version>/` contains both index.ttl (imports modules) and merged.ttl (materialized graph)
- **SHACL/SPARQL Rules Over OWL-RL**: Moving from embedded OWL-RL reasoning to explicit SHACL/SPARQL rules in RL_rules.shapes.ttl
- **JSON-LD 1.1 as Primary Serialization**: For contexts, instance data, and where possible ontologies and shapes
- **OPLaX Pattern Metadata**: Exposing ontology design patterns for LLM discovery
- **Standard Vocabularies**: Using schema.org, Prov-O, OWL-Time, and GeoSPARQL as foundational vocabularies

### Template-Based Development Workflow

**Development Process**:
1. **Edit Templates**: Modify files in `/templates/modules/`, `/templates/contexts/`, `/templates/shapes/`
2. **Configure Environment**: Set URI bases in `/config/environments/{env}.yml`
3. **Build Release**: Run `./build-release-enhanced.sh --env={env} --layers=all`
4. **Test**: Use generated files in `/release/{layer}/{version}/`

**Enhanced Build Pipeline**:
The `build-release-enhanced.sh` script processes the complete CogitareLink layer model:
1. **Environment Configuration**: Loads URI bases from config files
2. **Template Processing**: Processes templates with environment variable substitution
3. **Layer 0**: Generates JSON-LD contexts with proper URI references
4. **Layer 1**: Generates ontology modules and creates merged.ttl
5. **Layer 2**: Processes SHACL shapes and validation rules
6. **Layer 3**: Handles import cache and external ontology references
7. **Documentation**: Generates pyLODE documentation
8. **Versioning**: Updates both versioned and "latest" directories

#### pyLODE Documentation Generation

**Issue**: pyLODE duplicates metadata when a resource has multiple RDF types (owl:Ontology + prof:Profile).

**Root Cause**: pyLODE's `_make_metadata()` function in `profiles/vocpub.py` iterates through subjects with different types separately, causing the same subject to be processed multiple times and duplicating all metadata properties.

**Solution**: Follow W3C Profile semantics by separating the ontology and profile into different URIs:
- Ontology URI (`/ont/`) carries all metadata (creator, publisher, license, etc.)
- Profile URI (`/ont/profile/`) describes modular structure via `prof:hasResource`
- Profile references ontology via `prof:isProfileOf`

This follows the W3C PROF pattern where profiles describe how to implement specifications, rather than being the specification itself.

### URI Structure

The ontology uses a persistent URI structure:
```
https://schema-earth616-ks18.blocks.simbachain.com/nd/scdoc/ont/          # Ontology root
https://schema-earth616-ks18.blocks.simbachain.com/nd/scdoc/shapes/       # SHACL shapes
https://schema-earth616-ks18.blocks.simbachain.com/nd/scdoc/context/      # JSON-LD contexts
```

## GitHub Issue Creation Workflow

When Claude Code identifies ontology gaps or issues via MCP, use the existing GitHub issue templates:

### Available Issue Templates
- `module_proposal_template.md` - For missing ontology modules or major concept gaps
- `change_request_template.md` - For modifications to existing terms or patterns
- `shacl_shape_proposal_template.md` - For validation rule additions or changes  
- `pattern_proposal_template.md` - For new ontology design patterns
- `adr_template.md` - For architectural decisions requiring documentation

### Automated Issue Creation
```bash
# Create ontology gap issue using gh CLI
gh issue create --repo crcresearch/earth616_ontology \
  --template module_proposal_template.md \
  --title "Missing ontology module: [CONCEPT_NAME]" \
  --body "Detected via MCP vocabulary service - [CONTEXT_DETAILS]"

# Create term addition issue
gh issue create --repo crcresearch/earth616_ontology \
  --template change_request_template.md \
  --title "Add missing term: [TERM_NAME]" \
  --body "Required for: [USE_CASE] - Detected via Claude Code MCP"
```

### Issue-Driven Development Process
1. **Detection**: Claude Code + MCP identifies vocabulary gap
2. **Issue Creation**: Automatic GitHub issue using appropriate template
3. **Discussion**: Community discussion in GitHub issue
4. **Implementation**: Ontology changes with `schema:source` pointing to issue
5. **ADR Documentation**: Architectural decisions recorded in `/decisions/`

## Development Guidelines

### Template-Based Development (v0.1.4+)

**IMPORTANT**: As of version 0.1.4, development uses templates instead of direct module editing:

- **❌ OLD**: Edit files in `/modules/` (deprecated, moved to `/modules-deprecated/`)
- **✅ NEW**: Edit templates in `/templates/modules/` and build with `./build-release-enhanced.sh`

**Development Workflow**:
1. **Templates First**: Always edit `.template` files in `/templates/` directories
2. **Environment Configuration**: Use `/config/environments/{env}.yml` for URI configuration
3. **Build Before Testing**: Run `./build-release-enhanced.sh --env=local` to generate testable files
4. **Test Generated Files**: Test files in `/release/{layer}/latest/` not templates directly

### Content Guidelines

When modifying the ontology:
1. Keep JSON-LD contexts small (< 5KB) for Layer 0
2. Use SHACL shapes rather than OWL for closed-world constraints  
3. Follow the pattern-based approach with OPLaX metadata
4. Include appropriate SKOS annotations for LLM discovery
5. **Create GitHub issue first** before major changes (follow ADR 06)
6. **Link ontology terms to issues** using `schema:source` property
7. Update version in `/templates/modules/core/ontology.ttl.template` when making significant changes

### Migration from Legacy Modules

If you find references to old `/modules/` directory:
1. Check `/modules-deprecated/` for legacy files
2. Look for equivalent templates in `/templates/modules/`
3. Create new templates if needed, following existing patterns
4. Update any scripts to use `/release/ontology/latest/` for testing