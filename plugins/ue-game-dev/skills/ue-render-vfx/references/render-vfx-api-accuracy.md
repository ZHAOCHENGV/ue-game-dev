# Rendering And Niagara API Accuracy Notes

Use this reference before writing Unreal rendering, material, or Niagara guidance. It focuses on concrete engine concepts and common hallucination traps.

## Materials

- Prefer Material Instances for tuning and Material Functions for reusable graph logic.
- Static switches change shader permutations; scalar/vector/texture parameters tune instances without multiplying permutations the same way.
- Dynamic Material Instances are runtime objects; define owner, lifetime, and parameter update frequency.
- Custom HLSL nodes need explicit inputs and platform assumptions. Avoid promising engine shader APIs without checking the project version.

## Renderer Features

- Nanite, Lumen, Virtual Shadow Maps, forward rendering, mobile, VR, and console-like targets have different constraints.
- Treat renderer config changes as project-wide risk. Mention scalability groups and platform checks when changing them.
- For render targets and scene captures, check update frequency, resolution, format, memory cost, and ownership.

## Niagara

- CPU and GPU emitters have different collision, event, and data access limits.
- GPU emitters often need fixed bounds; missing bounds can look like random culling.
- Prefer user parameters for gameplay-driven values instead of duplicating systems.
- Check emitter/system scalability, spawn counts, tick cost, and renderer count before approving frequent or persistent effects.

## Evidence

- Include viewport/PIE visual validation.
- Include material stats, shader compile notes, Niagara debug evidence, or Unreal Insights when performance is part of the task.
