# Slate Panel Template

## Registration Shape

```cpp
void FSampleToolsEditorModule::StartupModule()
{
    FGlobalTabmanager::Get()->RegisterNomadTabSpawner(TabName,
        FOnSpawnTab::CreateRaw(this, &FSampleToolsEditorModule::SpawnTab));
}

void FSampleToolsEditorModule::ShutdownModule()
{
    FGlobalTabmanager::Get()->UnregisterNomadTabSpawner(TabName);
}
```

## Panel Rules

- Register and unregister menus, commands, tabs, and delegates symmetrically.
- Keep editor-only code in Editor modules.
- Use `ToolMenus` for menus/toolbars and Slate widgets for custom panels.
- Validate reload, shutdown, and plugin disable paths.
