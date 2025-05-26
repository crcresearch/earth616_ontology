#!/usr/bin/env python3
"""
Build PROF profile index by processing templates with environment configuration and 
generating both index.ttl (PROF profile) and pylode-config.ttl files.
"""
import os
import sys
import argparse
import yaml
import subprocess
from pathlib import Path

def load_environment_config(config_path):
    """Load environment configuration YAML."""
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        sys.stderr.write(f"Error loading config '{config_path}': {e}\n")
        sys.exit(1)

def process_template(template_path, output_path, env_vars):
    """Process template file using envsubst with environment variables."""
    try:
        # Set environment variables for envsubst
        env = os.environ.copy()
        env.update(env_vars)
        
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        # Use envsubst to substitute variables
        result = subprocess.run(
            ['envsubst'], 
            input=template_content, 
            text=True, 
            capture_output=True,
            env=env
        )
        
        if result.returncode != 0:
            sys.stderr.write(f"envsubst error: {result.stderr}\n")
            sys.exit(1)
            
        with open(output_path, 'w') as f:
            f.write(result.stdout)
            
        print(f"Generated {output_path} from template {template_path}")
        
    except Exception as e:
        sys.stderr.write(f"Error processing template '{template_path}': {e}\n")
        sys.exit(1)

def generate_prof_artifacts(profile_template, pylode_config_template, output_dir, env_config):
    """Generate PROF profile and pyLODE config from templates."""
    
    # Prepare environment variables
    env_vars = {}
    
    # Add template variables from config
    if 'ONTOLOGY_BASE' in env_config:
        env_vars['ONTOLOGY_BASE'] = env_config['ONTOLOGY_BASE']
    elif 'uri_bases' in env_config and 'ontology' in env_config['uri_bases']:
        env_vars['ONTOLOGY_BASE'] = env_config['uri_bases']['ontology']
    
    if 'CONTEXT_BASE' in env_config:
        env_vars['CONTEXT_BASE'] = env_config['CONTEXT_BASE']
    elif 'uri_bases' in env_config and 'context' in env_config['uri_bases']:
        env_vars['CONTEXT_BASE'] = env_config['uri_bases']['context']
        
    if 'SHAPES_BASE' in env_config:
        env_vars['SHAPES_BASE'] = env_config['SHAPES_BASE']
    elif 'uri_bases' in env_config and 'shapes' in env_config['uri_bases']:
        env_vars['SHAPES_BASE'] = env_config['uri_bases']['shapes']
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate index.ttl (PROF profile)
    index_output = os.path.join(output_dir, 'index.ttl')
    process_template(profile_template, index_output, env_vars)
    
    # Generate pylode-config.ttl
    pylode_output = os.path.join(output_dir, 'pylode-config.ttl')
    process_template(pylode_config_template, pylode_output, env_vars)
    
    return index_output, pylode_output

def main():
    parser = argparse.ArgumentParser(
        description="Build PROF profile index and pyLODE config from templates and environment config"
    )
    parser.add_argument('--env-config', '-e', required=True,
                        help='Path to environment configuration YAML file')
    parser.add_argument('--profile-template', '-p', required=True,
                        help='Path to PROF profile template file')
    parser.add_argument('--pylode-template', '-l', required=True,
                        help='Path to pyLODE config template file')
    parser.add_argument('--out-dir', '-o', required=True,
                        help='Output directory for generated files')
    args = parser.parse_args()

    # Load environment configuration
    env_config = load_environment_config(args.env_config)
    
    # Generate artifacts
    index_path, pylode_path = generate_prof_artifacts(
        args.profile_template,
        args.pylode_template, 
        args.out_dir,
        env_config
    )
    
    print(f"PROF artifacts generated:")
    print(f"  Index: {index_path}")
    print(f"  pyLODE config: {pylode_path}")

if __name__ == '__main__':
    main()