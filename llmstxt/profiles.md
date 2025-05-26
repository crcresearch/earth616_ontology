Title: The Profiles Vocabulary

URL Source: https://www.w3.org/TR/dx-prof/

Markdown Content:
[Jump to Table of Contents](https://www.w3.org/TR/dx-prof/#toc)[Pop Out Sidebar](https://www.w3.org/TR/dx-prof/#toc)

Abstract
--------

The Profiles Vocabulary is an RDF vocabulary created to allow the machine-readable description of profiles of specifications for information resources. It can be used to describe profile hierarchies wherein profiles of specifications may themselves have profiles indicated. It can also link multiple profile resources that make up a profile - guidelines, validation tools, schemas, term lists and so on - to it and allows for those profile resources to be described with formats, roles, and digital artifacts.

The namespace for PROF terms is `http://www.w3.org/ns/dx/prof/`.

 The PROF vocabulary, defined in OWL and encoded in RDF Turtle, is available at [prof.ttl](https://www.w3.org/TR/dx-prof/rdf/prof.ttl).

Status of This Document
-----------------------

_This section describes the status of this document at the time of its publication. Other documents may supersede this document. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at https://www.w3.org/TR/._

This document was published by the [Dataset Exchange Working Group](https://www.w3.org/2017/dxwg/) as a Working Group Note.

[GitHub Issues](https://github.com/w3c/dxwg/issues/) are preferred for discussion of this specification. Alternatively, you can send comments to our mailing list. Please send them to [public-dxwg-comments@w3.org](mailto:public-dxwg-comments@w3.org) ([archives](https://lists.w3.org/Archives/Public/public-dxwg-comments/)).

Publication as a Working Group Note does not imply endorsement by the W3C Membership. This is a draft document and may be updated, replaced or obsoleted by other documents at any time. It is inappropriate to cite this document as other than work in progress.

This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/Consortium/Patent-Policy/).

This document is governed by the [1 March 2019 W3C Process Document](https://www.w3.org/2019/Process-20190301/).

### Overview of DXWG documents on profiles[](https://www.w3.org/TR/dx-prof/#FamilyOfDocs)

This document is one from a set of documents on profiles, edited by the W3C Dataset Exchange Working Group (DXWG) and the Internet Engineering Taskforce (IETF). The documents are:

*   **[DX-PROF] this document, an RDF vocabulary that describes profiles and related resources**
*   [DX-PROF-CONNEG] specific guidance on how to negotiate for Internet resource content using profiles
*   [[DX-PROF-IETF](https://www.w3.org/TR/dx-prof/#bib-dx-prof-ietf "Indicating and Negotiating Profiles in HTTP")] - _Indicating and Negotiating Profiles in HTTP_: an [IETF](http://www.ietf.org/)[Internet-Draft](http://www.ietf.org/standards/ids/) defining HTTP Headers for HTTP content negotiation by profile
*   The DXWG also plans to provide [[DX-PROF-GUIDANCE](https://www.w3.org/TR/dx-prof/#bib-dx-prof-guidance "Profile Guidance")] - Profile Guidance: general recommendations and guidance on profiling.

Table of Contents
-----------------

1.   [1. Introduction](https://www.w3.org/TR/dx-prof/#introduction)
2.   [2. Conformance](https://www.w3.org/TR/dx-prof/#conformance)
    1.   [2.1 Diagram Conventions](https://www.w3.org/TR/dx-prof/#diagramconventions)

3.   [3. Definitions](https://www.w3.org/TR/dx-prof/#definitions)
4.   [4. Namespaces](https://www.w3.org/TR/dx-prof/#namespaces)
5.   [5. Motivation](https://www.w3.org/TR/dx-prof/#motivation)
    1.   [5.1 Motivating Requirements](https://www.w3.org/TR/dx-prof/#motivating-requirements)

6.   [6. Related Work](https://www.w3.org/TR/dx-prof/#relatedwork)
    1.   [6.1 Web Ontology Language (OWL)](https://www.w3.org/TR/dx-prof/#related-owl)
    2.   [6.2 Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/dx-prof/#related-dcat)
    3.   [6.3 Asset Description Metadata Schema (ADMS)](https://www.w3.org/TR/dx-prof/#related-adms)
    4.   [6.4 PROV-O: The PROV Ontology](https://www.w3.org/TR/dx-prof/#related-prov)
    5.   [6.5 The VoID Vocabulary](https://www.w3.org/TR/dx-prof/#related-void)
    6.   [6.6 Vocabulary of a Friend (VOAF)](https://www.w3.org/TR/dx-prof/#related-voaf)
    7.   [6.7 OGC's ModSpec](https://www.w3.org/TR/dx-prof/#related-modspec)
    8.   [6.8 Constraint Languages](https://www.w3.org/TR/dx-prof/#related-constraintlanguages)

7.   [7. Conceptual Model](https://www.w3.org/TR/dx-prof/#conceptualmodel)
    1.   [7.1 Initial Examples](https://www.w3.org/TR/dx-prof/#initial-examples)
    2.   [7.2 Roles Vocabulary](https://www.w3.org/TR/dx-prof/#roles-vocab)

8.   [8. Vocabulary Specification](https://www.w3.org/TR/dx-prof/#specification)
    1.   [8.1 RDF representation](https://www.w3.org/TR/dx-prof/#RDF-representation)
    2.   [8.2 Dependencies](https://www.w3.org/TR/dx-prof/#dependencies)
    3.   [8.3 Class: Profile](https://www.w3.org/TR/dx-prof/#Class:Profile)
        1.   [8.3.1 Property: hasResource](https://www.w3.org/TR/dx-prof/#Property:hasResource)
        2.   [8.3.2 Property: isProfileOf](https://www.w3.org/TR/dx-prof/#Property:isProfileOf)
        3.   [8.3.3 Property: isTransitiveProfileOf](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf)
        4.   [8.3.4 Property: hasToken](https://www.w3.org/TR/dx-prof/#Property:hasToken)

    4.   [8.4 Class: ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor)
        1.   [8.4.1 Property: hasArtifact](https://www.w3.org/TR/dx-prof/#Property:hasArtifact)
        2.   [8.4.2 Property: dct:conformsTo](https://www.w3.org/TR/dx-prof/#Property:conformsTo)
        3.   [8.4.3 Property: dct:format](https://www.w3.org/TR/dx-prof/#Property:format)
        4.   [8.4.4 Property: hasRole](https://www.w3.org/TR/dx-prof/#Property:hasRole)
        5.   [8.4.5 Property: isInheritedFrom](https://www.w3.org/TR/dx-prof/#Property:isInheritedFrom)

    5.   [8.5 Class: ResourceRole](https://www.w3.org/TR/dx-prof/#Class:ResourceRole)

9.   [9. Resource Role Instances](https://www.w3.org/TR/dx-prof/#resource-roles-vocab)
    1.   [9.1 Resource Role: Constraints](https://www.w3.org/TR/dx-prof/#Role:constraints)
    2.   [9.2 Resource Role: Example](https://www.w3.org/TR/dx-prof/#Role:example)
    3.   [9.3 Resource Role: Guidance](https://www.w3.org/TR/dx-prof/#Role:guidance)
    4.   [9.4 Resource Role: Mapping](https://www.w3.org/TR/dx-prof/#Role:mapping)
    5.   [9.5 Resource Role: Schema](https://www.w3.org/TR/dx-prof/#Role:schema)
    6.   [9.6 Resource Role: Specification](https://www.w3.org/TR/dx-prof/#Role:specification)
    7.   [9.7 Resource Role: Validation](https://www.w3.org/TR/dx-prof/#Role:validation)
    8.   [9.8 Resource Role: Vocabulary](https://www.w3.org/TR/dx-prof/#Role:vocabulary)

10.   [10. Examples](https://www.w3.org/TR/dx-prof/#examples)
    1.   [10.1 DCAT-AP](https://www.w3.org/TR/dx-prof/#eg-dcat-ap)
    2.   [10.2 DCAT-AP hierarchy](https://www.w3.org/TR/dx-prof/#eg-hierarchy)
    3.   [10.3 CSIRO Dummy Dublin Core AP](https://www.w3.org/TR/dx-prof/#eg-csiro-dummy-dcap)
    4.   [10.4 Geoscience Australia's Profile of ISO19115-1:2014](https://www.w3.org/TR/dx-prof/#eg-ga)
    5.   [10.5 Asset Description Metadata Schema](https://www.w3.org/TR/dx-prof/#eg-adms)

11.   [11. Test Suite](https://www.w3.org/TR/dx-prof/#testsuite)
12.   [12. Implementations](https://www.w3.org/TR/dx-prof/#implementations)
13.   [13. Alignments](https://www.w3.org/TR/dx-prof/#alignments)
    1.   [13.1 Dataset Catalogue Vocabulary](https://www.w3.org/TR/dx-prof/#alignment-dcat)
    2.   [13.2 Asset Description Metadata Schema](https://www.w3.org/TR/dx-prof/#alignment-adms)
    3.   [13.3 Dublin Core Terms](https://www.w3.org/TR/dx-prof/#alignment-dct)
    4.   [13.4 Web Ontology Language](https://www.w3.org/TR/dx-prof/#alignment-owl)
    5.   [13.5 Vocabulary of a Friend](https://www.w3.org/TR/dx-prof/#alignment-voaf)
    6.   [13.6 OGC/ISO Modular Specification](https://www.w3.org/TR/dx-prof/#alignment-modspec)
    7.   [13.7 Simple Knowledge Organization System](https://www.w3.org/TR/dx-prof/#alignment-skos)

14.   [14. Security and Privacy](https://www.w3.org/TR/dx-prof/#security_and_privacy)
15.   [15. Changes](https://www.w3.org/TR/dx-prof/#changes)
    1.   [15.1 Changes since last Public Draft](https://www.w3.org/TR/dx-prof/#changes-since-2pwd)
    2.   [15.2 Features at risk](https://www.w3.org/TR/dx-prof/#features-at-risk)

16.   [A. Appendices](https://www.w3.org/TR/dx-prof/#appendices)
    1.   [A.1 Acknowledgements](https://www.w3.org/TR/dx-prof/#acknowledgements)
    2.   [A.2 Issue Summary](https://www.w3.org/TR/dx-prof/#issue-summary)

17.   [B. References](https://www.w3.org/TR/dx-prof/#references)
    1.   [B.1 Normative references](https://www.w3.org/TR/dx-prof/#normative-references)
    2.   [B.2 Informative references](https://www.w3.org/TR/dx-prof/#informative-references)

1. Introduction[](https://www.w3.org/TR/dx-prof/#introduction)
--------------------------------------------------------------

_This section is non-normative._

This Profiles Vocabulary (PROF) provides a standardized, structured and human- & machine-readable set of terms to describe profiles. Its development was triggered by the appearance of multiple profiles of the Dataset Catalog Vocabulary (DCAT) [[VOCAB-DCAT](https://www.w3.org/TR/dx-prof/#bib-vocab-dcat "Data Catalog Vocabulary (DCAT)")] and examples of profile description and implementation guidance systems such as the Guidelines for Dublin Core Application Profiles [[DCAP](https://www.w3.org/TR/dx-prof/#bib-dcap "Guidelines for Dublin Core Application Profiles")] and the OpenGeospatial Consortium's Standard for Modular specifications [[MODSPEC](https://www.w3.org/TR/dx-prof/#bib-modspec "The Specification Model — A Standard for Modular specifications")].

Profiles aim to increase interoperability within a community of users by introducing constraints, extensions or combinations on the use of more general specifications. PROF is an RDF vocabulary created to describe relations between [specifications](https://www.w3.org/TR/dx-prof/#dfn-specification) and [profiles](https://www.w3.org/TR/dx-prof/#dfn-profile) and the profile resources that define and implement profiles. A _specification_ is "A basis for comparison; a reference point against which other things can be evaluated." (see the definition below) and a _profile_, perhaps an _application profile_, is defined as "A [data/application] specification that constrains, extends, combines, or provides guidance or explanation about the usage of other [data/application] specifications". Profile resources may be human-readable documents (PDFs, textual documents), vocabularies, schemas or ontologies (XSD, RDF), constraint language resources used by specific validation tools (SHACL, ShEx, Schematron), or any other files or profile resources that support the profile. In this specification, each profile resource is able to have roles assigned to it that define its functions within the profile.

This vocabulary's ontological basis for specification/profile relations is a specialization of the `dct:Standard` class which is defined here as a `prof:Profile`. A `prof:Profile` instance is related to either `dct:Standard` or `prof:Profile` instances by being a _profile of_ them, formally, [`prof:isProfileOf`](https://www.w3.org/TR/dx-prof/#Property:isProfileOf). Resources that conform to either a `dct:Standard` or a `prof:Profile` are formally described as doing so with the use of the `dct:conformsTo` predicate.

Data that conforms to a profile, in PROF, must conform to anything the profile is a profile of. To represent this formally, this vocabulary includes the property chain axiom `dct:conformsTo owl:propertyChainAxiom ( prof:isProfileOf dct:conformsTo )`. Individual communities may define what conformance to their profiles and the things they profile means and how to test for conformance if indeed they wish to.

In recognition of the existence of specifications and profiles that are made up of multiple resources – perhaps PDF documents, machine-readable constraint language files, code lists etc. – this vocabulary also provides for the description of the parts that constitute a profile or a specification. It defines a [`prof:ResourceDescriptor`](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) class which is used to qualify the relationship between a profile and profile resources. A `prof:Profile` may have any number of [`prof:hasResource`](https://www.w3.org/TR/dx-prof/#Property:hasResource) predicates indicating `prof:ResourceDescriptor` instances which then indicate the location (a URI) of the actual profile resource artifact with a [`prof:hasArtifact`](https://www.w3.org/TR/dx-prof/#Property:hasArtifact) predicate and then may describes the artifact's format and any specifications it conforms to with [`dct:format`](https://www.w3.org/TR/dx-prof/#Property:format)&[`dct:conformsTo`](https://www.w3.org/TR/dx-prof/#Property:conformsTo) predicates respectively. The role that the profile resource plays with respect to the profile may be indicating using a [`prof:ResourceRole`](https://www.w3.org/TR/dx-prof/#Class:ResourceRole) class instance linked to it with the [`prof:hasRole`](https://www.w3.org/TR/dx-prof/#Property:hasRole) predicate.

A vocabulary of `prof:ResourceRole` instances is provided in [§9. Resource Role Instances](https://www.w3.org/TR/dx-prof/#resource-roles-vocab) but communities are encouraged to create additional `prof:ResourceRole` instances with definitions suited to their purposes and, in the best case, to publish those additional instances for others to reuse.

2. Conformance[](https://www.w3.org/TR/dx-prof/#conformance)
------------------------------------------------------------

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key word _MAY_ in this document is to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://www.w3.org/TR/dx-prof/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")] [[RFC8174](https://www.w3.org/TR/dx-prof/#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")] when, and only when, they appear in all capitals, as shown here.

For the purpose of compliance, the normative sections of this document are:

*   [§7. Conceptual Model](https://www.w3.org/TR/dx-prof/#conceptualmodel),
*   [§8. Vocabulary Specification](https://www.w3.org/TR/dx-prof/#specification)&
*   [§11. Test Suite](https://www.w3.org/TR/dx-prof/#testsuite).

### 2.1 Diagram Conventions[](https://www.w3.org/TR/dx-prof/#diagramconventions)

All diagrams in this specification, apart from [Figure 4](https://www.w3.org/TR/dx-prof/#fig-skos-4.5.2 "Inferring a transitive hierarchy from asserted skos:broader statements. Dotted arrows represent statements inferred from the SKOS data model. Solid arrows represent asserted statements. Reproduction of Figure 4.5.2 in [SKOS-PRIMER]"), use elements defined in this key. The namespace prefixes in the key are defined in [§4. Namespaces](https://www.w3.org/TR/dx-prof/#namespaces).

[![Image 1: Diagram's element key](https://www.w3.org/TR/dx-prof/figures/element-key.svg)](https://www.w3.org/TR/dx-prof/figures/element-key.svg)

Figure 1 A key of the elements used in this specification's diagrams

3. Definitions[](https://www.w3.org/TR/dx-prof/#definitions)
------------------------------------------------------------

specification
A basis for comparison; a reference point against which other things can be evaluated.

_Source: DCMI Metadata Terms [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")]'s definition for a `Standard`._

data specification
A [specification](https://www.w3.org/TR/dx-prof/#dfn-specification), with human- and/or machine-processable representations, that defines the content and structure of data used in a given context.

data profile
A data specification that constrains, extends, combines, or provides guidance or explanation about the usage of other data specifications.

This definition includes what are sometimes called "application profiles", "metadata application profiles", or "metadata profiles". In this document, "data profile" and these other variants are all referred to as just "profiles".

data resource An entity is identified by a URI. Familiar examples include an electronic document, an image, a source of information with a consistent purpose. [[RFC3986](https://www.w3.org/TR/dx-prof/#bib-rfc3986 "Uniform Resource Identifier (URI): Generic Syntax")] metadata Information that is supplied about a resource. [[RFC3986](https://www.w3.org/TR/dx-prof/#bib-rfc3986 "Uniform Resource Identifier (URI): Generic Syntax")]token
A short name identifying something.

In the context of this specification, it is a [profile](https://www.w3.org/TR/dx-prof/#dfn-profile) that is usually identified by a token.

4. Namespaces[](https://www.w3.org/TR/dx-prof/#namespaces)
----------------------------------------------------------

The namespace for PROF is **`http://www.w3.org/ns/dx/prof/`**, however, PROF makes use of terms from other vocabularies, in particular Dublin Core [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")]. PROF itself only defines a small set of classes and properties of its own.

PROF also makes use of derivative namespaces of its own namespace for auxiliary vocabulary elements, such as instances of the `prof:ResourceRole` which are within the `http://www.w3.org/ns/dx/prof/role/` namespace.

A full set of namespaces and prefixes used in this specification is given in the table below.

| Prefix | Namespace |
| --- | --- |
| dcat | http://www.w3.org/ns/dcat# |
| dct | http://purl.org/dc/terms/ |
| owl | http://www.w3.org/2002/07/owl# |
| **prof** | **[http://www.w3.org/ns/dx/prof/](https://www.w3.org/ns/dx/prof/)** |
| role | http://www.w3.org/ns/dx/prof/role/ |
| prov | http://www.w3.org/ns/prov# |
| rdf | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs | http://www.w3.org/2000/01/rdf-schema# |
| skos | http://www.w3.org/2004/02/skos/core# |
| xsd | http://www.w3.org/2001/XMLSchema# |
| (others) | All other namespace prefixes are used in examples only. In particular, IRIs starting with "http://example.org" represent some application-dependent IRI [[RFC3987](https://www.w3.org/TR/dx-prof/#bib-rfc3987 "Internationalized Resource Identifiers (IRIs)")] |

5. Motivation[](https://www.w3.org/TR/dx-prof/#motivation)
----------------------------------------------------------

_This section is non-normative._

Until this vocabulary's creation, there was no formal W3C method for describing [profile](https://www.w3.org/TR/dx-prof/#dfn-profile) objects (Internet resources).

There are a multitude of possible ways to describe the components needed to define a profile and support validation of data claiming conformance to profiles, such as:

*   human-readable documents stating requirements (e.g. [[PDF](https://www.w3.org/TR/dx-prof/#bib-pdf "Document management -- Portable document format -- Part 1: PDF 1.7")]) 
*   usage and guidance notes
*    machine readable constraint languages (e.g. the abstract (Dublin Core's Description Set Profiles [[DCDSP](https://www.w3.org/TR/dx-prof/#bib-dcdsp "Description Set Profiles: A constraint language for Dublin Core Application Profiles")]) or the more concrete (SHACL [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")] & ShEx [[SHEX](https://www.w3.org/TR/dx-prof/#bib-shex "Shape Expressions Language 2.next")]). 

Describing the components within a profile with documents or constraint languages only does not indicate many things that may be important or interesting to know about a profile such as:

*   its dependence on standards or other profiles
*   inheritance of profile information from the things being profiled, or
*   related profile resources 
    *    guidance documents in addition to formal constraints 
    *    equivalent constraints written in different constraint languages for different forms of profile resource, e.g. SHACL for RDF and Schematron [[SCHEMATRON](https://www.w3.org/TR/dx-prof/#bib-schematron "ISO/IEC 19757-3:2016 Information technology -- Document Schema Definition Languages (DSDL) -- Part 3: Rule-based validation -- Schematron")] for XML. 
    *    supporting vocabularies of terms (code lists) 

Regarding profile/specification relations, a mechanism to relate profiles to specifications and other profiles, would allow both immediate knowledge of what things a profile profiles and also allow profile hierarchies to be established which could:

*    assist with the reuse of existing profiles 
    *    one can profile another profile, adding a small set of additional constraints and declaring compatibility with all profiled specifications. 
    *    reducing the total effort and information necessary to specify a profile 

*    allow for machine interpretation of profiles and automated profile negotiation with fallback options 
    *    if a client requests a profile which a server cannot deliver, a server may be able to instead deliver a more generic version of the requested data resource, using a profile link to the thing it profiles 
    *    a client may be able to generate a request that already indicates acceptable fallback options for data resources when the primary requested profile is unavailable 

### 5.1 Motivating Requirements[](https://www.w3.org/TR/dx-prof/#motivating-requirements)

For the purposes of dataset exchange and with the lack of a formal W3C method for describing the objects related to profiles, the DXWG undertook a process of Use Case and Requirements gathering. They established the [Dataset Exchange Use Case and Requirements](https://www.w3.org/TR/dcat-ucr/) document (the UCR document) [[DCAT-UCR](https://www.w3.org/TR/dx-prof/#bib-dcat-ucr "Dataset Exchange Use Cases and Requirements")] which groups requirements for profiles into the following sections:

*   [6.10 Profiles — abstract requirements applying to the general definition of profiles](https://www.w3.org/TR/dcat-ucr/#ProfileAbstractRequirements)
*   [6.11 Profiles — Profile functionality](https://www.w3.org/TR/dcat-ucr/#ProfileFunctionalityRequirements)
*   [6.12 Profiles — Profile distributions](https://www.w3.org/TR/dcat-ucr/#ProfileDistributionRequirements)
*   [6.13 Profiles — Profile metadata](https://www.w3.org/TR/dcat-ucr/#ProfileMetadataRequirements)

PROF addresses many of those Requirements – those that can be addressed by describing profile components and relations – and those Requirements link back to the Use Cases that motivated them.

The UCR document lists a further profiles Requirements section: [6.14 Profile and content negotiation](https://www.w3.org/TR/dcat-ucr/#ProfileNegotiationRequirements) however those are not addressed here but by the related [[DX-PROF-CONNEG](https://www.w3.org/TR/dx-prof/#bib-dx-prof-conneg "Content Negotiation by Profile")] document.

7. Conceptual Model[](https://www.w3.org/TR/dx-prof/#conceptualmodel)
---------------------------------------------------------------------

[![Image 2: Vocabulary overview diagram](https://www.w3.org/TR/dx-prof/figures/prof.svg)](https://www.w3.org/TR/dx-prof/figures/prof.svg)

Figure 2 OWL [[OWL2-OVERVIEW](https://www.w3.org/TR/dx-prof/#bib-owl2-overview "OWL 2 Web Ontology Language Document Overview (Second Edition)")] overview diagram of this vocabulary

This vocabulary is for describing relationships between standards/specifications, profiles of them and supporting artifacts such as validating resources.

The model takes the `dct:Standard` Class as a starting point and defines a specialization, a `Profile`, which is a `dct:Standard` that _profiles_ a `dct:Standard` or another `Profile`. `Standards`s or `Profile`s can have `Resource Descriptor`s associated with them that define rules for implementation, provide guidance on how to implement, or play some other role. `Resource Descriptor`s must indicate the role they play (to guide, to validate etc.), the formalism they adhere to (`dct:format`) and any `dct:Standard` that they themselves conform to (`dct:conformsTo`).

Any `rdfs:Resource`_MAY_ indicate conformance to a profile as per [Example 2](https://www.w3.org/TR/dx-prof/#eg-conformance-to-profile) by using `dct:conformsTo`. Individual communities _MAY_ determine what constitutes an appropriate URI to identify a profile.

_The remainder of this section is informative._

### 7.1 Initial Examples[](https://www.w3.org/TR/dx-prof/#initial-examples)

The example below illustrates the use of most parts of PROF and indicates how non-PROF profile metadata is stored alongside PROF metadata.

[![Image 3: An example profile of Dublin Core Terms](https://www.w3.org/TR/dx-prof/figures/initial.svg)](https://www.w3.org/TR/dx-prof/figures/initial.svg)

Figure 3 A full example profile described using common metadata and the Profiles Vocabulary 

[Example 1](https://www.w3.org/TR/dx-prof/#eg-initial-example)
: A full example described using PROF in RDF (turtle)

@prefix dct: <http://purl.org/dc/terms/> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix role: <http://www.w3.org/ns/dx/prof/role/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/profile/x>  # a Profile; it's identifying URI
  a prof:Profile ;

  # common metadata for the Profile

  # the Profile's label
  rdfs:label "Profile X" ;

  # regular metadata, a basic description of the Profile
  rdfs:comment """This is a Profile of Dublin Core Terms used to describe items in
CSIRO's publications catalogue."""@en ;

  # regular metadata, URI of publisher
  dct:publisher <http://catalogue.linked.data.gov.au/org/O-000886> ;

  # PROF metadata

  # this is a profile of Dublin Core Terms, referenced by its namespace
  prof:isProfileOf <http://purl.org/dc/terms/> ;

  # this profile has a SHACL profile resource that constrains it's use of Dublin Core
  prof:hasResource [
    a prof:ResourceDescriptor ;

    # it's in Turtle format
    dct:format <https://w3id.org/mediatype/text/turtle> ;

    # it conforms to SHACL, here refered to by its namespace URI as a Profile
    dct:conformsTo <https://www.w3.org/TR/shacl/> ;

    # this profile resource plays the role of "Validation"
    # described in this ontology's accompanying Roles vocabulary
    prof:hasRole role:Validation ;

    # this profile resource's actual file
    prof:hasArtifact <http://example.org/profile/x/resource/validator.ttl>
  ] ;

  # other profile resources this profile contains
  prof:hasResource ... ;

  # a short code to refer to the Profile with when a URI can't be used
  prof:hasToken "profx"
.

The following example demonstrates how data resources can indicate conformance to a profile. Note that in [Example 1](https://www.w3.org/TR/dx-prof/#eg-initial-example), there is also an example of this pattern whereby the `ResourceDescriptor` is indicated as conforming to the [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")] specification, which is also understood to be a profile to which things may conform.

[Example 2](https://www.w3.org/TR/dx-prof/#eg-conformance-to-profile)
: An example demonstrating how data resources can indicate conformance to profiles.

# Profile X
**<http://example.org/profile/x> a prof:Profile** ;
      dct:title "Profile X" .

# A data resource indicating conformance to Profile X.
# In this example it's a DCAT Dataset's Distribution
<http://example.org/dataset/001>
      a dcat:Dataset ;
      dcat:distribution :dataset-001-x .

:dataset-001-x
      a dcat:Distribution ;
      dct:title "Distribution of imaginary dataset 001 that conforms to Profile X" ;
      dcat:downloadURL <http://www.example.org/files/001.x> ;
      **dct:conformsTo <http://example.org/profile/x>** .

This next example shows how a conclusion about conformance can be drawn due to this vocabulary's inclusion of a property chain axiom about conformance.

[Example 3](https://www.w3.org/TR/dx-prof/#eg-conformance-axiom)
: Demonstrating conformance via the vocabulary's dct:conformsTo/prof:isProfileOf property chain.

# Profile X, is a profile of Specification Y
<http://example.org/profile/x> a prof:Profile ;
      prof:isProfileOf <http://example.org/specification/y>
      dct:title "Profile X" .

# A data resource indicating conformance to Profile X is given
<http://example.org/resource/a>
      dct:conformsTo <http://example.org/profile/x> .

# Due to the property chain axiom:
# dct:conformsTo owl:propertyChainAxiom ( prof:isProfileOf dct:conformsTo )
# the data resource above can be inferred to conform to Specification Y
<http://example.org/resource/a>
      **dct:conformsTo <http://example.org/specification/y>** .  # this triple is inferred

### 7.2 Roles Vocabulary[](https://www.w3.org/TR/dx-prof/#roles-vocab)

A starting point vocabulary of `Resource Role` instances that is expected to be extended by implementers of PROF to suite specialised needs is provided within this vocabulary in [§9. Resource Role Instances](https://www.w3.org/TR/dx-prof/#resource-roles-vocab).

8. Vocabulary Specification[](https://www.w3.org/TR/dx-prof/#specification)
---------------------------------------------------------------------------

### 8.1 RDF representation[](https://www.w3.org/TR/dx-prof/#RDF-representation)

The PROF vocabulary is available in RDF via the vocabulary namespace (`https://www.w3.org/ns/dx/prof/`). Alongside the primary artifact, there is a set of other RDF files that provide additional information, including:

1.    alignments to other vocabularies, some of which are normative, and others which are for guidance only 
2.    additional axioms, which can be useful in some contexts 
3.    validating graphs using [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")] 

These other artifacts are linked to throughout this document.

### 8.2 Dependencies[](https://www.w3.org/TR/dx-prof/#dependencies)

This vocabulary makes use of [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")] properties `conformsTo`&`format` in its normative specification.

### 8.3 Class: Profile[](https://www.w3.org/TR/dx-prof/#Class:Profile)

| [OWL Class](https://www.w3.org/TR/owl-syntax/#Classes) | [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile) |
| --- | --- |
| Label: | Profile |
| Definition: | A specification that constrains, extends, combines, or provides guidance or explanation about the usage of other specifications. This definition includes what are sometimes called "application profiles", "metadata application profiles", or "metadata profiles". |
| Sub class of: | [dct:Standard](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-Standard) |
| Source: | [https://www.w3.org/2017/dxwg/wiki/ProfileContext](https://www.w3.org/2017/dxwg/wiki/ProfileContext) |
| Usage Note: | The Profile class "may be used to model aspects of data structure and content (as per [profile](https://www.w3.org/TR/dx-prof/#dfn-profile)) or any other declared behaviour where a base specification can be identified and further requirements asserted. |

#### 8.3.1 Property: hasResource[](https://www.w3.org/TR/dx-prof/#Property:hasResource)

| RDF Property: | [prof:hasResource](https://www.w3.org/TR/dx-prof/#Property:hasResource) |
| --- | --- |
| OWL type: | [owl:ObjectProperty](https://www.w3.org/TR/owl2-rdf-based-semantics/#table-axiomatic-properties) |
| Label: | has resource |
| Definition: | A resource which describes the nature of an artifact and the role it plays in relation to the Profile |
| Range: | [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) |

#### 8.3.2 Property: isProfileOf[](https://www.w3.org/TR/dx-prof/#Property:isProfileOf)

| RDF Property: | [prof:isProfileOf](https://www.w3.org/TR/dx-prof/#Property:isProfileOf) |
| --- | --- |
| OWL type: | [owl:ObjectProperty](https://www.w3.org/TR/owl2-rdf-based-semantics/#table-axiomatic-properties) |
| Label: | is profile of |
| Definition: | A specification for which this Profile defines constraints, extensions, or which it uses in combination with other specifications, or provides guidance or explanation about its usage |
| Sub property of: | [prof:isTransitiveProfileOf](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf) |
| Domain: | [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile) |
| Range: | [dct:Standard](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-Standard) |
| Usage Note: | A Profile may define constraints on the usage of one or more specifications. All constraints of these specifications are inherited, in the sense that an object conforming to a profile conforms to all the constraints specified the targets of prof:isProfileOf relations. This property is optional, allowing any specification to be declared at the root of a profile hierarchy using the Profile class. Note that the axiom within this vocabulary that allows the inference that conformance to a profile means conformance to anything it profiles is part of the definition `§ 8.4.2 Property: dct:conformsTo`. The use of this prof:isTransitiveProfileOf as a super-property of prof:isProfileOf allows communities of practice to exploit transitive interpretations of hierarchical network of profiles as they see fit, while not interfering with the semantics of prof:isProfileOf, which cannot enforce such transitivity. Intuitively, one can interpret prof:isProfileOf statements as explicitly asserted direct profiling links, while prof:isTransitiveProfileOf is used to reflect more-general (and possibly indirect) ancestor relationships. |

#### 8.3.3 Property: isTransitiveProfileOf[](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf)

| RDF Property: | [prof:isTransitiveProfileOf](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf) |
| --- | --- |
| OWL type: | [owl:ObjectProperty](https://www.w3.org/TR/owl2-rdf-based-semantics/#table-axiomatic-properties) |
| Label: | is a transitive profile of |
| Definition: | A specification this Profile conforms to |
| Super property of: | [prof:isProfileOf](https://www.w3.org/TR/dx-prof/#Property:isProfileOf) |
| Domain: | [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile) |
| Range: | [dct:Standard](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-Standard) |
| Usage note: | This is a convenience property that may be used to access all specifications (including other profiles) that could provide useful information and related resources for the Profile (for example, for better identifying conformance requirements). This avoids forcing clients to traverse a profile hierarchy to find all relevant resources. If this property is used, then all such relationships should be present so a client can safely avoid hierarchy traversal. |

Note: Explanation of profiling transitivity

The property [prof:isTransitiveProfileOf](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf) defined here performs a role similar to that of the property [skos:broaderTransitive](https://www.w3.org/TR/skos-reference/#semantic-relations) defined in [[SKOS-REFERENCE](https://www.w3.org/TR/dx-prof/#bib-skos-reference "SKOS Simple Knowledge Organization System Reference")]. That property "...allows communities of practice to exploit transitive interpretations of hierarchical networks..." while freeing the simpler hierarchy property of [skos:broader](https://www.w3.org/TR/skos-reference/#semantic-relations) from having to enforce transitivity which would prevent broader but non-transitive relationships.

Figure 4.5.2 from [[SKOS-PRIMER](https://www.w3.org/TR/dx-prof/#bib-skos-primer "SKOS Simple Knowledge Organization System Primer")], reproduced below, illustrates the general principle of use of `skos:broaderTransitive`.

![Image 4: Figure 4.5.1 from the SKOS Primer WG Note](https://www.w3.org/TR/dx-prof/figures/broaderTransitive.jpg)

Figure 4 Inferring a transitive hierarchy from asserted skos:broader statements. Dotted arrows represent statements inferred from the SKOS data model. Solid arrows represent asserted statements. Reproduction of Figure 4.5.2 in [[SKOS-PRIMER](https://www.w3.org/TR/dx-prof/#bib-skos-primer "SKOS Simple Knowledge Organization System Primer")] 

This vocabulary defines [prof:isTransitiveProfileOf](https://www.w3.org/TR/dx-prof/#Property:isTransitiveProfileOf) to allow for the transitive interpretations of hierarchies of Profiles (of other Profiles and Standards) while freeing the simpler property, [prof:isProfileOf](https://www.w3.org/TR/dx-prof/#Property:isProfileOf) from having to enforce transitivity.

While this vocabulary provides this `prof:isProfileOf`&`prof:isTransitiveProfileOf` pair of properties, it does not specify how a particular implementation of a Profile that is related to another Profile or Standard by `prof:isTransitiveProfileOf` should implement specific inferences.

Inference based on `prof:isTransitiveProfileOf` will be more complex than inference based on `skos:broaderTransitive` due to Profiles being complex objects relative to SKOS Concepts.

[![Image 5: Property isTransitiveProfileOf in use](https://www.w3.org/TR/dx-prof/figures/isTransitiveProfileOf.svg)](https://www.w3.org/TR/dx-prof/figures/isTransitiveProfileOf.svg)

Figure 5 Property isTransitiveProfileOf in use. See the full explanation in the example text below.

[Example 4](https://www.w3.org/TR/dx-prof/#eg-isTransitiveProfileOf)
: Property isTransitiveProfileOf in use

# A profile that is within a hierarchy of profiles may wish to indicate it profiles
# things "further up the chain". To do this, prof:isTransitiveProfileOf can be used
# to indicate anything the profile is related to by a series of one or more
# prof:isProfileOf properties.

# Here the New Zealand profile of the ISO addressing standard is presented in a chain
# of profiles:

@prefix dct: <http://purl.org/dc/terms/> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix role: <http://www.w3.org/ns/dx/prof/role/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://linked.data.gov.au/def/iso19160-1-address-nz-profile>
  a prof:Profile ;
  rdfs:label "New Zealand Profile of ISO19160-1" ;
  rdfs:comment """This is a country-specific profile of the international
                  addressing standard, ISO19160-1:2015 (Address)""" ;
  prof:isProfileOf <http://linked.data.gov.au/def/iso19160-1-address> .

# The ISO thing that the NZ Profile profiles is actually a Web Ontology Language
# (OWL) version of the original ISO addressing standard
<http://linked.data.gov.au/def/iso19160-1-address>
  a prof:Profile ;
  rdfs:label "OWL Profile of ISO19160-1" ;
  rdfs:comment """This profile profiles both ISO19160-1 (Addressing) and also
                  the Web Ontology Language (OWL)""" ;
  prof:isProfileOf <https://www.iso.org/standard/61710.html> ,
                   <http://www.w3.org/2002/07/owl#> .

<https://www.iso.org/standard/61710.html>
  a dct:Standard ;
  rdfs:label "ISO 19160-1:2015 Addressing -- Part 1: Conceptual model" .

# Now, according to the semantics of prof:isTransitiveProfileOf, using the
# prof:isProfileOf statements above, one can infer the following additional
# statements:

<http://linked.data.gov.au/def/iso19160-1-address-nz-profile>
  prof:isTransitiveProfileOf <http://linked.data.gov.au/def/iso19160-1-address> ,
                             <https://www.iso.org/standard/61710.html> ,
                             <http://www.w3.org/2002/07/owl#> .

# These statements may help consumers understand which broad, well-known
# profiles data they have conforms to when they are presented only with its
# conformance to most specialised (lowest) profile in a hierarchy which they
# may not understand.

# In this example too, a user of the profile
# <http://linked.data.gov.au/def/iso19160-1-address-nz-profile> will also
# understand that data conforming to it is also conformant with OWL which is not
# in the direct hierarchy of addressing standards (iso19160-1-address-nz-profile >
# iso19160-1-address > ISO 19160-1:2015) but is critical to know about when using
# the specialised standard as it can indicate reasoning possibilities.

#### 8.3.4 Property: hasToken[](https://www.w3.org/TR/dx-prof/#Property:hasToken)

| RDF Property: | [prof:hasToken](https://www.w3.org/TR/dx-prof/#Property:hasToken) |
| --- | --- |
| OWL type: | [owl:DatatypeProperty](https://www.w3.org/TR/owl2-rdf-based-semantics/#table-axiomatic-datatypes) |
| Label: | has token |
| Definition: | The preferred identifier for the Profile, for use in circumstances where its URI cannot be used. |
| Domain: | [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile) |
| Range: | [xsd:token](https://www.w3.org/TR/xmlschema-2/#token) |
| Usage note: | A simple lexical form of identifier that may be accepted in some circumstances, such as API arguments or in content negotiation, to reference a profile. This is a “preferred term”, since alternative identifiers may be declared and used by any implementation |

### 8.4 Class: ResourceDescriptor[](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor)

The Resource Descriptor class' name may not convey its intention well. This name needs to be reconsidered with discussion about it here.

| [OWL Class](https://www.w3.org/TR/owl-syntax/#Classes) | [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) |
| --- | --- |
| Label: | Resource Descriptor |
| Definition: | A resource that defines an aspect - a particular part or feature - of a Profile |
| Usage note: | Used to indicate the formalism (via dct:format) and any adherence to a dct:Standard (via dct:conformsTo) to allow for machine mediation as well as its purpose via relation to a ResourceRole (via hasRole) |

#### 8.4.1 Property: hasArtifact[](https://www.w3.org/TR/dx-prof/#Property:hasArtifact)

| RDF Property: | [prof:hasArtifact](https://www.w3.org/TR/dx-prof/#Property:hasArtifact) |
| --- | --- |
| Label: | has artifact |
| Definition: | The URL of a downloadable file with particulars such as its format and role indicated by the Resource Descriptor |
| Domain: | [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) |
| Usage Note: | A property to link from a Resource Descriptor to an actual information resource (rdfs:Resource; an individual) that implements it |

#### 8.4.2 Property: dct:conformsTo[](https://www.w3.org/TR/dx-prof/#Property:conformsTo)

_This property is from the [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")] specification however the property chain axiom declared here is new in PROF._

| RDF Property: | [dct:conformsTo](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-conformsTo) |
| --- | --- |
| Label: | Conforms To |
| Definition: | An established standard to which the described resource conforms |
| Sub property of: | [dct:relation](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-relation) |
| Property Chain Axiom: | `owl:propertyChainAxiom ( prof:isProfileOf dct:conformsTo )` |
| Usage note: | This property is to be used to show conformance of a data resource to a specification (`dct:Standard`) or a profile (`prof:Profile`). The property chain axiom declared for this property means that if the thing conformed to is a profile of something else (indicated by `prof:isProfileOf`), then the conforming data resource will be inferred to be conformant to that other thing too. PROF does not specify the nature of conformance: communities using [specifications](https://www.w3.org/TR/dx-prof/#dfn-specification) and [profiles](https://www.w3.org/TR/dx-prof/#dfn-profile) are free to define appropriate conformance for their purposes. |

The property chain axiom `dct:conformsTo owl:propertyChainAxiom ( prof:isProfileOf dct:conformsTo ) ;` is a "feature at risk" until discussion about its inclusion in PROF has reached a conclusion.

#### 8.4.3 Property: dct:format[](https://www.w3.org/TR/dx-prof/#Property:format)

_This property's details are from the [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")] specification._

| RDF Property: | [dct:format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#terms-format) |
| --- | --- |
| Label: | Format |
| Definition: | The file format, physical medium, or dimensions of the resource |
| Sub property of: | [dc:format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#elements-format) |

#### 8.4.4 Property: hasRole[](https://www.w3.org/TR/dx-prof/#Property:hasRole)

| RDF Property: | [prof:hasRole](https://www.w3.org/TR/dx-prof/#Property:hasRole) |
| --- | --- |
| Label: | has role |
| Definition: | A description of a resource that defines an aspect - a particular part, feature or role - of a Profile |
| Domain: | [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) |
| Range: | [skos:Concept](https://www.w3.org/TR/skos-reference/#Concept) |
| Usage note: | A set of common roles are defined by the Profiles Vocabulary. These are not exhaustive or disjoint, and may be extended for situations where finer-grained description of purpose is necessary. A profile resource may perform multiple roles |

#### 8.4.5 Property: isInheritedFrom[](https://www.w3.org/TR/dx-prof/#Property:isInheritedFrom)

| RDF Property: | [prof:isInheritedFrom](https://www.w3.org/TR/dx-prof/#Property:isInheritedFrom) |
| --- | --- |
| Label: | is inherited from |
| Definition: | A base specification, a Resource Descriptor from which is to be considered a Resource Descriptor for this Profile also |
| Domain: | [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) |
| Range: | [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile) |
| Usage note: | This property is created for the convenience of clients. When profile describers wish to allow clients to discover all profile resources relevant to a Profile without having to navigating an inheritance hierarchy of prof:profileOf relations, this predicate may be used to directly associate inherited Profile Descriptors with the Profile. If this property is present, it should be used consistently and all relevant profile resources a client may need to utilise the profile should be present and described using this predicate |

Proposal: replace `isInhertiedFrom` with a more general property that allows any `ResourceDescriptor` to directly indicate the `Profile` that defines the `ResourceRole` of this resource.

This is a spin-off from [#642](https://github.com/w3c/dxwg/issues/642). The example provided there uses the property prof:inheritedFrom between a Resource Descriptor and a Profile.

As [@kcoyle](https://github.com/kcoyle) noted, all of the requirements related to inheritance all speak of profile inheritance. From the draft profiles guidance document: "2..4 Profile inheritance [RPFINHER] Profiles may add to or specialise clauses from one or more base specifications. Such profiles inherit all the constraints from base specifications."

In addition we have this, which I think may also refer to resources rather than profiles:

 "2.3 Profile of profiles [RPFPP] One can create a profile of profiles, with elements potentially inherited on several levels."

We've talked a lot about 'profile inheritance' and prof:isInheritedFrom may be about something slightly different (maybe a "consequence" of profile inheritance, but for the resources that embody these profiles).

NB: this issue is part of a wider discussion on profile inheritance ([#748](https://github.com/w3c/dxwg/issues/748), [#795](https://github.com/w3c/dxwg/issues/795) , [#842](https://github.com/w3c/dxwg/issues/842), maybe [#800](https://github.com/w3c/dxwg/issues/800), and 769), and we should try to avoid putting everything of that discussion into it!!!

To illustrate the use of `prof:isInheritedFrom`, the following example is given in both pictorial and code forms.

[![Image 6: Property isInheritedFrom in use](https://www.w3.org/TR/dx-prof/figures/isInheritedFrom.svg)](https://www.w3.org/TR/dx-prof/figures/isInheritedFrom.svg)

Figure 6 Property `isInheritedFrom` in use. Here the `prof:ResourceDescriptor` instance **Profile Y, Resource Descriptor 2** refers to the same artifact (a constraints file) as **Standard X, Resource Descriptor 1** and it is inherited by **Profile Y** from **Standard X** which **Profile Y** is a profile of. 

[Example 5](https://www.w3.org/TR/dx-prof/#eg-isInheritedFrom)
: Property isInheritedFrom in use

# If Standard X, described using PROF, is given as having a Resource
# Descriptor, RD_1, with role "Full Constraints" as follows:

@prefix ex1: <http://example.org/profile1/> .
@prefix ex2: <http://example.org/profile2/> .
@prefix dct: <http://purl.org/dc/terms/> .Property isInheritedFrom in use.
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix role: <http://www.w3.org/ns/dx/prof/role/> .

# example standard
# with a single resource indicated for this Standard
ex1:Standard_X
    a dct:Standard ;
    dct:title "Standard X" ;
    prof:hasResource ex1:RD_1 .

# Example ResourceDescriptor for Standard X
#   * conforms to the ShEx Expression Language
#   * in the JSON format
#   * used to validate instance data claiming conformance to Standard X
#   * the actual file described is ex1:constraints.json
ex1:RD_1
    a prof:ResourceDescriptor ;
    dct:conformsTo <http://shex.io/shex-semantics-20191008/> ;
    dct:format <https://w3id.org/mediatype/application/json> ;
    prof:hasRole role:validation ;
    prof:hasArtifact ex1:constraints.json .

# then, a profile of Standard X, perhaps Profile Y, may use
# prof:isInheritedFrom to re-use that Resource Descriptor RD_1

ex2:Profile_Y
    a prof:Profile ;
    dct:title "Profile Y" ;
    prof:isProfileOf ex1:Standard_X ;  # this is a profile of Standard X
    prof:hasResource
    [
        # Resource Descriptor 2 in diagram
        #   * inherited from Standard X
        #   * conforms to SHACL
        #   * in the Turtle format
        #   * with an example role Part Constraints - not defined. A changed role from
        #       the Resource Descriptor's role in relation to Profile_X
        #   * the actual file described is ex1:constraints.json
        a prof:ResourceDescriptor ;
        prof:isInheritedFrom ex1:Standard_X ;
        dct:conformsTo <https://www.w3.org/TR/shacl/> ;
        dct:format <https://w3id.org/mediatype/text/turtle> ;
        prof:hasRole ex:partConstraints ;
        prof:hasArtifact ex1:constraints.ttl
    ] ,
    [
        # Resource Descriptor 3 in diagram. Not inherited from anywhere
        #   * constraints are Profile Y's on top of Standard X's
        #   * this is indicate with example Role Extension Constraints
        a prof:ResourceDescriptor ;
        dct:conformsTo <http://www.w3.org/ns/shacl#> ;
        dct:format <https://w3id.org/mediatype/text/turtle> ;
        prof:hasRole ex:extensionConstraints ;
        prof:hasArtifact ex2:extension_constraints.ttl
    ] .

### 8.5 Class: ResourceRole[](https://www.w3.org/TR/dx-prof/#Class:ResourceRole)

| [OWL Class](https://www.w3.org/TR/owl-syntax/#Classes) | [prof:ResourceRole](https://www.w3.org/TR/dx-prof/#Class:ResourceRole) |
| --- | --- |
| Label: | Resource Role |
| Definition: | A role that an profile resource, described by a Resource Descriptor, plays |
| Sub class of: | [skos:Concept](https://www.w3.org/TR/skos-reference/#Concept) |
| Usage note: | Specific terms must come from a vocabulary. Such a vocabulary is provided in [§9. Resource Role Instances](https://www.w3.org/TR/dx-prof/#resource-roles-vocab) but other terms may also be used |

9. Resource Role Instances[](https://www.w3.org/TR/dx-prof/#resource-roles-vocab)
---------------------------------------------------------------------------------

The example ResourceRole instances in this document are considered a "feature at risk" until the total list and definitions for them can be widely agreed to.

If not listed here, ResourceRole instances will be listed in a supplimentary vocabulary to PROF.

Currently [PROF roles](https://www.w3.org/TR/dx-prof/#resource-roles-vocab) are defined in their own namespace, separate from the "base" one for PROF.

 In [#535](https://github.com/w3c/dxwg/issues/535) and [#536](https://github.com/w3c/dxwg/issues/536) points have been made for and against having them in separate namespace. But that discussion was mixed with the discussion on whether they should be documented in the same document as PROF, which is slightly different.

 In the end I am not sure there has been a definitive argument for keeping roles in the same namespace. So I would like the WG to re-examine this.

 Maybe to there has been progress on the front of possible W3C registry (such registry was envisioned at one point as a possible place for a role vocabulary).

In the meantime I think there should be a note acknowledging the issue in [the role section of the PROF spec](https://www.w3.org/TR/dx-prof/#resource-roles-vocab), asking for commenters to give feedback.

NB: I believe this is not a blocking issue for moving to CR.

Here are a small set of Resource Role instances developed during the creation of this vocabulary. Applications may choose to extend this list as required with new and specialised Resource Role instances for their purposes.

These instances are both `owl:NamedIndividual`s and `skos:Concept`s and have basic SKOS [[SKOS-REFERENCE](https://www.w3.org/TR/dx-prof/#bib-skos-reference "SKOS Simple Knowledge Organization System Reference")] properties.

Note

These Roles are defined within a namespace that is derived from, but separate from, the namespace for PROF. This namespace is: `http://www.w3.org/ns/dx/prof/role/` with the suggested RDF prefix of `role`. This is to allow for them to grow independently from the main vocabulary.

### 9.1 Resource Role: Constraints[](https://www.w3.org/TR/dx-prof/#Role:constraints)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:constraints](https://www.w3.org/TR/dx-prof/#Role:constraints) |
| --- | --- |
| Pref Label: | Constraints |
| Definition: | Descriptions of obligations, limitations or extensions that the profile defines |
| Usage Note: | Use this Role when you want to indicate the constraints that the associated Profile imposes on top of base specifications |

### 9.2 Resource Role: Example[](https://www.w3.org/TR/dx-prof/#Role:example)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:example](https://www.w3.org/TR/dx-prof/#Role:example) |
| --- | --- |
| Pref Label: | Example |
| Definition: | Sample instance data conforming to the profile |
| Usage Note: | Use this Role when you want to provide instances of data conforming to the profile to inform users |

### 9.3 Resource Role: Guidance[](https://www.w3.org/TR/dx-prof/#Role:guidance)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:guidance](https://www.w3.org/TR/dx-prof/#Role:guidance) |
| --- | --- |
| Pref Label: | Guidance |
| Definition: | Documents, in human-readable form, how to use the profile |
| Usage Note: | Many existing profiles treat their human-readable forms (PDF documents etc.) as authoritative. This role is suggestive of non-authoritativeness. For a role for a human-readable resource that is authoritative, see [Specification](https://www.w3.org/TR/dx-prof/#Role:specification). |

### 9.4 Resource Role: Mapping[](https://www.w3.org/TR/dx-prof/#Role:mapping)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:mapping](https://www.w3.org/TR/dx-prof/#Role:mapping) |
| --- | --- |
| Pref Label: | Mapping |
| Definition: | Describes conversions between two specifications |

### 9.5 Resource Role: Schema[](https://www.w3.org/TR/dx-prof/#Role:schema)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:schema](https://www.w3.org/TR/dx-prof/#Role:schema) |
| --- | --- |
| Pref Label: | Schema |
| Alternate Label: | Shape, Structure |
| Definition: | Machine-readable structural descriptions of data defined by the profile |

### 9.6 Resource Role: Specification[](https://www.w3.org/TR/dx-prof/#Role:specification)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:specification](https://www.w3.org/TR/dx-prof/#Role:specification) |
| --- | --- |
| Pref Label: | Specification |
| Definition: | Defining the profile in human-readable form |
| Usage Note: | This role indicates authoritativeness. For a role for a human-readable resource that is not authoritative, see [Guidance](https://www.w3.org/TR/dx-prof/#Role:guidance) |

### 9.7 Resource Role: Validation[](https://www.w3.org/TR/dx-prof/#Role:validation)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:validation](https://www.w3.org/TR/dx-prof/#Role:validation) |
| --- | --- |
| Pref Label: | Validation |
| Definition: | Supplies instructions about how to verify conformance of data to the profile |
| Usage Note: | This role implies inclusion or import of inherited constraints |

### 9.8 Resource Role: Vocabulary[](https://www.w3.org/TR/dx-prof/#Role:vocabulary)

| [SKOS Concept](https://www.w3.org/TR/skos-reference/#Concept) | [role:vocabulary](https://www.w3.org/TR/dx-prof/#Role:vocabulary) |
| --- | --- |
| Pref Label: | Vocabulary |
| Definition: | Defines terms used in the profile specification |

10. Examples[](https://www.w3.org/TR/dx-prof/#examples)
-------------------------------------------------------

_This section is non-normative._

This section contains a few examples of PROF in use to demonstrate aspects of this vocabulary. While efforts have been made to ensure they are accurate at the time of this document's publication, they are not to be considered authoritative; their purpose is only to illustrate this vocabulary's use.

### 10.1 DCAT-AP[](https://www.w3.org/TR/dx-prof/#eg-dcat-ap)

_This example showcases this vocabulary's description of parts of an existing, well-known, profile._

DCAT-AP is the widely used European _Application Profile_ of DCAT. DCAT-AP is described in document form (PDF & DOCX) and a constraints profile resource for instance validation is available, formulated using the W3C's Shapes Constraints Language constraints language [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")]. An image of the DCAT-AP model is also provided.

The figure uses elements from this vocabulary to describe part of the DCAT-AP Profile graphically - PDF & RDF profile resources only - to simplify the example.

[![Image 7: DCAT-AP described using this vocabulary](https://www.w3.org/TR/dx-prof/examples/dcat-ap.svg)](https://www.w3.org/TR/dx-prof/examples/dcat-ap.svg)

Figure 7 Part of the DCAT-AP Profile described using this ontology. Here two two Resource Descriptors are shown relating to the Profile indicating profile resources with "Guidance" and "Constraints" roles. 

In words this vocabulary's descriptions of DCAT-AP is:

*    a [prof:Profile](https://www.w3.org/TR/dx-prof/#Class:Profile)
    *    with a [prof:isProfileOf](https://www.w3.org/TR/dx-prof/#Property:isProfileOf) link to the DCAT [[VOCAB-DCAT-2](https://www.w3.org/TR/dx-prof/#bib-vocab-dcat-2 "Data Catalog Vocabulary (DCAT) - Version 2")] standard 

*    two [prof:ResourceDescriptor](https://www.w3.org/TR/dx-prof/#Class:ResourceDescriptor) objects - linked to the _prof:Profile_ object by [prof:hasResource](https://www.w3.org/TR/dx-prof/#Property:hasResource) properties 
    *    a document, with a [dct:format](https://www.w3.org/TR/dx-prof/#Property:format) value of [application/pdf](https://w3id.org/mediatype/application/pdf) and a [prof:hasRole](https://www.w3.org/TR/dx-prof/#Property:hasRole) value of [role:Guidance](https://www.w3.org/TR/dx-prof/#Role:guidance)
    *    a document, with a [dct:format](https://www.w3.org/TR/dx-prof/#Property:format) value of [text/turtle](https://w3id.org/mediatype/text/turtle), a [dct:conformsTo](https://www.w3.org/TR/dx-prof/#Property:conformsTo) value of [http://www.w3.org/ns/shacl](https://www.w3.org/ns/shacl) (the namespace of the [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")] specification) and a [prof:hasRole](https://www.w3.org/TR/dx-prof/#Property:hasRole) value of [role:Constraints](https://www.w3.org/TR/dx-prof/#Role:constraints)

 each with a [prof:hasArtifact](https://www.w3.org/TR/dx-prof/#Property:hasArtifact) value of an implementing profile resource object in the European Commission's ['joinup' data catalogue](https://joinup.ec.europa.eu/)
    *   [bb53cb4f017d4](https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f17e18570_b1d77_b4171_b9df5_bb53cb4f017d4)
    *   [b758e7401c096](https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f016d88c3_ba0b3_b4506_bae4e_b758e7401c096)

In RDF (turtle format), DCAT-AP is described using the Profiles Vocabulary, with many properties not listed in the summary figure and description above as:

[Example 6](https://www.w3.org/TR/dx-prof/#eg-eg-dcat-ap)
: DCAT-AP described using PROF in RDF (turtle)

@prefix dc:    <http://purl.org/dc/elements/1.1/> .
@prefix prof:  <http://www.w3.org/ns/dx/prof/> .
@prefix role:  <http://www.w3.org/ns/dx/prof/role/> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .

<https://joinup.ec.europa.eu/release/dcat-ap-v11>
  a prof:Profile ;
  prof:hasToken "dcat-ap" ;
  rdfs:label "DCAT-AP" ;
  rdfs:comment "DCAT Application Profile for data portals in Europe" ;
  dc:publisher "European Union" ;
  prof:isProfileOf <http://www.w3.org/ns/dcat> ;

  # SHACL constraints for the profile, guidance doc in Word & PDF & an image of the profile components
  prof:hasResource
    # Guidance doc in Word (DOCX)
    <https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f6f27f059_bf785_b4d7d_bb602_b6448aab73bd5> ,
    # Guidance doc in PDF
    <https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f17e18570_b1d77_b4171_b9df5_bb53cb4f017d4> ,
    # profile image (PNG)
    <https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f1131a208_b92e9_b4427_ba40c_b6c47746cd422> ,
    # Constraints in SHACL
    <https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f016d88c3_ba0b3_b4506_bae4e_b758e7401c096> ;
.

# The DCAT-AP profile itself has profiles: here GeoDCAT-AP v1.0 is given
<https://joinup.ec.europa.eu/release/geodcat-ap-v10>
  a prof:Profile ;
  rdfs:label "GeoDCAT-AP" ;
  prof:isProfileOf <https://joinup.ec.europa.eu/release/dcat-ap-v11> ;

<https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f6f27f059_bf785_b4d7d_bb602_b6448aab73bd5>
  a prof:ResourceDescriptor;
	rdfs:label "DCAT-AP Guidance Document (Word)" ;
	dct:format <https://w3id.org/mediatype/application/msword> ;
	prof:hasRole role:Guidance ;
.

<https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f17e18570_b1d77_b4171_b9df5_bb53cb4f017d4>
  a prof:ResourceDescriptor;
	rdfs:label "DCAT-AP Guidance Document (PDF)" ;
	dct:format <https://w3id.org/mediatype/application/pdf> ;
	prof:hasRole role:Guidance ;
.

<https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f1131a208_b92e9_b4427_ba40c_b6c47746cd422>
  a prof:ResourceDescriptor;
	rdfs:label "DCAT-AP Image" ;
	dct:format <https://w3id.org/mediatype/image/png> ;
	prof:hasRole role:Guidance ;
.

<https://joinup.ec.europa.eu/rdf_entity/http_e_f_fdata_ceuropa_ceu_fw21_f016d88c3_ba0b3_b4506_bae4e_b758e7401c096>
  a prof:ResourceDescriptor;
	rdfs:label "DCAT-AP Constraints" ;
	dct:conformsTo <http://www.w3.org/ns/shacl>; # the namespace for SHACL
	dct:format "text/turtle" ;
	prof:hasRole role:FullConstraints ;
.

### 10.2 DCAT-AP hierarchy[](https://www.w3.org/TR/dx-prof/#eg-hierarchy)

_This example showcases this vocabulary being used to indicated profiles within a complex hierarchy._

DCAT-AP, a profile of DCAT, has itself been profiled for various European countries, such as Belgium who has issued [DCAT-BE](http://dcat.be/). Additionally, there are several domain profiles of DCAT-AP, such as [[GeoDCAT-AP](https://www.w3.org/TR/dx-prof/#bib-geodcat-ap "GeoDCAT-AP: A geospatial extension for the DCAT application profile for data portals in Europe. Version 1.0.1")] - for describing geospatial datasets, dataset series and services - and [[StatDCAT-AP](https://www.w3.org/TR/dx-prof/#bib-statdcat-ap "StatDCAT-AP – DCAT Application Profile for description of statistical datasets. Version 1.0.1")] for enhancing interoperability between descriptions of statistical datasets. Further to this, there is even an Italian profile of GeoDCAT-AP, [GeoDCAT-AP_IT](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/news/geodcat-apit).

This profile hierarchy is represented graphically in the figure and RDF (turtle) below.

[![Image 8: DCAT-AP and related profiles in a hierarchy](https://www.w3.org/TR/dx-prof/examples/hierarchy.svg)](https://www.w3.org/TR/dx-prof/examples/hierarchy.svg)

Figure 8 DCAT-AP and related profiles in a hierarchy. The Profile labelled '?' shows a potential future profile instance that profiles both DCAT-BE & StatDCAT-AP. 

[Example 7](https://www.w3.org/TR/dx-prof/#eg-eg-hierarchy)
: The GeoDCAT-AP profile hierarchy described using PROF in RDF (turtle)

@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://www.w3.org/ns/dcat>
  a dct:Standard ;

<https://joinup.ec.europa.eu/release/dcat-ap-v11>
  a prof:Profile ;
  rdfs:label "DCAT-AP" ;
  prof:isProfileOf <http://www.w3.org/ns/dcat> ;

<http://dcat.be>
  a prof:Profile ;
  rdfs:label "DCAT-BE" ;
  prof:isProfileOf <https://joinup.ec.europa.eu/release/dcat-ap-v11> ;

<https://joinup.ec.europa.eu/release/geodcat-ap-v10>
  a prof:Profile ;
  rdfs:label "GeoDCAT-AP" ;
  prof:isProfileOf <https://joinup.ec.europa.eu/release/dcat-ap-v11> ;

<https://joinup.ec.europa.eu/solution/statdcat-application-profile-data-portals-europ>
  a prof:Profile ;
  rdfs:label "StatDCAT-AP" ;
  prof:isProfileOf <https://joinup.ec.europa.eu/release/dcat-ap-v11> ;

<https://joinup.ec.europa.eu/news/geodcat-apit1>
  a prof:Profile ;
  rdfs:label "GeoDCAT-AP_IT" ;
  prof:isProfileOf <https://joinup.ec.europa.eu/release/geodcat-ap-v10> ;

# an example as per the Figure above, not an existing profile
<http://example.org/profile/questionmark>
  a prof:Profile ;
  rdfs:label "?" ;
  prof:isProfileOf
      <https://joinup.ec.europa.eu/solution/statdcat-application-profile-data-portals-europ> ,
      <http://dcat.be> .

Since there are no cardinality restrictions on either the property `prof:isProfileOf` or other restrictions on the class definition of `prof:Profile` that prevent them from being used to represent polyhierarchies, Belgium could release a profile of [[StatDCAT-AP](https://www.w3.org/TR/dx-prof/#bib-statdcat-ap "StatDCAT-AP – DCAT Application Profile for description of statistical datasets. Version 1.0.1")] (e.g., StatDCAT-BE), that would be both a profile of DCAT-BE and [[StatDCAT-AP](https://www.w3.org/TR/dx-prof/#bib-statdcat-ap "StatDCAT-AP – DCAT Application Profile for description of statistical datasets. Version 1.0.1")]. This imagined profile, '?' in the figure above, would not be a profile of GeoDCAT-AP.

### 10.3 CSIRO Dummy Dublin Core AP[](https://www.w3.org/TR/dx-prof/#eg-csiro-dummy-dcap)

_This example uses a dummy profile created for this document to show how PROF describes profiles created according to the Guidelines for Dublin Core Application Profiles [[DCAP](https://www.w3.org/TR/dx-prof/#bib-dcap "Guidelines for Dublin Core Application Profiles")]._

The DCAP Guidelines document "explains the key components of a Dublin Core Application Profile and walks through the process of developing a profile". It "does not address the creation of machine-readable implementations of an application profile" which is what PROF does.

In this example, a dummy profile of Dublin Core TERMS [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")] is created to characterise documents in a hypothetical "ePublish" platform. The dummy profile contains many parts:

*   a profile overview document
*   a _How To_ document offering guidance on how to use the profile
*   two constraint language files - both conforming to DCAP's constraint syntax in plain text and RDF (turtle) formats
*   two profile description files - one an image (the [Figure 9](https://www.w3.org/TR/dx-prof/#fig-eg-csiro-dummy-dcap "CSIRO Dummy DCAP Profile characterised using PROF. Only two of the four Resource Descriptors in the RDF below are shown.") below) and the other an RDF file (the example RDF below)

[![Image 9: CSIRO Dummy DCAP Profile](https://www.w3.org/TR/dx-prof/examples/csiro-dummy-dcap.svg)](https://www.w3.org/TR/dx-prof/examples/csiro-dummy-dcap.svg)

Figure 9 CSIRO Dummy DCAP Profile characterised using PROF. Only two of the four Resource Descriptors in the RDF below are shown. 

[Example 8](https://www.w3.org/TR/dx-prof/#eg-eg-csiro-dummy-dcap)
: The CSIRO Dummy DCAP Profile characterised using PROF in RDF (turtle)

#
#   This document is a description, according to the Profiles Vocabulary (see https://www.w3.org/TR/dx-prof/)
#   of a dummy "CSIRO ePublish Repository" profile of the Dubline Core standard. This profile is known as a DCAP -
#   Dublin Core Application Profile
#
#   See http://dublincore.org/documents/profile-guidelines/ for more information about Dublin Core Application Profiles
#
@prefix dct: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix role: <http://www.w3.org/ns/dx/prof/role/> .

# Base Specification being profiled
<http://dublincore.org/documents/2012/06/14/dcmi-terms/> a dct:Standard ;
    rdfs:label "DCMI Metadata Terms" .

# dummy CSIRO profile of DC for ePublish repository
# URIs not dereferencable
<http://test.linked.data.gov.au/test/def/CSIRO-ePub-DCAP>
    a                 prof:Profile ;
    rdfs:label        "CSIRO's profile of DC for ePublish" ;
    prof:isProfileOf    <http://dublincore.org/documents/2012/06/14/dcmi-terms/> ;
    prof:token        "ePubDC"^^xsd:Token ;
    prof:hasResource  _:1 , _:2 , _:3 , _:4 .

# example's code repository home
_:1
    a                 prof:ResourceDescriptor ;
    rdfs:label        "Profile Specifcation" ;
    dct:format        <https://w3id.org/mediatype/text/html> ;
    # the official written text specifying the Profile
    prof:hasRole      role:Specification ;
    prof:hasArtifact  <http://linked.data.gov.au/def/CSIRO-ePub-DCAP/> .

# this is an RDF (turtle) version of the DSP constraints for this profile
_:2
    a                 prof:ResourceDescriptor ;
    rdfs:label        "Full constraints in RDF" ;
    dct:conformsTo    <http://dublincore.org/documents/2008/03/31/dc-dsp/> ; # the constraints conform to the DSP spec
    dct:format        <https://w3id.org/mediatype/text/turtle> ; # it's in Turtle format
    # this is full constraints: if your instance passes these, you're compliant with the profile
    prof:hasRole      role:Constraints ;
    prof:hasArtifact  <http://test.linked.data.gov.au/test/def/CSIRO-ePub-DCAP/constraints.ttl> .

_:3
    a                 prof:ResourceDescriptor ;
    rdfs:label        "Full constraints in DSP constraint language" ;
    dct:conformsTo    <http://dublincore.org/documents/2008/03/31/dc-dsp/> ; # the constraints conform to the DSP spec
    dct:format        <https://w3id.org/mediatype/text/plain> ; # it's in plain text format
    # this is full constraints: if your instance passes these, you're compliant with the profile
    prof:hasRole      role:Constraints ;
    prof:hasArtifact  <http://test.linked.data.gov.au/test/def/CSIRO-ePub-DCAP/constraints-dcap-syntax.txt> .

# this profile resource is a PDF file in the def about how to use the CSIRO-ePub-DCAP
_:4
    a                 prof:ResourceDescriptor ;
    rdfs:label        "Guidance document" ;
    dct:format        <https://w3id.org/mediatype/application/pdf> ;
    # general guidance info on how to use/implement this Profile
    prof:hasRole      role:Guidance ;
    prof:hasArtifact <http://test.linked.data.gov.au/test/def/CSIRO-ePub-DCAP/HowTo.pdf> .

This DCAP example shows, among other things, that a `Profile` may contain multiple `Resource Descriptor` individuals that perform the same `Resource Role` (here `Constraints`) that are differentiated on other bases, here on format: plain text & RDF (turtle).

### 10.4 Geoscience Australia's Profile of ISO19115-1:2014[](https://www.w3.org/TR/dx-prof/#eg-ga)

_This example shows a non-RDF profile of a non-RDF standard: ISO19115-1:2014 (Geographic information) [[ISO-19115-1-2014](https://www.w3.org/TR/dx-prof/#bib-iso-19115-1-2014 "Geographic information -- Metadata -- Part 1: Fundamentals")]._

Communities commonly make profiles of the International Organization for Standardization's standard ISO19115-1:2014 Geographic information -- Metadata -- Part 1: Fundamentals used for cataloguing spatial datasets. [Geoscience Australia](http://www.ga.gov.au/), Australia's national geological survey agency, has created a profile that constrains ISO19115-1:2014 in ways such as making optional properties in the standard mandatory for profile conformance.

The GA Profile of ISO19115 is published online as a collection of profile resources with an index document with the persistent URI [http://pid.geoscience.gov.au/def/schema/ga/ISO19115-1-2014](http://pid.geoscience.gov.au/def/schema/ga/ISO19115-1-2014).

Although not initially formulated with PROF in mind, nevertheless the various parts of the GA Profile of ISO19115 can be characterised using PROF as per [Figure 10](https://www.w3.org/TR/dx-prof/#fig-eg-ga "The GA Profile of ISO19115 characterised using PROF.") and the example RDF below. Note that the persistent URIs assigned to the profile by Geoscience Australia are used within the PROF description.

[![Image 10: GA Profile of ISO19115 in PROF](https://www.w3.org/TR/dx-prof/examples/ga.svg)](https://www.w3.org/TR/dx-prof/examples/ga.svg)

Figure 10 The GA Profile of ISO19115 characterised using PROF. 

[Example 9](https://www.w3.org/TR/dx-prof/#eg-eg-ga)
: GA Profile of ISO19115 according to PROF in RDF (turtle)

@prefix : <http://www.w3.org/ns/dx/prof/examples/ga.ttl#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix roles: <http://www.w3.org/ns/dx/prof/roles/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:ISO19115-1-2014
    a dct:Standard ;
    rdfs:label "ISO ISO19115-1:2014" ;
    rdfs:comment "The international standard ISO19115-1:2014 Geographic information - Metadata" ;
    dc:publisher "International Organization for Standardization" ;
    dct:source <https://www.iso.org/standard/53798.html>
.

<http://pid.geoscience.gov.au/def/schema/ga/ISO19115-1-2014>
    a prof:Profile ;
    prof:token "iso19115-ga" ;
    rdfs:label "ISO19115-1:2014 GA Profile";
    rdfs:comment """Provides a means to declare, and discover implementation profile resources to check, implementations of geographic metadata schema conforming to GA's profile."""@en;
    dct:publisher <http://pid.geoscience.gov.au/org/ga/geoscienceaustralia> ;
    prof:profileOf :ISO19115-1-2014 ;
    prof:hasResource :web , :spec , :schema , :constraints ;
.

:web
    a prof:ResourceDescriptor ;
    rdfs:label "GA Profile guidance document online" ;
    prof:hasRole roles:guidance ;
    dct:conformsTo :WebPage ;
    dct:format <https://w3id.org/mediatypes/text/html> ;
    prof:hasArtifact <http://pid.geoscience.gov.au/def/schema/ga/ISO19115-1-2014> ;
.

:spec
    a prof:ResourceDescriptor ;
    rdfs:label "GA Profile specification document";
    prof:hasRole roles:specification ;
    dct:format <https://w3id.org/mediatypes/application/pdf> ;
    prof:hasArtifact <http://pid.geoscience.gov.au/dataset/ga/122551> ;
.

:schema
    a prof:ResourceDescriptor ;
    rdfs:label "GA Profile XML Schema";
    prof:hasRole roles:specification ;
    dct:conformsTo :XSDSchema ;
    dct:format <https://w3id.org/mediatypes/text/xml> ;
    prof:hasArtifact <http://pid.geoscience.gov.au/def/schema/ga/ISO19115-3-2016/gapm.xsd> ;
.

:constraints
    a prof:ResourceDescriptor ;
    rdfs:label "GA Profile Schematron" ;
    prof:hasRole roles:fullConstraints ;
    dct:conformsTo :Schematron ;
    dct:format <https://w3id.org/mediatypes/text/xml> ;
    prof:hasArtifact <http://pid.geoscience.gov.au/def/schema/ga/schematron-rules-ga.sch> ;
.

:WebPage a dct:MediaTypeOrExtent ;
    rdfs:label "Web Page" ;
    rdfs:comment "A document written in HyperText Markup Language designed for human reading via a web browser." ;
    dct:source <https://www.w3.org/html/> ;
.

:Schematron a dct:MediaTypeOrExtent ;
    rdfs:label "Schematron" ;
    rdfs:comment "A language for making assertions about the presence or absence of patterns in XML documents." ;
    dct:source <http://schematron.com> ;
.

### 10.5 Asset Description Metadata Schema[](https://www.w3.org/TR/dx-prof/#eg-adms)

_This example shows a `Profile`, some of whose `Resource Descriptors` conform to standards._

The Asset Description Metadata Schema (ADMS) [[VOCAB-ADMS](https://www.w3.org/TR/dx-prof/#bib-vocab-adms "Asset Description Metadata Schema (ADMS)")] is a profile of DCAT, used to describe semantic assets. Both ADMS the `Profile` and two of its `Resource Descriptors` are published according to W3C specifications for _Recommendations_ and _Working Group Notes_.

[![Image 11: ADMS profile of DCAT](https://www.w3.org/TR/dx-prof/examples/adms.svg)](https://www.w3.org/TR/dx-prof/examples/adms.svg)

Figure 11 The ADMS profile of DCAT. 

[Example 10](https://www.w3.org/TR/dx-prof/#eg-eg-adms)
: ADMS profile of DCAT according to PROF in RDF (turtle)

@prefix : <http://www.w3.org/ns/dx/prof/examples/adms.ttl#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix roles: <http://www.w3.org/ns/dx/prof/roles/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

#
#   A series of standards defined in this examples document
#
:W3Cnote
  rdf:type dct:Standard ;
  rdfs:label "W3C Working Group Note Document" ;
.

:W3Crec
  rdf:type dct:Standard ;
  rdfs:label "W3C Recommendation Document" ;
.

#
#   ADMS, described as a profile of DCAT (original)
#
:ADMS
    a prof:Profile ;
    rdfs:label "ADMS" ;
    # this URI is for DCAT (original) as defined in the DCAT examples
    prof:profileOf <http://www.w3.org/ns/dx/prof/examples/dcat.ttl#dcat2014> ;
    prof:hasResource :ADMS-note ,
                     :ADMS-rdf ,
.

:ADMS-note
    a prof:ResourceDescriptor ;
    rdfs:label "ADMS specification document" ;
    prof:hasRole roles:specification ;
    dct:conformsTo prof:W3Cnote ;
    dct:format <https://w3id.org/mediatypes/text/html> ;
    prof:hasArtifact <https://www.w3.org/TR/vocab-adms/> ;
.

:ADMS-rdf
    a prof:ResourceDescriptor ;
    rdfs:label "ADMS RDF vocabulary" ;
    prof:hasRole roles:vocabulary ;
    dct:conformsTo <https://www.w3.org/TR/owl2-rdf-based-semantics/> ,
                   <https://www.w3.org/TR/rdf-schema/> ;
    dct:format <https://w3id.org/mediatypes/text/turtle> ;
    prof:hasArtifact <https://www.w3.org/ns/adms> ;
.

# additional information about DCAT (original) not present in the DCAT example
<http://www.w3.org/ns/dx/prof/examples/dcat.ttl#dcat-orig>
    dct:conformsTo :W3Crec .

11. Test Suite[](https://www.w3.org/TR/dx-prof/#testsuite)
----------------------------------------------------------

A software suite is made available to test implementations of this vocabulary for compliance. This suite comprises of [[SHACL](https://www.w3.org/TR/dx-prof/#bib-shacl "Shapes Constraint Language (SHACL)")] RDF graph validation templates and instructions for the application of those templates to implementations.

This issue was created in the [Profiles Ontology document](https://w3c.github.io/dxwg/profilesont/) and is listed in it. Once consensus on addressing it is reached here in comments below, the results will be added to the document and the issue closed.

12. Implementations[](https://www.w3.org/TR/dx-prof/#implementations)
---------------------------------------------------------------------

_This section is non-normative._

Implementation conformance reports for this vocabulary are given in:

*   [https://github.com/CSIRO-enviro-informatics/prof-ont-implementation-results](https://github.com/CSIRO-enviro-informatics/prof-ont-implementation-results)

13. Alignments[](https://www.w3.org/TR/dx-prof/#alignments)
-----------------------------------------------------------

_This section is non-normative._

This issue was created in the [Profiles Ontology document](https://w3c.github.io/dxwg/profilesont/) and is listed in it. Once consensus on addressing it is reached here in comments below, the results will be added to the document and the issue closed.

This section lists alignments between PROF and other, related, ontologies.

### 13.1 Dataset Catalogue Vocabulary[](https://www.w3.org/TR/dx-prof/#alignment-dcat)

PROF is considered a specialisation of the revised version of the Dataset Catalogue Vocabulary [[VOCAB-DCAT-2](https://www.w3.org/TR/dx-prof/#bib-vocab-dcat-2 "Data Catalog Vocabulary (DCAT) - Version 2")] for the purpose of cataloguing profiles. With this in mind, the main PROF classes - `Profile` and `Resource Descriptor` - specialise (are sub classes of) DCAT's `Resource` and `Distributions` respectively. This alignment is not normative, but is provided as a recommended way to consider general metadata needs when describing profiles.

These specialisations are indicated in [Figure 12](https://www.w3.org/TR/dx-prof/#fig-align-dcat "Alignment of PROF with DCAT [VOCAB-DCAT-2].") below as well as the data element mapping table that follows it.

![Image 12: Alignment of PROF with DCAT](https://www.w3.org/TR/dx-prof/alignments/dcat.svg)

Figure 12 Alignment of PROF with DCAT [[VOCAB-DCAT-2](https://www.w3.org/TR/dx-prof/#bib-vocab-dcat-2 "Data Catalog Vocabulary (DCAT) - Version 2")].

The following table relates PROF and DCAT elements.

| PROF element | Mapping property | DCAT element | Notes |
| --- | --- | --- | --- |
| prof:Profile | `rdfs:subClassOf` | dcat:Resource | `prof:Profile` is not a sub class of `dcat:Dataset` |
| prof:ResourceDescriptor | `rdfs:subClassOf` | dcat:Distribution |  |

While DCAT is referenced in the main PROF RDF file, the following separate RDF file contains just the mappings included in the table above too:

*   [alignments/dcat.ttl](https://www.w3.org/TR/dx-prof/alignments/dcat.ttl)

### 13.2 Asset Description Metadata Schema[](https://www.w3.org/TR/dx-prof/#alignment-adms)

The Asset Description Metadata Schema (ADMS) [[VOCAB-ADMS](https://www.w3.org/TR/dx-prof/#bib-vocab-adms "Asset Description Metadata Schema (ADMS)")] is a profile of DCAT, used to describe semantic assets. PROF is aligned with ADMS as per [Figure 13](https://www.w3.org/TR/dx-prof/#fig-align-adms "Alignment of PROF with ADMS [VOCAB-ADMS].") and table below.

Due to PROF being aligned with the revised version of DCAT and ADMS also being aligned with DCAT, classes and properties of the two vocabularies may be sensibly used beyond the mappings presented here. In particular the fact that both `prof:Profile` and `adms:Asset` are non-disjoint sub classes of `dcat:Resource`, albeit that the latter is such via being a sub class of `dcat:Dataset` which subclasses `dcat:Resource`, means that data resources could easily be dually typed as being of both `prof:Profile` and `adms:Asset`.

![Image 13: Alignment of PROF with ADMS](https://www.w3.org/TR/dx-prof/alignments/adms.svg)

Figure 13 Alignment of PROF with ADMS [[VOCAB-ADMS](https://www.w3.org/TR/dx-prof/#bib-vocab-adms "Asset Description Metadata Schema (ADMS)")].

The following table relates PROF and ADMS elements.

| PROF element | Mapping property | ADMS element |
| --- | --- | --- |
| prof:ResourceDescriptor | `rdfs:subClassOf` | adms:AssetDistribution |

The following RDF file contains just the mappings included in the table above:

*   [alignments/adms.ttl](https://www.w3.org/TR/dx-prof/alignments/adms.ttl)

### 13.3 Dublin Core Terms[](https://www.w3.org/TR/dx-prof/#alignment-dct)

PROF makes use of Dublin Core Terms [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")] directly with the PROF class `prof:Profile` being a sub class of `dct:Standard` and two Dublin Core Terms properties, `dct:format`&`dct:conformsTo` being recommended within PROF for use in describing instances of the `prof:ResourceDescriptor` class.

PROF is aligned with Dublin Core Terms as per [Figure 14](https://www.w3.org/TR/dx-prof/#fig-align-dct "Alignment of PROF with Dublin Core Terms [DCTERMS].") and table below.

![Image 14: Alignment of PROF with Dublin Core Terms](https://www.w3.org/TR/dx-prof/alignments/dct.svg)

Figure 14 Alignment of PROF with Dublin Core Terms [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")].

The following table relates PROF and Dublin Core Terms elements.

| PROF element | Mapping property | DCT element |
| --- | --- | --- |
| prof:Profile | `rdfs:subClassOf` | dct:Standard |

While Dublin Core Terms is referenced in the main PROF RDF file, the following RDF file contains just the mappings included in the table above:

*   [alignments/dct.ttl](https://www.w3.org/TR/dx-prof/alignments/dct.ttl)

### 13.4 Web Ontology Language[](https://www.w3.org/TR/dx-prof/#alignment-owl)

Raised by Reviewer 1 of the Profiles Ontology ESWC paper and elsewhere: PROF must differentiate itself from OWL, specifically `prof:isProfileOf` v. `owl:imports`.

PROF is a vocabulary formulated using the Web Ontology Language (OWL) [[OWL2-OVERVIEW](https://www.w3.org/TR/dx-prof/#bib-owl2-overview "OWL 2 Web Ontology Language Document Overview (Second Edition)")]. In addition to the basic modelling mechanics of PROF that use OWL, for example PROF classes being defined as `owl:Class` objects and PROF properties being OWL `owl:ObjectProperty` or other OWL property types, some of the core PROF modelling concepts relate to OWL ontology concepts.

PROF is aligned with OWL at a conceptual modelling level as per [Figure 15](https://www.w3.org/TR/dx-prof/#fig-align-owl "Alignment of PROF with OWL [OWL2-OVERVIEW].") and table below.

![Image 15: Alignment of PROF with OWL](https://www.w3.org/TR/dx-prof/alignments/owl.svg)

Figure 15 Alignment of PROF with OWL [[OWL2-OVERVIEW](https://www.w3.org/TR/dx-prof/#bib-owl2-overview "OWL 2 Web Ontology Language Document Overview (Second Edition)")].

| PROF element | Mapping property | OWL element |
| --- | --- | --- |
| prof:isProfileOf | `?` | owl:imports |

The following RDF file contains just the mappings included in the table above:

*   [alignments/owl.ttl](https://www.w3.org/TR/dx-prof/alignments/owl.ttl)

### 13.5 Vocabulary of a Friend[](https://www.w3.org/TR/dx-prof/#alignment-voaf)

Vocabulary of a Friend (VOAF) is a vocabulary specification providing elements allowing the description of vocabularies (RDFS vocabularies or OWL ontologies) [[VOAF](https://www.w3.org/TR/dx-prof/#bib-voaf "Vocabulary of a Friend (VOAF)")]. Due to VOAF being defined for use with RDF data resources instances only, PROF has an alignment with VOAF which is instance-specific: data resources described by instances of PROF's `prof:ResourceDescriptor` class with the property `prof:resourceRole` linking to the Resource Role `role:Vocabulary`, or a specialized version of it, may be a `voaf:Vocabulary`.

![Image 16: Alignment of PROF with VOAF](https://www.w3.org/TR/dx-prof/alignments/voaf.svg)

Figure 16 Alignment of PROF with VOAF [[VOAF](https://www.w3.org/TR/dx-prof/#bib-voaf "Vocabulary of a Friend (VOAF)")].

| PROF element | Mapping property | VOAF element |
| --- | --- | --- |
| instance of rdf:Resource | related to an instance of a `prof:ResourceDescriptor` via `prof:hasArtifact` that also relates to the Role `role:Vocabulary` or specialisation thereof | instance of voaf:Vocabulary |

The following RDF file contains just the mappings included in the table above:

*   [alignments/voaf.ttl](https://www.w3.org/TR/dx-prof/alignments/voaf.ttl)

### 13.6 OGC/ISO Modular Specification[](https://www.w3.org/TR/dx-prof/#alignment-modspec)

This issue was created in the [Profiles Ontology document](https://w3c.github.io/dxwg/profilesont/) and is listed in it. Once consensus on addressing it is reached here in comments below, the results will be added to the document and the issue closed.

Refer to OGC Modular Specification policy [[modspec]] and related work in ISO TC/211 [[cfg-mgmt]].

These specifications define how dependencies between 'standards' can be handled in a manageable way.

OGC profiling was in the Profile Guidance document in the related work and needs to be properly mentioned again, somewhere

### 13.7 Simple Knowledge Organization System[](https://www.w3.org/TR/dx-prof/#alignment-skos)

The Simple Knowledge Organization System (SKOS) [[SKOS-REFERENCE](https://www.w3.org/TR/dx-prof/#bib-skos-reference "SKOS Simple Knowledge Organization System Reference")] is a data model knowledge organization systems, such as thesauri, taxonomies, classification schemes and subject heading systems. PROF declares its instances of `Resource Role` to be instances of the `skos:Concept` class to indicate that they should be considered a hierarchy of concepts within a `skos:ConceptScheme`. Since they are SKOS hierarchy and it is recommended that implementers of PROF extend the hierarchy for their own needs, implementers should consider creating new `Resource Role` (also `skos:Concept`) and relating them to the existing instances with SKOS properties, particularly `skos:narrower`/`skos:broader`.

![Image 17: Alignment of PROF with SKOS](https://www.w3.org/TR/dx-prof/alignments/skos.svg)

Figure 17 Alignment of PROF with SKOS [[SKOS-REFERENCE](https://www.w3.org/TR/dx-prof/#bib-skos-reference "SKOS Simple Knowledge Organization System Reference")].

| PROF element | Mapping property | SKOS element |
| --- | --- | --- |
| prof:ResourceRole | `rdfs:subClassOf` | skos:Concept |

While SKOS is referenced in the main PROF RDF file, the following RDF file contains just the mappings included in the table above:

*   [alignments/skos.ttl](https://www.w3.org/TR/dx-prof/alignments/skos.ttl)

14. Security and Privacy[](https://www.w3.org/TR/dx-prof/#security_and_privacy)
-------------------------------------------------------------------------------

_This section is non-normative._

The PROF vocabulary, when used with likely extensions such as [[DCTERMS](https://www.w3.org/TR/dx-prof/#bib-dcterms "DCMI Metadata Terms")], supports the attribution of data and metadata to various participants such as data resource [creators](http://purl.org/dc/terms/creator), [publishers](http://purl.org/dc/terms/publisher) and other parties or agents via _qualified relations_ and, as such, may define terms that may be related to personal information. In addition, it may also be used with extensions that support the association of [rights](http://purl.org/dc/terms/rights) and [licenses](http://purl.org/dc/terms/license) with modelled Profiles and Resource Descriptors. These rights and licenses could potentially include or reference sensitive information such as user and asset identifiers as [described](https://www.w3.org/TR/odrl-vocab/#privacy-consideration) in [[ODRL-VOCAB](https://www.w3.org/TR/dx-prof/#bib-odrl-vocab "ODRL Vocabulary & Expression 2.2")]. Implementations that produce, maintain, publish or consume such vocabulary terms must take steps to ensure security and privacy considerations are addressed at the application level.

For a more complete view of those issues, cf. the [Security and Privacy Questionnaire for this specification](https://www.w3.org/2017/dxwg/wiki/ProfPrivacyAndSecurityQuestionnaire).

15. Changes[](https://www.w3.org/TR/dx-prof/#changes)
-----------------------------------------------------

_This section is non-normative._

### 15.1 Changes since last Public Draft[](https://www.w3.org/TR/dx-prof/#changes-since-2pwd)

Changes since the [Second Public Working Draft, 02 April 2019](https://www.w3.org/TR/2018/WD-dx-prof-20181218/), are:

*   Abstract shortened
*   Open Issues placed in relevant sections, not all at the start of the document
*   [§1. Introduction](https://www.w3.org/TR/dx-prof/#introduction) re-written to include reference to `dct:conformsTo` axiom
*   [§2.1 Diagram Conventions](https://www.w3.org/TR/dx-prof/#diagramconventions) added
*   [§3. Definitions](https://www.w3.org/TR/dx-prof/#definitions) added
*   [§4. Namespaces](https://www.w3.org/TR/dx-prof/#namespaces) includes a description of derivative namespaces namespace for auxiliary vocabulary elements
*   [§6. Related Work](https://www.w3.org/TR/dx-prof/#relatedwork) filled with content, as per placeholder issues
*   [§7. Conceptual Model](https://www.w3.org/TR/dx-prof/#conceptualmodel) diagram updated, a sentence about how individual communities may interpret `dct:conformsTo` added, a second & third Initial Example added
*   [§8. Vocabulary Specification](https://www.w3.org/TR/dx-prof/#specification) class & property definitions updated after much WG discussion, definitional phrasing aligned, some Usage Notes added, `dct:conformsTo` axiom added, diagrams updated
*   [§13. Alignments](https://www.w3.org/TR/dx-prof/#alignments) PROV alignment removed, OWL alignment still indicated incomplete with flagged Issue
*   [§14. Security and Privacy](https://www.w3.org/TR/dx-prof/#security_and_privacy) section completed
*   [§A. Appendices](https://www.w3.org/TR/dx-prof/#appendices) previous _Requirements_ section removed as not used

### 15.2 Features at risk[](https://www.w3.org/TR/dx-prof/#features-at-risk)

The following features of in this specification are considered AT RISK pending evidence of implementation:

Note

At the time of release of this specification as a _Working Group Note in December, 2019_, the list below contains all specification features since no implementation evidence has formally been gathered yet. This list will be reduced as evidence is documented.

*   `prof:Profile`
    *   `prof::hasResource`
    *   `prof:isProfileOf`
    *   `prof:isTransitiveProfileOf`
    *   `prof:hasToken`

*   `prof:ResourceDescriptor`
    *   `prof:hasArtifact`
    *   `dct:conformsTo`
    *   `dct:conformsTo`'s axiom: `dct:conformsTo owl:propertyChainAxiom ( prof:isProfileOf dct:conformsTo )`
    *   `dct:format`
    *   `prof:hasRole`
    *   `prof:isInheritedFrom`

*   `prof:ResourceRole`
*   `§ 9. Resource Role Instances` – all instances

A. Appendices[](https://www.w3.org/TR/dx-prof/#appendices)
----------------------------------------------------------

### A.1 Acknowledgements[](https://www.w3.org/TR/dx-prof/#acknowledgements)

The editors gratefully acknowledge the contributions made to this document by [all members of the working group](https://www.w3.org/2000/09/dbwg/details?group=99375&public=1), especially Antoine Isaac, Tom Baker, Simon Cox, Alejandra Gonzalez-Beltran, Andrea Perego.

The editors would also like to thank non-members of this working group for their comments, changes and ideas from which have been incorporated into this document. In particular: Paul Walk, Leslie Sikos, Stephen Richard, Kam Hay Fung, Heidi Vanparys and Irene Polikoff.

Finally, the editors also gratefully acknowledge the chairs of this Working Group: Karen Coyle and Peter Winstanley, former chair Caroline Burle and W3C staff contacts Phil Archer and Dave Raggett.

### A.2 Issue Summary[](https://www.w3.org/TR/dx-prof/#issue-summary)

*   [Issue 403](https://www.w3.org/TR/dx-prof/#issue-container-number-403): Reference OGC ModSpec
*   [Issue 573](https://www.w3.org/TR/dx-prof/#issue-container-number-573): Rename Resource Descriptor class
*   [Issue 1078](https://www.w3.org/TR/dx-prof/#issue-container-number-1078): Prof conformsTo axiom at risk
*   [Issue 842](https://www.w3.org/TR/dx-prof/#issue-container-number-842): Replace isInheritedFrom with a subproperty of rdfs:isDefinedBy
*   [Issue 857](https://www.w3.org/TR/dx-prof/#issue-container-number-857): What is the level of the inheritance link?
*   [Issue 1073](https://www.w3.org/TR/dx-prof/#issue-container-number-1073): Roles inclusion in PROF is at risk
*   [Issue 1048](https://www.w3.org/TR/dx-prof/#issue-container-number-1048): Should PROF roles be in a their own namespace?
*   [Issue 407](https://www.w3.org/TR/dx-prof/#issue-container-number-407): Prof Ont Test Suite tools
*   [Issue 405](https://www.w3.org/TR/dx-prof/#issue-container-number-405): Complete PROF/x alignments
*   [Issue 696](https://www.w3.org/TR/dx-prof/#issue-container-number-696): Alignment / differentiation with OWL
*   [Issue 403](https://www.w3.org/TR/dx-prof/#issue-container-number-403-0): Reference OGC ModSpec
*   [Issue 737](https://www.w3.org/TR/dx-prof/#issue-container-number-737): Refer to Open Geospatial Consortium Profiling
*   [Issue 791](https://www.w3.org/TR/dx-prof/#issue-container-number-791): PROF Voc & OGC Testbed 14: Characterization of RDF Application Profiles

B. References[](https://www.w3.org/TR/dx-prof/#references)
----------------------------------------------------------

### B.1 Normative references[](https://www.w3.org/TR/dx-prof/#normative-references)

[DCTERMS][DCMI Metadata Terms](http://dublincore.org/documents/dcmi-terms/). DCMI Usage Board. DCMI. 14 June 2012. DCMI Recommendation. URL: [http://dublincore.org/documents/dcmi-terms/](http://dublincore.org/documents/dcmi-terms/)[OWL2-OVERVIEW][OWL 2 Web Ontology Language Document Overview (Second Edition)](https://www.w3.org/TR/owl2-overview/). W3C OWL Working Group. W3C. 11 December 2012. W3C Recommendation. URL: [https://www.w3.org/TR/owl2-overview/](https://www.w3.org/TR/owl2-overview/)[RFC2119][Key words for use in RFCs to Indicate Requirement Levels](https://tools.ietf.org/html/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: [https://tools.ietf.org/html/rfc2119](https://tools.ietf.org/html/rfc2119)[RFC3986][Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986). T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard. URL: [https://tools.ietf.org/html/rfc3986](https://tools.ietf.org/html/rfc3986)[RFC3987][Internationalized Resource Identifiers (IRIs)](https://tools.ietf.org/html/rfc3987). M. Duerst; M. Suignard. IETF. January 2005. Proposed Standard. URL: [https://tools.ietf.org/html/rfc3987](https://tools.ietf.org/html/rfc3987)[RFC8174][Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://tools.ietf.org/html/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: [https://tools.ietf.org/html/rfc8174](https://tools.ietf.org/html/rfc8174)[SHACL][Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/). Holger Knublauch; Dimitris Kontokostas. W3C. 20 July 2017. W3C Recommendation. URL: [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/)[SKOS-REFERENCE][SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/). Alistair Miles; Sean Bechhofer. W3C. 18 August 2009. W3C Recommendation. URL: [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
### B.2 Informative references[](https://www.w3.org/TR/dx-prof/#informative-references)

[DCAP][Guidelines for Dublin Core Application Profiles](http://dublincore.org/documents/profile-guidelines/). Karen Coyle; Thomas Baker. DCMI. 18 May 2009. DCMI Recommended Resource. URL: [http://dublincore.org/documents/profile-guidelines/](http://dublincore.org/documents/profile-guidelines/)[DCAT-UCR][Dataset Exchange Use Cases and Requirements](https://www.w3.org/TR/dcat-ucr/). Jaroslav Pullmann; Rob Atkinson; Antoine Isaac; Ixchel Faniel. W3C. 17 January 2019. W3C Note. URL: [https://www.w3.org/TR/dcat-ucr/](https://www.w3.org/TR/dcat-ucr/)[DCDSP][Description Set Profiles: A constraint language for Dublin Core Application Profiles](http://dublincore.org/documents/dc-dsp/). Mikael Nilsson. DCMI. 31 March 2008. DCMI Working Draft. URL: [http://dublincore.org/documents/dc-dsp/](http://dublincore.org/documents/dc-dsp/)[DX-PROF-CONNEG][Content Negotiation by Profile](https://www.w3.org/TR/dx-prof-conneg/). Lars G. Svensson; Rob Atkinson; Nicholas Car. W3C. 30 April 2019. W3C Working Draft. URL: [https://www.w3.org/TR/dx-prof-conneg/](https://www.w3.org/TR/dx-prof-conneg/)[DX-PROF-GUIDANCE][Profile Guidance](https://w3c.github.io/dxwg/profiles/). 2018-12-31. W3C Editor's Draft. URL: [https://w3c.github.io/dxwg/profiles/](https://w3c.github.io/dxwg/profiles/)[DX-PROF-IETF][Indicating and Negotiating Profiles in HTTP](https://profilenegotiation.github.io/I-D-Profile-Negotiation/I-D-Profile-Negotiation). L. Svensson; R. Verborgh; H. Van de Sompel. 2019-11-20. IETF Internet-Draft. URL: [https://profilenegotiation.github.io/I-D-Profile-Negotiation/I-D-Profile-Negotiation](https://profilenegotiation.github.io/I-D-Profile-Negotiation/I-D-Profile-Negotiation)[GeoDCAT-AP][GeoDCAT-AP: A geospatial extension for the DCAT application profile for data portals in Europe. Version 1.0.1](https://joinup.ec.europa.eu/solution/geodcat-application-profile-data-portals-europe). European Commission. 2 August 2016. URL: [https://joinup.ec.europa.eu/solution/geodcat-application-profile-data-portals-europe](https://joinup.ec.europa.eu/solution/geodcat-application-profile-data-portals-europe)[ISO-19115-1-2014][Geographic information -- Metadata -- Part 1: Fundamentals](https://www.iso.org/standard/53798.html). ISO/TC 211. ISO. 2014. International Standard. URL: [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)[MODSPEC][The Specification Model — A Standard for Modular specifications](http://www.opengeospatial.org/standards/modularspec). 2009-10-19. OGC Policy Directive. URL: [http://www.opengeospatial.org/standards/modularspec](http://www.opengeospatial.org/standards/modularspec)[ODRL-VOCAB][ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/). Renato Iannella; Michael Steidl; Stuart Myles; Víctor Rodríguez-Doncel. W3C. 15 February 2018. W3C Recommendation. URL: [https://www.w3.org/TR/odrl-vocab/](https://www.w3.org/TR/odrl-vocab/)[OWL2-PRIMER][OWL 2 Web Ontology Language Primer (Second Edition)](https://www.w3.org/TR/owl2-primer/). Pascal Hitzler; Markus Krötzsch; Bijan Parsia; Peter Patel-Schneider; Sebastian Rudolph. W3C. 11 December 2012. W3C Recommendation. URL: [https://www.w3.org/TR/owl2-primer/](https://www.w3.org/TR/owl2-primer/)[owl2-rdf-based-semantics][OWL 2 Web Ontology Language RDF-Based Semantics (Second Edition)](https://www.w3.org/TR/owl2-rdf-based-semantics/). Michael Schneider. W3C. 11 December 2012. W3C Recommendation. URL: [https://www.w3.org/TR/owl2-rdf-based-semantics/](https://www.w3.org/TR/owl2-rdf-based-semantics/)[PDF][Document management -- Portable document format -- Part 1: PDF 1.7](https://www.iso.org/standard/51502.html). 2008-07. ISO Standard. URL: [https://www.iso.org/standard/51502.html](https://www.iso.org/standard/51502.html)[PROV-O][PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/). Timothy Lebo; Satya Sahoo; Deborah McGuinness. W3C. 30 April 2013. W3C Recommendation. URL: [https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/)[RDF-SCHEMA][RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/). Dan Brickley; Ramanathan Guha. W3C. 25 February 2014. W3C Recommendation. URL: [https://www.w3.org/TR/rdf-schema/](https://www.w3.org/TR/rdf-schema/)[RDF11-CONCEPTS][RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/). Richard Cyganiak; David Wood; Markus Lanthaler. W3C. 25 February 2014. W3C Recommendation. URL: [https://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/)[SCHEMATRON][ISO/IEC 19757-3:2016 Information technology -- Document Schema Definition Languages (DSDL) -- Part 3: Rule-based validation -- Schematron](https://www.iso.org/standard/55982.html). 2016-01. ISO Standard. URL: [https://www.iso.org/standard/55982.html](https://www.iso.org/standard/55982.html)[SHEX][Shape Expressions Language 2.next](https://shexspec.github.io/spec/). 2019-08-31. W3C Community Group Draft Report. URL: [https://shexspec.github.io/spec/](https://shexspec.github.io/spec/)[SKOS-PRIMER][SKOS Simple Knowledge Organization System Primer](https://www.w3.org/TR/skos-primer/). Antoine Isaac; Ed Summers. W3C. 18 August 2009. W3C Note. URL: [https://www.w3.org/TR/skos-primer/](https://www.w3.org/TR/skos-primer/)[StatDCAT-AP][StatDCAT-AP – DCAT Application Profile for description of statistical datasets. Version 1.0.1](https://joinup.ec.europa.eu/solution/statdcat-application-profile-data-portals-europe). European Commission. 28 May 2019. URL: [https://joinup.ec.europa.eu/solution/statdcat-application-profile-data-portals-europe](https://joinup.ec.europa.eu/solution/statdcat-application-profile-data-portals-europe)[VOAF][Vocabulary of a Friend (VOAF)](http://purl.org/vocommons/voaf). Bernard Vatant. OKFN. 24 May 2013. URL: [http://purl.org/vocommons/voaf](http://purl.org/vocommons/voaf)[VOCAB-ADMS][Asset Description Metadata Schema (ADMS)](https://www.w3.org/TR/vocab-adms/). Phil Archer; Gofran Shukair. W3C. 1 August 2013. W3C Note. URL: [https://www.w3.org/TR/vocab-adms/](https://www.w3.org/TR/vocab-adms/)[VOCAB-DCAT][Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat/). Fadi Maali; John Erickson. W3C. 16 January 2014. W3C Recommendation. URL: [https://www.w3.org/TR/vocab-dcat/](https://www.w3.org/TR/vocab-dcat/)[VOCAB-DCAT-2][Data Catalog Vocabulary (DCAT) - Version 2](https://www.w3.org/TR/vocab-dcat-2/). Riccardo Albertoni; David Browning; Simon Cox; Alejandra Gonzalez Beltran; Andrea Perego; Peter Winstanley. W3C. 28 May 2019. W3C Working Draft. URL: [https://www.w3.org/TR/vocab-dcat-2/](https://www.w3.org/TR/vocab-dcat-2/)[VOID][Describing Linked Datasets with the VoID Vocabulary](https://www.w3.org/TR/void/). Keith Alexander; Richard Cyganiak; Michael Hausenblas; Jun Zhao. W3C. 3 March 2011. W3C Note. URL: [https://www.w3.org/TR/void/](https://www.w3.org/TR/void/)