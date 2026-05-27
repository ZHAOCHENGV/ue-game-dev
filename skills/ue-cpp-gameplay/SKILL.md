---
name: ue-cpp-gameplay
description: 当 Unreal Engine 任务涉及 Actor、ActorComponent、UObject、DataAsset、Subsystem、输入、交互、生成、背包、战斗、Blueprint 暴露 API、存档/加载集成或 Game Feature C++ 玩法系统时使用。
---

# UE C++ Gameplay

## 概览

这个技能负责 UE C++ 玩法实现。先确认生命周期、所有权、反射暴露、Blueprint 接口和验证路径，再改代码。

## 使用场景

- 创建 Actor、Component、Subsystem、DataAsset、UObject 或 Gameplay 系统。
- 把 C++ API 暴露给 Blueprint，或整理蓝图接法。
- 实现输入、交互、生成、背包、战斗、存档 hook、运行时配置。
- 排查 UHT、反射、GC、生命周期、PIE 或 packaged runtime 问题。

## 工作流程

1. 读取 `.uproject`、模块 `.Build.cs`、最近相似类和命名约定。
2. 选择类型：`AActor`、`UActorComponent`、`UObject`、`UDataAsset`、`UGameInstanceSubsystem`、`UWorldSubsystem` 等。
3. 设计所有权：Outer、spawn/construct、GC 可见性、replication、save/load 和销毁路径。
4. 设计 Blueprint API：`UFUNCTION`、`UPROPERTY`、Category、默认值、事件和错误返回。
5. 验证：编译、UHT、Blueprint compile、PIE、日志和自动化测试。

## 规则

- `UObject` 引用要通过 `UPROPERTY`、`TObjectPtr`、弱引用或明确生命周期管理保持 GC 安全。
- Public 头文件保持最小包含，优先 forward declaration。
- `BlueprintReadWrite` 不应滥用，外部可写状态要有约束或 setter。
- 运行时逻辑不要依赖 Editor-only 模块或资产。
- 网络、存档、UI、异步等跨域需求要明确交接技能。

## 工具

- 当需要扫描 C++ 暴露给 Blueprint 的 API 时，可使用只读脚本 `skills/ue-cpp-gameplay/scripts/ue_blueprint_api_report.py`。
- 工具只读取源码并报告 `BlueprintCallable`、`BlueprintPure`、事件和可绑定属性，不编辑项目。

## 输出

- 类/模块设计：文件路径、继承、职责和生命周期。
- 反射接口：`UCLASS`、`USTRUCT`、`UFUNCTION`、`UPROPERTY` 设计。
- Blueprint 接法：节点、Pin、默认值、事件和失败路径。
- 验证：构建命令、PIE 场景、日志和回归点。

## 参考

- C++ 模式读取 `references/cpp-patterns.md`。
- 需要选择或草拟 `UGameInstanceSubsystem`、`UWorldSubsystem` 时读取 `references/subsystem-template.md`。
- Blueprint API 读取 `references/blueprint-api.md`。
- 验证步骤读取 `references/validation.md`。
