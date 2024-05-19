# Defense Supply Chain and Documentation Ontology (DSCDO)

## Development Methodology
**GitHub Integration:** The program leverages GitHub, a widely adopted platform for distributed version control and collaborative development. All ontology files and related documentation are hosted in a dedicated GitHub repository, enabling contributors to propose changes, review modifications, and merge accepted updates seamlessly.

**Pull Request Workflow:** Contributors can fork the main ontology repository, propose changes, and submit pull requests for review. This workflow ensures that all modifications undergo thorough peer review and approval before being merged into the main codebase, maintaining the ontologies' integrity and consistency.

**Semantic Versioning:** The ontology development process adheres to semantic versioning principles, where each version is assigned a unique identifier reflecting the level of change (major, minor, or patch). This practice facilitates clear communication of updates, compatibility tracking, and dependency management across the Knowledge Graph ecosystem.

**Modular Ontology Modeling:** Following the best practices outlined in ["Modular Ontology Modeling" by Cogan Shimizu et al.](https://www.semantic-web-journal.net/system/files/swj2886.pdf), the program adopts a modular approach to ontology development. This involves breaking down complex ontologies into smaller, reusable modules, promoting maintainability, extensibility, and collaborative development. The program embraces the principles of "extreme design" and the use of ontology design patterns, which provide proven solutions to common modeling challenges and promote consistency across the ontology modules. This workflow from requirements stories, though modular pattern-based design through ontology publication is illustrated in Fig 1 from  "Modular Ontology Modeling" included below.

![Modular Ontology Modeling ](img/modular_ontology_modeling.png)

Utilization of GitHub for Workflow Management and FAIR Data Principles Application:
- **Issue Tracking:** GitHub's issue tracking system is employed to manage the ontology development lifecycle, including feature requests, bug reports, and general discussions. This centralized approach ensures transparent communication and collaboration among stakeholders. The property `schema:source` is used to reference the source of the ontology term for example `schema:source <https://github.com/schemaorg/schemaorg/issues/2140>` is used to document the discussion around `3Dmodel` for inclusion in schema.org.
- **Project Boards:** Project boards within GitHub provide a visual representation of the ontology development workflow, allowing for the organization and prioritization of tasks, assignment of responsibilities, and tracking of progress.
- **FAIR Data Principles:** The program emphasizes adhering to the FAIR (Findable, Accessible, Interoperable, and Reusable) data principles throughout the ontology development process. To ensure optimal FAIR compliance, best practices from Daniel Garijo's lear licensing and provenance information. follows ["Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web"](https://arxiv.org/abs/2003.13084v1) and FAIRsFAIR ["D2.5 FAIR Semantics Recommendations Second Iteration"](https://zenodo.org/record/4314321#.YW2XNtnMIeY) are followed. This includes the use of persistent and unique identifiers, rich metadata descriptions, open and standardized formats, and clear licensing and provenance information. 
- **Documentation Generation:** The program leverages [WIDOCO](https://github.com/dgarijo/Widoco), a widely adopted tool for generating comprehensive documentation from ontology files. WIDOCO can be integrated into the GitHub Actions workflow, ensuring that documentation is automatically generated and updated with each commit, promoting transparency and accessibility of ontological resources.
- **Ontology Annotation:** [WIDOCO Annotations](https://github.com/dgarijo/Widoco/blob/master/doc/metadataGuide/guide.md) provide a list of annotation vocabularies that are supported for direct html rendering into the ontology documentation to provide additional context and provenance information. The [Metadata Checklist](https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html) provides a list of best practices for metadata annotation in the ontology documentation. [OPLaX (Ontology Pattern Language eXtended) ontology](https://github.com/stlab-istc-cnr/OPLaX) provide an additional set of annotation properties that support modular ontology development through a design pattern approach.
- **Ontology Diagramming:** [Chowlk Visual Notation](https://chowlk.linkeddata.es/) and [templates for generating](https://github.com/oeg-upm/Chowlk) visual representations of ontologies are used to provide a graphical overview of the ontology structure, classes, and relationships. This visual representation enhances the understanding of the ontology's complexity and facilitates communication among stakeholders. The [diagrams.net](https://app.diagrams.net/) and  [VSCode](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) Chowlk templates. 

## Expressivity

Ontology is modeled using [RDFS-Plus](http://mlwiki.org/index.php/RDFS-Plus) level of automatization with W3C [RDFS Schema](https://www.w3.org/TR/rdf-schema/) and selected W3C [OWL 2 Constructs](https://www.w3.org/TR/owl2-primer/). Additionally, to facilitate alignment and adoption using schema.org level base vocabularies as outlined in the schema.org [developer documentation](https://schema.org/docs/developers.html). This ontology is developed using [Modular Ontology Modeling Methodology](http://www.semantic-web-journal.net/content/modular-ontology-modeling-10) using [Ontology Design Patterns](http://ontologydesignpatterns.org/wiki/Main_Page) connected to form modules that build the larger ontology. Shape Constraints using [W3C Shapes Constraint Language](https://www.w3.org/TR/shacl/) are also provided for graph shape validation as discussed in the [SHACL and OWL](https://spinrdf.org/shacl-and-owl.html) document. Alignments are modeled similarly to the [RealEstateCore](https://github.com/RealEstateCore/rec) ontology that has created [modular alignments](https://github.com/RealEstateCore/rec/tree/master/ontology/alignments) that form the basis for adoption in [Azure Digital Twins](https://docs.microsoft.com/en-us/azure/digital-twins/concepts-ontologies) and cross linking to [Industry Standard Ontologies in a Knowledge Graph](https://docs.microsoft.com/en-us/azure/digital-twins/concepts-ontologies-adopt).

## Testing

Development of MSCDO uses [Github Actions](https://github.com/features/actions) to perform CI/CD of the ontology. It runs a [SHACL](https://www.w3.org/TR/shacl/) test suite against sample knowledge graph fragments using [pyshacl](https://github.com/RDFLib/pySHACL) and the [sharness](https://github.com/chriscool/sharness) [Test Anything Protocol](http://testanything.org). Results can be reviewed in the [actions page](https://github.com/LA3D/ammo/actions) of the AMMO Github repository.

## Persistent Identifiers and Namespace
The following URI structure is proposed for the prototype, similar to w3id.org redirect rule structure https://github.com/perma-id/w3id.org. Content negotiation will be used as part of the redirect rule to provide different serializations (JSON-LD, turtle, etc). It should be noted that this URI structure will likely need to be changed when deployed within a DoD network, and additional URI modeling may be required to capture additional functionality within the DoD networks. An example of this is the [“Adoption and Impact of an Identifier Policy – AstraZeneca”](https://fairtoolkit.pistoiaalliance.org/use-cases/adoption-and-impact-of-an-identifier-policy-astrazeneca/) which illustrates how AstraZeneca 
“…implemented a Uniform Resource Identifiers (URI) policy that describes how URIs need to be constructed to facilitate cross-enterprise Findability, Interoperability and Reuse of digital objects. Significant adoption benefits occur in information domains where one needs to utilize data across multiple sources and where one may not have control over information architecture within these sources. Focus areas taking advantage of this approach include clinical studies, translational medicine and competitive intelligence programs.”

Our minimum viable URI policy for the proposed system is as follows:
| URI Structure                                                    | URI Definition                                                                                   |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| https://schema.e616.crc.nd.edu/                                  | Root URI equivalent to w3id.org                                                                   |
| https://schema.e616.crc.nd.edu/org/                              | Organizational Root for example ND, SIMBA, etc.                                                   |
| https://schema.e616.crc.nd.edu/org/project/                      | Project Root                                                                                      |
| https://schema.e616.crc.nd.edu/org/project/ont/                  | Ontology URI Space                                                                                |
| https://schema.e616.crc.nd.edu/org/project/voc/                  | Vocabulary URI Space                                                                              |
| https://schema.e616.crc.nd.edu/org/project/shapes/               | Shapes Root URI Space to define shape documents used in the project                               |
| https://schema.e616.crc.nd.edu/org/project/shapes/shacl/         | Shapes Root URI for [SHACL](https://www.w3.org/TR/shacl/) encoded shapes                         |
| https://schema.e616.crc.nd.edu/org/project/shapes/shex/          | Shapes Root URI for [SHEX](https://shex.io/) encoded shapes (unused in this project but reserved) |




## Versions

The latest version of the full ontology can be found at https://schema.e616.crc.nd.edu/nd/doc/ont/ and specific release versions can be found at https://schema.e616.crc.nd.edu/nd/doc/ont/ {version number} for example https://schema.e616.crc.nd.edu/nd/doc/ont/0.1.0.

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/crcresearch/earth616_ontology/issues) to request new terms/classes or report errors or specific concerns related to the ontology.

## Acknowledgements

---

## Direct Contact

**Charles Vardeman**  
_Research Assistant Professor_  
[Center for Research Computing](https://crc.nd.edu), [University of Notre Dame](https://nd.edu)  
<cvardema@nd.edu>  
Github: [charlesvardeman](https://github.com/charlesvardeman)  
ORCID: [0000-0003-4091-6059](https://orcid.org/0000-0003-4091-6059)