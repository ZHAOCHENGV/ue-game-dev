#!/usr/bin/env python3
import argparse
import json


ROLE_RULES = [
    ("Project Explorer", ["旧", "二开", "熟悉", "接手", "onboarding", "legacy"]),
    ("UE Architecture Reviewer", ["架构", "模块", "插件", "Build.cs", "C++", "蓝图", "refactor"]),
    ("C++ Implementer", ["C++", "UFUNCTION", "Actor", "Component", "Subsystem"]),
    ("Blueprint Integrator", ["蓝图", "Blueprint", "Widget", "UMG"]),
    ("Verifier", ["测试", "验证", "PIE", "构建", "完成"]),
    ("GAS/Networking", ["GAS", "网络", "复制", "RPC", "replication"]),
    ("UI/UMG", ["UI", "UMG", "Widget", "HUD", "CommonUI"]),
    ("Enhanced Input", ["Enhanced Input", "IA_", "IMC_", "输入"]),
    ("Packaging/Release", ["打包", "发布", "RunUAT", "BuildCookRun", "CI"]),
    ("Log/Crash Triage", ["日志", "崩溃", "Saved/Logs", "callstack", "失败"]),
]


def contains_any(text: str, tokens: list[str]) -> bool:
    lowered = text.lower()
    return any(token.lower() in lowered for token in tokens)


def choose_mode(request: str, requested_mode: str | None) -> str:
    if requested_mode:
        return requested_mode
    if contains_any(request, ["full 模式", "完整审查", "全面审查", "全量"]):
        return "full"
    if contains_any(request, ["多 Agent", "多Agent", "multi-agent", "多专家", "团队协作", "并行专家"]):
        return "lean"
    return "solo"


def choose_roles(request: str, mode: str) -> list[str]:
    if mode == "solo":
        return []
    roles = ["Coordinator"]
    for role, tokens in ROLE_RULES:
        if contains_any(request, tokens) and role not in roles:
            roles.append(role)
    if mode == "full":
        for role in ["Project Explorer", "UE Architecture Reviewer", "Verifier"]:
            if role not in roles:
                roles.append(role)
    if len(roles) == 1:
        roles.extend(["Project Explorer", "Verifier"])
    if mode == "lean" and len(roles) > 4:
        keep = ["Coordinator"]
        for role in roles[1:]:
            if role in {"Project Explorer", "UE Architecture Reviewer", "Verifier"} or len(keep) < 4:
                keep.append(role)
        roles = keep[:4]
    return roles


def ownership_for_roles(roles: list[str]) -> list[str]:
    boundaries = []
    if "Project Explorer" in roles:
        boundaries.append("Project Explorer: read-only .uproject, Source/, Plugins/, Config/, Content filenames, Saved/CodexWorkflow/")
    if "UE Architecture Reviewer" in roles:
        boundaries.append("UE Architecture Reviewer: .Build.cs, .uplugin, module boundaries, Runtime/Editor dependency direction")
    if "C++ Implementer" in roles:
        boundaries.append("C++ Implementer: Source/ C++ headers and implementation files assigned by Coordinator")
    if "Blueprint Integrator" in roles:
        boundaries.append("Blueprint Integrator: Blueprint node/pin handoff and asset setup instructions; no binary .uasset edits")
    if "Verifier" in roles:
        boundaries.append("Verifier: build, Blueprint compile, PIE/test/log evidence")
    if not boundaries:
        boundaries.append("solo: no multi-agent ownership boundaries; use focused skill")
    return boundaries


def recommended_skills(request: str, roles: list[str], mode: str) -> list[str]:
    if mode == "solo":
        return ["ue-game-dev-router"]
    skills = ["ue-multi-agent-workflow"]
    if "Project Explorer" in roles:
        skills.append("ue-project-onboarding")
    if "UE Architecture Reviewer" in roles:
        skills.append("ue-architecture")
    if "C++ Implementer" in roles:
        skills.append("ue-cpp-gameplay")
    if "Blueprint Integrator" in roles:
        skills.append("ue-blueprint-workflow")
    if "Verifier" in roles:
        skills.append("ue-testing-automation")
    if "Log/Crash Triage" in roles:
        skills.append("ue-log-crash-triage")
    if "Packaging/Release" in roles and not contains_any(request, ["生成打包命令", "运行打包", "自动打包", "BuildCookRun", "RunUAT"]):
        skills.append("ue-performance-packaging")
    return list(dict.fromkeys(skills))


def packaging_boundary(request: str) -> str:
    if contains_any(request, ["生成打包命令", "运行打包", "自动打包", "BuildCookRun", "RunUAT", "一键打包"]):
        return "explicit automation requested"
    if contains_any(request, ["打包", "发布", "Cook", "UAT"]):
        return "review only"
    return "not relevant"


def build_plan(request: str, requested_mode: str | None) -> dict:
    mode = choose_mode(request, requested_mode)
    roles = choose_roles(request, mode)
    return {
        "tool": "ue-agent-plan",
        "read_only": True,
        "mode": mode,
        "roles": roles,
        "ownership_boundaries": ownership_for_roles(roles),
        "parallel_discovery": [
            f"{role}: collect evidence independently"
            for role in roles
            if role not in {"Coordinator", "C++ Implementer", "Blueprint Integrator"}
        ],
        "dependent_phases": ["Coordinator synthesis", "focused skill routing", "verification plan"] if mode != "solo" else [],
        "packaging_boundary": packaging_boundary(request),
        "recommended_next_skills": recommended_skills(request, roles, mode),
    }


def render_text(result: dict) -> str:
    lines = [
        "UE Agent Plan",
        f"- Mode: {result['mode']}",
        f"- Roles: {', '.join(result['roles']) or 'None'}",
        f"- Packaging boundary: {result['packaging_boundary']}",
        "- Ownership boundaries:",
    ]
    lines.extend(f"  - {boundary}" for boundary in result["ownership_boundaries"])
    lines.append("- Recommended next skills: " + ", ".join(result["recommended_next_skills"]))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan lightweight UE multi-agent coordination.")
    parser.add_argument("--request", required=True, help="User request to classify.")
    parser.add_argument("--mode", choices=["solo", "lean", "full"], default=None)
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    result = build_plan(args.request, args.mode)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))


if __name__ == "__main__":
    main()
