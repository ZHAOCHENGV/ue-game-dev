import hashlib
import json
import re
import sys
from collections import defaultdict
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
ROUTING_RULES = SKILLS / "ue-game-dev-router" / "references" / "routing-rules.json"
MULTI_AGENT_SKILL = SKILLS / "ue-multi-agent-workflow" / "SKILL.md"
CHANGELOG = ROOT / "CHANGELOG.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
AGENT_WORKFLOW_DOC = ROOT / "docs" / "agents" / "repo-workflow.md"
MULTI_AGENT_REFERENCES = [
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-roles.md",
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-output-template.md",
    SKILLS / "ue-multi-agent-workflow" / "references" / "ue-agent-conflict-resolution.md",
]
UE_TOOL_SCRIPTS = [
    SKILLS / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
    SKILLS / "ue-project-onboarding" / "scripts" / "ue_config_audit.py",
    SKILLS / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
    SKILLS / "ue-debug-validation" / "scripts" / "ue_editor_command_report.py",
    SKILLS / "ue-cpp-gameplay" / "scripts" / "ue_blueprint_api_report.py",
    SKILLS / "ue-architecture" / "scripts" / "ue_dependency_graph.py",
    SKILLS / "ue-multi-agent-workflow" / "scripts" / "ue_agent_plan.py",
]
WARNINGS: list[str] = []

MOJIBAKE_MARKERS = [
    "\ufffd",
    "鈥",
    "鉁",
    "鉂",
    "锟",
    "鎵",
    "閿",
    "鍏堢啛",
    "椤圭洰",
    "闇€",
    "鎵",
    "璇",
    "鍙",
    "鍒",
    "涔",
    "乣",
    "銆",
    "鈫",
    "涔辩爜",
]

USER_VISIBLE_TEXT_FILES = [
    README,
    PLUGIN_JSON,
    CHANGELOG,
    CONTRIBUTING,
    ROUTE_SCENARIOS,
    ROUTER_SKILL,
    SKILLS / "ue-workflow-state" / "SKILL.md",
    SKILLS / "ue-workflow-state" / "references" / "state-file-templates.md",
]

EXTERNAL_FLOW_SKILLS = [
    "diagnose",
    "tdd",
    "grill-with-docs",
    "improve-codebase-architecture",
]

SYNC_DIRS = [".codex-plugin", "assets", "rules", "skills", "templates"]
SYNC_FILES = ["CHANGELOG.md", "LICENSE", "NOTICE", "README.md"]


def warn(message: str) -> None:
    WARNINGS.append(message)


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


def load_json(path: Path) -> dict:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} invalid JSON: {exc}")


def load_route_rules(known_skills: set[str] | None = None) -> dict:
    data = load_json(ROUTING_RULES)
    routes = data.get("routes")
    if not isinstance(routes, list):
        fail("routing-rules.json must contain a routes list")

    known_skills = known_skills or skill_names(sorted(path for path in SKILLS.iterdir() if path.is_dir()))
    for entry in routes:
        if not isinstance(entry, dict):
            fail("routing-rules.json routes must be objects")
        skill = entry.get("skill")
        if skill not in known_skills:
            fail(f"routing-rules.json references unknown skill: {skill}")
        if not isinstance(entry.get("priority"), int | float):
            fail(f"routing-rules.json route must include numeric priority: {skill}")
        patterns = entry.get("patterns")
        if not isinstance(patterns, list) or not patterns or not all(isinstance(pattern, str) for pattern in patterns):
            fail(f"routing-rules.json route has invalid patterns: {skill}")

    guardrails = data.get("guardrails", {})
    if guardrails and not isinstance(guardrails, dict):
        fail("routing-rules.json guardrails must be an object")
    for skill, guardrail in guardrails.items():
        if skill not in known_skills:
            fail(f"routing-rules.json guardrail references unknown skill: {skill}")
        if not isinstance(guardrail, dict):
            fail(f"routing-rules.json guardrail must be an object: {skill}")
    return data


