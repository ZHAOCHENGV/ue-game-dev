---
name: ue-input-enhanced
description: 当 Unreal Engine 请求涉及 Enhanced Input、Input Actions、Input Mapping Contexts、输入 modifiers/triggers、PlayerController 或 Pawn 绑定、运行时映射变更、按键重绑、本地多人、UI 焦点/输入模式冲突或输入事件不触发时使用。
---

# UE Enhanced Input

## 概览

这个技能负责 UE Enhanced Input。先确认谁拥有输入、Mapping Context 何时添加、Input Action 如何绑定，再处理 UI 焦点、重绑和多人。

## 使用场景

- 创建 `IA_`、`IMC_`、modifier、trigger、输入绑定和重绑 UI。
- 排查 `IA_Jump` 不触发、输入被 UI 吃掉、Context 优先级错、Pawn 没绑定。
- 处理本地多人、Gamepad/Keyboard 切换、CommonUI 和输入模式冲突。

## 工作流程

1. 确认输入拥有者：PlayerController、Pawn、Character、EnhancedInputComponent、LocalPlayer Subsystem。
2. 检查 `Input Action`、`Input Mapping Context`、priority、添加/移除时机和平台映射。
3. 验证绑定：`SetupPlayerInputComponent`、`BindAction`、trigger event、函数签名。
4. 处理 UI：Input Mode、focus、mouse cursor、CommonUI action routing、mapping context 切换。
5. 验证 PIE、多设备、本地多人、暂停、重生和 possession 切换。

## 规则

- Mapping Context 应由 LocalPlayer Subsystem 管理，避免散落重复添加。
- 输入事件不触发时先查 possession、component、context、priority、trigger，再看业务逻辑。
- UI 打开/关闭要成对恢复输入模式和焦点。
- 重绑要保存用户设置，并处理冲突、不可绑定键和默认值恢复。
- 本地多人必须按 LocalPlayer 区分输入和 UI 焦点。

## 输出

- 输入资产：`IA_`、`IMC_`、modifier、trigger、默认键位。
- 绑定路径：Controller/Pawn/Component、函数、trigger event。
- UI/重绑策略：焦点、输入模式、保存和冲突处理。
- 验证：PIE、手柄/键鼠、本地多人和调试命令。

## 常见问题

| 症状 | 可能原因 | 首个检查点 |
|------|----------|------------|
| Action 从不触发 | Mapping Context 没加到 LocalPlayer Subsystem | 记录 `AddMappingContext` 的 owner 和 priority |
| Action 触发两次 | C++ 与 Blueprint 重复绑定或 setup 重复执行 | 检查 `SetupPlayerInputComponent` 和 Event Graph 输入节点 |
| UI 吃掉 Gameplay 输入 | Input Mode、focus 或 CommonUI activation 拥有 action | 检查焦点 widget 和 active mapping contexts |
| 重绑重启后丢失 | 用户设置未保存或 context 从默认值重建 | 检查 save slot/config 写入和 reload 顺序 |

## 参考

- 输入清单读取 `references/enhanced-input-checklist.md`。
- 重绑和 UI 读取 `references/rebinding-and-ui.md`。
