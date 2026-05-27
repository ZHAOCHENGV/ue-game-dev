# UE Game Dev 贡献指南

## 开发流程

1. 主版本在 `main` 分支开发。
2. 根目录插件文件是唯一源头，不要优先手改 `plugins/ue-game-dev/`。
3. 修改后运行 `python scripts\sync_marketplace_package.py` 刷新 marketplace 安装包。
4. 提交前运行：

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

5. 任何插件内容改动都要同步到 `ue-game-dev-zh`。中文分支保留代码、命令、路径、UE API、技能名和 `$ue-*` 引用英文不变，技能说明、注释、解释和文档正文使用中文。

## 新增技能

- 创建 `skills/<skill-name>/SKILL.md`、`skills/<skill-name>/agents/openai.yaml`，并至少提供一个有用的 `references/*.md`。
- `SKILL.md` frontmatter 必须包含 `name` 和 `description`。
- 在 `skills/ue-game-dev-router/SKILL.md` 增加路由说明。
- 在 `tests/route_scenarios.json` 增加对应路由场景。
- 对外能力变化时同步更新 `.codex-plugin/plugin.json`、`README.md` 和 `CHANGELOG.md`。

## 修改路由

- `scripts/validate_plugin.py` 中硬规则必须优先于评分规则：multi-agent、显式打包、打包失败分诊、workflow state、stage、brief、plan、done。
- 先写路由场景，再向 `SKILL_PATTERNS` 添加领域关键词。
- 用户常见输入可能中英混合时，同时补中英文场景。
- 保留 `$ue-build-release-automation` 的 forbidden 场景，避免被动触发自动打包。

## 新增工具

- 工具默认只读，除非计划明确要求写入。
- 输入路径要显式，例如 `--project` 或 `--log`。
- 支持 `--format json`，方便测试和自动化。
- 同步加入 `UE_TOOL_SCRIPTS`、`validate_tool_mentions()`、README 和拥有该工具的 SKILL。
- 在 `tests/` 下补单元测试。

## Marketplace 包

- 不要先编辑 `plugins/ue-game-dev/`。
- 修改根目录后运行 `scripts\sync_marketplace_package.py`。
- `validate_plugin.py` 会对 `.codex-plugin/`、`assets/`、`rules/`、`skills/`、`templates/`、`CHANGELOG.md`、`LICENSE` 和 `README.md` 做内容哈希比对。

## 提交信息

- 用户偏好详细中文提交日志。
- 提交信息应说明主要能力、验证命令，以及是否已同步 `ue-game-dev-zh`。
