# World Interaction Code Templates

## Interactable Interface

```cpp
// IInteractable.h
UINTERFACE(MinimalAPI, BlueprintType)
class UInteractable : public UInterface
{
    GENERATED_BODY()
};

class IInteractable
{
    GENERATED_BODY()

public:
    // 是否可以交互（距离、状态、权限检查）
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Interaction")
    bool CanInteract(AActor* Interactor) const;

    // 执行交互
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Interaction")
    void OnInteract(AActor* Interactor);

    // 获取交互提示文本
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Interaction")
    FText GetInteractionPrompt() const;
};
```

## Trace-Based Interaction Component

```cpp
// InteractionComponent.h
UCLASS(ClassGroup=(Interaction), meta=(BlueprintSpawnableComponent))
class MYGAME_API UInteractionComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UInteractionComponent();

    // 执行交互检测（由 PlayerController 或 Pawn 调用）
    UFUNCTION(BlueprintCallable, Category = "Interaction")
    void PerformInteractionTrace();

    // 尝试与当前目标交互
    UFUNCTION(BlueprintCallable, Category = "Interaction")
    void TryInteract();

    // 当前交互目标变化时通知 UI
    UPROPERTY(BlueprintAssignable, Category = "Interaction")
    FOnInteractionTargetChanged OnTargetChanged;

protected:
    // 交互检测距离
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Interaction",
        meta = (DisplayName = "交互距离"))
    float InteractionDistance = 300.0f;

    // 交互检测通道
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Interaction",
        meta = (DisplayName = "检测通道"))
    TEnumAsByte<ECollisionChannel> TraceChannel = ECC_Visibility;

private:
    // 弱引用当前目标，防止悬挂指针
    TWeakObjectPtr<AActor> CurrentTarget;
};
```

## Pickup Actor Pattern

```cpp
// PickupActor.h
UCLASS()
class MYGAME_API APickupActor : public AActor, public IInteractable
{
    GENERATED_BODY()

public:
    APickupActor();

    // IInteractable
    virtual bool CanInteract_Implementation(AActor* Interactor) const override;
    virtual void OnInteract_Implementation(AActor* Interactor) override;
    virtual FText GetInteractionPrompt_Implementation() const override;

protected:
    // 拾取物数据（数据驱动）
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Pickup",
        meta = (DisplayName = "拾取物数据"))
    TObjectPtr<UPickupDataAsset> PickupData;

    // 拾取后的处理：销毁、隐藏、禁用碰撞、进入对象池
    UPROPERTY(EditAnywhere, Category = "Pickup",
        meta = (DisplayName = "拾取后行为"))
    EPickupPostAction PostPickupAction = EPickupPostAction::Destroy;

    // 冷却时间（用于可重复拾取的物品）
    UPROPERTY(EditAnywhere, Category = "Pickup",
        meta = (DisplayName = "冷却时间", EditCondition = "PostPickupAction == EPickupPostAction::Cooldown"))
    float CooldownDuration = 5.0f;

private:
    // 防止重复拾取
    bool bIsConsumed = false;
};
```

## Overlap-Based Trigger Zone

```cpp
// Setup in constructor
TriggerVolume = CreateDefaultSubobject<USphereComponent>(TEXT("TriggerVolume"));
TriggerVolume->SetSphereRadius(200.0f);
TriggerVolume->SetCollisionProfileName(TEXT("Trigger"));
TriggerVolume->SetGenerateOverlapEvents(true);

// Bind overlap events
TriggerVolume->OnComponentBeginOverlap.AddDynamic(
    this, &AMyActor::OnTriggerBeginOverlap);
TriggerVolume->OnComponentEndOverlap.AddDynamic(
    this, &AMyActor::OnTriggerEndOverlap);

// Handler with validation
void AMyActor::OnTriggerBeginOverlap(
    UPrimitiveComponent* OverlappedComponent,
    AActor* OtherActor,
    UPrimitiveComponent* OtherComp,
    int32 OtherBodyIndex,
    bool bFromSweep,
    const FHitResult& SweepResult)
{
    if (!IsValid(OtherActor)) return;
    if (!OtherActor->Implements<UInteractable>()) return;
    if (bIsConsumed) return;  // 防止重复触发

    // 执行交互逻辑...
}
```
