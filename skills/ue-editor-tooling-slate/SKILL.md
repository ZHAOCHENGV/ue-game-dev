---
name: ue-editor-tooling-slate
description: 当 Unreal Engine 任务涉及编辑器插件、Slate 界面、ToolMenus、UICommands、工具栏/菜单扩展、Details 自定义、Property Type 自定义、Asset Type Actions、Factories、Tab Spawner 或 Editor Subsystem 时使用。
---

# UE Editor Tooling Slate

## 概览

这个技能负责 UE 编辑器工具和 Slate。重点是 Runtime/Editor 模块分离、注册与注销对称、UI 命令绑定、编辑器生命周期和资产操作安全。

## 使用场景

- 创建编辑器面板、菜单、工具栏按钮、Details 面板或资产右键操作。
- 实现 `FUICommandList`、`ToolMenus`、`SDockTab`、`SWidget`、`IDetailCustomization`。
- 排查热重载后重复菜单、关闭 Editor 崩溃、Runtime 依赖 Editor 模块。

## 工作流程

1. 确认插件/模块拆分：Runtime、Editor、Developer 或 Program。
2. 检查 `.uplugin`、`.Build.cs`、LoadingPhase、依赖和 API macro。
3. 设计注册点：StartupModule 注册，ShutdownModule 注销。
4. 实现 UI：Command、Style、Menu、Tab、Slate Widget、Details 或 Asset Action。
5. 验证：Editor 重启、热重载、禁用插件、资产选择、Undo/Redo 和 packaged build 边界。

## 规则

- Editor-only 类型不得进入 Runtime 模块。
- 所有注册都要有对应注销，避免重复菜单和悬挂 delegate。
- Slate UI 不要直接长期持有易销毁 UObject，使用弱引用并在使用前检查。
- 修改资产要走 transaction、dirty 标记和保存提示。
- 工具生成代码或资产前先检查命名、路径和冲突。

## 输出

- 模块设计：Editor 模块、依赖和加载时机。
- UI 结构：菜单、命令、Tab、Widget、Details、Asset Action。
- 代码位置：Public/Private、Style、Command、Subsystem。
- 验证：重启 Editor、禁用插件、资产操作、Undo/Redo 和打包边界。

## 参考

- 检查清单读取 `references/editor-tooling-checklist.md`。
- 代码模板读取 `references/editor-code-templates.md`。
