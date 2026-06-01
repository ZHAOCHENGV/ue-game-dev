# UE Production Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the UE Game Dev plugin more reliable in real Unreal Engine production projects by improving routing, project discovery, log triage, editor validation handoff, performance evidence, workflow state, multiplayer validation, release automation, and Chinese/UTF-8 synchronization.

**Architecture:** Keep the repository root as the source of truth and `plugins/ue-game-dev/` as the mirrored marketplace package. Build small read-only helper modules for real UE evidence, keep `.uasset` editing out of scope, and route users from broad intake to specific domain skills through data-backed tests. Every code phase starts with failing tests, updates root files first, runs `python scripts\sync_marketplace_package.py`, then validates the mirrored package and branch sync rules.

**Tech Stack:** Codex plugin manifests, Codex Skills markdown, Python 3.12 helper scripts and `unittest`, PowerShell on Windows, Unreal Engine project conventions, UBT/UHT/UAT log formats, optional generated Unreal commandlet commands, Git/GitHub `main` and `ue-game-dev-zh` branch sync.

---

## File Structure

- Modify `skills/ue-game-dev-router/SKILL.md`: keep user-facing routing rules, but move long keyword tables into data.
- Create `skills/ue-game-dev-router/references/routing-rules.json`: data-driven route patterns, priorities, packaging guardrails, and cross-domain handoffs.
- Modify `scripts/validate_plugin.py`: load routing data, validate routes, validate mojibake, validate branch/package sync constraints.
- Modify `tests/route_scenarios.json`: add real Chinese and English route coverage for production workflows.
- Modify `skills/ue-log-crash-triage/scripts/ue_log_triage.py`: add phase-aware UBT/UHT/UAT/Cook/crash parsing and structured evidence.
- Create `tests/fixtures/logs/*.log`: compact real-world-style log fixtures.
- Modify `skills/ue-project-onboarding/scripts/ue_project_scan.py`: scan config, targets, plugins, tags, Asset Manager, maps, and module boundaries.
- Create `skills/ue-project-onboarding/references/project-context-template.md`: production-grade `Saved/CodexWorkflow/project-context.md` template.
- Create `skills/ue-debug-validation/scripts/ue_editor_command_report.py`: generate safe Unreal Editor commandlet/report commands without running the editor.
- Modify `skills/ue-blueprint-workflow/SKILL.md`: route Blueprint asset work through read-only reports and compile/data-validation evidence.
- Modify `skills/ue-performance-packaging/SKILL.md`: require Unreal Insights/stat/memreport evidence for performance claims.
- Modify `skills/ue-gas-networking/references/networking-checklist.md`: add authority, prediction, replication, and rollback validation matrix.
- Modify `skills/ue-build-release-automation/SKILL.md`: expand BuildCookRun-only flow to BuildGraph, Project Launcher, CI/Horde/Jenkins, artifacts, symbols, and platform matrices.
- Modify `CONTRIBUTING.md` and `docs/agents/repo-workflow.md`: require root, marketplace package, local Codex App install, GitHub `main`, and `ue-game-dev-zh` synchronization.

## Global Verification

Run these after every task that changes plugin content:

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

Expected:

```text
OK: <skill-count> skills validated
Ran <n> tests ... OK
```

Then inspect:

```powershell
git status --short --branch
```

Expected: only intentional files are modified or added.

---

### Task 1: Data-Driven Router And Regression Harness

**Files:**
- Create: `skills/ue-game-dev-router/references/routing-rules.json`
- Modify: `skills/ue-game-dev-router/SKILL.md`
- Modify: `scripts/validate_plugin.py`
- Modify: `tests/route_scenarios.json`

- [ ] **Step 1: Add failing route scenarios**

Append these cases to `tests/route_scenarios.json`:

```json
{
  "name": "explicit_packaging_only_buildcookrun",
  "prompt": "帮我生成 Windows Shipping 的 RunUAT BuildCookRun 打包命令，并说明归档目录",
  "expected_skill": "ue-build-release-automation"
}
```

```json
{
  "name": "passive_packaging_readiness_not_automation",
  "prompt": "检查这个 UE 项目是否已经准备好打包发布，不要实际打包",
  "expected_skill": "ue-performance-packaging",
  "forbidden_skill": "ue-build-release-automation"
}
```

```json
{
  "name": "lyra_game_feature_gas_cross_domain",
  "prompt": "做一个 Lyra 风格 Game Feature，激活后注册 GAS Ability 和输入映射",
  "expected_skill": "ue-game-features"
}
```

```json
{
  "name": "network_prediction_character_movement",
  "prompt": "CharacterMovementComponent 自定义冲刺在 listen server 下预测回滚抖动",
  "expected_skill": "ue-character-movement"
}
```

