import os
import sys
import rdflib
from pyshacl import validate
from termcolor import colored

# Define paths
MODULES_LIST = os.path.join(os.path.dirname(__file__), '../tests/modules.txt')
SHAPES_FILE = os.path.join(os.path.dirname(__file__), '../tests/ontology-validation-shapes.ttl')
LOG_FILE = 'validation_log.txt'

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

def validate_individual_file(file_path, shapes_file, log_file):
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
            with open(log_file, 'a') as log:
                log.write(f"\nSHACL validation results for {file_path}:\n")
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
                    log.write(f"Focus Node: {focus_node}\n")
                    log.write(f"Path: {path}\n")
                    log.write(f"Message: {message}\n")
        return conforms
    except Exception as e:
        print(colored(f"SHACL validation error for {file_path}: {e}", 'red'))
        return False

def main():
    all_passed = True
    detailed_failures = []

    # Clear previous log file
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    # Read the list of modules from the file
    files = read_modules_file(MODULES_LIST)

    # Validate individual Turtle files for syntax errors
    for file_path in files:
        if not validate_turtle_file(file_path):
            all_passed = False

    # Validate each individual Turtle file with SHACL
    for file_path in files:
        if not validate_individual_file(file_path, SHAPES_FILE, LOG_FILE):
            all_passed = False
            detailed_failures.append(file_path)

    if all_passed:
        print(colored("All validations passed.", 'green'))
    else:
        print(colored("Some validations failed.", 'red'))
        print(colored("See detailed log in validation_log.txt", 'yellow'))
        print(colored(f"Files with SHACL validation errors: {', '.join(detailed_failures)}", 'red'))

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()