def validate_user_visible_text() -> None:
    for path in USER_VISIBLE_TEXT_FILES:
        if not path.exists():
            continue
        text = read_text(path)
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                fail(f"{path.relative_to(ROOT)} contains likely mojibake marker: {marker}")

    plugin = load_json(PLUGIN_JSON)
    prompts = plugin.get("interface", {}).get("defaultPrompt", [])
    if not all(isinstance(prompt, str) for prompt in prompts):
        fail("plugin default prompts must be strings")
    if not any("旧 UE 项目" in prompt for prompt in prompts):
        fail("plugin default prompts should include readable Chinese onboarding example")

    scenarios = json.loads(read_text(ROUTE_SCENARIOS))
    if not any("诊断" in scenario.get("prompt", "") for scenario in scenarios):
        fail("route scenarios should include readable Chinese diagnosis wording")
    if not AGENT_WORKFLOW_DOC.exists():
        fail(f"missing agent workflow documentation: {AGENT_WORKFLOW_DOC.relative_to(ROOT)}")


def skill_names(skill_dirs: list[Path]) -> set[str]:
    return {path.name for path in skill_dirs}


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
    plugin = load_json(PLUGIN_JSON)

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
        "audio",
        "metasound",
        "world-partition",
        "data-layers",
        "hlod",
        "level-streaming",
        "physics",
        "chaos",
        "destruction",
        "data-management",
        "data-table",
        "asset-manager",
        "game-features",
        "modular-gameplay",
        "lyra-experience",
        "mass-entity",
        "mass-ai",
        "pcg",
        "procedural-generation",
        "state-tree",
        "sequencer",
        "movie-render-queue",
        "character-movement",
        "network-prediction",
        "diagnose",
        "tdd",
        "grill-with-docs",
        "improve-codebase-architecture",
    ]:
        if keyword not in keywords:
            fail(f"plugin keywords should include {keyword}")


def validate_changelog_version() -> None:
    plugin = load_json(PLUGIN_JSON)
    version = plugin.get("version")
    if not isinstance(version, str):
        fail("plugin.json version must be a string")
    base_version = version.split("+", 1)[0]
    changelog = read_text(ROOT / "CHANGELOG.md")
    match = re.search(r"^## \[([0-9]+\.[0-9]+\.[0-9]+)\]", changelog, re.M)
    if not match:
        fail("CHANGELOG latest version header not found")
    if match.group(1) != base_version:
        fail(f"CHANGELOG latest version {match.group(1)} must match plugin.json version {version}")


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


def validate_external_flow_handoffs() -> None:
    router_skill = read_text(ROUTER_SKILL)
    workflow_state = read_text(SKILLS / "ue-workflow-state" / "SKILL.md")
    workflow_template = read_text(SKILLS / "ue-workflow-state" / "references" / "state-file-templates.md")
    contributing = read_text(CONTRIBUTING)
    agent_doc = read_text(AGENT_WORKFLOW_DOC)

    for skill_name in EXTERNAL_FLOW_SKILLS:
        if skill_name not in router_skill:
            fail(f"router must document external flow handoff: {skill_name}")
        if skill_name not in agent_doc:
            fail(f"agent workflow doc must mention external flow skill: {skill_name}")

    for token in ["CONTEXT.md", "CONTEXT-MAP.md", "docs/adr", ".agents/ue-project-context.md"]:
        if token not in workflow_state:
            fail(f"workflow state skill should mention read-only import source: {token}")
        if token not in workflow_template:
            fail(f"workflow state template should mention {token}")

    for token in [
        "Gameplay Tags",
        "Input/UI/GAS conventions",
        "Runtime/Editor split",
        "API verification notes",
    ]:
        if token not in workflow_template:
            fail(f"workflow state template should mention {token}")

    for token in ["mattpocock/skills", "ue-game-dev-zh", "update_codex_app_plugin.py", "GitHub"]:
        if token not in contributing:
            fail(f"CONTRIBUTING should mention {token}")


