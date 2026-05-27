# Automation Test 模板

```cpp
IMPLEMENT_SIMPLE_AUTOMATION_TEST(FInventoryRulesTest,
    "SampleGame.Inventory.Rules",
    EAutomationTestFlags::EditorContext | EAutomationTestFlags::EngineFilter)

bool FInventoryRulesTest::RunTest(const FString& Parameters)
{
    TestEqual(TEXT("Empty inventory starts at zero"), GetInitialItemCount(), 0);
    return true;
}
```

## Functional Test 说明

- 确定性 C++ 逻辑和验证 helper 使用 Automation Test。
- 地图、Actor、Blueprint 和 PIE 行为使用 Functional Test。
- 测试名称写清 feature 和预期行为。
- 完成交接中记录证据路径：命令、地图、net mode 和结果。
