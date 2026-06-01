import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
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

    def test_dry_run_reports_without_mutating(self) -> None:
        args = type(
            "Args",
            (),
            {
                "codex_home": "C:/Users/zhaocw/.codex",
                "dry_run": True,
                "skip_cachebuster": False,
                "cachebuster": None,
                "skip_reinstall": False,
                "codex_cli": None,
                "replace_marketplace": False,
            },
        )()
        with mock.patch.object(update_codex_app_plugin, "parse_args", return_value=args), mock.patch.object(
            update_codex_app_plugin, "update_cachebuster"
        ) as update_cachebuster, mock.patch.object(update_codex_app_plugin, "run") as run, redirect_stdout(StringIO()) as stdout:
            update_codex_app_plugin.main()

        output = stdout.getvalue()
        self.assertIn("Dry run for ue-game-dev@zhaochengv-ue", output)
        self.assertIn("Source version:", output)
        self.assertIn("Files that would be copied:", output)
        update_cachebuster.assert_not_called()
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
