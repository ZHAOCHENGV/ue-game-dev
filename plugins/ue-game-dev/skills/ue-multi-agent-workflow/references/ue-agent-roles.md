# UE Agent 角色

## 核心角色

| 角色 | 职责 |
|------|------|
| Coordinator | 范围、角色、依赖顺序、冲突处理、最终综合和后续技能路由。 |
| Project Explorer | 只读梳理旧项目/现有项目结构、模块、插件、资产命名和可读文档。 |
| UE Architecture Reviewer | 模块边界、Runtime/Editor 拆分、Blueprint/C++ ownership boundaries、依赖方向。 |
| C++ Implementer | C++ API、反射、UObject 生命周期、编译风险和 Blueprint 暴露面。 |
| Blueprint Integrator | Blueprint 节点、Pin、默认值、事件、资产交接和设计师实现步骤。 |
| Verifier | 构建、Blueprint compile、PIE、自动化测试、日志证据和完成判断。 |

## 可选专项角色

| 角色 | 触发场景 |
|------|----------|
| GAS/Networking | GAS、ASC、RPC、replication、prediction、多 PIE。 |
| UI/UMG | Widget Blueprint、CommonUI、HUD、输入模式、DPI。 |
| Enhanced Input | Input Action、Mapping Context、重绑、UI 焦点。 |
| AI/Animation | Behavior Tree、EQS、StateTree、AnimBP、Montage。 |
| Render/VFX | Material、Niagara、post process、shader、视觉性能。 |
| Packaging/Release | packaging readiness、Project Launcher、CI、release 风险审查。 |
| Log/Crash Triage | UBT/UHT/UAT、`Saved/Logs`、callstack、ensure/assert。 |

## 角色状态

- `COMPLETE`：角色已有足够证据完成检查。
- `CONCERNS`：可继续，但需要携带风险。
- `BLOCKED`：缺少项目路径、日志、权限、构建访问、编辑器检查或 ownership 信息。

## 轻量原则

- simple 单域任务不要启用完整角色池。
- `lean` 默认只选 Coordinator 和 1-2 个专项角色。
- `full` 才适合旧项目深度接手、架构审查或跨 C++/Blueprint/UI/资产/测试/packaging 的大任务。
- 每个角色必须说明文件/资产所有权边界，避免建议互相踩踏。
