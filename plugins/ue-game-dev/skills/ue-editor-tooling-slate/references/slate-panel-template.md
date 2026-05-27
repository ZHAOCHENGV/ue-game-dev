# Slate Panel 模板

## 注册形状

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

## 面板规则

- menu、command、tab、delegate 的注册和注销必须对称。
- Editor-only 代码放在 Editor module。
- 菜单/工具栏使用 `ToolMenus`，自定义面板使用 Slate widget。
- 验证 reload、shutdown 和 plugin disable 路径。