SKILL_PATTERNS: dict[str, list[tuple[str, float]]] = {
    "ue-game-features": [
        ("Game Feature", 4.0),
        ("GameFeature", 4.0),
        ("Game Feature Plugin", 4.0),
        ("ModularGameplay", 4.0),
        ("UGameFeatureAction", 4.0),
        ("UGameFrameworkComponentManager", 4.0),
        ("Lyra Experience", 4.0),
        ("Lyra-style", 4.0),
        ("Experience Action Set", 3.0),
        ("ability grants", 2.0),
        ("modular gameplay", 3.0),
        ("模块化玩法", 4.0),
        ("功能插件", 3.0),
        ("特性插件", 3.0),
        ("激活 Game Feature", 3.0),
        ("接入 Lyra Experience", 4.0),
    ],
    "ue-mass-entity": [
        ("Mass Entity", 4.0),
        ("MassEntity", 4.0),
        ("Mass AI", 4.0),
        ("MassAI", 4.0),
        ("Mass Crowd", 4.0),
        ("MassProcessor", 4.0),
        ("MassFragment", 4.0),
        ("MassTag", 3.0),
        ("MassObserver", 4.0),
        ("MassSpawner", 3.0),
        ("ZoneGraph", 2.0),
        ("Smart Object", 2.0),
        ("crowd agents", 3.0),
        ("群体 AI", 4.0),
        ("大量 NPC", 3.0),
        ("人群模拟", 3.0),
    ],
    "ue-procedural-generation": [
        ("PCG", 4.0),
        ("PCG graph", 4.0),
        ("PCG Graph", 4.0),
        ("procedural generation", 4.0),
        ("runtime procedural", 4.0),
        ("ProceduralMesh", 4.0),
        ("ProceduralMeshComponent", 4.0),
        ("InstancedStaticMesh", 3.0),
        ("HierarchicalInstancedStaticMesh", 3.0),
        ("HISM", 3.0),
        ("spline generation", 3.0),
        ("deterministic seed", 2.0),
        ("程序化生成", 4.0),
        ("生成地形", 3.0),
        ("生成植被", 3.0),
        ("样条生成", 3.0),
        ("实例化网格", 3.0),
    ],
    "ue-state-trees": [
        ("StateTree", 4.0),
        ("State Tree", 4.0),
        ("StateTreeTask", 4.0),
        ("StateTreeCondition", 4.0),
        ("StateTreeEvaluator", 4.0),
        ("StateTree schema", 3.0),
        ("hierarchical state", 2.0),
        ("状态树", 4.0),
        ("状态机任务", 3.0),
        ("状态转换", 3.0),
        ("状态树任务", 3.0),
    ],
    "ue-sequencer-cinematics": [
        ("Sequencer", 4.0),
        ("Level Sequence", 4.0),
        ("LevelSequence", 4.0),
        ("Movie Render Queue", 4.0),
        ("MRQ", 3.0),
        ("cutscene", 3.0),
        ("cinematic", 3.0),
        ("camera cut", 3.0),
        ("Take Recorder", 3.0),
        ("event track", 2.0),
        ("过场动画", 4.0),
        ("电影渲染", 4.0),
        ("镜头轨道", 3.0),
        ("渲染输出", 2.0),
    ],
    "ue-character-movement": [
        ("CharacterMovementComponent", 5.0),
        ("Character Movement", 4.0),
        ("custom movement mode", 4.0),
        ("movement mode", 3.0),
        ("network prediction", 4.0),
        ("movement replication", 4.0),
        ("replicated movement", 4.0),
        ("root motion", 2.5),
        ("locomotion", 2.0),
        ("client prediction", 3.0),
        ("server correction", 3.0),
        ("角色移动", 4.0),
        ("自定义移动模式", 4.0),
        ("移动网络预测", 4.0),
        ("运动复制", 4.0),
        ("移动复制", 4.0),
    ],
    "ue-render-vfx": [
        ("Niagara", 3.0),
        ("VFX", 3.0),
        ("Lumen", 2.0),
        ("Nanite", 2.0),
        ("material", 2.0),
        ("shader", 2.0),
        ("post process", 2.0),
        ("renderer", 1.5),
        ("gpu emitter", 2.0),
        ("粒子特效", 3.0),
        ("粒子系统", 3.0),
        ("后处理", 2.0),
        ("材质球", 2.0),
        ("材质", 1.5),
        ("着色器", 2.0),
        ("渲染管线", 2.0),
        ("渲染", 1.0),
        ("特效", 1.5),
    ],
    "ue-animation": [
        ("Animation Blueprint", 3.0),
        ("Montage", 3.0),
        ("Blend Space", 3.0),
        ("Control Rig", 2.0),
        ("Motion Matching", 2.0),
        ("Anim Notify", 2.0),
        ("root motion", 2.0),
        ("动画蓝图", 3.0),
        ("蒙太奇", 3.0),
        ("骨骼动画", 2.0),
        ("IK", 1.5),
        ("状态机", 1.5),
        ("角色动画", 2.0),
        ("动画", 1.0),
        ("动画重定向", 2.0),
    ],
    "ue-ai-navigation": [
        ("Behavior Tree", 3.0),
        ("Blackboard", 3.0),
        ("EQS", 3.0),
        ("NavMesh", 3.0),
        ("AI Controller", 2.0),
        ("AI Perception", 2.0),
        ("StateTree", 2.0),
        ("行为树", 3.0),
        ("导航网格", 3.0),
        ("巡逻", 2.0),
        ("AI感知", 2.0),
        ("寻路", 2.0),
        ("导航", 1.5),
        ("AI", 0.5),
    ],
    "ue-save-load-sync": [
        ("USaveGame", 3.0),
        ("SaveGame", 2.0),
        ("RepNotify", 1.5),
        ("save/load", 2.0),
        ("serialization", 1.5),
        ("schema version", 2.0),
        ("restore", 1.0),
        ("存档", 3.0),
        ("读档", 3.0),
        ("保存游戏", 2.0),
        ("数据持久化", 2.0),
        ("存读档", 2.0),
    ],
    "ue-debug-validation": [
        ("Gameplay Debugger", 3.0),
        ("PIE debug", 2.0),
        ("Actor Tick", 1.5),
        ("debug", 1.0),
        ("validation", 1.0),
        ("showdebug", 2.0),
        ("调试", 2.0),
        ("断点", 2.0),
        ("排查", 1.5),
        ("验证", 1.0),
        ("诊断", 1.5),
    ],
    "ue-client-ui": [
        ("UMG", 3.0),
        ("CommonUI", 3.0),
        ("HUD", 2.0),
        ("DPI", 1.5),
        ("input focus", 2.0),
        ("view model", 2.0),
        ("gamepad navigation", 2.0),
        ("背包UI", 2.0),
        ("用户界面", 2.0),
        ("血条", 2.0),
        ("控件", 1.5),
        ("菜单", 1.0),
        ("UI", 0.5),
    ],
    "ue-world-interaction": [
        ("pickup", 2.0),
        ("spawner", 2.0),
        ("overlap", 1.5),
        ("line trace", 2.0),
        ("interact prompt", 2.0),
        ("interaction radius", 2.0),
        ("拾取物品", 3.0),
        ("交互系统", 2.0),
        ("射线检测", 2.0),
        ("拾取", 2.0),
        ("碰撞检测", 1.5),
        ("交互", 1.0),
    ],
    "ue-testing-automation": [
        ("AutomationSpec", 3.0),
        ("FAutomationTestBase", 3.0),
        ("Functional Test", 3.0),
        ("Functional Tests", 3.0),
        ("automation test", 2.0),
        ("regression", 1.5),
        ("pie scenario", 1.5),
        ("自动化测试", 3.0),
        ("功能测试", 2.0),
        ("回归测试", 2.0),
        ("测试", 0.5),
    ],
    "ue-gas-networking": [
        ("GameplayAbility", 3.0),
        ("AttributeSet", 3.0),
        ("GameplayCue", 3.0),
        ("GameplayEffect", 3.0),
        ("ASC", 2.0),
        ("prediction", 1.5),
        ("gas", 1.5),
        ("技能系统", 2.0),
        ("属性集", 2.0),
        ("冷却", 1.0),
        ("预测", 1.0),
        ("效果", 0.5),
    ],
    "ue-architecture": [
        ("Build.cs dependency", 2.0),
        ("Public/Private", 2.0),
        ("module graph", 2.0),
        ("architecture", 2.0),
        ("module boundary", 2.0),
        ("circular dependency", 3.0),
        ("dependency graph", 2.0),
        ("循环依赖", 3.0),
        ("模块划分", 2.0),
        ("依赖关系", 2.0),
        ("解耦", 2.0),
        ("架构", 1.5),
    ],
    "ue-blueprint-workflow": [
        ("Event Graph", 3.0),
        ("Blueprint graph", 2.0),
        ("Widget Blueprint", 2.0),
        ("wire blueprint nodes", 2.0),
        ("node", 0.5),
        ("pin", 0.5),
        ("事件图", 2.0),
        ("蓝图图表", 2.0),
        ("蓝图节点", 2.0),
        ("连线", 1.0),
    ],
    "ue-editor-tooling-slate": [
        ("Slate", 3.0),
        ("ToolMenus", 3.0),
        ("UICommand", 3.0),
        ("UICommands", 3.0),
        ("Editor subsystem", 2.0),
        ("details customization", 2.0),
        ("tab spawner", 2.0),
        ("editor panel", 2.0),
        ("编辑器工具面板", 3.0),
        ("编辑器面板", 2.0),
        ("编辑器工具", 2.0),
    ],
    "ue-plugin-module-dev": [
        (".uplugin", 3.0),
        ("ModuleRules", 3.0),
        ("API macro", 2.0),
        ("Public Private", 2.0),
        ("plugin module", 2.0),
        ("runtime module", 2.0),
        ("editor module", 2.0),
        ("Runtime + Editor", 3.0),
        ("插件开发", 2.0),
        ("模块开发", 2.0),
        ("双模块插件", 2.0),
    ],
    "ue-input-enhanced": [
        ("Enhanced Input", 3.0),
        ("IA_", 3.0),
        ("Input Mapping", 3.0),
        ("输入系统", 2.0),
        ("按键绑定", 2.0),
        ("重绑定", 2.0),
    ],
    "ue-async-systems": [
        ("UBlueprintAsyncActionBase", 3.0),
        ("AsyncTask", 3.0),
        ("GameThread", 2.0),
        ("ParallelFor", 2.0),
        ("异步蓝图节点", 3.0),
        ("异步节点", 2.0),
        ("后台线程", 2.0),
        ("异步", 1.0),
    ],
    "ue-external-services": [
        ("HTTP", 2.0),
        ("WebSocket", 3.0),
        ("TCP", 2.0),
        ("JSON 接口", 3.0),
        ("外部服务", 2.0),
        ("心跳", 2.0),
        ("重连", 2.0),
        ("接口对接", 2.0),
    ],
    "ue-audio": [
        ("MetaSound", 3.0),
        ("Sound Cue", 3.0),
        ("AudioComponent", 3.0),
        ("Sound Class", 2.0),
        ("Sound Mix", 2.0),
        ("Concurrency", 1.5),
        ("Quartz", 2.0),
        ("audio", 1.5),
        ("sound", 1.0),
        ("attenuation", 2.0),
        ("spatialization", 2.0),
        ("空间化", 2.0),
        ("音效", 2.0),
        ("音频", 2.0),
        ("音乐", 1.5),
        ("声音", 1.0),
    ],
    "ue-world-streaming": [
        ("World Partition", 3.0),
        ("Data Layers", 3.0),
        ("HLOD", 3.0),
        ("Level Streaming", 3.0),
        ("Streaming Volume", 2.0),
        ("Large World Coordinates", 2.0),
        ("runtime grid", 2.0),
        ("actor loading", 2.0),
        ("open world", 2.0),
        ("关卡流送", 3.0),
        ("世界分区", 3.0),
        ("开放世界", 2.0),
    ],
    "ue-physics-destruction": [
        ("Chaos", 3.0),
        ("Physics Constraint", 3.0),
        ("Geometry Collection", 3.0),
        ("Fracture", 3.0),
        ("Ragdoll", 3.0),
        ("Physical Material", 2.0),
        ("collision channel", 2.0),
        ("physics", 1.5),
        ("destruction", 2.0),
        ("布娃娃", 3.0),
        ("物理约束", 3.0),
        ("破坏系统", 3.0),
        ("物理材质", 2.0),
        ("碰撞通道", 2.0),
        ("物理效果", 2.0),
        ("破碎", 2.0),
    ],
    "ue-data-management": [
        ("Primary Asset Manager", 3.0),
        ("Asset Manager", 2.5),
        ("DataTable", 3.0),
        ("CurveTable", 2.0),
        ("DataRegistry", 3.0),
        ("FStreamableManager", 3.0),
        ("Soft Reference", 2.0),
        ("Hard Reference", 2.0),
        ("Primary Asset Rules", 2.0),
        ("Chunk", 1.5),
        ("数据表", 3.0),
        ("物品数据", 2.0),
        ("数据资产", 2.0),
        ("资产管理", 2.0),
        ("异步加载", 2.0),
        ("软引用", 2.0),
        ("硬引用", 2.0),
    ],
    "ue-cpp-gameplay": [
        ("BlueprintCallable", 3.0),
        ("蓝图怎么接", 3.0),
    ],
    "ue-start": [
        ("where to start", 2.0),
        ("start a ue task", 2.0),
        ("unclear scope", 2.0),
        ("choose workflow", 2.0),
        ("从哪开始", 2.0),
        ("不知道怎么做", 1.5),
    ],
    "ue-performance-packaging": [
        ("profile", 2.0),
        ("profiling", 2.0),
        ("stat unit", 2.0),
        ("frame rate", 2.0),
        ("性能", 1.5),
        ("帧率", 2.0),
        ("内存", 1.0),
        ("优化", 1.0),
        ("打包准备", 2.0),
    ],
}


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

    if any(token in prompt for token in ["是否可以进入", "gate", "Gate", "检查一下这个功能是否可以"]):
        return "ue-gate-check"

    rules = load_route_rules()
    packaging_guard = rules.get("guardrails", {}).get("ue-build-release-automation", {})
    if any(token in prompt for token in packaging_guard.get("forbid_when_any", [])):
        if any(token in prompt or token in lower for token in ["打包", "packaging", "release readiness", "go/no-go"]):
            return "ue-performance-packaging"
    if any(token in prompt for token in packaging_guard.get("requires_any", [])):
        return "ue-build-release-automation"

    if any(token in prompt for token in ["Saved/CodexWorkflow", "项目记忆", "workflow state", "Workflow State", "module-map", "known-risks", "active-task"]):
        return "ue-workflow-state"
    if any(token in prompt for token in ["Saved/Logs", "callstack", "崩溃", "日志", "UBT", "UHT", "UAT", "Cook failed", "Blueprint compile", "蓝图编译错误"]):
        return "ue-log-crash-triage"
    if any(token in prompt for token in ["grill-with-docs", "需求模糊", "需求有点模糊", "术语不清", "追问", "澄清需求"]):
        return "ue-feature-brief"
    if any(token in prompt for token in ["是否已经准备好打包", "准备好打包", "打包发布", "打包前验证"]):
        return "ue-performance-packaging"
    if any(token in prompt for token in ["处于什么开发阶段", "开发阶段", "还缺什么", "阶段"]):
        return "ue-stage-detect"
    if any(token in prompt for token in ["旧 UE 项目", "旧项目", "二开", "熟悉"]):
        return "ue-project-onboarding"
    if any(token in prompt for token in ["需求简报", "整理需求", "先帮我想清楚"]):
        return "ue-feature-brief"
    if any(token in prompt for token in ["TDD", "tdd", "test-driven", "测试先行", "回归测试", "自动化测试"]):
        return "ue-testing-automation"
    if any(token in prompt for token in ["improve-codebase-architecture", "deep module", "架构复盘", "模块太乱", "test seam", "可测试性"]):
        return "ue-architecture"
    if any(token in prompt for token in ["diagnose", "诊断", "稳定复现", "复现", "插桩"]):
        return "ue-debug-validation"
    if any(token in prompt for token in ["实施计划", "实现计划", "C++/蓝图/资产/测试"]):
        return "ue-implementation-plan"
    if any(token in prompt for token in ["完成验收", "交接清单", "做完了"]):
        return "ue-feature-done"

    scores: dict[str, float] = defaultdict(float)
    for entry in rules.get("routes", []):
        skill_name = entry["skill"]
        priority = float(entry["priority"])
        for pattern in entry["patterns"]:
            if pattern in prompt or pattern.casefold() in lower:
                scores[skill_name] += priority
    for skill_name, patterns in SKILL_PATTERNS.items():
        for pattern, weight in patterns:
            if pattern in prompt or pattern.casefold() in lower:
                scores[skill_name] += weight
    if scores:
        return max(scores, key=scores.get)
    return "ue-game-dev-router"


