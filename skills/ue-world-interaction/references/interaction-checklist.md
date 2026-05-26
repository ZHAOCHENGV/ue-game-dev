# 世界交互检查清单

## 检测方式

- Line Trace：准星、视线、点击、短距离精确交互。
- Sphere/Box Overlap：范围感知、持续提示、拾取物附近检测。
- Interface scan：目标对象实现 `IInteractable` 或组件契约。
- Gameplay Tag：过滤类型、状态、阵营或交互条件。

## 交互契约

- 定义 `CanInteract`、`GetInteractionPrompt`、`Interact`、`OnFocusBegin/End`。
- 返回失败原因，便于 UI 和日志解释。
- 交互输入、检测、提示和执行不要全部堆在 Widget 里。
- 复杂交互放组件或系统，Actor 只提供目标状态。

## 反馈

- UI prompt、outline、高亮、音效、Niagara、动画和震动反馈要有 owner。
- 焦点切换时清理旧目标反馈。
- 失败反馈与成功反馈区分，避免玩家误以为已执行。

## 网络与存档

- 客户端可预测提示，核心结果由服务器确认。
- 拾取、开门、生成、销毁等状态要考虑 replication 和 late join。
- 需要持久化的世界状态使用稳定 ID，不保存临时 Actor 指针。

## 验证

- 距离边界、遮挡、多目标优先级、目标销毁、输入连按、多人、地图切换。
