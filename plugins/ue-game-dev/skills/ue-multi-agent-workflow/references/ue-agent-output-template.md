# UE Agent 输出模板

仅在 `lean` 或 `full` multi-agent 运行中使用本模板。简单任务（simple tasks）不要使用这个报告形状，直接通过具体 UE 技能回答。

```text
UE Multi-Agent Plan
- Mode: solo | lean | full
- Goal:
- Non-goals:
- Selected roles:
- Ownership boundaries:
- Parallel discovery:
- Dependent phases:
- Packaging boundary:

Parallel Discovery Results
- Coordinator: COMPLETE / CONCERNS / BLOCKED
- Project Explorer: COMPLETE / CONCERNS / BLOCKED
- [Specialist]: COMPLETE / CONCERNS / BLOCKED

Role Findings
- [Role]:
  - Evidence:
  - Finding:
  - Risk:
  - Recommended next skill:

Conflict And Blocker Log
- Status: NONE / CONCERNS / BLOCKED
- Owner:
- Reason:
- Decision needed:

Coordinator Synthesis
- Decisions:
- Implementation order:
- Files/assets to touch:
- Files/assets to avoid:
- Recommended next skills:
- Verification path:
- User action needed:
```

## 状态规则

| Status | 含义 |
|--------|------|
| `COMPLETE` | 角色已基于足够证据完成分配的检查。 |
| `CONCERNS` | 可以继续推进，但风险或不确定性必须带入下一步。 |
| `BLOCKED` | 缺少必要输入、权限、编辑器检查、构建访问或文件所有权信息。 |

## 保持轻量

- `lean` 模式中，每个角色的发现保持 1-3 条。
- `full` 模式中，给出足够证据让冲突可复查。
- 不粘贴完整日志，只引用第一个可行动错误或简短证据。
- 单个 Enhanced Input 问题、一个 BlueprintCallable 交接、一个 Blueprint 图修复、或一条 RunUAT 命令请求，不使用本模板。

## 打包边界行

打包自动化必须保持 explicit-only；packaging 风险审查不等于允许运行 package/build automation。

始终包含一行：

```text
Packaging boundary: review only / explicit automation requested / not relevant
```

如果是 `review only`，不要路由到 `$ue-build-release-automation`。
