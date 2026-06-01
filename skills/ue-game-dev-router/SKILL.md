---
name: ue-game-dev-router
description: 当 Unreal Engine 游戏或客户端开发请求需要路由到最具体的 UE 工作流技能，或请求横跨项目入口、阶段检测、门检、项目记忆、日志/崩溃、需求简报、实施计划、完成交接、旧项目接手、多 Agent、Blueprint、C++、插件、模块、编辑器工具、GAS、网络、输入、AI、动画、渲染、UI、物理、数据、测试、调试、性能或打包时使用。
---

# UE Game Dev Router

当请求横跨多个 Unreal Engine 领域，或最合适的工作流不明确时，先使用本技能。先判断阶段，再路由到最具体的同级技能。

## 阶段路由

- 用 `$ue-start` 处理范围、项目阶段或下一步流程不清的 UE 任务入口。
- 用 `$ue-stage-detect` 处理项目处于什么阶段、缺什么、下一步是什么的只读分析。
- 用 `$ue-gate-check` 处理是否能进入实现、验证、打包准备或显式发版打包的门检。
- 用 `$ue-feature-brief` 处理需要先整理成 UE 功能简报的粗略想法。
- 用 `$ue-implementation-plan` 处理需求已足够清晰、需要拆解 C++/Blueprint/资产/配置/测试/验证的任务。
- 用 `$ue-feature-done` 处理完成验收、交接、提交前确认或“是否做完”。
- 用 `$ue-project-onboarding` 处理旧项目接手、熟悉、审查、二开前分析，第一轮保持只读。
- 用 `$ue-workflow-state` 处理 `Saved/CodexWorkflow/` 项目记忆、模块地图、资产索引、决策、风险和当前任务状态。
- 用 `$ue-multi-agent-workflow` 处理用户明确要求 multi-agent、多专家、团队协作、并行专家、`lean` 或 `full` 模式，或复杂请求横跨旧项目接手、架构、C++/Blueprint/UI/资产/测试和发布/日志风险。

## 领域路由

