# UE Packaging 规则

## 边界

- 打包准备检查和打包自动化是两件事。
- 用户明确要求运行或生成 `RunUAT` / `BuildCookRun` / CI 打包时，才进入显式自动化流程。
- 只问“是否准备好打包”时，先做 readiness、日志和风险检查。

## 平台差异

| 平台 | 常见风险 |
|------|----------|
| Win64 | Editor-only 依赖、缺 DLL、路径过长、Visual C++ runtime |
| Android | SDK/NDK/JDK 版本、签名、texture format、权限、ABI |
| iOS | 证书、provisioning profile、Xcode、Metal、bundle id |
| Dedicated Server | Client-only/UI 依赖、地图列表、server target、Online 配置 |

## Cook 失败常见原因

- 缺失资产、redirector、硬编码路径或 soft reference 未纳入 Cook。
- Blueprint 编译错误或 nativization/反射问题。
- Runtime 模块引用 Editor-only 类型或插件。
- 平台不支持的纹理、音频、shader 或第三方库。
- `DefaultGame.ini` / `DefaultEngine.ini` 中地图、插件、平台设置不一致。

## 配置检查

- `[/Script/EngineSettings.GameMapsSettings]` 中默认地图和 GameMode。
- Packaging Settings 中 Maps to Cook、Use Pak、Full Rebuild、Build Configuration。
- 插件启用状态、platform allow/deny list 和 content inclusion。
- 第三方 DLL/so/dylib 的 RuntimeDependencies。

## 验证

- 保存 UAT log、Cook log、首个可行动错误和输出目录。
- 区分 Editor、Standalone、Development packaged 和 Shipping packaged 行为。
- 打包失败先走 `$ue-log-crash-triage` 找第一错误，再决定是否调整配置或进入显式自动化。
