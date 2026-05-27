# UE 性能规则

## Tick 与 Timer

- 不需要 Tick 的 Actor 设置 `PrimaryActorTick.bCanEverTick = false`。
- 低频逻辑优先事件或 Timer，避免无价值轮询。
- Tick 工作量要可界定、可 profiling。
- 避免在每帧循环里 Cast、搜索资产或调用 `GetAllActorsOfClass`。

## 内存与资产加载

- 可选、大型、装饰性或模式专属资产使用 soft reference。
- 首次使用可能卡顿时，在模式切换或加载边界预加载。
- 避免 DataTable 或 Data Asset 无意中 hard-reference 整个内容目录。
- soft reference 必须验证 packaged cook 覆盖。

## 渲染

- 使用 LOD、剔除距离、实例化、Nanite 适用性检查和材质复杂度审查。
- Niagara bounds 和 scalability 设置要明确。
- 控制 shader permutation 和 material feature switch。
- 视觉效果要在目标 scalability 上验证，不只看 Editor 默认设置。

## 物理

- 减少活跃 simulated bodies 和高频 overlap 检查。
- movable simulated object 避免 complex-as-simple collision，除非已测量成本。
- 只有稳定性需要时才启用 substepping。
- 限制破坏碎片生命周期、碰撞和 shard 数量。

## 网络

- 只复制最小权威状态。
- 使用 relevancy、dormancy 和频率控制。
- 避免高频 reliable RPC。
- 多人功能至少用匹配场景的 PIE 或 dedicated server 做 profiling。

## 打包

- Editor-only 行为与 packaged runtime 行为分离。
- 发布准备、打包失败诊断和自动打包是三个不同工作流。
- 行为依赖 Cook、Config、soft reference 或平台设置的功能要包含烟测。
