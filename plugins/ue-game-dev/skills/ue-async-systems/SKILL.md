---
name: ue-async-systems
description: 当 Unreal Engine 任务涉及 AsyncTask、Async()、UE::Tasks、FRunnable、FQueuedThreadPool、ParallelFor、Timer、Latent Action、Blueprint async action node、GameThread 回切、取消、生命周期安全或非阻塞客户端/玩法操作时使用。
---

# UE Async Systems

## 概览

这个技能处理 UE 异步与线程边界。核心原则是：离线计算或 IO 可以离开 GameThread，但 UObject 访问、组件修改、广播 Blueprint 事件和大多数 Gameplay 状态写入必须安全回到 GameThread。

## 使用场景

- 实现 `AsyncTask`、`Async()`、`UE::Tasks`、`FRunnable`、`ParallelFor` 或线程池任务。
- 创建 `UBlueprintAsyncActionBase` 节点、Latent Action、Timer 驱动流程。
- 排查后台线程访问 UObject、任务取消、地图切换后回调崩溃、PIE 退出卡住。

## 工作流程

1. 划分工作类型：CPU 计算、磁盘/网络 IO、延迟等待、批量数据处理或 Gameplay 回调。
2. 定义线程边界：哪些数据可复制到后台，哪些必须在 GameThread 读取或写入。
3. 设计生命周期：owner、World、Subsystem、弱引用、取消信号、超时和 PIE/关卡切换。
4. 定义结果交付：GameThread 回切、Delegate、Promise/Future、Blueprint 成功/失败 pin。
5. 给出验证：取消、销毁、失败、重复触发、长耗时和 packaged build 行为。

## 规则

- 后台线程不要直接读写 `UObject`、`AActor`、`UActorComponent` 或 `UWorld` 状态。
- 用值类型快照、线程安全队列或不可变数据把输入传给后台任务。
- 回调前检查弱引用、World 有效性、对象未 pending kill。
- Blueprint async node 必须有明确的激活、完成、失败和取消路径。
- `ParallelFor` 只用于无共享可变状态或有明确同步策略的数据。

## 输出

- 异步模型：选择 `AsyncTask`、`UE::Tasks`、`FRunnable`、Timer、Latent 或 Blueprint async node 的原因。
- 线程边界：后台可做什么、GameThread 做什么。
- 生命周期策略：取消、销毁、地图切换、超时和重复调用。
- 验证方案：单元/PIE/日志/压力场景。

## 参考

- 代码模式和节点结构读取 `references/async-patterns.md`。