def validate_route_scenarios(skill_dirs: list[Path]) -> None:
    try:
        scenarios = json.loads(read_text(ROUTE_SCENARIOS))
    except json.JSONDecodeError as exc:
        fail(f"route_scenarios.json invalid JSON: {exc}")

    known_skills = skill_names(skill_dirs)
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


def validate_router_coverage(skill_dirs: list[Path]) -> None:
    router_skill = read_text(ROUTER_SKILL)
    router_refs = set(re.findall(r"\$([a-z0-9-]+)", router_skill))
    known_skills = skill_names(skill_dirs)
    route_rules = load_route_rules(known_skills)
    unknown_router_refs = sorted(ref for ref in router_refs if ref.startswith("ue-") and ref not in known_skills)
    if unknown_router_refs:
        fail(f"router references unknown skills: {', '.join(unknown_router_refs)}")

    try:
        scenarios = json.loads(read_text(ROUTE_SCENARIOS))
    except json.JSONDecodeError as exc:
        fail(f"route_scenarios.json invalid JSON: {exc}")
    covered = {scenario.get("expected_skill") for scenario in scenarios}

    # Explicit packaging automation is covered by an explicit scenario, but keep this
    # hook for future router-only skills that should not be scenario-routed.
    coverage_exceptions: set[str] = set()
    missing = sorted(ref for ref in router_refs if ref.startswith("ue-") and ref not in coverage_exceptions and ref not in covered)
    if missing:
        fail(f"router route coverage missing scenarios for: {', '.join(missing)}")

    for entry in route_rules.get("routes", []):
        if entry["skill"] not in covered:
            fail(f"routing-rules.json route missing scenario coverage: {entry['skill']}")


