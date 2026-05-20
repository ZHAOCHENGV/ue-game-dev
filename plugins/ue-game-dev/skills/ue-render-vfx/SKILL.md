---
name: ue-render-vfx
description: Unreal Engine rendering, material, shader, and Niagara VFX workflow. Use for material graphs, material functions, custom HLSL, post process, renderer settings, lighting, LODs, Niagara systems, particles, GPU emitters, visual bugs, shader permutation cost, and rendering or VFX performance issues.
---

# UE Render VFX

Use this skill for visual features and visual performance. Treat assets, scalability, and platform constraints as part of the implementation.

## First Pass

1. Identify the target renderer and platform: deferred/forward, Nanite, Lumen, virtual shadow maps, mobile, VR, or console-like constraints.
2. Determine whether the work belongs in material graph, material function, Niagara, Blueprint, C++, post process, or renderer config.
3. Inspect nearby materials, Niagara systems, scalability settings, and naming conventions before adding assets or code.
4. For visual bugs, separate asset authoring problems from runtime state, bounds/culling, shader permutations, and platform feature support.

## Materials And Shaders

- Prefer material functions for reusable graph logic and material instances for tunable variations.
- Keep static switches intentional; each switch can multiply shader permutations.
- Use parameters with clear names and default values that are safe for instances.
- Watch instruction count, texture sample count, translucent overdraw, world-position-offset cost, and expensive per-pixel math.
- For custom HLSL, keep inputs explicit and document assumptions near the node or helper code.

## Niagara

- Define whether simulation is CPU or GPU and why.
- Set fixed bounds when GPU emitters or culling make effects disappear.
- Keep spawn/update scripts lean; move shared logic into modules when reused.
- Use user parameters for gameplay-driven values instead of duplicating systems.
- Validate LOD/scalability behavior for effects that appear often or persist.

## Verification

- Use a viewport/PIE visual pass for framing, culling, bounds, material parameter changes, and effect timing.
- Use shader compile output, material stats, Niagara debug tools, or Unreal Insights when performance is part of the task.
- Mention asset-side work that cannot be fully represented in text/code.

## References

- Read `references/rendering-checklist.md` for material, shader, and renderer review.
- Read `references/niagara-checklist.md` for Niagara authoring and debugging.
