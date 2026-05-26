# 编辑器工具检查清单

## 模块

- Editor 模块与 Runtime 模块分离。
- `.uplugin` Type、LoadingPhase、依赖和平台设置正确。
- Runtime 不依赖 `UnrealEd`、`AssetTools`、Slate editor-only 模块。

## 注册/注销

- StartupModule 注册菜单、命令、Tab、Style、AssetTypeActions。
- ShutdownModule 成对注销。
- 热重载或 Editor 重启后不重复注册。

## UI

- `FUICommandList`、`ToolMenus`、`SDockTab`、`SWidget` 生命周期清楚。
- Slate 不长期强持有易销毁 UObject。
- Details customization 处理多选、空对象和属性变更。

## 资产操作

- 修改资产使用 transaction、dirty 标记和保存提示。
- Factory、Asset Action、Content Browser 操作验证路径和命名冲突。

## 验证

- Editor 启动、禁用插件、热重载、Undo/Redo、资产选择、packaged build 边界。
