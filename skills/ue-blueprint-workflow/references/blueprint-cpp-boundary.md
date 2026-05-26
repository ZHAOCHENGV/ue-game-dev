# Blueprint / C++ 边界

## C++ 适合拥有

- 稳定运行时 API。
- 权威 gameplay 状态。
- Replication、RPC、prediction。
- Save/load schema 和迁移。
- 性能敏感循环、复杂数据结构、异步和线程边界。
- 多个 Blueprint 复用的组件、Subsystem 和接口。

## Blueprint 适合拥有

- 设计师调参和默认资产。
- 视觉、音频、UI、动画、Timeline 等表现逻辑。
- 简单事件响应和图级编排。
- Widget Blueprint、Anim Blueprint 和关卡特定组合。

## 交接格式

```text
C++ provides:
- Function/event/property:
- Inputs:
- Outputs:
- Failure behavior:

Blueprint implements:
- Asset:
- Graph:
- Nodes:
- Defaults:
- Validation:
```

## 边界案例

- 如果 Blueprint 需要改权威状态，优先提供 C++ command，而不是暴露可写字段。
- 如果 C++ 需要触发表现，优先提供 BlueprintImplementableEvent 或 delegate。
- 如果 UI 需要 gameplay 数据，使用 ViewModel、Subsystem 或只读 API。
- 如果逻辑每帧运行或会复制到多人，优先考虑 C++。