- [ ] **Step 2: Run validation and capture the failure**

Run:

```powershell
$env:PYTHONUTF8='1'
python scripts\validate_plugin.py
```

Expected: route validation fails because route data has not been extracted and at least one new scenario is not recognized.

- [ ] **Step 3: Create routing data file**

Create `skills/ue-game-dev-router/references/routing-rules.json`:

```json
{
  "guardrails": {
    "ue-build-release-automation": {
      "requires_any": ["RunUAT", "BuildCookRun", "Project Launcher", "CI 打包", "一键打包", "生成打包命令", "实际打包"],
      "forbid_when_any": ["是否准备好打包", "打包前检查", "不要实际打包", "readiness", "go/no-go"]
    }
  },
  "routes": [
    {
      "skill": "ue-log-crash-triage",
      "priority": 100,
      "patterns": ["Saved/Logs", "UHT", "UBT", "UAT", "Cook failed", "callstack", "崩溃", "日志诊断"]
    },
    {
      "skill": "ue-game-features",
      "priority": 92,
      "patterns": ["Game Feature", "GameFeatureData", "ModularGameplay", "Lyra Experience", "模块化玩法"]
    },
    {
      "skill": "ue-character-movement",
      "priority": 90,
      "patterns": ["CharacterMovementComponent", "Network Prediction", "FSavedMove", "角色移动", "预测回滚"]
    },
    {
      "skill": "ue-performance-packaging",
      "priority": 80,
      "patterns": ["是否准备好打包", "打包前检查", "release readiness", "go/no-go", "性能回归", "Unreal Insights"]
    },
    {
      "skill": "ue-build-release-automation",
      "priority": 70,
      "patterns": ["RunUAT", "BuildCookRun", "Project Launcher", "CI 打包", "一键打包", "生成打包命令"]
    }
  ]
}
```

- [ ] **Step 4: Teach validator to load route data**

In `scripts/validate_plugin.py`, add a constant:

```python
ROUTING_RULES = SKILLS / "ue-game-dev-router" / "references" / "routing-rules.json"
```

Add this loader near `load_json`:

```python
def load_route_rules() -> dict:
    data = load_json(ROUTING_RULES)
    if not isinstance(data.get("routes"), list):
        fail("routing-rules.json must contain a routes list")
    for entry in data["routes"]:
        if entry.get("skill") not in skill_names(validate_skill_dirs()):
            fail(f"routing-rules.json references unknown skill: {entry.get('skill')}")
        if not entry.get("patterns"):
            fail(f"routing-rules.json route has no patterns: {entry.get('skill')}")
    return data
```

Then adjust `route_prompt(prompt: str)` to score `routing-rules.json` before falling back to `SKILL_PATTERNS`. Preserve the explicit packaging boundary before generic keyword scoring:

```python
rules = load_route_rules()
packaging_guard = rules.get("guardrails", {}).get("ue-build-release-automation", {})
if any(token in prompt for token in packaging_guard.get("forbid_when_any", [])):
    if any(token in prompt for token in ["打包", "packaging", "release readiness", "go/no-go"]):
        return "ue-performance-packaging"
if any(token in prompt for token in packaging_guard.get("requires_any", [])):
    return "ue-build-release-automation"
```

- [ ] **Step 5: Shorten router skill and point to data**

In `skills/ue-game-dev-router/SKILL.md`, add:

```markdown
## Routing Data

The validator-backed keyword and priority table lives in `references/routing-rules.json`.
Keep this skill readable for humans and keep exact route regression behavior in that JSON file.
When adding a route, add both a JSON route rule and at least one `tests/route_scenarios.json` case.
```

- [ ] **Step 6: Verify Task 1**

Run:

