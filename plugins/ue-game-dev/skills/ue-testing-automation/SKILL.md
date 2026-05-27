---
name: ue-testing-automation
description: 当 Unreal Engine 任务涉及插件或玩法功能测试、AutomationSpec、FAutomationTestBase、Functional Tests、编辑器烟测、PIE/多人场景、资产验证、打包烟测或回归计划时使用。
---

# UE Testing Automation

## 概览

这个技能负责 UE 测试与验证设计。根据风险选择 Automation、Functional Test、PIE、Editor smoke、资产验证、多人场景或打包烟测。

## 使用场景

- 给 C++/Blueprint/插件/编辑器工具/UI/GAS/网络功能写测试方案。
- 创建 `AutomationSpec`、`FAutomationTestBase`、Functional Test 或命令行测试。
- 设计回归矩阵、PIE 多客户端、资产验证、packaged build smoke。

## 工作流程

1. 明确风险：编译、反射、Blueprint、资产、UI、网络、性能、打包。
2. 选择测试层：unit、automation、functional、editor smoke、PIE、manual checklist。
3. 定义 fixture：地图、Actor、资产、输入、预期状态和清理。
4. 写出运行命令、结果位置、失败诊断和 CI 可行性。
5. 如果测试代价过高，给出最小烟测和剩余风险。

## 规则

- 不为简单文档改动强行设计重测试；按风险扩展覆盖。
- Blueprint 和资产改动至少要有 compile/PIE/引用检查路径。
- 网络功能要说明 server/client 数量、authority 和同步观察点。
- 编辑器工具要验证注册、注销、Undo/Redo 和禁用插件。
- 打包相关要区分 readiness、diagnosis 和 explicit automation。

## 输出

- 测试矩阵：层级、场景、预期、命令。
- 自动化候选：AutomationSpec、Functional Test、Editor smoke 或 CI。
- 手工验证：PIE、多人、UI、资产、打包烟测。
- 证据记录：可用 `templates/ue-test-evidence.md`。

## 参考

- 测试清单读取 `references/testing-checklist.md`。
- 需要 Automation Test 或 Functional Test 代码骨架时读取 `references/automation-test-template.md`。
