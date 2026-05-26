# UE UI 模式

## 状态分层

- Gameplay 系统拥有权威状态。
- ViewModel、Subsystem 或 Controller 暴露 UI 可读状态。
- Widget 展示状态并发送用户意图，不直接拥有复杂 gameplay 数据。

## 打开与关闭

- 打开 UI 时设置 Input Mode、鼠标显示、焦点默认项和 Mapping Context。
- 关闭 UI 时恢复焦点、输入模式、鼠标显示和上一个界面状态。
- 弹窗和菜单栈要有统一返回逻辑。

## 刷新

- 优先事件驱动、delegate、ViewModel 通知或显式 refresh。
- 避免 Tick 和昂贵 Binding。
- 大列表使用分页、池化或虚拟化。

## 验证

- DPI、窗口尺寸、手柄/键鼠、暂停、加载、多人本地玩家。
