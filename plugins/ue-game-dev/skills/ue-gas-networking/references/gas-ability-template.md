# GAS Ability Template

```cpp
UCLASS()
class SAMPLEGAME_API UGA_Fireball : public UGameplayAbility
{
    GENERATED_BODY()

public:
    UGA_Fireball();

    virtual void ActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo,
        const FGameplayEventData* TriggerEventData) override;
};
```

## Checklist

- Define activation policy, cost, cooldown, and authority expectations.
- Keep prediction keys valid for predicted client work.
- AttributeSet values replicate with clear `OnRep` handlers.
- GameplayCues handle presentation; authoritative state stays in abilities/effects.
- Test listen server and dedicated server behavior when prediction matters.
