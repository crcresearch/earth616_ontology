<!--
  Redesign Plan: Expose DSCDO for CogitareLink Agents
  File: design/redesign.md
-->
# DSCDO & CogitareLink Integration: Redesign Plan

## 1. Introduction and Objectives

This document presents a comprehensive plan to refactor the Defense Supply Chain and Documentation Ontology (DSCDO) repository so that:
  1. DSCDO becomes a drop-in domain for CogitareLink agents with zero-code configuration.
  2. The OPLaX pattern vocabulary (in modules/imports/oplax.owl) is surfaced via an index ontology, enabling LLMs to navigate pattern metadata.
  3. The release pipeline produces a clear separation between:
     - an **Index Ontology** (owl:imports raw modules, OPLaX, patterns),
     - a **Merged Ontology** (for programmatic use and Widoco docs),
     - bundled **Contexts** and **Shapes** under the ontology URI space,
     - a **CogitareLink Bundle** (`data/scdoc/`) following the 4-layer model.

## 2. Requirements

1. **Index Ontology (`index.ttl`)** available at `<baseURI>/ont/`:
   - Declares `owl:imports` for each raw module TTL/OWL (including OPLaX).
   - Contains version metadata (`owl:versionIRI`, `dcterms:modified`, etc.).
2. **Merged Ontology (`merged.ttl`)**:
   - Unchanged: merge of modules listed in `tests/modules.txt` + OPLaX.
3. **Contexts** (`.jsonld`):
   - Bundled under `<baseURI>/ont/contexts/` (versioned and “latest”).
4. **Shapes** (`.jsonld`) and **SHACL TTL**:
   - Bundled under `<baseURI>/ont/shapes/shacl/` (versioned and “latest”).
5. **Patterns** (`.ttl`):
   - Raw pattern files under `<baseURI>/ont/patterns/` for on-demand fetch.
6. **CogitareLink Bundle** (`data/scdoc/`):
   - `context.jsonld` (minimal Layer 0 context),
   - `ontology.ttl` (the index ontology),
   - `shapes.ttl` (concatenated SHACL shapes TTL),
   - `rules.ttl` (optional inference rules),
   - `instances/` (example JSON-LD docs).
7. **JSON-LD 1.1 as Primary Representation**:
   - Use JSON-LD 1.1 for all Layer 0 contexts and Layer 3 data to leverage advanced container, set, and graph features.
   - Publish the index ontology and SHACL shapes also as JSON-LD 1.1, with TTL provided as a secondary serialization for programmatic merges and tooling.

## 3. Foundational Vocabularies

## 3. Foundational Vocabularies

To maximize LLM familiarity and interoperability, DSCDO will reuse widely adopted foundational ontologies:

- **schema.org**: for common classes and properties (organizations, persons, events, documents, URLs, dates).
- **Prov-O** (`http://www.w3.org/ns/prov#`): to represent provenance activities, agents, and entities.
- **OWL-Time** (`http://www.w3.org/2006/time#`): for temporal grounding (instants, intervals, durations).
- **GeoSPARQL** (`http://www.opengis.net/ont/geosparql#`): for spatial data (geometries, features, spatial relationships).

Domain-specific vocabularies (e.g., GS1 EPCIS/CBV, SPDX, ML Commons Croissant) will be imported only where needed within modules or shapes, keeping the core ontology concise and maximizing LLM familiarity.
## 4. Enforcing Semantics: Open-World vs Closed-World

To maintain a lightweight open-world ontology while centralizing domain logic in SHACL, we propose:

- **Open-World Layer (schema.org, Prov-O, OWL-Time, GeoSPARQL)**
  - Use schema:domainIncludes and schema:rangeIncludes (or rdfs:comment) in TTL modules as advisory guidance.
  - Do not assert owl:domain or owl:range for external vocabularies, and do not enforce them in SHACL.
  - Preserve open-world semantics; treat them as unconstrained pointers.

