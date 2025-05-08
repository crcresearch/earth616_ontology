 # Adopt JSON-LD 1.1 as primary serialization

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/25

 ## Status
 _Proposed_

 ## Decision
 Use JSON-LD 1.1 as the primary serialization for contexts (Layer 0), instance data (Layer 3), and optionally ontology and shapes; retain Turtle (TTL) as a secondary format for tooling.

 ## Context
JSON-LD 1.1 provides advanced graph and container features needed for context prompts (Layer 0) and agent data processing (Layer 3). In CogitareLink, contexts are loaded directly into the model prompt to establish prefix↔IRI mappings and term definitions, and instance data streams leverage JSON-LD 1.1’s set and graph constructs for accurate reasoning. Turtle (TTL) remains available as a secondary format for tooling that requires materialized merges or SHACL rule execution.

 ## Consequences
 - Leverages JSON-LD 1.1 features for LLM prompts and data exchange.
 - Some tooling consumers may require TTL fallbacks.