```powershell
$env:PYTHONUTF8='1'
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

Expected: validation and unit tests pass, and passive readiness still does not route to `ue-build-release-automation`.

- [ ] **Step 7: Commit Task 1**

```powershell
git add skills/ue-game-dev-router scripts/validate_plugin.py tests/route_scenarios.json
git commit -m "硬化 UE 路由回归与显式打包边界"
```

---

### Task 2: UE Log Triage V2

**Files:**
- Modify: `skills/ue-log-crash-triage/scripts/ue_log_triage.py`
- Modify: `skills/ue-log-crash-triage/SKILL.md`
- Create: `tests/fixtures/logs/uht_reflection_error.log`
- Create: `tests/fixtures/logs/ubt_link_error.log`
- Create: `tests/fixtures/logs/cook_asset_error.log`
- Create: `tests/fixtures/logs/crash_assert_callstack.log`
- Modify: `tests/test_ue_tools.py`

- [ ] **Step 1: Add fixture logs**

Create `tests/fixtures/logs/uht_reflection_error.log`:

```text
Running UnrealHeaderTool SampleGame.uproject
Source/SampleGame/Public/InventoryItem.h(18): Error: Unrecognized type 'FItemDefintion' - type must be a UCLASS, USTRUCT or UENUM
Total of 0 written
UnrealHeaderTool failed for target 'SampleGameEditor'
```

Create `tests/fixtures/logs/ubt_link_error.log`:

```text
Building SampleGameEditor...
Module.SampleGame.cpp.obj : error LNK2019: unresolved external symbol "public: void UInventoryComponent::AddItem(void)"
SampleGameEditor.exe : fatal error LNK1120: 1 unresolved externals
UnrealBuildTool failed.
```

Create `tests/fixtures/logs/cook_asset_error.log`:

```text
LogCook: Display: Cooking /Game/Maps/L_Main
LogLinker: Warning: Unable to load package '/Game/UI/WBP_MissingInventory'
LogCook: Error: Content is missing from cook. Referenced by /Game/Maps/L_Main
AutomationTool exiting with ExitCode=25 (Error_UnknownCookFailure)
```

Create `tests/fixtures/logs/crash_assert_callstack.log`:

```text
LogWindows: Error: Assertion failed: AbilitySystemComponent [File:D:/Project/Source/SampleGame/CombatPawn.cpp] [Line: 77]
LogWindows: Error: [Callstack] 0x00007ff CombatPawn::BeginPlay()
LogWindows: Error: [Callstack] 0x00007ff AActor::DispatchBeginPlay()
Fatal error!
```

- [ ] **Step 2: Add failing tests**

Add to `tests/test_ue_tools.py`:

```python
    def test_log_triage_classifies_real_ue_phases(self) -> None:
        cases = [
            ("uht_reflection_error.log", "UHT", "reflection"),
            ("ubt_link_error.log", "Link", "linker"),
            ("cook_asset_error.log", "Cook", "missing asset"),
            ("crash_assert_callstack.log", "Crash", "assertion"),
        ]
        for filename, phase, root_cause_token in cases:
            with self.subTest(filename=filename):
                result = run_tool(
                    ROOT / "skills" / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
                    "--log",
                    str(ROOT / "tests" / "fixtures" / "logs" / filename),
                )
                self.assertEqual(result["failure_phase"], phase)
                self.assertIn(root_cause_token, result["probable_root_cause"].lower())
                self.assertTrue(result["evidence"])
```

- [ ] **Step 3: Run the failing test**

Run:

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools.UEToolTests.test_log_triage_classifies_real_ue_phases
```

Expected: at least one case fails because `infer_root_cause` and phase extraction are too shallow.

- [ ] **Step 4: Implement phase taxonomy**

In `ue_log_triage.py`, add:

```python
PHASE_HINTS = [
    ("UHT", re.compile(r"UnrealHeaderTool|\.generated\.h|Unrecognized type|UCLASS|USTRUCT|UENUM", re.I)),
    ("Link", re.compile(r"\bLNK\d+|unresolved external|fatal error LNK", re.I)),
    ("Cook", re.compile(r"LogCook|Cook failed|missing from cook|Unable to load package", re.I)),
    ("Crash", re.compile(r"Assertion failed|Fatal error|Exception_Access_Violation|\[Callstack\]", re.I)),
    ("UAT", re.compile(r"RunUAT|BuildCookRun|AutomationTool|PackagingResults", re.I)),
    ("Build", re.compile(r"\berror C\d+|\berror:", re.I)),
    ("Blueprint", re.compile(r"Blueprint Runtime Error|Blueprint compile", re.I)),
]
```

Replace `classify_phase` with a function that returns the first matching high-priority phase from `PHASE_HINTS`, with Cook only winning over UAT when a Cook-specific line appears before the final AutomationTool summary.

- [ ] **Step 5: Improve root-cause text**

Replace `infer_root_cause` with:

```python
def infer_root_cause(first_failure: str, phase: str) -> str:
    lowered = first_failure.lower()
    if phase == "UHT":
        return "Reflection error; inspect UCLASS/USTRUCT/UENUM/UFUNCTION/UPROPERTY declarations and generated header order near the first failure."
    if phase == "Link":
        return "Linker error; inspect missing implementations, module dependencies, export macros, and target/module visibility."
    if phase == "Cook" and ("missing" in lowered or "unable to load package" in lowered):
        return "Cook missing asset/package reference; inspect redirectors, maps-to-cook, Primary Asset rules, and hard references from the reported asset."
    if phase == "Crash" or "assertion failed" in lowered:
        return "Assertion or crash; inspect the referenced source file, preconditions, object lifetime, and the first non-engine callstack frame."
    if phase == "Blueprint":
        return "Blueprint runtime or compile error; inspect the named Blueprint, pin compatibility, null references, and compile status."
    return "Use the earliest actionable failure as the next investigation point."
```

