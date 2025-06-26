# Defense Supply Chain and Documentation Ontology (DSCDO) - JSON-LD Contexts Directory

Welcome to the JSON-LD Contexts Directory for the Defense Supply Chain and Documentation Ontology (DSCDO). This directory contains the context files that enable semantic interoperability for supply chain documentation and events, specifically designed to support LLM-based agentic systems that navigate linked data.

## Our Modular Context Approach

DSCDO uses a modular approach to JSON-LD contexts that follows these principles:

1. **Base + Type-Specific Structure**: We separate contexts into a common base and specialized type-specific contexts.
2. **Explicit Validation Links**: Each type-specific context links directly to its corresponding SHACL validation shape.
3. **Rich Semantic Annotations**: Contexts include natural language descriptions to support LLM understanding.
4. **"Follow Your Nose" Pattern**: Contexts are designed to let agents discover validation rules and related resources.

## Directory Structure

The JSON-LD Contexts Directory is organized as follows:

```
/contexts
    - context-base.jsonld (Common prefixes and shared terms)
    - context-document.jsonld (SCDigitalDocument and related types)
    - context-event.jsonld (TransferEvent, TransformationEvent, etc.)
    - context-identifier.jsonld (Identifier patterns and vocabulary)
    /examples
        - document-instance.jsonld (Example document using the contexts)
        - event-instance.jsonld (Example event using the contexts)
```

## Context Files Explained

### Base Context: `context-base.jsonld`

This foundational context defines namespace prefixes and cross-cutting terms:

```json
{
  "@context": {
    "@version": 1.1,
    "dscdo": "https://schema-earth616-ks18.blocks.simbachain.com/nd/scdoc/ont/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "epcis": "https://ref.gs1.org/epcis/",
    "sh": "http://www.w3.org/ns/shacl#",
    
    "id": "@id",
    "type": "@type"
  }
}
```

### Type-Specific Contexts

Each type has its own context file that imports the base context and adds specialized terms:

**Document Context: `context-document.jsonld`**

```json
{
  "@context": [
    "https://example.org/contexts/dscdo/context-base.jsonld",
    {
      "documentType": {"@id": "dscdo:hasdocumenttype", "@type": "@id"},
      "documentContent": {"@id": "dscdo:hasdocumentcontent", "@type": "@id"},
      "contentText": "dscdo:processedtext",
      "SCDigitalDocument": "dscdo:Scdigitaldocument",
      "workflowExecution": {"@id": "dscdo:workflowExecution", "@type": "@id"}
    }
  ],
  "@graph": [
    {
      "@id": "dscdo:Scdigitaldocument",
      "skos:definition": "Represents digital document that is supply chain documentation",
      "sh:shapesGraph": "https://example.org/shapes/DocumentShape-v1.jsonld"
    }
  ]
}
```

**Event Context: `context-event.jsonld`**

```json
{
  "@context": [
    "https://example.org/contexts/dscdo/context-base.jsonld",
    {
      "eventTime": {"@id": "prov:startedAtTime", "@type": "xsd:dateTime"},
      "location": {"@id": "dscdo:hasSTETE", "@type": "@id"},
      "sourceAgent": {"@id": "dscdo:assumesRole", "@type": "@id"},
      "targetAgent": {"@id": "dscdo:assumesRole", "@type": "@id"},
      "TransferEvent": "dscdo:TransferEvent",
      "TransformationEvent": "dscdo:TransformationEvent"
    }
  ],
  "@graph": [
    {
      "@id": "dscdo:TransferEvent",
      "skos:definition": "An event involving the transfer of goods or materials.",
      "sh:shapesGraph": "https://example.org/shapes/TransferEventShape-v1.jsonld"
    }
  ]
}
```

## Integration with EPCIS and Schema.org

Our contexts leverage two established vocabularies:

1. **EPCIS Integration**: We selectively incorporate relevant terms from the EPCIS standard, particularly for supply chain events, with explicit mappings to DSCDO equivalents.

2. **Schema.org Adoption**: We use Schema.org as our model for general concepts like organizations, people, and creative works, following its straightforward RDFS structure and rich annotations approach.

## Supporting Agentic Systems

These contexts are specifically designed to support LLM-based agentic systems by:

1. **Providing Rich Annotations**: Natural language definitions help LLMs understand terms.
2. **Linking to Validation Shapes**: Direct connections to SHACL shapes enable validation.
3. **Enabling Discovery**: Clear paths to related resources support the "follow your nose" pattern.
4. **Maintaining Consistency**: Predictable patterns make processing easier for agents.

## How to Use

### 1. Include the Appropriate Context

Reference the context file that matches your data type:

```json
{
  "@context": "https://example.org/contexts/dscdo/context-document.jsonld",
  "@id": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
  "@type": "SCDigitalDocument",
  "documentType": "dscdo:PurchaseOrder",
  "contentText": "This purchase order describes receipt of 100 units..."
}
```

### 2. Follow Validation Rules

Use the SHACL shapes linked from the context to validate your data:

```
GET https://example.org/shapes/DocumentShape-v1.jsonld
```

### 3. Develop Agentic Workflows

LLM agents can follow this pattern:
1. Access an instance document
2. Fetch its context
3. Find and apply the validation shape
4. Process the validated data

## Contributing

We welcome contributions to improve and expand the DSCDO contexts. Please submit pull requests or open issues on our GitHub repository for any suggestions or improvements.
