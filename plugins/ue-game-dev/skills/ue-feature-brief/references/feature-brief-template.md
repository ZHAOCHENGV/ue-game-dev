# UE Feature Brief Template

```text
UE Feature Brief

Goal
- <One sentence describing the player/designer/editor outcome.>

Project Context
- Project:
- UE version:
- Target platform:
- Existing systems/assets found:

Ownership
- C++:
- Blueprint:
- Assets/data:
- UI:
- Networking/GAS:
- Editor/runtime module:

Behavior
- Trigger:
- Success result:
- Failure/edge result:
- Feedback to player/designer:
- State changes:
- Data/assets involved:

Constraints
- Authority/replication:
- Save/load:
- Performance:
- Packaging/platform:
- Naming/module conventions:
- Accessibility/localization:
- Editor/runtime boundary:

Validation
- C++ build:
- Blueprint compile:
- PIE/editor smoke:
- Automated test or asset validation:
- Multiplayer/client count:
- Cook/package smoke if relevant:

Open Questions
- <Only blockers that cannot be answered from local inspection.>

Recommended Next Skill
- $ue-implementation-plan or a domain skill:
```

## Example Snippet

```text
Goal
- Let the player pick up nearby items and see inventory feedback immediately.

Ownership
- C++: inventory component owns durable item state and validation.
- Blueprint: pickup actor handles prompt visibility and designer-authored feedback.
- UI: inventory widget listens for inventory-changed events and refreshes manually.

Validation
- C++ build: touched game module.
- Blueprint compile: pickup actor and inventory widget.
- PIE/editor smoke: overlap prompt, use input, inventory count, full-inventory failure.
```

Use the brief to remove ambiguity. If the brief already requires concrete file changes, move to `$ue-implementation-plan` or the most specific domain skill.
