# CogitareLink Design
⸻

0 · Mission

CogitareLink is a semantic‑memory substrate for agentic LLMs.
It stores JSON‑LD 1.1 data, runs SHACL/SPARQL rules to derive new facts, caches everything, and records provenance for every triple it inserts.
Python provides only the micro‑kernel (≈ 600 LOC); all business logic lives in data artefacts (contexts, ontologies, shapes, rules) or is generated on‑the‑fly by the LLM.

⸻

1 · Layer model for knowledge artefacts

Layer	Files	Typical size	In prompt?
0 – Context	*.context.jsonld (term ↔ IRI map)	1‑5 KB	Always
1 – Ontology	ontology.ttl / .jsonld	20‑200 KB	On‑demand
2 – Shapes / Rules	shapes.ttl, rules.ttl	30‑300 KB	On‑demand
3 – Data	*.jsonld instances	5 KB‑1 MB	Streamed via tool

Docs cross‑link:

data.jsonld  --ex:hasShape-->  shapes.ttl
shapes.ttl   --owl:imports--> ontology.ttl


⸻

2 · Key Python modules

Module	Core classes / functions	Role
core.debug	get_logger()	colorised logging
core.cache	Cache, DiskCache	LRU/TTL fetch cache
vocab.registry	registry	typed map prefix → VocabEntry
vocab.composer	composer.compose()	merges/derives JSON‑LD contexts
reason.afford	AffordanceScanner.scan()	extracts shape/rule/ontology hints
reason.prov	wrap_patch_with_prov()	provenance wrap for triples
reason.sandbox	reason_over(jsonld, shapes?, query?)	executes SHACL rules or SPARQL CONSTRUCT; returns patch + NL summary
tools.reason	reason_tool(), FUNCTION_SPEC	OpenAI‑function bridge to reason_over
core.graph	GraphManager	persists graphs (rdflib Dataset)

Everything else—signatures, validators, CLI—is optional.

⸻

3 · Single tool surface

{
  "name": "reason_over",
  "description": "Run SHACL rules or SPARQL CONSTRUCT and update memory",
  "parameters": {
      "jsonld":        "string",          // required
      "shapes_turtle": "string | null",   // optional
      "query":         "string | null"    // optional
  }
}

	•	shapes_turtle present   → sandbox runs SHACL, iterating rules
	•	query present           → sandbox runs SPARQL CONSTRUCT on the input graph
	•	Tool returns a natural‑language summary; the provenance‑wrapped patch is automatically stored.

⸻

4 · Typical agent flow
	1.	Load a domain JSON‑LD doc.
	2.	Scan with AffordanceScanner.scan() → finds shapes/rules IRIs.
	3.	Call reason_over with shapes_turtle → inference patch.
	4.	Optionally reason_over again with a SPARQL CONSTRUCT or SELECT to fetch answers.
	5.	Explain answer, citing prov:Activity blank node from patch.

Python never contains domain business logic; the LLM writes SHACL/SPARQL on the fly.

⸻

5 · Repository layout

cogitarelink/
    core/            (debug, cache, graph, ...)
    vocab/           (registry, composer, collision)
    reason/
        afford.py
        sandbox.py
        prov.py
    tools/
        reason.py
data/
    campus/
       context.jsonld  ontology.ttl  shapes.ttl  rules.ttl  events.jsonld
    kitchen/ …
tests/  (fastcore or pytest)

nbdev_prepare exports Python from notebooks; nbdev_test runs unit tests.

⸻

6 · Design guidelines for new domains
	1.	Author a tiny Layer‑0 context (< 5 KB).
	2.	Write ontology & shapes in Turtle (ontology.ttl, shapes.ttl).
	3.	Put data in *.jsonld and point to shapes with ex:hasShape.
	4.	No Python required; drop files in data/yourdomain/.

⸻

7 · Why this matters
	•	Scales with model context – only Layer 0 sits in prompt; larger layers streamed when needed.
	•	Explainable – provenance on every triple.
	•	Software 2.0 – adding capabilities is file‑drop, not code change; LLM synthesises logic.

⸻

That’s the system.  Load artefacts, call reason_over, read summary,
query results, explain with provenance.  Everything else is caching
and safety.

