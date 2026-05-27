# Data Asset Patterns

## 选择存储形态

| 需求 | 优先选择 |
|------|----------|
| 设计师编辑的对象记录，并包含资产引用 | `UDataAsset` 或 `UPrimaryDataAsset` |
| 大量同构行 | `UDataTable` |
| 需要插值的数值调参 | `UCurveTable` 或 Curve asset |
| 运行时 registry 与 lookup 集成 | DataRegistry |
| 项目或环境设置 | Config / `UDeveloperSettings` |

## 稳定 ID

- save 和 network reference 使用稳定 row name、Primary Asset ID 或 Gameplay Tag。
- 不要把本地化显示名保存为 ID。
- row、asset 或 tag 重命名时记录迁移。
- 设计师可见文本与 runtime identity 分离。

## 验证清单

- 缺失 row 行为明确。
- Runtime 前能检测重复 ID。
- 资产引用符合期望 class。
- Soft reference 有 cook 覆盖。
- Packaged build 能找到与 Editor PIE 相同的数据。

## 常见陷阱

- 中央 singleton hard-reference 每个 item icon 或 mesh。
- 需要复杂编辑器行为或 per-row 资产继承时仍强用 DataTable。
- 把 mutable runtime state 写进共享 Data Asset。
- 假设 row rename 不影响 save、UI binding 或 backend payload。