- 用 `$ue-cpp-gameplay` 处理 Actor、Component、UObject、DataAsset、Subsystem、输入驱动玩法、世界交互、存档 hook 和通用 Gameplay C++。
- 用 `$ue-blueprint-workflow` 处理 Blueprint 图逻辑、Event Graph、函数图、输入事件、节点/Pin 连线、Widget Blueprint 和蓝图编译验证。
- 用 `$ue-plugin-module-dev` 处理 UE 插件结构、`.uplugin`、模块描述、Runtime/Editor 拆分、`.Build.cs`、API macro、Public/Private 和命名规范。
- 用 `$ue-editor-tooling-slate` 处理编辑器插件、Slate UI、ToolMenus、UICommands、工具栏/菜单扩展、Details 自定义、资产操作和 Editor Subsystem。
- 用 `$ue-architecture` 处理模块布局、`.Build.cs` 依赖、Public/Private 边界、反射暴露策略、插件边界和大型重构。
- 用 `$ue-gas-networking` 处理 GAS abilities、attributes、effects、cues、prediction、replication、RPC、authority flow 和多人调试。
- 用 `$ue-input-enhanced` 处理 Enhanced Input、Input Actions、Input Mapping Contexts、Modifiers/Triggers、Pawn/Controller 绑定、运行时映射、按键重绑、本地多人输入和 UI 焦点冲突。
- 用 `$ue-async-systems` 处理 `AsyncTask`、`Async()`、`UE::Tasks`、`FRunnable`、`ParallelFor`、`UBlueprintAsyncActionBase`、GameThread 回切、取消和生命周期。
- 用 `$ue-external-services` 处理 HTTP、REST、JSON、WebSocket、TCP、后端 API、流式响应、心跳、重连、请求队列、认证头和外部服务集成。
- 用 `$ue-audio` 处理 MetaSound、Sound Cue、AudioComponent、Sound Class/Mix、Concurrency、Quartz、空间化、衰减和音频性能。
- 用 `$ue-world-streaming` 处理 World Partition、Data Layers、HLOD、Level Streaming、Streaming Volume、Large World Coordinates、Runtime Grid 和 Actor 加载/卸载。
- 用 `$ue-game-features` 处理 Game Feature Plugin、ModularGameplay、Lyra Experience、UGameFeatureAction、运行时组件/能力/Input/UI 授予和模块化玩法激活。
- 用 `$ue-mass-entity` 处理 Mass Entity、MassProcessor、MassFragment、Mass Crowd、Mass AI、ZoneGraph、Smart Objects 和大量 NPC 数据导向模拟。
- 用 `$ue-procedural-generation` 处理 PCG、PCG Graph、程序化生成、ProceduralMesh、ISM/HISM、Spline 生成、确定性 seed、生成碰撞和运行时生成。
- 用 `$ue-state-trees` 处理 StateTree、StateTreeTask、Condition、Evaluator、AI/Gameplay 状态树、Mass 行为和状态转换调试。
- 用 `$ue-sequencer-cinematics` 处理 Sequencer、Level Sequence、Movie Render Queue、过场动画、镜头轨道、事件轨道、Take Recorder 和渲染输出流水线。
- 用 `$ue-character-movement` 处理 CharacterMovementComponent、角色移动、自定义移动模式、移动复制、网络预测、server correction、root motion 和 locomotion bug。
- 用 `$ue-physics-destruction` 处理 Chaos Physics、碰撞通道/配置、Physical Material、Geometry Collection、Fracture、布娃娃、Physics Constraint、物理动画混合和物理调试。
- 用 `$ue-data-management` 处理 Primary Asset Manager、Data Asset、DataTable、CurveTable、DataRegistry、软/硬引用、异步资产加载、Cook 规则、Chunk 和玩法数据验证。
- 用 `$ue-save-load-sync` 处理 SaveGame schema、序列化、恢复流程、RepNotify、RPC 入口和持久状态/网络状态交叉。
- 用 `$ue-world-interaction` 处理拾取、生成器、Overlap/Trace 交互、交互半径、世界 Actor 生命周期和成功/失败反馈。
- 用 `$ue-render-vfx` 处理 renderer settings、材质、Material Function、shader、post process、Niagara、粒子、GPU simulation、LOD 和视觉性能。
- 用 `$ue-client-ui` 处理 UMG、HUD、CommonUI、ViewModel、Enhanced Input UI 流程、加载界面、本地化、DPI 和 UI 性能。
- 用 `$ue-log-crash-triage` 处理日志、UBT/UHT 编译错误、链接错误、Blueprint 编译错误、Editor 崩溃、callstack、ensure/assert、UAT/Cook/打包失败或 `Saved/Logs`。
- 用 `$ue-debug-validation` 处理行为异常或尚未验证的运行时、资产、Blueprint、C++、网络或编辑器配置诊断。
- 用 `$ue-build-release-automation` 只处理用户当前明确要求打包、创建/运行一键打包、生成 `RunUAT`/`BuildCookRun`、配置 Project Launcher 或 CI 发版自动化的请求。Do not route here for passive readiness checks.
- 用 `$ue-performance-packaging` 处理 profiling、stat review、打包失败诊断、构建配置、发布准备、打包烟测和 go/no-go 清单。
- 用 `$ue-ai-navigation` 处理 Behavior Tree、Blackboard、EQS、NavMesh、AI Controller、AI Perception、StateTree、群体 AI 和自主行为。
- 用 `$ue-animation` 处理 Animation Blueprint、Montage、Blend Space、状态机、IK、Control Rig、Motion Matching、root motion、Anim Notify 和动画性能。
- 用 `$ue-testing-automation` 处理 AutomationSpec、`FAutomationTestBase`、Functional Test、编辑器工具烟测、PIE/多人场景、资产验证、打包烟测和回归计划。