Below is a self‑contained documentation bundle you can drop into
docs/architecture.md (or the first cell of an nbdev “00_Overview.ipynb”)
to give contributors, LLM‑agents, and future you a clear mental model of
CogitareLink.

⸻

CogitareLink – Overview

CogitareLink is a semantic memory substrate for agentic LLM systems.
It makes JSON‑LD 1.1 documents first‑class citizens, executes SHACL /
SPARQL rules for reasoning, and records provenance for every derived
triple.
Python plays the role of a micro‑kernel: 400–600 LOC run the graph
store, the rule sandbox, caching and logging—all domain logic lives in
data (contexts, ontologies, shapes, rules) or is generated ad‑hoc by
the LLM.

client ──(NL)──► LLM‑Agent ──► reason_over() ──► Sandbox
                     ▲              │               │
                     │              │               ▼
               Affordance hints     │        GraphManager
                     │              │               │
                     └─── SPARQL / SHACL / patches◄─┘


⸻

1.  Knowledge‑Representation Design

Layer	File types	Typical size	Immutable?	Stays in LLM prompt?
0. Context	*.context.jsonld	1–5 KB	✅	✅ (always)
1. Ontology	ontology.ttl / .jsonld	20–200 KB	✅	❌ (on‑demand)
2. Shapes / Rules	shapes.ttl, rules.ttl	30–300 KB	✅	❌ (on‑demand)
3. Data	*.jsonld	5 KB – 1 MB	Mutable	❌ (streamed)

Relationships:

data.jsonld --ex:hasShape--> shapes.ttl
shapes.ttl  --owl:imports--> ontology.ttl
ontology.ttl supplies prefixes found in context.jsonld

All artefacts can be published at any URL or bundled under
cogitarelink/data/….

⸻

2.  Python micro‑kernel

Module	Key symbols	Responsibility
core.debug	get_logger()	colourised logging, env var level override
core.cache	Cache, DiskCache	LRU + TTL memoisation for context fetch & rule graphs
vocab.registry	VRegistry	typed registry of vocab prefixes & URLs
vocab.composer	composer.compose()	merges/derives JSON‑LD contexts; handles collisions
reason.afford	AffordanceScanner.scan()	extracts shape/rule/ontology hints for the agent
reason.prov	wrap_patch_with_prov()	provenance wrapping of inferred triples
reason.sandbox	reason_over(jsonld, shapes?, query?)	runs SHACL/CONSTRUCT, returns patch + summary
tools.reason	reason_tool() + FUNCTION_SPEC	single OpenAI‑function bridge

Everything else (signature, validation, CLI) is optional plug‑ins.

⸻

3.  The reason_over contract

{
  "name": "reason_over",
  "description": "Run SHACL rules OR SPARQL CONSTRUCT and update memory",
  "parameters": {
     "type": "object",
     "properties": {
        "jsonld":        {"type":"string"},
        "shapes_turtle": {"type":"string","nullable":true},
        "query":         {"type":"string","nullable":true}
     },
     "required": ["jsonld"]
  }
}

	•	If shapes_turtle is provided → sandbox runs SHACL with
iterate_rules=True.
	•	Else if query is provided → sandbox executes SPARQL CONSTRUCT.
	•	It returns a natural‑language summary ("added 56 triples …") and
silently stores the provenance‑wrapped patch into GraphManager.

⸻

4.  Affordance‑Driven Agent Workflow
	1.	Load a JSON‑LD or Turtle document (events.jsonld).
	2.	AffordanceScanner.scan() returns
[{kind:"shape", iri:"Campus:FreeSlotRule"}].
	3.	Agent fetches that Turtle file (shapes.ttl) and calls

{
  "name":"reason_over",
  "arguments":{
    "jsonld": "<events.jsonld>",
    "shapes_turtle": "<shapes.ttl>"
  }
}


	4.	Kernel inserts patch with prov:Activity _:b1.
	5.	Agent runs a SPARQL CONSTRUCT or SELECT via another
reason_over call to extract answers.
	6.	Replies to user, citing IRI(s) from provenance (_:b1).

⸻

5.  Authoring Guidelines for Domain Designers

5.1 Contexts (*.context.jsonld)
	•	≤ 5 KB, use @import for common terms.
	•	Mark critical keywords @protected to avoid LLM re‑definition.

