#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


ASSET_PREFIXES = {
    "InputActions": ("IA_",),
    "InputMappingContexts": ("IMC_",),
    "WidgetBlueprints": ("WBP_", "WB_"),
    "Blueprints": ("BP_",),
    "AnimationBlueprints": ("ABP_",),
    "BehaviorTrees": ("BT_",),
    "Niagara": ("NS_", "NE_"),
    "Materials": ("M_", "MI_", "MF_"),
    "Maps": ("L_",),
}


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


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def classify_assets(content_dir: Path) -> dict[str, list[str]]:
    assets = {key: [] for key in ASSET_PREFIXES}
    if not content_dir.exists():
        return assets

    for path in sorted(content_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".uasset", ".umap"}:
            continue
        name = path.name
        if path.suffix.lower() == ".umap":
            assets["Maps"].append(name)
            continue
        for category, prefixes in ASSET_PREFIXES.items():
            if any(path.stem.startswith(prefix) for prefix in prefixes):
                assets[category].append(name)
                break
    return assets


def module_matches(path: Path, root: Path, module_filter: str | None) -> bool:
    if not module_filter:
        return True
    normalized = path.relative_to(root).parts
    return len(normalized) >= 2 and normalized[0] == "Source" and normalized[1] == module_filter


def scan_project(project: Path, module_filter: str | None = None) -> dict:
    uproject = find_uproject(project)
    root = uproject.parent
    data = read_json(uproject)

    modules = [entry.get("Name", "") for entry in data.get("Modules", []) if entry.get("Name")]
    if module_filter:
        modules = [name for name in modules if name == module_filter]
    enabled_plugins = [
        entry.get("Name", "")
        for entry in data.get("Plugins", [])
        if entry.get("Name") and entry.get("Enabled", False)
    ]
    source_files = []
    build_files = []
    source_root = root / "Source"
    if source_root.exists():
        for path in sorted(source_root.rglob("*")):
            if not path.is_file():
                continue
            if not module_matches(path, root, module_filter):
                continue
            if path.suffix in {".h", ".hpp", ".cpp", ".cs"}:
                source_files.append(path.name)
            if path.name.endswith(".Build.cs") or path.name.endswith(".Target.cs"):
                build_files.append(str(path.relative_to(root)).replace("\\", "/"))

    plugins = []
    plugin_root = root / "Plugins"
    if plugin_root.exists():
        plugins = [str(path.relative_to(root)).replace("\\", "/") for path in sorted(plugin_root.rglob("*.uplugin"))]

    return {
        "tool": "ue-project-scan",
        "read_only": True,
        "project": {
            "name": uproject.stem,
            "root": str(root),
            "uproject": str(uproject),
            "engine_association": data.get("EngineAssociation", "Unknown"),
        },
        "modules": modules,
        "enabled_plugins": enabled_plugins,
        "source_files": source_files,
        "build_files": build_files,
        "plugin_descriptors": plugins,
        "assets": classify_assets(root / "Content"),
        "recommended_next_skills": ["ue-project-onboarding", "ue-workflow-state"],
    }


def render_text(result: dict) -> str:
    lines = [
        "UE Project Scan",
        f"- Project: {result['project']['name']} ({result['project']['engine_association']})",
        f"- Modules: {', '.join(result['modules']) or 'None found'}",
        f"- Enabled plugins: {', '.join(result['enabled_plugins']) or 'None found'}",
        f"- Source files: {len(result['source_files'])}",
        f"- Build files: {len(result['build_files'])}",
    ]
    for category, names in result["assets"].items():
        if names:
            lines.append(f"- {category}: {', '.join(names[:12])}")
    lines.append("- Recommended next skills: " + ", ".join(result["recommended_next_skills"]))
    return "\n".join(lines)


def render_markdown(result: dict) -> str:
    lines = [
        "# UE Project Scan",
        "",
        f"- Project: {result['project']['name']}",
        f"- Engine: {result['project']['engine_association']}",
        f"- Root: {result['project']['root']}",
        f"- Modules: {', '.join(result['modules']) or 'None found'}",
        f"- Enabled plugins: {', '.join(result['enabled_plugins']) or 'None found'}",
        f"- Source files: {len(result['source_files'])}",
        f"- Build files: {len(result['build_files'])}",
    ]
    if result["source_files"]:
        lines.extend(["", "## Source Files", ""])
        lines.extend(f"- {name}" for name in result["source_files"])
    if result["build_files"]:
        lines.extend(["", "## Build Files", ""])
        lines.extend(f"- {name}" for name in result["build_files"])
    lines.extend(["", "## Recommended Next Skills", ""])
    lines.extend(f"- {name}" for name in result["recommended_next_skills"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Unreal project scanner.")
    parser.add_argument("--project", required=True, help="Path to a UE project directory or .uproject file.")
    parser.add_argument("--filter", help="Only include files from the named Source module.")
    parser.add_argument("--format", choices=["json", "text", "markdown"], default="text")
    parser.add_argument("--output-format", choices=["json", "text", "markdown"], help="Alias for --format.")
    args = parser.parse_args()

    output_format = args.output_format or args.format
    result = scan_project(Path(args.project).resolve(), args.filter)
    if output_format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif output_format == "markdown":
        print(render_markdown(result))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
