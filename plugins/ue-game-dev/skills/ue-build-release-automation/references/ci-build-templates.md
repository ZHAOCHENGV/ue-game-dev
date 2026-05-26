# CI 打包模板

## 通用步骤

```text
1. Checkout repository
2. Restore/cache DerivedDataCache if policy allows
3. Locate Unreal Engine installation
4. Generate project files if needed
5. Run BuildCookRun
6. Upload logs
7. Archive packaged artifacts
```

## GitHub Actions 片段

```yaml
name: UE Package

on:
  workflow_dispatch:

jobs:
  package:
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - name: Package Win64
        shell: powershell
        run: |
          & "C:\Program Files\Epic Games\UE_5.4\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
            -project="${{ github.workspace }}\MyGame.uproject" `
            -noP4 `
            -platform=Win64 `
            -clientconfig=Development `
            -build -cook -stage -pak -archive `
            -archivedirectory="${{ github.workspace }}\Artifacts\Win64"
      - uses: actions/upload-artifact@v4
        with:
          name: package-logs
          path: |
            Saved/Logs/**
            Engine/Programs/AutomationTool/Saved/Logs/**
```

## 注意事项

- UE 打包通常需要 self-hosted runner。
- 不要把证书、token、keystore、provisioning profile 写进仓库。
- DDC cache 要按项目、平台和引擎版本隔离。
- CI 产物目录要和源码、Intermediate、Saved 分离。
- 失败时上传完整日志，但报告中只总结首个可行动错误。
