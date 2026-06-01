# Changelog

本文件记录 ue-game-dev 插件的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [0.15.0] - 2026-06-01

### 新增
- 新增 `ue-game-features` 和 `ue-character-movement` 两个一等领域技能，覆盖 Game Feature/ModularGameplay/Lyra Experience、CharacterMovementComponent、网络预测和自定义移动模式。
- 新增 `skills/ue-game-dev-router/references/routing-rules.json`，把高优先级路由、显式打包 guardrail 和新领域关键词纳入数据化回归。
- 新增 UE 日志诊断 fixtures，覆盖 UHT 反射错误、Link 错误、Cook 缺失资产和 Crash/assert callstack。
- 新增 `ue_editor_command_report.py`，只读生成 DataValidation、CompileAllBlueprints、MapCheck 等 Editor commandlet 命令。
- 新增项目上下文模板、性能证据模板、BuildGraph/发布产物参考和 CharacterMovement 预测矩阵。

### 变更
- 强化 `ue_project_scan.py`，补充 Target 文件、Gameplay Tags、Asset Manager primary asset types 和 Runtime->Editor 风险扫描。
- 强化 `ue_log_triage.py` 的 UBT/UHT/UAT/Cook/Crash 阶段分类和根因文案，避免把 UAT 总结行误当根因。
- 强化 workflow state 的 local/team/import 模式和 stale detection 字段。
- 强化 GAS/网络验证矩阵、性能证据链、BuildGraph/Jenkins/Horde 发布自动化说明。
- `update_codex_app_plugin.py` 新增 `--dry-run`，可在不改本地 Codex App 缓存的情况下检查版本、目标路径和待复制文件数量。

### 验证
- `python scripts\validate_plugin.py`
- `python -m unittest discover tests`
- `git diff --check`

## [0.13.1] - 2026-06-01

### 新增
- 在 `ue-game-dev-router` 中加入 mattpocock/skills 风格的外部流程衔接说明：`diagnose`、`tdd`、`grill-with-docs` 和 `improve-codebase-architecture` 只作为后续流程建议，不复制进插件。
- 扩展 `Saved/CodexWorkflow/project-context.md` 模板，加入 target platforms、asset conventions、Gameplay Tags、Input/UI/GAS conventions、Runtime/Editor split、API verification notes，以及 `CONTEXT.md`、`CONTEXT-MAP.md`、`docs/adr/` 和 `.agents/ue-project-context.md` 的只读参考入口。
- 新增 `docs/agents/repo-workflow.md`，记录 GitHub、领域文档、外部工程技能和发布同步规则。

### 变更
- 增加 route scenarios，覆盖 UE bug 诊断、日志后续 diagnose、TDD 测试先行、架构复盘和需求模糊追问。
- `validate_plugin.py` 增加用户可见文本 mojibake 检测、外部工程流程 handoff 校验和 agent 工作流文档校验。
- `CONTRIBUTING.md` 增加本地 Codex App 更新、GitHub 分支同步和 mattpocock/skills 参考边界说明。

### 修复
- 统一根目录与市场包的用户可见中文验证基线，防止 README、默认 prompt、route scenarios、router 和 workflow-state 模板继续出现乱码。

## [0.13.0] - 2026-05-27

### 新增
- `ue-physics-destruction` 技能：覆盖 Chaos Physics、碰撞通道、Physical Material、Geometry Collection、Fracture、布娃娃、Physics Constraint 和物理调试。
- `ue-data-management` 技能：覆盖 Primary Asset Manager、Data Asset、DataTable、CurveTable、DataRegistry、软/硬引用、异步加载、Cook 和 Chunk 规则。
- `ue_config_audit.py` 只读工具：审计默认地图、Enhanced Input、Maps to Cook 和 editor-only 配置风险。
- `ue_dependency_graph.py` 只读工具：解析 `.Build.cs` 依赖、Runtime→Editor 风险、循环依赖和 Mermaid 模块图。
- `rules/ue-naming.md`、`rules/ue-performance.md`、`CONTRIBUTING.md` 和架构文档，用于插件维护与贡献流程。

