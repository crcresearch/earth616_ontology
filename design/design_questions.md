# Design Questions

- What is the best knowledge representation language for LLMs in Agentic Systems?
    - Markdown prompt engineering
    - Turtle or N3 file
    - Single source of truth?
- How best to represent reasoning rules?
- Where should the reasoning be instantiated
    - In the graph database?
    - By the retreiver LLM using the ontology?
- How to avoid the Semantic Web Pitfalls (Lessons Learned)

---

Below is a revised set of research questions that focus on the underlying design patterns for agentic systems, including multi-agent approaches, specialized sub-agents, and difficult modeling domains such as geospatial and temporal reasoning. The questions integrate advanced LLM reasoning capabilities, symbolic reasoning as a tool, competency questions for ontology validation, and retriever-agentic architectures grounded in modular ontology design patterns.

## Foundational Design Patterns and System Architectures

	1.	Agentic Design Patterns & Ontology Modularity:
How do foundational agentic design patterns (e.g., Reflection, Tool Use, Planning, Multi-Agent Collaboration) interact with modular ontology design patterns to create more interpretable, scalable, and adaptable knowledge-driven LLM systems?

	2.	Sub-Agent Specialization and Coordination:
What architectural strategies best support diverse sub-agents with specialized roles (e.g., a retrieval agent for querying KGs, a reasoning agent applying symbolic rules, a planning agent coordinating multi-step tasks) working collectively to achieve complex objectives?

	3.	Adaptive Agentic Pipelines:
How can we dynamically orchestrate different agentic patterns—invoking certain tools or sub-agents only when needed—to maintain efficiency and accuracy in response to changing user queries, domain complexities, or data availability?

## Symbolic Reasoning as a Core Agentic Tool

	4.	Symbolic Reasoning as a First-Class Sub-Agent:
In what ways can a dedicated symbolic reasoning sub-agent (running rule-based reasoning, constraint checking, or ontology validation) improve the overall correctness and explainability of LLM outputs, and what interfaces should it share with other agents?
	
    5.	Continuous Improvement Through Reflection:
How can the reflection pattern be extended to incorporate symbolic validations of intermediate reasoning steps, ensuring that the LLM’s chain-of-thought is periodically examined and refined by a symbolic agent before finalizing responses?
	
    6.	Planning with Symbolic Guidance:
Can the planning sub-agent leverage explicit ontological hierarchies, temporal/ geospatial constraints, and rule sets to organize tasks, prioritize tool use, and orchestrate other sub-agents, particularly for domains where precise logical ordering matters (e.g., scheduling, route planning)?

## Competency Questions for Ontology Construction and Validation

	7.	Competency Questions as Ontology Benchmarks:
How can competency questions be systematically integrated into the agentic workflow, enabling specialized ontology-construction or ontology-maintenance sub-agents to detect, propose, and refine ontology modules, ensuring that the knowledge base remains aligned with evolving user needs?
	8.	Iterative Ontology Evolution via Reflection & Collaboration:
Could multi-agent collaboration, guided by competency questions, drive an iterative cycle where one agent identifies ontology gaps (e.g., missing temporal relations), another proposes new axioms or classes, and a reasoning sub-agent validates the changes?
	9.	Automated Ontology Extensions for Complex Domains:
How can domain-specific competency questions (e.g., for geospatial/topological relationships or temporal event sequencing) guide ontology evolution, ensuring that sub-agents specialized in these areas collaboratively improve the ontology’s expressiveness and coverage?

## Retriever-Agentic Systems Utilizing Knowledge Graphs

	10.	Retriever Agents with Modular Ontologies:
How can retriever agents leverage modular ontologies to more efficiently select relevant subsets of knowledge, especially when dealing with complex geospatial queries (e.g., “Find historical events within a 50km radius of a given coordinate and time period”) or intricate temporal constraints?

	11.	Integrating Symbolic and Vector-Based Retrieval:
In what ways can hybrid retrieval strategies—combining embedding-based vector search for semantic approximation and symbolic queries for exact constraints—enhance the quality and accuracy of LLM responses, and can specific sub-agents specialize in one retrieval paradigm?

	12.	Dynamic Query Refinement by Sub-Agents:
How can multiple sub-agents collaborate to iteratively refine queries to a KG, using domain-specific ontological modules (geospatial, temporal, domain entities) and symbolic reasoners to produce richer, more context-aware answers?

## Addressing Complex Modeling Challenges: Geospatial & Temporal Reasoning

	13.	Temporal Reasoning Sub-Agent:
What specialized patterns enable a temporal reasoning sub-agent to interpret, align, and sequence events retrieved from the KG, integrate these sequences into the LLM’s chain-of-thought, and ensure consistency with domain-specific temporal constraints?

	14.	Geospatial Reasoning Tools and Planning:
How can a geospatial reasoning sub-agent, equipped with spatial ontologies and geometric reasoners, assist the planning and retrieval sub-agents in answering queries that require spatial grounding, route optimization, or place-based disambiguation?

	15.	Integrating Uncertain Geospatial/Temporal Data:
Can reflection and tool use patterns help manage uncertainty in geospatial or temporal data (e.g., approximate coordinates, ambiguous event dates) by invoking specialized validation sub-agents or reasoning tools that refine or confirm approximate reasoning steps?

## Evaluation, Robustness, and Long-Term Sustainability

	16.	Benchmarking Multi-Agentic Ontology-Driven Systems:
What metrics or benchmarks should be developed to evaluate multi-agentic systems integrating ontologies, symbolic reasoners, and retriever agents, particularly for complex temporal and geospatial queries?

	17.	Stress-Testing Agent Roles and Interactions:
How can adversarial or stress-testing scenarios be used to evaluate the robustness of agentic architectures—e.g., introducing contradictory temporal constraints or ambiguous geospatial data—and how can reflection or collaboration patterns mitigate inconsistencies?

	18.	Long-Term Maintenance and Ontology Evolution:
As domains change over time, how can specialized sub-agents continuously monitor domain developments, competency questions, and user feedback to prompt ontology updates, adding or refining temporal/geospatial concepts and ensuring the knowledge base remains relevant?

	19.	Domain-Specific Agent Configurations:
How do we generalize agentic design patterns across domains with different complexity profiles (e.g., biomedical vs. geospatial intelligence)? Can template-based sub-agents and ontology modules be reused or adapted to new contexts?

	20.	Human-in-the-Loop Interventions:
When fully automated agentic patterns fail (e.g., in complex temporal reasoning or novel geospatial scenarios), what guidelines ensure effective human oversight, enabling domain experts to guide ontology refinement, adjust competency questions, or recalibrate sub-agent roles?
