# Sequencer Cinematics Checklist

Use this checklist for Level Sequence, Sequencer, camera cuts, runtime playback, event tracks, Take Recorder, and Movie Render Queue work.

## Discovery

- Locate Level Sequence assets, sequence actors, cameras, event tracks, audio tracks, binding overrides, and playback triggers.
- Identify whether actors are possessables, spawnables, streamed level actors, or runtime-spawned actors.
- Check whether playback is local-only, server-triggered, replicated by gameplay state, or offline render-only.

## Runtime Playback

- Define playback owner and interruption policy.
- Restore camera/input/UI state after playback.
- Validate skipped playback and missing binding behavior.
- Keep gameplay authority outside cinematic-only event tracks unless explicitly designed.

## Render Output

- Confirm Movie Render Queue preset, resolution, frame range, anti-aliasing, warmup, output path, audio, and console variables.
- Run a short frame-range test before long renders.
- Record render settings in the final handoff.

## Evidence

- PIE playback result.
- Packaged playback note when the sequence ships in game.
- MRQ test output note when the task is render-focused.
