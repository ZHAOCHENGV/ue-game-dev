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

    def test_dry_run_reports_without_mutating(self) -> None:
        with mock.patch.object(
            update_codex_app_plugin,
            "parse_args",
            return_value=type(
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
            )(),
        ), mock.patch.object(update_codex_app_plugin, "update_cachebuster") as update_cachebuster, mock.patch.object(
            update_codex_app_plugin,
            "run",
        ) as run:
            stdout = StringIO()
            with redirect_stdout(stdout):
                update_codex_app_plugin.main()

        output = stdout.getvalue()
        self.assertIn("Dry run for ue-game-dev@zhaochengv-ue", output)
        self.assertIn("Source version:", output)
        self.assertIn("Files that would be copied:", output)
        update_cachebuster.assert_not_called()
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
