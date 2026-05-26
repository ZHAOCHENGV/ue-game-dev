# UE Gate Check 模板

```text
Verdict: PASS | CONCERNS | FAIL
Target phase:
Evidence:
- Requirements:
- Build:
- Blueprint:
- PIE:
- Tests:
- Logs:
- Performance/Packaging:

Blockers:
-

Risks:
-

Next action:
Recommended skill:
```

## 判定说明

- `PASS`：证据足够进入下一阶段。
- `CONCERNS`：可进入，但风险需要带着走。
- `FAIL`：存在阻塞，下一阶段会无效或高风险。

## 注意

- 没跑过的验证写“未验证”，不要写通过。
- 打包准备检查不等于允许自动打包。
