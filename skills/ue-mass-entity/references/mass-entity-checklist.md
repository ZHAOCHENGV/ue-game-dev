# Mass Entity 检查清单

当任务涉及 Mass processor、fragment、trait、spawner、crowd 或大规模 NPC 模拟时使用。

## 发现

- 确认启用的 Mass 插件：MassEntity、MassGameplay、MassRepresentation、MassAI、MassCrowd、ZoneGraph、SmartObjects 等。
- 定位已有 processor、fragment、tag、trait、observer、spawner 和 representation 配置。
- 记录目标实体规模、更新频率、表现 LOD、服务器/客户端边界和是否需要存档。

## 数据模型

- 每个 per-entity 状态用 fragment 或 tag 表达。
- 多实体共享的大配置放 shared fragment 或 Data Asset。
- Trait 只负责组装 entity composition，不承担长期运行逻辑。
- Actor bridge 必须说明实体到 Actor/Component 的映射和生命周期。

## Processor 与 Observer

- 每个 processor 只处理一个模拟关注点，并说明执行 phase。
- 写 fragment 的 processor 要说明读写依赖，避免隐式顺序假设。
- 添加/移除 fragment 的反应使用 observer，而不是每帧扫描所有实体。
- 清理路径要覆盖 despawn、representation 释放和 gameplay bridge 断开。

## 验证

- PIE 中确认 spawn 数量、fragment/tag 存在性和 processor 执行顺序。
- 测量目标规模下 processor 与 representation 成本。
- 检查 representation LOD、Actor spawn/despawn 和可见性切换。
- 如果实体行为影响玩法，至少验证服务器权威或客户端表现边界。
