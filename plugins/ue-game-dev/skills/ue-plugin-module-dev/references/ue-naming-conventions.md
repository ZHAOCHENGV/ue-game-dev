# UE Naming Conventions

Reference basis: Epic's recommended asset naming convention uses `[AssetTypePrefix]_[AssetName]_[Descriptor]_[Variant]`.

## Asset Name Shape

- Use `Prefix_Name_Descriptor_Variant`.
- Keep the prefix short and type-specific.
- Keep `Name` stable and searchable.
- Use `Descriptor` for purpose, socket, state, team, material role, or style.
- Use `Variant` for numbered or lettered alternatives such as `A`, `B`, `01`, or color/style variants.

## Common Asset Prefixes

- `BP_`: Blueprint class.
- `BI_` or project-standard `BPI_`: Blueprint Interface.
- `WBP_`: Widget Blueprint.
- `ABP_`: Animation Blueprint.
- `BS_`: Blend Space.
- `SM_`: Static Mesh.
- `SK_`: Skeletal Mesh.
- `SKEL_`: Skeleton.
- `PA_`: Physics Asset.
- `M_`: Material.
- `MI_`: Material Instance.
- `MF_`: Material Function.
- `T_`: Texture.
- `RT_`: Render Target.
- `FXS_`: Niagara System.
- `FXE_`: Niagara Emitter.
- `FXF_`: Niagara Function.
- `PS_`: Particle System.
- `S_`: Sound.
- `SC_`: Sound Cue.
- `DT_`: Data Table.
- `DA_`: Data Asset.
- `E_`: Enum asset.
- `LV_`: Level or map when the project uses that convention.

Prefer the existing project prefix if it already differs consistently.
When Epic's table and an established project convention differ, keep the project convention unless the task is explicitly standardizing names.

## C++ Type Names

- `AName`: Actor.
- `UName`: UObject, ActorComponent, Subsystem, DataAsset, UserWidget.
- `FName`: struct.
- `EName`: enum.
- `IName`: interface.
- `SName`: Slate widget.
- `TName`: template/container style.
- Boolean members start with `b`.

## C++ Files

- Match file names to the primary type without the Unreal prefix when that is the project style, or with it when the project already does so. Be consistent.
- Typical project style: `InventoryComponent.h` contains `UInventoryComponent`.
- Keep `.h` and `.cpp` paired for normal classes.
- Put public headers under `Public/` only when another module should include them.
- Put implementation-only headers under `Private/`.

## Plugin And Module Names

- Plugin folder and `.uplugin` base name should match: `Plugins/MyFeature/MyFeature.uplugin`.
- Module names should be PascalCase and stable.
- Module API macro should match the module name uppercased with `_API`, such as `MYFEATURE_API`.
- Editor module often appends `Editor`, such as `MyFeatureEditor`.

## Reflected API Names

- Keep `UCLASS`, `USTRUCT`, `UENUM`, `UFUNCTION`, and `UPROPERTY` names stable after Blueprint assets reference them.
- Use clear Blueprint categories and display names only when they improve designer usability.
- Plan redirectors before renaming assets or moving Blueprint class paths.

## Avoid

- Spaces, punctuation-heavy names, non-ASCII names, and vague names like `NewBlueprint`, `Test`, or `MyAsset`.
- Renaming referenced assets without planning redirectors and reference fix-up.
- Using asset prefixes for C++ module names or C++ prefixes for content assets.
