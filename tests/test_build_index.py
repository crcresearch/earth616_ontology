import textwrap
from pathlib import Path

import pytest
from rdflib import URIRef
from rdflib.namespace import OWL

from scripts.build_index import build_index_graph


def test_build_index_basic(tmp_path):
    # Prepare metadata TTL with a simple ontology declaration
    metadata = tmp_path / "metadata.ttl"
    metadata.write_text(textwrap.dedent("""
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix owl: <http://www.w3.org/2002/07/owl#> .
        <http://example.org/ont/> a owl:Ontology .
    """))

    # Prepare modules directory with one module TTL and one OWL
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    (modules_dir / "alpha.ttl").write_text(textwrap.dedent("""
        @prefix : <http://example.org/ont/modules/alpha#> .
        :AClass a owl:Class .
    """))
    (modules_dir / "beta.owl").write_text(textwrap.dedent("""
        @prefix : <http://example.org/ont/modules/beta#> .
        :BClass a owl:Class .
    """))

    # Prepare patterns directory with one pattern TTL
    patterns_dir = tmp_path / "patterns"
    patterns_dir.mkdir()
    (patterns_dir / "xpattern.ttl").write_text(textwrap.dedent("""
        @prefix : <http://example.org/ont/patterns/xpattern#> .
        :PatternX a owl:Class .
    """))

    # Build the index graph
    graph = build_index_graph(str(metadata), str(modules_dir), str(patterns_dir))
    ontology_iri = URIRef("http://example.org/ont/")

    # Verify that each module and pattern import is present
    expected_modules = ["alpha", "beta"]
    for name in expected_modules:
        iri = URIRef(f"http://example.org/ont/modules/{name}")
        assert (ontology_iri, OWL.imports, iri) in graph, f"Missing import for module {name}"

    # Verify pattern import
    pattern_iri = URIRef("http://example.org/ont/patterns/xpattern")
    assert (ontology_iri, OWL.imports, pattern_iri) in graph, "Missing import for pattern xpattern"


def test_no_metadata_fails(tmp_path):
    # Missing ontology declaration should exit
    metadata = tmp_path / "empty.ttl"
    metadata.write_text("")
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    with pytest.raises(SystemExit):
        build_index_graph(str(metadata), str(modules_dir))