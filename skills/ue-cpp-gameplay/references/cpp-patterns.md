# UE C++ Gameplay Patterns

## Module And Class Placement

- Put runtime gameplay classes in runtime modules; keep editor-only factories, detail customizations, and asset actions in editor modules.
- Check `.Build.cs` dependencies before adding includes. Prefer adding the narrow module dependency that owns the type.
- Keep public headers stable. Move helpers and private implementation details into `.cpp` or `Private/` headers.

## UObject And Reflection

- Use `TObjectPtr` for reflected UObject references owned or tracked by a UObject.
- Use `TWeakObjectPtr` for cached references that may disappear.
- Use soft references for assets/classes that should not force-load.
- Use `UPROPERTY` for UObject references that must be visible to GC.
- Prefer `BlueprintReadOnly` over `BlueprintReadWrite` unless designers must mutate the value.
- Expose reflection only for a reason: Blueprint access, serialization, config, replication, editor editing, delegates, or asset references.
- Keep `USTRUCT` data transfer types small and stable when they cross Blueprint or service boundaries.

## Subsystems And Settings

- Use `UGameInstanceSubsystem` for runtime services that survive map transitions, such as account/session clients, inventory cache, matchmaking facades, or project-wide managers.
- Use `UWorldSubsystem` for state scoped to a world or PIE instance.
- Use `ULocalPlayerSubsystem` for per-local-player services such as input profile, user UI state, or local platform identity.
- Use `UEditorSubsystem` for editor-only workflow services.
- Use `UDeveloperSettings` for project-configurable defaults and read with `GetDefault<T>()`; use `GetMutableDefault<T>()` only in editor/tooling flows that intentionally edit config.
- Avoid hiding gameplay state in global singletons when a subsystem lifetime would make ownership and teardown clearer.

## Actor And Component Lifecycle

- Constructor: create default subobjects and set defaults only.
- `OnRegister` / `InitializeComponent`: component setup that depends on registration.
- `BeginPlay`: world-ready runtime binding and initial state.
- `EndPlay`: unbind delegates, clear timers, stop async work.
- Avoid gameplay logic in construction scripts that must also run correctly at runtime.

## Delegates And Timers

- Store delegate handles when the source can outlive the listener.
- Guard duplicate binds when setup can run more than once.
- Clear timers in `EndPlay` for Actor-owned behavior.
- Prefer event-driven updates over polling.

## Async And External Boundaries

- Use `$ue-async-systems` for background CPU work, game-thread handoff, `UBlueprintAsyncActionBase`, worker lifetime, and cancellation.
- Use `$ue-external-services` for HTTP, JSON, WebSocket, TCP, backend clients, streaming services, heartbeat, and reconnect logic.
- Keep service DTOs and async result structs separate from authoritative mutable gameplay state.
