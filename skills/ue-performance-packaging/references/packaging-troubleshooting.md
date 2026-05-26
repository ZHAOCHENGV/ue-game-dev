# 打包问题排查

## 常见阶段

- UBT build。
- UHT reflection。
- Cook。
- Stage。
- Pak/IoStore。
- Archive。

## 首个错误

- 优先找第一个 actionable error。
- 不要只看最后的 AutomationTool summary。
- 保留文件、资产、模块和平台上下文。

## 常见原因

- Blueprint compile error。
- 资产缺失或 redirector。
- Runtime 引用 Editor-only 类型。
- 第三方库未复制到 packaged build。
- 平台 SDK、证书或签名配置错误。
- 默认地图或 Cook 地图配置不正确。

## 下一步

- 有日志时进入 `$ue-log-crash-triage`。
- 只是准备度检查继续 `$ue-performance-packaging`。
- 用户明确要求生成/运行打包命令时进入 `$ue-build-release-automation`。
