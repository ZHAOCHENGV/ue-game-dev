---
name: ue-data-management
description: Unreal Engine data management workflow for Primary Asset Manager, Data Assets, DataTable, CurveTable, DataRegistry, soft and hard references, FStreamableManager async loading, Primary Asset Rules, cook chunks, and runtime data validation. Use when requests involve gameplay data modeling, asset loading strategy, item tables, or cook-aware asset references.
---

# UE Data Management

Use this skill for gameplay data models, asset reference strategy, async loading, and cook-aware asset organization. Keep designer editing, runtime load cost, save compatibility, and packaging rules aligned.

## First Pass

1. Identify the data shape: Data Asset, Primary Data Asset, DataTable, CurveTable, Config, Gameplay Tags, DataRegistry, or backend data.
2. Locate owners: systems that author, load, cache, mutate, save, replicate, or display the data.
3. Decide whether references should be hard, soft, primary asset IDs, row handles, gameplay tags, or config keys.
4. Check cook rules, chunking, asset manager settings, and async loading paths before introducing new references.
5. Define validation: editor data audit, missing row handling, async load failure behavior, packaged build access, and version migration.

## Data Modeling Rules

- Use Data Assets for object-like records with asset references and designer-friendly editing.
- Use DataTables for tabular rows that share one struct and benefit from CSV/JSON import/export.
- Use CurveTables for numeric curves and balancing data that needs interpolation.
- Use Config for environment or project settings, not large gameplay catalogs.
- Use Gameplay Tags for stable semantic identifiers; avoid stringly typed category logic.

## Asset Loading Rules

- Use hard references only when always-loaded ownership is intentional.
- Use `TSoftObjectPtr`, `TSoftClassPtr`, `FSoftObjectPath`, or Primary Asset IDs for optional or large assets.
- Load soft references through `FStreamableManager` or the Asset Manager with explicit success/failure handling.
- Keep async load callbacks safe: validate UObject lifetime and return to the game thread before touching gameplay objects.
- Ensure soft-referenced assets are included by Primary Asset Rules, map references, explicit cook lists, or bundle rules.

## Runtime And Packaging

- Validate DataTable row structs, missing row fallbacks, duplicate IDs, and row rename risks.
- Version save data that stores row names, asset IDs, or soft paths.
- Avoid editor-only assets in runtime references.
- Include packaged build checks for asset discovery and async load behavior.

## References

- Read `references/data-asset-patterns.md` before choosing Data Asset, DataTable, DataRegistry, or Config.
- Read `references/async-loading-checklist.md` before adding soft references or `FStreamableManager` loading.
- Use shared `rules/ue-naming.md` for asset prefixes, Gameplay Tag naming, and module naming.