跨域任务先进入“第一个失败点或用户可见行为”的拥有技能，再按需引入其他技能。用户明确要求多 Agent 时，先进入 `$ue-multi-agent-workflow` 定义角色、所有权边界、并行发现和后续技能。

若请求涉及其他尚无专属技能的领域，基于通用 UE 最佳实践处理，并明确告知当前插件暂无该领域专属技能。

## 外部工程流程交接

UE Game Dev 仍然是 Unreal 领域路由器。不要把 mattpocock/skills 的通用工程技能复制或替换进本插件；只在它们能增强 UE 工作流时作为后续流程交接提示。

- UE bug、运行时回归、性能回归，或 `$ue-log-crash-triage` 之后还需要继续定位的日志问题，UE 归属仍是 `$ue-log-crash-triage` 或 `$ue-debug-validation`，然后建议外部 `diagnose` 的“复现 -> 最小化 -> 假设 -> 插桩 -> 修复 -> 回归测试”闭环。
- 新 UE 功能明确要求 TDD、测试先行、回归测试或 test-driven implementation 时，UE 归属先进入 `$ue-testing-automation` 或 `$ue-implementation-plan`，然后建议外部 `tdd` 维持 red/green/refactor 纪律。
- 需求模糊、术语负载过重、项目语言不清或计划需要实现前追问时，UE 归属先进入 `$ue-feature-brief`，然后建议 `grill-with-docs` 式地对照项目上下文和 ADR 追问。
- 旧 UE 项目、模块纠缠、Runtime/Editor 依赖问题、模块边界过浅或 test seam 很差时，UE 归属先进入 `$ue-project-onboarding` 或 `$ue-architecture`，然后建议 `improve-codebase-architecture` 做更深的架构复盘。

## 中文路由提示

- “粒子特效 / 后处理 / 材质球 / 着色器”路由到 `$ue-render-vfx`。
- “角色动画 / 动画蓝图 / 蒙太奇 / 状态机 / IK”路由到 `$ue-animation`。
- “行为树 / 巡逻 / 寻路 / AI感知 / 导航网格”路由到 `$ue-ai-navigation`。
- “Game Feature / ModularGameplay / Lyra Experience / 模块化玩法 / 功能插件”路由到 `$ue-game-features`。
- “Mass Entity / Mass AI / Mass Crowd / 群体 AI / 大量 NPC / 人群模拟”路由到 `$ue-mass-entity`。
- “PCG / 程序化生成 / 生成地形 / 生成植被 / ProceduralMesh / HISM”路由到 `$ue-procedural-generation`。
- “StateTree / 状态树 / 状态树任务 / 状态转换”路由到 `$ue-state-trees`。
- “Sequencer / Level Sequence / Movie Render Queue / 过场动画 / 镜头轨道”路由到 `$ue-sequencer-cinematics`。
- “CharacterMovementComponent / 角色移动 / 自定义移动模式 / 网络预测 / 移动复制”路由到 `$ue-character-movement`。
- “存档 / 读档 / 数据持久化”路由到 `$ue-save-load-sync`。
- “布娃娃 / 物理约束 / 破坏系统 / 碰撞通道”路由到 `$ue-physics-destruction`。
- “DataTable / 数据表 / 数据资产 / 软引用 / 异步加载 / 资产管理”路由到 `$ue-data-management`。
- “诊断 / 稳定复现 / 插桩 / 运行时 bug”路由到 `$ue-debug-validation`，需要时再衔接 `diagnose`。
- “TDD / 测试先行 / 回归测试 / 自动化测试”路由到 `$ue-testing-automation`，用户明确要求测试先行时再衔接 `tdd`。
- “需求模糊 / 术语不清 / 追问 / 澄清需求”路由到 `$ue-feature-brief`，项目语言很关键时再衔接 `grill-with-docs`。
- “架构复盘 / 模块太乱 / 可测试性 / test seam”路由到 `$ue-architecture`，模块深度问题明显时再衔接 `improve-codebase-architecture`。

