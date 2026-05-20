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

## Probable Root Cause
- Cause:
- Why this is the first failure:
- Downstream symptoms:

## Inspection Targets
- Files:
- Assets:
- Config:
- Logs still needed:

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
