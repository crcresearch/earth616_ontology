# Release Notes - Version 0.1.4

## Repository Cleanup and Template Migration

This release completes the migration to template-based development and cleans up deprecated artifacts.

### Major Changes

#### 🔧 Build System Migration
- **REMOVED**: `build-release.sh` (deprecated build script)
- **ENHANCED**: `build-release-enhanced.sh` now supports full CogitareLink layer model
- **FIXED**: Version detection now uses `templates/modules/core/ontology.ttl.template`

#### 📁 Directory Structure Cleanup
- **DEPRECATED**: `/modules/` → moved to `/modules-deprecated/` with migration guide
- **ACTIVE**: `/templates/modules/` - primary development location for ontology modules
- **GENERATED**: `/release/ontology/{version}/` - output of build process

#### 📖 Documentation Updates
- **UPDATED**: `CLAUDE.md` with current template-based development workflow
- **ADDED**: Clear migration guidance from old `/modules/` to new template system
- **CLARIFIED**: CogitareLink four-layer model implementation

### Development Process Changes

#### Template-Based Development (NEW)
```bash
# ❌ OLD: Direct module editing
nano modules/core/event.ttl

# ✅ NEW: Template-based development  
nano templates/modules/core/event.ttl.template
./build-release-enhanced.sh --env=local --layers=all
```

#### Environment Configuration
- Configure URI bases in `/config/environments/{env}.yml`
- Support for local, production, and custom environments
- Template variable substitution for consistent URI management

### Testing and Validation
- **UPDATED**: `tests/modules.txt` to reference generated release files
- **MAINTAINED**: All existing validation scripts work with new structure
- **COMPATIBLE**: Sister repository `mcp_vocabulary_service` can use GitHub releases

### Migration Guide

For developers transitioning from v0.1.3 and earlier:

1. **Stop editing `/modules/` directly** (now deprecated)
2. **Use `/templates/modules/` for development**
3. **Run build process** before testing: `./build-release-enhanced.sh --env=local`
4. **Test generated files** in `/release/ontology/latest/`

### Compatibility

- ✅ GitHub releases continue to work with existing MCP vocabulary service
- ✅ All existing scripts and tools compatible with release structure
- ✅ Previous ontology versions remain accessible
- ✅ URI structure unchanged for end users

### Sister Repository Integration

The `mcp_vocabulary_service` can now build containers using GitHub releases without requiring local checkout of this repository, making deployment much more flexible.

---

This release establishes a clean foundation for the 0.1.4 ontology release and future development.