# UE Agent Conflict Resolution

Use this file when two or more UE roles disagree, need the same file, or produce incompatible next steps. For simple single-domain tasks, do not load this file; keep the focused workflow light.

## Conflict Types

| Type | Example | Resolver |
|------|---------|----------|
| File ownership | C++ and Architecture both want to edit `.Build.cs`. | Coordinator assigns one owner and serializes changes. |
| Runtime/Editor boundary | C++ role adds editor dependency to runtime module. | Architecture Reviewer advises; Coordinator decides or asks user. |
| Blueprint/C++ handoff | C++ exposes an API but Blueprint Integrator needs different pins/defaults. | C++ Implementer and Blueprint Integrator reconcile through Coordinator. |
| Packaging boundary | Packaging/Release wants to run automation from a readiness review. | Coordinator blocks automation unless user explicitly asked. |
| Evidence conflict | Verifier cannot reproduce a role's COMPLETE claim. | Verifier marks `CONCERNS` or `BLOCKED`; Coordinator updates synthesis. |

## Resolution Protocol

1. Name the conflict and affected files/assets.
2. Identify the owning role for each file or decision.
3. Prefer the project's existing convention over a new abstraction.
4. If one role's change affects another domain, require Coordinator approval before implementation.
5. If the conflict changes user-visible behavior, module architecture, packaging automation, or asset authoring burden, ask the user before proceeding.
6. If required evidence is missing, mark `BLOCKED` instead of guessing.

## Escalation Rules

- Coordinator is the final synthesizer inside the multi-agent workflow.
- Architecture Reviewer has priority for module boundaries, Runtime/Editor split, and dependency direction.
- Verifier has priority for whether something can be called `COMPLETE`.
- Blueprint Integrator has priority for designer-facing handoff clarity.
- Packaging/Release cannot override the explicit packaging boundary.

## Blocking Conditions

Mark `BLOCKED` when:

- A role would need to edit outside its ownership boundary.
- `.uasset` internals are required but only filenames are available.
- Build, editor, or logs are required but inaccessible.
- The user has not explicitly approved packaging automation.
- Two implementation options have different product or design consequences.

## Output Snippet

```text
Conflict And Blocker Log
- Status: BLOCKED
- Conflict: Runtime module dependency would pull editor-only code into packaged build.
- Roles: UE Architecture Reviewer, C++ Implementer, Packaging/Release
- Affected files: Source/<Module>/<Module>.Build.cs
- Coordinator decision: stop implementation and ask user to choose runtime-safe design or editor-only module split.
```
