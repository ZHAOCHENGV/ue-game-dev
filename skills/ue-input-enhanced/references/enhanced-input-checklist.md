# Enhanced Input 检查清单

## 资产

- `IA_` 命名清晰，Value Type 与用途一致：Boolean、Axis1D、Axis2D、Axis3D。
- `IMC_` 按模式组织：Gameplay、Vehicle、Menu、Debug、PhotoMode 等。
- Modifier 和 Trigger 必须有明确目的，避免叠加后难以解释。
- 默认键位、手柄、鼠标、触屏和平台差异要记录。

## 添加 Mapping Context

- 通过 `ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>()` 添加/移除。
- 添加时记录 priority，UI、菜单、Debug、Gameplay 的优先级要明确。
- Pawn possession、respawn、map travel、local multiplayer 都要重新确认 context。
- 不要在多个地方重复添加同一个 context 而不移除。

## 绑定

- 在 `SetupPlayerInputComponent` 或项目约定位置绑定。
- 确认 `EnhancedInputComponent` cast 成功。
- `BindAction` 的 trigger event 要符合行为：Started、Triggered、Completed、Canceled。
- 函数签名与 `FInputActionValue` 或具体输入值匹配。

## 输入不触发排查

- Pawn 是否被正确 Possess。
- PlayerController 是否有 LocalPlayer。
- Mapping Context 是否已添加且 priority 正确。
- UI 是否抢焦点或 Input Mode 阻断。
- Trigger 条件是否满足，Value Type 是否匹配。
- 输入设备是否映射到当前平台。

## 验证

- PIE 单人、多 PIE、本地多人、手柄/键鼠切换、暂停/恢复、UI 打开/关闭。
- 使用 `showdebug enhancedinput` 或项目可用日志观察 action 状态。
