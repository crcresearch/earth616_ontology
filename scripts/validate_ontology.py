import os
import sys
import rdflib
from pyshacl import validate
from termcolor import colored

# Define paths
MODULES_LIST = os.path.join(os.path.dirname(__file__), '../tests/modules.txt')
SHAPES_FILE = os.path.join(os.path.dirname(__file__), '../tests/ontology-validation-shapes.ttl')

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

def validate_individual_file(file_path, shapes_file):
    try:
        data_graph = rdflib.Graph()
        data_graph.parse(file_path, format='ttl')
        
        conforms, results_graph, results_text = validate(
            data_graph=data_graph, 
            shacl_graph=shapes_file, 
            inference='rdfs', 
            abort_on_first=False, 
            meta_shacl=False, 
            advanced=True
        )
        
        if conforms:
            print(colored(f"SHACL validation passed for {file_path}", 'green'))
        else:
            print(colored(f"SHACL validation failed for {file_path}", 'red'))
            for result in results_graph.query("""
                SELECT ?focusNode ?message ?path
                WHERE {
                    ?result a sh:ValidationResult ;
                            sh:focusNode ?focusNode ;
                            sh:resultMessage ?message ;
                            sh:resultPath ?path .
                }
            """):
                focus_node, message, path = result
                print(colored(f"Focus Node: {focus_node}", 'red'))
                print(colored(f"Path: {path}", 'red'))
                print(colored(f"Message: {message}", 'red'))
        return conforms
    except Exception as e:
        print(colored(f"SHACL validation error for {file_path}: {e}", 'red'))
        return False

def main():
    all_passed = True

    # Read the list of modules from the file
    files = read_modules_file(MODULES_LIST)

    # Validate individual Turtle files for syntax errors
    for file_path in files:
        if not validate_turtle_file(file_path):
            all_passed = False

    # Validate each individual Turtle file with SHACL
    for file_path in files:
        if not validate_individual_file(file_path, SHAPES_FILE):
            all_passed = False

    if all_passed:
        print(colored("All validations passed.", 'green'))
        sys.exit(0)
    else:
        print(colored("Some validations failed.", 'red'))
        sys.exit(1)

if __name__ == "__main__":
    main()