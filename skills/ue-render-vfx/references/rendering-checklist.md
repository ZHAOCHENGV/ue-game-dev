# Rendering And Material Checklist

## Renderer Context

- Confirm target platform, renderer path, scalability level, and project renderer settings.
- Check whether Nanite, Lumen, VSM, forward shading, MSAA, translucency, or mobile constraints apply.
- Record viewport/editor vs packaged runtime differences before judging a visual bug.
- Check whether the issue appears at all scalability levels or only a specific profile.

## Materials

- Review instruction count, texture samples, overdraw, static switches, and WPO cost.
- Prefer instances for tuning and material functions for shared logic.
- Keep parameter defaults safe and names clear.
- Watch for unsupported nodes on mobile or feature-level-limited targets.
- Treat high instruction count, many texture samples, expensive translucency, and WPO on dense meshes as review triggers.
- Prefer scalar/vector parameters in instances for tuning instead of duplicating master materials.

## Shaders And Permutations

- Avoid unnecessary static switches and feature flags.
- Keep custom HLSL inputs explicit.
- Check shader compile output when adding permutations.
- Minimize static switch combinations that multiply permutations across platforms, quality levels, and material instances.
- Check derived data cache and shader compile noise when a change appears to stall editor iteration.

## Visual Debugging

- Test bounds/culling, LODs, post process volumes, lighting channels, exposure, and scalability changes.
- Use view modes such as shader complexity, quad overdraw, light complexity, Nanite visualization, and Lumen visualization when relevant.
- Capture asset path, material instance, renderer settings, scalability bucket, camera angle, and expected visual delta.

## VFX Integration

- For Niagara, validate fixed bounds, renderer count, translucent overdraw, collision mode, and scalability rules.
- For post process, validate volume priority, blend weight, unbound state, camera overrides, and platform support.
- For lighting changes, validate exposure, shadow method, virtual shadow maps, Lumen/Nanite assumptions, and mobile fallback.
