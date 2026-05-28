# StateTree 检查清单

当任务涉及 StateTree task、condition、evaluator、AI/Gameplay 状态树或 Mass 行为时使用。

## 发现

- 定位 StateTree 资产、schema、owner、运行入口和相关 C++/Blueprint 类型。
- 确认 StateTree 用于 AI、Gameplay 状态、Mass 行为、Smart Object，还是工具/编辑器流程。
- 记录 context data、参数、外部事件、Blackboard/fragment/subsystem 依赖。

## 任务与转换

- 每个 task 说明 Enter、Tick、Exit、完成、失败和取消行为。
- Condition 只判断条件，避免隐藏副作用。
- Evaluator 负责可观测的数据更新，不应悄悄改 gameplay state。
- 转换路径要覆盖成功、失败、超时和中断。

## 集成

- AI 场景记录 Controller、Pawn、NavMesh、感知和 Behavior Tree/StateTree 分工。
- Mass 场景记录 fragment 读写、processor phase 和 StateTree 执行边界。
- Gameplay 场景说明 authority、复制、存档和 UI 通知边界。

## 验证

- 使用 StateTree debugger 或日志确认状态转换。
- 复现每条关键 transition 的触发条件。
- 检查重复进入时 task 数据不会泄漏。
- 多人或 Mass 场景下验证权威端和表现端行为。
