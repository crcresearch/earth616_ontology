# Deprecated Modules Directory

This directory contains the legacy module files that are no longer used for development.

## Migration to Template-Based Development

As of version 0.1.4, development has moved to a template-based approach:

- **Old location**: `modules/` (this directory)
- **New location**: `templates/modules/` (source templates)
- **Generated output**: `release/ontology/{version}/` (built modules)

## What Changed

1. **Template-based development**: All modules are now defined as templates in `templates/modules/` with environment variable substitution
2. **Build process**: Use `build-release-enhanced.sh` instead of `build-release.sh`
3. **URI configuration**: URIs are now configurable via environment files in `config/environments/`

## Migration Path

If you need to reference these old modules:
1. Check if equivalent templates exist in `templates/modules/`
2. If not, create new templates based on these files
3. Update any references to use the new build process

This directory will be removed in a future release once all migration is complete.