# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains the Defense Supply Chain and Documentation Ontology (DSCDO), designed to standardize supply chain documentation in defense operations using Knowledge Graphs, ontologies, and AI technologies. The ontology is transitioning to adopt the CogitareLink four-layer model for improved LLM agent integration.

## Common Commands

### Installation
```bash
# Install Python dependencies using uv
pip install uv
uv install
```

### Build Release Artifacts
```bash
# Generate release artifacts (ontology, documentation, contexts, shapes)
uv run bash build-release.sh
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

The ontology is being redesigned around the CogitareLink four-layer model:

1. **Layer 0 (Context)**: Small (< 5KB) JSON-LD context files in `/contexts/` defining term mappings
2. **Layer 1 (Ontology)**: Modular ontology files in `/modules/` with classes and properties
3. **Layer 2 (Shapes)**: SHACL validation shapes in `/shapes/` 
4. **Layer 3 (Data)**: Instance data in JSON-LD format, typically in test examples

### Key Design Decisions (ADRs)

- **Separate Index vs. Merged Ontologies**: `/release/ontology/<version>/` contains both index.ttl (imports modules) and merged.ttl (materialized graph)
- **SHACL/SPARQL Rules Over OWL-RL**: Moving from embedded OWL-RL reasoning to explicit SHACL/SPARQL rules in RL_rules.shapes.ttl
- **JSON-LD 1.1 as Primary Serialization**: For contexts, instance data, and where possible ontologies and shapes
- **OPLaX Pattern Metadata**: Exposing ontology design patterns for LLM discovery
- **Standard Vocabularies**: Using schema.org, Prov-O, OWL-Time, and GeoSPARQL as foundational vocabularies

### Release Pipeline

The build-release-enhanced.sh script:
1. Validates Turtle syntax
2. Processes templates with environment variable substitution
3. Merges modules into a single ontology
4. Generates documentation using pyLODE
5. Copies JSON-LD contexts and SHACL shapes to versioned directories
6. Updates the "latest" directories

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

## Development Guidelines

When modifying the ontology:
1. Keep JSON-LD contexts small (< 5KB) for Layer 0
2. Use SHACL shapes rather than OWL for closed-world constraints
3. Follow the pattern-based approach with OPLaX metadata
4. Include appropriate SKOS annotations for LLM discovery
5. Update version in modules/core/metadata.ttl when making significant changes