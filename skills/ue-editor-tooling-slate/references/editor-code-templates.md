# 编辑器工具代码模板

## 模块注册

```cpp
void FMyEditorModule::StartupModule()
{
    RegisterMenus();
    RegisterCommands();
}

void FMyEditorModule::ShutdownModule()
{
    UnregisterMenus();
    UnregisterCommands();
}
```

## ToolMenus

```cpp
UToolMenus::RegisterStartupCallback(
    FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FMyEditorModule::RegisterMenus));
```

注销：

```cpp
UToolMenus::UnRegisterStartupCallback(this);
UToolMenus::UnregisterOwner(this);
```

## Tab Spawner

```cpp
FGlobalTabmanager::Get()->RegisterNomadTabSpawner(
    MyTabName,
    FOnSpawnTab::CreateRaw(this, &FMyEditorModule::SpawnTab));
```

## Details Customization

```cpp
PropertyEditorModule.RegisterCustomClassLayout(
    "MyObject",
    FOnGetDetailCustomizationInstance::CreateStatic(&FMyDetails::MakeInstance));
```

## 注意

- 注册和注销必须对称。
- Editor-only 代码不要进入 Runtime 模块。
- 修改资产时使用 transaction 和 dirty 标记。
