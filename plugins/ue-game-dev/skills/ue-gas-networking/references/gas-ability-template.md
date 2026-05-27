# GAS Ability 模板

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

## 检查清单

- 定义 activation policy、cost、cooldown 和 authority 预期。
- 预测型客户端逻辑保持 prediction key 有效。
- AttributeSet 值复制时提供清晰 `OnRep`。
- GameplayCue 处理表现；权威状态留在 Ability/Effect 中。
- 涉及 prediction 时测试 listen server 和 dedicated server 行为。
