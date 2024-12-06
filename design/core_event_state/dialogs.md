Here is the revised **Core State-Event Pattern** documentation, updated to include logical refinements and address consistency concerns, formatted to match the style of previous ontology design pattern publications:

---

# **Core State-Event Pattern**

### **Authors**
Your Name  
Institution or Organization  
Email Address  

### **Abstract**
The Core State-Event Pattern is an extension of the Core Event Pattern that integrates the concept of **states** and **state transitions** into event modeling. States represent the conditions or lifecycle stages of entities, while transitions capture changes between states, typically triggered by events. This pattern provides a minimal, logically consistent framework for representing dynamic systems where entities undergo changes over time and space. The design emphasizes modularity, extensibility, and logical consistency, making it suitable for applications such as supply chains, IoT monitoring, and process tracking.

---

## **1. Introduction and Motivation**
Dynamic systems often require both **event-based** and **state-based** modeling to represent entities and their transformations over time. Events represent occurrences, but states provide additional context about the lifecycle and conditions of entities. For example:
- A container in a supply chain moves through states such as `Produced`, `InTransit`, and `Stored`, triggered by events like transport or storage.
- A machine in an IoT system may transition from `Operational` to `Damaged` due to overheating events.

While the Core Event Pattern provides a strong foundation for event modeling, it does not explicitly address states or their transitions. This pattern extends the Core Event Pattern by integrating states, transitions, and their interactions with events, ensuring logical consistency while maintaining modularity.

---

## **2. The Pattern**

### **2.1 Key Concepts**
1. **State**:
   - Represents a condition or lifecycle stage of an entity.
   - Examples: `ProducedState`, `InTransitState`, `StoredState`, `DamagedState`.

2. **StateTransition**:
   - Represents the transition between states, triggered by an event.
   - Captures `hasPreState` (starting state) and `hasPostState` (resulting state).

3. **Event**:
   - An occurrence in time and space that causes state changes or other effects.

4. **StatefulEntity**:
   - A subclass of `Entity` that can have states (e.g., physical objects, agents, or systems).

5. **SpatioTemporalExtent**:
   - Represents the temporal and spatial context of events and states.

### **2.2 Relationships**
- `hasState`: Links a `StatefulEntity` to its current state.
- `hasPreState`/`hasPostState`: Links a `StateTransition` to its preceding and succeeding states.
- `triggers`: Links an `Event` to the `StateTransition` it causes.
- `occursAt`: Links an `Event` or `State` to its spatiotemporal extent.
- `isSubStateOf`: Captures hierarchical relationships between states.

### **2.3 Axioms**
#### **Event Axioms (from Core Event Pattern)**
1. Every event has a spatiotemporal extent:
  $$
   \text{Event} \sqsubseteq \exists \text{hasSpatioTemporalExtent}.\text{SpatioTemporalExtent}
   $$

2. Every event has at least one participant role:
   $$
   \text{Event} \sqsubseteq \exists \text{providesParticipantRole}.\text{ParticipantRole}
   $$

3. SubEvent relationships are transitive:
   $$
   \text{subEventOf} \circ \text{subEventOf} \sqsubseteq \text{subEventOf}
   $$

#### **State Axioms**
1. Only stateful entities can have states:
   $$
   \text{StatefulEntity} \sqsubseteq \exists \text{hasState}.\text{State}
   $$

2. States have temporal extents:
   $$
   \text{State} \sqsubseteq \exists \text{hasTemporalExtent}.\text{TemporalExtent}
   $$

3. States are temporally disjoint for the same entity:
   $$
   \text{StatefulEntity}(x) \land \text{hasState}(x, s_1) \land \text{hasState}(x, s_2) \land s_1 \neq s_2 \rightarrow \neg \text{overlaps}(\text{TemporalExtent}(s_1), \text{TemporalExtent}(s_2))
   $$

#### **State-Event Axioms**
1. Events trigger state transitions:
   $$
   \text{Event} \sqsubseteq \exists \text{triggers}.\text{StateTransition}
   $$

2. State transitions link pre- and post-states:
   $$
   \text{StateTransition} \sqsubseteq \exists \text{hasPreState}.\text{State} \land \exists \text{hasPostState}.\text{State}
   $$

3. Temporal alignment of states and transitions:
   $$
   \text{StateTransition}(x) \rightarrow \text{endsBeforeOrMeets}(\text{TemporalExtent}(\text{hasPreState}(x)), \text{TemporalExtent}(\text{hasPostState}(x)))
   $$

4. Events and state transitions have overlapping temporal extents:
   $$
   \text{Event}(x) \land \text{triggers}(x, y) \rightarrow \text{overlaps}(\text{TemporalExtent}(x), \text{TemporalExtent}(y))
   $$

5. States in a hierarchy must belong to the same type of entity:
   $$
   \text{isSubStateOf}(s_1, s_2) \land \text{hasState}(e, s_1) \rightarrow \text{hasState}(e, s_2)
   $$

---

## **3. Competency Questions**
1. **State Queries**:
   - What is the current state of entity X?
   - What are all the states entity X has gone through?

2. **State-Event Relationships**:
   - Which event triggered the state transition for entity X?
   - What transitions were caused by event Y?

3. **Temporal Queries**:
   - How long has entity X been in state Z?
   - Which states overlapped with event Y?

4. **Entity Classification**:
   - Is entity X a stateful entity?
   - What types of entities can have states?

---

## **4. Implementation Notes**
### **OWL Encoding**
The pattern can be encoded in OWL to enable automated reasoning:
- Class axioms for `State`, `Event`, `StatefulEntity`, and `StateTransition`.
- Property axioms for `hasState`, `triggers`, and `hasTemporalExtent`.

### **SHACL Validation**
Define SHACL shapes for:
- Validating that only `StatefulEntities` can have states.
- Ensuring every `StateTransition` has both `hasPreState` and `hasPostState`.
- Checking temporal consistency between states and transitions.

---

## **5. Examples**
### **Example 1: Supply Chain**
- **StatefulEntity**: A container of goods.
- **States**: `ProducedState`, `InTransitState`, `StoredState`.
- **Events**: `TransportEvent`, `StorageEvent`.
- **StateTransition**: `InTransit → Stored` caused by a `StorageEvent`.

### **Example 2: IoT Monitoring**
- **StatefulEntity**: A smart sensor.
- **States**: `OperationalState`, `DamagedState`.
- **Events**: `OverheatEvent`.
- **StateTransition**: `Operational → Damaged` triggered by an `OverheatEvent`.

---

## **6. Comparison to Other Patterns**
The Core State-Event Pattern builds on the Core Event Pattern by explicitly modeling states and transitions. Unlike purely event-centric models, it provides lifecycle representation, enabling richer reasoning about entity dynamics.

---

## **7. Conclusion**
The Core State-Event Pattern is a minimal, extensible framework for modeling dynamic systems. By integrating states and events, it supports lifecycle reasoning, traceability, and causal analysis across diverse domains. Logical refinements ensure consistency and modularity for real-world applications.

---

Would you like assistance in formalizing this pattern in OWL or SHACL or testing it with example data?