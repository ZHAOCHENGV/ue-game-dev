---
name: ue-plugin-module-dev
description: Unreal Engine plugin and module development workflow for `.uplugin`, `.uproject` module descriptors, Runtime/Editor/Developer module split, `ModuleRules` and `.Build.cs`, Public/Private folder boundaries, export API macros, plugin content/config/resources, module startup/shutdown, editor module boundaries, dependency hygiene, packaging compatibility, Epic-style coding rules, and UE asset/code file naming conventions. Use when requests involve creating, refactoring, debugging, or reviewing UE plugins or modules.
---

# UE Plugin Module Dev

Use this skill for Unreal Engine `.uplugin` plugins and C++ modules. Keep plugin/module structure, dependencies, and naming consistent before writing implementation code.

## First Pass

1. Read the `.uproject`, existing `.uplugin` files, target files, all relevant `.Build.cs` files, and `Source/<ModuleName>/Public` and `Private` folders.
2. Identify whether the work is project module, runtime plugin module, editor plugin module, developer/tooling module, or content-only plugin.
3. Map module type, loading phase, public API, private implementation, reflected Blueprint surface, and asset paths.
4. Check naming before creating files or assets. Use project conventions first, then Epic-style prefixes and Unreal class prefixes.
5. If the plugin includes editor tooling, identify the Editor module that owns it and hand UI behavior details to `$ue-editor-tooling-slate`.

## Plugin Structure

- Put reusable feature plugins under `Plugins/<PluginName>/`.
- Keep descriptor file as `Plugins/<PluginName>/<PluginName>.uplugin`.
- Use `Source/<ModuleName>/` for C++ modules.
- Split C++ module code into `Public/` headers that are part of the public API and `Private/` implementation files.
- Keep plugin resources such as icons under `Resources/` when needed.
- Use plugin `Content/` only when the plugin intentionally ships assets. Keep content paths stable after assets are referenced by Blueprints or maps.

## Module Rules

- Use Runtime modules for packaged gameplay/runtime code.
- Use Editor modules for editor-only UI, details panels, asset actions, factories, custom editors, and editor commands.
- Use a paired `MyPlugin` Runtime module plus `MyPluginEditor` Editor module when runtime code and editor tooling both exist.
- Keep editor-only dependencies out of runtime modules.
- Put public header dependencies in `PublicDependencyModuleNames`; put implementation-only dependencies in `PrivateDependencyModuleNames`.
- Add dependencies only after verifying which module owns the type.
- Avoid circular dependencies. Extract shared interfaces or contracts into a smaller shared module when needed.
- For third-party libraries, isolate vendor headers/libs behind a narrow module boundary and expose Unreal-friendly types to the rest of the project.

## Editor Tooling Boundary

- Put ToolMenus, UICommands, tab spawners, Slate editor panels, detail customizations, asset type actions, factories, and editor subsystems in Editor modules.
- Keep runtime modules free of `UnrealEd`, `AssetTools`, `PropertyEditor`, `LevelEditor`, `ToolMenus`, and other editor-only dependencies.
- Do not design command/menu/detail panel behavior here; use `$ue-editor-tooling-slate` when the task is primarily editor UI/tool behavior.

## C++ API And File Naming

- Match Unreal class prefixes: `U` for UObject types, `A` for Actors, `F` for structs, `E` for enums, `I` for interfaces, `S` for Slate widgets.
- Keep header/source names aligned with the main reflected type, such as `MyFeatureComponent.h` and `MyFeatureComponent.cpp`.
- Use the module export macro for public types that cross module boundaries, for example `MYMODULE_API`.
- Keep reflected names and Blueprint class paths stable. Renames can require redirectors and asset migration.
- Prefer forward declarations in public headers and includes in `.cpp`.
- Follow Epic-style C++ formatting and naming. Avoid clever abstractions that fight Unreal reflection, serialization, or garbage collection.

## Asset Naming

- Follow Epic's recommended asset pattern: `[AssetTypePrefix]_[AssetName]_[Descriptor]_[Variant]`.
- Examples: `BP_InventoryItem`, `SM_Crate_A`, `M_Hologram`, `MI_Hologram_Red`, `FXS_Impact_Sparks`, `WBP_InventoryPanel`.
- Keep asset names ASCII, descriptive, searchable, and stable once referenced.
- Do not mix code module names, plugin names, and content asset prefixes casually. Each has a different purpose.

## Escalation

- Use `$ue-architecture` when the work is broad system/module design beyond one plugin or module.
- Use `$ue-cpp-gameplay` when module structure is clear and the task is gameplay C++ implementation.
- Use `$ue-blueprint-workflow` when plugin/module work requires Blueprint graph setup or validation.
- Use `$ue-performance-packaging` when plugin changes fail cook/package or affect release readiness.

## References

- Read `references/plugin-module-checklist.md` for `.uplugin`, module, `.Build.cs`, and packaging review.
- Read `references/ue-naming-conventions.md` before creating or renaming UE assets, C++ files, modules, plugins, or Blueprint-exposed APIs.
- Read `references/ue-cpp-coding-standard.md` before creating public C++ APIs or reviewing plugin code quality.
- Read `references/third-party-library-wrapper.md` when wrapping external C++ libraries, SDKs, DLLs, static libs, or platform-specific vendor binaries.
