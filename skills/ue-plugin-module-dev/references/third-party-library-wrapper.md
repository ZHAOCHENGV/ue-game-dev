# 第三方库封装为 UE 模块

## 目录建议

```text
Plugins/MyPlugin/
  Source/
    MyPluginRuntime/
    MyThirdParty/
      MyThirdParty.Build.cs
      Include/
      Lib/
      Bin/
```

## Build.cs 要点

- 头文件路径放 `PublicIncludePaths` 或更窄的 include 设置。
- 静态库按平台加入 `PublicAdditionalLibraries`。
- 动态库加入 `PublicDelayLoadDLLs` 和 `RuntimeDependencies`。
- 用 `Target.Platform` 区分 Win64、Android、iOS、Linux、Mac。
- 不要让 Runtime 模块直接包含 SDK 的大量私有头；封装成薄 C++ wrapper。

## DLL / so / dylib

- Win64 DLL 需要复制到 packaged build 可加载位置。
- Android `.so` 要匹配 ABI，并处理 Gradle/UPL。
- iOS 静态库或 framework 要处理签名、bitcode/架构和 bundle。
- packaged build 中验证库加载失败日志，而不是只测 Editor。

## API 边界

- 对上层 UE 代码暴露稳定 UObject/struct API。
- 第三方类型不要泄漏到 Blueprint 或大量 Public 头中。
- 错误码转换成 UE 可读 enum、log category 或 result struct。
- 异步 SDK 回调回到 GameThread 后再触发 UObject/Blueprint。

## 许可证与发布

- 记录第三方库版本、许可证、二进制来源和平台限制。
- CI/打包脚本要能找到库文件，不依赖开发者本机绝对路径。
