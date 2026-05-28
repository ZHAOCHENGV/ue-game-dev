# Character Movement 检查清单

当任务涉及 `CharacterMovementComponent` 调参、自定义移动模式、网络预测、root motion 或移动 Bug 时使用。

## 发现

- 定位 Character 类、MovementComponent 类、Controller 输入绑定、Animation Blueprint、Ability hook 和移动配置值。
- 检查 capsule size、collision profile、floor check、step height、slope limit、braking、acceleration、gravity 和 movement mode transition。
- 判断位移来自输入、CharacterMovement 模拟、root motion、launch/impulse、ability task、physics，还是手动 transform。

## 网络

- 确认 local role、owner、autonomous proxy、simulated proxy 和 server correction 行为。
- 移动影响 gameplay 时，用至少两个客户端复现。
- 记录 velocity、acceleration、movement mode、base actor、root motion state 和 correction events。

## 自定义移动

- 定义进入和退出条件。
- Physics update 要尽量适合 prediction。
- 避免和 CharacterMovement 未同步地混用手动 transform。
- 给动画状态机提供 custom mode 的交接信号。

## 证据

- 本地 PIE 手感检查。
- 两客户端 correction、smoothing 或 jitter 检查。
- 动画/root motion 同步说明。
- 碰撞、坡度、台阶和 base actor 边界验证。
