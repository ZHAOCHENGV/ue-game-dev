# UE Intake Checklist

## Classify The Request

```text
[ ] Is there a local .uproject path?
[ ] Is the user asking to understand an existing project first?
[ ] Is this a new feature, bug, refactor, test, performance, or packaging request?
[ ] Is the requested outcome player-facing, designer-facing, editor-facing, or release-facing?
[ ] Is the owning area clear: C++, Blueprint, UI, GAS/networking, input, AI, animation, rendering, plugin/module, or packaging?
[ ] Is there enough information to implement, or should this become a feature brief first?
```

## Minimal Questions

Ask only the first blocker:

- Project path when no `.uproject` is discoverable.
- Target UE version when multiple engine installs matter.
- Target platform when packaging/performance/platform settings matter.
- Expected behavior and current behavior when debugging.
- Whether Codex should stay read-only when touching an old project.

## Routing Examples

| Request | Stage | Next skill |
|---------|-------|------------|
| "先熟悉这个旧项目" | onboarding | `$ue-project-onboarding` |
| "我要做一个背包系统，先帮我想清楚" | brief | `$ue-feature-brief` |
| "按这个需求写实施计划" | plan | `$ue-implementation-plan` |
| "蓝图输入事件不触发" | debug/input | `$ue-input-enhanced` or `$ue-debug-validation` |
| "打包失败，看日志" | packaging diagnostic | `$ue-performance-packaging` |
| "生成 RunUAT 一键打包脚本" | explicit packaging automation | `$ue-build-release-automation` |
