# UE Gate Check Template

```text
UE Gate Check: <from stage> -> <to stage>

Verdict:
- <PASS | CONCERNS | FAIL>

Evidence checked:
- <file, asset name, command, log, or manual evidence>

Required checks:
- [PASS] <check>
- [CONCERNS] <check>
- [FAIL] <check>
- [MANUAL] <check>

Blockers:
- <Only items that make the next stage unsafe>

Advisory concerns:
- <Items that should be handled soon but do not necessarily block>

Recommended next skill:
- $<skill-name> — <why>

Optional state update:
- If the user wants persistent state, update Saved/CodexWorkflow/ue-stage.md to <stage>.
```

## UE Gate Checklist

### Brief -> Plan

```text
[ ] Goal is one sentence and testable.
[ ] Owning module/system is known.
[ ] Blueprint/C++/asset responsibilities are split.
[ ] Network/save/performance/platform constraints are named.
[ ] Validation path exists.
```

### Plan -> Implementation

```text
[ ] Files/assets to inspect or change are named.
[ ] Module dependencies are known.
[ ] Blueprint handoff is planned for exposed C++ APIs.
[ ] Tests or editor/PIE smoke checks are planned.
[ ] Explicit packaging is absent unless requested by the user.
```

### Validation -> Packaging Readiness

```text
[ ] Targeted build or syntax check result exists, or limitation is stated.
[ ] Blueprint compile and graph checks are described.
[ ] Runtime/editor module split is reviewed.
[ ] Asset references, maps, plugins, and platform settings are reviewed.
[ ] Package automation is not run unless explicitly requested.
```
