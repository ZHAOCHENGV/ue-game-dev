# UE Plugin And Module Checklist

## Descriptor Files

- `.uplugin` belongs at `Plugins/<PluginName>/<PluginName>.uplugin`.
- `.uproject` and `.uplugin` module entries should list module `Name`, `Type`, and `LoadingPhase`.
- Keep Runtime and Editor modules separate when editor dependencies are involved.
- Keep plugin version, friendly name, description, category, and enabled-by-default policy intentional when shipping outside one project.

## Module Layout

- `Source/<ModuleName>/<ModuleName>.Build.cs`
- `Source/<ModuleName>/Public`
- `Source/<ModuleName>/Private`
- Optional editor module: `Source/<ModuleName>Editor/`

## Module Type Decisions

- Runtime: code required in packaged builds.
- Editor: editor-only tools, Slate panels, detail customizations, factories, asset actions, editor commands.
- Developer/tooling: development-time helpers not required in packaged runtime.
- Content-only plugin: assets only, no C++ module.

## Build.cs Review

- Public dependencies are required by public headers.
- Private dependencies are required only by `.cpp` or private headers.
- Do not add `UnrealEd`, `Blutility`, editor style, asset tools, or details modules to runtime modules.
- If a public header exposes a type from another module, that dependency usually must be public.
- If only implementation uses a type, keep it private.

## Startup And Shutdown

- Keep module `StartupModule` and `ShutdownModule` narrow.
- Register editor extensions only in editor modules.
- For concrete menu/command/tab/detail/action registration patterns, use `$ue-editor-tooling-slate`.
- Avoid loading heavy assets in module startup.

## Packaging Risks

- Editor-only references in runtime module.
- Missing runtime dependencies.
- Plugin content not included or referenced incorrectly.
- Reflected class rename without redirectors.
- Asset paths moved after Blueprint references exist.
