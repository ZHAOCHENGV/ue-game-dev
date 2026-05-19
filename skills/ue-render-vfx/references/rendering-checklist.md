# Rendering And Material Checklist

## Renderer Context

- Confirm target platform, renderer path, scalability level, and project renderer settings.
- Check whether Nanite, Lumen, VSM, forward shading, MSAA, translucency, or mobile constraints apply.

## Materials

- Review instruction count, texture samples, overdraw, static switches, and WPO cost.
- Prefer instances for tuning and material functions for shared logic.
- Keep parameter defaults safe and names clear.
- Watch for unsupported nodes on mobile or feature-level-limited targets.

## Shaders And Permutations

- Avoid unnecessary static switches and feature flags.
- Keep custom HLSL inputs explicit.
- Check shader compile output when adding permutations.

## Visual Debugging

- Test bounds/culling, LODs, post process volumes, lighting channels, exposure, and scalability changes.
