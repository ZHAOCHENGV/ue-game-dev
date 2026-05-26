# 按键重绑与 UI

## 重绑流程

1. 列出可重绑的 `Input Action` 和默认键位。
2. 打开重绑 UI 时切换到合适 Input Mode，并设置焦点。
3. 捕获下一次键/轴输入，过滤 Escape、鼠标移动、保留键和平台不可用键。
4. 检查冲突：同组 action、同设备、同 context。
5. 保存用户映射，应用到 Enhanced Input Subsystem。
6. 提供恢复默认和取消操作。

## UI 焦点

- 打开菜单时记录之前焦点和 gameplay mapping context。
- 关闭菜单时恢复输入模式、鼠标显示、焦点和 context。
- CommonUI 项目要确认 action routing 和 back handler。
- 本地多人要按 LocalPlayer 保存焦点和映射。

## 保存

- 键位设置可放 SaveGame、GameUserSettings 扩展或项目已有设置系统。
- 保存内容包括 action、key、slot、device、context 和版本号。
- 加载失败或版本不匹配时回退默认值。

## 验证

- 键鼠、手柄、冲突、取消、恢复默认、重启游戏、不同玩家。
- UI 打开时 gameplay 不误触发，关闭后 gameplay 输入恢复。
