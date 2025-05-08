 # Move inference from OWL-RL to SHACL/SPARQL

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/22

 ## Status
 _Proposed_

 ## Decision
 Remove OWL-RL based reasoning and express all inference rules as SHACL rules or SPARQL CONSTRUCT shapes in `RL_rules.shapes.ttl`.

 ## Context
 Embedded OWL-RL reasoners introduce hidden behavior. Explicit SHACL/SPARQL rules offer transparent reasoning that CogitareLink agents can invoke directly.

 ## Consequences
 - Improves transparency and provenance of inferred triples.
 - Requires manual re-authoring of existing OWL-RL rules, with potential coverage gaps.