---
name: ue-mass-entity
description: 当 Unreal Engine 请求涉及 Mass Entity、MassProcessor、MassFragment、MassTag、MassObserver、MassSpawner、Mass Crowd、Mass AI、ZoneGraph、Smart Objects、大量 NPC 群体或数据导向模拟时使用。
---

# UE Mass Entity

这个技能处理 Mass Entity 与大规模数据导向模拟。重点是明确 processor 所有权、fragment 数据、表现层和传统 Gameplay/AI 的交接点。

## 工作流程

1. 读取 `.uproject`、启用的 Mass 插件、模块 `.Build.cs`、现有 processor、fragment、trait、spawner、ZoneGraph 和 crowd 配置。
2. 判断实体领域：人群、交通、AI agent、感知式模拟、仅表现 actor，还是 gameplay bridge。
3. 梳理数据所有权：fragment、tag、shared fragment、trait、processor、observer、subsystem 和 actor representation。
4. 决定行为位置：Mass processor、StateTree/Mass 行为、AI Controller 桥接、ActorComponent 或普通 gameplay actor。
5. 定义验证：spawn 数量、processor phase、fragment 变更、representation、服务器/客户端行为和性能。

## 设计规则

- 单个实体状态优先建模为 fragment 和 tag；只有桥接到 Actor 时才引入 per-entity UObject 状态。
- Processor 聚焦一个模拟关注点，并放入正确 execution phase。
- 添加/移除 fragment 的响应优先用 observer，不用大范围轮询。
- Actor representation 保持轻量；不要为每个 entity 生成完整 Actor，除非项目明确需要。
- 通用配置放 shared fragment，避免把大块不可变数据复制到每个 entity。
- Mass 是模拟框架，不是所有 Gameplay Actor 的替代品；必须明确桥接点和所有权。

## 跨域交接

- Behavior Tree、EQS、NavMesh 或 AI Perception 仍归 `$ue-ai-navigation`。
- Mass 行为由 StateTree task/evaluator 驱动时进入 `$ue-state-trees`。
- 人群规模、processor 成本、representation LOD 或 packaged 行为是主要风险时进入 `$ue-performance-packaging`。
- Actor/Component 桥接或 Gameplay C++ 包装进入 `$ue-cpp-gameplay`。

## 输出

- Mass 数据模型：fragments、tags、traits、shared fragments 和 processors。
- 执行模型：processor phase、observer、spawn/despawn 和 representation。
- Gameplay 交接：Actor bridge、AI/StateTree、网络和保存状态边界。
- 验证：实体数量、执行顺序、表现层 LOD、性能和最小 PIE 场景。

## 参考

- 添加 Mass processor、fragment、trait、observer 或 crowd 行为前读取 `references/mass-entity-checklist.md`。
