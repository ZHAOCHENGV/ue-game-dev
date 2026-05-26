# UE C++ 验证

## 构建

- 运行触及模块的目标构建，确认 UHT、编译和链接通过。
- 修改反射宏、头文件或 `.Build.cs` 后，特别关注 generated code 和 module dependency。
- Warning 不应无视；判断是否会影响 Blueprint、Cook 或 packaged build。

## Blueprint

- 如果新增或修改 Blueprint-facing API，编译相关 Blueprint。
- 验证节点搜索名、Category、Pin、默认值和事件是否符合预期。
- 检查子 Blueprint 是否覆盖了旧默认值或旧事件。

## PIE

- 用最小地图/场景触发目标行为。
- 覆盖成功路径、失败路径、重复调用、对象销毁和地图切换。
- 多人功能至少说明 server/client 场景。

## 日志

- 新增日志使用项目 log category。
- 错误日志包含对象名、状态、输入参数或资产路径。
- 记录首个失败症状，方便后续 `$ue-log-crash-triage`。
