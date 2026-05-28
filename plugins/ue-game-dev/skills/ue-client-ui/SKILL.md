---
name: ue-client-ui
description: 当 Unreal Engine 任务涉及 UMG、Widget Blueprint、CommonUI、HUD、菜单、ViewModel、输入焦点、Enhanced Input UI 流程、加载界面、本地化、无障碍、DPI/布局或 UI 性能时使用。
---

# UE Client UI

## 概览

这个技能负责 UE 客户端 UI。先确认 UI 层级、状态来源、输入焦点和刷新方式，再设计 Widget、CommonUI、ViewModel、HUD 或菜单流程。

## 使用场景

- 设计背包、HUD、主菜单、设置面板、加载界面、提示框或交互提示。
- 排查按钮不响应、焦点丢失、手柄导航异常、DPI 适配、Widget Tick 性能。
- 集成 CommonUI、Enhanced Input、MVVM/ViewModel、本地化和 UI 音效。

## 工作流程

1. 确认 UI 拥有者：PlayerController、HUD、LocalPlayer Subsystem、GameInstance Subsystem 或 Widget。
2. 定义状态来源：Gameplay 组件、SaveGame、ViewModel、DataAsset、Async service 或 replicated state。
3. 设计 Widget 层级：根容器、弹窗、导航栈、输入模式、焦点默认项和关闭路径。
4. 确定刷新方式：事件驱动、ViewModel 通知、显式刷新或低频 Timer。
5. 验证 DPI、窗口尺寸、手柄/键鼠、暂停、加载、多人本地玩家和 packaged build。

## 规则

- UI 不应直接拥有复杂 Gameplay 状态；它读取或订阅状态并发出用户意图。
- 避免 Tick 和昂贵 Binding；大列表使用池化、分页或虚拟化策略。
- 输入模式、鼠标显示、焦点恢复和 CommonUI action routing 必须成对处理。
- UI 与 Enhanced Input 冲突时，先明确当前 Input Mode 和 Mapping Context 优先级。
- 本地化文本使用 `FText`，不要把玩家可见文本写成 `FString` 常量。

## 输出

- UI 架构：Widget、HUD、Controller、Subsystem、ViewModel 分工。
- 交互流：打开、刷新、确认、取消、关闭、焦点恢复。
- 资产与代码：WBP、DataAsset、Style、Input Action、C++ 类。
- 验证：DPI、手柄/键鼠、PIE、packaged build 和性能观察。

## 参考

- Runtime UI API 准确性读取 `references/ui-api-accuracy.md`。
- UI 模式读取 `references/ui-patterns.md`。
- 代码模板读取 `references/ui-code-templates.md`。
