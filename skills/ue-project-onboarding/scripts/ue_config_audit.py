import argparse
import json
import re
from pathlib import Path


def find_uproject(project: Path) -> Path:
    if project.is_file() and project.suffix == ".uproject":
        return project
    matches = sorted(project.glob("*.uproject"))
    if matches:
        return matches[0]
    matches = sorted(project.rglob("*.uproject"))
    if matches:
        return matches[0]
    raise SystemExit(f"No .uproject found under {project}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


def read_uproject(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path} invalid JSON: {exc}") from exc


def check_default_map(default_engine: str) -> dict:
    match = re.search(r"^GameDefaultMap\s*=\s*(.+)$", default_engine, re.M)
    if match and match.group(1).strip():
        return {"status": "PASS", "message": "DefaultMap configured", "value": match.group(1).strip()}
    return {"status": "FAIL", "message": "GameDefaultMap is not configured"}


def check_enhanced_input(uproject: dict) -> dict:
    plugins = uproject.get("Plugins", [])
    enabled = any(entry.get("Name") == "EnhancedInput" and entry.get("Enabled", True) for entry in plugins)
    if enabled:
        return {"status": "PASS", "message": "EnhancedInput plugin enabled"}
    return {"status": "WARN", "message": "EnhancedInput plugin is not enabled in .uproject"}


def check_maps_to_cook(default_game: str, default_engine: str) -> dict:
    text = default_game + "\n" + default_engine
    maps = re.findall(r"MapsToCook=\(FilePath=\"([^\"]+)\"\)", text)
    if maps:
        return {"status": "PASS", "message": "Maps to Cook configured", "maps": maps}
    return {"status": "WARN", "message": "Maps to Cook is empty or not configured"}


def check_editor_only(default_engine: str, default_game: str) -> dict:
    text = default_engine + "\n" + default_game
    risky = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and ("UnrealEd" in line or "EditorUtility" in line or "/Editor/" in line)
    ]
    if risky:
        return {"status": "WARN", "message": "Editor-only looking settings found", "entries": risky}
    return {"status": "PASS", "message": "No obvious editor-only runtime settings found"}


def audit(project: Path) -> dict:
    uproject_path = find_uproject(project)
    root = uproject_path.parent
    uproject = read_uproject(uproject_path)
    default_engine = read_text(root / "Config" / "DefaultEngine.ini")
    default_game = read_text(root / "Config" / "DefaultGame.ini")

    checks = {
        "default_map": check_default_map(default_engine),
        "enhanced_input": check_enhanced_input(uproject),
        "maps_to_cook": check_maps_to_cook(default_game, default_engine),
        "editor_only_settings": check_editor_only(default_engine, default_game),
    }
    return {
        "project": uproject_path.stem,
        "uproject": str(uproject_path),
        "checks": checks,
        "recommended_next_skills": ["ue-project-onboarding", "ue-performance-packaging"],
    }


def render_text(result: dict) -> str:
    lines = [f"UE Config Audit: {result['project']}"]
    for name, check in result["checks"].items():
        lines.append(f"- {name}: {check['status']} - {check['message']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Unreal Config audit helper.")
    parser.add_argument("--project", required=True, help="Path to a UE project directory or .uproject file.")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    result = audit(Path(args.project))
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
