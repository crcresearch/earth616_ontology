# Recommended ontology metadata properties and documentation guidelines #
Discussion: https://github.com/crcresearch/earth616_ontology/issues/9

## Status ##
Proposed

## Decision ## 
Implement the following documentation and metadata guidelines for the ontology:

1. Include the recommended ontology metadata properties from Table 1 in the "Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web" paper as SHACL rules. The required properties are:

- License (dcterms:license)
- Creator (dcterms:creator) 
- Contributor (dcterms:contributor)
- Creation date (dcterms:created) 
- Previous version (owl:priorVersion)
- Namespace URI (vann:preferredNamespaceUri)
- Version IRI (owl:versionIRI) 
- Namespace prefix (vann:preferredNamespacePrefix)
- Title (dcterms:title)
- Description (dcterms:description) 
- Citation (dcterms:bibliographicCitation)

2. Document all Classes and Properties defined by the ontology. For each term, include the recommended properties from Table 2 in the paper:

- Label (rdfs:label)
- Definition (skos:definition) 
- Note (skos:note)
- Example (skos:example)
- Editorial note (skos:editorialNote)
- Change note (skos:changeNote)
- Scope note (skos:scopeNote)

3. Use schema:source to link ontology terms to the GitHub issue where the term was discussed and accepted, for example:

```turtle
ex:MyClass
  a owl:Class ;
  schema:source <https://github.com/my-org/my-ontology/issues/42> .
```

4. Use OPLaX annotations to document ontology design patterns (ODPs) and modules used in the ontology:

- Annotate ODPs using the OPLa-core annotations  
- Document schema diagrams for ODPs using OPLa-SD annotations
- Annotate content ODPs using OPLa-CP
- Use OPLaX to delineate modules within the overall ontology

5. Generate a human-readable HTML documentation of the full ontology using a tool like WIDOCO that creates sections for all classes, properties, data properties, named individuals, and ontology design patterns from the metadata.

## Context ##
Providing recommended metadata about the ontology, having clear definitions and annotations for all ontology terms, linking terms to their GitHub discussions, and documenting ontology design patterns and modular structure is important for making the ontology FAIR (Findable, Accessible, Interoperable, Reusable).

The "Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web" paper provides guidelines on the key metadata properties to include. SKOS provides a rich set of annotation properties for documenting ontologies. schema:source allows linking ontology terms to where they were discussed. OPLaX provides a standard way to annotate ontology design patterns and modules. Adopting these recommendations will align the ontology with community best practices.

## Consequences ##
Requiring the recommended metadata properties, class/property documentation using SKOS, links to GitHub issues, and ODP/module annotations will:

- Improve discoverability by providing key information for ontology catalogs and registries
- Clarify licensing, provenance, and versioning to make the ontology more reusable
- Make the ontology easier to understand and use by providing rich definitions and annotations for all terms
- Allow tracing ontology terms back to their GitHub issue discussions 
- Document the design patterns and modular structure used in the ontology

Ontology editors will need to ensure all the required documentation is included, which will add some additional effort. But overall this will significantly improve the quality and FAIRness of the ontology's documentation and metadata. The generated HTML documentation will make it much easier for users to explore and understand the ontology.

Citations:
[1] [SKOS Reference](https://www.w3.org/TR/skos-reference/)
[2] [SKOS Primer](https://www.w3.org/TR/skos-primer/)
[3] [Syntax for GitHub's form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)
[4][ "Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web" ](https://ar5iv.labs.arxiv.org/html/2003.13084)
[5] [OPLaX (Ontology Pattern Language eXtended) ontology](https://w3id.org/OPLaX/)
[6] [Extensions to the Ontology Design Pattern Representation Language](https://ceur-ws.org/Vol-2459/short2.pdf)
[7] [Extended OPLa Ontology Files](https://github.com/Data-Semantics-Laboratory/Extended-OPLa)