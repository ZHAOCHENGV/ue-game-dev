# UE Animation 检查清单

## 输入变量

- 速度、加速度、方向、是否在空中、是否瞄准、装备状态、Gameplay Tag。
- 变量写入位置：Character、Movement Component、AnimInstance、Ability 或 StateTree。
- 确认变量在 Preview、PIE、多人和 dedicated server 下的来源。

## 状态机

- Locomotion、Jump、Land、Combat、HitReact、Dead 等状态边界清楚。
- Transition 条件可解释，避免多个状态互相抢切。
- Blend time、sync group、additive、pose cache 和 state alias 要按需求使用。

## Montage

- 确认 Slot、Group、Section、Blend In/Out、Root Motion、Play Rate。
- 处理 Montage interrupted、completed、blend out 和 cancel。
- 多人下确认由 server、owning client 还是 simulated proxy 触发。

## Notify 与曲线

- Notify 用于轻量事件桥接，不放重业务逻辑。
- Notify State 要处理 begin/end 中断。
- 曲线命名要稳定，例如 `FootIKAlpha`、`AimOffsetYaw`、`DamageWindow`。

## IK / Control Rig

- 检查骨骼命名、retarget pose、IK Rig、Control Rig、LOD 和平台预算。
- Foot IK、hand IK、look at、aim offset 要和动画层顺序一致。

## 验证

- Anim Preview、PIE、`showdebug animation`、Montage slot、Notify 日志。
- 检查 root motion、网络平滑、LOD、性能和 packaged build 差异。