- [ ] **Step 6: Update skill instructions**

Add to `skills/ue-log-crash-triage/SKILL.md`:

```markdown
## Phase-Aware Triage

Classify the earliest actionable failure before summarizing the final UAT or Cook failure.
Do not treat `AutomationTool exiting`, `UnknownCookFailure`, or `BUILD FAILED` as the root cause when an earlier UHT, linker, Blueprint, asset, or assertion line exists.
```

- [ ] **Step 7: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
git diff --check
```

- [ ] **Step 8: Commit Task 2**

```powershell
git add skills/ue-log-crash-triage tests/test_ue_tools.py tests/fixtures/logs
git commit -m "增强 UE 日志诊断阶段识别"
```

---

### Task 3: UE Project Scan V2 And Context Template

**Files:**
- Modify: `skills/ue-project-onboarding/scripts/ue_project_scan.py`
- Create: `skills/ue-project-onboarding/references/project-context-template.md`
- Modify: `skills/ue-workflow-state/references/state-file-templates.md`
- Modify: `tests/test_ue_tools.py`

- [ ] **Step 1: Add failing scan assertions**

Extend `setUp` in `tests/test_ue_tools.py` with config files:

```python
        write(
            self.project / "Config" / "DefaultGameplayTags.ini",
            """
            [/Script/GameplayTags.GameplayTagsList]
            +GameplayTagList=(Tag="Ability.Fireball",DevComment="Fireball ability")
            +GameplayTagList=(Tag="UI.Inventory.Open",DevComment="Inventory UI")
            """,
        )
        write(
            self.project / "Config" / "DefaultGame.ini",
            """
            [/Script/Engine.AssetManagerSettings]
            +PrimaryAssetTypesToScan=(PrimaryAssetType="Item",AssetBaseClass="/Script/SampleGame.ItemDataAsset",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/Game/Data/Items")))
            """,
        )
```

Add test:

```python
    def test_project_scan_reports_production_context(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
            "--project",
            str(self.project),
        )

        self.assertIn("SampleGame.Target.cs", result["targets"])
        self.assertIn("SampleEditor.Target.cs", result["targets"])
        self.assertIn("Ability.Fireball", result["gameplay_tags"])
        self.assertTrue(any(entry["type"] == "Item" for entry in result["asset_manager"]["primary_asset_types"]))
        self.assertIn("Runtime module SampleGame depends on editor-like module SampleEditor", result["risks"])
```

- [ ] **Step 2: Run failing scan test**

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools.UEToolTests.test_project_scan_reports_production_context
```

Expected: keys such as `targets`, `gameplay_tags`, `asset_manager`, and `risks` are missing.

- [ ] **Step 3: Implement config scanners**

Add functions to `ue_project_scan.py`:

```python
def scan_targets(source_root: Path, root: Path) -> list[str]:
    if not source_root.exists():
        return []
    return sorted(str(path.relative_to(root)).replace("\\", "/") for path in source_root.rglob("*.Target.cs"))


def scan_gameplay_tags(config_root: Path) -> list[str]:
    tags: list[str] = []
    for path in sorted(config_root.glob("DefaultGameplayTags*.ini")):
        text = path.read_text(encoding="utf-8", errors="replace")
        tags.extend(re.findall(r'Tag="([^"]+)"', text))
    return sorted(dict.fromkeys(tags))


def scan_asset_manager(config_root: Path) -> dict:
    primary_types: list[dict] = []
    for path in [config_root / "DefaultGame.ini", config_root / "DefaultEngine.ini"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r'PrimaryAssetType="([^"]+)".*?Directories=\(\(Path="([^"]+)"\)\)', text):
            primary_types.append({"type": match.group(1), "path": match.group(2)})
    return {"primary_asset_types": primary_types}
```

Import `re` at the top.

- [ ] **Step 4: Implement basic production risks**

Add:

```python
def detect_risks(modules: list[str], build_files: list[str]) -> list[str]:
    risks: list[str] = []
    module_set = set(modules)
    for module in modules:
        if module.endswith("Editor"):
            continue
        for candidate in module_set:
            if candidate.endswith("Editor") and candidate in " ".join(build_files):
                risks.append(f"Runtime module {module} depends on editor-like module {candidate}")
    return sorted(dict.fromkeys(risks))
```

