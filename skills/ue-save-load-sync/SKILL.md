---
name: ue-save-load-sync
description: 当 Unreal Engine 任务涉及 SaveGame schema、序列化、恢复管线、持久 ID、版本迁移、replicated runtime state、RepNotify、RPC 入口点、云存档或本地/网络状态同步时使用。
---

# UE Save Load Sync

## 概览

这个技能负责存档、加载和持久状态同步。先区分“可持久化状态”和“运行时复制状态”，再设计 schema、版本迁移、恢复顺序和网络边界。

## 使用场景

- 实现 `USaveGame`、自定义 `FArchive`、配置存档、云存档或本地存档。
- 排查加载后状态缺失、Actor 重复生成、版本不兼容、RepNotify 覆盖存档值。
- 设计持久 ID、资产引用、关卡切换、多人会话中的保存时机。

## 工作流程

1. 列出需要持久化的数据：玩家、背包、任务、世界 Actor、设置、运行时生成对象。
2. 定义 schema：结构体、版本号、持久 ID、软引用、默认值和迁移策略。
3. 设计保存/加载时机：checkpoint、手动保存、地图切换、退出、云同步。
4. 区分网络状态：server authority、replicated runtime state、RPC 触发和客户端表现。
5. 验证新档、旧档、坏档、缺资产、多人、关卡切换和 packaged build。

## 规则

- 存档不要直接保存临时 Actor 指针；使用稳定 ID、软引用或可重建数据。
- schema 需要版本号和迁移路径。
- 加载顺序必须处理依赖：Subsystem、GameInstance、World、PlayerState、Actor、UI。
- 多人游戏通常由服务器决定权威持久状态。
- 云同步要定义冲突解决、离线行为和失败回退。

## 输出

- 数据模型：保存字段、版本、ID、引用和默认值。
- 流程：保存、加载、迁移、恢复、网络同步。
- Blueprint/C++ 边界：API、事件、错误处理和 UI 通知。
- 验证：新旧档、损坏档、多 PIE、关卡切换和 packaged build。

## 参考

- 存档清单读取 `references/save-load-sync-checklist.md`。
- 模板读取 `references/save-load-templates.md`。
