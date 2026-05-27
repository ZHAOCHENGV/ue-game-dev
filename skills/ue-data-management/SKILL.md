---
name: ue-data-management
description: 当 Unreal Engine 请求涉及 Primary Asset Manager、Data Asset、DataTable、CurveTable、DataRegistry、软/硬引用、FStreamableManager 异步加载、Primary Asset Rules、Cook Chunk、玩法数据建模或资产加载策略时使用。
---

# UE Data Management

这个技能处理玩法数据模型、资产引用策略、异步加载和 Cook 感知的资产组织。目标是同时照顾设计师编辑、运行时加载成本、存档兼容和打包规则。

## 工作流程

1. 判断数据形态：Data Asset、Primary Data Asset、DataTable、CurveTable、Config、Gameplay Tags、DataRegistry 或后端数据。
2. 定位拥有者：谁创建、加载、缓存、修改、保存、复制或展示这些数据。
3. 决定引用策略：hard reference、soft reference、Primary Asset ID、row handle、Gameplay Tag 或 config key。
4. 引入新引用前检查 Cook 规则、chunk、Asset Manager 设置和异步加载路径。
5. 定义验证：Editor 数据审计、缺失 row、异步加载失败、packaged build 访问和版本迁移。

## 数据建模规则

- 记录像对象、有资产引用、需要设计师编辑时，优先 Data Asset。
- 大量同构行并需要 CSV/JSON 导入导出时，优先 DataTable。
- 数值曲线和平衡数据使用 CurveTable 或 Curve asset。
- Config 用于环境或项目设置，不用于大型玩法目录。
- Gameplay Tag 用于稳定语义 ID，避免字符串驱动分类逻辑。

## 资产加载规则

- 只有确实随 owner 常驻加载时才用 hard reference。
- 可选、大型、装饰性或模式专属资产使用 `TSoftObjectPtr`、`TSoftClassPtr`、`FSoftObjectPath` 或 Primary Asset ID。
- soft reference 通过 `FStreamableManager` 或 Asset Manager 加载，并处理成功/失败。
- async load callback 要检查 UObject 生命周期，并在 GameThread 写玩法对象。
- soft reference 资产必须通过 Primary Asset Rules、map 引用、显式 Cook 列表或 bundle 进入 Cook。

## 运行时与打包

- 验证 DataTable row struct、缺失 row fallback、重复 ID 和 row rename 风险。
- 存档里保存 row name、asset ID 或 soft path 时必须有版本迁移策略。
- Runtime 引用中避免 editor-only 资产。
- 对资产发现和异步加载行为做 packaged build 检查。

## 输出

- 数据形态决策：Data Asset、DataTable、DataRegistry、Config 或 backend。
- 引用策略：hard/soft、Primary Asset ID、row handle、Gameplay Tag。
- 加载流程：同步、异步、缓存、失败路径和生命周期。
- 验证：Editor 数据检查、PIE、packaged build、Cook 和迁移风险。

## 参考

- 选择 Data Asset、DataTable、DataRegistry 或 Config 前读取 `references/data-asset-patterns.md`。
- 添加 soft reference 或 `FStreamableManager` 加载前读取 `references/async-loading-checklist.md`。
- 资产前缀、Gameplay Tag 和模块命名使用共享 `rules/ue-naming.md`。
