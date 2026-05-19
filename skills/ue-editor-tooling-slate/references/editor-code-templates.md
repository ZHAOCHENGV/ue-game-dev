# Editor Tooling Code Templates

## ToolMenus Registration

```cpp
// 在 StartupModule 中注册菜单
void FMyEditorModule::StartupModule()
{
    // 注册菜单扩展
    UToolMenus::RegisterStartupCallback(
        FSimpleMulticastDelegate::FDelegate::CreateRaw(
            this, &FMyEditorModule::RegisterMenus));
}

void FMyEditorModule::RegisterMenus()
{
    // 扩展主菜单栏
    UToolMenu* Menu = UToolMenus::Get()->ExtendMenu(
        "LevelEditor.MainMenu.Tools");

    FToolMenuSection& Section = Menu->AddSection(
        "MyToolsSection",
        LOCTEXT("MyToolsSectionLabel", "我的工具"));

    Section.AddMenuEntry(FMyEditorCommands::Get().OpenMyTool);
}

// 在 ShutdownModule 中注销
void FMyEditorModule::ShutdownModule()
{
    UToolMenus::UnRegisterStartupCallback(this);
    UToolMenus::UnregisterOwner(this);
    FMyEditorCommands::Unregister();
}
```

## UICommands Definition

```cpp
// MyEditorCommands.h
class FMyEditorCommands : public TCommands<FMyEditorCommands>
{
public:
    FMyEditorCommands()
        : TCommands<FMyEditorCommands>(
            TEXT("MyEditor"),
            LOCTEXT("MyEditorCommands", "我的编辑器命令"),
            NAME_None,
            FMyEditorStyle::GetStyleSetName())
    {}

    virtual void RegisterCommands() override;

    TSharedPtr<FUICommandInfo> OpenMyTool;
};

// MyEditorCommands.cpp
void FMyEditorCommands::RegisterCommands()
{
    UI_COMMAND(OpenMyTool,
        "Open My Tool",
        "Opens the custom editor tool panel",
        EUserInterfaceActionType::Button,
        FInputChord());
}
```

## Nomad Tab Spawner

```cpp
// 注册
FGlobalTabmanager::Get()->RegisterNomadTabSpawner(
    MyTabName,
    FOnSpawnTab::CreateRaw(this, &FMyEditorModule::SpawnMyTab))
    .SetDisplayName(LOCTEXT("MyTabTitle", "我的工具面板"))
    .SetMenuType(ETabSpawnerMenuType::Hidden);

// 生成
TSharedRef<SDockTab> FMyEditorModule::SpawnMyTab(
    const FSpawnTabArgs& Args)
{
    return SNew(SDockTab)
        .TabRole(ETabRole::NomadTab)
        [
            SNew(SMyToolWidget)
        ];
}

// 注销
FGlobalTabmanager::Get()->UnregisterNomadTabSpawner(MyTabName);
```

## Detail Customization

```cpp
// MyClassCustomization.h
class FMyClassCustomization : public IDetailCustomization
{
public:
    static TSharedRef<IDetailCustomization> MakeInstance();
    virtual void CustomizeDetails(IDetailLayoutBuilder& DetailBuilder) override;
};

// Registration in module startup
FPropertyEditorModule& PropertyModule =
    FModuleManager::LoadModuleChecked<FPropertyEditorModule>("PropertyEditor");
PropertyModule.RegisterCustomClassLayout(
    UMyClass::StaticClass()->GetFName(),
    FOnGetDetailCustomizationInstance::CreateStatic(
        &FMyClassCustomization::MakeInstance));

// Unregistration in module shutdown
PropertyModule.UnregisterCustomClassLayout(
    UMyClass::StaticClass()->GetFName());
```

## Asset Type Actions

```cpp
// Register
IAssetTools& AssetTools =
    FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools")
    .Get();
MyAssetTypeActions = MakeShared<FMyAssetTypeActions>();
AssetTools.RegisterAssetTypeActions(MyAssetTypeActions.ToSharedRef());

// Unregister
if (MyAssetTypeActions.IsValid())
{
    IAssetTools& AssetTools =
        FModuleManager::LoadModuleChecked<FAssetToolsModule>("AssetTools")
        .Get();
    AssetTools.UnregisterAssetTypeActions(MyAssetTypeActions.ToSharedRef());
}
```
