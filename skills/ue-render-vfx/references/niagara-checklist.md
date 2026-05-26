# Niagara 检查清单

## 系统选择

- CPU emitter 适合需要碰撞事件、Gameplay 回调或少量精确粒子。
- GPU emitter 适合大量视觉粒子，但不要依赖 CPU 事件。
- 明确 System、Emitter、User Parameter 和触发方的生命周期。

## Bounds 与裁剪

- 粒子消失先检查 fixed bounds、camera culling、scalability 和 LOD。
- 大范围特效需要合理 bounds，避免过大导致一直渲染。
- 附着 Actor 或移动源时，确认 bounds 是否随 owner 更新。

## 参数与触发

- User Parameter 按 gameplay 含义命名，例如 `ImpactNormal`、`Intensity`、`SurfaceType`。
- 不要每帧写入无变化参数；优先事件触发或低频更新。
- Spawn burst、loop、deactivate、destroy 要和 owner 生命周期一致。

## 性能

- 检查 tick cost、particle count、overdraw、material complexity、collision、lights。
- 使用 scalability 限制低端平台数量、距离、LOD 和透明特效。
- GPU sim、ribbon、mesh renderer、collision 和 light renderer 要分别评估成本。

## 验证

- Editor viewport、PIE、packaged build、目标平台都要看一次高风险特效。
- 记录资产路径、触发事件、预期视觉、实际症状和性能指标。
