# Navigation 检查清单

## NavMesh

- 地图中存在 `NavMeshBoundsVolume`，范围覆盖 AI 活动区域。
- Supported Agents 的 radius、height、step height、slope 与 Pawn 碰撞匹配。
- Runtime Generation 与动态障碍需求一致。
- 关卡流送或 World Partition 场景确认 nav data 加载时机。

## MoveTo

- 目标 Actor/Location 有效且可达。
- AIController 已 Possess Pawn，BrainComponent 正在运行。
- Pawn 有 MovementComponent，collision channel 不阻挡自身移动。
- Acceptance Radius、Use Pathfinding、Allow Partial Path 设置符合需求。

## 动态障碍

- 门、移动平台、临时阻挡物需要 nav modifier、dynamic obstacle 或 smart link。
- 不要让大量动态物体持续重建 NavMesh。
- 对跳跃、攀爬、传送使用 Smart Nav Link 或自定义移动逻辑。

## 调试

- `show Navigation`
- `showdebug ai`
- Gameplay Debugger 的 NavMesh、Path、Behavior Tree 页面。
- Visual Logger 记录路径请求和失败原因。
