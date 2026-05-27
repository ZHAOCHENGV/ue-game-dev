# Destruction Patterns

## Geometry Collection Ownership

- 作者化 fracture 使用 Geometry Collection；普通不破坏道具使用 StaticMesh simulation 即可。
- Blueprint 或 C++ hook 前先定义 cluster hierarchy、damage threshold、collision particles 和 removal rules。
- 玩法状态与破坏表现分离。权威玩法决定 destroyed，Chaos 负责呈现 fracture。

## Damage Flow

1. 验证 hit/overlap 或 gameplay damage source。
2. 通过窄 component 或 interface 施加 damage，不要散落在多个 Blueprint graph。
3. 从一个状态切换触发 fracture、VFX、audio、camera shake 和 gameplay reward。
4. 除非项目确实需要碎片持久化，否则只保存 gameplay state。

## 性能边界

- 限制活跃碎片和 debris lifetime。
- 使用 clustering 避免一次产生过多 rigid bodies。
- 在代表性平台 scalability 上 profiling。
- 低端平台提供 fallback：预破碎 mesh、更少 shard 或非模拟破坏。

## 验证

- 使用 Field 或 Cached Simulation 时测试 Editor PIE、standalone 和 packaged build。
- 确认复制项目不会让客户端独立决定 break state。
- 检查破坏后的 navmesh、collision blocking 和 save/load 行为。
