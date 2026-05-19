# Packaging Troubleshooting Guide

## Common Cook/Package Failures

### Missing Asset Reference
- **症状**: `LogCook: Error: ... was not found`
- **原因**: 蓝图或 DataTable 引用了被删除/移动的资产
- **修复**: 使用 Reference Viewer 定位引用源，修复或添加 Redirector

### Editor-Only Reference in Runtime
- **症状**: `LogLinker: Warning: ... is editor-only but referenced by runtime`
- **原因**: Runtime 模块或蓝图引用了 Editor-only 类型
- **修复**: 移除引用或将被引用类型移到 Runtime 模块

### Missing Module Dependency
- **症状**: `Unresolved external symbol` 或 `cannot open input file`
- **原因**: `.Build.cs` 缺少必要的模块依赖
- **修复**: 添加到 `PublicDependencyModuleNames` 或 `PrivateDependencyModuleNames`

### Plugin Not Available in Package
- **症状**: 编辑器正常但打包后功能缺失
- **原因**: 插件未标记为 `Installed` 或类型为 Editor-only
- **修复**: 确认 `.uplugin` 模块类型为 Runtime 且插件已启用

## Pre-Package Checklist

```
[ ] DefaultEngine.ini: 目标平台渲染设置正确
[ ] DefaultGame.ini: MapsToCook 包含所有需要的关卡
[ ] Project Settings > Maps: Default Maps 设置正确
[ ] Project Settings > Packaging: 排除不需要的目录
[ ] 所有 Runtime 蓝图编译通过无警告
[ ] 没有硬编码的开发环境路径
[ ] 第三方插件支持目标平台
[ ] 所有资产引用使用软引用或 PrimaryAsset
```

## Build Configuration Quick Reference

| 配置 | 用途 | 性能 | 调试 |
|------|------|------|------|
| DebugGame | 开发调试 | 最低 | 完整 |
| Development | 日常开发 | 中等 | 有限 |
| Test | QA 测试 | 接近发布 | 最小 |
| Shipping | 正式发布 | 最高 | 无 |
