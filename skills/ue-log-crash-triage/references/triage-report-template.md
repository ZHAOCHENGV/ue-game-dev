# 日志 / 崩溃分诊报告模板

```text
Failure stage:
First actionable error:
Evidence:
- Log file:
- Line:
- Message:
- Related file/asset/module:

Likely cause:
Why this is first:
Recommended next skill:
Immediate next action:
```

## 错误类型

- UBT：C++ 编译、include、module dependency、toolchain。
- UHT：反射宏、generated header、UCLASS/USTRUCT/UFUNCTION/UPROPERTY。
- Link：缺符号、API macro、模块依赖、第三方库。
- Blueprint compile：节点缺失、Pin 不兼容、父类/API 变化。
- Cook：资产缺失、Editor-only 依赖、平台不支持、redirector。
- Runtime crash：空指针、生命周期、线程、assert/ensure。

## 报告规则

- 报第一个可行动错误，不把最终 summary 当根因。
- 引用日志要短，保留文件、行号、模块和错误文本。
- 不确定时标注推断依据。
