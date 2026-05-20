# UE Game Dev - Codex Plugin

面向 Unreal Engine 游戏与客户端开发的 Codex 技能插件。它不是 Unreal Editor 的 `.uplugin` 插件，不需要放进 UE 项目的 `Plugins/` 目录；它是给 Codex App 使用的 UE 开发工作流插件，用来辅助项目入口判断、需求简报、实施计划、完成验收、旧项目接手、二开前分析、UE C++、蓝图、Enhanced Input、GAS、网络同步、渲染、材质、Niagara、UI、调试、测试和显式打包自动化等开发任务。

## 安装方法

### 方式一：安装到 Codex 本地插件目录

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

### 方式二：开发时使用目录链接

如果你正在本地开发这个插件，不想每次修改后复制文件，可以把插件目录链接到 Codex 本地插件目录：

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\plugins\ue-game-dev" -Target "C:\path\to\ue-game-dev"
```

之后重启 Codex App，Codex 会从链接目录读取最新文件。

## 快速调用

安装并启用后，推荐用最短入口调用：

```text
@ue-game-dev 先熟悉这个旧 UE 项目，后面我要基于它二开
@ue-game-dev 我想做一个 UE 背包系统，先帮我整理需求简报
@ue-game-dev 按这个功能需求写一份 C++/蓝图/资产/测试实施计划
@ue-game-dev 帮我设计一个 UE 编辑器插件
@ue-game-dev 检查这个 GAS 网络同步流程
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

本插件包含 **1 个路由技能 + 22 个领域技能**，覆盖 UE 开发全链路：

| 技能 | 领域 |
|------|------|
| `ue-game-dev-router` | 请求路由与分发 |
| `ue-start` | UE 任务入口判断、阶段识别、下一步路由 |
| `ue-feature-brief` | 功能需求简报、范围澄清、约束整理 |
| `ue-implementation-plan` | C++/蓝图/资产/配置/测试实施计划 |
| `ue-feature-done` | 功能完成验收、验证证据、交接清单 |
| `ue-project-onboarding` | 旧项目接手、项目熟悉、二开前分析 |
| `ue-cpp-gameplay` | C++ 游戏逻辑（Actor、Component、Subsystem） |
| `ue-blueprint-workflow` | 蓝图工作流（事件图、函数图、Widget） |
| `ue-plugin-module-dev` | 插件与模块开发（.uplugin、Build.cs、命名规范） |
| `ue-editor-tooling-slate` | 编辑器工具与 Slate UI |
| `ue-architecture` | 架构设计与模块边界 |
| `ue-input-enhanced` | Enhanced Input（Input Action、Mapping Context、重绑定、UI 焦点） |
| `ue-gas-networking` | GAS 技能系统与网络同步 |
| `ue-save-load-sync` | 存档/加载与状态同步 |
| `ue-world-interaction` | 世界交互（拾取、生成器、碰撞） |
| `ue-render-vfx` | 渲染、材质与 Niagara 特效 |
| `ue-client-ui` | 客户端 UI（UMG、CommonUI、HUD） |
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
2. 路由器先判断阶段：入口判断、需求简报、实施计划、具体实现、调试验证、完成验收或显式打包。
3. 路由器分发到最匹配的领域技能，例如 C++ 游戏逻辑会进入 `ue-cpp-gameplay`。
4. 领域技能提供专业化工作流、检查清单、命名规范和参考模板。
5. 跨领域任务会按优先级组合多个技能，例如功能简报 + C++ 实施计划 + 蓝图交接 + 自动化测试。

> 自动打包能力只在用户明确提出“打包 / 自动打包 / 一键打包 / RunUAT / BuildCookRun / CI 打包 / 发版流水线”等请求时使用。普通性能检查、发布前检查或打包失败诊断仍由 `ue-performance-packaging` 处理，不会被动触发打包。

## 目录结构

```text
ue-game-dev/
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
├── scripts/
│   └── validate_plugin.py
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
python scripts\validate_plugin.py
```

该脚本会检查 `plugin.json`、技能 frontmatter、`agents/openai.yaml`、README 技能数量，以及自动打包技能必须保持显式调用。

## 许可证

[MIT](LICENSE)
