# UE Build System API Accuracy

This reference adapts API-accuracy guidance from `quodsoler/unreal-engine-skills` into the UE Game Dev plugin style. Use it when a task touches `.Build.cs`, module layout, plugin descriptors, or include/link errors.

## Build.cs Placement

- `PublicDependencyModuleNames` is for modules whose types appear in public headers or public inline code.
- `PrivateDependencyModuleNames` is for modules only used by `.cpp` files or private headers.
- `PublicIncludePaths` and `PrivateIncludePaths` should be rare in modern UE module layout; prefer normal `Public/` and `Private/` folders.
- Do not add broad dependencies to silence include errors; identify the module that owns the actual type.

## Runtime Versus Editor

- Runtime modules must not depend on `UnrealEd`, `AssetTools`, `PropertyEditor`, `LevelEditor`, `ToolMenus`, or editor-only style/tooling modules.
- Editor modules may depend on runtime modules, but runtime modules should not depend on editor modules.
- If shared contracts are needed, extract a narrow runtime/shared module instead of creating a circular dependency.

## Public API Macros

- Public classes that cross module boundaries need the module export macro such as `MYMODULE_API`.
- Private implementation classes that never cross module boundaries do not need export macros.
- Keep public headers minimal and stable; forward declare where possible and include concrete headers in `.cpp`.

## Target And Descriptor Review

- `.uproject` and `.uplugin` module entries should match actual module folder names.
- Target files define build target type and included modules; do not confuse target modules with plugin descriptor modules.
- Loading phases should be intentional. Editor registration commonly uses editor module startup, while runtime gameplay should not rely on editor startup.

## Link/Include Triage

- Include error: find the header that declares the type and add the narrow include in the `.cpp` or public header that needs it.
- Link error: check the owning module dependency and export macro before changing code shape.
- Reflection/UHT error: check generated include order, macro placement, unsupported reflected types, and missing module dependencies.
- Packaged build error: look first for editor-only dependencies, uncooked assets, or plugin descriptor/module type mismatch.
