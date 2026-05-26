---
name: ue-world-interaction
description: 当 Unreal Engine 请求涉及拾取物、生成器、Overlap、Line Trace、交互提示、交互半径、视觉/音频反馈、Actor 生命周期或世界交互结果处理时使用。
---

# UE World Interaction

## 概览

这个技能负责世界交互系统。先明确交互发起者、目标、检测方式、反馈和结果归属，再设计 C++/Blueprint/资产流程。

## 工作流程

1. 选择检测方式：Trace、Overlap、接口扫描、Gameplay Tag 或专门交互组件。
2. 定义契约：`IInteractable`、ActorComponent、DataAsset、UI prompt、成功/失败原因。
3. 处理生命周期：生成、激活、冷却、销毁、复用、存档和网络 authority。
4. 设计反馈：高亮、Widget、音效、Niagara、动画、输入提示。
5. 验证：距离、遮挡、多目标优先级、多人和关卡切换。

## 规则

- Trace 适合视线/准星交互，Overlap 适合范围感知和持续提示。
- 交互结果由权威方确认，客户端可做预测提示但不能直接提交核心状态。
- 交互接口只暴露必要能力，复杂业务交给目标组件或系统。
- UI prompt 不应直接拥有交互状态。

## 输出

- 交互架构：Interactor、Interactable、检测、提示、执行和反馈。
- Blueprint/C++ 边界：接口、事件、组件、默认值。
- 资产：Widget、音效、VFX、DataAsset、Input Action。
- 验证：PIE、多目标、多人、失败路径。

## 参考

- 交互清单读取 `references/interaction-checklist.md`。
- 模板读取 `references/interaction-templates.md`。
