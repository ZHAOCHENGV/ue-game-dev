---
name: ue-state-trees
description: 当 Unreal Engine 请求涉及 StateTree、StateTreeTask、StateTreeCondition、StateTreeEvaluator、AI/Gameplay 状态树、层级状态、Mass/Smart Object 行为或状态转换调试时使用。
---

# UE State Trees

这个技能处理 UE StateTree 工作流。重点是把状态层级、任务生命周期、条件/evaluator 数据、AI 或 Mass 集成和调试证据放在一起。

## 工作流程

1. 读取 StateTree 资产、schema、绑定的 AI/Mass/Gameplay 入口、相关 Blackboard/Controller/Subsystem 和模块依赖。
2. 判断用途：AI 行为、Gameplay 状态、Mass 行为、Smart Object 流程，还是传统状态机替代。
3. 梳理数据流：参数、context data、evaluator、condition、task、transition 和外部事件。
4. 确认任务生命周期：Enter、Tick、Exit、完成/失败、取消，以及重复进入时的数据清理。
5. 定义验证：状态转换路径、条件命中、任务返回值、调试视图、多人 authority 和性能。

## 设计规则

- StateTree 适合层级状态和数据驱动行为，不要把复杂长期系统状态全塞进单个 task。
- Task 只拥有自己的短生命周期行为，长期状态放在 owner、subsystem、fragment 或 Blackboard 等明确位置。
- Evaluator/condition 应保持可观测，避免隐藏副作用。
- 转换条件要可解释，优先记录失败路径而不只是成功路径。
- 与 Mass 集成时，明确 fragment 数据读写和 processor/StateTree 的职责分界。

## 跨域交接

- Behavior Tree、NavMesh、EQS、AI Perception 仍进入 `$ue-ai-navigation`。
- Mass processor、fragment、crowd representation 进入 `$ue-mass-entity`。
- 需要 C++ task/evaluator 或 Gameplay bridge 时进入 `$ue-cpp-gameplay`。
- 行为异常或状态不跳转时可进入 `$ue-debug-validation` 收集证据。

## 参考

- 添加 StateTree task、condition、evaluator 或状态转换前读取 `references/state-tree-checklist.md`。
