# Debug Validation Templates

## Log Category Setup

```cpp
// MyGame.h
DECLARE_LOG_CATEGORY_EXTERN(LogMyGame, Log, All);

// MyGame.cpp
DEFINE_LOG_CATEGORY(LogMyGame);
```

## Network Debug Logging

```cpp
void DebugLogNetState(const AActor* Actor, const FString& Context)
{
#if !UE_BUILD_SHIPPING
    if (!IsValid(Actor)) return;
    const UWorld* World = Actor->GetWorld();
    UE_LOG(LogMyGame, Log,
        TEXT("[NET][%s] Actor=%s, NetMode=%s, Role=%s, RemoteRole=%s, Auth=%d"),
        *Context, *Actor->GetName(),
        World ? *UEnum::GetValueAsString(World->GetNetMode()) : TEXT("None"),
        *UEnum::GetValueAsString(Actor->GetLocalRole()),
        *UEnum::GetValueAsString(Actor->GetRemoteRole()),
        Actor->HasAuthority());
#endif
}
```

## Safe Pointer Validation

```cpp
// 使用 ensure 进行开发期校验
if (!ensure(IsValid(TargetActor)))
{
    UE_LOG(LogMyGame, Error, TEXT("%s: TargetActor invalid"), *FString(__FUNCTION__));
    return;
}
```

## Common Console Commands

```
stat fps / stat unit / stat game / stat net
showflag.navigation 1
ai.debug
log LogMyGame Verbose
obj list class=MyClass
```