### 变更
- 路由验证改为硬规则优先、领域加权评分 fallback，并补充大量中文路由场景。
- marketplace mirror 校验增加内容哈希比对，防止根目录与 `plugins/ue-game-dev/` 不同步。
- `plugin.json`、`README.md` 和市场包元数据更新到 `0.13.0`，补充 physics、chaos、destruction、data-management、asset-manager、config-audit 和 dependency-graph 等关键词。

## [0.12.0] - 2026-05-26

### 新增
- `ue-audio` 技能：覆盖 MetaSound、Sound Cue、AudioComponent、Sound Class/Mix、Concurrency、Quartz、空间化、衰减、音频调试和平台音频设置。
- `ue-world-streaming` 技能：覆盖 World Partition、Data Layers、HLOD、Level Streaming、Runtime Grid、Streaming Source、Actor 加载/卸载和开放世界验证。
- 路由场景补齐 AI、动画、架构、蓝图、UI、调试、编辑器工具、GAS、插件模块、渲染/VFX、存档、起步、测试、交互、音频和世界流送领域覆盖。

### 变更
- 扩充 `rules/` 下 C++、蓝图、网络、资产和打包共享规则，补充 Good/Bad 示例、Anti-Pattern、UE5 注意事项和验证边界。
- `ue-game-dev-router` 新增音频和世界流送专属路由，并将 audio、level streaming、World Partition 从覆盖缺口列表移除。
- `plugin.json`、`README.md` 和市场包元数据更新到 `0.12.0`，补充 audio、metasound、world-partition、data-layers、hlod、level-streaming 等关键词。

## [0.11.0] - 2026-05-26

### 新增
- `ue-async-systems` 技能：覆盖 `AsyncTask`、`Async()`、`UE::Tasks`、`FRunnable`、`ParallelFor`、`UBlueprintAsyncActionBase`、GameThread 回切、取消和生命周期安全。
- `ue-external-services` 技能：覆盖 HTTP/REST、JSON、WebSocket、TCP、外部服务客户端、心跳、重连、请求队列、认证头和 UI/Gameplay 分发。
- `ue-plugin-module-dev/references/third-party-library-wrapper.md`：补充第三方 C++ 库、SDK、DLL/静态库封装为 UE 插件/模块的通用边界。
- 路由场景新增异步蓝图节点、HTTP JSON 接口和 WebSocket 客户端用例。

### 变更
- `ue-game-dev-router` 新增异步系统和外部服务路由，并明确外部服务通信不等同于 GAS/UE 复制。
- `ue-cpp-gameplay`、`ue-architecture`、`ue-plugin-module-dev` 补充 Subsystem、`UDeveloperSettings`、异步、外部服务和第三方库封装的交接边界。
- `plugin.json`、`README.md` 更新到 `0.11.0`，补充 async、HTTP、WebSocket、TCP、JSON 和 backend API 关键词。

## [0.10.0] - 2026-05-21

### 新增
- `ue-project-scan` 只读工具：扫描 `.uproject`、模块、插件、源码文件、Build 文件和常见资产文件名。
- `ue-log-triage` 只读工具：提取 UE 日志中的首个可行动错误、失败阶段、证据和下一步技能，保持打包边界为 review-only。
- `ue-blueprint-api-report` 只读工具：扫描 C++ 头文件中的 Blueprint 暴露 API，并生成蓝图接法提示。
- `ue-agent-plan` 只读工具：根据请求生成 `solo` / `lean` / `full` 多 Agent 分工、所有权边界和后续技能。
- `tests/test_ue_tools.py`：为四个工具增加 fixture 驱动的单元测试。

