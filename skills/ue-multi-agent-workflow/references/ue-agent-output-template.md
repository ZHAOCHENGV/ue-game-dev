# UE Agent Output Template

Use this template only for `lean` or `full` multi-agent runs. For simple tasks, do not use this report shape; answer through the focused UE skill.

```text
UE Multi-Agent Plan
- Mode: solo | lean | full
- Goal:
- Non-goals:
- Selected roles:
- Ownership boundaries:
- Parallel discovery:
- Dependent phases:
- Packaging boundary:

Parallel Discovery Results
- Coordinator: COMPLETE / CONCERNS / BLOCKED
- Project Explorer: COMPLETE / CONCERNS / BLOCKED
- [Specialist]: COMPLETE / CONCERNS / BLOCKED

Role Findings
- [Role]:
  - Evidence:
  - Finding:
  - Risk:
  - Recommended next skill:

Conflict And Blocker Log
- Status: NONE / CONCERNS / BLOCKED
- Owner:
- Reason:
- Decision needed:

Coordinator Synthesis
- Decisions:
- Implementation order:
- Files/assets to touch:
- Files/assets to avoid:
- Recommended next skills:
- Verification path:
- User action needed:
```

## Status Rules

| Status | Meaning |
|--------|---------|
| `COMPLETE` | Role finished its assigned pass with enough evidence. |
| `CONCERNS` | Work can continue, but risk or uncertainty must be carried forward. |
| `BLOCKED` | Required input, permission, editor inspection, build access, or file ownership is missing. |

## Keep It Light

- In `lean` mode, keep role findings to 1-3 bullets per role.
- In `full` mode, include enough evidence to make conflicts reviewable.
- Do not paste full logs. Quote only the first actionable error or concise evidence.
- Do not include this template for a single Enhanced Input issue, one BlueprintCallable handoff, one Blueprint graph fix, or one RunUAT command request.

## Packaging Line

Keep packaging automation explicit-only; a packaging risk review is not permission to run package/build automation.

Always include one line:

```text
Packaging boundary: review only / explicit automation requested / not relevant
```

If it says `review only`, do not route to `$ue-build-release-automation`.
