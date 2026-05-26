#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


FUNCTION_KINDS = [
    "BlueprintCallable",
    "BlueprintPure",
    "BlueprintImplementableEvent",
    "BlueprintNativeEvent",
]
PROPERTY_KINDS = ["BlueprintAssignable", "BlueprintReadOnly", "BlueprintReadWrite"]


def display_name(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", " ", name).strip()


def macro_kind(macro: str, kinds: list[str]) -> str | None:
    for kind in kinds:
        if kind in macro:
            return kind
    return None


def category_from_macro(macro: str) -> str:
    match = re.search(r'Category\s*=\s*"([^"]+)"', macro)
    return match.group(1) if match else "Default"


def collect_statement(lines: list[str], start: int) -> str:
    parts = []
    for index in range(start, min(len(lines), start + 8)):
        stripped = lines[index].strip()
        if not stripped:
            continue
        parts.append(stripped)
        if ";" in stripped or "{" in stripped:
            break
    return " ".join(parts)


def module_name_for(path: Path, root: Path) -> str:
    parts = path.relative_to(root).parts
    if len(parts) >= 2 and parts[0] == "Source":
        return parts[1]
    return ""


def parse_file(path: Path, root: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    apis = []
    owner_kind = "UInterface" if any("UINTERFACE" in line for line in lines) else "UObject"
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("UFUNCTION"):
            kind = macro_kind(stripped, FUNCTION_KINDS)
            if not kind:
                continue
            statement = collect_statement(lines, index + 1)
            match = re.search(r"\b([A-Za-z_]\w*)\s*\(", statement)
            if not match:
                continue
            name = match.group(1)
            apis.append(api_entry(name, kind, path, root, category_from_macro(stripped), statement, owner_kind))
        elif stripped.startswith("UPROPERTY"):
            kind = macro_kind(stripped, PROPERTY_KINDS)
            if not kind:
                continue
            statement = collect_statement(lines, index + 1)
            match = re.search(r"\b([A-Za-z_]\w*)\s*;", statement)
            if not match:
                continue
            name = match.group(1)
            apis.append(api_entry(name, kind, path, root, category_from_macro(stripped), statement, owner_kind))
    return apis


def api_entry(name: str, kind: str, path: Path, root: Path, category: str, signature: str, owner_kind: str) -> dict:
    node_name = display_name(name)
    return {
        "name": name,
        "kind": kind,
        "owner_kind": owner_kind,
        "module": module_name_for(path, root),
        "category": category,
        "file": str(path.relative_to(root)).replace("\\", "/"),
        "signature": signature,
        "blueprint_steps": [
            f"Search for {node_name} in the target Blueprint graph.",
            "Connect exec and data pins according to the C++ signature.",
            "Compile the Blueprint and run a PIE smoke check.",
        ],
    }


def report(project: Path, module_filter: str | None = None, interface_only: bool = False) -> dict:
    root = project.resolve()
    source_root = root / "Source"
    apis = []
    for path in sorted(source_root.rglob("*")) if source_root.exists() else []:
        if module_filter and module_name_for(path, root) != module_filter:
            continue
        if path.suffix.lower() in {".h", ".hpp"}:
            apis.extend(parse_file(path, root))
    if interface_only:
        apis = [entry for entry in apis if entry["owner_kind"] == "UInterface"]
    return {
        "tool": "ue-blueprint-api-report",
        "read_only": True,
        "project": str(root),
        "apis": apis,
        "recommended_next_skill": "ue-cpp-gameplay",
    }


def render_text(result: dict) -> str:
    lines = ["UE Blueprint API Report", f"- APIs found: {len(result['apis'])}"]
    for entry in result["apis"]:
        lines.append(f"- {entry['kind']}: {entry['name']} ({entry['file']})")
    lines.append(f"- Recommended next skill: {result['recommended_next_skill']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Report Blueprint-exposed Unreal C++ API.")
    parser.add_argument("--project", required=True, help="Path to a UE project directory.")
    parser.add_argument("--module", help="Only scan the named Source module.")
    parser.add_argument("--interface", action="store_true", help="Only report UInterface Blueprint APIs.")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    result = report(Path(args.project), args.module, args.interface)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
