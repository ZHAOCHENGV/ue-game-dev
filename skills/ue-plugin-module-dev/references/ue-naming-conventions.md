# UE 命名规范

## C++ 类型前缀

| 类型 | 前缀 | 示例 |
|------|------|------|
| UObject 派生 | `U` | `UInventoryComponent` |
| Actor 派生 | `A` | `AInteractableActor` |
| Struct | `F` | `FInventoryEntry` |
| Enum | `E` | `EItemRarity` |
| Interface | `I` / `U` | `IInteractable` / `UInteractable` |
| Slate Widget | `S` | `SInventoryPanel` |

## 资产前缀

| 类型 | 前缀 |
|------|------|
| Blueprint | `BP_` |
| Widget Blueprint | `WBP_` |
| Animation Blueprint | `ABP_` |
| Static Mesh | `SM_` |
| Skeletal Mesh | `SK_` |
| Material | `M_` |
| Material Instance | `MI_` |
| Texture | `T_` |
| Niagara System | `NS_` |
| Sound Cue | `SC_` |
| Sound Wave | `SW_` |
| Data Asset | `DA_` |
| Input Action | `IA_` |
| Input Mapping Context | `IMC_` |

## 命名形状

```text
[AssetTypePrefix]_[AssetName]_[Descriptor]_[Variant]
```

示例：

```text
BP_InventoryPickup_Health_Small
WBP_InventoryPanel_Default
IA_Interact
IMC_Gameplay_Default
NS_HitImpact_Metal
```

## 模块与插件

- 模块名使用清晰 PascalCase，例如 `InventoryRuntime`、`InventoryEditor`。
- API macro 与模块名一致，例如 `INVENTORYRUNTIME_API`。
- Runtime 与 Editor 模块名要能看出职责。
- 插件目录名、`.uplugin` name 和主模块名保持一致或有明确映射。

## 规则

- 不为临时测试资产使用最终命名空间，避免后续误引用。
- 不用 `NewBlueprint`、`Test2`、`Final_Final` 这类不可维护名称。
- 重命名资产后处理 redirector 并验证引用。
