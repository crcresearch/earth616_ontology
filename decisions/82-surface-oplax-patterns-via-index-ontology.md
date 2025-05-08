 # Surface OPLaX patterns via index ontology

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/27

 ## Status
 _Proposed_

 ## Decision
 Import OPLaX pattern modules into the index ontology to expose pattern metadata via `owl:imports` and SKOS annotations.

 ## Context
CogitareLink’s AffordanceScanner.extract() relies on owl:imports and SKOS annotations in the index ontology (Layer 1) to discover OPLaX pattern metadata at runtime. Importing OPLaX modules directly into the index ontology ensures that agents can retrieve design-pattern guidance seamlessly during navigation and validation, without separate lookups or network requests.

 ## Consequences
 - Pattern guidance becomes directly discoverable in the ontology index.
 - Increases index ontology size and dependency on pattern changes.