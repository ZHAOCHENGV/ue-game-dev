---
name: ue-procedural-generation
description: 当 Unreal Engine 请求涉及 PCG、PCG Graph、ProceduralMeshComponent、InstancedStaticMesh、HierarchicalInstancedStaticMesh、Spline、运行时生成、确定性 seed、流送集成、碰撞或导航生成时使用。
---

# UE Procedural Generation

这个技能处理 PCG 图、运行时生成、实例化和生成式世界流程。重点是把确定性、流送、碰撞、导航、Cook 和性能边界提前说明。

## 工作流程

1. 判断生成方式：设计器编辑的 PCG、运行时 PCG、ProceduralMesh、ISM/HISM 放置、Spline 生成，还是自定义 C++ 生成。
2. 读取 `.uproject`、启用的 PCG/Procedural 插件、生成资产、目标地图、World Partition/Data Layer 设置和命名约定。
3. 定义生成结果所有权：编辑器 bake 资产、运行时 transient actor、可保存状态、复制状态，还是由 seed 确定性再生成。
4. 梳理依赖：输入数据、seed、bounds、biome/data assets、collision、navmesh、streaming grid 和 cleanup。
5. 定义验证：确定性、性能、碰撞/navmesh、packaged build 和流送行为。

## PCG 规则

- 设计师驱动的空间生成和数据化摆放优先使用 PCG Graph。
- inputs、bounds、seed、filters 和输出 actor/component 必须显式。
- 避免依赖 editor-only actor 或未 Cook 的资产。
- 扩大 bounds 前先验证 graph 成本和生成实例数量。
- 需要策划迭代时，把生成配置放在 Data Asset 中。

## 运行时生成规则

- 高数量重复网格优先使用 ISM/HISM，避免为静态装饰生成大量完整 Actor。
- 只有几何确实运行时变化时才使用 ProceduralMesh 或运行时 mesh 方案。
- 提前定义 collision 生成与 navmesh 更新行为。
- 需要跨会话或网络同步时，保持 deterministic seed 稳定。
- 生成编排与玩法状态变更分离，避免生成器直接拥有过多 gameplay 逻辑。

## 跨域交接

- 生成依赖 World Partition、Data Layers、runtime grid 或 level streaming 时进入 `$ue-world-streaming`。
- biome 表、生成规则资产、软引用、Asset Manager 规则或 Cook 收录进入 `$ue-data-management`。
- 实例数量、碰撞成本、Cook 体积或 packaged 行为是主要风险时进入 `$ue-performance-packaging`。

## 参考

- 实现 PCG Graph、运行时生成、实例化或生成碰撞前读取 `references/procedural-generation-checklist.md`。