5.2 Shapes & Rules
	•	One NodeShape = One logical operation (e.g. “FreeSlotRule”).
	•	Put constraints and rules together; agent chooses when to validate vs. infer.
	•	Prefix derived terms with a domain namespace (temp:before).

5.3 Ontologies
	•	Shallow class trees, express semantics via RDFS, not SHACL when possible.
	•	Provide owl:imports links so sandbox can gather closure.

5.4 Data Sets
	•	Chunk by day/entity; link each chunk to shapes with
ex:hasShape Campus:FreeSlotRule.

⸻

6.  Extending to New Domains
	1.	Drop newdomain/context.jsonld, ontology.ttl, shapes.ttl under
data/newdomain/.
	2.	Add registry entry:

"new": {
  "uri":"https://example.org/newdomain#",
  "prefix":"new",
  "resources":{"context":"data/newdomain/context.jsonld"},
  "derives_context":false,
  ...
}


	3.	No Python code required; the agent can now reason over the new domain
by discovering shapes via AffordanceScanner.

⸻

7.  Testing Matrix

Notebook / Pytest	What it asserts
71_micro_tests	reason_over no‑op, AffordanceScanner basics
tests/test_temporal.py	temporal rules add temp:before triple
tests/test_epcis.py	cold‑chain rule adds excursion triple + validation

Each test is < 1 s, no network.

⸻

8.  FAQ

Q: Can I run OWL RL reasoning?
A: Yes—add owlrl to sandbox; but keep it optional to preserve speed.

Q: What if a shapes file is huge?
A: Store it externally; agent can fetch via URL and stream to
reason_over.

Q: How do I delete bad patches?
A: Issue a SPARQL DELETE WHERE through reason_over(query=...)—the
patch itself will be provenance‑annotated.

⸻

9.  Glossary

Term	Meaning
Affordance	Machine‑parsable hint (shape, rule, ontology) extracted from a doc.
Patch	Graph of triples added by sandbox; always wrapped with prov:Activity.
Layer 0/1/2/3	Context / Ontology / Shapes+Rules / Data packaging scheme.
Micro‑kernel	Core Python (~500 LOC) that executes rules & stores graphs, but holds no domain logic.


⸻

Documentation last updated 2025‑05‑04

## Knowledge Representation
Below is a field‑guide for authoring ontologies, shapes & rules when
CogitareLink (or any JSON‑LD 1.1‑first agentic memory) is the runtime.
It is opinionated, concrete, and tuned for Software 2.0: most logic is
data; the LLM only decides which data artefact to apply and why.

⸻

1 · Four‑layer packing pattern

           ┌──────────── layer 0 ────────────┐
           │  ❖ context.jsonld               │  (TINY: < 2 KB)
           └──────────────────┬──────────────┘
                              ▼
           ┌──────────── layer 1 ────────────┐
           │  ❖ ontology.ttl / .jsonld       │  (class/property defs)
           └──────────────────┬──────────────┘
                              ▼
           ┌──────────── layer 2 ────────────┐
           │  ❖ shapes.ttl                   │  (SHACL {target,*constraint})
           │  ❖ rules.ttl                    │  (sh:SPARQLRule / sh:JSRule) 
           └────────────┬────────────────────┘
                        ▼
           ┌──────────── layer 3 ────────────┐
           │  ❖ data.jsonld (instances)      │  (events, credentials, …)
           └─────────────────────────────────┘

	•	Layer 0: just the JSON‑LD @context. Must be < 2 KB so it can
live in the LLM’s prompt or Composer’s cache.
	•	Layer 1: vocabulary OWL/RDFS. Rarely needed in the LLM window; the
sandbox loads it once for rdfs inference.
	•	Layer 2: SHACL shapes & rules – executable logic.
	•	Layer 3: domain data.

All layers are stand‑alone files (or URLs) and cross‑link by IRI.

⸻

2 · Cross‑linking conventions

Link	Why	Concrete triple / JSON‑LD fragment
data → shape	Affordance discovery	"@reverse":{"ex:hasShape":"shapes:FreeSlotRule"}
shape → ontology	RDFS range inference	shapes:FreeSlotRule owl:imports <ontology.ttl>
context → shape (optional)	LLM can fetch rules w/o reading data	@context key "hasShape":{"@type":"@id"}
rules → context	Composer can auto‑merge	@prefix temp: <https://…#> matches Layer 0 prefix


