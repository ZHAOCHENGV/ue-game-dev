# UE Naming Rules

## C++ Type Prefixes

| Prefix | Use |
|--------|-----|
| `U` | `UObject` derived classes, components, subsystems, data assets |
| `A` | `AActor` derived classes |
| `F` | Structs and non-UObject value types |
| `E` | Enums |
| `I` | Unreal interfaces |
| `S` | Slate widgets |
| `T` | Templates and containers |

## Asset Prefixes

| Prefix | Asset |
|--------|-------|
| `BP_` | Blueprint class |
| `WBP_` | Widget Blueprint |
| `ABP_` | Animation Blueprint |
| `SM_` | Static Mesh |
| `SK_` | Skeletal Mesh |
| `M_` | Material |
| `MI_` | Material Instance |
| `T_` | Texture |
| `NS_` | Niagara System |
| `FXS_` | Niagara or VFX system in projects using that convention |
| `IA_` | Enhanced Input Action |
| `IMC_` | Input Mapping Context |
| `DA_` | Data Asset |
| `DT_` | DataTable |

## Module And Plugin Names

- Keep module names stable and aligned with API macros, for example `InventoryRuntime` and `INVENTORYRUNTIME_API`.
- Use clear `Runtime` and `Editor` suffixes when a plugin has both module types.
- Do not rename reflected types, modules, or assets without documenting redirector and Blueprint impact.

## Gameplay Tags

- Use hierarchical, stable tags such as `Ability.Fireball`, `UI.Inventory.Open`, or `State.Stunned`.
- Keep display text separate from tag identity.
- Document tag migrations when saves, backend payloads, or assets store tags.

## Folder Names

- Prefer domain folders that match ownership: `Characters`, `UI`, `Input`, `Abilities`, `Data`, `Maps`, `Materials`, `VFX`, `Audio`.
- Avoid generic dumping grounds such as `Misc`, `NewFolder`, or `Temp` in production content.
