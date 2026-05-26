# GAS 网络检查清单

## 权威

- 谁激活 Ability：client predicted、server only、server initiated。
- ASC owner/avatar 是否正确。
- Replication Mode：Full、Mixed、Minimal 是否适合项目。

## 预测

- 预测输入是否可回滚。
- cost/cooldown 是否在预测和服务器确认间一致。
- 失败原因能否反馈给 owning client。

## 复制

- AttributeSet 字段是否使用 RepNotify。
- Gameplay Cue 是否在目标客户端出现。
- Tag、Effect、Montage 状态是否按预期同步。

## 验证

- Listen Server。
- Dedicated Server。
- 多 PIE。
- 人为延迟或 packet loss。
- late join / respawn / possession change。