Add `targets`, `gameplay_tags`, `asset_manager`, and `risks` to the returned scan result.

- [ ] **Step 5: Add context template**

Create `skills/ue-project-onboarding/references/project-context-template.md`:

```markdown
# UE Project Context

## Engine And Project

- Engine version:
- Project name:
- Target platforms:
- Runtime modules:
- Editor modules:
- Enabled plugins:

## Content Conventions

- Asset prefixes:
- Map naming:
- UI naming:
- Blueprint parent patterns:
- Gameplay Tags:
- Input conventions:
- GAS conventions:

## Architecture Notes

- Runtime/Editor split:
- Primary Asset Manager rules:
- Save/load ownership:
- Network authority model:
- External services:

## API Verification Notes

- Engine source/API version checked:
- C++ reflection assumptions:
- Blueprint exposure assumptions:
- Known deprecated APIs:

## Local References

- Existing `CONTEXT.md`:
- Existing `CONTEXT-MAP.md`:
- Existing `docs/adr/`:
- Existing `.agents/ue-project-context.md`:
```

- [ ] **Step 6: Link template from workflow state**

In `skills/ue-workflow-state/references/state-file-templates.md`, add a section named `Project Context Template` that points to `ue-project-onboarding/references/project-context-template.md` and states that existing `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`, and `.agents/ue-project-context.md` are read-only inputs.

- [ ] **Step 7: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
git diff --check
```

- [ ] **Step 8: Commit Task 3**

```powershell
git add skills/ue-project-onboarding skills/ue-workflow-state tests/test_ue_tools.py
git commit -m "扩展 UE 项目扫描与上下文模板"
```

---

### Task 4: Safe Editor Commandlet Report Layer

**Files:**
- Create: `skills/ue-debug-validation/scripts/ue_editor_command_report.py`
- Modify: `skills/ue-debug-validation/SKILL.md`
- Modify: `skills/ue-blueprint-workflow/SKILL.md`
- Modify: `skills/ue-testing-automation/SKILL.md`
- Modify: `tests/test_ue_tools.py`

- [ ] **Step 1: Add failing command generator test**

Add to `tests/test_ue_tools.py`:

```python
    def test_editor_command_report_generates_safe_commands(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-debug-validation" / "scripts" / "ue_editor_command_report.py",
            "--project",
            str(self.project / "SampleGame.uproject"),
            "--engine-cmd",
            "C:/UE/UE_5.6/Engine/Binaries/Win64/UnrealEditor-Cmd.exe",
        )

        self.assertTrue(result["read_only"])
        self.assertIn("-run=DataValidation", result["commands"]["data_validation"])
        self.assertIn("-run=CompileAllBlueprints", result["commands"]["blueprint_compile"])
        self.assertIn("-run=MapCheck", result["commands"]["map_check"])
        self.assertIn("Do not run without user approval", result["safety"])
```

- [ ] **Step 2: Run failing test**

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools.UEToolTests.test_editor_command_report_generates_safe_commands
```

Expected: script file is missing.

- [ ] **Step 3: Create command report script**

Create `skills/ue-debug-validation/scripts/ue_editor_command_report.py`:

```python
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
        for name, command in result["commands"].items():
            print(f"{name}: {command}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Document safety boundary**

Add to `skills/ue-debug-validation/SKILL.md`:

```markdown
## Editor Commandlet Reports

Use `scripts/ue_editor_command_report.py` to generate DataValidation, CompileAllBlueprints, and MapCheck command lines.
The helper is read-only because it only prints commands.
Launching Unreal Editor commandlets requires explicit user approval and should be treated as an external-state-changing validation step.
```

Add to `skills/ue-blueprint-workflow/SKILL.md`:

```markdown
For `.uasset` Blueprint work, do not modify binary assets directly.
Generate or request read-only compile reports, DataValidation reports, MapCheck output, or exact graph instructions.
```

- [ ] **Step 5: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python -m unittest tests.test_ue_tools
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
git diff --check
```

- [ ] **Step 6: Commit Task 4**

```powershell
git add skills/ue-debug-validation skills/ue-blueprint-workflow skills/ue-testing-automation tests/test_ue_tools.py
git commit -m "加入安全的 UE 编辑器命令报告层"
```

---

### Task 5: Performance Evidence Workflow

**Files:**
- Modify: `skills/ue-performance-packaging/SKILL.md`
- Modify: `skills/ue-performance-packaging/references/performance-packaging-checklist.md`
- Create: `skills/ue-performance-packaging/references/performance-evidence-template.md`
- Modify: `tests/route_scenarios.json`
- Modify: `scripts/validate_plugin.py`

