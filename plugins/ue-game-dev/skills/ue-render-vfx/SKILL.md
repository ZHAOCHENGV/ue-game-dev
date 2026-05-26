---
name: ue-render-vfx
description: 当 Unreal Engine 任务涉及渲染设置、材质、Material Function、自定义 HLSL、后处理、光照、LOD、Niagara、粒子、GPU emitter、视觉 Bug 或视觉性能时使用。
---

# UE Render VFX

## 概览

这个技能负责 UE 渲染、材质和 Niagara。先确认视觉目标、平台预算、资产路径和性能约束，再设计材质、VFX 或渲染调试方案。

## 使用场景

- 创建材质、后处理、Niagara 粒子、GPU 爆炸、拖尾、命中特效。
- 排查材质不显示、粒子被裁剪、LOD 错误、shader 编译慢、GPU/CPU 过高。
- 优化材质指令数、shader permutation、Niagara bounds、Scalability。

## 工作流程

1. 确认目标平台、渲染管线、地图、光照方案和性能预算。
2. 识别资产：Material、Material Instance、Texture、Niagara System/Emitter、Mesh、Post Process。
3. 设计参数：Scalar/Vector/Texture、User Parameter、Dynamic Material、Gameplay 触发。
4. 检查性能：材质复杂度、overdraw、bounds、tick、GPU/CPU sim、LOD 和 scalability。
5. 验证 Editor viewport、PIE、目标平台和 packaged build。

## 输出

- 资产设计：命名、路径、参数、实例化策略。
- 渲染/VFX 流程：触发方、生命周期、LOD、scalability。
- 性能风险：指令数、overdraw、shader permutation、Niagara tick/bounds。
- 验证：视觉检查、stat/profile、平台或 packaged build。

## 参考

- Niagara 清单读取 `references/niagara-checklist.md`。
- 渲染清单读取 `references/rendering-checklist.md`。
