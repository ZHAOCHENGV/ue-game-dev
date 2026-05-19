# BuildCookRun Command Reference

## Windows Local Package

Use this shape when the user asks for a local Windows package:

```powershell
& "D:\UE_5.6\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
  -project="F:\UEObject\ProjectName\ProjectName.uproject" `
  -noP4 `
  -platform=Win64 `
  -clientconfig=Development `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="F:\Builds\ProjectName\Win64-Development" `
  -utf8output
```

## Shipping Package

Use `Shipping` only when the user asks for release, QA, store submission, or a final distributable:

```powershell
& "<EngineRoot>\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun `
  -project="<Project.uproject>" `
  -noP4 `
  -platform=Win64 `
  -clientconfig=Shipping `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="<ArchiveDir>" `
  -utf8output
```

## Common Flags

| Flag | Use |
|------|-----|
| `-build` | Compile required targets before cooking. |
| `-cook` | Cook assets for the target platform. |
| `-stage` | Copy cooked content and binaries to staging. |
| `-pak` | Package cooked files into pak containers. |
| `-iostore` | Use IoStore containers when the project already uses them. |
| `-archive` | Copy staged build to a durable artifact directory. |
| `-archivedirectory=` | Final output directory for artifacts. |
| `-clientconfig=` | `Development`, `Test`, or `Shipping`. |
| `-serverconfig=` | Dedicated server configuration when packaging server targets. |
| `-map=` | Cook a specific map list when project settings are insufficient. |
| `-clean` | Remove previous intermediates; ask before using because it increases build time. |
| `-utf8output` | Keep Windows logs readable. |

## Platform Notes

- `Win64`: Use for Windows desktop client packages.
- `Android`: confirm SDK/NDK/JDK, signing, package name, texture format, and ABI before generating commands.
- `Linux`: confirm installed cross-compile toolchain on Windows hosts.
- Dedicated server: confirm a `Server.Target.cs` exists before using server flags.

## Output Summary Template

```text
Packaging command:
<exact command>

Inputs:
- Project: <path>
- Engine: <path>
- Platform/config: <platform>/<config>
- Archive: <path>

Result:
- Ran command: yes/no
- Exit code: <code>
- UAT log: <path>
- Artifact: <path>
- First blocker: <error or none>
```
