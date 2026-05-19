# UE C++ Coding Standard Checklist

## Naming

- Use Unreal prefixes: `A`, `U`, `F`, `E`, `I`, `S`, `T`.
- Prefix booleans with `b`.
- Keep public API names descriptive and stable.
- Keep module API macros correct for cross-module public types.

## Headers

- Include only what the header needs.
- Prefer forward declarations in public headers.
- Put implementation details in `.cpp` or private headers.
- Keep generated header include last in reflected headers.

## Reflection

- Use reflection macros only when needed by Blueprint, serialization, replication, config, editor tooling, or UHT.
- Prefer narrow Blueprint exposure.
- Avoid exposing mutable authoritative state as `BlueprintReadWrite`.
- Keep metadata meaningful and sparse.

## UObject Safety

- Use `UPROPERTY` for UObject references that must be tracked by GC.
- Use `TObjectPtr` in reflected object members for UE5 codebases where project style supports it.
- Use `TWeakObjectPtr` for cached non-owning references.
- Use soft references for assets/classes that should not force load.
- Validate UObject lifetimes before async/delegate use.

## Runtime Behavior

- Disable Tick by default.
- Prefer events, timers, delegates, and subsystems over polling.
- Unbind delegates and clear timers when lifetimes differ.
- Avoid hard asset loads in constructors and module startup.

## Build Quality

- Keep runtime and editor dependencies separate.
- Keep warning-free builds.
- Verify UHT after reflection changes.
- Add target-specific validation for networking, assets, editor tools, and packaging.
