---
name: ue-multi-agent-workflow
description: 当 Unreal Engine 请求明确要求 multi-agent、多专家、并行专家、团队协作、lean/full 模式，或复杂跨域任务需要项目接手、架构审查、C++/Blueprint/UI/资产/测试/发布风险协调时使用。
---

# UE Multi-Agent Workflow

## 概览

这个技能是轻量多 Agent 编排协议，用于复杂 UE 任务的角色分工、并行发现和 Coordinator 汇总。简单单域问题不要强行启用多 Agent。

## Mode 选择

| Mode | 使用方式 |
|------|----------|
| `solo` | 简单单域任务，直接回到具体技能，不输出多 Agent 报告 |
| `lean` | 默认复杂任务，通常启用 Coordinator + 1-2 个专项角色 |
| `full` | 旧项目深度接手、插件架构审查、跨 C++/Blueprint/UI/资产/测试/发布风险的大任务 |

## Coordinator 职责

Coordinator 负责范围、角色、依赖顺序、冲突处理和最终综合。所有角色输出都必须回到 Coordinator，由 Coordinator 决定下一步进入哪个具体 UE 技能。

## 角色池

- Project Explorer：只读梳理旧项目、目录、模块、插件、资产命名。
- UE Architecture Reviewer：模块边界、Runtime/Editor 拆分、Blueprint/C++ 所有权。
- C++ Implementer：反射、UObject 生命周期、API、编译风险。
- Blueprint Integrator：节点、Pin、默认值、资产交接和设计师步骤。
- UI/UMG Specialist：Widget、CommonUI、DPI、输入焦点。
- GAS/Networking Specialist：ASC、RPC、复制、预测、多 PIE。
- AI/Animation Specialist：Behavior Tree、EQS、StateTree、AnimBP、Montage。
- Render/VFX Specialist：材质、Niagara、shader、视觉性能。
- Packaging/Release Specialist：发布准备、Project Launcher、CI、打包风险。
- Log/Crash Triage：UBT/UHT/UAT、`Saved/Logs`、callstack、ensure/assert。
- Verifier：构建、Blueprint compile、PIE、自动化测试、日志证据。

## Ownership boundaries

- 每个角色必须声明自己读取或建议修改的文件/资产边界。
- 两个角色不能同时声称拥有同一文件的最终决策；冲突交给 Coordinator。
- C++ API 与 Blueprint 图的交接要写明 owner、输入、输出和验证。
- 自动打包边界必须显式：multi-agent request must not trigger `$ue-build-release-automation` by itself。

## Parallel Discovery Results

并行发现结果统一使用以下格式：

```text
Role:
Status: READY | CONCERNS | BLOCKED
Files inspected:
Findings:
Risks:
Recommended next skill:
```

`BLOCKED` 只用于缺少必要文件、权限、日志、项目路径、用户授权或会导致结论无效的关键证据。

## 读取策略

- `solo` 不读取多 Agent references。
- `lean` 只读取当前角色需要的一份 reference。
- `full` 可读取全部 reference，但仍要按需摘要。
- Do not load these references when the task is a narrow single-domain fix.

## 工具

- 可用只读脚本 `skills/ue-multi-agent-workflow/scripts/ue_agent_plan.py` 根据请求生成 `solo` / `lean` / `full` 角色计划。
- 工具只生成分工建议，不修改 UE 项目。

## 输出

- Mode 和选择理由。
- Coordinator synthesis：综合结论、依赖顺序和后续技能。
- Parallel Discovery Results：各角色状态、发现、风险、阻塞。
- Ownership boundaries：文件/资产/系统归属边界。
- Focused follow-up：进入哪个具体 UE 技能继续实施或验证。

## 参考

- 角色定义读取 `references/ue-agent-roles.md`。
- 输出模板读取 `references/ue-agent-output-template.md`。
- 冲突处理读取 `references/ue-agent-conflict-resolution.md`。
