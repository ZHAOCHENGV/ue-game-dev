# UE 项目接手审查清单

## 项目入口

- 找到 `.uproject`，记录项目名、EngineAssociation、模块和启用插件。
- 读取 `Source/`、`Plugins/`、`Config/`、target 文件和 `.Build.cs`。
- 标记目标平台、默认地图、GameMode、输入系统和核心插件。

## 源码结构

- 按模块列出 Public/Private、Runtime/Editor、Subsystem、Actor、Component、UI、Service。
- 检查明显循环依赖、Editor 依赖泄漏、Public 头过重和命名不一致。
- 找出主要 gameplay、UI、input、save、network、AI、animation、render/VFX 系统。

## 资产与内容

- 只能基于文件名和路径推断 `.uasset` 内容，避免把推断写成事实。
- 记录 Blueprint、Widget、Input Action、Mapping Context、DataAsset、Niagara、Material、Map。
- 检查命名前缀、目录归属、可能的 redirector 或缺失资产风险。

## 配置与构建

- 读取 `DefaultGame.ini`、`DefaultEngine.ini`、`DefaultInput.ini` 和平台配置。
- 检查插件启用、地图设置、packaging settings、Online/Network、input settings。
- 记录可用测试、CI、脚本、README 和最近日志。

## 输出重点

- 项目地图，不是文件清单堆砌。
- 已确认事实与推断分开。
- 给后续二开最有价值的风险、约定和下一步技能。
