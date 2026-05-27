---
name: ue-log-crash-triage
description: 当用户提供或要求分析 Unreal Engine 日志、UBT 编译错误、UHT 反射错误、链接错误、Blueprint 编译错误、Editor 崩溃、callstack、ensure/assert、UAT 打包失败、Cook 错误或 Saved/Logs 输出时使用。
---

# UE Log Crash Triage

## 概览

这个技能用于日志和崩溃分诊。目标是找到第一个可行动错误、失败阶段、证据和下一步技能，而不是摘录整段日志。

## 使用场景

- 分析 `Saved/Logs`、UAT、UBT、UHT、Cook、PackagingResults、Editor crash 或 callstack。
- 排查 C++ 编译、UHT 反射、链接、Blueprint compile、资产 Cook、插件加载失败。
- 从大量日志中找第一个真正原因，而非后续连锁错误。

## 工作流程

1. 确认日志来源：Editor、UBT、UHT、UAT、Cook、PIE、Crash Reporter 或 platform log。
2. 定位失败阶段和第一个可行动错误。
3. 收集证据：错误行、文件路径、模块、资产、callstack 顶部、相关前文。
4. 分类：编译、反射、链接、资产、配置、网络、运行时崩溃、打包。
5. 路由下一步：C++、Blueprint、资产、打包性能、debug validation 或 build automation。

## 工具

- 可用只读脚本 `skills/ue-log-crash-triage/scripts/ue_log_triage.py` 快速提取日志首个可行动错误。
- 工具读取日志并输出失败阶段、证据和建议技能，不修改项目，也不执行打包。

## 规则

- 优先报告第一个 actionable error，不要被最后的 summary 误导。
- UHT 错误通常要检查宏、反射类型、generated header 和头文件包含顺序。
- Cook 错误要查资产路径、redirector、编辑器专用资产、平台不支持格式。
- 崩溃要区分 assertion、ensure、access violation、null UObject 和线程问题。
- 打包失败诊断不等于自动打包；显式打包才进入 `$ue-build-release-automation`。

## 输出

- Failure stage：UBT/UHT/Link/Cook/UAT/Editor/PIE/Runtime。
- First actionable error：最小可行动错误。
- Evidence：关键日志行和文件/资产路径。
- Likely cause：推断原因，标明推断依据。
- Next skill：后续具体 UE 技能名和建议验证。

## 常见问题

| 症状 | 可能原因 | 首个检查点 |
|------|----------|------------|
| `Cook failed` 前有大量 warning | 更早的资产加载、Blueprint 编译或 missing class 错误 | 向上找第一个 `Error:` |
| unresolved external | 缺实现、模块依赖或 API macro 错误 | 检查符号所属模块和 `.Build.cs` |
| Blueprint compile error | Pin 断裂、成员改名或父类 API 缺失 | 打开命名 Blueprint 并在 C++ 编译后重新 compile |
| callstack 末尾在引擎代码 | 项目回调更早传入无效数据 | 找到 engine frame 之上的第一个项目 frame |

## 参考

- 分诊报告模板读取 `references/triage-report-template.md`。
