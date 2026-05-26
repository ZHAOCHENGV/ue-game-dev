---
name: ue-project-onboarding
description: 当请求要求 Codex 了解、审查、接手、继承、熟悉或为现有 Unreal Engine 项目二次开发做准备，且在改动前需要只读项目梳理时使用。
---

# UE Project Onboarding

## 概览

这个技能用于旧项目或现有项目接手。第一轮保持只读，目标是形成项目地图、模块/插件理解、资产命名、风险和后续工作流建议。

## 使用场景

- “先熟悉这个旧 UE 项目，后面我要二开”。
- 审查项目结构、模块、插件、资产、配置、Build 文件和已知风险。
- 为后续需求简报、实施计划、调试或多 Agent 协作建立上下文。

## 工作流程

1. 定位 `.uproject`，读取引擎版本、模块、插件和目标平台。
2. 扫描 `Source/`、`Plugins/`、`Config/`、`Content/` 文件名、target 和 `.Build.cs`。
3. 识别主要系统：Gameplay、UI、Input、GAS、AI、Animation、SaveGame、Services、Editor tools。
4. 记录风险：循环依赖、Editor-only 泄漏、命名混乱、资产缺失、测试缺口、打包风险。
5. 输出 onboarding report，并建议下一步技能。

## 工具

- 可用只读脚本 `skills/ue-project-onboarding/scripts/ue_project_scan.py` 快速扫描项目结构。
- 工具只读取 `.uproject`、模块、插件、源码文件、Build 文件和常见资产文件名，不编辑 `.uasset` 或项目文件。

## 规则

- 接手阶段不要修改代码、资产或配置，除非用户明确要求进入实现。
- 不要假设 Content 资产内容；只能基于文件名、路径和可读文本推断。
- 对不确定结论标注“推断”，并说明依据。
- 输出要帮助下一轮二开，而不是堆文件列表。

## 输出

- 项目概览：路径、UE 版本、模块、插件、平台。
- 系统地图：主要目录、类、资产命名和职责。
- 风险与缺口：构建、架构、资产、测试、打包、文档。
- 建议下一步：`$ue-workflow-state`、`$ue-feature-brief`、`$ue-implementation-plan` 或领域技能。

## 参考

- 审查清单读取 `references/project-audit-checklist.md`。
- 报告模板读取 `references/onboarding-report-template.md`。
