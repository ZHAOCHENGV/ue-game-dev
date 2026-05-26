# Blueprint 图检查清单

## 图结构

- Event Graph 入口清晰，不承载超长业务逻辑。
- 函数名、变量名和 comment 表达意图。
- 节点链过长时拆函数或组件。
- 避免深层宏和隐藏副作用。

## 输入和事件

- 输入事件只在拥有输入的 Pawn/Controller/UI 中绑定。
- Delegate 绑定和解绑成对。
- Timer、Delay、Async 回调在 owner 销毁后安全。

## 性能

- 避免 Tick 中 Cast、Get All Actors、创建 Widget、遍历大数组。
- UI Binding 谨慎使用，优先事件刷新。
- 大量 Actor/Widget 使用池化或降频。

## 验证

- Blueprint compile 无错误。
- Pin 类型兼容。
- 默认值和实例覆写正确。
- PIE 覆盖成功、失败和重复触发。
