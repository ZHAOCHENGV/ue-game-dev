---
name: ue-physics-destruction
description: 当 Unreal Engine 请求涉及 Chaos Physics、碰撞通道、Physical Material、Geometry Collection、Fracture、布娃娃、Physics Constraint、物理动画混合、碰撞调试、物理性能、可破坏物或 Chaos 排查时使用。
---

# UE Physics Destruction

这个技能处理 UE5 Chaos 物理、碰撞配置、可破坏物、布娃娃和物理调试。重点是把玩法权威、碰撞数据、资产制作和运行时性能放在同一条链上。

## 工作流程

1. 判断请求属于碰撞过滤、刚体模拟、布娃娃、约束、Geometry Collection 破坏，还是物理性能。
2. 定位拥有者：Actor、Mesh/Component 层级、Collision Profile、Physical Material、Physics Asset、相关 Blueprint/C++。
3. 明确状态性质：纯表现、玩法权威、需要复制、需要存档，还是由动画驱动。
4. 修改 profile 或资产前先收集证据：collision view、Physics Debugger、日志和最小 PIE 复现。
5. 定义验证路径：overlap/hit、impulse response、constraint 稳定性、fracture 行为、网络 authority 和 packaged sanity。

## 碰撞与模拟规则

- 有意使用项目 collision channel，不要用宽泛的 `BlockAll` 或 `OverlapAll` 解决所有玩法交互。
- Object Type、Trace Response 和 Collision Enabled 必须一致：Query Only、Physics Only 或 Query and Physics。
- 可复用玩法类别优先使用命名 Collision Profile。
- 排查代码前先验证 `GenerateOverlapEvents`、`Simulation Generates Hit Events`、mass、damping 和 collision complexity。
- Physical Material 用于表面行为、脚步/VFX 路由、friction/restitution 调整，不要按 mesh 名硬编码表面行为。

## Chaos 与破坏

- 作者化 fracture 使用 Geometry Collection，不要把普通 StaticMeshComponent 模拟当作破坏系统。
- 先定义 damage threshold、cluster、collision particles、移除/生命周期规则，再接 Blueprint 或 C++ hook。
- 玩法权威要明确：服务器决定 destroyed 状态，客户端呈现 fracture/VFX/audio，除非项目有确定性同步层。
- 使用 Field、Cached Simulation 或平台 scalability 时，必须在 cooked build 验证。

## 布娃娃与约束

- Skeletal 模拟、命中反应和布娃娃使用 Physics Asset 与 constraint profile。
- 动画与物理混合要定义进入、恢复和清理状态。
- 合理设置 angular limit、mass ratio、projection 和必要的 substepping，避免约束抖动。
- 网络布娃娃要说明是本地表现还是服务器权威复制状态。

## 输出

- 碰撞/物理设置：组件、profile、channel、object type、hit/overlap 配置。
- 破坏或布娃娃流程：触发条件、权威位置、表现、清理和存档/复制影响。
- 调试证据：`show COLLISION`、`stat physics`、Physics Debugger 或最小 PIE 复现。
- 验证：Editor、PIE、多人和 packaged build 中需要确认的行为。

## 参考

- 修改碰撞、模拟、布娃娃或约束前读取 `references/chaos-physics-checklist.md`。
- 实现 Geometry Collection 或 fracture 流程前读取 `references/destruction-patterns.md`。
- 涉及物理性能、Tick 或平台 scalability 时使用共享 `rules/ue-performance.md`。