### 变更
- `ue-project-onboarding`、`ue-log-crash-triage`、`ue-cpp-gameplay` 和 `ue-multi-agent-workflow` 补充工具调用说明和只读边界。
- `README.md` 新增内置工具表和命令示例。
- `plugin.json` 版本更新到 `0.10.0`，补充工具关键词和说明。
- `scripts/validate_plugin.py` 增加内置工具脚本存在性校验。

## [0.9.1] - 2026-05-21

### 新增
- `ue-multi-agent-workflow/references/ue-agent-roles.md`：补充 13 个 UE Agent 角色位、职责边界、触发条件和文件所有权规则。
- `ue-multi-agent-workflow/references/ue-agent-output-template.md`：补充 `lean` / `full` 多 Agent 统一输出模板、状态含义和打包边界输出行。
- `ue-multi-agent-workflow/references/ue-agent-conflict-resolution.md`：补充角色冲突、文件冲突、Blueprint/C++ 交接冲突和显式打包边界冲突的处理协议。

### 变更
- `ue-multi-agent-workflow` 主技能改为按需读取 reference，并明确 `solo` 模式不输出多 Agent 报告，避免简单任务流程过重。
- `README.md` 新增 Agent 编排说明，列出核心角色、可选专项角色、模式选择和不会默认启用多 Agent 的简单场景。
- `plugin.json` 版本更新到 `0.9.1`。
- `scripts/validate_plugin.py` 增加多 Agent reference 文件存在性和关键边界内容校验。

## [0.9.0] - 2026-05-21

### 新增
- `ue-multi-agent-workflow` 技能 — 用于用户明确要求多 Agent、多专家、团队协作、`lean`/`full` 模式，或复杂 UE 跨域任务需要角色分工、并行发现、文件所有权边界和协调汇总时使用。
- 路由场景测试新增多 Agent 旧项目接手、插件架构审查、打包失败风险排查，以及 Enhanced Input 不应误触发多 Agent 的回归用例。

### 变更
- `ue-game-dev-router` 新增多 Agent 编排路由，同时保持简单单域任务直接进入具体技能。
- `plugin.json`、`README.md` 和市场展示说明更新到 `0.9.0`，补充多 Agent / 多专家 / 并行工作流关键词。
- `scripts/validate_plugin.py` 增加多 Agent 技能结构、router 引用、关键词和自动打包边界校验。

## [0.8.1] - 2026-05-21

### 变更
- 将插件图标调整为 Codex App 深色界面更清晰的黑色圆角背景、白色 UE 标志和白色 `UNREAL ENGINE` 文字。
- 同步更新市场安装包内的图标资源，便于 Codex App 重新安装或刷新插件缓存时使用新图标。

## [0.8.0] - 2026-05-20

### 新增
- Codex App 插件市场兼容结构：新增 `.agents/plugins/marketplace.json`，可作为 Codex App 的插件市场源被添加。
- 新增 `plugins/ue-game-dev/` 市场安装包镜像，供 marketplace 条目通过 `./plugins/ue-game-dev` 发现和安装插件。
- 新增 `scripts/sync_marketplace_package.py`，用于把根目录插件内容同步到市场安装包镜像。

### 变更
- `plugin.json` 默认提示精简为 3 条，适配 Codex App 插件市场卡片和 composer 入口展示。
- `scripts/validate_plugin.py` 增加 marketplace 清单、市场包路径、安装策略、分类和版本一致性校验。
- `README.md` 补充 Codex App “添加插件市场”安装方式、字段填写建议和市场包维护流程。

## [0.7.0] - 2026-05-20

