# UE Stage Report Template

```text
UE Stage Report

Detected stage:
- <Onboarding | Feature Brief | Implementation Plan | Implementation | Validation | Packaging Readiness | Explicit Packaging>

Confidence:
- <High | Medium | Low> — <why>

Evidence:
- Project:
- Engine:
- Source/modules:
- Plugins:
- Config:
- Blueprint/assets:
- Tests/validation:
- Packaging/release:
- Saved/CodexWorkflow:

Missing or risky artifacts:
- <Gap, risk, or unknown>

Recommended next skill:
- $<skill-name> — <why>

Suggested persistent workflow files:
- Saved/CodexWorkflow/project-profile.md
- Saved/CodexWorkflow/active-task.md
- Saved/CodexWorkflow/ue-stage.md
```

## Heuristics

- Existing UE project + no project report: Onboarding.
- User has a feature idea but no clear owning module/assets: Feature Brief.
- Feature has clear behavior but no work breakdown: Implementation Plan.
- Files changed or user asks to implement directly: Implementation.
- User asks "is it done", "how to test", or "verify": Validation.
- User asks package readiness, cook errors, or release risk: Packaging Readiness.
- User asks `RunUAT`, `BuildCookRun`, one-click package, archive, or CI build: Explicit Packaging.
