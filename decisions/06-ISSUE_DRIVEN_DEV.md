# GitHub Issue Driven Development for Ontology Modules and Terms

Discussion: [#6](https://github.com/crcresearch/earth616_ontology/issues/6)

## Status
Accepted

## Decision
We will adopt GitHub Issue Driven Development for managing the development of ontology modules and terms. Each ontology term will be associated with a GitHub issue to document discussions, decisions, and changes related to that term. This approach will provide traceability, transparency, and accountability in the development process.

## Context ##
To adopt best practices in ontology and vocabulary development, we propose using GitHub issues to document and manage the process. Traceable provenance to discussions is crucial for the development and evolution of ontology terms. This approach aligns with the practices used by prominent ontologies such as Schema.org, which utilize similar methods for their vocabulary releases. Associating each vocabulary term with a GitHub issue via the `schema:source` property ensures comprehensive documentation and facilitates efficient collaboration and review processes.


```turtle
@prefix ex: <http://example.org/ontology/> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Define the ontology term
ex:NewTerm a schema:Property ;
    schema:name "New Term" ;
    schema:description "A new term added to the ontology." ;
    schema:source <https://github.com/your-repo/issues/123> ;
    schema:creator <http://example.org/person/JohnDoe> .

# Define the person involved
<http://example.org/person/JohnDoe> a schema:Person ;
    schema:name "John Doe" .
```

## Consequences ##
### Benefits
1. **Improved Collaboration**: GitHub provides a collaborative environment where team members can discuss and review ontology and vocabulary terms in a centralized platform.
2. **Traceability**: Each term's history and discussions can be tracked through GitHub issues, providing clear documentation of changes and decisions.
3. **Integration**: GitHub issues can be integrated with other tools and workflows, facilitating seamless development and project management.
4. **Transparency**: Public repositories on GitHub ensure transparency, allowing external stakeholders to follow the development process and contribute.
5. **Accountability**: Assigning issues to team members increases accountability and clarifies responsibilities.

### Drawbacks
1. **Learning Curve**: Team members unfamiliar with GitHub may require training to use the platform effectively.
2. **Dependency on GitHub**: Relying on GitHub means we are dependent on its availability and features.
3. **Management Overhead**: Properly managing issues and ensuring they are up-to-date adds to the project management workload.

### Consequences
1. **Increased Efficiency**: By centralizing discussions and decisions, we can avoid redundant conversations and streamline the development process.
2. **Enhanced Quality**: Transparent discussions and reviews can lead to better ontology terms and modules.


### Conclusion
By using GitHub issues for ontology and vocabulary development, we aim to enhance collaboration, traceability, and accountability within our team. Despite the learning curve and management overhead, the benefits of a centralized, transparent, and well-documented development process outweigh the drawbacks.