### 新增
- `ue-workflow-state` 技能 — 用于创建、读取和刷新 `Saved/CodexWorkflow/` 项目记忆，保存项目上下文、模块地图、资产索引、决策、已知风险和当前任务状态。
- `ue-log-crash-triage` 技能 — 用于分诊 UBT/UHT 编译错误、链接错误、蓝图编译错误、Editor 崩溃、callstack、ensure/assert、UAT/Cook/打包失败和 `Saved/Logs` 输出。
- `ue-workflow-state/references/state-file-templates.md` — 项目记忆默认 markdown 文件模板。
- `ue-log-crash-triage/references/triage-report-template.md` — 日志/崩溃分诊报告模板。

### 变更
- `ue-game-dev-router` 新增项目记忆和日志/崩溃分诊路由。
- `README.md`、`plugin.json` 和路由场景测试更新到 `0.7.0`。

## [0.6.0] - 2026-05-20

### 新增
- `ue-stage-detect` 技能 — 用于只读检测 UE 项目当前工作流阶段、缺口和下一步建议。
- `ue-gate-check` 技能 — 用于阶段门检查，输出 `PASS / CONCERNS / FAIL` 就绪评估。
- `templates/ue-task.md` — UE 功能/修复任务模板。
- `templates/ue-test-evidence.md` — UE 构建、蓝图、PIE、测试、多人和打包风险证据模板。
- `rules/` 规则包 — 新增 UE C++、蓝图、网络、资产和打包规则。
- `tests/route_scenarios.json` — 路由场景测试数据，覆盖旧项目接手、需求简报、实施计划、阶段检测、阶段门、自动打包边界、Enhanced Input 和完成验收。

### 变更
- `ue-game-dev-router` 新增阶段检测与阶段门路由，并引用共享规则包。
- `ue-feature-done` 增加证据表输出要求，可使用 `templates/ue-test-evidence.md` 保存验证记录。
- `scripts/validate_plugin.py` 增加共享文件检查、路由场景测试和自动打包边界回归测试。
- `README.md` 和 `plugin.json` 更新到 `0.6.0`，补充阶段检测、阶段门和证据化验收能力说明。

## [0.5.0] - 2026-05-20

### 新增
- `ue-start` 技能 — 用于 UE 任务入口判断、阶段识别和下一步技能路由。
- `ue-feature-brief` 技能 — 用于将粗略 UE 功能想法整理成可实施的需求简报。
- `ue-implementation-plan` 技能 — 用于将明确需求拆成 C++、蓝图、资产、配置、测试和验证计划。
- `ue-feature-done` 技能 — 用于功能完成验收、验证证据、蓝图/编辑器交接和残余风险说明。
- `scripts/validate_plugin.py` — 插件自检脚本，校验技能结构、README 技能数量、`plugin.json` 和自动打包显式调用边界。

### 变更
- 强化 `ue-game-dev-router`，将其作为统一生产工作流入口，先判断阶段，再分发到领域技能。
- `README.md` 增加工作流型调用示例、自检说明和 22 个领域技能清单。
- `plugin.json` 更新到 `0.5.0`，补充 project intake、feature brief、implementation plan、completion handoff 等关键词和默认提示。

## [0.4.0] - 2026-05-19

### 新增
- `ue-build-release-automation` 技能 — 用于用户显式请求自动打包、一键打包、`RunUAT`、`BuildCookRun`、Project Launcher 或 CI 发版流水线时生成/执行打包流程。
  - `references/buildcookrun-commands.md` — 常用 `BuildCookRun` 命令、参数和输出模板。
  - `references/release-automation-checklist.md` — 自动打包前置检查、执行规则、打包后冒烟和失败归因。
  - `references/ci-build-templates.md` — PowerShell 打包脚本和 GitHub Actions 自托管 runner 模板。
- `ue-input-enhanced` 技能 — 用于 Enhanced Input、Input Action、Input Mapping Context、触发器/修饰器、按键重绑定、UI 焦点冲突和输入事件不触发排查。
  - `references/enhanced-input-checklist.md` — Enhanced Input 资产、C++ 绑定、Build.cs 和验证清单。
  - `references/rebinding-and-ui.md` — 运行时重绑定、UI 输入模式、CommonUI 和蓝图交接模板。

