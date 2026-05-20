# Save Load Code Templates

## SaveGame Class Template

```cpp
// MySaveGame.h
UCLASS()
class MYGAME_API UMySaveGame : public USaveGame
{
    GENERATED_BODY()

public:
    // 存档版本号，用于数据迁移
    UPROPERTY(VisibleAnywhere, Category = "SaveGame")
    int32 SaveVersion = 1;

    // 存档时间戳
    UPROPERTY(VisibleAnywhere, Category = "SaveGame")
    FDateTime SaveTimestamp;

    // 玩家数据
    UPROPERTY(VisibleAnywhere, Category = "SaveGame")
    FPlayerSaveData PlayerData;

    // 世界状态
    UPROPERTY(VisibleAnywhere, Category = "SaveGame")
    TArray<FActorSaveData> WorldActors;

    // 任务进度
    UPROPERTY(VisibleAnywhere, Category = "SaveGame")
    TMap<FName, FQuestSaveData> QuestProgress;
};
```

## Stable Identifier Pattern

```cpp
// 使用稳定标识符而非 UObject 指针
USTRUCT(BlueprintType)
struct FActorSaveData
{
    GENERATED_BODY()

    // 稳定唯一标识符（不随关卡重加载改变）
    UPROPERTY()
    FGuid PersistentId;

    // Actor 类路径（使用软引用）
    UPROPERTY()
    FSoftClassPath ActorClass;

    // 位置和旋转
    UPROPERTY()
    FTransform ActorTransform;

    // 序列化的自定义状态数据
    UPROPERTY()
    TArray<uint8> CustomStateData;
};
```

## Save/Load Flow

```cpp
// 保存
void UMySaveSubsystem::SaveGame(const FString& SlotName)
{
    UMySaveGame* SaveObject = NewObject<UMySaveGame>();
    SaveObject->SaveVersion = CurrentSaveVersion;
    SaveObject->SaveTimestamp = FDateTime::Now();

    // 收集需要保存的状态
    CollectPlayerState(SaveObject->PlayerData);
    CollectWorldActors(SaveObject->WorldActors);
    CollectQuestProgress(SaveObject->QuestProgress);

    // 异步保存
    UGameplayStatics::AsyncSaveGameToSlot(
        SaveObject, SlotName, 0,
        FAsyncSaveGameToSlotDelegate::CreateUObject(
            this, &UMySaveSubsystem::OnSaveCompleted));
}

// 加载
void UMySaveSubsystem::LoadGame(const FString& SlotName)
{
    if (!UGameplayStatics::DoesSaveGameExist(SlotName, 0))
    {
        UE_LOG(LogSave, Warning, TEXT("存档槽位 %s 不存在"), *SlotName);
        return;
    }

    UGameplayStatics::AsyncLoadGameFromSlot(
        SlotName, 0,
        FAsyncLoadGameFromSlotDelegate::CreateUObject(
            this, &UMySaveSubsystem::OnLoadCompleted));
}
```

## Version Migration Pattern

```cpp
void UMySaveSubsystem::MigrateSaveData(UMySaveGame* SaveObject)
{
    // 按版本逐步迁移
    if (SaveObject->SaveVersion < 2)
    {
        // v1 -> v2: 添加任务系统字段
        // 旧存档没有任务数据，初始化为空
        SaveObject->QuestProgress.Reset();
        SaveObject->SaveVersion = 2;
    }

    if (SaveObject->SaveVersion < 3)
    {
        // v2 -> v3: 重构玩家数据结构
        MigratePlayerDataV2ToV3(SaveObject->PlayerData);
        SaveObject->SaveVersion = 3;
    }
}
```
