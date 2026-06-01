# Runtime And Editor Plugin Scaffold

```text
Plugins/SampleTools/
  SampleTools.uplugin
  Source/
    SampleToolsRuntime/
      SampleToolsRuntime.Build.cs
      Public/
      Private/
    SampleToolsEditor/
      SampleToolsEditor.Build.cs
      Public/
      Private/
```

## Module Rules

- Runtime module depends only on runtime-safe modules.
- Editor module may depend on `UnrealEd`, `ToolMenus`, `Slate`, and project runtime contracts.
- Public headers expose stable contracts; Private headers keep implementation details local.
- API macro names must match the module name, for example `SAMPLETOOLSRUNTIME_API`.

## Validation

- Confirm `.uplugin` module `Type` values.
- Confirm Runtime does not depend on Editor.
- Build Editor target after adding editor modules.
- Test packaged game when runtime module content or config changes.
