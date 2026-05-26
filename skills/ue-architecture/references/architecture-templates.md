# UE 架构模板

## 模块图

```text
Module:
- Type:
- Depends on:
- Public API:
- Private implementation:
- Blueprint exposure:
- Assets owned:
- Risks:
```

## Ownership Boundaries

```text
System:
- Owns state:
- Reads state:
- Sends commands:
- Emits events:
- Blueprint extension points:
- Save/replication boundary:
```

## 迁移计划

```text
Goal:
Current coupling:
Target boundary:
Step 1:
Step 2:
Step 3:
Validation:
Rollback:
```

## 架构审查输出

- 当前结构：模块、插件、目录和依赖。
- 问题：循环依赖、Editor 泄漏、Public 头过重、ownership 不清。
- 建议：目标模块图、API、迁移顺序。
- 风险：Blueprint 兼容、资产引用、打包、测试缺口。
- 验证：构建、Blueprint compile、PIE、packaged build。
