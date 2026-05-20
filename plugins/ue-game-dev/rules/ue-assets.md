# UE Asset Rules

- Follow project asset naming conventions before adding new assets.
- Prefer soft references or Primary Asset rules for optional content.
- Check redirectors, missing references, hard-coded paths, and editor-only asset references before packaging readiness.
- Keep runtime assets out of editor-only plugin/module dependencies.
- For UI/input/animation/VFX assets, list exact asset names and expected compile/runtime validation.
- Avoid broad Content scans unless the task is an asset audit; use targeted filename discovery first.
