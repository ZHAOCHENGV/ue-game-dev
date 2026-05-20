import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
README = ROOT / "README.md"
ROUTE_SCENARIOS = ROOT / "tests" / "route_scenarios.json"
PACKAGING_OPENAI = SKILLS / "ue-build-release-automation" / "agents" / "openai.yaml"
PACKAGING_SKILL = SKILLS / "ue-build-release-automation" / "SKILL.md"
ROUTER_SKILL = SKILLS / "ue-game-dev-router" / "SKILL.md"


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
    if not any("RunUAT" in prompt for prompt in prompts):
        fail("plugin default prompts should include RunUAT example")
    if not any("Enhanced Input" in prompt for prompt in prompts):
        fail("plugin default prompts should include Enhanced Input example")


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


def route_prompt(prompt: str) -> str:
    lower = prompt.lower()
    if any(token in prompt for token in ["RunUAT", "BuildCookRun", "一键打包", "自动打包", "生成打包命令", "打包命令"]):
        return "ue-build-release-automation"
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
        ROUTE_SCENARIOS,
    ]
    for path in required_files:
        if not path.exists():
            fail(f"missing support file: {path.relative_to(ROOT)}")


def main() -> None:
    skill_dirs = validate_skill_dirs()
    validate_readme_skill_count(skill_dirs)
    validate_plugin_json()
    validate_packaging_boundary()
    validate_required_support_files()
    validate_route_scenarios(skill_dirs)
    print(f"OK: {len(skill_dirs)} skills validated")


if __name__ == "__main__":
    main()
