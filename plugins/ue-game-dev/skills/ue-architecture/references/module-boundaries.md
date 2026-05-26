# UE 模块边界

## Runtime / Editor

- Runtime 模块包含 packaged build 需要的 gameplay、data、service、UI runtime 代码。
- Editor 模块包含 Slate、ToolMenus、AssetTools、Details customization、Factories、UnrealEd 依赖。
- Runtime 不得依赖 Editor；Editor 可以依赖 Runtime。
- `.uplugin` 中模块 Type、LoadingPhase 和平台限制要与职责一致。

## Public / Private

- Public 放跨模块 API：类型声明、接口、轻量 struct、必要组件。
- Private 放实现细节、helper、重 include、editor-only implementation。
- Public 头尽量 forward declare，避免把大量引擎头传播给所有依赖者。
- API macro 只用于需要跨模块导出的类型和函数。

## 依赖方向

```text
Editor Tools -> Runtime API -> Core Gameplay/Data
UI -> Gameplay API / ViewModel -> Gameplay State
Services -> Typed DTO / Subsystem -> Gameplay Consumer
```

避免：

```text
Runtime -> Editor
Gameplay -> UI Widget
Core Data -> Feature-specific Actor
Low-level module -> High-level feature module
```

## Blueprint/C++ 边界

- C++ 定义稳定 API、生命周期、authority、replication 和 save/load。
- Blueprint 组合资产、表现、调参和设计师可见流程。
- 跨模块 Blueprint 类型也会形成依赖，不能只看 C++ include。

## 迁移顺序

1. 先定义目标 ownership boundaries。
2. 增加新接口或 adapter，保持旧调用可编译。
3. 移动实现到目标模块。
4. 修复 `.Build.cs` 和 include。
5. 编译、Blueprint compile、PIE 和打包风险验证。
