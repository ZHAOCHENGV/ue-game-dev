import argparse
import json
import re
from pathlib import Path


EDITOR_MODULES = {
    "UnrealEd",
    "Blutility",
    "EditorFramework",
    "EditorStyle",
    "KismetCompiler",
    "AssetTools",
    "LevelEditor",
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


def read_uproject(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path} invalid JSON: {exc}") from exc


def parse_array(text: str, name: str) -> list[str]:
    modules: list[str] = []
    pattern = re.compile(rf"{name}\.AddRange\(\s*new\s+string\[\]\s*\{{(.*?)\}}\s*\)", re.S)
    for body in pattern.findall(text):
        modules.extend(re.findall(r'"([^"]+)"', body))
    single_pattern = re.compile(rf"{name}\.Add\(\s*\"([^\"]+)\"\s*\)")
    modules.extend(single_pattern.findall(text))
    return sorted(dict.fromkeys(modules))


def parse_build_file(path: Path, root: Path, module_types: dict[str, str]) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    module = path.name.removesuffix(".Build.cs")
    public = parse_array(text, "PublicDependencyModuleNames")
    private = parse_array(text, "PrivateDependencyModuleNames")
    return {
        "module": module,
        "type": module_types.get(module, "Unknown"),
        "file": str(path.relative_to(root)).replace("\\", "/"),
        "public_dependencies": public,
        "private_dependencies": private,
        "all_dependencies": sorted(dict.fromkeys(public + private)),
    }


def detect_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    visiting: list[str] = []
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            cycle = visiting[visiting.index(node) :] + [node]
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if node in visited:
            return
        visiting.append(node)
        for dep in graph.get(node, []):
            if dep in graph:
                visit(dep)
        visiting.pop()
        visited.add(node)

    for node in graph:
        visit(node)
    return cycles


def dependency_depth(module: str, graph: dict[str, list[str]], seen: set[str] | None = None) -> int:
    seen = seen or set()
    if module in seen:
        return 0
    seen.add(module)
    deps = [dep for dep in graph.get(module, []) if dep in graph]
    if not deps:
        return 0
    return 1 + max(dependency_depth(dep, graph, set(seen)) for dep in deps)


def analyze(project: Path) -> dict:
    uproject_path = find_uproject(project)
    root = uproject_path.parent
    uproject = read_uproject(uproject_path)
    module_types = {entry.get("Name"): entry.get("Type", "Unknown") for entry in uproject.get("Modules", [])}

    modules = [
        parse_build_file(path, root, module_types)
        for path in sorted((root / "Source").rglob("*.Build.cs"))
    ]
    graph = {entry["module"]: entry["all_dependencies"] for entry in modules}
    issues: list[dict] = []

    for entry in modules:
        if entry["type"] == "Runtime":
            for dep in entry["all_dependencies"]:
                if dep in EDITOR_MODULES or dep.endswith("Editor"):
                    issues.append(
                        {
                            "type": "editor_dependency",
                            "module": entry["module"],
                            "dependency": dep,
                            "message": f"Runtime module {entry['module']} depends on editor-only {dep}",
                        }
                    )

    for cycle in detect_cycles(graph):
        issues.append({"type": "cycle", "cycle": cycle, "message": " -> ".join(cycle)})

    return {
        "project": uproject_path.stem,
        "modules": modules,
        "issues": issues,
        "dependency_depth": {module: dependency_depth(module, graph) for module in graph},
        "recommended_next_skills": ["ue-architecture"],
    }


def render_text(result: dict) -> str:
    lines = [f"UE Dependency Graph: {result['project']}"]
    for entry in result["modules"]:
        deps = ", ".join(entry["all_dependencies"]) or "None"
        lines.append(f"- {entry['module']} ({entry['type']}): {deps}")
    for issue in result["issues"]:
        lines.append(f"! {issue['type']}: {issue['message']}")
    return "\n".join(lines)


def render_mermaid(result: dict) -> str:
    lines = ["graph TD"]
    for entry in result["modules"]:
        if not entry["all_dependencies"]:
            lines.append(f"    {entry['module']}")
        for dep in entry["all_dependencies"]:
            lines.append(f"    {entry['module']} --> {dep}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Unreal Build.cs dependency graph helper.")
    parser.add_argument("--project", required=True, help="Path to a UE project directory or .uproject file.")
    parser.add_argument("--format", choices=["json", "text", "mermaid"], default="text")
    args = parser.parse_args()

    result = analyze(Path(args.project))
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.format == "mermaid":
        print(render_mermaid(result))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
