import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
README = ROOT / "README.md"
MARKETPLACE_JSON = ROOT / ".agents" / "plugins" / "marketplace.json"
MARKETPLACE_PACKAGE = ROOT / "plugins" / "ue-game-dev"
ROUTE_SCENARIOS = ROOT / "tests" / "route_scenarios.json"
PACKAGING_OPENAI = SKILLS / "ue-build-release-automation" / "agents" / "openai.yaml"
PACKAGING_SKILL = SKILLS / "ue-build-release-automation" / "SKILL.md"
ROUTER_SKILL = SKILLS / "ue-game-dev-router" / "SKILL.md"
MULTI_AGENT_SKILL = SKILLS / "ue-multi-agent-workflow" / "SKILL.md"
MULTI_AGENT_REFERENCES = [
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-roles.md",
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-output-template.md",
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-conflict-resolution.md",
]
UE_TOOL_SCRIPTS = [
    SKILLS / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
    SKILLS / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
    SKILLS / "ue-cpp-gameplay" / "scripts" / "ue_blueprint_api_report.py",
    SKILLS / "ue-multi-agent-workflow" / "scripts" / "ue_agent_plan.py",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"invalid frontmatter line in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_skill_dirs() -> list[Path]:
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        text = read_text(skill_md)
        fields = parse_frontmatter(text, skill_md)
        expected_name = skill_dir.name
        if fields.get("name") != expected_name:
            fail(f"{skill_md.relative_to(ROOT)} name must be {expected_name}")
        if not fields.get("description"):
            fail(f"{skill_md.relative_to(ROOT)} missing description")
        if "TODO" in text or "[TODO" in text:
            fail(f"{skill_md.relative_to(ROOT)} contains TODO placeholder")
        if not openai_yaml.exists():
            fail(f"missing agents/openai.yaml for {skill_dir.name}")
    return skill_dirs


def validate_readme_skill_count(skill_dirs: list[Path]) -> None:
    readme = read_text(README)
    match = re.search(r"1 个路由技能 \+ (\d+) 个领域技能", readme)
    if not match:
        fail("README skill count line not found")
    documented_domain_count = int(match.group(1))
    actual_domain_count = len(skill_dirs) - 1
    if documented_domain_count != actual_domain_count:
        fail(
            "README domain skill count mismatch: "
            f"documented {documented_domain_count}, actual {actual_domain_count}"
        )


def validate_plugin_json() -> None:
    try:
        plugin = json.loads(read_text(PLUGIN_JSON))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json invalid JSON: {exc}")

    if plugin.get("name") != "ue-game-dev":
        fail("plugin.json name must be ue-game-dev")
    if not plugin.get("version"):
        fail("plugin.json missing version")
    if plugin.get("skills") != "./skills/":
        fail("plugin.json skills must be ./skills/")

    prompts = plugin.get("interface", {}).get("defaultPrompt", [])
    if len(prompts) > 3:
        fail("plugin default prompts should include at most 3 entries for marketplace UI")
    if not any("CodexWorkflow" in prompt for prompt in prompts):
        fail("plugin default prompts should include CodexWorkflow example")
    if not any("Saved/Logs" in prompt or "callstack" in prompt for prompt in prompts):
        fail("plugin default prompts should include log/crash triage example")
    keywords = set(plugin.get("keywords", []))
    for keyword in [
        "runuat",
        "enhanced-input",
        "workflow-state",
        "log-triage",
        "multi-agent",
        "agent-orchestration",
        "ue-project-scan",
        "ue-log-triage",
        "blueprint-api-report",
        "agent-plan",
        "async",
        "blueprint-async-action",
        "external-services",
        "http",
        "websocket",
        "tcp",
        "json",
    ]:
        if keyword not in keywords:
            fail(f"plugin keywords should include {keyword}")


def validate_packaging_boundary() -> None:
    openai_yaml = read_text(PACKAGING_OPENAI)
    packaging_skill = read_text(PACKAGING_SKILL)
    router_skill = read_text(ROUTER_SKILL)

    if "allow_implicit_invocation: false" not in openai_yaml:
        fail("ue-build-release-automation must disable implicit invocation")
    if "Use only when" not in packaging_skill:
        fail("packaging skill must state explicit-only invocation")
    if "Do not route here for passive readiness checks" not in router_skill:
        fail("router must protect automatic packaging from passive routing")
    if "must not trigger `$ue-build-release-automation` by itself" not in read_text(MULTI_AGENT_SKILL):
        fail("multi-agent workflow must protect automatic packaging from implicit routing")


def validate_multi_agent_support() -> None:
    multi_agent_skill = read_text(MULTI_AGENT_SKILL)
    router_skill = read_text(ROUTER_SKILL)

    for token in ["Mode", "Coordinator", "Parallel Discovery Results", "BLOCKED", "Ownership boundaries", "Do not load these references"]:
        if token not in multi_agent_skill:
            fail(f"multi-agent skill should mention {token}")
    if "$ue-multi-agent-workflow" not in router_skill:
        fail("router must reference ue-multi-agent-workflow")

    for path in MULTI_AGENT_REFERENCES:
        text = read_text(path)
        for token in ["Coordinator", "BLOCKED", "simple", "packaging"]:
            if token not in text:
                fail(f"{path.relative_to(ROOT)} should mention {token}")


def route_prompt(prompt: str) -> str:
    lower = prompt.lower()
    multi_agent = any(
        token in prompt
        for token in ["多 Agent", "多Agent", "multi-agent", "Multi-Agent", "多专家", "团队协作", "并行专家", "full 模式", "lean 模式"]
    )
    complex_coordination = multi_agent and any(
        token in prompt
        for token in ["旧 UE 项目", "旧项目", "二开", "架构", "C++", "蓝图", "UI", "资产", "测试", "打包失败", "Saved/Logs", "Build.cs"]
    )
    if complex_coordination:
        return "ue-multi-agent-workflow"
    failure_or_log = any(token in prompt for token in ["失败", "错误", "日志", "崩溃", "callstack", "Crash", "crash", "Cook failed", "PackagingResults"])
    if failure_or_log and any(token in prompt for token in ["RunUAT", "BuildCookRun", "UAT", "UBT", "UHT", "Saved/Logs"]):
        return "ue-log-crash-triage"
    if any(token in prompt for token in ["RunUAT", "BuildCookRun", "一键打包", "自动打包", "生成打包命令", "打包命令"]):
        return "ue-build-release-automation"
    if any(token in prompt for token in ["Saved/CodexWorkflow", "项目记忆", "workflow state", "Workflow State", "module-map", "known-risks", "active-task"]):
        return "ue-workflow-state"
    if any(token in prompt for token in ["Saved/Logs", "callstack", "崩溃", "日志", "UBT", "UHT", "UAT", "Cook failed", "Blueprint compile", "蓝图编译错误"]):
        return "ue-log-crash-triage"
    if any(token in prompt for token in ["是否可以进入", "gate", "Gate", "检查一下这个功能是否可以"]):
        return "ue-gate-check"
    if any(token in prompt for token in ["是否已经准备好打包", "准备好打包", "打包发布", "打包前验证"]):
        return "ue-performance-packaging"
    if any(token in prompt for token in ["处于什么开发阶段", "开发阶段", "还缺什么", "阶段"]):
        return "ue-stage-detect"
    if any(token in prompt for token in ["旧 UE 项目", "旧项目", "二开", "熟悉"]):
        return "ue-project-onboarding"
    if any(token in prompt for token in ["需求简报", "整理需求", "先帮我想清楚"]):
        return "ue-feature-brief"
    if any(token in prompt for token in ["实施计划", "实现计划", "C++/蓝图/资产/测试"]):
        return "ue-implementation-plan"
    if any(token in prompt for token in ["完成验收", "交接清单", "做完了"]):
        return "ue-feature-done"
    if "Enhanced Input" in prompt or "IA_" in prompt or "Input Mapping" in prompt:
        return "ue-input-enhanced"
    if any(token in prompt for token in ["UBlueprintAsyncActionBase", "AsyncTask", "后台线程", "GameThread", "ParallelFor", "异步蓝图节点", "异步节点"]):
        return "ue-async-systems"
    if any(token in prompt for token in ["HTTP", "WebSocket", "TCP", "JSON 接口", "外部服务", "心跳", "重连"]):
        return "ue-external-services"
    if "BlueprintCallable" in prompt or "蓝图怎么接" in prompt:
        return "ue-cpp-gameplay"
    if "gas" in lower:
        return "ue-gas-networking"
    return "ue-game-dev-router"


def validate_route_scenarios(skill_dirs: list[Path]) -> None:
    try:
        scenarios = json.loads(read_text(ROUTE_SCENARIOS))
    except json.JSONDecodeError as exc:
        fail(f"route_scenarios.json invalid JSON: {exc}")

    known_skills = {path.name for path in skill_dirs}
    for scenario in scenarios:
        name = scenario.get("name", "<unnamed>")
        prompt = scenario.get("prompt", "")
        expected = scenario.get("expected_skill")
        forbidden = scenario.get("forbidden_skill")
        if expected not in known_skills:
            fail(f"route scenario {name} expects unknown skill: {expected}")
        if forbidden and forbidden not in known_skills:
            fail(f"route scenario {name} forbids unknown skill: {forbidden}")
        actual = route_prompt(prompt)
        if actual != expected:
            fail(f"route scenario {name}: expected {expected}, got {actual}")
        if forbidden and actual == forbidden:
            fail(f"route scenario {name}: routed to forbidden skill {forbidden}")


def validate_required_support_files() -> None:
    required_files = [
        ROOT / "templates" / "ue-task.md",
        ROOT / "templates" / "ue-test-evidence.md",
        ROOT / "rules" / "ue-cpp.md",
        ROOT / "rules" / "ue-blueprint.md",
        ROOT / "rules" / "ue-networking.md",
        ROOT / "rules" / "ue-assets.md",
        ROOT / "rules" / "ue-packaging.md",
        SKILLS / "ue-workflow-state" / "references" / "state-file-templates.md",
        SKILLS / "ue-log-crash-triage" / "references" / "triage-report-template.md",
        SKILLS / "ue-async-systems" / "references" / "async-patterns.md",
        SKILLS / "ue-external-services" / "references" / "service-client-patterns.md",
        SKILLS / "ue-plugin-module-dev" / "references" / "third-party-library-wrapper.md",
        ROUTE_SCENARIOS,
        ROOT / "tests" / "test_ue_tools.py",
        *UE_TOOL_SCRIPTS,
    ]
    for path in required_files:
        if not path.exists():
            fail(f"missing support file: {path.relative_to(ROOT)}")


def validate_tool_mentions() -> None:
    expected_mentions = {
        "ue_project_scan.py": SKILLS / "ue-project-onboarding" / "SKILL.md",
        "ue_log_triage.py": SKILLS / "ue-log-crash-triage" / "SKILL.md",
        "ue_blueprint_api_report.py": SKILLS / "ue-cpp-gameplay" / "SKILL.md",
        "ue_agent_plan.py": SKILLS / "ue-multi-agent-workflow" / "SKILL.md",
    }
    readme = read_text(README)
    for script_name, skill_path in expected_mentions.items():
        if script_name not in read_text(skill_path):
            fail(f"{skill_path.relative_to(ROOT)} should mention {script_name}")
        if script_name not in readme:
            fail(f"README should mention {script_name}")


def validate_marketplace_package() -> None:
    if not MARKETPLACE_JSON.exists():
        return

    try:
        marketplace = json.loads(read_text(MARKETPLACE_JSON))
    except json.JSONDecodeError as exc:
        fail(f"marketplace.json invalid JSON: {exc}")

    if marketplace.get("name") != "zhaochengv-ue":
        fail("marketplace name must be zhaochengv-ue")
    if marketplace.get("interface", {}).get("displayName") != "ZHAOCHENGV UE Plugins":
        fail("marketplace displayName must be ZHAOCHENGV UE Plugins")

    entries = marketplace.get("plugins", [])
    matching = [entry for entry in entries if entry.get("name") == "ue-game-dev"]
    if len(matching) != 1:
        fail("marketplace must contain exactly one ue-game-dev entry")

    entry = matching[0]
    if entry.get("source", {}).get("source") != "local":
        fail("ue-game-dev marketplace source must be local")
    if entry.get("source", {}).get("path") != "./plugins/ue-game-dev":
        fail("ue-game-dev marketplace path must be ./plugins/ue-game-dev")
    if entry.get("policy", {}).get("installation") != "AVAILABLE":
        fail("ue-game-dev marketplace installation policy must be AVAILABLE")
    if entry.get("policy", {}).get("authentication") != "ON_INSTALL":
        fail("ue-game-dev marketplace authentication policy must be ON_INSTALL")
    if entry.get("category") != "Coding":
        fail("ue-game-dev marketplace category must be Coding")

    package_plugin_json = MARKETPLACE_PACKAGE / ".codex-plugin" / "plugin.json"
    package_skills = MARKETPLACE_PACKAGE / "skills"
    package_assets = MARKETPLACE_PACKAGE / "assets"
    package_rules = MARKETPLACE_PACKAGE / "rules"
    package_templates = MARKETPLACE_PACKAGE / "templates"
    package_readme = MARKETPLACE_PACKAGE / "README.md"
    package_license = MARKETPLACE_PACKAGE / "LICENSE"
    for path in [
        package_plugin_json,
        package_skills,
        package_assets,
        package_rules,
        package_templates,
        package_readme,
        package_license,
    ]:
        if not path.exists():
            fail(f"missing marketplace package file: {path.relative_to(ROOT)}")

    root_plugin = json.loads(read_text(PLUGIN_JSON))
    package_plugin = json.loads(read_text(package_plugin_json))
    if package_plugin.get("name") != root_plugin.get("name"):
        fail("marketplace package plugin name must match root plugin")
    if package_plugin.get("version") != root_plugin.get("version"):
        fail("marketplace package plugin version must match root plugin")

    for tool_path in UE_TOOL_SCRIPTS:
        package_tool = MARKETPLACE_PACKAGE / tool_path.relative_to(ROOT)
        if not package_tool.exists():
            fail(f"marketplace package missing UE tool script: {package_tool.relative_to(ROOT)}")


def main() -> None:
    skill_dirs = validate_skill_dirs()
    validate_readme_skill_count(skill_dirs)
    validate_plugin_json()
    validate_packaging_boundary()
    validate_multi_agent_support()
    validate_required_support_files()
    validate_tool_mentions()
    validate_marketplace_package()
    validate_route_scenarios(skill_dirs)
    print(f"OK: {len(skill_dirs)} skills validated")


if __name__ == "__main__":
    main()
