# Changelog

本文件记录 ue-game-dev 插件的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

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
