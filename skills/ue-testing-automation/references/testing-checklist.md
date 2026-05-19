# Testing Checklist

## Choose The Layer

- Pure C++ behavior: `AutomationSpec`, simple automation tests, or regular unit-style helpers inside an Unreal automation test.
- UObject and reflection API: automation test that constructs objects with `NewObject`, checks metadata-facing behavior, and avoids editor-only dependencies unless required.
- Blueprint-facing API: C++ contract test plus Blueprint compile or editor smoke validation.
- Runtime gameplay: PIE or Functional Test map with explicit setup actors and expected state.
- Networked gameplay: server plus at least one client; verify authority, ownership, replication, RPC order, prediction, and late join behavior when relevant.
- Editor tooling: editor automation or smoke path for startup registration, command execution, UI creation, transactions, undo/redo, package dirtiness, and shutdown cleanup.
- Asset pipeline: asset validation pass for naming, folder policy, references, redirectors, Blueprint compile, DataAsset required fields, material/Niagara/animation setup, and cookability.
- Packaging: targeted cook/package smoke for touched platform and module set.

## Plugin And Module Checks

- `.uplugin` lists test/editor/runtime modules with correct `Type` and `LoadingPhase`.
- Runtime modules do not depend on `UnrealEd`, `AssetTools`, `PropertyEditor`, `ToolMenus`, or other editor-only modules.
- Editor tests live in editor/test modules rather than shipping runtime modules.
- Public headers remain minimal; tests should not require private headers from another module unless the project has a deliberate friend/test pattern.
- Export macros are present on public types used across module boundaries.

## Assertions To Prefer

- Assert observable behavior: replicated value changed, ability activated, widget state updated, asset was created, command registered, or package cooked.
- Assert failure behavior: invalid input rejected, missing asset logged, authority denied, RPC ignored, task aborts cleanly, or tool reports a user-facing error.
- Assert cleanup: delegates removed, timers cleared, spawned actors destroyed, tabs unregistered, customizations unregistered, and transient packages not left dirty.
- Assert naming using the project convention first, then Epic-style asset pattern `[AssetTypePrefix]_[AssetName]_[Descriptor]_[OptionalVariantLetterOrNumber]`.

## Run Notes

- Prefer targeted filters over running all editor automation during iteration.
- Record the exact Unreal version and target because automation behavior can differ across UE4, UE5.0-5.4, UE5.5, UE5.6, and later versions.
- When a full automation run is too expensive, keep a fast smoke path plus a named manual validation path.
- Treat a passing compile as insufficient for Blueprint, editor tool, networking, rendering, Niagara, animation, and packaging changes.
