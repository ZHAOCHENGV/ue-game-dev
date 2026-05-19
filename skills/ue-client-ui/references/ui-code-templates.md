# Client UI Code Templates

## HUD Widget Management Pattern

```cpp
// MyHUDSubsystem.h — 使用 LocalPlayerSubsystem 管理 UI
UCLASS()
class MYGAME_API UMyHUDSubsystem : public ULocalPlayerSubsystem
{
    GENERATED_BODY()

public:
    virtual void Initialize(FSubsystemCollectionBase& Collection) override;
    virtual void Deinitialize() override;

    // 显示/隐藏指定 UI 层
    UFUNCTION(BlueprintCallable, Category = "UI")
    void ShowWidget(TSubclassOf<UUserWidget> WidgetClass);

    UFUNCTION(BlueprintCallable, Category = "UI")
    void HideWidget(TSubclassOf<UUserWidget> WidgetClass);

private:
    // 已创建的 Widget 缓存
    UPROPERTY()
    TMap<TSubclassOf<UUserWidget>, TObjectPtr<UUserWidget>> WidgetCache;
};
```

## View Model Pattern (MVVM-lite)

```cpp
// HealthViewModel.h
UCLASS(BlueprintType)
class MYGAME_API UHealthViewModel : public UObject
{
    GENERATED_BODY()

public:
    // UI 绑定属性
    UPROPERTY(BlueprintReadOnly, Category = "Health",
        meta = (DisplayName = "当前生命值"))
    float CurrentHealth = 100.0f;

    UPROPERTY(BlueprintReadOnly, Category = "Health",
        meta = (DisplayName = "最大生命值"))
    float MaxHealth = 100.0f;

    UPROPERTY(BlueprintReadOnly, Category = "Health",
        meta = (DisplayName = "生命值百分比"))
    float HealthPercent = 1.0f;

    // 数据变化通知（UI 绑定此委托刷新）
    UPROPERTY(BlueprintAssignable, Category = "Health")
    FOnHealthDataChanged OnDataChanged;

    // 从游戏状态更新 ViewModel
    void UpdateFromAttribute(float NewCurrent, float NewMax);
};

// HealthViewModel.cpp
void UHealthViewModel::UpdateFromAttribute(float NewCurrent, float NewMax)
{
    CurrentHealth = NewCurrent;
    MaxHealth = FMath::Max(NewMax, 1.0f);
    HealthPercent = CurrentHealth / MaxHealth;
    OnDataChanged.Broadcast();
}
```

## CommonUI Activatable Widget

```cpp
// MyMenuWidget.h
UCLASS()
class MYGAME_API UMyMenuWidget : public UCommonActivatableWidget
{
    GENERATED_BODY()

protected:
    virtual void NativeOnActivated() override;
    virtual void NativeOnDeactivated() override;
    virtual UWidget* NativeGetDesiredFocusTarget() const override;

    UPROPERTY(meta = (BindWidget))
    TObjectPtr<UCommonButtonBase> StartButton;

    UPROPERTY(meta = (BindWidget))
    TObjectPtr<UCommonButtonBase> SettingsButton;

    UPROPERTY(meta = (BindWidget))
    TObjectPtr<UCommonButtonBase> QuitButton;
};
```

## Input Mode Switching

```cpp
// 切换到纯 UI 模式（菜单）
void SetUIOnlyMode(APlayerController* PC, UWidget* FocusWidget)
{
    FInputModeUIOnly InputMode;
    InputMode.SetWidgetToFocus(FocusWidget->TakeWidget());
    InputMode.SetLockMouseToViewportBehavior(EMouseLockMode::DoNotLock);
    PC->SetInputMode(InputMode);
    PC->SetShowMouseCursor(true);
}

// 切换到游戏+UI 混合模式（HUD 交互）
void SetGameAndUIMode(APlayerController* PC)
{
    FInputModeGameAndUI InputMode;
    InputMode.SetLockMouseToViewportBehavior(EMouseLockMode::LockAlways);
    InputMode.SetHideCursorDuringCapture(false);
    PC->SetInputMode(InputMode);
}

// 切换回纯游戏模式
void SetGameOnlyMode(APlayerController* PC)
{
    FInputModeGameOnly InputMode;
    PC->SetInputMode(InputMode);
    PC->SetShowMouseCursor(false);
}
```
