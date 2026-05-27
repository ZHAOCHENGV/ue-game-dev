# Runtime 与 Editor 插件脚手架

```text
Plugins/SampleTools/
  SampleTools.uplugin
  Source/
    SampleToolsRuntime/
      SampleToolsRuntime.Build.cs
      Public/
      Private/
    SampleToolsEditor/
      SampleToolsEditor.Build.cs
      Public/
      Private/
```

## 模块规则

- Runtime module 只依赖 runtime-safe modules。
- Editor module 可以依赖 `UnrealEd`、`ToolMenus`、`Slate` 和项目 runtime contracts。
- Public headers 暴露稳定 contract；Private headers 保存实现细节。
- API macro 必须匹配模块名，例如 `SAMPLETOOLSRUNTIME_API`。

## 验证

- 确认 `.uplugin` module `Type`。
- 确认 Runtime 不依赖 Editor。
- 添加 Editor module 后构建 Editor target。
- Runtime module 内容或配置变化后测试 packaged game。
