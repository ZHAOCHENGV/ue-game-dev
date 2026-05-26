---
name: ue-workflow-state
description: 当用户要求创建、刷新、读取或使用 Unreal Engine 项目的持久 AI 可读记忆，尤其是 Saved/CodexWorkflow 项目上下文、模块地图、资产索引、决策、已知风险、旧项目接手记录或当前任务状态时使用。
---

# UE Workflow State

## 概览

这个技能负责 `Saved/CodexWorkflow/` 项目记忆。它把跨会话有用的信息写成 AI 可读 Markdown，帮助后续二开、计划、调试和验收不用从零开始。

## 使用场景

- “为这个 UE 项目建立项目记忆”。
- 旧项目接手后保存项目地图、模块、资产、风险和决策。
- 新会话读取已有 CodexWorkflow 作为上下文。
- 功能完成后刷新 active task、known risks、验证证据。

## 建议文件

- `Saved/CodexWorkflow/project-context.md`
- `Saved/CodexWorkflow/module-map.md`
- `Saved/CodexWorkflow/asset-index.md`
- `Saved/CodexWorkflow/decisions.md`
- `Saved/CodexWorkflow/known-risks.md`
- `Saved/CodexWorkflow/active-task.md`

## 工作流程

1. 读取现有 `Saved/CodexWorkflow/`，避免覆盖用户已有记录。
2. 从 `.uproject`、`Source/`、`Plugins/`、`Config/` 和文档中提取稳定事实。
3. 将推断和事实分开标注，记录更新时间和证据来源。
4. 更新当前任务时保留历史决策，不删除不相关风险。
5. 输出本次写入/刷新内容和后续使用建议。

## 规则

- 不把临时猜测写成事实。
- 不保存敏感 token、私钥或账号。
- 记录应服务后续 Codex 阅读，避免长篇流水账。
- 用户只要求读取时保持只读。

## 输出

- 已读取或写入的 CodexWorkflow 文件。
- 新增事实、决策、风险和当前任务状态。
- 后续建议：进入 onboarding、brief、plan、debug 或 done。

## 参考

- 文件模板读取 `references/state-file-templates.md`。
