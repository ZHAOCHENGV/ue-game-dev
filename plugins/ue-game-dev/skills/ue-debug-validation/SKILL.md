---
name: ue-debug-validation
description: 当 Unreal Engine 任务涉及输出日志、资产检查、Blueprint 编译、C++ 失败、网络 Bug、编辑器配置、复现隔离、运行时行为排查或回归验证时使用。
---

# UE Debug Validation

## 概览

这个技能用于“行为不对但原因未明”的 UE 排查。先收集证据，再缩小复现，再提出最小修复或验证路径。

## 使用场景

- Actor Tick 执行了但效果不对、输入触发了但状态没变、组件存在但不可见。
- Blueprint 编译或运行异常、资产引用丢失、配置不生效。
- 网络同步、PIE 多窗口、Dedicated Server、Listen Server 行为不一致。
- 需要完成后回归验证或调试证据。

## 工作流程

1. 明确期望行为、实际行为、首次出现版本和最小复现场景。
2. 收集证据：Output Log、breakpoint、Blueprint watch、`stat`、`showdebug`、Gameplay Debugger、Visual Logger。
3. 分离层级：输入、Actor 生命周期、组件、资产、网络、UI、动画、渲染或配置。
4. 一次只验证一个假设，记录证据和排除项。
5. 给出修复建议前，说明尚未验证的风险和需要的测试。

## 常用命令

- `stat unit`、`stat game`、`stat slate`、`stat net`、`stat audio`、`stat anim`。
- `showdebug enhancedinput`、`showdebug abilitysystem`、`showdebug animation`、`showdebug ai`。
- Gameplay Debugger、Visual Logger、Blueprint breakpoints、条件断点、PIE 多客户端。

## 规则

- 不要从症状直接跳到修复；先确认触发链是否到达目标层。
- Blueprint 和 C++ 混合问题要同时验证节点、反射声明、默认值和实例覆盖。
- 多人问题必须说明 server/client、ownership、authority、replication 和 RPC 方向。
- 资产问题要确认路径、重定向、Cook、加载时机和编辑器缓存。

## 输出

- 复现：步骤、地图、角色、输入、期望/实际。
- 证据：日志、断点、调试命令、截图或观察结果。
- 假设：已验证、已排除、仍需验证。
- 下一步：最小修复、回归场景或应切换的领域技能。

## 常见问题

| 症状 | 可能原因 | 首个检查点 |
|------|----------|------------|
| Tick 执行但状态没变 | 实例不对、authority guard 或数据被覆盖 | 记录对象名、role、owner 和 Tick 前后数值 |
| Blueprint 节点连了但无效果 | PIE debug object 不对或 latent context 不对 | 设置正确调试对象并重新编译资产 |
| PIE 正常但 packaged build 失败 | Editor-only 引用、资产未 Cook 或配置差异 | 检查 `WITH_EDITOR`、模块依赖和 packaged log |
| 多人客户端与服务器不一致 | Ownership、RPC 方向或 RepNotify 顺序问题 | 记录 role、owner、instigator 和复制时间点 |

## 参考

- 调试清单读取 `references/debug-checklist.md`。
- 报告模板读取 `references/debug-templates.md`。
