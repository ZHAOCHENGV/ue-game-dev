# UE External Service Client Patterns

## Ownership Choices

| Client type | Good owner | Notes |
|-------------|------------|-------|
| Account/session API | `UGameInstanceSubsystem` | Survives map transitions and owns auth/session state |
| World-scoped service | `UWorldSubsystem` | Use when service state belongs to a world/session |
| Per-player backend state | `ULocalPlayerSubsystem` | Good for local user settings, presence, or UI-facing user data |
| Editor-only tool service | `UEditorSubsystem` or editor module singleton | Keep dependencies out of runtime modules |
| Reusable actor-specific endpoint | `UActorComponent` | Use only when lifetime truly follows an actor |

Avoid putting service clients directly in widgets. Widgets should subscribe to subsystem events or view models.

## Build.cs Dependencies

Common runtime dependencies:

```csharp
PrivateDependencyModuleNames.AddRange(new string[]
{
    "HTTP",
    "Json",
    "JsonUtilities",
    "WebSockets",
    "Sockets",
    "Networking"
});
```

Add only the modules needed by the protocol. Keep editor-only dependencies in editor modules.

## HTTP Request Flow

Recommended flow:

1. Build URL, verb, headers, body.
2. Start request through `FHttpModule`.
3. In completion callback, validate owner and response.
4. Parse JSON into a typed DTO or narrow struct.
5. Return to game-thread owned state and broadcast a typed result.

Failure cases to model:

- Request not started.
- Timeout or connection failure.
- Non-2xx response code.
- Empty response body when body is required.
- Invalid JSON.
- Valid JSON with application-level error.
- Owner destroyed before callback.

## JSON Contracts

- Keep wire DTOs separate from authoritative gameplay state.
- Validate required fields before applying data.
- Keep schema version or response type checks when backend contracts can evolve.
- Log enough context to debug the endpoint and response code without printing secrets.

## WebSocket Flow

Recommended flow:

1. Create socket in a subsystem or service object.
2. Bind connected, message, error, and closed delegates.
3. Send an auth or hello message after connection if required.
4. Parse incoming messages by type.
5. Dispatch typed events to listeners on the game thread.
6. Heartbeat with ping or app-level message if the protocol needs it.
7. Reconnect with bounded backoff when disconnection is recoverable.

Reconnect rules:

- Do not reconnect after intentional shutdown.
- Limit retry rate and expose state to UI.
- Clear timers and unbind delegates on shutdown.
- Make duplicate `Connect()` calls idempotent.

## TCP Socket Rules

- Define framing before parsing: fixed size, delimiter, length prefix, or protocol-specific packet header.
- Run blocking receive loops off the game thread.
- Marshal parsed messages back to the game thread.
- Stop and close sockets during owner teardown.
- Prefer WebSocket or HTTP when the service protocol allows it; raw TCP increases responsibility for framing, reconnect, and partial reads.

## UI And Gameplay Handoff

- Service result objects should be typed and small.
- UI should observe service state rather than own network requests.
- Gameplay state that matters in multiplayer should still be validated or owned by the authoritative server.
- For backend-driven gameplay data, define trust boundaries: cached display data, server-authoritative state, client prediction, or editor-only tooling.

## Verification

- Build the owning module after dependency changes.
- Add a fake endpoint, mocked local service, or controlled test server when possible.
- Test success, malformed JSON, timeout/failure, owner destruction before callback, reconnect, and intentional disconnect.
- Verify packaged build behavior when the service is runtime-facing.
