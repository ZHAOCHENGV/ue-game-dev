import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
README = ROOT / "README.md"
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


def main() -> None:
    skill_dirs = validate_skill_dirs()
    validate_readme_skill_count(skill_dirs)
    validate_plugin_json()
    validate_packaging_boundary()
    print(f"OK: {len(skill_dirs)} skills validated")


if __name__ == "__main__":
    main()
