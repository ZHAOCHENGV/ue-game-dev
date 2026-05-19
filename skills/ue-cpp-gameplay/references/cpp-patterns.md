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
