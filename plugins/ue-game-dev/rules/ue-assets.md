# UE Asset Rules

## Naming

- Follow project asset naming conventions before adding new assets.
- Use established local prefixes when they differ from the table below.

| Prefix | Asset Type |
|--------|------------|
| `BP_` | Blueprint Actor/Object |
| `BPI_` | Blueprint Interface |
| `WBP_` | Widget Blueprint |
| `ABP_` | Animation Blueprint |
| `SM_` | Static Mesh |
| `SK_` | Skeletal Mesh |
| `M_` / `MI_` | Material / Material Instance |
| `T_` | Texture |
| `FXS_` / `NS_` | Niagara System |
| `IA_` | Input Action |
| `IMC_` | Input Mapping Context |
| `DA_` / `PDA_` | Data Asset / Primary Data Asset |
| `L_` | Level/Map |

## Reference Safety

- Prefer soft references or Primary Asset rules for optional content.
- Avoid hard-coded content paths in gameplay code unless there is a documented load boundary.
- Check redirectors, missing references, hard-coded paths, and editor-only asset references before packaging readiness.
- Keep runtime assets out of editor-only plugin/module dependencies.
- Do not reference editor utility widgets, factories, or preview-only assets from runtime assets.

## Asset Scope

- For UI/input/animation/VFX assets, list exact asset names and expected compile/runtime validation.
- Avoid broad Content scans unless the task is an asset audit; use targeted filename discovery first.
- When adding assets, name the owner folder, dependency direction, and whether the asset is runtime, editor-only, or test-only.

## Common Problems

- A Blueprint references a renamed or moved asset through a stale redirector.
- A runtime map depends on an Editor module class through a placed Actor or component.
- A soft reference is never registered with Primary Asset rules and fails to cook.
- A material instance or Niagara system works in editor because of uncooked preview-only dependencies.

## Validation

- Validate asset load in PIE and, when packaging is relevant, in a cooked build or cook smoke test.
- For Primary Assets, confirm type, scan path, cook rule, and asset ID.
- For `.uasset` analysis, use editor-visible metadata and filenames; do not treat binary assets as source text.
