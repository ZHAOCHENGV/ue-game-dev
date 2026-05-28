---
name: ue-ai-navigation
description: 当 Unreal Engine 任务涉及 NPC 行为、Behavior Tree、Blackboard、EQS、NavMesh、AI Controller、AI Perception、StateTree、Mass Entity、群体移动或 AI 调试时使用。
---

# UE AI Navigation

## 概览

这个技能负责 UE AI 与导航工作流。先确认 AI 决策归属、导航数据、感知来源和调试证据，再设计或排查 Behavior Tree、StateTree、EQS、NavMesh 和 AI Controller。

## 使用场景

- 设计 NPC 巡逻、追击、搜索、战斗、撤退、交互等行为。
- 排查 AI 不移动、路径失败、感知不触发、任务卡住或状态切换异常。
- 搭建 Behavior Tree、Blackboard、EQS、AI Perception、NavLink、Smart Object 或 StateTree。
- 做多人场景中的 AI 权威、复制和客户端表现边界。

## 工作流程

1. 确认 AI 拥有者：Pawn、AIController、Behavior Tree、StateTree、Mass processor 或 Gameplay Ability。
2. 检查导航基础：NavMeshBoundsVolume、agent radius/height、Supported Agents、Runtime Generation、动态障碍和关卡流送。
3. 定义 Blackboard key：目标 Actor、位置、状态枚举、感知时间戳、可达性和失败原因。
4. 把高频感知、路径和查询结果缓存到服务或组件，避免每帧重复重算。
5. 对行为切换写出可观察证据：Gameplay Debugger、`showdebug ai`、EQS 预览、Visual Logger 和 PIE 场景。

## 设计规则

- Behavior Tree 适合清晰的任务树；StateTree 适合状态驱动、Gameplay State 或 UE5 项目。
- EQS 用于可解释的环境查询，不要把复杂业务规则藏在单个 query 里。
- 感知事件只负责记录事实，决策应放在 Controller、Tree/StateTree 或专门组件中。
- 动态场景先确认 NavMesh 是否需要 runtime rebuild，再决定移动逻辑。
- 多人 AI 通常由服务器拥有状态，客户端只表现复制结果或局部视觉反馈。

## 调试清单

- 确认 AIController 是否 Possess 了 Pawn，BrainComponent 是否运行。
- 检查 Behavior Tree task 是否返回 `Succeeded`、`Failed` 或仍在 `InProgress`。
- 验证 Blackboard key 类型、名称和写入时机。
- 检查 MoveTo 目标是否可达、是否被碰撞/agent 设置阻挡。
- 用 Gameplay Debugger 查看感知、行为树、路径和当前目标。

## 输出

- AI 架构：Controller、Pawn、Behavior Tree/StateTree、Blackboard、感知和移动组件分工。
- 关键资产：BT、BB、EQS、NavMesh、DataAsset、Gameplay Tag 或 StateTree 名称。
- 实现步骤：C++/Blueprint/资产配置分开描述。
- 验证方案：至少包含一个 PIE 场景和一条调试命令。

## 参考

- StateTree 与 Mass AI 路由边界读取 `references/state-tree-mass-ai-accuracy.md`。
- 行为设计时读取 `references/ai-behavior-checklist.md`。
- 导航、MoveTo 或 NavMesh 问题读取 `references/navigation-checklist.md`。
