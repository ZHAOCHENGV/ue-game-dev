# Runtime UI API 准确性备注

编写或审查 UMG、CommonUI、MVVM、HUD 或 runtime Slate 建议时使用本参考。

## UMG 与 Widget 生命周期

- `UUserWidget` 初始化通常放在 `NativeOnInitialized`、`NativeConstruct`、`NativeDestruct`，并按生命周期绑定/解绑事件。
- 可事件驱动时，避免昂贵的 Blueprint per-frame binding 和 widget `Tick`。
- 玩家可见文本使用 `FText`，保留本地化能力。
- 被动显示 widget 不应直接修改 gameplay 状态，除非项目明确采用 command widget 模式。

## CommonUI

- 尊重 activatable widget stack、input action、back handling、focus 和平台提示。
- UI 状态所有权优先归 local player/controller/subsystem，不要用全局单例乱管本地用户。
- 焦点变化时同时验证键鼠与手柄流程。

## MVVM 与 ViewModel

- 复制/gameplay 状态保留在 gameplay system，通过 view model 或 UI state object 暴露适合展示的值。
- Widget 监听 gameplay system 时，必须记录 delegate/event 订阅和 teardown。
- 多人项目区分本地预测 UI 与服务器确认状态。

## Slate 边界

- 项目已有 runtime Slate 时可以使用；编辑器面板、Details 自定义、Tab Spawner、ToolMenus 和 UICommands 归 `$ue-editor-tooling-slate`。

## 证据

- 至少检查一个窄视口和一个宽视口或 DPI scale。
- 菜单或 CommonUI 屏幕变化必须包含焦点/导航验证。
