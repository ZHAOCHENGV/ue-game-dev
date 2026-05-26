---
name: ue-build-release-automation
description: 当用户明确要求为 Unreal Engine 项目创建或运行打包、RunUAT、BuildCookRun、Project Launcher、CI 发版流水线或一键构建自动化时使用。
---

# UE Build Release Automation

## 显式调用边界

Use only when the current user explicitly asks to package, build, release, run `RunUAT`/`BuildCookRun`, create Project Launcher profiles, or create CI release automation.

这个技能会生成或指导执行打包自动化，属于主动操作边界。不要因为用户只是询问发布准备、性能检查或打包失败诊断就自动进入这里；那些情况先走 `$ue-performance-packaging` 或 `$ue-log-crash-triage`。

## 使用场景

- 生成 Win64/Android/iOS/Server 的 `RunUAT BuildCookRun` 命令。
- 创建一键打包脚本、Project Launcher 配置或 CI release job。
- 设计构建产物目录、版本号、日志采集、归档和失败回传。
- 用户明确要求“打包”“自动打包”“运行打包”“发版流水线”。

## 工作流程

1. 确认 `.uproject` 路径、UE 安装路径、平台、配置、目标、Maps、Cook 策略和输出目录。
2. 选择构建方式：本地 PowerShell/Bat、Project Launcher、BuildGraph、GitHub Actions/Jenkins/TeamCity。
3. 生成命令前说明风险：会写入 `Saved/`、`Intermediate/`、`Binaries/`、输出目录和日志。
4. 如果需要运行命令，先得到用户明确授权并记录环境。
5. 输出失败诊断入口：`Saved/Logs`、UAT log、Cook log、首个可行动错误和后续 `$ue-log-crash-triage`。

## 命令规则

- 默认使用显式路径，不依赖当前目录猜测。
- 区分 Development、Shipping、Client、Server、Editor target。
- Cook/Stage/Pak/Archive 参数要和平台匹配。
- Android/iOS 必须提示 SDK、证书、签名、NDK/Xcode 或设备配置风险。
- CI 中要缓存 DerivedDataCache，但不要缓存易污染的 Intermediate 产物。

## 输出

- 打包前提：项目、引擎、平台、配置和地图。
- 命令或流水线片段：保留 `RunUAT`、`BuildCookRun`、环境变量和路径。
- 产物与日志：Archive 目录、日志位置、失败时下一步。
- 安全提示：是否会写入大量构建产物，是否需要用户授权运行。

## 参考

- 命令模板读取 `references/buildcookrun-commands.md`。
- CI 模板读取 `references/ci-build-templates.md`。
- 发版检查读取 `references/release-automation-checklist.md`。
