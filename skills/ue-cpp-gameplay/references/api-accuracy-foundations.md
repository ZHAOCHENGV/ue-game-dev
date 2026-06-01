# UE C++ API Accuracy Foundations

This reference distills API-accuracy checks inspired by the public MIT-licensed `quodsoler/unreal-engine-skills` project. Use it to reduce hallucinated UE C++ APIs before presenting code.

## Reflection Sanity

- Every reflected class, struct, and enum needs the matching generated include and `GENERATED_BODY()`.
- Use `UCLASS`, `USTRUCT`, `UENUM`, `UFUNCTION`, and `UPROPERTY` only where reflection, Blueprint access, config, serialization, replication, or editor exposure is actually needed.
- In UE5, prefer `GENERATED_BODY()` for structs; do not introduce legacy generated-body macros.
- Dynamic multicast delegate bindings with `AddDynamic` require the target function to be a `UFUNCTION`.
- RPC declarations need their generated `_Implementation` body. Do not invent validation signatures unless the target engine/project style already uses them.

## UObject Lifetime

- Reflected UObject members should be `UPROPERTY()` and usually `TObjectPtr<T>` in UE5 codebases.
- Use `TWeakObjectPtr<T>` for non-owning cached UObject references that may be destroyed.
- Use `TSoftObjectPtr<T>`, `TSoftClassPtr<T>`, or Primary Asset IDs for optional assets that should not force-load.
- Do not use `TSharedPtr` or `TUniquePtr` for UObject-derived types.
- For non-UObject owners that must hold UObject references, use an explicit GC reference strategy such as `FGCObject` or a UObject owner.

## Containers And Strings

- Use UE containers (`TArray`, `TMap`, `TSet`) for reflected/gameplay-facing data unless the boundary specifically requires STL.
- Avoid mutating `TArray` during ranged-for iteration; iterate by index when removing.
- Use `FName` for stable identifiers, `FString` for mutable strings/paths, and `FText` for player-visible localized text.
- Prefer Gameplay Tags over stringly typed gameplay categories when the project already uses tags.

## Subsystem Access

- `UGameInstanceSubsystem`: access through `GetGameInstance()->GetSubsystem<T>()`; persists across map loads.
- `UWorldSubsystem`: access through `GetWorld()->GetSubsystem<T>()`; scoped to a world/PIE instance.
- `ULocalPlayerSubsystem`: access through the local player; per local user.
- `UEngineSubsystem`: access through `GEngine->GetEngineSubsystem<T>()`; global engine lifetime.

## Replication Checks

- A replicated property needs both the reflected specifier and `GetLifetimeReplicatedProps`.
- `ReplicatedUsing` needs a matching `UFUNCTION` OnRep handler.
- Define owner, authority, prediction, save/load, and UI notification boundaries before exposing mutable replicated state to Blueprint.

## Before Sending Code

- Verify class/function names against nearby project code or UE headers when possible.
- Name the owning module for every include/API that may require `.Build.cs` changes.
- Mention engine-version assumptions when using newer APIs such as `TObjectPtr`, Enhanced Input, StateTree, Mass, or PCG.
