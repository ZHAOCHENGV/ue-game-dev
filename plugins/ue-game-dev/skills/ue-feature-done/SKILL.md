---
name: ue-feature-done
description: 当 Unreal Engine 工作准备收尾、声称完成、提交、交接或用户询问是否已完成时使用，尤其适用于 C++、Blueprint、资产、模块、UI、网络、测试、性能或打包相关任务。
---

# UE Feature Done

## 概览

这个技能用于完成验收。不要只说“完成了”；要给出证据、未验证项、风险、回归范围和交接说明。

## 使用场景

- 功能实现后需要确认是否可交付。
- 用户要求提交前检查、验收清单、测试证据或交接说明。
- C++、Blueprint、资产、UI、网络、性能或打包风险需要收尾记录。

## 工作流程

1. 回看原始目标和范围，确认是否有偏离。
2. 汇总实际改动：代码、Blueprint、资产、配置、文档、测试。
3. 运行合适验证：构建、Blueprint compile、PIE、自动化测试、日志、多人、打包烟测。
4. 标记未验证项和原因，不把未跑过的检查写成通过。
5. 输出交接：如何测试、已知风险、后续建议和回滚点。

## 证据要求

- C++：目标模块构建、UHT/链接结果、关键日志。
- Blueprint：编译状态、事件唯一性、Pin 兼容、PIE 流程。
- UI：输入焦点、DPI/窗口尺寸、手柄/键鼠。
- 网络：server/client、authority、replication、RPC 场景。
- 性能/打包：stat/profiling、Cook/package 或明确未执行原因。

## 输出

- 结果：完成、部分完成或存在阻塞。
- 变更摘要：文件/资产/配置和行为变化。
- 验证证据：命令、场景、结果。
- 未验证与风险：具体、诚实、可追踪。
- 下一步：如果需要，给出最小后续行动。

## 参考

- 验收清单读取 `references/done-checklist.md`。
- 可使用 `templates/ue-test-evidence.md` 记录证据。
