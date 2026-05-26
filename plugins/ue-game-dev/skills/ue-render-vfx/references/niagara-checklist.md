# Niagara Checklist

## System Design

- Choose CPU simulation for gameplay-facing collision/events that need CPU data.
- Choose GPU simulation for high-count visual particles when CPU readback is not needed.
- Use user parameters for gameplay-driven values.
- Keep shared logic in modules when reused.
- Decide whether the system is one-shot, looped, pooled, attached, or world-placed.
- Keep spawn ownership clear: Blueprint, C++, Anim Notify, GameplayCue, or placed actor.

## Reliability

- Set fixed bounds for GPU emitters or effects that disappear unexpectedly.
- Confirm auto-activation, pooling, warmup, and reset behavior.
- Check local/world space assumptions and attachment behavior.
- Validate User Parameter names, default values, and update frequency.
- Check emitter reset behavior when reused by pooled components.

## Performance

- Review spawn rate, update scripts, collision, events, renderer count, translucent overdraw, and tick behavior.
- Add LOD/scalability rules for frequent or persistent effects.
- Validate effect lifetime and cleanup for pooled actors/components.
- Prefer GPU emitters for high particle counts only when collision/readback constraints allow it.
- Keep bounds tight enough for culling but large enough to avoid popping.
- Watch translucent material overdraw, light usage, ribbon/trail count, and distance field collisions.

## Debugging

- Use Niagara Debugger to inspect active systems, parameter values, emitter state, and tick cost.
- Toggle solo emitters to isolate which emitter causes a visual or performance issue.
- Capture system asset path, owner, activation path, platform/scalability level, and reproduction camera angle.
