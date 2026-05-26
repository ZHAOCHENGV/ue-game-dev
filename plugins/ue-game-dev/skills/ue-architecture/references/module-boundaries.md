# UE Architecture Boundary Checklist

## Module Types

- Runtime layer: gameplay, client runtime, data systems, replicated state.
- Editor layer: asset actions, detail panels, factories, editor utilities.
- Developer/tools layer: build-time or development helpers not needed in packaged runtime.
- Shared contracts layer: interfaces, lightweight types, and data contracts used across systems.

## Dependency Direction

- Higher-level features may depend on lower-level contracts.
- Runtime code must not depend on editor-only layers.
- UI/client code should not own authoritative gameplay state.
- Networking authority should live in server-owned gameplay systems.
- Break cycles with a contracts/common module or interfaces.
- External service clients should depend inward on shared DTOs/contracts; gameplay systems consume typed service events rather than owning HTTP/WebSocket/TCP details.
- Async workers should have an owning subsystem/component/service that defines cancellation and teardown.

## Service Ownership

- Use `UGameInstanceSubsystem` for app/session level clients that must survive map travel.
- Use `UWorldSubsystem` for world/session-scoped services.
- Use `ULocalPlayerSubsystem` for local user state or UI-facing per-player service data.
- Use editor modules or `UEditorSubsystem` for tool-only service integration.
- Keep widgets as subscribers. They should not own network clients, socket loops, or backend auth state.

## Reflection And Assets

- Reflected class/module moves can break Blueprint class paths.
- Public Blueprint APIs are harder to change than private C++ helpers.
- List asset redirector and migration impact before moving classes or renaming modules.

## Output Template

- Module: responsibility
- Public surface: exposed reflected types and intended callers
- Private implementation: hidden systems
- Dependencies: direction and ownership reason
- Risks: cyclic references, asset paths, Blueprint breakage
