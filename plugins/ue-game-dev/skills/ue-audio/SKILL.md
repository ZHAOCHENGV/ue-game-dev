---
name: ue-audio
description: Unreal Engine audio workflow for MetaSound, Sound Cue, AudioComponent, Sound Classes, Sound Mixes, Sound Concurrency, Quartz timing, spatialization, attenuation, audio debugging, audio performance, and platform audio settings. Use when requests involve gameplay audio, adaptive music, sound effects, runtime audio components, or audio performance.
---

# UE Audio

Use this skill for Unreal gameplay audio, adaptive music, runtime sound playback, and audio debugging. Keep audio authored for designers while making ownership, lifetime, and performance explicit.

## First Pass

1. Identify the audio stack: MetaSound, Sound Cue, raw Sound Wave, AudioComponent, Quartz, Sound Class/Mix, or middleware.
2. Map who owns playback: Actor, component, subsystem, UI widget, Anim Notify, Niagara event, or gameplay ability.
3. Check whether sound is local-only, replicated by gameplay event, or server-authoritative state that triggers client presentation.
4. Locate attenuation, concurrency, Sound Class, Sound Mix, and platform audio settings before changing behavior.
5. Decide whether the work belongs in assets, Blueprint, C++, or a hybrid.

## Runtime Audio Rules

- Use `UAudioComponent` for sounds that need lifetime control, parameter updates, fades, or attachment.
- Use fire-and-forget helpers only for short, stateless one-shot sounds.
- Keep gameplay authority separate from audio presentation; replicate gameplay events, not raw audio playback.
- Stop or fade owned AudioComponents on owner destruction, state exit, or level transition.
- Route reusable audio policy through subsystems, components, data assets, or existing audio managers.

## MetaSound And Sound Cue

- Prefer MetaSound for procedural, parameterized, or adaptive UE5 audio graphs.
- Use Sound Cues when the project already standardizes on them or only needs simple randomization/routing.
- Name parameters clearly and document which gameplay owner sets them.
- Validate parameter update frequency; avoid per-frame audio parameter churn unless it is intentional.

## Mixing And Performance

- Use Sound Classes and Sound Mixes for category-level volume, ducking, and runtime mix state.
- Use Sound Concurrency for repeated effects such as footsteps, weapons, UI clicks, and ambience emitters.
- Configure attenuation and spatialization for world sounds; keep UI sounds non-spatial unless intended.
- Profile with Unreal audio stats when voices, virtualization, streaming, or platform compression are part of the issue.

## Verification

- Validate in PIE with the expected listener, camera, and local-player setup.
- Check start, stop, fade, loop, owner destruction, level transition, and pause behavior.
- For multiplayer, test that each client hears only the intended local or replicated presentation.
- For platform work, confirm compression, streaming, channel count, and concurrency settings on the target platform.

## References

- Read `references/audio-checklist.md` for MetaSound, Sound Cue, AudioComponent, concurrency, attenuation, and profiling checks.
- Use `$ue-blueprint-workflow` when graph-level Blueprint event wiring is the main task.
- Use `$ue-cpp-gameplay` when audio playback requires C++ components, subsystems, or gameplay APIs.
- Use `$ue-gas-networking` when audio is triggered by networked abilities, cues, or replicated combat state.
