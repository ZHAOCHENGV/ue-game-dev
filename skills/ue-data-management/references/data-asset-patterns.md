# Data Asset Patterns

## Choose The Storage Shape

| Need | Prefer |
|------|--------|
| Designer-edited object record with asset references | `UDataAsset` or `UPrimaryDataAsset` |
| Large table of uniform rows | `UDataTable` |
| Numeric tuning over an input range | `UCurveTable` or Curve asset |
| Runtime registry and lookup integration | DataRegistry |
| Project/environment setting | Config / `UDeveloperSettings` |

## Stable IDs

- Use stable row names, Primary Asset IDs, or Gameplay Tags for save and network references.
- Do not save localized display names as IDs.
- Document migration when renaming rows, assets, or tags.
- Keep designer-facing display text separate from runtime identity.

## Validation Checklist

- Missing row behavior is explicit.
- Duplicate IDs are detected before runtime.
- Asset references match expected classes.
- Soft references have cook coverage.
- Packaged build can find the same data as editor PIE.

## Common Pitfalls

- Hard-referencing every item icon or mesh from a central singleton.
- Using DataTables for records that need per-row asset inheritance or complex editor behavior.
- Storing mutable runtime state in shared data assets.
- Assuming a row rename will not affect saves, UI bindings, or backend payloads.
