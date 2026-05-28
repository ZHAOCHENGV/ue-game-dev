---
name: ue-character-movement
description: 当 Unreal Engine 请求涉及 CharacterMovementComponent、角色移动、Custom Movement Mode、移动复制、网络预测、client prediction、server correction、root motion、locomotion 或移动 Bug 调试时使用。
---

# UE Character Movement

这个技能处理 `CharacterMovementComponent`、角色移动调参、自定义移动模式和网络预测。重点是把输入、模拟、动画、复制和修正证据放在同一条链上。

## 工作流程

1. 读取 Character/Pawn、MovementComponent、Controller 输入绑定、Animation Blueprint、Ability hook 和移动配置。
2. 判断移动来源：玩家输入、CharacterMovement 模拟、root motion、launch/impulse、ability task、physics，还是手写 transform。
3. 梳理移动状态：movement mode、custom mode、速度/加速度、base actor、floor check、collision 和 capsule 设置。
4. 多人项目必须记录 local role、autonomous proxy、simulated proxy、server correction 和 smoothing 行为。
5. 定义验证：本地手感、两客户端修正、动画/root motion 同步、碰撞边界和 packaged runtime。

## 设计规则

- 不要混用手动 `SetActorLocation` 和 CharacterMovement 模拟，除非明确同步和预测方案。
- 自定义移动模式要定义进入/退出条件、physics update、网络序列化和动画状态交接。
- 移动参数调优前先确认 capsule、floor、slope、step height、braking、gravity 和 collision profile。
- root motion、GAS ability task 和 CharacterMovement 的 authority 要明确，避免多个系统争夺最终位移。
- 网络可见移动必须用两客户端验证 correction、jitter、teleport、base actor 和 movement mode 切换。

## 跨域交接

- Animation Blueprint、Blend Space、Montage、root motion 姿态进入 `$ue-animation`。
- GAS ability 引发的移动、prediction key 或 ability task 进入 `$ue-gas-networking`。
- 输入绑定和重绑进入 `$ue-input-enhanced`。
- 行为异常复现和证据收集可进入 `$ue-debug-validation`。

## 参考

- 调整 `CharacterMovementComponent`、自定义移动模式或网络预测前读取 `references/character-movement-checklist.md`。
