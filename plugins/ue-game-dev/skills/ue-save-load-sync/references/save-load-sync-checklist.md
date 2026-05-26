# 存档与同步检查清单

## 数据

- 需要持久化的字段。
- 不应持久化的运行时临时状态。
- 稳定 ID。
- 资产 soft reference。
- schema version。

## 流程

- 保存时机。
- 加载时机。
- 迁移。
- 恢复顺序。
- 失败回退。

## 网络

- server authority。
- replicated runtime state。
- RPC 触发。
- RepNotify 与加载值的顺序。
- late join。

## 验证

- 新档。
- 旧档。
- 损坏档。
- 缺资产。
- 地图切换。
- 多 PIE。
