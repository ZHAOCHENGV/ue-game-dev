#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def quote(value: str) -> str:
    return f'"{value}"' if " " in value else value


def report(project: Path, engine_cmd: str) -> dict:
    project_arg = quote(str(project))
    editor = quote(engine_cmd)
    return {
        "tool": "ue-editor-command-report",
        "read_only": True,
        "project": str(project),
        "commands": {
            "data_validation": f"{editor} {project_arg} -run=DataValidation -unattended -nop4 -log",
            "blueprint_compile": f"{editor} {project_arg} -run=CompileAllBlueprints -unattended -nop4 -log",
            "map_check": f"{editor} {project_arg} -run=MapCheck -unattended -nop4 -log",
        },
        "safety": "Do not run without user approval; these commands launch Unreal Editor commandlets and may write logs/intermediate files.",
        "recommended_next_skill": "ue-debug-validation",
    }


def render_text(result: dict) -> str:
    lines = ["UE Editor Command Report"]
    for name, command in result["commands"].items():
        lines.append(f"- {name}: {command}")
    lines.append(f"- Safety: {result['safety']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate safe Unreal Editor commandlet report commands.")
    parser.add_argument("--project", required=True)
    parser.add_argument("--engine-cmd", required=True)
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    result = report(Path(args.project), args.engine_cmd)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
