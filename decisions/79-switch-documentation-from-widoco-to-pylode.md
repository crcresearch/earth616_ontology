 # Switch documentation from Widoco to pyLODE

 Discussion: https://github.com/crcresearch/earth616_ontology/issues/24

 ## Status
 _Proposed_

 ## Decision
 Replace Widoco with pyLODE for HTML generation, storing templates in-repo to allow Python-native extension by agents.

 ## Context
 Widoco’s templating doesn’t support zero-code customization by Codex/CogitareLink agents. pyLODE aligns with our Python-first toolchain and supports in-repo templates.

 ## Consequences
 - Enables customizable, in-repo documentation templates.
 - Adds maintenance responsibility for pyLODE template code.