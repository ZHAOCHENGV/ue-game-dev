#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


ACTIONABLE_PATTERNS = [
    re.compile(r"\b(error|fatal error|assertion failed|ensure condition failed|exception_access_violation)\b", re.I),
    re.compile(r"\bLNK\d+|UnrealHeaderTool|Blueprint Runtime Error|Cook failed|PackagingResults\b", re.I),
]


def classify_phase(lines: list[str]) -> str:
    text = "\n".join(lines)
    if re.search(r"Cook failed|LogCook|Cooking", text, re.I):
        return "Cook"
    if re.search(r"UnrealHeaderTool|UHT|generated\.h", text, re.I):
        return "UHT"
    if re.search(r"\bLNK\d+|unresolved external", text, re.I):
        return "Link"
    if re.search(r"RunUAT|BuildCookRun|PackagingResults|AutomationTool", text, re.I):
        return "UAT"
    if re.search(r"Blueprint Runtime Error|Blueprint compile", text, re.I):
        return "Blueprint"
    if re.search(r"Fatal error|Assertion failed|Crash|callstack", text, re.I):
        return "Crash"
    if re.search(r"\berror:", text, re.I):
        return "Build"
    return "Unknown"


def is_summary_noise(line: str) -> bool:
    return bool(re.search(r"AutomationTool exiting|ExitCode=|UnknownCookFailure|BUILD FAILED|ERROR:\s*Cook failed", line, re.I))


def failure_at(lines: list[str], index: int) -> dict:
    line = lines[index]
    start = max(0, index - 2)
    end = min(len(lines), index + 3)
    context = [entry.strip() for entry in lines[start:end] if entry.strip() and entry.strip() != line.strip()]
    return {
        "message": line.strip(),
        "line": index + 1,
        "evidence": [line.strip(), *context],
    }


def find_failures(lines: list[str], top_n: int) -> list[dict]:
    failures = []
    for index, line in enumerate(lines):
        if is_summary_noise(line):
            continue
        if any(pattern.search(line) for pattern in ACTIONABLE_PATTERNS):
            failures.append(failure_at(lines, index))
            if len(failures) >= top_n:
                break
    return failures


def find_first_failure(lines: list[str]) -> tuple[str, list[str]]:
    failures = find_failures(lines, 1)
    if failures:
        return failures[0]["message"], failures[0]["evidence"]
    return "No actionable failure found", []


def triage_log(path: Path, top_n: int = 1) -> dict:
    if not path.exists():
        raise SystemExit(f"Log file not found: {path}")
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    failures = find_failures(lines, max(1, top_n))
    if failures:
        first_failure = failures[0]["message"]
        evidence = failures[0]["evidence"]
    else:
        first_failure = "No actionable failure found"
        evidence = []
    phase = classify_phase(lines)
    return {
        "tool": "ue-log-triage",
        "read_only": True,
        "log_source": str(path),
        "first_actionable_failure": first_failure,
        "failure_phase": phase,
        "evidence": evidence,
        "actionable_failures": failures,
        "probable_root_cause": infer_root_cause(first_failure, phase),
        "recommended_next_skill": "ue-log-crash-triage",
        "packaging_boundary": "review only",
    }


def infer_root_cause(first_failure: str, phase: str) -> str:
    if "Assertion failed" in first_failure:
        return "A runtime/editor assertion is the earliest actionable failure; inspect the referenced source file and state preconditions."
    if phase == "UHT":
        return "Reflection or generated-header error; inspect UCLASS/USTRUCT/UFUNCTION/UPROPERTY declarations near the first failure."
    if phase == "Link":
        return "Linker failure; inspect module dependencies, missing implementation, or export macros."
    if phase == "Cook":
        return "Cook failed after an earlier actionable error; fix the first error before treating the final cook summary as root cause."
    return "Use the first actionable failure as the next investigation point."


def render_text(result: dict) -> str:
    return "\n".join(
        [
            "UE Log/Crash Triage",
            f"- Log source: {result['log_source']}",
            f"- First actionable failure: {result['first_actionable_failure']}",
            f"- Failure phase: {result['failure_phase']}",
            f"- Probable root cause: {result['probable_root_cause']}",
            f"- Recommended next skill: {result['recommended_next_skill']}",
            f"- Packaging boundary: {result['packaging_boundary']}",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Unreal log triage helper.")
    parser.add_argument("--log", required=True, help="Path to an Unreal log file.")
    parser.add_argument("--top-n", type=int, default=1, help="Number of actionable failures to return.")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    result = triage_log(Path(args.log).resolve(), args.top_n)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
