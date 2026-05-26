---
name: ue-gate-check
description: 当用户询问 Unreal Engine 项目或功能是否可以进入实现、验证、打包准备、显式发版打包，或需要 PASS/CONCERNS/FAIL 门检结论、阻塞项和证据时使用。
---

# UE Gate Check

## 概览

这个技能输出阶段门结论：`PASS`、`CONCERNS` 或 `FAIL`。它用于判断是否可以进入下一阶段，不负责主动打包；明确打包自动化才进入 `$ue-build-release-automation`。

## 使用场景

- “这个功能能进入实现了吗？”
- “现在能做打包前验证了吗？”
- “这个项目是否准备好发布/测试/验收？”
- 需要列出阻塞项、风险、证据和下一步。

## 工作流程

1. 确认目标阶段：implementation、validation、packaging readiness、release automation。
2. 读取现有证据：需求简报、实施计划、构建结果、Blueprint 编译、PIE、测试、日志、性能。
3. 判断阻塞：缺需求、缺资产、编译失败、网络未验证、性能/打包风险、用户授权缺失。
4. 输出 `PASS`、`CONCERNS` 或 `FAIL`，并给出最小解除阻塞动作。

## 判定规则

- `PASS`：进入下一阶段所需证据充分，只有可接受的小风险。
- `CONCERNS`：可以前进，但需要明确跟踪风险或补充验证。
- `FAIL`：存在会导致下一阶段无效或高风险的阻塞项。
- 没有跑过的验证不能写成通过，只能写“未验证”。

## 输出

- Verdict：`PASS`、`CONCERNS` 或 `FAIL`。
- Evidence：已确认的文件、命令、日志、PIE/测试结果。
- Blockers：必须解决的问题。
- Risks：可接受但需跟踪的风险。
- Next action：下一步技能或最小操作。

## 参考

- 门检报告读取 `references/gate-check-template.md`。
