# DSCDO CogitareLink Bundle

This directory contains the Defense Supply Chain and Documentation Ontology (DSCDO) packaged according to the CogitareLink four-layer model with OPLaX pattern annotations.

## Structure

The bundle follows CogitareLink's four-layer structure:

1. **Layer 0 (Context)**: `context.jsonld` - A minimal JSON-LD context defining key prefixes.
2. **Layer 1 (Ontology)**: 
   - `ontology.ttl` - The index ontology with OPLaX annotations
   - `modules.jsonld` - A JSON-LD index of all available modules
3. **Layer 2 (Shapes & Rules)**:
   - `shapes.ttl` - Combined SHACL shapes for validation
   - `rules.ttl` - OWL-RL rules expressed as SHACL rules
4. **Layer 3 (Data)**: `instances/*.jsonld` - Example data instances

## OPLaX Annotations

The ontology uses OPLaX (Ontology Pattern Language eXtended) to describe:

- **Modules**: Logical partitions of the ontology (`oplax:Module`)
- **Patterns**: Design patterns that solve specific modeling problems (`oplax:Pattern`)
- **Competency Questions**: Natural language questions that the ontology can answer (`oplax:hasCompetencyQuestion`)
- **Intents**: Purposes of each module or pattern (`oplax:hasIntent`)

## Usage with CogitareLink

CogitareLink agents should:

1. Load the Layer 0 context first
2. Explore the index ontology to discover modules and patterns 
3. Selectively load only the modules needed for a task
4. Use SHACL shapes to validate instance data

Example of finding relevant modules:

```sparql
# SPARQL to find modules with competency questions about documents
SELECT ?module ?question WHERE {
  ?module a oplax:Module ;
          oplax:hasCompetencyQuestion ?question .
  FILTER(CONTAINS(LCASE(?question), "document"))
}
```

## Version

This bundle corresponds to DSCDO version 0.1.4.
