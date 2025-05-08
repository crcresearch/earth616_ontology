 # Separate Index vs Merged Ontologies

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/21

 ## Status
 _Proposed_

 ## Decision
 Ship both an index ontology (imports raw modules and OPLaX patterns) and a merged ontology (materialized graph) to serve different use cases.

 ## Context
Within CogitareLink’s four-layer model, the index ontology (Layer 1: Ontology Modules) is fetched on-demand by the AffordanceScanner for class/property navigation. The merged ontology serves as a materialized graph used by the GraphManager and programmatic tooling (e.g., CI pipelines) for querying, validation, and transformation.

 ## Consequences
 - Provides targeted artifacts for both agents and tools.
 - Requires maintaining consistent versioning across two outputs.