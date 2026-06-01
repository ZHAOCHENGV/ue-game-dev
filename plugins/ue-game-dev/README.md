# UE Game Dev - Codex Plugin

面向 Unreal Engine 游戏与客户端开发的 Codex 技能插件。它不是 Unreal Editor 的 `.uplugin` 插件，不需要放进 UE 项目的 `Plugins/` 目录；它是给 Codex App 使用的 UE 开发工作流插件，用来辅助项目入口判断、阶段检测、阶段门检查、项目记忆、日志/崩溃分诊、需求简报、实施计划、多 Agent 编排、证据化完成验收、旧项目接手、二开前分析、UE C++、蓝图、异步系统、外部 HTTP/WebSocket/TCP 服务、Game Feature、Mass Entity、PCG、StateTree、Sequencer、CharacterMovementComponent、Enhanced Input、GAS、网络同步、渲染、材质、Niagara、UI、调试、测试和显式打包自动化等开发任务。

插件还内置一组只读 UE 辅助工具，用于快速扫描项目结构、提取日志首个可行动错误、整理 C++ 暴露给蓝图的 API，以及生成轻量多 Agent 分工计划。这些工具默认不修改 UE 项目、不编辑 `.uasset`、不执行打包。部分 UE C++ API 准确性参考借鉴自 MIT 许可的 `quodsoler/unreal-engine-skills`，并改写为本插件的 Codex 工作流结构。

## 安装方法

### 方式一：通过 Codex App 添加插件市场（推荐）

本仓库已经兼容 Codex App 的插件市场结构：

- `.agents/plugins/marketplace.json`：插件市场清单。
- `plugins/ue-game-dev/`：Codex App 可安装的插件包。

在 Codex App 的插件页面选择添加插件市场时，可以这样填写：

```text
Name: ZHAOCHENGV UE Plugins
Source: https://github.com/ZHAOCHENGV/ue-game-dev.git
Git Ref: main
Sparse Path: 留空，或在界面必填时填 .
```

如果 Codex App 支持 GitHub 仓库简写，`Source` 也可以填写：

```text
ZHAOCHENGV/ue-game-dev
```

添加市场源后，在市场列表中安装并启用 `UE Game Dev` 即可。注意不要把 `Sparse Path` 填成 `plugins/ue-game-dev`：这个目录是 marketplace 清单指向的插件包，市场清单本身位于仓库根目录的 `.agents/plugins/marketplace.json`。

### 方式二：安装到 Codex 本地插件目录

