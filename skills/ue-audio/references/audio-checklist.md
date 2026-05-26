# UE Audio Checklist

## Playback Ownership

- Identify the owner: Actor, component, subsystem, UI widget, Anim Notify, Niagara event, or ability.
- Decide whether playback is one-shot, looped, attached, pooled, or managed by an `UAudioComponent`.
- Define stop/fade behavior for owner destruction, state exit, map travel, pause, and retry paths.
- For multiplayer, replicate gameplay events or cues; do not replicate raw audio state unless the project has a specific audio sync layer.

## MetaSound And Sound Cue

- Use MetaSound for procedural graphs, parameterized adaptive audio, and UE5-native audio logic.
- Use Sound Cue for simple randomization, modulation, and legacy project consistency.
- Name exposed parameters by gameplay meaning, for example `EngineRpm`, `HealthRatio`, or `SurfaceType`.
- Keep parameter update rates bounded; prefer event-driven updates or coarse timers over unnecessary per-frame writes.

## AudioComponent

- Use AudioComponents for looping ambience, attached emitters, fades, parameter updates, and explicit lifecycle control.
- Store component references with `UPROPERTY` or clear owner lifetime when created in C++.
- Validate `AutoActivate`, attachment socket, attenuation override, and whether the component persists across owner state changes.
- Stop or fade components before destroying the owner when abrupt cuts are undesirable.

## Mixing, Concurrency, And Spatialization

- Use Sound Classes for category volume and Sound Mixes for runtime ducking or mix transitions.
- Configure concurrency for repeated effects: footsteps, UI clicks, impacts, weapons, and ambient emitters.
- Check voice limit, resolution rule, retrigger time, and virtualization behavior.
- For world sounds, validate attenuation shape, falloff, occlusion, spatialization, and listener position.
- For UI sounds, keep them non-spatial and local-player scoped unless the design says otherwise.

## Platform And Profiling

- Confirm compression, streaming, sample rate, and channel count for the target platform.
- Use `stat audio` and the Audio Insights tooling when voices, source count, or CPU cost is suspected.
- Test cooked builds when platform codec, streaming, or asset cooking behavior is part of the risk.
- Capture the first audible symptom, expected behavior, asset path, owner, and runtime trigger in any handoff report.
