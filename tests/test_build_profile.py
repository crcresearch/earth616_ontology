import os
from pathlib import Path

import pytest
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL

from scripts.build_profile import build_profile, read_ontology_iri


def test_read_ontology_iri():
    # Read the ontology IRI from the core metadata file
    iri = read_ontology_iri('modules/core/metadata.ttl')
    assert iri.startswith('https://schema-earth616-ks18.blocks.simbachain.com/nd/scdoc/ont/')
    # Should be an absolute HTTP(s) IRI
    assert iri.startswith('http')


def test_build_profile(tmp_path):
    # Output path
    out = tmp_path / 'profile.ttl'
    # Build the profile
    build_profile(
        metadata_path='modules/core/metadata.ttl',
        modules_txt='tests/modules.txt',
        out_path=str(out)
    )
    # Ensure file created
    assert out.exists(), "Profile TTL was not written"

    # Load into graph
    g = Graph()
    g.parse(str(out), format='turtle')

    # Extract ontology IRI to build expected module IRIs
    base_iri = read_ontology_iri('modules/core/metadata.ttl')

    # Read tests/modules.txt for expected modules
    expected = []
    with open('tests/modules.txt') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            _, path = line.split(',', 1)
            rel = os.path.relpath(path.strip(), 'modules').replace(os.path.sep, '/')
            rel_no_ext = os.path.splitext(rel)[0]
            expected.append(f"{base_iri}modules/{rel_no_ext}")

    # The profile should declare one PROFILE subject equal to the ontology IRI
    profile_iri = URIRef(read_ontology_iri('modules/core/metadata.ttl'))
    assert (profile_iri, RDF.type, PROF.Profile) in g, "Top-level prof:Profile missing"
    # For each expected module IRI, ensure a ResourceDescriptor links the profile to the module
    for iri in expected:
        module_iri = URIRef(iri)
        # find a descriptor node that has prof:hasArtifact = module_iri
        found = False
        for desc in g.objects(subject=profile_iri, predicate=PROF.hasResource):
            if (desc, PROF.hasArtifact, module_iri) in g and (desc, PROF.hasRole, LODE.config) in g:
                found = True
                break
        assert found, f"Missing resource descriptor for module {iri}"