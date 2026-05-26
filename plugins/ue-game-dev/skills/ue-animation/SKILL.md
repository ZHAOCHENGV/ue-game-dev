---
name: ue-animation
description: 当 Unreal Engine 任务涉及 Animation Blueprint、Montage、Blend Space、状态机、IK、Control Rig、骨骼网格、Anim Notify、root motion、Motion Matching、Linked Anim Graph、动画曲线、Pose Snapshot 或动画性能时使用。
---

# UE Animation

## 概览

这个技能负责 UE 动画系统的实现、排查和交接。先确认动画由谁驱动，再把状态机、Montage、IK、通知、曲线和性能验证拆清楚。

## 使用场景

- 设计移动 Blend Space、Locomotion 状态机、跳跃/落地/转身/攻击动画。
- 排查 Animation Blueprint 不更新、Montage 不播放、Notify 不触发、root motion 不生效。
- 集成 Control Rig、IK Retargeter、Motion Matching、Linked Anim Graph 或 Pose Snapshot。
- 优化动画 Tick、骨骼评估、Notify 频率、曲线和 LOD。

## 工作流程

1. 确认动画拥有者：Character、SkeletalMeshComponent、AnimInstance、Ability、StateTree 或 Sequencer。
2. 识别输入变量：速度、加速度、是否在空中、朝向、Gameplay Tag、装备状态和能力状态。
3. 决定动画层次：状态机负责持续状态，Montage 负责短时动作，Notify 负责事件桥接，Control Rig/IK 负责姿态修正。
4. 写清 Blueprint 与 C++ 边界：C++ 提供稳定状态和事件，Anim Blueprint 负责图逻辑和资产组合。
5. 设定验证：Anim Preview、PIE、`showdebug animation`、Montage slot、Notify 日志和性能指标。

## 设计规则

- 不要在 Anim Blueprint Event Graph 中做重业务逻辑或频繁 Cast。
- Montage 播放必须确认 Slot、Section、Blend In/Out、Root Motion Mode 和网络触发方。
- IK 和 Control Rig 先确认骨骼命名、Retarget Pose、LOD 和平台性能预算。
- Root motion 要同时验证 CharacterMovement、Montage、动画资产和网络行为。
- Notify 只做轻量事件分发，复杂效果交给组件、Ability 或 Gameplay Cue。

## 常见问题

- 动画状态不切换：检查变量写入线程、AnimInstance 拥有者和状态机 transition 条件。
- Montage 没效果：检查 Slot 节点、Montage Group、播放返回值和被其他 Montage 打断。
- Notify 不触发：检查触发时机、Montage section、Notify State 生命周期和 dedicated server 行为。
- 移动抖动：检查 root motion、网络平滑、同步组和 Blend Space 采样。

## 输出

- 动画资产与类清单：AnimBP、Blend Space、Montage、Control Rig、IK Rig/Retargeter。
- 图层设计：状态机、Slot、Linked Anim Graph、Notify 和曲线用途。
- 实现步骤：C++ 状态、Blueprint 图、资产设置和验证顺序。
- 验证证据：预览、PIE、调试命令、网络场景和性能检查。

## 参考

- 实现清单读取 `references/animation-checklist.md`。
- 性能和 LOD 问题读取 `references/animation-performance.md`。