- [ ] **Step 1: Add validation requirement**

In `scripts/validate_plugin.py`, add `performance-evidence-template.md` to `validate_required_support_files`.

- [ ] **Step 2: Create evidence template**

Create `skills/ue-performance-packaging/references/performance-evidence-template.md`:

```markdown
# UE Performance Evidence

## Scenario

- Map:
- Platform:
- Build configuration:
- PIE or packaged:
- Player count:
- Scalability:

## Frame Evidence

- `stat unit` Game:
- `stat unit` Draw:
- `stat unit` GPU:
- Frame time target:
- Observed regression:

## Memory Evidence

- `memreport -full` path:
- Top memory buckets:
- Suspect assets:

## Unreal Insights

- Trace file:
- Capture duration:
- Game thread hotspot:
- Render thread hotspot:
- Asset loading hotspot:

## Decision

- PASS / CONCERNS / FAIL:
- Required fix before release:
- Follow-up skill:
```

- [ ] **Step 3: Update performance skill**

Add to `skills/ue-performance-packaging/SKILL.md`:

```markdown
## Evidence Before Claims

Do not claim a performance issue is fixed from code inspection alone.
Ask for or produce evidence from `stat unit`, `stat game`, `stat gpu`, `memreport -full`, Unreal Insights traces, packaged smoke tests, or platform profiler output.
For release readiness, separate editor PIE performance from packaged runtime performance.
```

- [ ] **Step 4: Add route scenario**

Append:

```json
{
  "name": "unreal_insights_performance_regression",
  "prompt": "这个 UE5 项目打包后帧率回退，帮我按 Unreal Insights、stat unit、memreport 做证据链",
  "expected_skill": "ue-performance-packaging"
}
```

- [ ] **Step 5: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

- [ ] **Step 6: Commit Task 5**

```powershell
git add skills/ue-performance-packaging scripts/validate_plugin.py tests/route_scenarios.json
git commit -m "补强 UE 性能证据工作流"
```

---

### Task 6: Workflow State Team And Local Modes

**Files:**
- Modify: `skills/ue-workflow-state/SKILL.md`
- Modify: `skills/ue-workflow-state/references/state-file-templates.md`
- Modify: `skills/ue-project-onboarding/SKILL.md`
- Modify: `CONTRIBUTING.md`

- [ ] **Step 1: Define state modes**

Add to `skills/ue-workflow-state/SKILL.md`:

```markdown
## State Modes

- Local mode: `Saved/CodexWorkflow/` is for machine-local AI memory, active task notes, generated scans, and temporary evidence. Do not commit it unless the project team explicitly wants shared AI state.
- Team mode: `docs/codex-workflow/` or project-approved documentation is for stable context, decisions, module maps, and onboarding notes that should survive across machines.
- Import mode: existing `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`, and `.agents/ue-project-context.md` are read-only sources unless the user asks to update them.
```

- [ ] **Step 2: Add stale detection fields**

In `skills/ue-workflow-state/references/state-file-templates.md`, add:

