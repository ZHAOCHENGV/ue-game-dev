# UE Async Pattern Guide

## Pattern Selection

| Need | Prefer | Avoid |
|------|--------|-------|
| Delay or periodic game-thread work | `FTimerManager`, delegates, tick only when necessary | Worker thread for simple timing |
| Return from a worker callback to gameplay/UI | `AsyncTask(ENamedThreads::GameThread, ...)` | Touching UObjects off-thread |
| Short CPU/background job | `Async(EAsyncExecution::ThreadPool, ...)` or `UE::Tasks` | Custom `FRunnable` |
| Many independent CPU items | `ParallelFor` | Shared mutable UObject state inside loop |
| Long-lived blocking worker | `FRunnable` plus explicit stop/join | Detached threads with no owner |
| Blueprint-facing async operation | `UBlueprintAsyncActionBase` | Latent hidden state without cleanup |
| External HTTP/WebSocket/TCP | `$ue-external-services` patterns | Mixing backend client state into gameplay actors |

## Game-Thread Handoff

- Gather raw values off-thread; apply them to UObjects on the game thread.
- Capture weak owners:

```cpp
TWeakObjectPtr<UMySubsystem> WeakOwner = this;
Async(EAsyncExecution::ThreadPool, [WeakOwner]()
{
    FMyResult Result = DoSlowWorkWithoutUObjects();
    AsyncTask(ENamedThreads::GameThread, [WeakOwner, Result = MoveTemp(Result)]()
    {
        if (!WeakOwner.IsValid())
        {
            return;
        }
        WeakOwner->HandleResult(Result);
    });
});
```

- Do not capture raw `this` when a callback can outlive the owner.
- Keep results copyable or movable without referencing thread-unsafe engine objects.

## Cancellation And Teardown

- Define the owner that cancels work: Actor `EndPlay`, Component `EndPlay`, Subsystem `Deinitialize`, async action `SetReadyToDestroy`, or module `ShutdownModule`.
- Store request handles, future handles, thread objects, or cancellation tokens where the owner can reach them.
- Treat cancellation as a state transition. Late callbacks should check the state and return.
- Stop long-lived `FRunnable` workers before module unload or owner destruction.

## Blueprint Async Action Shape

Use a small UObject task object when Blueprint needs explicit completion pins:

```cpp
UCLASS()
class UMyAsyncAction : public UBlueprintAsyncActionBase
{
    GENERATED_BODY()

public:
    UPROPERTY(BlueprintAssignable)
    FMyAsyncResultDelegate OnSuccess;

    UPROPERTY(BlueprintAssignable)
    FMyAsyncResultDelegate OnFailure;

    UFUNCTION(BlueprintCallable, meta=(BlueprintInternalUseOnly="true", WorldContext="WorldContextObject"))
    static UMyAsyncAction* RunMyAsyncTask(UObject* WorldContextObject, FName RequestId);

    virtual void Activate() override;

private:
    TWeakObjectPtr<UObject> WeakWorldContext;
    FName RequestId;
    bool bCancelled = false;
};
```

Implementation rules:

- Validate inputs before starting work.
- Broadcast failure for invalid input instead of silently doing nothing.
- Broadcast delegates on the game thread.
- Call `SetReadyToDestroy()` after terminal success/failure when no longer needed.
- If cancellation is supported, expose it intentionally and make repeated cancellation safe.

## Parallel Work Rules

- Use `ParallelFor` only when each item is independent.
- Use thread-safe containers or pre-sized result arrays with one writer per index.
- Do not spawn actors, update components, broadcast Blueprint events, or mutate UObjects inside the parallel body.
- Merge and apply results on the game thread after the loop.

## Verification

- Run a targeted build for the owning module.
- Add a PIE smoke check that starts the async operation, destroys or unloads the owner early, and confirms late callbacks do not crash.
- For Blueprint async nodes, compile the target Blueprint and validate success and failure pins.
- For long workers, test shutdown while work is active.
