---
name: ue-external-services
description: Unreal Engine external service integration workflow for HTTP, REST, JSON, WebSocket clients or servers, TCP sockets, backend API clients, streaming responses, heartbeats, reconnect logic, request queues, auth headers, async callbacks, Blueprint handoff, and UI/gameplay event distribution. Use for non-GAS communication with web services or external processes; use ue-gas-networking for Unreal gameplay replication and ability prediction.
---

# UE External Services

Use this skill for Unreal projects that talk to services outside Unreal networking: REST APIs, JSON backends, WebSocket streams, TCP sockets, telemetry services, local companion apps, or tool servers. Keep service clients separate from gameplay authority and UI presentation.

## First Pass

1. Identify protocol and ownership: HTTP request, REST client, WebSocket stream, TCP socket, local process, editor-only service, runtime service, or dedicated server service.
2. Read the owning module `.Build.cs` and confirm dependencies such as `HTTP`, `Json`, `JsonUtilities`, `WebSockets`, `Sockets`, or `Networking`.
3. Decide where the client lives: GameInstance subsystem, World subsystem, LocalPlayer subsystem, Editor subsystem, module service, or actor component.
4. Define message contracts: request structs, response structs, error shape, retry rules, auth headers, and versioning.
5. Define callback flow: service callback -> parse/validate -> game-thread handoff -> subsystem delegate -> UI/gameplay listener.

## Implementation Rules

- Keep external service code out of GAS replication logic. Backend APIs do not replace server authority for gameplay state.
- Prefer subsystem-owned clients over scattering HTTP/WebSocket code across widgets or actors.
- Add module dependencies intentionally and keep editor-only service clients out of runtime modules when they are tool-only.
- Parse JSON into typed structs or narrow DTOs before updating gameplay/UI state.
- Treat network errors, invalid JSON, timeout, auth failure, and server error as first-class results.
- Use weak owner captures for async callbacks. Validate owner and world before broadcasting.
- Broadcast to UI/gameplay on the game thread through delegates, events, or view models already used by the project.
- Do not block the game thread on socket reads, HTTP completion, or reconnect delays.

## Protocol Guidance

- Use HTTP for request/response APIs, login, inventory queries, telemetry submission, or one-shot backend calls.
- Use WebSocket for persistent bidirectional streams, chat, live notifications, tool events, or streaming service state.
- Use TCP sockets only when the service protocol requires raw sockets or a local tool has a custom framing protocol.
- Use `$ue-async-systems` when CPU work, blocking IO, or Blueprint async node shape dominates the design.

## References

- Read `references/service-client-patterns.md` for HTTP, JSON, WebSocket, TCP, retries, heartbeat, reconnect, and subsystem ownership patterns.
- Read `references/http-service-template.md` when the task needs a reusable HTTP service client shape.
- Use `$ue-client-ui` when the remaining task is UI presentation or widget state.
- Use `$ue-save-load-sync` when external service responses must persist locally or reconcile with durable saved state.
- Use `$ue-gas-networking` only when the question is Unreal gameplay replication, GAS prediction, RPC authority, or replicated ability state.
