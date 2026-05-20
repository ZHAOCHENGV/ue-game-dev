# UE Project Audit Checklist

Use this checklist when onboarding an existing UE project before secondary development.

## Project Identity

- `.uproject` path, project name, `EngineAssociation`
- Modules in `.uproject`
- Enabled plugins and any plugin marked beta/experimental
- Source control state, branch, and dirty files

## Code Layout

- `Source/<Project>/Public` and `Private`
- `<Module>.Build.cs` dependencies
- `.Target.cs` editor/game targets
- Project plugins under `Plugins/`
- Runtime modules vs Editor modules
- API macros and exported public headers

## Runtime Entry Points

- GameMode / GameState
- GameInstance / LocalPlayer / Subsystems
- PlayerController / PlayerState
- Character / Pawn / Components
- HUD / UI managers / CommonUI setup
- SaveGame classes and persistence managers
- AbilitySystemComponent, AttributeSets, GameplayAbilities
- AIController, Behavior Tree, Blackboard, EQS, StateTree

## Asset Discovery

Prefer filename discovery before reading binary asset contents.

- Maps: `*.umap`
- Blueprints: `BP_*.uasset`, `BPI_*`, `BPC_*`
- Widgets: `WBP_*`, `WB_*`
- Input: `IA_*`, `IMC_*`
- GAS: `GA_*`, `GE_*`, `GC_*`, Gameplay Tags config
- Animation: `ABP_*`, `AM_*`, `BS_*`, `CR_*`
- Data: `DA_*`, `DT_*`, `Curve*`
- Rendering/VFX: `M_*`, `MI_*`, `MF_*`, `NS_*`

## Config Review

- `Config/DefaultEngine.ini`
- `Config/DefaultGame.ini`
- `Config/DefaultInput.ini`
- `Config/DefaultEditor.ini`
- Collision channels, asset manager settings, gameplay tags, maps and modes, input settings

## Risk Signals

- Runtime module depending on editor-only modules
- Public headers exposing unnecessary dependencies
- Circular module dependencies
- Hard-coded asset paths without validation
- Missing `UPROPERTY` for UObject references that need GC tracking
- Replicated state without clear authority owner
- Blueprint APIs renamed without migration notes
- Plugin copied into UE project `Plugins/` when it is not a `.uplugin`
- Old engine version or migrated assets without redirector cleanup

## Suggested Validation

- Targeted editor build for touched modules
- Blueprint compile check for touched assets
- PIE smoke test for startup, possession, input, and UI
- Multiplayer PIE scenario for replicated state
- Asset validation or redirector cleanup before packaging
