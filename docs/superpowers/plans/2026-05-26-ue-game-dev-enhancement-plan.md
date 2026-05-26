# UE Game Dev Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the `ue-game-dev` Codex plugin with stronger shared UE rules, broader router test coverage, audio and world streaming skills, deeper thin skills/references, and stricter validation while keeping the marketplace package synchronized.

**Architecture:** Treat the repository root as the source of truth and `plugins/ue-game-dev/` as the Codex marketplace package mirror. Each implementation phase changes root files first, runs `python scripts/sync_marketplace_package.py`, then verifies the root and mirrored package with `python scripts/validate_plugin.py`, unit tests, and targeted structural checks.

**Tech Stack:** Codex Skills markdown, JSON plugin metadata, Python 3.12 validation scripts, PowerShell/Git on Windows, GitHub remote `https://github.com/ZHAOCHENGV/ue-game-dev.git`.

---

## Current Verified Baseline

- Skill directories: `30`.
- Reference markdown files under `skills/**/references/`: `52`.
- Route scenarios: `19`.
- Router skill references: `29`.
- Route scenario skill coverage: `15/29`; uncovered: `ue-ai-navigation`, `ue-animation`, `ue-architecture`, `ue-blueprint-workflow`, `ue-client-ui`, `ue-debug-validation`, `ue-editor-tooling-slate`, `ue-gas-networking`, `ue-plugin-module-dev`, `ue-render-vfx`, `ue-save-load-sync`, `ue-start`, `ue-testing-automation`, `ue-world-interaction`.
- Shared rule files are intentionally present but too thin: `ue-packaging.md` 7 lines, `ue-assets.md` 7, `ue-networking.md` 8, `ue-blueprint.md` 8, `ue-cpp.md` 9.
- Thinnest `SKILL.md` files: `ue-debug-validation` 25 lines, `ue-save-load-sync` 26, `ue-blueprint-workflow` 27.
- Current branch at planning time: `codex/add-async-external-service-skills`.

## Non-Negotiable Repository Rule

Every phase that changes any of these root paths must sync the marketplace package before validation:

- `.codex-plugin/`
- `assets/`
- `rules/`
- `skills/`
- `templates/`
- `CHANGELOG.md`
- `LICENSE`
- `README.md`

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
```

Then verify root and mirror are aligned:

```powershell
Compare-Object (rg --files skills) (rg --files plugins\ue-game-dev\skills | ForEach-Object { $_ -replace '^plugins\\ue-game-dev\\','' })
Compare-Object (rg --files rules) (rg --files plugins\ue-game-dev\rules | ForEach-Object { $_ -replace '^plugins\\ue-game-dev\\','' })
Compare-Object (rg --files templates) (rg --files plugins\ue-game-dev\templates | ForEach-Object { $_ -replace '^plugins\\ue-game-dev\\','' })
```

Expected: no output from all three `Compare-Object` commands.

## Commit And Push Policy

Per user preference, future implementation commits should go directly to `main` unless the user explicitly asks for a PR branch. Commit messages should be detailed Chinese messages, for example:

```text
扩充 UE 共享规则并同步插件市场包

