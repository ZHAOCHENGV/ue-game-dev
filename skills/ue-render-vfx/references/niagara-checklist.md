# Niagara Checklist

## System Design

- Choose CPU simulation for gameplay-facing collision/events that need CPU data.
- Choose GPU simulation for high-count visual particles when CPU readback is not needed.
- Use user parameters for gameplay-driven values.
- Keep shared logic in modules when reused.

## Reliability

- Set fixed bounds for GPU emitters or effects that disappear unexpectedly.
- Confirm auto-activation, pooling, warmup, and reset behavior.
- Check local/world space assumptions and attachment behavior.

## Performance

- Review spawn rate, update scripts, collision, events, renderer count, translucent overdraw, and tick behavior.
- Add LOD/scalability rules for frequent or persistent effects.
- Validate effect lifetime and cleanup for pooled actors/components.