- **Closed-World Layer (DSCDO Core Modules)**
  - Define precise domain and range axioms in DSCDO's own namespace as owl:domain and owl:range where needed.
  - Enforce structural constraints via SHACL NodeShapes (sh:class, sh:minCount, sh:maxCount).
  - Encode complex axioms through SHACL constraint components (sh:not, sh:or, sh:and) or sh:Rule/SPARQL CONSTRUCT shapes to derive required triples.

 - **Moving Domain Logic to SHACL**
  - Identify all current OWL axioms used for business rules.

    **OWL Axioms to Refactor:**
    - In `modules/core/event.ttl`, remove global restrictions on `owl:Thing` (e.g., universal restrictions on `dscdo:subEventOf`, `hasInformationObject`, `providesParticipantRole`, `hasSpatioTemporalExtent`).  Move each into SHACL NodeShapes or rule shapes enforcing the same constraint.
    - Drop the meta-model axioms:
      ```turtle
      rdfs:range rdfs:subPropertyOf owl:ObjectProperty .
      rdfs:domain rdfs:subPropertyOf owl:ObjectProperty .
      ```
      Express property type constraints in SHACL instead.
    - Audit all `rdfs:domain`/`rdfs:range` in DSCDO modules:
      - For external vocabularies (schema.org, Prov-O, OWL-Time, GeoSPARQL), convert to advisory annotations (e.g. `schema:domainIncludes` / `schema:rangeIncludes` or `skos:note`) and remove `owl:domain`/`owl:range`.
      - For DSCDO properties, keep domain/range as documentation but enforce cardinality, class membership, and complex axioms via SHACL constraints and rules.

  - For structural validation, author NodeShapes capturing mandatory/exclusive properties.
  - For inference, write SHACL rules or SPARQL CONSTRUCT shapes that generate equivalent RDF.
  - Keep ontology modules focused on schema (classes, properties, SKOS labels, OPLaX) while SHACL handles validation and derivation.

- **Benefits for LLM Agents**
  - Index ontology remains simple and open-world.
  - CogitareLink’s `reason_over` leverages SHACL artifacts for validation and inference without code changes.
  - Agents see rich SKOS/OPLaX guidance but rely on shapes/rules to enforce and derive semantics.

## 5. Proposed Architecture

```text
  CogitareLink Agent
         │
  GET <baseURI>/ont/   →  Content negotiation → index.ttl
         │
  Index Ontology (index.ttl)
     owl:imports → modules/*.ttl, modules/imports/oplax.owl, patterns/*.ttl
         ↓
  Fetch raw modules & OPLaX for pattern metadata

  Merged Ontology (merged.ttl) + Widoco docs under <baseURI>/ont/<version>/
  Contexts under <baseURI>/ont/contexts/
  Shapes under <baseURI>/ont/shapes/shacl/
```

### CogitareLink Four-Layer Alignment

To integrate seamlessly with CogitareLink, DSCDO maps into the four-layer model:

- **Layer 0 (Context):**
  - JSON-LD contexts (*.jsonld) serve as prefix-to-IRI maps and any term enumerations for closed-world assumptions.
  - No domain logic—always loaded in-prompt for LLMs.
- **Layer 1 (Ontology Modules):**
  - Turtle/OWL files with class and property declarations.
  - Enriched with SKOS annotations (skos:prefLabel, skos:definition, skos:note, skos:example) and breadcrumb links (skos:broader/narrower).
  - Imports OPLaX (modules/imports/oplax.owl) so pattern metadata is discoverable by the LLM.
- **Layer 2 (Shapes & Rules):**
  - SHACL NodeShapes for structural validation (minCount, datatypes, cardinality).
  - SHACL rules or SPARQL CONSTRUCT shapes for inferencing, encoding all business logic in data artifacts.
  - Enables CogitareLink’s `reason_over` to apply both validation and derivation passes.
- **Layer 3 (Data):**
  - JSON-LD instance documents (*.jsonld) pointing to shapes via ex:hasShape or similar.
  - Streamed to the agent at runtime to trigger shape-based inference.

### Why This Matters for LLM Agents

- The **Context** layer (< 5 KB) lives in-prompt, ensuring the model always knows your prefixes.
- **Ontology Modules** are fetched on-demand; rich SKOS and OPLaX annotations give the LLM human-readable guidance and pattern links without code.
- **Shapes & Rules** drive all reasoning—no hidden Python, just data-driven SHACL/SPARQL rules that the agent can invoke.
- **Data** is streamed in as JSON-LD; agents call `reason_over(shapes_turtle=...)` to derive new triples with full provenance.

### Typical Agent Workflow

1. Prompt includes Layer 0 context.jsonld.
2. Agent fetches Layer 1 ontology.ttl (index ontology) and reads SKOS labels, definitions, and OPLaX pattern metadata.
3. AffordanceScanner scans Layer 2 shapes.ttl for NodeShapes and rule shapes.
4. Agent streams a JSON-LD instance (Layer 3) and calls `reason_over(shapes_turtle=...)` to run SHACL rules.
5. New triples (and natural-language summaries) are returned and stored with provenance by the micro-kernel.


