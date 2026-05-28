---
name: ue-game-features
description: 当 Unreal Engine 请求涉及 Game Feature Plugin、ModularGameplay、UGameFeatureAction、GameFrameworkComponentManager、Lyra Experience、运行时功能激活、能力/Input/UI 授予或模块化玩法架构时使用。
---

# UE Game Features

这个技能处理 UE5 Game Feature Plugins 与模块化玩法。重点是把插件激活生命周期、运行时授予、资产加载、回滚和跨系统边界说清楚。

## 工作流程

1. 读取 `.uproject`、相关 `.uplugin`、已启用 Game Feature 插件、`DefaultGame.ini`、模块 `.Build.cs` 和现有 Experience/Action Set 资产。
2. 判断工作属于 Game Feature Plugin、ModularGameplay 组件注入、Lyra 风格 Experience、ability/input/UI 授予，还是 data-only 功能包。
3. 梳理激活生命周期：registered、loaded、active、deactivating、error，以及资产、组件、输入、能力和 delegate 如何清理。
4. 如果功能触及 GAS、Enhanced Input、UI、Data Asset、复制或存档，先由本技能拥有 Game Feature 边界，再按需交给对应技能。
5. 定义验证：激活、反复停用/启用、缺失资产、Cook 收录、多人 authority 和回滚行为。

## 设计规则

- 一个 Game Feature 插件聚焦一个玩法能力或内容包。
- 只有功能自己拥有可复用 runtime 代码时，才把 runtime 模块放进 feature 插件；编辑器辅助逻辑放配套 editor 模块。
- 用 `UGameFeatureAction` 资产表达激活期动作，例如组件注入、能力授予、输入映射、数据注册或 UI 条目。
- 功能拥有的可选内容优先用稳定 Data Asset 和软引用，避免无意强加载。
- 激活和停用必须幂等，重复切换不应复制组件、输入映射、ability spec、delegate 或 UI 层。
- Lyra 风格 Experience 要把 Experience、Action Set、Pawn Data、Ability Set、Input Config 和 HUD layer 当作一条激活故事。

## 跨域交接

- 功能授予 ability、attribute、effect 或 gameplay cue 时，在边界明确后进入 `$ue-gas-networking`。
- 功能新增 Input Action 或 Mapping Context 时进入 `$ue-input-enhanced`。
- 功能新增 HUD layer、菜单或 CommonUI 条目时进入 `$ue-client-ui`。
- `.uplugin`、模块描述、`.Build.cs` 和插件打包结构进入 `$ue-plugin-module-dev`。
- feature-owned Primary Asset、bundle、Cook 规则和 chunking 进入 `$ue-data-management`。

## 输出

- Game Feature 边界：插件、模块、资产、激活入口和依赖。
- 激活/停用流程：授予内容、清理内容、失败状态和日志证据。
- 跨域计划：GAS/Input/UI/Data/Replication 的后续技能与所有权。
- 验证清单：PIE、重复切换、Cook、多客户端和缺失资产行为。

## 参考

- 修改或审查 Game Feature 插件、Action、Lyra Experience 前读取 `references/game-feature-checklist.md`。
