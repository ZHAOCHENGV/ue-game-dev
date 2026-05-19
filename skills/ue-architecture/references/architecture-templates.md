# Architecture Code Templates

## Module Dependency Graph (Mermaid)

Use this template to visualize module relationships before refactoring:

```
[ProjectCore] Runtime
  ├── PublicDependency: Core, CoreUObject, Engine
  ├── Public surface: shared interfaces, data types, gameplay tags
  └── No editor dependencies

[ProjectGameplay] Runtime
  ├── PublicDependency: ProjectCore
  ├── PrivateDependency: GameplayAbilities, GameplayTags
  ├── Public surface: gameplay components, subsystems
  └── Depends on ProjectCore contracts

[ProjectUI] Runtime
  ├── PublicDependency: ProjectCore, UMG, CommonUI
  ├── PrivateDependency: ProjectGameplay (for view models)
  └── Public surface: widget base classes, UI subsystem

[ProjectEditor] Editor
  ├── PublicDependency: ProjectCore
  ├── PrivateDependency: UnrealEd, PropertyEditor, AssetTools
  └── Public surface: custom editors, detail panels, asset actions
```

## Game Feature Plugin Template

```
Plugins/GameFeatures/GF_MyFeature/
├── GF_MyFeature.uplugin
├── Source/
│   ├── GF_MyFeatureRuntime/
│   │   ├── GF_MyFeatureRuntime.Build.cs
│   │   ├── Public/
│   │   │   └── GF_MyFeatureRuntimeModule.h
│   │   └── Private/
│   │       └── GF_MyFeatureRuntimeModule.cpp
│   └── GF_MyFeatureEditor/  (optional)
├── Content/
└── Config/
```

## Game Feature Plugin uplugin Template

```json
{
  "FileVersion": 3,
  "Version": 1,
  "VersionName": "1.0",
  "FriendlyName": "My Feature",
  "Description": "Feature description",
  "Category": "Game Features",
  "CreatedBy": "Team",
  "Modules": [
    {
      "Name": "GF_MyFeatureRuntime",
      "Type": "Runtime",
      "LoadingPhase": "Default"
    }
  ],
  "ExplicitlyLoaded": true,
  "BuiltInInitialFeatureState": "Active",
  "Plugins": [
    {
      "Name": "GameFeatures",
      "Enabled": true
    },
    {
      "Name": "ModularGameplay",
      "Enabled": true
    }
  ]
}
```

## Shared Contracts Module Pattern

When two modules need to reference each other, extract a thin shared contracts module:

```
ProjectContracts (Runtime, minimal)
├── Interfaces: IInventoryProvider, ICombatTarget, IInteractable
├── Structs: FItemHandle, FCombatResult
├── Enums: EInteractionType, EItemRarity
├── GameplayTags: shared tag constants
└── No implementation, no assets, no heavy dependencies
```

Both modules depend on `ProjectContracts` instead of each other, breaking the cycle.

## Reflection Exposure Decision Checklist

Before adding `UCLASS`/`USTRUCT`/`UFUNCTION`/`UPROPERTY`:

1. Does Blueprint need to see this? If no, keep it C++ only.
2. Does serialization need this? If yes, add `UPROPERTY()`.
3. Does replication need this? If yes, add `Replicated` or `ReplicatedUsing`.
4. Does editor tooling need this? If yes, add `EditAnywhere`/`VisibleAnywhere`.
5. Is this part of a stable public API? If yes, add careful metadata. If no, keep private.
