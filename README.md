# UE Game Dev — Codex Plugin

面向 Unreal Engine 游戏与客户端开发的 Codex 技能插件。通过 Router + 领域技能的分层架构，为 UE 开发的各个环节提供专业化的工作流指导。

## 功能概览

本插件包含 **1 个路由技能 + 15 个领域技能**，覆盖 UE 开发全链路：

| 技能 | 领域 |
|------|------|
| `ue-game-dev-router` | 🔀 请求路由与分发 |
| `ue-cpp-gameplay` | 🎮 C++ 游戏逻辑（Actor、Component、Subsystem） |
| `ue-blueprint-workflow` | 📊 蓝图工作流（事件图、函数图、Widget） |
| `ue-plugin-module-dev` | 🔌 插件与模块开发（.uplugin、Build.cs、命名规范） |
| `ue-editor-tooling-slate` | 🛠️ 编辑器工具与 Slate UI |
| `ue-architecture` | 🏗️ 架构设计与模块边界 |
| `ue-gas-networking` | ⚔️ GAS 技能系统与网络同步 |
| `ue-save-load-sync` | 💾 存档/加载与状态同步 |
| `ue-world-interaction` | 🌍 世界交互（拾取、生成器、碰撞） |
| `ue-render-vfx` | 🎨 渲染、材质与 Niagara 特效 |
| `ue-client-ui` | 🖥️ 客户端 UI（UMG、CommonUI、HUD） |
| `ue-debug-validation` | 🔍 调试与验证 |
| `ue-performance-packaging` | 📦 性能分析与打包发布 |
| `ue-ai-navigation` | 🤖 AI 行为树、EQS、导航系统 |
| `ue-animation` | 🏃 动画蓝图、蒙太奇、IK、状态机 |
| `ue-testing-automation` | ✅ 自动化测试、功能测试、PIE/多人验证、资产校验 |

## 工作原理

```
用户请求 → ue-game-dev-router（路由分析）→ 最匹配的领域技能
                                           ↓
                                    专业化的规则、检查清单和参考文档
```

1. **路由器**接收用户请求，分析所涉及的 UE 领域
2. **分发**到最匹配的领域技能（如 C++ 游戏逻辑 → `ue-cpp-gameplay`）
3. 领域技能提供**专业化的工作流规则**和**参考文档检查清单**
4. 跨领域任务会**按优先级链式调用**多个技能

## 目录结构

```
ue-game-dev/
├── .codex-plugin/
│   └── plugin.json          # 插件元数据
├── assets/
│   └── ue-game-dev.svg      # 插件图标
├── skills/
│   ├── ue-game-dev-router/  # 路由技能
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── ue-cpp-gameplay/     # 领域技能示例
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   │       ├── cpp-patterns.md
│   │       ├── blueprint-api.md
│   │       └── validation.md
│   └── ...                  # 其余 14 个领域技能
├── LICENSE
├── .gitattributes
└── README.md
```

## 每个技能的结构

```
skill-name/
├── SKILL.md              # 技能定义：触发条件、工作流规则、跨技能引用
├── agents/
│   └── openai.yaml       # Agent 接口配置
└── references/           # 参考文档（检查清单、模式、代码模板）
    ├── checklist-1.md
    └── checklist-2.md
```

## 使用方式

在支持 Codex 插件的环境中安装本插件后，可通过以下方式触发：

```
Use UE Game Dev to design this Unreal plugin, module, or editor tool.
Use UE Game Dev to review this GAS and replication flow.
Use UE Game Dev to add tests for this UE feature.
```

## 许可证

[MIT](LICENSE)
