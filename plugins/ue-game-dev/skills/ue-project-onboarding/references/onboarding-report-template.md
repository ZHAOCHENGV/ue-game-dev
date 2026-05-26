# UE Project Onboarding Report Template

```text
# UE Project Onboarding Report

## Project Snapshot
- Path:
- Project:
- Engine:
- Modules:
- Enabled plugins:
- Target platforms:
- Source control/worktree state:

## Code Structure
- Runtime modules:
- Editor modules:
- Important classes:
- Important config:
- Build targets:
- Third-party dependencies:
- Generated or external code:

## Asset Structure
- Maps:
- Blueprints:
- UI:
- Input:
- Data:
- GAS / AI / Animation / Rendering:
- Audio / world streaming:
- Naming conventions observed:

## Main Flows
- Startup:
- Input:
- Gameplay:
- UI:
- Save/load:
- Networking/GAS:
- Async/external services:
- Packaging/release:

## Blueprint/C++ Boundary
- C++ owns:
- Blueprint owns:
- Unknowns requiring editor inspection:

## Risks
- Build/module:
- Asset references:
- Runtime/editor boundary:
- Networking/authority:
- Packaging/performance:
- Missing editor-only evidence:
- High-risk unknowns:

## Safe Next Steps
- Recommended next skill:
- Smallest next task:
- Suggested validation:
- Files/assets to inspect next:
```

## Filling Guidance

- Keep this report read-only: summarize what was found, not what should be changed immediately.
- Use exact file paths for modules, config, and representative assets.
- Separate confirmed facts from hypotheses and unknowns.
- Prefer "not found in scan" over "does not exist" when editor-only asset inspection was unavailable.
- Recommend one smallest next task so secondary development can start without re-auditing the whole project.
