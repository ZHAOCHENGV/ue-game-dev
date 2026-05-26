---
name: ue-plugin-module-dev
description: 当 Unreal Engine 任务涉及 .uplugin、.uproject 模块描述、Runtime/Editor/Developer 模块拆分、ModuleRules、.Build.cs、Public/Private 边界、export API macro、插件内容/配置/资源、第三方库封装或 UE 命名规范时使用。
---

# UE Plugin Module Dev

## 概览

这个技能负责 UE 插件和模块开发。重点是模块类型、依赖方向、Public/Private、API macro、编辑器边界、资源和第三方库封装。

## 使用场景

- 创建 Runtime + Editor 双模块插件。
- 调整 `.uplugin`、`.uproject`、`.Build.cs`、LoadingPhase、EnabledByDefault。
- 封装第三方 C++ SDK、DLL、静态库或平台库。
- 排查模块加载、符号导出、编辑器依赖泄漏、打包失败。

## 工作流程

1. 读取现有 `.uplugin`、`.uproject`、模块目录、`.Build.cs` 和 target 文件。
2. 选择模块类型：Runtime、Editor、Developer、ThirdParty、Program。
3. 设计依赖：Public/PrivateDependencyModuleNames、IncludePath、平台条件和 Editor-only 分支。
4. 设置 API macro、Public/Private 头、资源目录、Content、Config 和命名。
5. 验证 Editor 构建、Runtime 构建、插件启停、packaged build 和平台库部署。

## 规则

- Runtime 模块不能依赖 Editor 模块。
- Public 头只暴露跨模块 API；内部实现放 Private。
- 所有跨模块类型使用正确 `MODULE_API` macro。
- 第三方库封装要区分 include、lib、dll、delay-load、runtime dependencies 和许可证。
- 资产与代码命名遵循 UE 约定，避免和项目已有前缀冲突。

## 输出

- 插件/模块结构：目录、模块类型、依赖方向。
- `.uplugin` 和 `.Build.cs` 修改点。
- Public API、Private 实现和 Blueprint 暴露策略。
- 验证：编译、Editor 启动、插件禁用、packaged build 和平台库加载。

## 参考

- 模块清单读取 `references/plugin-module-checklist.md`。
- 命名规范读取 `references/ue-naming-conventions.md`。
- C++ 规范读取 `references/ue-cpp-coding-standard.md`。
- 第三方库封装读取 `references/third-party-library-wrapper.md`。
