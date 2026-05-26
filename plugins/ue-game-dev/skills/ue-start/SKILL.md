---
name: ue-start
description: 当用户开始一个范围不清的 Unreal Engine 任务、询问从哪里开始、提到新/旧 UE 项目，或需要先判断应进入接手、需求、计划、实现、调试、测试、性能或打包流程时使用。
---

# UE Start

## 概览

这是 UE 工作的轻量入口技能。先判断用户所处阶段，只问会阻塞安全路由的最少问题，然后把任务交给最合适的 UE 工作流技能。

## 入口判断

1. 识别项目阶段：旧项目接手、新功能、Bug/调试、重构、测试/验证、性能/发布准备，或显式打包自动化。
2. 记录已知上下文：`.uproject` 路径、UE 版本、目标平台、模块/插件区域、Blueprint/C++ 归属和期望结果。
3. 如果本地存在 UE 项目，先只读检查 `.uproject`、`Source/`、`Plugins/`、`Config/`，再建议实现路径。
4. 如果用户希望 Codex 先熟悉现有项目，保持只读并路由到 `$ue-project-onboarding`。
5. 如果只是功能想法且细节不足，路由到 `$ue-feature-brief`。
6. 如果需求已清楚且需要拆解工作，路由到 `$ue-implementation-plan`。

## 阶段路由

| 用户意图 | 路由 |
|----------|------|
| “先熟悉项目”、“接手旧项目”、“二开前分析” | `$ue-project-onboarding` |
| “我想做一个功能”但需求仍模糊 | `$ue-feature-brief` |
| 明确功能，询问如何实现 | `$ue-implementation-plan`，之后进入领域技能 |
| 行为异常、日志、崩溃、Blueprint 不触发 | `$ue-debug-validation` 或 `$ue-log-crash-triage` |
| 需要测试方案或验证路径 | `$ue-testing-automation` |
| 性能、Cook/Package 失败、发布准备 | `$ue-performance-packaging` |
| 明确要构建、打包、发布自动化 | `$ue-build-release-automation` |

## 输出

返回一段简短入口结论：

- 阶段：`onboarding`、`brief`、`plan`、`implementation`、`debug`、`validation`、`performance` 或 `packaging`。
- 已知事实：项目路径、版本、领域、限制条件。
- 阻塞问题：如有，只问一个最关键问题。
- 下一技能：给出精确 `$skill-name` 和原因。
- 立即动作：只读扫描、需求简报、实施计划、实现或验证。

## 参考

- 当请求模糊或跨多个 UE 领域时，读取 `references/intake-checklist.md`。