## 6. Implementation Steps

1. **Include OPLaX**
   - Append `oplax,./modules/imports/oplax.owl` in `tests/modules.txt`.
   - Enhance `scripts/merge_ontology.py` to parse `.owl` formats.
2. **Update Root Ontology**
   - In `modules/core/metadata.ttl`, add `owl:imports <../imports/oplax.owl>` to the ontology declaration.
3. **Generate `index.ttl`**
   - Copy raw `modules/` and `patterns/` into `${VERSION_DIR}/modules` & `/patterns` in `build-release.sh`.
   - Script a block that reads `tests/modules.txt` and emits an `owl:imports` list, plus OPLaX and patterns.
4. **Revise Widoco Invocation**
   - Point Widoco at `index.ttl` instead of `merged.ttl` to generate HTML & WebVOWL over the import graph.
5. **Bundle Contexts & Shapes**
   - In `build-release.sh`, copy JSON-LD contexts into `${VERSION_DIR}/contexts/`.
   - Copy SHACL JSON-LD shapes into `${VERSION_DIR}/shapes/shacl/`.
6. **Create CogitareLink Bundle**
   - Build or extend a script to output `data/scdoc/` with the four-layer artifacts.
7. **Documentation Updates**
   - Add a “Using DSCDO with CogitareLink” section in `README.md`.
   - Reference this `design/redesign.md` for contributors.

## 7. Testing & Validation

- **Merge Tests**: ensure `scripts/merge_ontology.py` handles all extensions.
- **SHACL Validation**: run existing `tests/shacl-test.sh` against `index.ttl + shapes.ttl`.
- **SPARQL Tests**: validate competency queries on `merged.ttl`.
- **CogitareLink Smoke Test**: configure a local CogitareLink instance to load `data/scdoc/` and `reason_over` against a sample JSON-LD.

## 8. Directory Structure After Redesign

```
design/
  ├─ redesign.md          # this plan
  └─ cogitarelink.md      # existing design notes

data/scdoc/
  ├─ context.jsonld
  ├─ ontology.ttl
  ├─ shapes.ttl
  ├─ rules.ttl
  └─ instances/

release/ontology/<version>/
  ├─ index.ttl
  ├─ merged.ttl
  ├─ modules/
  ├─ patterns/
  ├─ contexts/
  ├─ shapes/shacl/
  ├─ index-en.html
  └─ webvowl/, sections/, provenance/, resources/
```

## 9. Rollout & Timeline

1. Review and finalize this plan.
2. Update tests/modules.txt & merge_ontology.py.
3. Modify `metadata.ttl` imports.
4. Implement `index.ttl` generation and revised build-release.sh.
5. Build and test CogitareLink bundle.
6. Update docs/README, bump to v0.2.0.
7. Gather feedback and iterate.

## 10. Additional Considerations

Beyond the core redesign steps, ensure we address:

- **Stories & Test Fixtures**: Expose the `stories/` user stories and SPARQL tests as example workflows or fixtures in the CogitareLink bundle (e.g. `data/scdoc/stories/`).
- **ADR & Documentation Links**: Surface key Architectural Decision Records (in `decisions/`) in the index documentation or CogitareLink bundle.
- **Patterns & Alignment TTLs**: Include alignment TTLs (e.g. from `design/CCO-Alignment/` or pattern directories) via OPLaX imports or a dedicated `patterns/alignments.ttl`.
- **Context Enumerations**: Merge closed-world term lists (such as enumerated `DocumentType` values) into the Layer 0 context so agents can enforce them.
- **CI Smoke Tests**: Extend CI (e.g. GitHub Actions) to run a CogitareLink smoke test that loads `data/scdoc/` and executes a simple `reason_over` invocation.
- **Metadata Propagation**: Copy ontology metadata (title, description, versionInfo, license, authorship) into `index.ttl` so the Widoco-generated HTML retains full documentation.
- **URI Redirects & Content Negotiation**: Document or supply redirect rules (e.g. w3id.org, HTTP server config) mapping `<baseURI>/ont/…` to the correct artifacts.
- **Pre-commit & Packaging**: Ensure new build scripts and data bundles conform to existing pre-commit hooks or explicitly disable them as needed, and update package metadata if applicable.