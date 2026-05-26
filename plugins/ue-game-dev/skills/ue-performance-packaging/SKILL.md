---
name: ue-performance-packaging
description: 当 Unreal Engine 请求涉及 PIE 性能检查、runtime stat、profiling、资产引用验证、构建配置、打包失败诊断、平台设置、发布准备、打包烟测或 go/no-go 检查时使用。
---

# UE Performance Packaging

## 概览

这个技能处理性能和打包准备，但不主动生成或运行打包自动化。用户明确要求自动打包时才切到 `$ue-build-release-automation`。

## 使用场景

- 帧率、卡顿、内存、shader、Niagara、UI、动画或网络性能检查。
- Cook/package 失败诊断、发布前检查、packaged build 差异。
- 构建配置、平台设置、资产引用、Editor-only 依赖和烟测清单。

## 工作流程

1. 确认目标平台、配置、地图、性能预算和失败阶段。
2. 收集证据：`stat unit`、`stat game`、`stat gpu`、`stat slate`、Insights、UAT/Cook log。
3. 区分 Editor、PIE、Standalone、packaged build 行为。
4. 检查资产引用、Cook 设置、DefaultGame.ini、DefaultEngine.ini、插件和平台 SDK。
5. 输出 go/no-go 结论和最小后续验证。

## 输出

- 性能/打包目标与当前证据。
- 风险分类：CPU、GPU、内存、IO、Cook、配置、平台、资产。
- 下一步：profiling、日志分诊、资产修复、配置调整或显式打包自动化。
- 验证：PIE、Standalone、packaged build、目标平台烟测。

## 参考

- 性能与打包清单读取 `references/performance-packaging-checklist.md`。
- 打包问题读取 `references/packaging-troubleshooting.md`。
