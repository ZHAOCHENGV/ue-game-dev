---
name: ue-architecture
description: 当 Unreal Engine 任务涉及系统归属、模块图、层级边界、依赖方向、Blueprint/C++ 暴露面、跨模块引用、迁移风险、循环依赖或大型 UE 功能组织时使用。
---

# UE Architecture

## 概览

这个技能用于 UE 架构判断。目标是让模块、插件、Blueprint、资产和运行时系统各有清晰归属，避免循环依赖、编辑器依赖泄漏到 Runtime，以及难以测试的跨层耦合。

## 工作流程

1. 读取 `.uproject`、`.uplugin`、`Source/`、`Plugins/`、`Config/` 和相关 `.Build.cs`。
2. 画出模块方向：Runtime、Editor、Developer、ThirdParty、Game Feature、UI、Gameplay、Online/Services。
3. 标记每个系统的拥有者、公共 API、Blueprint 暴露点、资产依赖和生命周期。
4. 检查 Public/Private 头文件、`ModuleRules`、API macro、反射类型和构建依赖。
5. 给出迁移顺序：先稳定接口，再移动实现，再修复引用，再验证构建和资产。

## 决策规则

- Runtime 模块不能依赖 Editor 模块；Editor 扩展放到独立 Editor 模块。
- Public 只放真正跨模块需要的类型；实现细节保持在 Private。
- Blueprint 面向稳定、设计师可理解的 API，不暴露临时内部状态。
- 资产引用优先走 DataAsset、Primary Asset、Soft Object Path 或配置化入口。
- 大功能先定义 ownership boundaries，再讨论具体类名。

## 常见风险

- `.Build.cs` 为了“先编过”随意加依赖，导致模块方向失控。
- Public 头文件包含大型引擎或项目头，拖慢编译并放大耦合。
- UI、Gameplay、Networking、SaveGame 互相直接引用，难以测试和替换。
- Editor-only 类型进入 Runtime，Cook 或 packaged build 才暴露问题。

## 输出

- 模块/插件依赖图：用文字或 Mermaid 表达方向。
- Ownership boundaries：每个系统谁拥有状态、谁只读、谁发事件。
- 迁移计划：文件移动、Build.cs 修改、API 调整、Blueprint 兼容策略。
- 验证：目标构建、Editor 启动、Blueprint 编译、PIE 和打包风险。

## 工具

- 涉及 `.Build.cs` 依赖、模块循环、Runtime 依赖 Editor 或 Mermaid 模块图时，使用只读脚本 `skills/ue-architecture/scripts/ue_dependency_graph.py`。
- 工具输出只能作为架构证据，不直接修改模块文件。

## 参考

- 模块边界读取 `references/module-boundaries.md`。
- 架构报告或迁移计划读取 `references/architecture-templates.md`。
