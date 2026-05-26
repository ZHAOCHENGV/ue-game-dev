# UE UI 代码模板

## Widget 创建

```cpp
UUserWidget* Widget = CreateWidget<UUserWidget>(OwningPlayer, WidgetClass);
if (Widget)
{
    Widget->AddToViewport();
}
```

## 输入模式

```cpp
FInputModeUIOnly InputMode;
InputMode.SetWidgetToFocus(Widget->TakeWidget());
InputMode.SetLockMouseToViewportBehavior(EMouseLockMode::DoNotLock);
PlayerController->SetInputMode(InputMode);
PlayerController->SetShowMouseCursor(true);
```

关闭时要恢复：

```cpp
FInputModeGameOnly InputMode;
PlayerController->SetInputMode(InputMode);
PlayerController->SetShowMouseCursor(false);
```

## ViewModel / 事件刷新

```text
Gameplay state changes
  -> Component/Subsystem broadcasts event
  -> UI controller/ViewModel stores display state
  -> Widget refreshes specific fields
```

## Blueprint 接法

```text
1. 创建 WBP_XXX。
2. 设置 owning player。
3. Add to Viewport 或加入 CommonUI stack。
4. 设置输入模式和焦点。
5. 绑定 ViewModel/delegate。
6. 关闭时解绑并恢复输入。
```

## 注意

- 不要在 Tick 中轮询 Gameplay 状态。
- Widget 持有 Actor 引用时使用有效性检查。
- 本地多人按 LocalPlayer 分离 UI 和输入。
