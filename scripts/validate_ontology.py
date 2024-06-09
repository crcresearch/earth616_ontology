# validate_ontology.py
import os
import sys
import rdflib
from pyshacl import validate
from termcolor import colored

# Define paths
MODULES_LIST = os.path.join(os.path.dirname(__file__), '../tests/modules.txt')
SHAPES_FILE = os.path.join(os.path.dirname(__file__), '../tests/ontology-validation-shapes.ttl')
MERGED_ONTOLOGY_FILE = os.path.join(os.path.dirname(__file__), 'merged.ttl')

def read_modules_file(modules_file):
    with open(modules_file, 'r') as f:
        files = [line.strip().split(',')[1] for line in f.readlines()]
    return files

def validate_turtle_file(file_path):
    try:
        graph = rdflib.Graph()
        graph.parse(file_path, format='ttl')
        print(colored(f"Syntax validation passed for {file_path}", 'green'))
        return True
    except Exception as e:
        print(colored(f"Syntax validation failed for {file_path}: {e}", 'red'))
        return False

def merge_ontology(files, output_file):
    try:
        with open(output_file, 'w') as outfile:
            for file in files:
                with open(file) as infile:
                    outfile.write(infile.read() + "\n")
        print(colored(f"Ontology files merged into {output_file}", 'green'))
        return True
    except Exception as e:
        print(colored(f"Failed to merge ontology files: {e}", 'red'))
        return False

def validate_ontology(shapes_file, ontology_file):
    try:
        conforms, results_graph, results_text = validate(data_graph=ontology_file, shacl_graph=shapes_file, inference='rdfs', abort_on_first=False, meta_shacl=False, advanced=True)
        if conforms:
            print(colored("SHACL validation passed.", 'green'))
        else:
            print(colored("SHACL validation failed.", 'red'))
        print(results_text)
        return conforms
    except Exception as e:
        print(colored(f"SHACL validation error: {e}", 'red'))
        return False

def main():
    all_passed = True

    # Read the list of modules from the file
    files = read_modules_file(MODULES_LIST)

    # Validate individual Turtle files
    for file_path in files:
        if not validate_turtle_file(file_path):
            all_passed = False

    # Merge ontology files for SHACL validation
    if not merge_ontology(files, MERGED_ONTOLOGY_FILE):
        all_passed = False

    # Validate merged ontology with SHACL
    if not validate_ontology(SHAPES_FILE, MERGED_ONTOLOGY_FILE):
        all_passed = False

    if all_passed:
        print(colored("All validations passed.", 'green'))
        sys.exit(0)
    else:
        print(colored("Some validations failed.", 'red'))
        sys.exit(1)

if __name__ == "__main__":
    main()