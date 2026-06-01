import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

import scripts.validate_plugin as validate_plugin


class ValidatePluginTests(unittest.TestCase):
    def test_user_visible_text_rejects_mojibake(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            manifest = root / ".codex-plugin" / "plugin.json"
            scenarios = root / "tests" / "route_scenarios.json"
            skill = root / "skills" / "ue-game-dev-router" / "SKILL.md"
            manifest.parent.mkdir(parents=True)
            scenarios.parent.mkdir(parents=True)
            skill.parent.mkdir(parents=True)
            (root / "README.md").write_text("鍏堢啛鎮夎繖涓棫 UE 项目\n", encoding="utf-8")
            manifest.write_text(
                '{"interface":{"defaultPrompt":["@ue-game-dev 为项目建立 Saved/CodexWorkflow 项目记忆"]}}',
                encoding="utf-8",
            )
            scenarios.write_text("[]", encoding="utf-8")
            skill.write_text("---\nname: ue-game-dev-router\ndescription: test\n---\n", encoding="utf-8")

            with mock.patch.object(validate_plugin, "ROOT", root), mock.patch.object(
                validate_plugin, "README", root / "README.md"
            ), mock.patch.object(
                validate_plugin, "PLUGIN_JSON", manifest
            ), mock.patch.object(
                validate_plugin, "ROUTE_SCENARIOS", scenarios
            ), mock.patch.object(
                validate_plugin, "ROUTER_SKILL", skill
            ):
                with redirect_stdout(StringIO()):
                    with self.assertRaises(SystemExit):
                        validate_plugin.validate_user_visible_text()

    def test_route_prompt_keeps_packaging_and_multi_agent_hard_rules(self) -> None:
        cases = {
            "用多 Agent 排查打包失败，查看 Saved/Logs 和 Build.cs": "ue-multi-agent-workflow",
            "分析这个 RunUAT 打包失败日志，找出第一个错误": "ue-log-crash-triage",
            "给这个项目生成 Win64 Development 的 RunUAT BuildCookRun 打包命令": "ue-build-release-automation",
            "检查这个项目是否已经准备好打包发布": "ue-performance-packaging",
        }

        for prompt, expected in cases.items():
            with self.subTest(prompt=prompt):
                self.assertEqual(validate_plugin.route_prompt(prompt), expected)

    def test_route_prompt_covers_common_chinese_domain_prompts(self) -> None:
        cases = {
            "帮我做一个粒子特效": "ue-render-vfx",
            "角色动画状态机怎么设计": "ue-animation",
            "帮我做存档和读档": "ue-save-load-sync",
            "行为树巡逻怎么实现": "ue-ai-navigation",
            "调试断点排查这个问题": "ue-debug-validation",
            "帮我做一个背包UI": "ue-client-ui",
            "做一个拾取物品的交互系统": "ue-world-interaction",
            "写几个自动化测试验证这个功能": "ue-testing-automation",
            "帮我分析模块划分和解耦方案": "ue-architecture",
            "帮我做一个编辑器工具面板": "ue-editor-tooling-slate",
            "帮我创建一个 Runtime + Editor 双模块插件": "ue-plugin-module-dev",
            "帮我配一个空间化的音效": "ue-audio",
            "帮我做一个异步蓝图节点": "ue-async-systems",
            "帮我做按键绑定和重绑定": "ue-input-enhanced",
        }

        for prompt, expected in cases.items():
            with self.subTest(prompt=prompt):
                self.assertEqual(validate_plugin.route_prompt(prompt), expected)

    def test_route_prompt_supports_new_skill_domains(self) -> None:
        self.assertEqual(validate_plugin.route_prompt("帮我做一个布娃娃物理效果"), "ue-physics-destruction")
        self.assertEqual(validate_plugin.route_prompt("帮我用 DataTable 管理物品数据"), "ue-data-management")
        cases = {
            "Design a Game Feature Plugin with ModularGameplay and Lyra Experience actions": "ue-game-features",
            "帮我做一个模块化 Game Feature 插件，接入 Lyra Experience": "ue-game-features",
            "Implement Mass Entity crowd agents with MassProcessor and MassFragment": "ue-mass-entity",
            "帮我用 Mass Entity 做一群 NPC 群体 AI": "ue-mass-entity",
            "Create a PCG graph and runtime procedural generation system": "ue-procedural-generation",
            "帮我做 PCG 程序化生成地形和植被": "ue-procedural-generation",
            "Implement StateTree tasks and transitions for NPC combat": "ue-state-trees",
            "帮我用 StateTree 状态树做敌人战斗逻辑": "ue-state-trees",
            "Create a Sequencer cutscene and Movie Render Queue pipeline": "ue-sequencer-cinematics",
            "帮我做 Sequencer 过场动画和 Movie Render Queue 输出": "ue-sequencer-cinematics",
            "Tune CharacterMovementComponent network prediction and custom movement mode": "ue-character-movement",
            "帮我调 CharacterMovementComponent 角色移动和网络预测": "ue-character-movement",
            "Build a Lyra-style Game Feature plugin with GAS ability grants": "ue-game-features",
        }

        for prompt, expected in cases.items():
            with self.subTest(prompt=prompt):
                self.assertEqual(validate_plugin.route_prompt(prompt), expected)

    def test_marketplace_hash_mismatch_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            package = root / "plugins" / "ue-game-dev"
            for directory in [".codex-plugin", "assets", "rules", "skills", "templates"]:
                (root / directory).mkdir(parents=True)
                (package / directory).mkdir(parents=True)
                (root / directory / "same.txt").write_text("root\n", encoding="utf-8")
                (package / directory / "same.txt").write_text("root\n", encoding="utf-8")
            (root / "README.md").write_text("root readme\n", encoding="utf-8")
            (package / "README.md").write_text("mirror readme\n", encoding="utf-8")

            with mock.patch.object(validate_plugin, "ROOT", root), mock.patch.object(
                validate_plugin, "MARKETPLACE_PACKAGE", package
            ):
                with redirect_stdout(StringIO()):
                    with self.assertRaises(SystemExit):
                        validate_plugin.validate_marketplace_content_sync()

    def test_route_prompt_supports_mattpocock_flow_handoffs(self) -> None:
        cases = {
            "诊断这个 UE 运行时 bug，先建立稳定复现再排查": "ue-debug-validation",
            "分析这个 Saved/Logs 崩溃日志，然后进入 diagnose 闭环继续定位": "ue-log-crash-triage",
            "用 TDD 给这个 UE 背包功能补测试和实现计划": "ue-testing-automation",
            "这个老 UE 项目模块太乱，帮我做 improve-codebase-architecture 架构复盘": "ue-architecture",
            "需求有点模糊，先按 grill-with-docs 的方式追问并整理 UE 功能简报": "ue-feature-brief",
        }

        for prompt, expected in cases.items():
            with self.subTest(prompt=prompt):
                self.assertEqual(validate_plugin.route_prompt(prompt), expected)

    def test_router_documents_mattpocock_flow_handoffs(self) -> None:
        router = validate_plugin.read_text(validate_plugin.ROUTER_SKILL)
        for token in ["diagnose", "tdd", "grill-with-docs", "improve-codebase-architecture"]:
            with self.subTest(token=token):
                self.assertIn(token, router)

    def test_changelog_version_accepts_codex_cachebuster(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            manifest = root / ".codex-plugin" / "plugin.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                '{"name":"ue-game-dev","version":"0.14.1+codex.20260601000000"}',
                encoding="utf-8",
            )
            (root / "CHANGELOG.md").write_text("## [0.14.1]\n\n- Test\n", encoding="utf-8")

            with mock.patch.object(validate_plugin, "ROOT", root), mock.patch.object(
                validate_plugin, "PLUGIN_JSON", manifest
            ):
                validate_plugin.validate_changelog_version()


if __name__ == "__main__":
    unittest.main()