1. 打开 PowerShell，创建本地插件目录和本地 marketplace 目录：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\plugins"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\plugins"
```

2. 将本仓库克隆到 Codex 本地插件目录：

```powershell
git clone https://github.com/zhaocw/ue-game-dev "$env:USERPROFILE\plugins\ue-game-dev"
```

如果你已经有本仓库源码，也可以把当前目录复制过去：

```powershell
Copy-Item -Recurse -Force "C:\path\to\ue-game-dev" "$env:USERPROFILE\plugins\ue-game-dev"
```

3. 确认或创建本地插件市场文件：

```text
%USERPROFILE%\.agents\plugins\marketplace.json
```

内容示例：

```json
{
  "name": "zhaocw-local",
  "interface": {
    "displayName": "zhaocw Local Plugins"
  },
  "plugins": [
    {
      "name": "ue-game-dev",
      "source": {
        "source": "local",
        "path": "./plugins/ue-game-dev"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Coding"
    }
  ]
}
```

如果 `marketplace.json` 已经存在，只需要把上面 `plugins` 数组里的 `ue-game-dev` 条目追加进去。

4. 重启 Codex App，然后在插件页面启用 `UE Game Dev`。

### 方式三：开发时使用目录链接

如果你正在本地开发这个插件，不想每次修改后复制文件，可以把插件目录链接到 Codex 本地插件目录：

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\plugins\ue-game-dev" -Target "C:\path\to\ue-game-dev"
```

之后重启 Codex App，Codex 会从链接目录读取最新文件。

## 快速调用

安装并启用后，推荐用最短入口调用：

```text
@ue-game-dev 先熟悉这个旧 UE 项目，后面我要基于它二开
@ue-game-dev 帮我看这个 UE 项目现在处于什么开发阶段，还缺什么
@ue-game-dev 检查一下这个功能是否可以进入打包前验证阶段
@ue-game-dev 为这个 UE 项目建立 Saved/CodexWorkflow 项目记忆
@ue-game-dev 分析这个 Saved/Logs 日志或崩溃 callstack，找出第一个可行动错误
@ue-game-dev 用多 Agent 熟悉这个旧 UE 项目，准备二开
@ue-game-dev 我想做一个 UE 背包系统，先帮我整理需求简报
@ue-game-dev 按这个功能需求写一份 C++/蓝图/资产/测试实施计划
@ue-game-dev 帮我设计一个 UE 编辑器插件
@ue-game-dev 检查这个 GAS 网络同步流程
@ue-game-dev 帮我做一个 UBlueprintAsyncActionBase 异步蓝图节点
@ue-game-dev 帮我在 UE 里接一个 HTTP JSON 接口，把返回数据分发给 UI
@ue-game-dev 帮我用 MetaSound 和 AudioComponent 做一个自适应音效系统
@ue-game-dev 帮我配置 World Partition、Data Layers 和 HLOD
@ue-game-dev 帮我做一个模块化 Game Feature 插件，接入 Lyra Experience
@ue-game-dev 帮我用 PCG 程序化生成地形和植被
@ue-game-dev 帮我调 CharacterMovementComponent 角色移动和网络预测
@ue-game-dev 给这个项目生成 Win64 Development 的 RunUAT 打包命令
@ue-game-dev 帮我排查 Enhanced Input 的 IA_Jump 为什么不触发
```

如果你的 Codex App 版本支持 `/` 插件入口，也可以这样使用：

```text
/ue-game-dev 设计一个 Runtime + Editor 双模块 UE 插件
/ue-game-dev 排查这个蓝图输入事件为什么没有触发
```

也可以直接用自然语言：

```text
Use UE Game Dev to design this Unreal plugin, module, or editor tool.
Use UE Game Dev to review this GAS and replication flow.
Use UE Game Dev to add tests for this UE feature.
```

> 注意：`@ue-game-dev` 和 `/ue-game-dev` 是否出现自动补全，取决于当前 Codex App 版本和插件市场加载状态。如果 `/` 没有弹出插件，优先使用 `@ue-game-dev` 或直接写 `Use UE Game Dev ...`。

## 功能概览

本插件包含 **1 个路由技能 + 39 个领域技能**，覆盖 UE 开发全链路：

| 技能 | 领域 |
|------|------|
| `ue-game-dev-router` | 请求路由与分发 |
| `ue-start` | UE 任务入口判断、阶段识别、下一步路由 |
| `ue-stage-detect` | UE 项目阶段检测、缺口分析、下一步建议 |
| `ue-gate-check` | 阶段门检查、PASS/CONCERNS/FAIL 就绪评估 |
| `ue-feature-brief` | 功能需求简报、范围澄清、约束整理 |
| `ue-implementation-plan` | C++/蓝图/资产/配置/测试实施计划 |
| `ue-feature-done` | 功能完成验收、验证证据、交接清单 |
| `ue-project-onboarding` | 旧项目接手、项目熟悉、二开前分析 |
| `ue-workflow-state` | 项目记忆、Saved/CodexWorkflow 状态文件、跨会话上下文刷新 |
| `ue-multi-agent-workflow` | 多 Agent / 多专家编排、复杂跨域任务分工、并行发现和协调汇总 |
| `ue-cpp-gameplay` | C++ 游戏逻辑（Actor、Component、Subsystem） |
| `ue-blueprint-workflow` | 蓝图工作流（事件图、函数图、Widget） |
| `ue-plugin-module-dev` | 插件与模块开发（.uplugin、Build.cs、命名规范） |
| `ue-editor-tooling-slate` | 编辑器工具与 Slate UI |
| `ue-architecture` | 架构设计与模块边界 |
| `ue-async-systems` | 异步系统、线程切换、Blueprint Async Action、取消与生命周期 |
| `ue-external-services` | HTTP、JSON、WebSocket、TCP、外部服务客户端 |
| `ue-audio` | MetaSound、Sound Cue、AudioComponent、Quartz、空间化和音频性能 |
| `ue-world-streaming` | World Partition、Data Layers、HLOD、Level Streaming 和开放世界流送 |
| `ue-game-features` | Game Feature Plugin、ModularGameplay、Lyra Experience、运行时功能激活 |
| `ue-mass-entity` | Mass Entity、Mass AI、Mass Crowd、Processor/Fragment/Observer |
| `ue-procedural-generation` | PCG、ProceduralMesh、ISM/HISM、样条和运行时程序化生成 |
| `ue-state-trees` | StateTree 任务、Evaluator、Condition、Transition 和状态机设计 |
| `ue-sequencer-cinematics` | Sequencer、Level Sequence、过场动画、Movie Render Queue |
| `ue-character-movement` | CharacterMovementComponent、移动模式、Root Motion、移动复制和网络预测 |
| `ue-physics-destruction` | Chaos 物理、碰撞、布娃娃、Geometry Collection 和破坏系统 |
| `ue-data-management` | DataTable、Data Asset、Asset Manager、软引用和异步资产加载 |
| `ue-input-enhanced` | Enhanced Input（Input Action、Mapping Context、重绑定、UI 焦点） |
| `ue-gas-networking` | GAS 技能系统与网络同步 |
| `ue-save-load-sync` | 存档/加载与状态同步 |
| `ue-world-interaction` | 世界交互（拾取、生成器、碰撞） |
| `ue-render-vfx` | 渲染、材质与 Niagara 特效 |
| `ue-client-ui` | 客户端 UI（UMG、CommonUI、HUD） |
| `ue-log-crash-triage` | 日志、崩溃、UBT/UHT/UAT、蓝图编译错误分诊 |
| `ue-debug-validation` | 调试与验证 |
| `ue-performance-packaging` | 性能分析与打包发布 |
| `ue-build-release-automation` | 显式自动打包、RunUAT/BuildCookRun、CI 发版流水线 |
| `ue-ai-navigation` | AI 行为树、EQS、导航系统 |
| `ue-animation` | 动画蓝图、蒙太奇、IK、状态机 |
| `ue-testing-automation` | 自动化测试、功能测试、PIE/多人验证、资产校验 |

## 工作原理

```text
用户请求 -> ue-game-dev-router（路由分析）-> 最匹配的领域技能
                                           |
                                           v
                                    专业化的规则、检查清单和参考文档
```

1. `ue-game-dev-router` 接收用户请求，分析所涉及的 UE 领域。
2. 路由器先判断阶段：入口判断、阶段检测、项目记忆、多 Agent 编排、需求简报、实施计划、具体实现、日志/崩溃分诊、调试验证、完成验收或显式打包。
3. 路由器分发到最匹配的领域技能，例如 C++ 游戏逻辑会进入 `ue-cpp-gameplay`。
4. 领域技能提供专业化工作流、检查清单、命名规范和参考模板。
5. 跨领域任务会按优先级组合多个技能，例如功能简报 + C++ 实施计划 + 蓝图交接 + 自动化测试。

异步系统和外部服务通信被拆成两个独立技能：`ue-async-systems` 负责 `AsyncTask`、`Async()`、`UE::Tasks`、`FRunnable`、`ParallelFor`、`UBlueprintAsyncActionBase`、GameThread 回切、取消和生命周期；`ue-external-services` 负责 HTTP/REST、JSON、WebSocket、TCP、心跳、重连、请求队列、认证头和服务结果分发。它们不会替代 `ue-gas-networking`，后者仍专注 GAS、RPC、复制、预测和 UE 多人玩法状态。

音频和开放世界流送现在也有独立技能：`ue-audio` 覆盖 MetaSound、Sound Cue、AudioComponent、Sound Class/Mix、Concurrency、Quartz、空间化、衰减和音频性能；`ue-world-streaming` 覆盖 World Partition、Data Layers、HLOD、Level Streaming、Runtime Grid、Streaming Source 和流送验证。

从 `0.14.0` 开始，插件新增一组从 UE C++ API 准确性参考中提炼出的领域技能：`ue-game-features`、`ue-mass-entity`、`ue-procedural-generation`、`ue-state-trees`、`ue-sequencer-cinematics` 和 `ue-character-movement`。这些技能保留 Codex 的项目接手、路由、验证和交接方式，同时补强 Game Feature、Mass、PCG、StateTree、Sequencer 和 CharacterMovementComponent 等 UE5 专项领域。

从 `0.14.1` 开始，router 额外记录 mattpocock/skills 风格的工程流程交接：UE 日志和运行时 bug 仍先进入 `ue-log-crash-triage` 或 `ue-debug-validation`，再建议本地 `diagnose` 闭环；明确要求测试先行时进入 `ue-testing-automation`，再衔接 `tdd`；需求模糊时先走 `ue-feature-brief`，可用 `grill-with-docs` 式追问；老项目模块混乱时先走 `ue-project-onboarding` 或 `ue-architecture`，再衔接 `improve-codebase-architecture`。这些流程只是提示和交接，不把通用技能整包复制进 UE 插件。

多 Agent 能力是轻量编排层，适合“用多 Agent 熟悉旧项目”“full 模式审查插件架构”“多专家排查打包失败风险”这类复杂请求。它会先给出 Coordinator、Project Explorer、Architecture Reviewer、C++ Implementer、Blueprint Integrator、Verifier 等角色分工、文件所有权边界、并行发现结果和后续应进入的具体技能；普通单点问题仍会直接路由到对应技能。

> 自动打包能力只在用户明确提出“打包 / 自动打包 / 一键打包 / RunUAT / BuildCookRun / CI 打包 / 发版流水线”等请求时使用。普通性能检查、发布前检查或打包失败诊断仍由 `ue-performance-packaging` 处理，不会被动触发打包。

## Agent 编排说明

`ue-multi-agent-workflow` 目前提供 **13 个角色位**，但不会每次全部启用。它默认把多 Agent 当成复杂任务的协调协议，而不是简单任务的固定流程。

核心角色：

| Agent 角色 | 负责内容 |
|------|------|
| Coordinator | 范围、分工、依赖顺序、冲突处理和最终汇总 |
| Project Explorer | 旧项目/现有项目的只读结构侦察 |
| UE Architecture Reviewer | 模块边界、Runtime/Editor 拆分、Blueprint/C++ 所有权 |
| C++ Implementer | C++ API、反射暴露、UObject 生命周期和编译风险 |
| Blueprint Integrator | 蓝图节点、pin 连接、默认值、资产交接和设计师实现步骤 |
| Verifier | 构建、蓝图编译、PIE、自动化测试、日志证据和完成判断 |

可选专项角色：

| Agent 角色 | 触发场景 |
|------|------|
| GAS/Networking | GAS、RPC、复制、预测、多人 PIE |
| UI/UMG | Widget Blueprint、CommonUI、HUD、输入模式、DPI |
| Enhanced Input | Input Action、Mapping Context、重绑定、UI 焦点 |
| AI/Animation | Behavior Tree、EQS、StateTree、动画蓝图、蒙太奇 |
| Render/VFX | 材质、Niagara、后处理、shader、视觉性能 |
| Packaging/Release | 打包风险、发布准备、Project Launcher、CI 发布关注点 |
| Log/Crash Triage | UBT/UHT/UAT、`Saved/Logs`、callstack、ensure/assert |

模式选择：

| 模式 | 用法 |
|------|------|
| `solo` | 简单单域任务，直接回到具体技能，不输出多 Agent 报告 |
| `lean` | 默认复杂任务，通常启用 Coordinator + 1-2 个专项角色 |
| `full` | 旧项目深度接手、插件架构审查、跨 C++/蓝图/UI/资产/测试/发布风险的大任务 |

为避免简单任务变重，下面这些场景不会默认启用多 Agent：单个 Enhanced Input 事件不触发、一个 `BlueprintCallable` 方法的蓝图接法、蓝图单点连线、单条 `RunUAT` 命令生成、普通解释性问题。多 Agent 参考协议位于 `skills/ue-multi-agent-workflow/references/`，包括角色职责、统一输出模板和冲突处理规则，仅在 `lean` 或 `full` 模式按需读取。

## 内置工具

| 工具 | 路径 | 用途 |
|------|------|------|
| `ue-project-scan` | `skills/ue-project-onboarding/scripts/ue_project_scan.py` | 只读扫描 `.uproject`、模块、插件、源码文件、Build 文件和常见资产文件名 |
| `ue-config-audit` | `skills/ue-project-onboarding/scripts/ue_config_audit.py` | 只读审计 `Config/*.ini`、默认地图、Enhanced Input、Maps to Cook 和 editor-only 配置风险 |
| `ue-log-triage` | `skills/ue-log-crash-triage/scripts/ue_log_triage.py` | 从 UE 日志中提取首个可行动错误、失败阶段、证据和下一步技能 |
| `ue-editor-command-report` | `skills/ue-debug-validation/scripts/ue_editor_command_report.py` | 只生成 DataValidation、CompileAllBlueprints、MapCheck 等 Unreal Editor commandlet 命令，不直接启动编辑器 |
| `ue-blueprint-api-report` | `skills/ue-cpp-gameplay/scripts/ue_blueprint_api_report.py` | 扫描 `BlueprintCallable`、`BlueprintPure`、蓝图事件和可绑定属性，生成蓝图接法提示 |
| `ue-dependency-graph` | `skills/ue-architecture/scripts/ue_dependency_graph.py` | 解析 `.Build.cs` 模块依赖、循环依赖、Runtime→Editor 风险，并可输出 Mermaid 图 |
| `ue-agent-plan` | `skills/ue-multi-agent-workflow/scripts/ue_agent_plan.py` | 根据用户请求生成 `solo` / `lean` / `full` 角色分工、所有权边界和后续技能 |

示例：

```powershell
python skills\ue-project-onboarding\scripts\ue_project_scan.py --project F:\UEObject\MyGame --format json
python skills\ue-project-onboarding\scripts\ue_config_audit.py --project F:\UEObject\MyGame --format json
python skills\ue-log-crash-triage\scripts\ue_log_triage.py --log F:\UEObject\MyGame\Saved\Logs\MyGame.log --format json
python skills\ue-debug-validation\scripts\ue_editor_command_report.py --project F:\UEObject\MyGame\MyGame.uproject --engine-cmd C:\UE\UE_5.6\Engine\Binaries\Win64\UnrealEditor-Cmd.exe --format json
python skills\ue-cpp-gameplay\scripts\ue_blueprint_api_report.py --project F:\UEObject\MyGame --format json
python skills\ue-architecture\scripts\ue_dependency_graph.py --project F:\UEObject\MyGame --format mermaid
python skills\ue-multi-agent-workflow\scripts\ue_agent_plan.py --request "用多 Agent 熟悉这个旧 UE 项目，准备二开" --format json
```

## 目录结构

```text
ue-game-dev/
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── assets/
│   ├── UE_Logo_Black_Centered.svg.png
│   └── ue-game-dev.svg
├── skills/
│   ├── ue-game-dev-router/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── ue-project-onboarding/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   ├── ue-cpp-gameplay/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   └── ...
├── plugins/
│   └── ue-game-dev/
│       ├── .codex-plugin/
│       ├── assets/
│       ├── rules/
│       ├── skills/
│       └── templates/
├── scripts/
│   ├── sync_marketplace_package.py
│   └── validate_plugin.py
├── templates/
│   ├── ue-task.md
│   └── ue-test-evidence.md
├── rules/
│   ├── ue-cpp.md
│   ├── ue-blueprint.md
│   ├── ue-networking.md
│   ├── ue-assets.md
│   └── ue-packaging.md
├── tests/
│   └── route_scenarios.json
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## 每个技能的结构

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── checklist.md
    └── templates.md
```

## 自检

修改插件后可以运行：

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

`sync_marketplace_package.py` 会把根目录插件同步到 `plugins/ue-game-dev/` 市场安装包。`validate_plugin.py` 会检查 `plugin.json`、技能 frontmatter、`agents/openai.yaml`、README 技能数量、共享模板/规则文件、路由场景、marketplace 清单、市场包内容哈希一致性，以及自动打包技能必须保持显式调用。

如果要把当前工作区内容同步到本机 Codex App 插件缓存，可以运行：

```powershell
python scripts\update_codex_app_plugin.py
```

该脚本会刷新 `+codex.<timestamp>` 版本后缀、同步 marketplace 包、运行校验，并通过 Codex CLI 重新安装 `ue-game-dev@zhaochengv-ue`。只想更新文件、不重装 App 插件时可加 `--skip-reinstall`。

## 工作流工件

- `templates/ue-task.md`：用于保存 UE 单个功能/修复任务的目标、范围、实现计划和验收条件。
- `templates/ue-test-evidence.md`：用于记录构建、蓝图编译、PIE、自动化测试、多人验证和打包风险证据。
- `Saved/CodexWorkflow/`：推荐用于 UE 项目内的 AI 可读项目记忆，例如 `project-context.md`、`module-map.md`、`asset-index.md`、`decisions.md`、`known-risks.md` 和 `active-task.md`。
- `rules/`：集中存放 UE C++、蓝图、网络、资产、命名、性能和打包规则，供 router、领域技能和自检脚本引用。
- `tests/route_scenarios.json`：记录典型用户请求应路由到哪个技能，防止自动打包等边界被误改。
- `CONTRIBUTING.md`：记录新增技能、修改路由、扩展工具、marketplace 同步和中文分支同步流程。
- `docs/architecture.md`：用 Mermaid 描述 Router 硬规则和领域加权评分 fallback 的整体结构。

## 许可证

[MIT](LICENSE)

## Attribution

- This plugin includes rewritten and workflow-adapted Unreal Engine API accuracy guidance inspired by `quodsoler/unreal-engine-skills`, copyright (c) 2025 quodsoler, licensed under MIT.
