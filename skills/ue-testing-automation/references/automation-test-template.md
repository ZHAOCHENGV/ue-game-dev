# Automation Test Template

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

## Functional Test Notes

- Use Automation Tests for deterministic C++ logic and validation helpers.
- Use Functional Tests for map, Actor, Blueprint, and PIE behavior.
- Name tests by feature and expected behavior.
- Include evidence path in completion handoff: command, map, net mode, and result.
