# 插件与模块检查清单

## 描述文件

- `.uplugin` 中 `FileVersion`、`VersionName`、`FriendlyName`、`Category`、`CanContainContent` 正确。
- 模块 Type 与职责一致：Runtime、Editor、Developer、Program。
- LoadingPhase 合理，不依赖尚未初始化的系统。
- 平台 allow/deny list 与第三方库和目标平台一致。

## Build.cs

- Public/PrivateDependencyModuleNames 最小化。
- Runtime 模块不依赖 `UnrealEd`、`AssetTools`、`Blutility` 等 Editor 模块。
- Include path、third-party lib、runtime dependency 按平台配置。
- API macro 与模块名一致。

## 目录

- Public 只放跨模块 API。
- Private 放实现、注册、helper 和 editor-only 细节。
- Resources、Content、Config、Shaders 是否需要随插件分发。
- 插件 Content 需要 `.uplugin` 启用 `CanContainContent`。

## 验证

- Editor 启动、插件启用/禁用、热重载或重启。
- 目标模块编译、Blueprint compile、PIE。
- packaged build 中 Runtime 模块不拉 Editor 依赖。
- 第三方 DLL/so/dylib 能在打包后加载。
