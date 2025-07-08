# ADR 84: URI Structure for Oxigraph Graph Database Service

Discussion: https://github.com/crcresearch/earth616_ontology/issues/31

## Status
_Proposed_

## Decision
Establish a flexible, dereferenceable URI structure for entities and named graphs in the Oxigraph graph database service that supports API-based dereferencing and extensible partitioning strategies.

## Context

### Current Architecture
The earth616 infrastructure includes an Oxigraph SPARQL 1.1 database service accessed through a Document Graph Store (DGS) API. The extraction workflow needs to mint URIs for entities and named graphs that follow linked data principles while supporting future partitioning requirements.

### Dereferenceability Requirements
URIs must be dereferenceable through HTTP GET requests, with the DGS service acting as a dereferencing API that wraps SPARQL queries. This enables agents to "follow their nose" by discovering resource types and relationships through standard HTTP content negotiation.

### Partitioning Evolution
- **Phase 1**: Single named graph for initial testing and development
- **Future phases**: Multiple named graphs partitioned by manufacturer, data sensitivity, or workflow-specific requirements
- **Cross-graph entities**: Parts, components, and organizations may span multiple graphs and require consistent identification

### Linked Data Principles
- **Opaque URIs**: No semantic information encoded in URI structure to maximize flexibility
- **Content negotiation**: Support TTL, JSON-LD, and HTML responses based on Accept headers
- **Discoverable catalogs**: DCAT-compliant graph discovery mechanisms
- **Canonical identification**: Consistent entity identification across graph boundaries

## Decision Details

### Base URI Structure
```
https://oxigraph.blocks.simbachain.com/entity/{identifier}     # Entities
https://oxigraph.blocks.simbachain.com/graphs/{graph-id}      # Named graphs
https://oxigraph.blocks.simbachain.com/graphs                 # Graph catalog
```

### Entity URI Pattern
- **Format**: `https://oxigraph.blocks.simbachain.com/entity/{identifier}`
- **Identifier**: Opaque identifier (UUID, hash, or other format as requirements evolve)
- **Examples**:
  ```
  https://oxigraph.blocks.simbachain.com/entity/c4b0d1e2-f3a4-4b5c-8d6e-7f8g9h0i1j2k
  https://oxigraph.blocks.simbachain.com/entity/sha256-abc123def456...
  ```

### Named Graph URI Pattern
- **Format**: `https://oxigraph.blocks.simbachain.com/graphs/{graph-id}`
- **Graph ID**: Extensible identifier supporting various partitioning schemes
- **Examples**:
  ```
  https://oxigraph.blocks.simbachain.com/graphs/main                    # Initial single graph
  https://oxigraph.blocks.simbachain.com/graphs/manufacturer-boeing     # Future manufacturer partitioning
  https://oxigraph.blocks.simbachain.com/graphs/classification-cui      # Future sensitivity partitioning
  ```

### API Dereferencing Implementation

#### Entity Dereferencing
```http
GET https://oxigraph.blocks.simbachain.com/entity/c4b0d1e2-f3a4-4b5c-8d6e-7f8g9h0i1j2k
Accept: text/turtle

# DGS wraps SPARQL query:
# CONSTRUCT { <https://oxigraph.blocks.simbachain.com/entity/c4b0d1e2-f3a4-4b5c-8d6e-7f8g9h0i1j2k> ?p ?o }
# WHERE { GRAPH ?g { <https://oxigraph.blocks.simbachain.com/entity/c4b0d1e2-f3a4-4b5c-8d6e-7f8g9h0i1j2k> ?p ?o } }
```

#### Named Graph Dereferencing
```http
GET https://oxigraph.blocks.simbachain.com/graphs/main
Accept: application/ld+json

# DGS returns VoID dataset description plus optional statistics
```

#### Graph Catalog
```http
GET https://oxigraph.blocks.simbachain.com/graphs
Accept: text/turtle

# Returns DCAT catalog of available named graphs
```

### Content Negotiation
- **text/turtle**: Primary format for tooling and SPARQL compatibility
- **application/ld+json**: Primary format for agent consumption and CogitareLink integration
- **text/html**: Human-readable documentation and exploration
- **Default**: text/turtle when Accept header is missing or ambiguous

### DCAT Catalog Structure
```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix void: <http://rdfs.org/ns/void#> .

<https://oxigraph.blocks.simbachain.com/graphs>
    a dcat:Catalog ;
    dcterms:title "Supply Chain Document Graph Catalog" ;
    dcterms:description "A catalog of all ingested supply chain document sets" ;
    dcat:dataset
        <https://oxigraph.blocks.simbachain.com/graphs/main> .

<https://oxigraph.blocks.simbachain.com/graphs/main>
    a dcat:Dataset, void:Dataset ;
    dcterms:title "Main Document Graph" ;
    dcterms:issued "2025-07-08"^^xsd:date ;
    void:triples 15420 ;
    void:entities 1543 .
```

### Integration with Vocabulary Service
- **Schema URIs**: Continue using vocabulary service (`https://vocab.earth616.localhost/nd/scdoc/ont/`)
- **Instance URIs**: Use oxigraph service (`https://oxigraph.blocks.simbachain.com/entity/`)
- **Clear separation**: Vocabulary service serves ontology/schema, DGS serves instance data
- **Cross-service linking**: Standard RDF properties link schema to instances

## Implementation Requirements

### DGS Service Extensions
1. **Entity endpoint**: `/entity/{identifier}` route with SPARQL-wrapped dereferencing
2. **Graph endpoint**: `/graphs/{graph-id}` route returning VoID descriptions
3. **Catalog endpoint**: `/graphs` route returning DCAT catalog
4. **Content negotiation**: Accept header processing for TTL/JSON-LD/HTML
5. **CORS support**: Enable cross-origin requests for web-based agents

### Extraction Workflow Integration
1. **URI minting**: Generate opaque identifiers for new entities
2. **Named graph selection**: Target appropriate graph based on partitioning rules
3. **Cross-graph linking**: Use consistent URIs for entities that span graphs
4. **Provenance recording**: Link extraction metadata to minted URIs

## Consequences

### Positive
- **Flexible evolution**: URI structure supports unknown future partitioning requirements
- **Linked data compliance**: Standard dereferencing and content negotiation patterns
- **Agent-friendly**: Opaque URIs force proper dereferencing behavior
- **API integration**: Clean separation between SPARQL backend and HTTP frontend
- **Ontology alignment**: Works seamlessly with existing vocabulary service architecture

### Negative
- **Initial complexity**: Requires DGS service extensions for dereferencing
- **URI opacity**: Debugging may require dereferencing to understand resource types
- **Service coordination**: Multiple services (vocabulary, DGS) must coordinate for complete linked data experience

### Risks
- **Service dependencies**: Entity dereferencing depends on DGS service availability
- **Performance**: CONSTRUCT queries for dereferencing may impact performance at scale
- **Caching strategy**: May need caching layer for frequently accessed entities

## Future Considerations
- **Graph partitioning schemes**: URI structure accommodates manufacturer, sensitivity, or workflow-based partitioning
- **Federation**: Structure supports potential future federation across multiple Oxigraph instances
- **Versioning**: Opaque identifiers allow for versioning strategies without URI changes
- **Cross-graph queries**: SPARQL federation patterns for queries spanning multiple graphs