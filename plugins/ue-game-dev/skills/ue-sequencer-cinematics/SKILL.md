---
name: ue-sequencer-cinematics
description: Unreal Engine Sequencer and cinematics workflow for LevelSequence, MovieScene tracks, camera cuts, cutscenes, gameplay-triggered sequences, binding, take recorder, Movie Render Queue, cinematic assets, event tracks, and packaged playback validation. Use when requests involve Sequencer, Level Sequence, cutscenes, cinematics, camera tracks, Movie Render Queue, or rendered cinematic output.
---

# UE Sequencer Cinematics

Use this skill for Sequencer, cutscenes, Level Sequences, and Movie Render Queue workflows. Keep asset binding, playback ownership, and packaged behavior explicit.

## First Pass

1. Locate Level Sequence assets, sequence actors, camera actors, event tracks, binding overrides, gameplay triggers, and render settings.
2. Identify whether the task is runtime playback, authored cutscene, cinematic camera work, event synchronization, Take Recorder, or Movie Render Queue output.
3. Map ownership: level placed sequence actor, spawned player, subsystem/controller trigger, Blueprint, or C++ playback wrapper.
4. Check whether actors are possessed/spawned, whether bindings survive level streaming, and whether events need authority or local-only behavior.
5. Define validation: PIE playback, skipped/interrupted playback, packaged build, audio sync, camera restore, and render output.

## Sequencer Rules

- Keep actor bindings stable; use binding overrides when runtime actors differ from editor-authored actors.
- Define camera cut ownership and how view target returns after playback.
- Treat event tracks as integration points, not hidden gameplay authority.
- Keep level streaming and World Partition actor availability in mind when sequences reference level actors.
- Avoid using cinematic tracks to mutate long-lived gameplay state without a clear handoff.

## Movie Render Queue Rules

- Separate runtime playback validation from offline render validation.
- Keep output format, resolution, anti-aliasing, warmup, and console variables explicit.
- Check shot names, frame ranges, audio, and camera cuts before long renders.
- Confirm render-only settings do not leak into packaged gameplay assumptions.

## Integration Rules

- Use `$ue-client-ui` for dialogue UI, subtitles, skip prompts, or cinematic HUD suppression.
- Use `$ue-audio` when timing depends on MetaSound, Quartz, dialogue, or spatial audio.
- Use `$ue-world-streaming` when sequences cross streamed levels, World Partition cells, or Data Layers.

## References

- Read `references/sequencer-cinematics-checklist.md` before implementing or reviewing Sequencer playback, bindings, events, or Movie Render Queue output.
