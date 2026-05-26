# UE 调试检查清单

## 复现

- 地图、角色、输入、步骤、期望结果、实际结果。
- 是否只在 PIE、Standalone、packaged、多人或特定平台出现。
- 最近改动、首次出现版本、是否稳定复现。

## 证据

- Output Log、callstack、Blueprint breakpoint、C++ breakpoint。
- `stat unit`、`stat game`、`stat net`、`showdebug`、Gameplay Debugger。
- 相关资产路径、类名、配置项和实例默认值。

## 分层

- 输入是否触发。
- Actor/Component 生命周期是否到达。
- 状态是否被写入。
- 事件/delegate 是否绑定。
- 网络 authority/ownership 是否正确。
- UI/动画/渲染反馈是否收到状态。

## 结论

- 已确认事实。
- 已排除假设。
- 仍需验证项。
- 下一步最小修复或进一步分诊技能。
