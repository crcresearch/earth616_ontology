<!---
  Integration Plan: Docling Pydantic Models ↔ DSCDO Ontology via JSON-LD Contexts
  Location: design/docgraph/JSONLD_Pydantic_Integration.md
-->
# Integrating Docling Pydantic Models with the DSCDO Ontology

This document summarizes the design conversation for:
1. Folding the Docling Pydantic document graph (`design/docgraph`) into the
   DSCDO (Earth-616) ontology and CogitareLink’s four-layer architecture.
2. Enabling round-trip conversion between JSON-LD 1.1 and Pydantic models via a
   dedicated Layer 0 context.

## Goals
- Represent an abstract **Document** (e.g. Purchase Order #123) → concrete
  PDF/Word (`SCDigitalDocument`) → structured JSON-LD (`DoclingDocument`).
- Allow partners to supply alternate JSON-LD representations that map to
  the same Pydantic models via custom contexts.
- Round-trip JSON-LD ↔ Pydantic without code changes, driven solely by contexts.
- Align with **design/redesign.md** four-layer requirements.

## Four-Layer Architecture
1. **Layer 0 (Context)**
   - JSON-LD contexts (< 5 KB) loaded in-prompt:
     - `data/scdoc/context.jsonld` (DSCDO core prefixes)
     - `design/docgraph/docling-context.jsonld` (Pydantic field → IRI map)
2. **Layer 1 (Ontology Modules)**
   - `index.ttl` with `owl:imports` of DSCDO + `design/docgraph` module,
     declaring classes like `dd:DoclingDocument`, `dd:DocumentPage`, etc.
3. **Layer 2 (Shapes & Rules)**
   - SHACL NodeShapes + SPARQL rules under `/ont/shapes/shacl/` enforcing
     structure and deriving triples (no embedded Python).
4. **Layer 3 (Data)**
   - JSON-LD instance documents using the contexts.
   - Agents call `reason_over(shapes_turtle=...)` to validate and infer.

## Layer 0: JSON-LD Context Example
Create `design/docgraph/docling-context.jsonld`:
```jsonld
{
  "@context": {
    "dd":        "https://example.org/docgraph/ont#",
    // Root document class
    "DoclingDocument": "dd:DoclingDocument",
    // Core DoclingDocument fields
    "name":      "dd:name",
    "version":   "dd:version",
    "furniture": { "@id": "dd:furniture", "@type": "@id" },
    "body":      { "@id": "dd:body",      "@type": "@id" },
    "groups":    { "@id": "dd:groups",    "@type": "@id" },
    "texts":     { "@id": "dd:texts",     "@type": "@id" },
    "pictures":  { "@id": "dd:pictures",  "@type": "@id" },
    "tables":    { "@id": "dd:tables",    "@type": "@id" },
    "key_value_items": { "@id": "dd:key_value_items", "@type": "@id" },
    "form_items":      { "@id": "dd:form_items",      "@type": "@id" },
    // Pages as index container
    "pages":     { "@id": "dd:pages",     "@container": "@index" },
    // Common provenance & geometry
    "prov":      "http://www.w3.org/ns/prov#",
    "provenance": "prov:wasGeneratedBy",
    "bbox":      "dd:bbox",
    // NodeItem references
    "self_ref":  { "@id": "@id" },
    "parent":    { "@id": "dd:parent",    "@type": "@id" },
    "children":  { "@id": "dd:children",  "@type": "@id", "@container": "@list" }
    // …extend for remaining fields: label, orig, text, formatting, image, etc.
  }
}
```

## JSON-LD ↔ Pydantic Bridge
Add a small Python mixin in `design/docgraph/io/jsonld.py`:
```python
from pyld import jsonld
from pydantic import BaseModel
from typing import Type, TypeVar

T = TypeVar("T", bound=BaseModel)

class JsonLdMixin(BaseModel):
    @classmethod
    def from_jsonld(cls: Type[T], doc: dict, context: dict) -> T:
        compacted = jsonld.compact(doc, context["@context"])
        # `compacted` now uses Pydantic field names (by alias)
        return cls.model_validate(compacted)

    def to_jsonld(self, context: dict) -> dict:
        data = self.model_dump(by_alias=True, exclude_none=True)
        data["@type"] = self.__class__.__name__
        data["@context"] = context["@context"]
        return jsonld.compact(data, context["@context"])
```

## Implementation Steps
1. Create `design/docgraph/docling-context.jsonld` with mappings above.
2. Define a small `design/docgraph/ontology/docgraph.ttl` module:
   - Classes: `dd:DoclingDocument`, `dd:StructuredContent`, `dd:DocumentPage`, etc.
   - Properties: `dd:hasStructuredContent`, `dd:isStructuredContentOf`, `dd:hasPage`, `dd:processedText`, etc.
3. Update `data/scdoc/ontology.ttl` to `owl:imports` the new `docgraph.ttl`.
4. Author SHACL shapes under `data/scdoc/shapes.ttl` (or `/ont/shapes/shacl/`) for `dd:*` classes.
5. Place `JsonLdMixin` in `design/docgraph/io/jsonld.py` and integrate into each Pydantic BaseModel.
6. Provide example JSON-LD instances in `data/scdoc/instances/` demonstrating:
   - PDF ↔ JSON-LD ↔ Pydantic round-trip
   - Alternate contexts mapping a different JSON-LD structure into the same models.

This plan ensures a lightweight, context-driven interface (Layer 0) for any JSON-LD 1.1 ↔ Pydantic integration,
while fully leveraging DSCDO’s ontology modules, shapes, and rules in CogitareLink’s four-layer design.

## Ontology Glue: Digital Document Representation

To model the structured conceptual view of a document (pages, sections, items, etc.) in the DSCDO ontology, the following extensions are required:

1. Class: dscdo:DigitalDocumentRepresentation
   - SubClassOf: dscdo:DocumentContent (or prov:Entity)
   - Purpose: encapsulate the Pydantic/JSON-LD “DoclingDocument” structure for retrieval and augmented generation
   - Annotations:
     - rdfs:label “Digital Document Representation”@en
     - rdfs:comment “A structured conceptual representation of a digital document, segmented into pages, sections, and items for retrieval and LLM-based augmentation.”@en
     - dcterms:isDefinedBy / skos:definition as appropriate

2. ObjectProperty: dscdo:hasRepresentation
   - Domain: dscdo:ScDigitalDocument
   - Range: dscdo:DigitalDocumentRepresentation
   - Purpose: link a raw digital document (PDF, DOCX) to its structured JSON-LD/Pydantic model
   - Annotations:
     - rdfs:label “hasRepresentation”@en
     - rdfs:comment “Links a digital document to its structured conceptual representation for retrieval and LLM-based augmentation.”@en

3. ObjectProperty: dscdo:isRepresentationOf
   - SubPropertyOf: dscdo:contentExtractedFrom (or declared owl:inverseOf hasRepresentation)
   - Domain: dscdo:DigitalDocumentRepresentation
   - Range: dscdo:ScDigitalDocument
   - Annotations:
     - rdfs:label “isRepresentationOf”@en
     - rdfs:comment “Inverse of dscdo:hasRepresentation.”@en

4. SHACL Shapes (Layer 2)
   - NodeShape for dscdo:ScDigitalDocument:
     • sh:property [ sh:path dscdo:hasRepresentation ; sh:minCount 1 ; sh:maxCount 1 ]
   - NodeShape for dscdo:DigitalDocumentRepresentation:
     • sh:property [ sh:path dscdo:isRepresentationOf ; sh:minCount 1 ; sh:maxCount 1 ]
   - Enforce class membership, cardinality, and datatype constraints for a closed-world assertion of this linkage

5. JSON-LD Context (Layer 0)
   - In docling-context.jsonld, add mappings:
     ```jsonld
     "DigitalDocumentRepresentation": "dscdo:DigitalDocumentRepresentation",
     "hasRepresentation": { "@id": "dscdo:hasRepresentation", "@type": "@id" },
     "isRepresentationOf": { "@id": "dscdo:isRepresentationOf", "@type": "@id" }
     ```

6. Index Ontology Import (Layer 1)
   - Ensure the module defining these classes/properties is listed in data/scdoc/ontology.ttl via owl:imports

These ontology extensions provide the necessary “glue” for any agent or tooling to seamlessly navigate between the physical digital artifact and its structured, Pydantic-backed representation.