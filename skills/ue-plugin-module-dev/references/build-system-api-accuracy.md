# UE Build System API 准确性

本参考将 `quodsoler/unreal-engine-skills` 的 API 准确性思路改写进 UE Game Dev 插件风格。任务触及 `.Build.cs`、模块布局、插件描述或 include/link 错误时使用。

## Build.cs 放置

- `PublicDependencyModuleNames` 用于 public header 或 public inline code 中出现的类型所属模块。
- `PrivateDependencyModuleNames` 用于只在 `.cpp` 或 private header 中使用的模块。
- 现代 UE 模块布局下，`PublicIncludePaths` 和 `PrivateIncludePaths` 应很少使用；优先依赖标准 `Public/` 与 `Private/` 目录。
- 不要为了消除 include 错误添加宽泛依赖；先找到类型真正所属模块。

## Runtime 与 Editor

- Runtime 模块不能依赖 `UnrealEd`、`AssetTools`、`PropertyEditor`、`LevelEditor`、`ToolMenus` 或 editor-only style/tooling 模块。
- Editor 模块可以依赖 runtime 模块，runtime 模块不应依赖 editor 模块。
- 需要共享契约时，抽出窄 runtime/shared 模块，而不是制造循环依赖。

## Public API Macro

- 跨模块暴露的 public class 需要模块导出宏，例如 `MYMODULE_API`。
- 永不跨模块边界的 private 实现类不需要 export macro。
- Public header 保持最小和稳定，能 forward declare 就不要在头文件重 include。

## Target 与 Descriptor

- `.uproject` 和 `.uplugin` 的 module entry 必须匹配真实模块目录名。
- Target 文件定义 build target 类型和 included modules，不要把 target module 与 plugin descriptor module 混淆。
- Loading Phase 应明确；编辑器注册通常在 editor module startup，runtime gameplay 不应依赖 editor startup。

## Include/Link 分诊

- Include error：找到声明类型的 header，在真正需要的位置加窄 include。
- Link error：先检查 owning module dependency 和 export macro。
- Reflection/UHT error：检查 generated include 顺序、宏位置、不支持的反射类型和缺失模块依赖。
- Packaged build error：优先检查 editor-only 依赖、未 Cook 资产或 plugin descriptor/module type 不匹配。