## 模糊请求处理

1. 阶段词优先于领域词，例如“需求简报”“实施计划”“验收”。
2. 错误、日志、崩溃、不触发优先走 `$ue-log-crash-triage` 或 `$ue-debug-validation`。
3. 性能、帧率、内存、Cook、package readiness 优先走 `$ue-performance-packaging`。
4. 同时涉及 Blueprint 和 C++ 时，先判断用户要改图、暴露 API 还是实现运行时系统。
5. 仍不明确时，只问一个会改变路由的问题。

## 生产工作流

```text
intake -> stage detect -> workflow state -> brief -> gate check -> implementation plan -> domain implementation -> log/debug triage -> feature done -> workflow state refresh
```

- 只有在用户明确要求多 Agent，或任务复杂到需要角色协调时，才在 onboarding、architecture review、implementation planning 或 log/release risk review 前插入 `$ue-multi-agent-workflow`。
- 旧项目接手在用户批准实现前保持只读。
- 用 brief 消除需求歧义，用 gate check 输出 PASS/CONCERNS/FAIL，用 implementation plan 拆 C++、Blueprint、资产、配置和验证。
- 用 `Saved/CodexWorkflow/` 保存跨会话项目理解。
- 声称完成或交接前使用 `$ue-feature-done`。

## 显式打包边界

- 自动打包是主动操作，不是被动建议。
- 不要仅因为任务涉及发布准备、性能、测试或打包失败诊断就调用 `$ue-build-release-automation`。
- 只有用户使用“打包”“一键打包”“自动打包”“生成打包脚本”“运行打包”“BuildCookRun”“RunUAT”“Project Launcher”“CI 打包”“发版流水线”等明确自动化意图时才路由过去。
- 如果用户只是问项目是否准备好打包，先路由到 `$ue-performance-packaging`。

## Blueprint 与 C++ 分工

- Blueprint 和 C++ 是同级工作流，不因为能改代码就默认用 C++。
- 图级逻辑、设计师调参、事件连线、Widget 行为和快速玩法组合优先 Blueprint。
- 可复用运行时系统、性能敏感循环、高级网络、自定义异步、引擎 API 和稳定多蓝图 API 优先 C++。
- 混合功能先定义 C++ 基类/API，再说明 Blueprint 扩展点、默认值、图连线和验证。

## 预检发现

- 先定位 `.uproject`，读取引擎版本、模块、插件和项目名。
- 在建议改动前映射 `Source/`、`Content/`、`Config/`、`Plugins/`、target 文件和模块 `.Build.cs`。
- 新建资产或代码前检查现有 Blueprint、Input Action、Input Mapping Context、Widget、Gameplay Tag 和命名模式。
- 遵循 UE 命名：C++ 前缀 `U`、`A`、`F`、`E`、`I`、`S`，模块 API macro，资产名 `[AssetTypePrefix]_[AssetName]_[Descriptor]_[Variant]`。

## 工作规则

- 优先遵循项目已有约定、模块边界、命名和 subsystem 模式。
- C++ 保持反射卫生：`UCLASS`、`USTRUCT`、`UFUNCTION`、`UPROPERTY` 正确，UObject 引用具备 GC 意识，Public 头最小化。
- Blueprint 先描述图流，再给出节点/Pin 连线，验证编译并避免重复输入事件。
- Runtime 与 Editor 依赖分离，编辑器工具注册/注销对称。
- 多人任务必须说明 authority、ownership、replication、prediction 和验证场景。
- 使用共享 `rules/` 处理 C++、Blueprint、网络、资产、命名、性能和打包规则。

## 验证

- 优先运行触及模块的 UE 构建或可用的语法/构建检查。
- Blueprint 工作验证编译、事件唯一性、Pin 兼容和资产引用。
- 网络工作给出最小 PIE 或 Dedicated Server 场景。
- 渲染/UI/性能/打包工作要区分 Editor 行为和 packaged runtime 行为。
