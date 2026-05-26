# UE Agent 冲突处理

## 冲突类型

- 文件冲突：两个角色建议修改同一 C++、Blueprint、资产或配置文件。
- ownership 冲突：C++、Blueprint、UI、网络或存档都声称拥有同一状态。
- 顺序冲突：某角色建议先实现，另一个角色指出需要先完成架构或验证。
- packaging 冲突：风险审查被误解为允许打包自动化。
- 证据冲突：日志、项目结构或资产状态给出相反结论。

## 处理规则

1. Coordinator 先记录冲突，不立即选边。
2. 要求每个角色给出证据来源：文件、日志、命令、资产路径或观察结果。
3. 优先使用项目现有约定，其次使用 UE 模块/反射/资产规则。
4. 如果冲突影响实现安全，状态标记为 `BLOCKED`，并提出一个最小澄清问题。
5. 如果只是偏好差异，Coordinator 选择较小影响面并记录 tradeoff。

## Blueprint/C++ 交接冲突

- C++ 拥有稳定 API、authority、replication、save/load 和性能敏感逻辑。
- Blueprint 拥有表现、调参、默认资产、简单组合和设计师工作流。
- UI 不拥有 gameplay authority，只发出用户意图并订阅状态。
- 冲突无法解决时，先定义接口，再分别实现 C++ 和 Blueprint 侧。

## 打包边界冲突

- packaging readiness review 不等于运行打包。
- multi-agent request 本身不授权 `$ue-build-release-automation`。
- simple 单域任务不应因为有 packaging 关键词就升级成多 Agent 或打包自动化。
- 用户明确说“运行打包”“生成 BuildCookRun”“创建 CI 发版流水线”时，才进入显式自动化。
- 否则输出 `Packaging boundary: review only`。

## 输出要求

```text
Conflict:
Evidence:
Decision:
Owner:
Risk carried forward:
Next skill:
```

如果缺少必要证据，使用 `BLOCKED`，不要伪装成确定结论。
