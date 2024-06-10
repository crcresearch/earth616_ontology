import os
import rdflib
from pyshacl import validate
from termcolor import colored

# Define paths
SHAPES_FILE = os.path.join(os.path.dirname(__file__), 'shacl-tests.ttl')
CONFORMING_DIR = os.path.join(os.path.dirname(__file__), 'conforming')
FAILING_DIR = os.path.join(os.path.dirname(__file__), 'failing')

def extract_rule_metadata(shapes_graph):
    rules = []
    for shape in shapes_graph.subjects(rdflib.RDF.type, rdflib.URIRef('http://www.w3.org/ns/shacl#NodeShape')):
        label = shapes_graph.value(shape, rdflib.RDFS.label)
        note = shapes_graph.value(shape, rdflib.URIRef('http://www.w3.org/2004/02/skos/core#note'))
        rules.append((label, note))
    return rules

def validate_file(file_path, shapes_file):
    data_graph = rdflib.Graph()
    data_graph.parse(file_path, format='ttl')
    shapes_graph = rdflib.Graph()
    shapes_graph.parse(shapes_file, format='ttl')
    conforms, results_graph, results_text = validate(
        data_graph=data_graph, 
        shacl_graph=shapes_graph, 
        inference=None,  # No inferencing
        abort_on_first=False, 
        meta_shacl=False, 
        advanced=True
    )
    return conforms, results_graph, results_text, data_graph, shapes_graph

def run_tests():
    all_passed = True

    # Validate conforming test cases
    print(colored("Validating conforming test cases:", 'blue'))
    conforming_files = os.listdir(CONFORMING_DIR)
    if not conforming_files:
        print(colored("No conforming test cases found.", 'yellow'))
    for file_name in conforming_files:
        file_path = os.path.join(CONFORMING_DIR, file_name)
        conforms, results_graph, results_text, data_graph, shapes_graph = validate_file(file_path, SHAPES_FILE)
        note = data_graph.value(subject=None, predicate=rdflib.URIRef('http://www.w3.org/2004/02/skos/core#note'))
        rules = extract_rule_metadata(shapes_graph)
        if conforms:
            print(colored(f"Conforming test passed for {file_name}: {note}", 'green'))
        else:
            print(colored(f"Conforming test failed for {file_name}: {note}", 'red'))
            print(results_text)
            all_passed = False
        print(colored("Applied Rules:", 'cyan'))
        for label, rule_note in rules:
            print(f"  - {label}: {rule_note}")

    # Validate failing test cases
    print(colored("Validating failing test cases:", 'blue'))
    failing_files = os.listdir(FAILING_DIR)
    if not failing_files:
        print(colored("No failing test cases found.", 'yellow'))
    for file_name in failing_files:
        file_path = os.path.join(FAILING_DIR, file_name)
        conforms, results_graph, results_text, data_graph, shapes_graph = validate_file(file_path, SHAPES_FILE)
        note = data_graph.value(subject=None, predicate=rdflib.URIRef('http://www.w3.org/2004/02/skos/core#note'))
        rules = extract_rule_metadata(shapes_graph)
        if not conforms:
            print(colored(f"Failing test passed (correctly failed) for {file_name}: {note}", 'green'))
        else:
            print(colored(f"Failing test failed (incorrectly passed) for {file_name}: {note}", 'red'))
            print(results_text)
            all_passed = False
        print(colored("Applied Rules:", 'cyan'))
        for label, rule_note in rules:
            print(f"  - {label}: {rule_note}")

    if all_passed:
        print(colored("All tests passed.", 'green'))
    else:
        print(colored("Some tests failed.", 'red'))

if __name__ == "__main__":
    run_tests()