```markdown
## Freshness

- Last scan time:
- Engine version at scan:
- Git branch at scan:
- Git commit at scan:
- Uproject hash:
- Source module hash summary:
- Config hash summary:
- Stale when:
  - EngineAssociation changes.
  - `.uproject` modules/plugins change.
  - `Source/**.Build.cs` changes.
  - `Config/Default*.ini` changes.
```

- [ ] **Step 3: Document contribution rule**

In `CONTRIBUTING.md`, add:

```markdown
When changing workflow-state templates, update both the root skill files and the mirrored `plugins/ue-game-dev` package, then refresh the local Codex App installation and push both `main` and `ue-game-dev-zh`.
```

- [ ] **Step 4: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

- [ ] **Step 5: Commit Task 6**

```powershell
git add skills/ue-workflow-state skills/ue-project-onboarding CONTRIBUTING.md
git commit -m "明确 UE 工作流状态的本地与团队模式"
```

---

### Task 7: GAS, Networking, And Character Movement Validation Matrices

**Files:**
- Modify: `skills/ue-gas-networking/references/networking-checklist.md`
- Modify: `skills/ue-gas-networking/references/gas-patterns.md`
- Modify: `skills/ue-character-movement/SKILL.md`
- Create: `skills/ue-character-movement/references/movement-prediction-matrix.md`
- Modify: `scripts/validate_plugin.py`

- [ ] **Step 1: Add required support file validation**

Add `skills/ue-character-movement/references/movement-prediction-matrix.md` to `validate_required_support_files`.

- [ ] **Step 2: Create movement prediction matrix**

Create `skills/ue-character-movement/references/movement-prediction-matrix.md`:

```markdown
# Character Movement Prediction Matrix

| Scenario | Authority Owner | Client Prediction | Server Correction | Evidence |
|---|---|---|---|---|
| Sprint | Server validates intent | Client predicts speed change | Correct movement mode and max speed | Two-client PIE with packet lag |
| Dash | Server validates cooldown and direction | Client predicts launch | Reconcile location and montage | Listen server and dedicated server |
| Root motion ability | Server owns ability activation | Client predicts montage when allowed | Correct montage section and root motion source | GAS prediction key log |
| Custom movement mode | Server owns mode transition | Client predicts mode if deterministic | Correct movement mode byte and velocity | `p.NetShowCorrections 1` |
```

- [ ] **Step 3: Expand GAS networking checklist**

Add:

```markdown
## Multiplayer Validation Matrix

| Check | Listen Server | Dedicated Server | High Ping | Packet Loss |
|---|---|---|---|---|
| Ability activation | required | required | required | optional for early prototype |
| GameplayEffect replication | required | required | required | required before release |
| GameplayCue presentation | required | required | required | required before release |
| Attribute prediction | required when predicted | required when predicted | required | required |
```

- [ ] **Step 4: Update character movement skill**

Add to `skills/ue-character-movement/SKILL.md`:

```markdown
For custom movement, define the prediction contract before code changes: saved move data, compressed flags, correction tolerance, montage/root-motion ownership, and minimum PIE/dedicated-server validation.
Use `references/movement-prediction-matrix.md` for the validation table.
```

- [ ] **Step 5: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

- [ ] **Step 6: Commit Task 7**

```powershell
git add skills/ue-gas-networking skills/ue-character-movement scripts/validate_plugin.py
git commit -m "补强 GAS 与角色移动网络验证矩阵"
```

---

### Task 8: Release Automation Expansion

**Files:**
- Modify: `skills/ue-build-release-automation/SKILL.md`
- Modify: `skills/ue-build-release-automation/references/buildcookrun-commands.md`
- Modify: `skills/ue-build-release-automation/references/ci-build-templates.md`
- Create: `skills/ue-build-release-automation/references/buildgraph-and-artifacts.md`
- Modify: `scripts/validate_plugin.py`
- Modify: `tests/route_scenarios.json`

- [ ] **Step 1: Add explicit BuildGraph scenario**

Append:

```json
{
  "name": "explicit_buildgraph_release_pipeline",
  "prompt": "帮我设计 UE BuildGraph 发布流水线，包含符号、归档产物和 Jenkins 参数",
  "expected_skill": "ue-build-release-automation"
}
```

- [ ] **Step 2: Create BuildGraph artifact reference**

Create `skills/ue-build-release-automation/references/buildgraph-and-artifacts.md`:

```markdown
# BuildGraph And Release Artifacts

## Release Inputs

- Project:
- Engine version:
- Platform:
- Configuration:
- Client/server targets:
- Cook maps:
- DLC/chunk rules:

## Artifact Outputs

- Packaged build:
- Symbols:
- Crash reporter symbols:
- Logs:
- Build metadata:
- AutomationTool output:
- Installer/archive:

## CI Notes

- Jenkins/Horde node labels:
- Shared DDC:
- Clean workspace policy:
- Credentials and signing:
- Archive retention:
```

- [ ] **Step 3: Link reference from skill**

Add to `skills/ue-build-release-automation/SKILL.md`:

```markdown
Use `references/buildgraph-and-artifacts.md` when the user asks for BuildGraph, Horde, Jenkins, Project Launcher profiles, symbols, release artifacts, or multi-platform release automation.
This skill still requires explicit packaging or automation intent.
```

- [ ] **Step 4: Extend CI templates**

In `ci-build-templates.md`, add compact Jenkins and Horde checklist sections with required parameters:

```markdown
## Jenkins Parameters

- `UE_PROJECT`
- `UE_ENGINE_ROOT`
- `PLATFORM`
- `CONFIGURATION`
- `ARCHIVE_DIR`
- `BUILD_VERSION`
- `RUN_TESTS`
```

- [ ] **Step 5: Verify and sync**

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

- [ ] **Step 6: Commit Task 8**

```powershell
git add skills/ue-build-release-automation scripts/validate_plugin.py tests/route_scenarios.json
git commit -m "扩展 UE 发布自动化到 BuildGraph 与产物管理"
```

---

### Task 9: Encoding, Local Install, And Branch Sync Hardening

**Files:**
- Modify: `scripts/validate_plugin.py`
- Modify: `scripts/update_codex_app_plugin.py`
- Modify: `CONTRIBUTING.md`
- Modify: `docs/agents/repo-workflow.md`
- Modify: `tests/test_validate_plugin.py`
- Modify: `tests/test_update_codex_app_plugin.py`

- [ ] **Step 1: Add mojibake regression tests**

In `tests/test_validate_plugin.py`, add:

```python
    def test_mojibake_markers_include_common_chinese_garble(self) -> None:
        import scripts.validate_plugin as validator

        markers = set(validator.MOJIBAKE_MARKERS)
        self.assertIn("锟", markers)
        self.assertIn("鎵", markers)
        self.assertIn("閿", markers)
```

- [ ] **Step 2: Expand marker list**

In `scripts/validate_plugin.py`, ensure `MOJIBAKE_MARKERS` includes:

```python
"锟",
"鎵",
"閿",
"鐢",
"涓",
"缁",
"乱码",
```

- [ ] **Step 3: Add local install dry-run validation**

In `scripts/update_codex_app_plugin.py`, ensure the script supports:

```powershell
python scripts\update_codex_app_plugin.py --dry-run
```

and reports source version, destination path, and files that would be copied without writing files.

- [ ] **Step 4: Add branch sync checklist**

In `docs/agents/repo-workflow.md`, add:

```markdown
## Release Sync Checklist

1. Run validation on the implementation branch.
2. Merge or fast-forward `main`.
3. Run `python scripts\sync_marketplace_package.py`.
4. Run `python scripts\update_codex_app_plugin.py`.
5. Push `main`.
6. Fast-forward or merge `ue-game-dev-zh`.
7. Push `ue-game-dev-zh`.
8. Confirm Codex App plugin list shows `UE Game Dev` and readable Chinese prompts.
```

- [ ] **Step 5: Verify**

```powershell
$env:PYTHONUTF8='1'
python scripts\update_codex_app_plugin.py --dry-run
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

- [ ] **Step 6: Commit Task 9**

```powershell
git add scripts CONTRIBUTING.md docs/agents tests
git commit -m "强化中文编码与插件同步发布检查"
```

---

### Task 10: Final Package, Local App, GitHub Branch Sync

**Files:**
- Modify: `.codex-plugin/plugin.json`
- Modify: `plugins/ue-game-dev/.codex-plugin/plugin.json`
- Modify: `CHANGELOG.md`
- Modify: `README.md`

- [ ] **Step 1: Bump version**

Set `.codex-plugin/plugin.json` version to:

```json
"version": "0.15.0+codex.20260601000000"
```

Run:

```powershell
python scripts\sync_marketplace_package.py
```

- [ ] **Step 2: Update changelog**

Add to the top of `CHANGELOG.md`:

```markdown
## [0.15.0] - 2026-06-01

- Hardened UE routing with data-backed regression scenarios.
- Improved UBT/UHT/UAT/Cook/crash log triage.
- Expanded project scanning for production context, tags, targets, and Asset Manager data.
- Added safe Editor commandlet report generation.
- Added performance evidence, networking validation, release automation, and branch sync guardrails.
```

- [ ] **Step 3: Final validation**

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
git status --short --branch
```

- [ ] **Step 4: Update local Codex App install**

```powershell
python scripts\update_codex_app_plugin.py
```

Expected: local plugin cache contains the new version and the plugin list can show `UE Game Dev` with readable Chinese prompt text after refresh.

- [ ] **Step 5: Commit final version**

```powershell
git add .codex-plugin plugins/ue-game-dev CHANGELOG.md README.md
git commit -m "发布 UE Game Dev 生产硬化版本"
```

- [ ] **Step 6: Push GitHub branches**

```powershell
git push origin main
git checkout ue-game-dev-zh
git merge main
git push origin ue-game-dev-zh
git checkout main
```

Expected: `main` and `ue-game-dev-zh` both contain the same plugin content, changelog, marketplace package, and validation scripts.

---

## Self-Review

- Spec coverage: The plan covers router size, log triage, project scanning, editor commandlets, Blueprint safe boundary, performance evidence, workflow state, GAS/networking/CharacterMovement validation, release automation, encoding, local install, and GitHub branch sync.
- Placeholder scan: No `TODO` or `TBD` placeholders are used. Steps include exact files, commands, and expected behavior.
- Type consistency: Python helper functions return JSON-compatible dictionaries matching the existing `run_tool` test helper. Route cases use existing `expected_skill` and `forbidden_skill` fields.
- Risk note: Some tasks refer to skills that exist in the upgraded plugin cache but may not exist in an older dirty worktree. Before implementation, run `python scripts\validate_plugin.py`; if `ue-game-features` or `ue-character-movement` is missing, implement or sync those skills before Task 1 route cases.
