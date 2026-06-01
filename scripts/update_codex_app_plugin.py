#!/usr/bin/env python3
"""Sync and reinstall the local UE Game Dev plugin into Codex App."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "ue-game-dev"
MARKETPLACE_NAME = "zhaochengv-ue"
ROOT_MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
PACKAGE_ROOT = ROOT / "plugins" / PLUGIN_NAME


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Update the plugin cachebuster, sync plugins/ue-game-dev, validate the package, "
            "and reinstall it into the Codex App plugin cache."
        )
    )
    parser.add_argument(
        "--codex-home",
        help=(
            "Codex home directory that owns config.toml. Defaults to CODEX_HOME, or the "
            "desktop user's ~/.codex when run from the Codex sandbox."
        ),
    )
    parser.add_argument(
        "--codex-cli",
        default=os.environ.get("CODEX_CLI_PATH"),
        help="Path to codex.exe. Defaults to CODEX_CLI_PATH, config.toml, or PATH discovery.",
    )
    parser.add_argument(
        "--cachebuster",
        help="Cachebuster token to append as +codex.<token>. Defaults to a UTC timestamp.",
    )
    parser.add_argument(
        "--skip-cachebuster",
        action="store_true",
        help="Do not rewrite plugin.json version before syncing.",
    )
    parser.add_argument(
        "--skip-reinstall",
        action="store_true",
        help="Only update/sync/validate local files; do not call Codex CLI.",
    )
    parser.add_argument(
        "--replace-marketplace",
        action="store_true",
        help="If zhaochengv-ue points at another local root, remove and re-add it.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print version, target Codex home, and package file count without changing files or reinstalling.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    codex_home = resolve_codex_home(args.codex_home)

    if args.dry_run:
        manifest = load_json(ROOT_MANIFEST)
        destination = codex_home / "plugins" / "cache" / MARKETPLACE_NAME / PLUGIN_NAME
        package_files = [path for path in PACKAGE_ROOT.rglob("*") if path.is_file()] if PACKAGE_ROOT.exists() else []
        print(f"Dry run for {PLUGIN_NAME}@{MARKETPLACE_NAME}", flush=True)
        print(f"- Source version: {manifest.get('version', 'Unknown')}", flush=True)
        print(f"- Source package: {PACKAGE_ROOT}", flush=True)
        print(f"- Destination root: {destination}", flush=True)
        print(f"- Files that would be copied: {len(package_files)}", flush=True)
        print("- No files changed.", flush=True)
        return

    if not args.skip_cachebuster:
        update_cachebuster(ROOT_MANIFEST, args.cachebuster or default_cachebuster())

    run([sys.executable, str(ROOT / "scripts" / "sync_marketplace_package.py")])
    run([sys.executable, str(ROOT / "scripts" / "validate_plugin.py")])

    if args.skip_reinstall:
        print("Skipped Codex App reinstall.", flush=True)
        return

    codex_cli = resolve_codex_cli(args.codex_cli, codex_home)
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)

    ensure_marketplace(codex_cli, env, args.replace_marketplace)
    run([str(codex_cli), "plugin", "add", f"{PLUGIN_NAME}@{MARKETPLACE_NAME}"], env=env)
    print(f"Installed {PLUGIN_NAME}@{MARKETPLACE_NAME} into {codex_home}", flush=True)


def update_cachebuster(manifest_path: Path, cachebuster: str) -> None:
    manifest = load_json(manifest_path)
    version = manifest.get("version")
    if not isinstance(version, str) or not version.strip():
        raise ValueError(f"{manifest_path} must contain a non-empty string version.")

    next_version = with_cachebuster(version, sanitize_cachebuster(cachebuster))
    manifest["version"] = next_version
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Updated plugin version: {version} -> {next_version}", flush=True)


def resolve_codex_home(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()

    env_home = os.environ.get("CODEX_HOME")
    if env_home:
        return Path(env_home).expanduser().resolve()

    home = Path.home()
    if home.name.casefold() != "codexsandboxoffline":
        return (home / ".codex").resolve()

    desktop_home = find_desktop_codex_home()
    if desktop_home:
        return desktop_home

    return (home / ".codex").resolve()


def find_desktop_codex_home() -> Path | None:
    users_root = Path("C:/Users")
    if not users_root.exists():
        return None

    for config_path in sorted(users_root.glob("*/.codex/config.toml")):
        if config_path.parts[-3].casefold() == "codexsandboxoffline":
            continue
        try:
            config = tomllib.loads(config_path.read_text(encoding="utf-8"))
        except OSError:
            continue
        except tomllib.TOMLDecodeError:
            continue

        node_env = (
            config.get("mcp_servers", {})
            .get("node_repl", {})
            .get("env", {})
        )
        if isinstance(node_env.get("CODEX_CLI_PATH"), str):
            return config_path.parent.resolve()

    return None


def load_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object.")
    return payload


def default_cachebuster() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


def sanitize_cachebuster(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9-]+", "-", value.strip().lower())
    sanitized = re.sub(r"-{2,}", "-", sanitized).strip("-")
    if not sanitized:
        raise ValueError("Cachebuster must contain at least one letter or digit.")
    return sanitized


def with_cachebuster(version: str, cachebuster: str) -> str:
    return f"{version.split('+', 1)[0]}+codex.{cachebuster}"


def resolve_codex_cli(explicit: str | None, codex_home: Path) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())

    candidates.extend(read_codex_cli_from_config(codex_home))

    which = shutil.which("codex")
    if which:
        candidates.append(Path(which))

    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()

    raise FileNotFoundError(
        "Could not find Codex CLI. Pass --codex-cli or set CODEX_CLI_PATH."
    )


def read_codex_cli_from_config(codex_home: Path) -> list[Path]:
    config_path = codex_home / "config.toml"
    if not config_path.is_file():
        return []

    config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    node_env = (
        config.get("mcp_servers", {})
        .get("node_repl", {})
        .get("env", {})
    )
    cli_path = node_env.get("CODEX_CLI_PATH")
    return [Path(cli_path)] if isinstance(cli_path, str) else []


def ensure_marketplace(codex_cli: Path, env: dict[str, str], replace_marketplace: bool) -> None:
    list_result = run(
        [str(codex_cli), "plugin", "marketplace", "list"],
        env=env,
        capture=True,
    )
    configured_root = parse_marketplace_root(list_result.stdout)
    current_root = normalize_path(ROOT)

    if configured_root is None:
        run([str(codex_cli), "plugin", "marketplace", "add", str(ROOT)], env=env)
        return

    if normalize_path(configured_root) == current_root:
        print(f"Marketplace {MARKETPLACE_NAME} already points at {ROOT}", flush=True)
        return

    if not replace_marketplace:
        raise RuntimeError(
            f"Marketplace {MARKETPLACE_NAME} points at {configured_root}, not {ROOT}. "
            "Re-run with --replace-marketplace if you want this script to switch it."
        )

    run([str(codex_cli), "plugin", "marketplace", "remove", MARKETPLACE_NAME], env=env)
    run([str(codex_cli), "plugin", "marketplace", "add", str(ROOT)], env=env)


def parse_marketplace_root(output: str) -> Path | None:
    for line in output.splitlines():
        stripped = line.strip()
        if not stripped or stripped.upper().startswith("MARKETPLACE"):
            continue
        parts = re.split(r"\s{2,}", stripped, maxsplit=1)
        if len(parts) == 2 and parts[0] == MARKETPLACE_NAME:
            return Path(parts[1])
    return None


def normalize_path(path: Path) -> str:
    return str(path.expanduser().resolve()).casefold()


def run(
    command: list[str],
    *,
    env: dict[str, str] | None = None,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    print("> " + " ".join(command), flush=True)
    return subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=True,
        text=True,
        capture_output=capture,
    )


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as err:
        print(f"Command failed with exit code {err.returncode}: {' '.join(err.cmd)}", file=sys.stderr)
        if err.stdout:
            print(err.stdout, file=sys.stderr)
        if err.stderr:
            print(err.stderr, file=sys.stderr)
        raise SystemExit(err.returncode) from err
    except Exception as err:  # noqa: BLE001 - CLI script should print concise failures.
        print(str(err), file=sys.stderr)
        raise SystemExit(1) from err
