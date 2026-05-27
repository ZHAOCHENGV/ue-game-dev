# Async Loading 检查清单

## 引用策略

- 必须随 owner 常驻加载的资产使用 hard reference。
- 可选、大型、装饰性或模式专属资产使用 soft reference 或 Primary Asset ID。
- 一个功能作为整体加载时，把相关 soft references 归入 Asset Manager bundle。
- 只被 soft path 发现的资产必须检查 Primary Asset Rules、chunk ID 和 cook rules。

## 加载流程

1. 验证请求的 ID、row handle、soft object path 或 Primary Asset ID。
2. 通过 Asset Manager 或 `FStreamableManager` 开始异步加载。
3. 根据 owner lifetime 保存或取消 handle。
4. completion callback 中检查 UObject 有效性和失败路径。
5. 在 GameThread 应用结果，并广播窄 success/failure 事件。

## 失败模式

- 资产没有 Cook 进包。
- 资产 class 不匹配。
- owner 在 callback 前销毁。
- 重复并发请求竞争同一个 cache。
- save data 指向已重命名 row 或 asset。

## 验证

- 对 soft-reference discovery 测试 Editor PIE、standalone 和 packaged build。
- 包含缺失 asset/row 场景。
- 对首次加载 hitch 做 profiling，必要时在模式边界 preload。
