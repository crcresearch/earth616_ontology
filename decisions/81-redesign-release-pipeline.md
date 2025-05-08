 # Redesign release pipeline

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/26

 ## Status
 _Proposed_

 ## Decision
 Implement a release pipeline that emits versioned and “latest” artifacts for all four layers: `index.ttl`, `merged.ttl`, JSON-LD contexts, SHACL shapes & rules, and the CogitareLink bundle (`data/scdoc`).

 ## Context
To support CogitareLink’s four-layer model (Context, Ontology Modules, Shapes & Rules, Data), agents and CI/CD pipelines require stable, machine-readable endpoints for each artifact type: JSON-LD contexts, index and merged ontologies, SHACL shapes & rules, and domain data bundles. This consistency ensures predictable discovery and retrieval during agent workflows and automated releases.

 ## Consequences
 - Provides automated multi-artifact releases.
 - Introduces additional CI/CD complexity.