### 变更
- `ue-game-dev-router` 新增 Enhanced Input 路由。
- `ue-game-dev-router` 增加显式打包边界：自动打包只在用户主动提出打包/RunUAT/BuildCookRun/CI 发版等请求时使用，普通发布检查仍走 `ue-performance-packaging`。
- `README.md` 和 `plugin.json` 更新技能数量、默认提示、关键词和插件能力说明。

## [0.3.1] - 2026-05-19

### 变更
- `ue-cpp-gameplay` 要求新增或修改 Blueprint 暴露 C++ API 后，必须给出蓝图实现/调用步骤、节点搜索名、pin 连接和验证方式。
- `ue-cpp-gameplay/references/blueprint-api.md` 增加 Blueprint Implementation Steps 模板和不同 API 暴露类型的蓝图说明规则。
- `ue-blueprint-workflow` 补充 C++ API 节点级接线说明要求。

## [0.3.0] - 2026-05-19

### 新增
- `ue-project-onboarding` 技能 — 用于旧项目接手、项目熟悉、二开前只读分析和接手报告。
  - `references/project-audit-checklist.md` — UE 项目结构、模块、资产、配置和风险检查清单。
  - `references/onboarding-report-template.md` — UE 项目接手报告模板。

### 变更
- `ue-game-dev-router` 新增旧项目、二开、接手、熟悉项目等场景的路由入口。
- `README.md` 和 `plugin.json` 更新项目接手/二开前分析能力说明。

## [0.2.1] - 2026-05-19

### 新增
- `README.md` 增加 Codex 本地插件安装步骤、`marketplace.json` 示例和开发目录链接方式。
- `README.md` 增加 `@ue-game-dev` 与 `/ue-game-dev` 快速调用示例。

### 变更
- `plugin.json` 增加别名触发说明，便于通过 `@ue-game-dev`、`/ue-game-dev` 或自然语言调用插件。
- `plugin.json` 更新 composer 默认提示为更短的中文入口示例。

## [0.2.0] - 2026-05-19

### 新增
- `ue-ai-navigation` 技能 — 覆盖行为树、黑板、EQS、NavMesh、AI 感知、StateTree
  - `references/ai-behavior-checklist.md` — AI 行为检查清单
  - `references/navigation-checklist.md` — 导航系统检查清单
- `ue-animation` 技能 — 覆盖动画蓝图、蒙太奇、IK、Control Rig、Motion Matching
  - `references/animation-checklist.md` — 动画检查清单
  - `references/animation-performance.md` — 动画性能参考
- `ue-testing-automation` 技能 — 覆盖 AutomationSpec、FAutomationTestBase、Functional Tests、编辑器冒烟测试、PIE/多人验证、资产校验
  - `references/testing-checklist.md` — 测试层级选择、插件/模块检查、断言和运行建议
- `README.md` — 项目说明文档
- `CHANGELOG.md` — 版本变更记录
- `LICENSE` — MIT 许可证文件
- `.gitattributes` — 行尾符统一控制

### 变更
- `ue-game-dev-router` — 新增 AI/导航、动画、测试自动化路由条目，新增兜底规则
- `plugin.json` — 精简 description，新增 AI/动画/测试关键词，清理占位符元数据
- `plugin.json` — 更新 shortDescription 和 longDescription 以反映新技能

## [0.1.0] - 初始版本

### 新增
- 插件框架和 `plugin.json` 元数据
- `ue-game-dev-router` 路由技能
- 12 个领域技能：cpp-gameplay、blueprint-workflow、plugin-module-dev、editor-tooling-slate、architecture、gas-networking、save-load-sync、world-interaction、render-vfx、client-ui、debug-validation、performance-packaging
- 每个技能包含 SKILL.md、agents/openai.yaml 和 references 参考文档
- SVG 插件图标
