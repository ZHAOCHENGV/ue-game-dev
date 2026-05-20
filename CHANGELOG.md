# Changelog

本文件记录 ue-game-dev 插件的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

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
