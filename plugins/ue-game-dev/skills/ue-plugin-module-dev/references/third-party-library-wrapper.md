# Third-Party Library Wrapper Patterns

## Boundary Shape

- Put vendor binaries, headers, and platform glue behind a plugin or module boundary.
- Expose Unreal-friendly wrapper types to the rest of the project instead of leaking vendor types into gameplay modules.
- Keep public headers small. Prefer wrapper interfaces, `USTRUCT` DTOs, or subsystem APIs over direct vendor includes.
- Add platform-specific library paths and delay-load settings in `.Build.cs` only where the vendor library is used.

## Module Layout

Common options:

- Runtime plugin module: wraps a library used in packaged builds.
- Editor plugin module: wraps an SDK used only by editor tools.
- ThirdParty folder: stores vendor headers/libs under the plugin when redistribution is allowed.
- Separate shared contracts module: exposes only DTOs/interfaces when multiple feature modules consume the wrapper.

## Build.cs Review

- Add include paths only for the wrapper module when possible.
- Link only platform-compatible `.lib`, `.a`, `.dll`, `.dylib`, or framework files.
- Keep runtime DLL staging explicit when packaged builds need vendor binaries.
- Avoid adding vendor include paths to broad project modules.
- Gate platform-specific settings with `Target.Platform`.

## Runtime Safety

- Convert vendor callbacks to Unreal delegates or subsystem events on the game thread.
- Convert vendor strings, arrays, errors, and handles into Unreal types at the boundary.
- Own vendor handles with deterministic cleanup in subsystem deinitialize, module shutdown, or wrapper destructors.
- Do not call blocking vendor APIs from the game thread unless the vendor guarantees they are non-blocking.

## Packaging Risks

- Missing staged DLLs or dynamic libraries.
- Editor-only SDK linked from a runtime module.
- Vendor headers leaking into public headers and forcing broad dependency churn.
- Platform-specific binaries checked into the wrong path.
- License or redistribution restrictions on bundled binaries.

## Handoff

- Use `$ue-external-services` if the library primarily talks to HTTP, WebSocket, TCP, or backend services.
- Use `$ue-async-systems` if the wrapper needs worker threads, callback handoff, cancellation, or async Blueprint nodes.
- Use `$ue-performance-packaging` when the wrapper works in editor but fails cook/package/stage.
