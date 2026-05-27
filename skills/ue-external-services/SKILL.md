---
name: ue-external-services
description: 当 Unreal Engine 任务涉及 HTTP、REST、JSON、WebSocket 客户端或服务端、TCP socket、后端 API 客户端、流式响应、心跳、重连、请求队列、认证头、异步取消或外部进程/服务集成时使用。
---

# UE External Services

## 概览

这个技能处理 UE 与外部服务通信。它不等同于 UE gameplay replication；HTTP/WebSocket/TCP 是服务通信层，GAS/RPC/复制仍由 `$ue-gas-networking` 处理。

## 使用场景

- 接入 HTTP JSON 接口、登录、配置拉取、排行榜、聊天、支付状态或遥测。
- 实现 WebSocket 长连接、心跳、重连、消息分发和断线恢复。
- 使用 TCP/UDP/外部进程桥接 SDK、工具或本地服务。
- 排查请求超时、JSON 解析、认证、线程回调和 UI 分发问题。

## 工作流程

1. 定义服务边界：协议、URL、认证、请求/响应 schema、超时、重试和错误码。
2. 选择拥有者：GameInstance Subsystem、LocalPlayer Subsystem、World Subsystem、Service UObject 或插件模块。
3. 设计异步结果：delegate、promise、Blueprint async node、队列或状态机。
4. 解析 typed result，避免把裸 JSON 字符串扩散到玩法层。
5. 验证网络失败、重试、取消、地图切换、退出 PIE 和 packaged build。

## 规则

- 不要在 UI Widget 中直接散落 HTTP 请求；用服务层统一管理。
- 回调进入 Gameplay 或 UI 前确认线程、World 和对象生命周期。
- WebSocket 要定义 heartbeat、reconnect backoff、消息版本和关闭原因。
- 认证头、token 和敏感配置不要硬编码进公开源码。
- 外部服务状态与 UE 多人复制要分层，不要把二者混为一个系统。

## 输出

- 服务契约：endpoint、method、headers、schema、错误码。
- UE 结构：Subsystem/Service、请求对象、响应类型、事件分发。
- 失败策略：超时、重试、取消、断线、降级和日志。
- 验证：mock、真实服务、PIE、packaged build 和网络异常。

## 参考

- 服务客户端模式读取 `references/service-client-patterns.md`。
- 需要 HTTP 服务客户端、JSON 解析和 UI 分发模板时读取 `references/http-service-template.md`。
