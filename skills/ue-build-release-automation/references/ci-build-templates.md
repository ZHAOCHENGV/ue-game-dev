# CI Build Templates

## PowerShell Script Shape

Use parameterized scripts so local and CI builds share the same entry point:

```powershell
param(
  [Parameter(Mandatory=$true)][string]$EngineRoot,
  [Parameter(Mandatory=$true)][string]$ProjectPath,
  [string]$Platform = "Win64",
  [string]$Config = "Development",
  [Parameter(Mandatory=$true)][string]$ArchiveDir
)

$RunUAT = Join-Path $EngineRoot "Engine\Build\BatchFiles\RunUAT.bat"
if (-not (Test-Path $RunUAT)) { throw "RunUAT not found: $RunUAT" }
if (-not (Test-Path $ProjectPath)) { throw "Project not found: $ProjectPath" }

& $RunUAT BuildCookRun `
  -project="$ProjectPath" `
  -noP4 `
  -platform=$Platform `
  -clientconfig=$Config `
  -build `
  -cook `
  -stage `
  -pak `
  -archive `
  -archivedirectory="$ArchiveDir" `
  -utf8output

if ($LASTEXITCODE -ne 0) {
  throw "BuildCookRun failed with exit code $LASTEXITCODE"
}
```

## GitHub Actions Shape

Use only for self-hosted Windows runners that already have Unreal Engine and platform SDKs installed:

```yaml
name: Package Unreal

on:
  workflow_dispatch:
    inputs:
      config:
        type: choice
        options: [Development, Shipping]
        default: Development

jobs:
  package:
    runs-on: [self-hosted, Windows]
    steps:
      - uses: actions/checkout@v4
      - name: Package
        shell: powershell
        run: |
          .\Build\Package.ps1 `
            -EngineRoot "${{ vars.UE_ENGINE_ROOT }}" `
            -ProjectPath "${{ github.workspace }}\ProjectName.uproject" `
            -Platform "Win64" `
            -Config "${{ inputs.config }}" `
            -ArchiveDir "${{ github.workspace }}\Artifacts\Win64-${{ inputs.config }}"
      - uses: actions/upload-artifact@v4
        with:
          name: Win64-${{ inputs.config }}
          path: Artifacts/Win64-${{ inputs.config }}
```

## CI Rules

- Keep engine install, SDK setup, signing secrets, and artifact upload outside the skill unless the user asks for that provider.
- Use self-hosted runners for UE builds unless the user has a custom image.
- Store UAT logs as artifacts.
- Fail the job when `RunUAT` returns non-zero.
- Keep release publishing as a separate explicit stage after package validation.