- 扩充 C++、蓝图、网络、资产和打包规则文件
- 增加 Good/Bad 示例、Anti-Pattern 和 UE5 注意事项
- 同步 plugins/ue-game-dev 市场安装包
- 通过 validate_plugin.py 和单元测试验证
```

Before direct push to `main`, always run fresh verification and inspect `git status --short --branch`.

---

### Task 1: Expand Shared `rules/` Files

**Files:**
- Modify: `rules/ue-cpp.md`
- Modify: `rules/ue-blueprint.md`
- Modify: `rules/ue-networking.md`
- Modify: `rules/ue-assets.md`
- Modify: `rules/ue-packaging.md`
- Mirror after sync: `plugins/ue-game-dev/rules/*.md`

- [ ] **Step 1: Expand `rules/ue-cpp.md`**

Add focused sections, not a course chapter:

```markdown
## Reflection And Ownership

- Keep reflected state narrow and intentional.
- Use `UPROPERTY` for UObject references that must be visible to GC.
- Prefer `TObjectPtr` for reflected UObject references in UE5.

### Good

```cpp
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Combat")
TObjectPtr<UCombatComponent> CombatComponent;
```

### Bad

```cpp
UCombatComponent* CombatComponent; // GC cannot see this reference.
```
```

Also add: Blueprint exposure rules, Tick avoidance, Runtime/Editor dependency split, UE5 notes for `TObjectPtr`, `UE::Tasks`, Chaos, and `FInstancedStruct`.

- [ ] **Step 2: Expand `rules/ue-blueprint.md`**

Add sections for graph shape, input event uniqueness, Widget Blueprint update strategy, Blueprint/C++ boundary, and anti-patterns:

```markdown
## Anti-Patterns

- Long Event Graphs with unrelated workflows mixed together.
- Repeated key/input events in multiple Blueprints.
- Per-frame casts or expensive UI bindings.
- Hidden authoritative state mutation from arbitrary widgets.
```

- [ ] **Step 3: Expand `rules/ue-networking.md`**

Add sections for authority, replicated properties, RPCs, GAS handoff, listen server differences, and validation:

```markdown
## Replication

- Replicate server-owned observable state, not client intent.
- Use `RepNotify` for client presentation updates.
- Keep RPC payloads small and rate-limited.
- Validate ownership before accepting client RPCs.
```

- [ ] **Step 4: Expand `rules/ue-assets.md`**

Add asset prefix table and reference safety rules:

```markdown
| Prefix | Asset Type |
|--------|------------|
| `BP_` | Blueprint Actor/Object |
| `WBP_` | Widget Blueprint |
| `IA_` | Input Action |
| `IMC_` | Input Mapping Context |
| `M_` / `MI_` | Material / Material Instance |
```

- [ ] **Step 5: Expand `rules/ue-packaging.md`**

Add explicit packaging boundary, platform notes, cook failure patterns, and config checklist:

```markdown
## Cook Failure Patterns

- Missing or moved assets referenced by maps or Blueprints.
- Editor-only classes referenced from runtime assets.
- Runtime module depending on editor-only modules.
- Required maps not included by maps-to-cook or Primary Asset rules.
```

- [ ] **Step 6: Sync marketplace package**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
```

Expected: prints `synced marketplace package: ...\plugins\ue-game-dev`.

- [ ] **Step 7: Verify phase 1**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\validate_plugin.py
python -m unittest tests.test_ue_tools
git diff --check
```

Expected:

```text
OK: 30 skills validated
Ran 4 tests ... OK
```

- [ ] **Step 8: Commit phase 1 to `main` if requested**

Only after user approval to proceed with direct main commit:

```powershell
git checkout main
git pull origin main
git add rules plugins/ue-game-dev/rules
git commit -m "扩充 UE 共享规则文件

- 扩充 C++、蓝图、网络、资产和打包规则
- 增加示例、Anti-Pattern 和 UE5 注意事项
- 同步 plugins/ue-game-dev 市场安装包
- 通过插件自检和单元测试验证"
git push origin main
```

---

### Task 2: Add Route Coverage And Two Missing Domain Skills

**Files:**
- Create: `skills/ue-audio/SKILL.md`
- Create: `skills/ue-audio/agents/openai.yaml`
- Create: `skills/ue-audio/references/audio-checklist.md`
- Create: `skills/ue-world-streaming/SKILL.md`
- Create: `skills/ue-world-streaming/agents/openai.yaml`
- Create: `skills/ue-world-streaming/references/world-partition-checklist.md`
- Modify: `skills/ue-game-dev-router/SKILL.md`
- Modify: `tests/route_scenarios.json`
- Modify: `.codex-plugin/plugin.json`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Mirror after sync: corresponding files under `plugins/ue-game-dev/`

- [ ] **Step 1: Add failing route scenarios first**

Append route scenarios before implementing router logic. Include at least:

```json
{
  "name": "audio_metasound",
  "prompt": "帮我用 MetaSound 实现自适应音效系统",
  "expected_skill": "ue-audio"
}
```

```json
{
  "name": "world_partition_data_layers",
  "prompt": "帮我配置 World Partition 和 Data Layers",
  "expected_skill": "ue-world-streaming"
}
```

Also add one scenario for each currently uncovered router skill: `ue-ai-navigation`, `ue-animation`, `ue-architecture`, `ue-blueprint-workflow`, `ue-client-ui`, `ue-debug-validation`, `ue-editor-tooling-slate`, `ue-gas-networking`, `ue-plugin-module-dev`, `ue-render-vfx`, `ue-save-load-sync`, `ue-start`, `ue-testing-automation`, `ue-world-interaction`.

- [ ] **Step 2: Run route validation and observe expected failure**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\validate_plugin.py
```

Expected: failure because `ue-audio` and `ue-world-streaming` directories do not exist or route logic does not return them yet.

- [ ] **Step 3: Create `ue-audio` skill**

Create `skills/ue-audio/SKILL.md` with frontmatter:

```markdown
---
name: ue-audio
description: Unreal Engine audio workflow for MetaSound, Sound Cue, AudioComponent, Sound Classes, Sound Mixes, Sound Concurrency, Quartz timing, spatialization, attenuation, audio debugging, and platform audio settings. Use when requests involve gameplay audio, adaptive music, sound effects, runtime audio components, or audio performance.
---
```

Body sections: First Pass, Implementation Rules, MetaSound And Runtime Audio, Verification, References.

Create `skills/ue-audio/agents/openai.yaml`:

```yaml
interface:
  display_name: "UE Audio"
  short_description: "Plan and debug Unreal audio, MetaSound, and runtime audio systems."
  default_prompt: "Use $ue-audio to design or debug Unreal MetaSound, Sound Cue, AudioComponent, or audio performance work."
```

Create `skills/ue-audio/references/audio-checklist.md` with focused checklist for MetaSound, Sound Cue, AudioComponent, Sound Mix/Class, Concurrency, attenuation/spatialization, platform settings, and profiling.

- [ ] **Step 4: Create `ue-world-streaming` skill**

Create `skills/ue-world-streaming/SKILL.md` with frontmatter:

```markdown
---
name: ue-world-streaming
description: Unreal Engine world streaming workflow for World Partition, Data Layers, HLOD, Level Streaming, Level Streaming Volumes, Large World Coordinates, runtime grid setup, actor loading/unloading, streaming performance, and open-world validation.
---
```

Body sections: First Pass, World Partition Rules, Level Streaming Rules, Data Layers And HLOD, Verification, References.

Create `skills/ue-world-streaming/agents/openai.yaml`:

```yaml
interface:
  display_name: "UE World Streaming"
  short_description: "Plan Unreal World Partition, Data Layers, HLOD, and level streaming."
  default_prompt: "Use $ue-world-streaming to design or debug World Partition, Data Layers, HLOD, or level streaming."
```

Create `skills/ue-world-streaming/references/world-partition-checklist.md` with checklist for map mode, grid, Data Layers, HLOD, streaming sources, runtime loading, origin/LWC concerns, and packaged validation.

- [ ] **Step 5: Update router**

Modify `skills/ue-game-dev-router/SKILL.md`:

```markdown
- Use `$ue-audio` for MetaSound, Sound Cues, AudioComponents, Sound Classes, Sound Mixes, Sound Concurrency, Quartz timing, spatialization, attenuation, and audio performance.
- Use `$ue-world-streaming` for World Partition, Data Layers, HLOD, Level Streaming, Level Streaming Volumes, Large World Coordinates, runtime grid setup, and actor loading/unloading.
```

Update the coverage gap sentence so audio, level streaming, and World Partition are removed from the fallback list. Keep physics and destruction as explicit gaps unless the user later approves `ue-physics-destruction`.

- [ ] **Step 6: Update `scripts/validate_plugin.py` route helper**

Add prompt detection for the two new skills in `route_prompt`:

```python
if any(token in prompt for token in ["MetaSound", "Sound Cue", "AudioComponent", "音效", "音频", "Quartz"]):
    return "ue-audio"
if any(token in prompt for token in ["World Partition", "Data Layers", "HLOD", "Level Streaming", "关卡流", "开放世界"]):
    return "ue-world-streaming"
```

Also add plugin keywords to `validate_plugin_json`: `audio`, `metasound`, `world-partition`, `data-layers`, `hlod`, `level-streaming`.

- [ ] **Step 7: Update metadata and docs**

Update `.codex-plugin/plugin.json`:

- version: next minor, for example `0.12.0`.
- description includes audio and world streaming.
- keywords include `audio`, `metasound`, `world-partition`, `data-layers`, `hlod`, `level-streaming`.

Update `README.md`:

- Skill count from `1 + 29` to `1 + 31`.
- Add `ue-audio` and `ue-world-streaming` to the feature table.
- Add quick-call examples.

Update `CHANGELOG.md` with a new `0.12.0` entry.

- [ ] **Step 8: Sync marketplace package and verify phase 2**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest tests.test_ue_tools
git diff --check
```

Expected:

```text
OK: 32 skills validated
Ran 4 tests ... OK
```

Also run:

```powershell
Compare-Object (rg --files skills) (rg --files plugins\ue-game-dev\skills | ForEach-Object { $_ -replace '^plugins\\ue-game-dev\\','' })
```

Expected: no output.

---

### Task 3: Deepen Thin Skills And References

**Files:**
- Modify: `skills/ue-debug-validation/SKILL.md`
- Modify: `skills/ue-save-load-sync/SKILL.md`
- Modify: `skills/ue-blueprint-workflow/SKILL.md`
- Modify: `skills/ue-cpp-gameplay/references/validation.md`
- Modify: `skills/ue-project-onboarding/references/onboarding-report-template.md`
- Modify: `skills/ue-log-crash-triage/references/triage-report-template.md`
- Modify: `skills/ue-feature-brief/references/feature-brief-template.md`
- Modify: `skills/ue-render-vfx/references/niagara-checklist.md`
- Modify: `skills/ue-world-interaction/references/interaction-checklist.md`
- Modify: `skills/ue-blueprint-workflow/references/blueprint-cpp-boundary.md`
- Modify: `skills/ue-render-vfx/references/rendering-checklist.md`
- Mirror after sync: corresponding files under `plugins/ue-game-dev/`

- [ ] **Step 1: Deepen `ue-debug-validation`**

Add concise sections for:

- debug evidence order
- `stat` command families
- `showdebug`
- Gameplay Debugger
- PIE multi-window/network debugging
- breakpoint and conditional breakpoint guidance

- [ ] **Step 2: Deepen `ue-save-load-sync`**

Add concise sections for:

- `USaveGame` vs custom `FArchive`
- schema versioning
- cloud/local sync boundaries
- server-authoritative save timing
- restore and RepNotify handoff

- [ ] **Step 3: Deepen `ue-blueprint-workflow`**

Add concise sections for:

- Widget Blueprint event flow
- manual refresh vs property binding
- Blueprint performance anti-patterns
- graph decomposition and macro/function boundary

- [ ] **Step 4: Deepen eight references**

For each reference, add practical checklists and short examples. Keep each file focused; do not turn references into course chapters.

- [ ] **Step 5: Sync and verify phase 3**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest tests.test_ue_tools
git diff --check
```

Expected:

```text
OK: 32 skills validated
Ran 4 tests ... OK
```

---

### Task 4: Add Script Incremental Capabilities

**Files:**
- Modify: `skills/ue-project-onboarding/scripts/ue_project_scan.py`
- Modify: `skills/ue-log-crash-triage/scripts/ue_log_triage.py`
- Modify: `skills/ue-cpp-gameplay/scripts/ue_blueprint_api_report.py`
- Modify: `tests/test_ue_tools.py`
- Mirror after sync: corresponding files under `plugins/ue-game-dev/`

- [ ] **Step 1: Add failing tests for new script options**

Extend `tests/test_ue_tools.py` with tests for:

- `ue_project_scan.py --filter SampleGame`
- `ue_project_scan.py --format markdown` or `--output-format markdown`
- `ue_log_triage.py --top-n 2`
- `ue_blueprint_api_report.py --module SampleGame`
- `ue_blueprint_api_report.py --interface`

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python -m unittest tests.test_ue_tools
```

Expected: failing tests because options are not implemented.

- [ ] **Step 3: Implement options minimally**

Implement only the options covered by tests:

- `ue_project_scan.py`: module filter and markdown output.
- `ue_log_triage.py`: `--top-n` returning a list of actionable failures while preserving existing single-failure fields for compatibility.
- `ue_blueprint_api_report.py`: module filter and UInterface reporting.

- [ ] **Step 4: Sync and verify phase 4**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest tests.test_ue_tools
git diff --check
```

Expected:

```text
OK: 32 skills validated
All tests OK
```

---

### Task 5: Strengthen `validate_plugin.py`

**Files:**
- Modify: `scripts/validate_plugin.py`
- Modify: `tests/route_scenarios.json` if route coverage validation needs metadata cleanup.

- [ ] **Step 1: Add reference existence validation**

Parse each `skills/*/SKILL.md` for:

- local references like `references/foo.md`
- cross-skill references like `ue-blueprint-workflow/references/foo.md`

Fail when a referenced file does not exist.

- [ ] **Step 2: Add `$ue-*` target validation**

Parse `SKILL.md` files for `$ue-*` references and fail when `skills/<name>/` does not exist.

- [ ] **Step 3: Add route coverage validation**

Parse `skills/ue-game-dev-router/SKILL.md` for `$ue-*` references and ensure each has at least one `tests/route_scenarios.json` scenario.

If explicit-only packaging or special edge cases need exceptions, encode the exception list in the validator with a comment explaining why.

- [ ] **Step 4: Add CHANGELOG version sync validation**

Read `.codex-plugin/plugin.json` version and require `CHANGELOG.md` to contain a latest matching `## [x.y.z]` header.

