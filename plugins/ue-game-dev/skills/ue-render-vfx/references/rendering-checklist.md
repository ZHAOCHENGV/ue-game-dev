# UE Rendering 检查清单

## 材质

- 检查材质域、blend mode、shading model、two-sided、translucency 和 usage flags。
- 优先通过 Material Instance 暴露参数，不复制大量 Material。
- 控制 shader permutation：static switch、quality switch、feature level 分支要有必要性。
- 材质复杂度、overdraw、texture sample、custom HLSL 都要按平台预算评估。

## 纹理与资源

- 验证纹理尺寸、压缩格式、mip、sRGB、normal map 设置和 streaming。
- UI、mask、normal、HDR、virtual texture 使用各自合适设置。
- 运行时动态材质要有 owner 和释放策略，避免无限创建 MID。

## 光照与后处理

- 明确 Lumen、Nanite、Virtual Shadow Map、baked lighting 或 mobile renderer 目标。
- Post Process Volume、camera override 和 project setting 之间要避免互相覆盖。
- 视觉问题要区分 Editor viewport、PIE、Standalone 和 packaged build。

## 性能

- 使用 `stat gpu`、GPU Visualizer、Unreal Insights、Shader Complexity、Quad Overdraw。
- 检查 draw call、material instruction、overdraw、shadow、translucency 和 Niagara tick。
- 目标平台验证 scalability、device profile、resolution scale 和 fallback。

## 交接

- 记录资产路径、材质参数、触发条件、预期视觉和首个异常症状。
- 给出最小复现场景和截图/视频需求。
