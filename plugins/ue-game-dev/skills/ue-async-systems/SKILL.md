---
name: ue-async-systems
description: Unreal Engine asynchronous C++ workflow for AsyncTask, Async(), UE::Tasks, FRunnable, FQueuedThreadPool, ParallelFor, timers, latent or Blueprint async action nodes, game-thread handoff, cancellation, lifetime safety, and non-blocking gameplay/client operations. Use when requests involve background work, async Blueprint nodes, thread handoff, long-running CPU work, or avoiding game-thread stalls.
---

# UE Async Systems

Use this skill for Unreal Engine asynchronous work that must stay responsive, game-thread safe, and Blueprint-friendly when needed. Keep async code narrow: isolate the slow work, define the owner lifetime, then hand results back to the game thread before touching UObjects or gameplay state.

## First Pass

1. Identify the operation type: short game-thread deferral, CPU work, blocking IO, external service callback, tick/timer scheduling, latent action, or Blueprint async node.
2. Find the owner and lifetime: Actor, Component, Subsystem, UObject task object, module singleton, or external client.
3. Decide the callback surface: C++ delegate, multicast delegate, latent result, `UBlueprintAsyncActionBase`, promise/future, or subsystem event.
4. Mark what can run off-thread and what must return to the game thread. Treat UObject access, Blueprint delegates, actor spawning, world state, and UI updates as game-thread work.
5. Define cancellation and teardown before implementation: EndPlay, Deinitialize, module shutdown, HTTP/WebSocket disconnect, or async node activation cleanup.

## Implementation Rules

- Use timers or delegates for scheduled game-thread work; do not create threads for simple delays.
- Use `AsyncTask(ENamedThreads::GameThread, ...)` only to return to the game thread, not to hide slow work.
- Use `Async(EAsyncExecution::ThreadPool, ...)`, `UE::Tasks`, or a queued thread pool for bounded CPU/background work.
- Use `FRunnable` only for long-lived workers with clear startup, stop, and join semantics.
- Use `ParallelFor` only for independent, CPU-bound loops with no UObject mutation inside the parallel body.
- Use `TWeakObjectPtr` or a weak lambda capture when async callbacks may outlive the UObject owner.
- Broadcast Blueprint delegates on the game thread and only after validating the async action object and world context are still valid.
- Keep cancellation idempotent. A callback arriving after cancellation should become a no-op, not a crash.
- Avoid blocking waits on the game thread. Do not call `Wait()`, socket receive loops, or file/network blocking calls from gameplay/UI paths.

## Blueprint Async Nodes

- Use `UBlueprintAsyncActionBase` when designers need a node with exec pins and async completion/failure delegates.
- Store `WorldContextObject` or owner references safely, usually as weak references unless the async action intentionally owns a request object.
- Expose a static `BlueprintCallable` factory with `BlueprintInternalUseOnly="true"` when following common async node patterns.
- Perform validation in the factory or `Activate()`, then broadcast failure on the game thread for invalid input.
- Document exact Blueprint node search name, input pins, success/failure delegates, cancellation behavior, and PIE validation steps.

## References

- Read `references/async-patterns.md` for selection guidance across timers, `AsyncTask`, `Async`, `UE::Tasks`, `FRunnable`, `ParallelFor`, and Blueprint async nodes.
- Use `$ue-external-services` when async work is primarily HTTP, WebSocket, TCP, JSON, backend APIs, heartbeats, or reconnect logic.
- Use `$ue-cpp-gameplay` after async ownership is clear and the remaining work is normal gameplay C++.
- Use `$ue-debug-validation` when symptoms involve race conditions, callbacks after destruction, game-thread asserts, or intermittent crashes.