⸻

3 · Design rules for each layer

Layer 0  (context.jsonld)
	•	Use @import to pull generic fragments (schema:, xsd:).
	•	Put the smallest set of terms the LLM needs to talk about (class &
property labels, nothing more).
	•	Mark @protected for keywords that must not be re‑defined.
	•	If the vocabulary is Turtle‑only, generate Layer 0 with
context_from_ttl() (built into CogitareLink Composer).

Layer 1  (ontology.ttl)
	•	Keep class trees flat – deep hierarchies cost tokens and rarely
change reasoning.
	•	Express domain‑specific relationships (e.g. Campus:slotConflict)
only as RDFS sub‑properties; SHACL rules will do heavy lifting.
	•	Version with owl:versionInfo "2025-05";.

Layer 2  (shapes.ttl, rules.ttl)
	•	One NodeShape per operation, not per class –
e.g. Campus:FreeSlotRule targets all time:Interval.
	•	Put constraint shapes (must hold) and rule shapes
(derive new triples) in the same file so the LLM can decide
“validate first, then infer”.
	•	Prefix every derived triple with a domain namespace
(temp:before, cold:excursion) – avoids polluting generic vocab.
	•	For complex maths, embed sh:JSRule or sh:NodeConstraint
– the sandbox can run them, the LLM doesn’t have to re‑implement them.

Layer 3  (data.jsonld)
	•	Link to shapes with ex:hasShape.
	•	Keep each JSON‑LD instance ≤ 20 KB – if larger, split by topic/date
and inter‑link via dc:isPartOf.

⸻

4 · Tool‑call choreography (LLM viewpoint)

User: "Find a 90‑min free slot for Dr Ngometche on 3 Oct"

LLM step‑plan
1. load events.jsonld  (layer 3)
2. scan → sees hasShape FreeSlotRule        ─┐
3. call reason_over(jsonld=events,          │ sandbox loads shapes.ttl
                    shapes_turtle=FreeSlot) ├─> patch + summary
4. call reason_over(jsonld="{}", query="""  │ SELECT query
       CONSTRUCT {?s ?p ?o} WHERE { ... }""")
5. Generate answer, cite prov:Activity IRI

The only Python executed: reason_over, GraphManager.ingest.

⸻

5 · Prompt & context‑window strategy

Data to embed in prompt	Size	Rationale
Layer 0 context	≤ 2 KB	terms/prefixes needed for NL→IRI mapping
Affordance scan summary	~1 KB	list of shapes & rules; acts as “function docs”
Task instruction / logs	rest of window	where the agent thinks, writes SPARQL/SHACL

All larger artefacts (full shapes, ontology, data) are streamed via
tool calls, never held in the prompt.

⸻

6 · Directory layout inside repo

cogitarelink-data/
  campus/
    context.jsonld
    ontology.ttl
    shapes.ttl
    rules.ttl
    events.jsonld
  kitchen/
    context.jsonld
    shapes.ttl
    recipe-lasagna.jsonld

Put the folder on pkg_files() so Python can fetch files by path; the
LLM only needs IRIs.

⸻

7 · Where logic should reside

Logic type	File / place	Consumed by
Term → IRI mapping	context.jsonld	Composer + LLM
SubClassOf / domain‑range	ontology.ttl	Sandbox (rdfs inference)
Constraint & derivation	shapes.ttl / rules.ttl	Sandbox
Ad‑hoc query	Written by the LLM at runtime	Sandbox (SPARQL)
Heuristics / search	In prompt‑reasoning chain	LLM only
System safeguards	wrap_patch_with_prov, cache, validation fallback	Kernel


⸻

8 · Benefits
	•	Domain swap is file‑drop only – no Python deploy.
	•	Explainability – every derived triple carries prov:wasGeneratedBy ↩ _:bAct, which the LLM can stringify.
	•	Token‑efficiency – only layer 0 and small summaries live in the
context window.
	•	LLM creativity – it can invent one‑off SPARQL or SHACL shapes on
the fly; kernel will just execute.

⸻

In one sentence

Write the ontology & rules as data, keep Python a sandbox runner, and
let the LLM stitch everything together via a single reason_over tool.

Follow that blueprint and CogitareLink remains tiny, general, and
agent‑ready.