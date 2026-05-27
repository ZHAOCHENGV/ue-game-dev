---
name: ue-testing-automation
description: Unreal Engine testing automation workflow for plugin and gameplay features, AutomationSpec, FAutomationTestBase, Functional Tests, editor smoke tests, PIE and multiplayer scenarios, asset validation, packaging smoke checks, and regression planning. Use when adding, reviewing, or deciding test coverage for UE C++, Blueprint, editor tooling, GAS, networking, UI, rendering, AI, animation, or plugin/module changes.
---

# UE Testing Automation

Use this skill when Unreal work needs a repeatable validation path. Prefer the smallest automated or scripted check that proves the behavior, then add manual editor/PIE checks only where the engine surface cannot be automated reasonably.

## First Pass

1. Read the `.uproject`, plugin descriptors, module `.Build.cs` files, existing test modules, `Source/*/Tests`, `Config`, and any CI/build scripts.
2. Identify the changed surface: pure C++, UObject/Blueprint API, editor tool, asset pipeline, gameplay runtime, networked flow, UI, rendering/VFX, AI, animation, packaging, or migration.
3. Choose the test layer that catches the failure closest to its source.
4. Confirm required dependencies are in the correct module only. Keep editor test dependencies out of runtime modules.
5. Define how the test runs: commandlet, automation filter, editor automation, PIE, functional map, multi-client PIE, dedicated server, cook/package smoke, or manual verification.

## Test Selection

- Use `AutomationSpec` for readable C++ behavior tests, async latent steps, and scenario-style coverage.
- Use `FAutomationTestBase` or simple automation tests for narrow engine/API checks.
- Use Functional Tests for map-based gameplay validation, actor interaction, level setup, and designer-visible scenarios.
- Use editor automation or smoke tests for ToolMenus, tabs, factories, details customizations, asset actions, import/reimport, and editor subsystems.
- Use PIE or multiplayer PIE scenarios for possession, authority, prediction, replication, RPC, GAS activation, UI tied to local players, and save/restore flows.
- Use asset validation checks for naming, required tags, folder policy, Blueprint compile status, redirectors, DataAssets, materials, Niagara systems, and animation asset setup.
- Use packaging smoke checks for module descriptor mistakes, editor dependency leaks, cook failures, missing assets, shader/cook errors, and platform-specific runtime assumptions.

## Implementation Rules

- Put test code in a dedicated test module or clearly scoped test folder that matches the project pattern.
- Name tests by behavior and feature, not implementation detail.
- Keep tests deterministic: avoid real time sleeps, random asset discovery order, editor selection state, and global state pollution.
- Avoid loading the whole project or all assets unless the test is explicitly an asset audit.
- Clean up transient objects, packages, spawned actors, delegates, console variables, and subsystem state after each test.
- For Blueprint-exposed APIs, cover the C++ contract and include a Blueprint compile or smoke validation path when graphs are involved.
- For plugin work, validate Runtime and Editor modules separately.
- For multiplayer work, state the server/client count, authority expectation, replicated property or RPC path, and expected client-observed result.
- For editor tools, verify registration/unregistration symmetry and run at least one startup/shutdown or reopen smoke path.
- For rendering, Niagara, and animation, combine automated asset/config checks with a visual or performance sanity path when pixels or motion matter.

## Output Shape

- State the risk being tested.
- List the selected test layer and why it fits.
- Identify files/modules that should own the test.
- Provide concrete test cases with setup, action, expected result, and cleanup.
- Provide the run command or editor path when known.
- State any manual validation that remains.

## References

- Read `references/testing-checklist.md` for test type selection, plugin-specific checks, assertions, and run notes.
- Read `references/automation-test-template.md` when the output needs a concrete Automation Test or Functional Test skeleton.
- Use `$ue-debug-validation` when first reproducing an unknown failure.
- Use `$ue-performance-packaging` when validation includes cook, packaging, profiling, or release readiness.
- Use `$ue-plugin-module-dev` when test dependencies require module or descriptor changes.
