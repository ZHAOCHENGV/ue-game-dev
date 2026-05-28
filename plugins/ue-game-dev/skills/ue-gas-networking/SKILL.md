---
name: ue-gas-networking
description: 当 Unreal Engine 任务涉及 Gameplay Ability System、Ability、Attribute、Gameplay Effect、Gameplay Cue、prediction、Ability Task、Blueprint Ability、ASC replication、RPC、authority flow 或多人能力调试时使用。
---

# UE GAS Networking

## 概览

这个技能处理 GAS 与多人同步。先确认 ASC 所在位置、属性归属、预测策略和 authority flow，再设计 Ability、Effect、Cue 和验证场景。

## 使用场景

- 创建 GameplayAbility、AttributeSet、GameplayEffect、GameplayCue。
- 排查 Ability 不激活、预测回滚、属性不同步、Cue 不显示、RPC 方向错误。
- 设计客户端预测、服务器确认、输入绑定、冷却、消耗、标签阻塞和多人 PIE 验证。

## 工作流程

1. 确认 ASC 在 Pawn、PlayerState 或组件中，明确 owner/avatar actor。
2. 设计属性和标签：AttributeSet、GameplayTag、GE modifier、replication mode。
3. 定义能力生命周期：输入、CanActivate、Commit、Task、EndAbility、Cancel。
4. 区分预测与服务器权威：哪些效果可预测，哪些必须等服务器。
5. 验证 dedicated/listen server、client latency、reconnect 或 possession 切换。

## 规则

- 属性变化用 AttributeSet 和 GE 表达，避免绕过 GAS 直接改 replicated 字段。
- Ability Task 生命周期必须跟 Ability 结束/取消绑定。
- Gameplay Cue 用于表现，不应承载核心权威逻辑。
- RepNotify、RPC 和 ASC replication mode 要与项目多人模型一致。
- Blueprint Ability 适合组合逻辑，复杂规则和安全校验放 C++。

## 输出

- GAS 架构：ASC、AttributeSet、Ability、Effect、Cue、Tag 分工。
- 网络路径：输入、预测、服务器确认、复制和回滚。
- Blueprint/C++ 边界：可调项、事件、任务和安全校验。
- 验证：多人 PIE、延迟、日志、Gameplay Debugger 和属性观察。

## 参考

- GAS API 准确性与网络所有权读取 `references/gas-api-accuracy.md`。
- GAS 模式读取 `references/gas-patterns.md`。
- 需要 GameplayAbility、AttributeSet 或 GameplayCue 模板时读取 `references/gas-ability-template.md`。
- 网络清单读取 `references/networking-checklist.md`。
