# GAS 模式

## ASC 位置

- PlayerState：适合角色切换、重生后状态保留的多人项目。
- Pawn/Character：适合简单项目或能力完全绑定当前 Pawn。
- 组件封装：适合项目已有 gameplay 组件结构。

## Ability 生命周期

- 输入触发。
- `CanActivateAbility` 检查 tag、cost、cooldown、authority。
- `CommitAbility` 提交 cost/cooldown。
- Ability Task 等待事件、montage、target data 或延迟。
- `EndAbility` / cancel 清理任务和状态。

## Effect 与 Attribute

- 持久属性变化用 GameplayEffect。
- 临时 buff/debuff 用 duration/infinite GE。
- UI 读取 Attribute change delegate，不直接轮询。

## Gameplay Cue

- 用于视觉、音频和表现。
- 不承载权威 gameplay 逻辑。
- Cue 参数要足够表达表现，但不要塞大量状态。
