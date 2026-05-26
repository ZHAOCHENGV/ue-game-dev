# UE 外部服务客户端模式

## 服务层结构

推荐把 HTTP/WebSocket/TCP 集成放在 Subsystem 或 service UObject 中，而不是散落到 Widget 或 Actor。

```text
GameInstanceSubsystem / LocalPlayerSubsystem
  -> Request builder
  -> Transport client (HTTP/WebSocket/TCP)
  -> Typed response parser
  -> Delegate / async node / event queue
  -> Gameplay or UI consumer
```

## HTTP JSON

- endpoint、method、headers、body schema 和 response schema 要写清楚。
- 响应解析成 typed struct，不把裸 JSON 字符串扩散到 UI/Gameplay。
- 设置 timeout、retry、错误码映射和日志 request id。
- 认证 token 从安全配置或运行时登录结果取得，不硬编码在源码中。

## WebSocket

- 定义连接状态：Disconnected、Connecting、Connected、Reconnecting、Closing。
- 心跳要有 interval、timeout、missed count 和关闭策略。
- 重连使用 backoff，避免断线后高频重连。
- 消息要包含 type/version/request id，便于向后兼容和分发。

## TCP/外部进程

- 明确二进制协议或文本协议、分包、粘包和编码。
- worker thread 只处理 socket IO 和字节解析，Gameplay 回调回到 GameThread。
- 外部进程路径、权限、端口占用和生命周期要可诊断。
- 退出 PIE 和 Editor 时关闭 socket/进程，避免残留连接。

## Blueprint Async Node

- 对用户操作型请求可提供 `UBlueprintAsyncActionBase`。
- 输出 Success、Failure、Timeout、Cancelled，并包含错误码和错误文本。
- 节点不应长期持有 UI Widget；用弱引用和 owner 生命周期管理。

## 验证

- 成功响应、4xx/5xx、超时、断网、坏 JSON、认证过期、重复请求。
- 地图切换、PIE 停止、退出 Editor、packaged build。
- 如果结果驱动 UI，验证焦点、刷新和失败提示。
