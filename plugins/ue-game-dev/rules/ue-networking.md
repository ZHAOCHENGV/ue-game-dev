# UE Networking 规则

## 权威与所有权

- 先回答“哪台机器拥有状态”：server、owning client、simulated proxy 或 standalone。
- Gameplay-critical 状态默认由服务器权威修改，客户端只发意图或做可回滚预测。
- RPC 前确认 Actor ownership、relevance、lifetime 和调用方向。
- RepNotify 只处理状态到达后的反应，不应隐藏核心业务决策。

## Replication

- `DOREPLIFETIME` 必须与 `UPROPERTY(Replicated)` 或 `ReplicatedUsing` 配套。
- 不要复制高频、可推导或纯表现数据；复制最小状态，客户端本地表现。
- 大数组或频繁变化集合优先考虑 Fast Array Serializer、差量事件或服务器查询。
- 新增复制字段后验证 initial replication、late join、reconnect 和 actor dormancy。

## RPC

- RPC 参数保持小而稳定，避免传大 struct、资产对象或频繁逐帧调用。
- `Server` RPC 需要验证输入合法性；不要信任客户端提交的结果。
- `NetMulticast` 只用于确实需要广播的短表现事件，不替代状态复制。
- 可靠 RPC 不是“更好”，大量 reliable 会造成队列堆积。

## GAS 与多人

- GAS 任务使用 ASC replication mode、prediction key、Gameplay Cue 和 Ability Task 生命周期来表达同步。
- 属性变化走 GameplayEffect/AttributeSet，不要绕过 GAS 直接写 replicated 字段。
- Ability 激活失败要能区分 tag 阻塞、cooldown、cost、authority 或 prediction rollback。

## 验证

- 至少说明 Listen Server、Dedicated Server 或多 PIE 的最小测试场景。
- 检查 server/client 日志、ownership、authority、relevance、packet loss/latency。
- 明确 Editor PIE 与 packaged multiplayer 的差异风险。
