# Enhanced Input Checklist

## Asset Setup

```text
[ ] Input Actions use project naming, usually IA_<ActionName>.
[ ] Action value type matches usage: Digital, Axis1D, Axis2D, or Axis3D.
[ ] Triggers are intentional: Started, Triggered, Completed, Canceled, Ongoing.
[ ] Modifiers are documented: dead zone, negate, swizzle, scalar, smoothing.
[ ] Input Mapping Contexts use project naming, usually IMC_<ModeOrPawn>.
[ ] Mapping context priority is explicit when multiple contexts can be active.
[ ] Device-specific mappings are separated when keyboard/gamepad/touch differ.
```

## C++ Binding Pattern

```cpp
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"

void AMyCharacter::BeginPlay()
{
    Super::BeginPlay();

    if (const APlayerController* PC = Cast<APlayerController>(GetController()))
    {
        if (const ULocalPlayer* LocalPlayer = PC->GetLocalPlayer())
        {
            if (UEnhancedInputLocalPlayerSubsystem* Subsystem =
                LocalPlayer->GetSubsystem<UEnhancedInputLocalPlayerSubsystem>())
            {
                Subsystem->AddMappingContext(DefaultMappingContext, 0);
            }
        }
    }
}

void AMyCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    if (UEnhancedInputComponent* EnhancedInput = Cast<UEnhancedInputComponent>(PlayerInputComponent))
    {
        EnhancedInput->BindAction(MoveAction, ETriggerEvent::Triggered, this, &AMyCharacter::HandleMove);
    }
}
```

## Build.cs

Add the module where the C++ code references Enhanced Input types:

```csharp
PrivateDependencyModuleNames.AddRange(new string[]
{
    "EnhancedInput"
});
```

Use `PublicDependencyModuleNames` only if public headers expose Enhanced Input types.

## Validation

```text
[ ] The pawn/controller is possessed by the expected local player.
[ ] Mapping context is added once and not repeatedly every tick.
[ ] Input action event fires in PIE.
[ ] Correct trigger pin is used for the intended behavior.
[ ] Axis values are normalized or clamped where gameplay expects it.
[ ] Multiplayer commands do not mutate authoritative state only on the client.
[ ] Blueprint graphs compile with no duplicate input event conflicts.
```

## Common Failure Sources

| Symptom | First Check |
|---------|-------------|
| Event never fires | Mapping context was not added to `UEnhancedInputLocalPlayerSubsystem`. |
| Works before respawn only | Mapping context or bindings are not restored after possession changes. |
| Wrong axis direction | Modifier order, negate, or swizzle is wrong. |
| Gamepad ignored | Mapping missing, device assigned to another local player, or action type mismatch. |
| UI blocks action | Focus/input mode/CommonUI consumed the action. |
