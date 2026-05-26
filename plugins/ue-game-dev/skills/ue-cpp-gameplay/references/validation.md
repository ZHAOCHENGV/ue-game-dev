# UE C++ Validation Checklist

## Build Checks

- Build the touched target with the same engine install the project uses.
- If UHT reflection changed, confirm generated code succeeds and Blueprint-exposed names are stable.
- For module changes, regenerate project files only when descriptors or module layout changed.
- Treat UHT errors as source-of-truth for reflection metadata, include order, and generated header placement.
- Resolve warnings that indicate invalid reflection metadata, deprecated APIs, or editor/runtime dependency leaks.

## Runtime Checks

- Start PIE for gameplay paths that depend on world, possession, input, collision, or assets.
- Check logs for ensures, warnings, missing assets, failed loads, invalid casts, and replication warnings.
- For editor-facing properties, confirm defaults and categories are usable in Details panels.
- For asset references, confirm packaging-sensitive paths use soft references or primary assets where appropriate.
- For multiplayer-sensitive code, run server plus at least one client or explain why the path is local-only.

## Blueprint API Checks

- Search for each new `BlueprintCallable`, `BlueprintPure`, event, delegate, or property by its expected node/display name.
- Confirm target pin source, input pin types, output handling, and graph placement.
- Compile at least one consuming Blueprint or provide exact editor validation steps when assets cannot be edited here.

## Handoff Evidence

- Record target name, command or editor action, result, and first remaining risk.
- Include PIE map, actor path, input/action, and expected visible result for gameplay changes.
- If validation is blocked by missing Unreal Editor access, state the precise command or editor check the user should run.
