 # Refactor domain/range axioms into SHACL and advisory annotations

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/23

 ## Status
 _Proposed_

 ## Decision
 Strip `owl:domain` and `owl:range` for external vocabularies; convert to `schema:domainIncludes`/`schema:rangeIncludes` or `skos:note`; enforce closed-world constraints via SHACL NodeShapes.

 ## Context
 To maintain open-world semantics in the ontology while performing closed-world validation, domain and range axioms should live in SHACL rather than OWL.

 ## Consequences
 - Preserves open-world ontology semantics and centralizes validation in SHACL.
 - Consumers must use SHACL shapes for domain/range validation.