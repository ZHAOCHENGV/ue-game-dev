# StateTree 与 Mass AI 准确性备注

当 AI/navigation 请求提到 StateTree、Mass Entity、群体 AI，或混合 Behavior Tree 与 UE 新 AI 框架时使用本参考。

## 路由边界

- Behavior Tree、Blackboard、EQS、NavMesh、AI Controller、AI Perception 和传统自主 agent 使用本 AI/navigation 技能。
- 任务主要是 StateTree task、evaluator、condition、transition、schema 或层级状态设计时，路由到 `$ue-state-trees`。
- 任务主要是 Mass processor、fragment、tag、observer、Mass spawner、Mass Crowd 或数据导向大量 agent 时，路由到 `$ue-mass-entity`。

## StateTree 集成

- StateTree 可以驱动 AI 或 gameplay state，不一定需要 Behavior Tree selector。
- Condition 和 transition 要显式，不要把转换决策藏在 task 内。
- Evaluator 用于外部数据收集，task 用于具备 enter/tick/exit 的动作。
- 用 StateTree debug 工具或定向日志验证 active state、transition path 和 task completion。

## Mass AI 集成

- Mass Entity 使用 fragment/tag/processor，而不是每个 agent 一个 UObject-heavy 状态。
- Actor representation 是桥接层，不一定是真实数据源。
- ZoneGraph、Smart Objects、StateTree 和 representation LOD 都可能参与 crowd 行为。
- 验证 entity count、processor phase、representation transition 和目标规模性能。
