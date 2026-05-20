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
