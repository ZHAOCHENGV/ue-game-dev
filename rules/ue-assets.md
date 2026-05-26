# UE Assets 规则

## 命名前缀速查

| 类型 | 常用前缀 |
|------|----------|
| Blueprint | `BP_` |
| Widget Blueprint | `WBP_` |
| Static Mesh | `SM_` |
| Skeletal Mesh | `SK_` |
| Material | `M_` |
| Material Instance | `MI_` |
| Texture | `T_` |
| Niagara System | `NS_` 或 `FXS_` |
| Sound Cue / Sound Wave | `SC_` / `SW_` |
| Input Action / Mapping Context | `IA_` / `IMC_` |
| Data Asset / Primary Data Asset | `DA_` / `PDA_` |

## 引用规则

- 运行时可选资产优先用 soft reference，避免硬引用把大量资产拉进内存或 Cook。
- 不要硬编码长资产路径；用 DataAsset、配置、Primary Asset 或集中表管理。
- Editor-only 资产和类型不要泄漏到 Runtime 或 packaged build。
- 移动/重命名资产后处理 redirector，并验证引用链。

## 目录与归属

- 资产目录应按功能、系统或插件归属组织，不要把所有内容堆进 `Content/Blueprints`。
- 插件资产放在插件 Content 下，并确认 `.uplugin` 是否启用 `CanContainContent`。
- 共享资产要有明确 owner，避免多个系统随意修改同一 DataAsset。

## 验证

- 检查资产引用、缺失贴图、材质编译、蓝图编译和 Cook。
- 目标平台验证压缩、LOD、贴图尺寸、音频格式和 shader permutation。
- 对运行时加载的 soft reference，验证加载失败和异步时序。
