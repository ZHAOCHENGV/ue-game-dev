---
name: ue-stage-detect
description: 当用户询问 Unreal Engine 项目处于什么阶段、当前工作流缺什么、是否缺少实施/测试/打包前材料，或需要只读阶段与缺口分析时使用。
---

# UE Stage Detect

## 概览

这个技能只读判断 UE 项目的开发阶段和缺口。它不实现功能，而是说明项目当前具备什么、缺什么、下一步应该进入哪个技能。

## 阶段

- `intake`：入口信息不足，需先确认项目、目标或范围。
- `onboarding`：旧项目/现有项目需要只读熟悉。
- `brief`：需求需要澄清为功能简报。
- `planning`：需求清楚但缺实施计划。
- `implementation`：可以进入代码、Blueprint、资产或配置改动。
- `validation`：需要构建、PIE、测试或资产验证。
- `performance`：需要 profiling、打包准备或发布前检查。
- `done`：需要证据化验收和交接。

## 工作流程

1. 读取 `.uproject`、目录结构、README、计划文档、测试证据和最近日志。
2. 判断是否已有需求、计划、实现、测试、验证和项目记忆。
3. 标记缺口：需求不清、架构未知、测试缺失、打包风险、日志未分诊。
4. 输出阶段、证据、缺口和下一步技能。

## 规则

- 保持只读；不要改项目文件。
- 用证据判断阶段，不凭感觉。
- 如果用户要“开始做”，先给阶段结论，再说明是否应转入 brief、plan 或 domain skill。
- 不把没有证据的风险写成事实。

## 输出

- Stage：当前阶段。
- Evidence：支持判断的文件、目录、日志或测试。
- Gaps：进入下一阶段前缺什么。
- Next skill：建议的具体 UE 技能名。
- Minimal next action：最小下一步。

## 参考

- 阶段报告读取 `references/stage-report-template.md`。