def validate_skill_references(skill_dirs: list[Path]) -> None:
    known_skills = skill_names(skill_dirs)
    reference_pattern = re.compile(r"(?<![\w/-])((?:[a-z0-9-]+/)?references/[A-Za-z0-9_.-]+\.md)")
    skill_ref_pattern = re.compile(r"\$([a-z0-9-]+)")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        text = read_text(skill_md)

        for match in reference_pattern.finditer(text):
            ref = match.group(1)
            parts = ref.split("/", 1)
            if len(parts) == 2 and parts[0] in known_skills:
                path = SKILLS / parts[0] / parts[1]
            else:
                path = skill_dir / ref
            if not path.exists():
                fail(f"{skill_md.relative_to(ROOT)} references missing file: {ref}")

        for ref in skill_ref_pattern.findall(text):
            if ref.startswith("ue-") and ref not in known_skills:
                fail(f"{skill_md.relative_to(ROOT)} references unknown skill: ${ref}")


def validate_reference_sizes() -> None:
    for path in sorted(SKILLS.glob("*/references/*.md")):
        size = path.stat().st_size
        if size < 500:
            warn(f"{path.relative_to(ROOT)} is small ({size} bytes)")


def validate_required_support_files() -> None:
    required_files = [
        ROOT / "templates" / "ue-task.md",
        ROOT / "templates" / "ue-test-evidence.md",
        ROOT / "NOTICE",
        ROOT / "rules" / "ue-cpp.md",
        ROOT / "rules" / "ue-blueprint.md",
        ROOT / "rules" / "ue-networking.md",
        ROOT / "rules" / "ue-assets.md",
        ROOT / "rules" / "ue-packaging.md",
        ROOT / "rules" / "ue-naming.md",
        ROOT / "rules" / "ue-performance.md",
        SKILLS / "ue-workflow-state" / "references" / "state-file-templates.md",
        SKILLS / "ue-log-crash-triage" / "references" / "triage-report-template.md",
        SKILLS / "ue-async-systems" / "references" / "async-patterns.md",
        SKILLS / "ue-external-services" / "references" / "service-client-patterns.md",
        SKILLS / "ue-audio" / "references" / "audio-checklist.md",
        SKILLS / "ue-world-streaming" / "references" / "world-partition-checklist.md",
        SKILLS / "ue-performance-packaging" / "references" / "performance-evidence-template.md",
        SKILLS / "ue-game-features" / "references" / "game-feature-checklist.md",
        SKILLS / "ue-mass-entity" / "references" / "mass-entity-checklist.md",
        SKILLS / "ue-procedural-generation" / "references" / "procedural-generation-checklist.md",
        SKILLS / "ue-state-trees" / "references" / "state-tree-checklist.md",
        SKILLS / "ue-sequencer-cinematics" / "references" / "sequencer-cinematics-checklist.md",
        SKILLS / "ue-character-movement" / "references" / "character-movement-checklist.md",
        SKILLS / "ue-character-movement" / "references" / "movement-prediction-matrix.md",
        SKILLS / "ue-project-onboarding" / "references" / "project-context-template.md",
        SKILLS / "ue-build-release-automation" / "references" / "buildgraph-and-artifacts.md",
        SKILLS / "ue-physics-destruction" / "references" / "chaos-physics-checklist.md",
        SKILLS / "ue-data-management" / "references" / "data-asset-patterns.md",
        SKILLS / "ue-plugin-module-dev" / "references" / "third-party-library-wrapper.md",
        ROUTING_RULES,
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
        "ue_config_audit.py": SKILLS / "ue-project-onboarding" / "SKILL.md",
        "ue_log_triage.py": SKILLS / "ue-log-crash-triage" / "SKILL.md",
        "ue_editor_command_report.py": SKILLS / "ue-debug-validation" / "SKILL.md",
        "ue_blueprint_api_report.py": SKILLS / "ue-cpp-gameplay" / "SKILL.md",
        "ue_dependency_graph.py": SKILLS / "ue-architecture" / "SKILL.md",
        "ue_agent_plan.py": SKILLS / "ue-multi-agent-workflow" / "SKILL.md",
    }
    readme = read_text(README)
    for script_name, skill_path in expected_mentions.items():
        if script_name not in read_text(skill_path):
            fail(f"{skill_path.relative_to(ROOT)} should mention {script_name}")
        if script_name not in readme:
            fail(f"README should mention {script_name}")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_marketplace_content_sync() -> None:
    for dir_name in SYNC_DIRS:
        root_dir = ROOT / dir_name
        package_dir = MARKETPLACE_PACKAGE / dir_name
        if not root_dir.exists():
            continue
        if not package_dir.exists():
            fail(f"missing marketplace package directory: {package_dir.relative_to(ROOT)}")

        for root_file in sorted(root_dir.rglob("*")):
            if not root_file.is_file():
                continue
            package_file = package_dir / root_file.relative_to(root_dir)
            if not package_file.exists():
                fail(f"marketplace mirror missing: {package_file.relative_to(ROOT)}")
            if file_hash(root_file) != file_hash(package_file):
                fail(f"marketplace mirror out of sync: {root_file.relative_to(ROOT)}")

        for package_file in sorted(package_dir.rglob("*")):
            if not package_file.is_file():
                continue
            root_file = root_dir / package_file.relative_to(package_dir)
            if not root_file.exists():
                warn(f"marketplace mirror has extra file: {package_file.relative_to(ROOT)}")

    for filename in SYNC_FILES:
        root_file = ROOT / filename
        package_file = MARKETPLACE_PACKAGE / filename
        if not root_file.exists():
            continue
        if not package_file.exists():
            fail(f"marketplace mirror missing: {package_file.relative_to(ROOT)}")
        if file_hash(root_file) != file_hash(package_file):
            fail(f"marketplace mirror out of sync: {filename}")


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
    package_notice = MARKETPLACE_PACKAGE / "NOTICE"
    for path in [
        package_plugin_json,
        package_skills,
        package_assets,
        package_rules,
        package_templates,
        package_readme,
        package_license,
        package_notice,
    ]:
        if not path.exists():
            fail(f"missing marketplace package file: {path.relative_to(ROOT)}")

    root_plugin = load_json(PLUGIN_JSON)
    package_plugin = load_json(package_plugin_json)
    if package_plugin.get("name") != root_plugin.get("name"):
        fail("marketplace package plugin name must match root plugin")
    if package_plugin.get("version") != root_plugin.get("version"):
        fail("marketplace package plugin version must match root plugin")

    for tool_path in UE_TOOL_SCRIPTS:
        package_tool = MARKETPLACE_PACKAGE / tool_path.relative_to(ROOT)
        if not package_tool.exists():
            fail(f"marketplace package missing UE tool script: {package_tool.relative_to(ROOT)}")
    validate_marketplace_content_sync()


def main() -> None:
    skill_dirs = validate_skill_dirs()
    validate_user_visible_text()
    validate_readme_skill_count(skill_dirs)
    validate_plugin_json()
    validate_changelog_version()
    validate_packaging_boundary()
    validate_multi_agent_support()
    validate_external_flow_handoffs()
    validate_skill_references(skill_dirs)
    validate_required_support_files()
    validate_tool_mentions()
    validate_marketplace_package()
    validate_route_scenarios(skill_dirs)
    validate_router_coverage(skill_dirs)
    validate_reference_sizes()
    for message in WARNINGS:
        print(f"WARN: {message}")
    print(f"OK: {len(skill_dirs)} skills validated")


if __name__ == "__main__":
    main()
