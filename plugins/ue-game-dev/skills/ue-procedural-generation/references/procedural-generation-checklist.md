# 程序化生成检查清单

当任务涉及 PCG Graph、运行时生成、ProceduralMesh、ISM/HISM、Spline 或生成式世界时使用。

## 发现

- 确认启用的 PCG/procedural 插件和目标引擎版本。
- 定位 PCG Graph、输入 actor、bounds、data assets、biome 规则、目标地图和 World Partition/Data Layer 设置。
- 记录生成结果是 editor baked、runtime transient、可保存状态、可复制状态，还是由 seed 再生成。

## 确定性与数据

- 每个生成入口要有明确 seed、bounds、输入数据和清理策略。
- 需要跨会话或网络一致时，生成结果应由稳定数据和 seed 决定。
- Designer-facing 配置放 Data Asset 或表格，避免硬编码在图或 C++ 里。
- 生成资产要检查 Asset Manager/Cook 规则和软引用加载。

## 运行时性能

- 大量重复静态网格使用 ISM/HISM。
- ProceduralMesh 只用于确实需要运行时改变几何的场景。
- 记录 instance count、collision cost、navmesh update 和 streaming cost。
- 扩大生成区域前先做小 bounds 性能验证。

## 验证

- 同一 seed 多次生成结果一致。
- Packaged build 中生成资产可加载，不依赖 editor-only 对象。
- 碰撞、导航和交互行为符合预期。
- World Partition/Data Layer 场景下验证加载、卸载和清理。
