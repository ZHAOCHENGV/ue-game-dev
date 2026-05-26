# UE 测试清单

## 测试层级

- C++ 小逻辑：AutomationSpec 或 `FAutomationTestBase`。
- Gameplay 流程：Functional Test、PIE 场景或自动化地图。
- Blueprint/资产：编译、引用、默认值、PIE 行为。
- 编辑器工具：注册、菜单、Tab、Undo/Redo、禁用插件。
- 网络：Listen/Dedicated、多 PIE、authority、replication、RPC。
- 打包：Cook、packaged build smoke、平台配置。

## 选择原则

- 风险高、共享逻辑、容易回归的代码优先自动化。
- 资产和 UI 改动至少要有手工/PIE 验证路径。
- 多人和异步功能要覆盖失败、取消、延迟和 owner 销毁。
- 无法自动化时写清手工步骤和证据。

## Automation 命令要素

- 项目路径。
- Test filter。
- NullRHI 或真实渲染需求。
- 日志输出位置。
- 失败时如何定位首个错误。

## 证据

- 记录命令、场景、结果、日志路径和截图/视频（如适用）。
- 未运行的验证必须写“未验证”和原因。
- 结论使用 `PASS`、`CONCERNS` 或 `FAIL`。

## 回归矩阵

- 新档/旧档、Editor/PIE/Standalone/packaged、单人/多人、键鼠/手柄、目标平台。
