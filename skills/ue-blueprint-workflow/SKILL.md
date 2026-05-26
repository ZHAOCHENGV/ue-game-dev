---
name: ue-blueprint-workflow
description: 当 Unreal Engine 请求涉及 Blueprint 图实现、输入事件、函数链、Event Graph、Widget Blueprint、节点/Pin 连线、Blueprint/C++ 集成或蓝图编译验证时使用。
---

# UE Blueprint Workflow

## 概览

这个技能用于蓝图图表级工作。输出应说明节点、Pin、事件流、默认值、资产引用和编译验证，而不是只给 C++ 方案。

## 使用场景

- 连接 Event Graph、Function Graph、Macro、Widget Blueprint、Input Action 或交互事件。
- 排查 Blueprint 不触发、Pin 类型不兼容、Cast 链过深、重复绑定事件或编译错误。
- 设计 Blueprint 与 C++ 的分工边界、可调参数和设计师扩展点。

## 工作流程

1. 确认蓝图类型：Actor、ActorComponent、Widget、AnimBP、GameMode、Controller、Subsystem 派生类或 DataAsset。
2. 找到触发入口：BeginPlay、Input Action、Overlap、Delegate、Timer、UI 回调、Anim Notify 或 Gameplay Event。
3. 写出图流：节点顺序、关键 Pin、分支条件、失败路径和需要的变量。
4. 说明 C++ 交接：`BlueprintCallable`、`BlueprintPure`、`BlueprintImplementableEvent`、`BlueprintAssignable`、`UPROPERTY`。
5. 验证编译、事件唯一性、资产引用、PIE 行为和日志输出。

## 规则

- 不要把长业务流程堆在一个 Event Graph；拆成函数、组件或 C++ API。
- 避免每帧 Cast、循环查找、Widget Tick 绑定和深层宏嵌套。
- UI 刷新优先事件驱动或显式刷新，不依赖昂贵 Binding。
- 输入事件不要在多个蓝图重复绑定，先确认拥有输入的 Pawn/Controller/UI。
- Blueprint 负责组合和调参，复杂状态、性能敏感逻辑和稳定 API 放 C++。

## 输出

- 图表位置：具体 Blueprint、Graph、事件或函数。
- 节点流：按顺序列出节点、Pin、变量和失败分支。
- 资产/默认值：需要创建或设置的 Blueprint、Widget、DataAsset、Input Action。
- 验证：Compile、PIE、日志、断点和回归场景。

## 参考

- 图表质量清单读取 `references/graph-checklist.md`。
- Blueprint/C++ 边界读取 `references/blueprint-cpp-boundary.md`。