- [ ] **Step 5: Add reference minimum-size warning or failure**

Use a warning for files below `500` bytes at first. Do not fail existing thin references until Task 3 has completed.

- [ ] **Step 6: Verify final state**

Run:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:Path"
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest tests.test_ue_tools
git diff --check
git status --short --branch
```

Expected:

```text
OK: 32 skills validated
Ran ... tests ... OK
```

`git status` should show only intentional implementation changes before committing.

---

## Deferred Decisions

- `ue-physics-destruction`: Router still lists physics and destruction as coverage gaps. Add this only after confirming it is a real priority.
- `ue-data-management`: Useful for DataRegistry, Primary Asset Manager, DataTable, CurveTable, and async asset loading, but it overlaps with assets, save/load, and world streaming. Decide separately.
- UE version target: Default examples should target UE5.x. Add UE4.27 compatibility notes only when the rule differs materially.
- Language: Keep skill bodies and rules mostly English for consistency with existing files; Chinese notes are acceptable in README/CHANGELOG and user-facing planning docs.

## Final Verification Checklist

- [ ] `python scripts\validate_plugin.py` passes.
- [ ] `python -m unittest tests.test_ue_tools` passes.
- [ ] `git diff --check` passes.
- [ ] Root and `plugins/ue-game-dev/` mirrors are synchronized.
- [ ] `README.md`, `CHANGELOG.md`, root `.codex-plugin/plugin.json`, and mirrored plugin metadata all agree on version and skill count.
- [ ] No `tests/__pycache__/` remains.
- [ ] Commit message is detailed Chinese if committing to `main`.
