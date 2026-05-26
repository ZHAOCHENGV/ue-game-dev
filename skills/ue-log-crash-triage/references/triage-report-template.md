# UE Log/Crash Triage Report Template

````markdown
# UE Log/Crash Triage

## Source
- Log path or pasted source:
- Timestamp:
- UE version:
- Project/module:
- User action before failure:

## First Actionable Failure
```text
<short excerpt around the first actionable error>
```

## Classification
- Phase: Build / UHT / Link / Editor / PIE / Blueprint Compile / Cook / Stage / Package / Runtime
- Subsystem:
- Recommended next skill:
- Confidence: High / Medium / Low
- Boundary: diagnosis only / fix candidate / packaging automation explicitly requested

## Probable Root Cause
- Cause:
- Why this is the first failure:
- Downstream symptoms:
- Similar-looking noise to ignore:

## Inspection Targets
- Files:
- Assets:
- Config:
- Logs still needed:
- Commands to rerun:

## Fix Path
1.
2.
3.

## Verification
- Command:
- Editor check:
- Manual smoke:

## Workflow State Update
- Add to `Saved/CodexWorkflow/known-risks.md`: yes/no
- Risk entry:
````

## Classification Notes

- UHT errors usually point at reflection metadata, generated header placement, missing includes, or invalid Blueprint exposure.
- Link errors usually point at module dependencies, missing implementation, export macros, or third-party library linkage.
- Cook failures often report many follow-on asset errors; choose the first missing class, failed load, Blueprint compile error, or assert that explains the cascade.
- Runtime crashes need callstack frame ownership before proposing fixes; do not confuse the crashing caller with the first invalid state.
- Packaging automation stays out of scope unless the user explicitly asks to run or generate `RunUAT`/`BuildCookRun`.
