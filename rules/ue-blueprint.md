# UE Blueprint 规则

## 图表结构

- Event Graph 只保留入口和编排逻辑；复杂流程拆到函数、组件、Subsystem 或 C++。
- 节点链超过一屏时，优先拆函数或加清晰 reroute/comment。
- 不要在多个 Blueprint 重复绑定同一个输入事件；先确认真正拥有输入的是 Pawn、Controller 还是 UI。
- Widget Blueprint 中的 UI 刷新优先事件驱动，不依赖昂贵 Binding 或 Tick。

## 常见 Anti-Pattern

- 每帧 `Cast To`、`Get All Actors Of Class`、查找 Widget 或遍历大数组。
- 深层 Cast 链把 UI、Gameplay、SaveGame、Network 状态绑死。
- 把权威游戏状态存放在 Widget 或临时 Actor 中。
- 用宏隐藏复杂状态机，导致调试和断点困难。
- 事件绑定没有成对解绑，造成重复触发或销毁后回调。

## Blueprint 与 C++ 分工

- Blueprint 适合资产组合、调参、表现、输入连线、Widget 行为和设计师可编辑流程。
- C++ 适合稳定 API、性能敏感逻辑、复杂数据结构、网络权威、异步和跨蓝图复用系统。
- 混合功能先定义 C++ 契约，再说明 Blueprint 默认值、事件、图连线和验证。

## Widget Blueprint

- 避免在 Tick 中拉取 Gameplay 状态；用事件、ViewModel、delegate 或显式刷新。
- 打开/关闭 UI 时成对处理 Input Mode、鼠标显示、焦点恢复和 Mapping Context。
- 列表类 UI 要考虑池化、分页或虚拟化，避免一次创建大量 Widget。
- 玩家可见文本使用 `FText`，本地化路径要在设计阶段明确。

## 验证

- 每次图改动后确认 Blueprint compile 无错误和 warning。
- 验证事件唯一性、Pin 类型、默认值、资产引用和失败路径。
- 对输入、UI、多人和异步回调至少跑一个 PIE 场景。
