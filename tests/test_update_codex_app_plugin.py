import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import scripts.update_codex_app_plugin as update_codex_app_plugin


class UpdateCodexAppPluginTests(unittest.TestCase):
    def test_resolve_codex_home_uses_explicit_path(self) -> None:
        self.assertEqual(
            update_codex_app_plugin.resolve_codex_home("C:/Users/zhaocw/.codex"),
            Path("C:/Users/zhaocw/.codex").resolve(),
        )

    def test_resolve_codex_home_prefers_desktop_home_from_sandbox(self) -> None:
        with mock.patch.dict(update_codex_app_plugin.os.environ, {}, clear=True), mock.patch.object(
            update_codex_app_plugin.Path,
            "home",
            return_value=Path("C:/Users/CodexSandboxOffline"),
        ), mock.patch.object(
            update_codex_app_plugin,
            "find_desktop_codex_home",
            return_value=Path("C:/Users/zhaocw/.codex"),
        ):
            self.assertEqual(
                update_codex_app_plugin.resolve_codex_home(None),
                Path("C:/Users/zhaocw/.codex"),
            )

    def test_cachebuster_rewrites_build_metadata_only(self) -> None:
        self.assertEqual(
            update_codex_app_plugin.with_cachebuster("0.14.0+codex.old", "abc123"),
            "0.14.0+codex.abc123",
        )
        self.assertEqual(update_codex_app_plugin.sanitize_cachebuster("  My Build_01  "), "my-build-01")

    def test_update_cachebuster_preserves_manifest_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "plugin.json"
            manifest.write_text(
                json.dumps({"name": "ue-game-dev", "version": "0.14.0", "skills": "./skills/"}),
                encoding="utf-8",
            )

            update_codex_app_plugin.update_cachebuster(manifest, "test")

            payload = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(payload["version"], "0.14.0+codex.test")
            self.assertEqual(payload["name"], "ue-game-dev")

    def test_parse_marketplace_root_finds_zhaochengv_entry(self) -> None:
        output = "MARKETPLACE  ROOT\nzhaochengv-ue  C:/tmp/ue-game-dev\nother  C:/other\n"
        self.assertEqual(
            update_codex_app_plugin.parse_marketplace_root(output),
            Path("C:/tmp/ue-game-dev"),
        )


if __name__ == "__main__":
    unittest.main()
