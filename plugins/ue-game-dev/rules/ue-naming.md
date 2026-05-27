# UE 命名规则

## C++ 类型前缀

| 前缀 | 用途 |
|------|------|
| `U` | `UObject` 派生类、组件、Subsystem、Data Asset |
| `A` | `AActor` 派生类 |
| `F` | Struct 和非 UObject 值类型 |
| `E` | Enum |
| `I` | Unreal Interface |
| `S` | Slate Widget |
| `T` | 模板与容器 |

## 资产前缀

| 前缀 | 资产 |
|------|------|
| `BP_` | Blueprint class |
| `WBP_` | Widget Blueprint |
| `ABP_` | Animation Blueprint |
| `SM_` | Static Mesh |
| `SK_` | Skeletal Mesh |
| `M_` | Material |
| `MI_` | Material Instance |
| `T_` | Texture |
| `NS_` | Niagara System |
| `FXS_` | 项目采用该约定时的 Niagara 或 VFX system |
| `IA_` | Enhanced Input Action |
| `IMC_` | Input Mapping Context |
| `DA_` | Data Asset |
| `DT_` | DataTable |

## 模块与插件命名

- 模块名保持稳定，并与 API macro 对齐，例如 `InventoryRuntime` 和 `INVENTORYRUNTIME_API`。
- 同一插件同时包含 Runtime 和 Editor 模块时，用清晰的 `Runtime` / `Editor` 后缀。
- 重命名反射类型、模块或资产前，先记录 redirector 和 Blueprint 影响。

## Gameplay Tag

- 使用层级化、稳定的 tag，例如 `Ability.Fireball`、`UI.Inventory.Open`、`State.Stunned`。
- 显示文本与 tag identity 分离。
- save、backend payload 或资产存储 tag 时，记录 tag 迁移。

## 文件夹命名

- 优先使用能反映 ownership 的领域目录：`Characters`、`UI`、`Input`、`Abilities`、`Data`、`Maps`、`Materials`、`VFX`、`Audio`。
- 生产内容避免 `Misc`、`NewFolder`、`Temp` 这类垃圾桶目录。
