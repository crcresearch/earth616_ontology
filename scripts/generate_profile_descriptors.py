#!/usr/bin/env python3
"""
Dynamic Profile Generator - Extracts rich metadata from module templates
and generates ResourceDescriptor entries for the profile.

Uses OPLaX patterns, semantic annotations, and dependency analysis.
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Set, Optional
from collections import defaultdict

try:
    from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD, URIRef, Literal
    from rdflib.namespace import DCTERMS, SKOS
except ImportError:
    print("Warning: rdflib not available, using fallback text parsing")
    Graph = None

# Define namespaces
OPLAX = Namespace("http://ontologydesignpatterns.org/opla-core#")
CPA = Namespace("http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl#")
SCHEMA = Namespace("https://schema.org/")
DSCDO = Namespace("http://example.org/ont/")  # Placeholder for template processing

def preprocess_template(template_path: Path) -> str:
    """Read template and substitute variables for RDF parsing."""
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace template variables with dummy URIs for parsing
    content = content.replace('${ONTOLOGY_BASE}', 'http://example.org/ont')
    content = content.replace('${CONTEXT_BASE}', 'http://example.org/context')
    content = content.replace('${SHAPES_BASE}', 'http://example.org/shapes')
    
    return content

def extract_module_path_from_template(template_path: Path) -> str:
    """Extract module path from template file path."""
    # Convert templates/modules/scdocumentation/document-chunks.ttl.template
    # to scdocumentation/document-chunks
    rel_path = str(template_path).split('templates/modules/')[1]
    return rel_path.replace('.ttl.template', '')

def extract_module_metadata_rdflib(template_path: Path) -> Dict:
    """Extract metadata using rdflib RDF parsing."""
    try:
        content = preprocess_template(template_path)
        g = Graph()
        g.parse(data=content, format='turtle')
        
        metadata = {
            'path': extract_module_path_from_template(template_path),
            'template_path': str(template_path),
        }
        
        # Find the module ontology URI
        ontology_uris = list(g.subjects(RDF.type, OWL.Ontology))
        if not ontology_uris:
            print(f"Warning: No owl:Ontology found in {template_path}")
            return metadata
            
        ontology = ontology_uris[0]
        
        # Extract basic metadata
        metadata.update({
            'ontology_uri': str(ontology),
            'label': str(g.value(ontology, RDFS.label) or ""),
            'comment': str(g.value(ontology, RDFS.comment) or ""),
            'creator': str(g.value(ontology, DCTERMS.creator) or ""),
            'created': str(g.value(ontology, DCTERMS.created) or ""),
            'source': str(g.value(ontology, DCTERMS.source) or ""),
            'version': str(g.value(ontology, OWL.versionInfo) or ""),
        })
        
        # Extract imports and dependencies
        imports = [str(imp) for imp in g.objects(ontology, OWL.imports)]
        metadata['imports'] = imports
        metadata['module_imports'] = [imp for imp in imports if '/modules/' in imp]
        metadata['pattern_imports'] = [imp for imp in imports if '/patterns/' in imp]
        
        # Check if this is a pattern
        is_pattern = (ontology, RDF.type, OPLAX.Pattern) in g
        metadata['is_pattern'] = is_pattern
        
        if is_pattern:
            metadata.update({
                'pattern_name': str(g.value(ontology, OPLAX.hasPatternName) or ""),
                'addresses_scenario': str(g.value(ontology, OPLAX.addressesScenario) or ""),
                'has_intent': str(g.value(ontology, CPA.hasIntent) or ""),
            })
        
        return metadata
        
    except Exception as e:
        print(f"Warning: Failed to parse {template_path} with rdflib: {e}")
        return extract_module_metadata_fallback(template_path)

def extract_module_metadata_fallback(template_path: Path) -> Dict:
    """Fallback text-based metadata extraction."""
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = {
        'path': extract_module_path_from_template(template_path),
        'template_path': str(template_path),
    }
    
    # Extract basic metadata using regex
    label_match = re.search(r'rdfs:label\s+"([^"]+)"', content)
    if label_match:
        metadata['label'] = label_match.group(1)
    
    comment_match = re.search(r'rdfs:comment\s+"([^"]+)"', content)
    if comment_match:
        metadata['comment'] = comment_match.group(1)
    
    # Extract imports
    import_matches = re.findall(r'owl:imports\s+<[^>]*/(modules/[^>]+)>', content)
    metadata['module_imports'] = import_matches
    
    pattern_matches = re.findall(r'owl:imports\s+<[^>]*/(patterns/[^>]+)>', content)
    metadata['pattern_imports'] = pattern_matches
    
    return metadata

def extract_module_metadata(template_path: Path) -> Dict:
    """Extract metadata from module template."""
    if Graph is not None:
        return extract_module_metadata_rdflib(template_path)
    else:
        return extract_module_metadata_fallback(template_path)

def build_dependency_graph(modules_metadata: List[Dict]) -> Dict[str, Set[str]]:
    """Build module dependency graph from imports."""
    graph = defaultdict(set)
    path_to_metadata = {m['path']: m for m in modules_metadata}
    
    for module in modules_metadata:
        deps = set()
        for imp in module.get('module_imports', []):
            # Extract module path from import URI
            if '/modules/' in imp:
                dep_path = imp.split('/modules/')[1]
                if dep_path in path_to_metadata:
                    deps.add(dep_path)
        graph[module['path']] = deps
    
    return dict(graph)

def topological_sort_with_categories(dependency_graph: Dict[str, Set[str]], modules_metadata: List[Dict]) -> List[Dict]:
    """Topological sort with category-based ordering."""
    
    # Category order (lower numbers = earlier in build)
    category_order = {
        'core': 1,
        'scdocumentation': 2,
        'supplychain': 3,
        'traceability': 4,
        'design': 5,
        'spdx': 6,
        'imports': 7,
    }
    
    path_to_metadata = {m['path']: m for m in modules_metadata}
    
    # Simple topological sort with category weighting
    visited = set()
    result = []
    
    def visit(path):
        if path in visited or path not in path_to_metadata:
            return
        visited.add(path)
        
        # Visit dependencies first
        for dep in dependency_graph.get(path, set()):
            visit(dep)
        
        result.append(path_to_metadata[path])
    
    # Sort modules by category first, then visit in dependency order
    modules_by_category = sorted(modules_metadata, key=lambda m: (
        category_order.get(m['path'].split('/')[0], 99),
        m['path']
    ))
    
    for module in modules_by_category:
        visit(module['path'])
    
    return result

def determine_module_role(module_metadata: Dict) -> Optional[str]:
    """Determine PROF role based on module characteristics."""
    path = module_metadata['path']
    
    if path.startswith('core/'):
        return 'role:specification'
    elif path.startswith('design/'):
        return 'role:constraints'
    elif path.startswith('scdocumentation/'):
        return 'role:specification'
    elif path.startswith('traceability/'):
        return 'role:validation'
    elif path.startswith('imports/'):
        return 'role:vocabulary'
    
    return None

def detect_module_relationships(module_metadata: Dict, all_modules: List[Dict]) -> Dict[str, List[str]]:
    """Detect extends/constrains relationships between modules."""
    relationships = {
        'extends': [],
        'constrains': [],
        'enables': [],
        'validates_against': []
    }
    
    path = module_metadata['path']
    comment = module_metadata.get('comment', '').lower()
    
    # Heuristic relationship detection
    if 'extends' in comment or 'extension' in comment:
        # Look for base modules this might extend
        if path.startswith('design/') and 'scdocumentation/document' in [m['path'] for m in all_modules]:
            relationships['extends'].append('${ONTOLOGY_BASE}/modules/scdocumentation/document')
    
    if 'constrain' in comment or 'validation' in comment:
        # Look for modules this might constrain
        if 'tru' in comment.lower() and 'traceability/tru' in [m['path'] for m in all_modules]:
            relationships['constrains'].append('${ONTOLOGY_BASE}/modules/traceability/tru')
    
    return relationships

def generate_resource_descriptor(module_metadata: Dict, order: int, all_modules: List[Dict]) -> str:
    """Generate a single ResourceDescriptor entry."""
    
    label = module_metadata.get('label') or title_case(module_metadata['path'])
    comment = module_metadata.get('comment') or f"Module for {module_metadata['path']}"
    
    # Clean up long comments
    if len(comment) > 200:
        comment = comment[:197] + "..."
    
    descriptor = f'''    prof:hasResource [
        a prof:ResourceDescriptor ;
        rdfs:label "{label}" ;
        rdfs:comment "{comment}" ;
        dcterms:format "text/turtle" ;
        prof:hasArtifact <${{ONTOLOGY_BASE}}/modules/{module_metadata['path']}> ;'''
    
    # Add role if detected
    role = determine_module_role(module_metadata)
    if role:
        descriptor += f'\n        prof:hasRole {role} ;'
    
    # Add relationships
    relationships = detect_module_relationships(module_metadata, all_modules)
    for rel_type, targets in relationships.items():
        if targets:
            targets_str = ', '.join(f'<{target}>' for target in targets)
            prop_name = f'dscdo:{rel_type.replace("_", "")}'
            if rel_type == 'validates_against':
                prop_name = 'dscdo:validatesAgainst'
            elif rel_type == 'enables':
                prop_name = 'dscdo:enablesModule'
                
            descriptor += f'\n        {prop_name} {targets_str} ;'
    
    descriptor += f'\n        sh:order {order} ;\n    ] ;'
    
    return descriptor

def title_case(path: str) -> str:
    """Convert module path to title case."""
    return path.replace('/', ' ').replace('-', ' ').title() + ' Module'

def discover_module_templates(templates_dir: Path) -> List[Path]:
    """Discover all module templates."""
    templates = []
    modules_dir = templates_dir / 'modules'
    
    if modules_dir.exists():
        for template in modules_dir.rglob('*.ttl.template'):
            # Skip profile templates
            if 'profile' not in template.name:
                templates.append(template)
    
    return sorted(templates)

def generate_profile_descriptors(templates_dir: Path) -> str:
    """Main function to generate profile descriptors."""
    
    print(f"Discovering module templates in {templates_dir}")
    template_paths = discover_module_templates(templates_dir)
    
    if not template_paths:
        print("No module templates found")
        return ""
    
    print(f"Found {len(template_paths)} module templates")
    
    # Extract metadata from all modules
    modules_metadata = []
    for template_path in template_paths:
        print(f"Processing: {template_path}")
        metadata = extract_module_metadata(template_path)
        if metadata.get('label'):  # Only include modules with labels
            modules_metadata.append(metadata)
        else:
            print(f"  Warning: No label found, skipping")
    
    if not modules_metadata:
        print("No valid modules found")
        return ""
    
    # Build dependency graph and sort
    dependency_graph = build_dependency_graph(modules_metadata)
    ordered_modules = topological_sort_with_categories(dependency_graph, modules_metadata)
    
    print(f"Generated dependency ordering for {len(ordered_modules)} modules")
    
    # Generate ResourceDescriptor entries
    descriptors = []
    for i, module in enumerate(ordered_modules, 1):
        descriptor = generate_resource_descriptor(module, i, ordered_modules)
        descriptors.append(descriptor)
        print(f"  {i:2d}. {module['path']} - {module.get('label', 'No label')}")
    
    return '\n\n'.join(descriptors)

def main():
    """Command line interface."""
    if len(sys.argv) != 2:
        print("Usage: python generate_profile_descriptors.py <templates_dir>")
        sys.exit(1)
    
    templates_dir = Path(sys.argv[1])
    if not templates_dir.exists():
        print(f"Templates directory not found: {templates_dir}")
        sys.exit(1)
    
    descriptors = generate_profile_descriptors(templates_dir)
    
    if descriptors:
        print("\n" + "="*80)
        print("GENERATED RESOURCE DESCRIPTORS:")
        print("="*80)
        print(descriptors)
    else:
        print("No descriptors generated")
        sys.exit(1)

if __name__ == '__main__':
    main()