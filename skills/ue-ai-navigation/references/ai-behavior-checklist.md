# AI 行为检查清单

## 行为归属

- 确认行为由 AIController、Behavior Tree、StateTree、Gameplay Ability、Mass processor 还是 Pawn 组件驱动。
- Blackboard key 要有明确类型、写入方和清理时机。
- 感知事件只记录事实，决策交给行为树/状态树/组件。

## Behavior Tree

- Task 必须明确返回 `Succeeded`、`Failed` 或保持 `InProgress` 的条件。
- Service 不要做昂贵查询；需要缓存或降频。
- Decorator 条件要可解释，并能在 Gameplay Debugger 中观察。
- MoveTo 失败要记录目标、可达性、路径和阻塞原因。

## StateTree

- 适合状态驱动 AI、Gameplay State 或 UE5 项目。
- Enter/Exit 行为要处理打断、重复进入和资源释放。
- 与 Blackboard/Gameplay Tag 交互时明确谁是事实源。

## 验证

- `showdebug ai`
- Gameplay Debugger
- Visual Logger
- EQS preview
- 多 PIE 或 dedicated server 行为
