# Rendering 与 Niagara API 准确性备注

编写 Unreal 渲染、材质或 Niagara 建议前使用本参考，重点是具体引擎概念和常见幻觉点。

## 材质

- 参数调优优先使用 Material Instance，可复用图逻辑使用 Material Function。
- Static Switch 会增加 shader permutation；scalar/vector/texture parameter 调整实例，通常不会以同样方式增加 permutation。
- Dynamic Material Instance 是运行时对象，要定义 owner、生命周期和参数更新频率。
- Custom HLSL 节点需要显式输入和平台假设，不要在未确认项目版本时承诺具体引擎 shader API。

## Renderer 功能

- Nanite、Lumen、Virtual Shadow Maps、Forward Rendering、Mobile、VR 和主机类目标平台约束不同。
- Renderer config 修改是项目级风险；改动时说明 scalability group 和平台检查。
- Render target 与 scene capture 要检查更新频率、分辨率、格式、内存成本和所有权。

## Niagara

- CPU 和 GPU emitter 的 collision、event 和 data access 限制不同。
- GPU emitter 通常需要 fixed bounds；缺失 bounds 可能表现为随机裁剪。
- Gameplay 驱动参数优先用 user parameter，不要复制多个 system。
- 频繁或常驻特效要检查 emitter/system scalability、spawn count、tick cost 和 renderer count。

## 证据

- 包含 viewport/PIE 视觉验证。
- 性能相关任务包含 material stats、shader compile 说明、Niagara debug 证据或 Unreal Insights。
