# BuildCookRun 命令模板

## Win64 Development

```powershell
& "C:\Program Files\Epic Games\UE_5.4\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
  -project="C:\Path\To\Project\MyGame.uproject" `
  -noP4 `
  -platform=Win64 `
  -clientconfig=Development `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="C:\Builds\MyGame-Win64-Development"
```

## Win64 Shipping

```powershell
& "C:\Program Files\Epic Games\UE_5.4\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
  -project="C:\Path\To\Project\MyGame.uproject" `
  -noP4 `
  -platform=Win64 `
  -clientconfig=Shipping `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="C:\Builds\MyGame-Win64-Shipping"
```

## Dedicated Server

```powershell
& "C:\Program Files\Epic Games\UE_5.4\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
  -project="C:\Path\To\Project\MyGame.uproject" `
  -noP4 `
  -server `
  -serverplatform=Win64 `
  -serverconfig=Development `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="C:\Builds\MyGame-Server"
```

## 填写前确认

- UE 安装路径。
- `.uproject` 绝对路径。
- 平台、配置、client/server target。
- 需要 Cook 的地图。
- Archive 输出目录。
- 是否允许本次会话运行打包命令。

## 失败后

- 保存 UAT log 和 Cook log。
- 找第一个 actionable error。
- 需要分诊时进入 `$ue-log-crash-triage`。
