import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_tool(script: Path, *args: str) -> dict:
    completed = subprocess.run(
        [sys.executable, str(script), *args, "--format", "json"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return json.loads(completed.stdout)


def run_text_tool(script: Path, *args: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).strip() + "\n", encoding="utf-8")


class UEToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.project = Path(self.tmp.name) / "SampleGame"
        self.project.mkdir()
        write(
            self.project / "SampleGame.uproject",
            """
            {
              "FileVersion": 3,
              "EngineAssociation": "5.6",
              "Modules": [
                { "Name": "SampleGame", "Type": "Runtime" },
                { "Name": "SampleEditor", "Type": "Editor" }
              ],
              "Plugins": [
                { "Name": "EnhancedInput", "Enabled": true },
                { "Name": "GameplayAbilities", "Enabled": true }
              ]
            }
            """,
        )
        write(
            self.project / "Source" / "SampleGame" / "SampleGame.Build.cs",
            """
            using UnrealBuildTool;

            public class SampleGame : ModuleRules
            {
                public SampleGame(ReadOnlyTargetRules Target) : base(Target)
                {
                    PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine" });
                    PrivateDependencyModuleNames.AddRange(new string[] { "EnhancedInput", "GameplayAbilities", "UMG", "SampleEditor" });
                }
            }
            """,
        )
        write(
            self.project / "Source" / "SampleEditor" / "SampleEditor.Build.cs",
            """
            using UnrealBuildTool;

            public class SampleEditor : ModuleRules
            {
                public SampleEditor(ReadOnlyTargetRules Target) : base(Target)
                {
                    PublicDependencyModuleNames.AddRange(new string[] { "Core", "SampleGame" });
                    PrivateDependencyModuleNames.AddRange(new string[] { "UnrealEd", "Slate", "SlateCore" });
                }
            }
            """,
        )
        write(
            self.project / "Source" / "SampleGame" / "SampleGame.Target.cs",
            """
            using UnrealBuildTool;
            using System.Collections.Generic;

            public class SampleGameTarget : TargetRules
            {
                public SampleGameTarget(TargetInfo Target) : base(Target)
                {
                    Type = TargetType.Game;
                    ExtraModuleNames.Add("SampleGame");
                }
            }
            """,
        )
        write(
            self.project / "Source" / "SampleEditor.Target.cs",
            """
            using UnrealBuildTool;
            using System.Collections.Generic;

            public class SampleEditorTarget : TargetRules
            {
                public SampleEditorTarget(TargetInfo Target) : base(Target)
                {
                    Type = TargetType.Editor;
                    ExtraModuleNames.AddRange(new string[] { "SampleGame", "SampleEditor" });
                }
            }
            """,
        )
        write(
            self.project / "Source" / "SampleGame" / "InventoryComponent.h",
            """
            #pragma once

            #include "CoreMinimal.h"
            #include "Components/ActorComponent.h"
            #include "InventoryComponent.generated.h"

            DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnInventoryChanged, int32, NewCount);

            UCLASS(BlueprintType, Blueprintable)
            class SAMPLEGAME_API UInventoryComponent : public UActorComponent
            {
                GENERATED_BODY()

            public:
                UFUNCTION(BlueprintCallable, Category="Inventory")
                void AddItem(FName ItemId, int32 Count);

                UFUNCTION(BlueprintPure, Category="Inventory")
                int32 GetItemCount(FName ItemId) const;

                UFUNCTION(BlueprintImplementableEvent, Category="Inventory")
                void OnItemAdded(FName ItemId);

                UPROPERTY(BlueprintAssignable, Category="Inventory")
                FOnInventoryChanged OnInventoryChanged;
            };
            """,
        )
        write(
            self.project / "Source" / "SampleEditor" / "SampleEditorTool.h",
            """
            #pragma once

            #include "CoreMinimal.h"
            #include "UObject/Object.h"
            #include "SampleEditorTool.generated.h"

            UCLASS()
            class SAMPLEEDITOR_API USampleEditorTool : public UObject
            {
                GENERATED_BODY()

            public:
                UFUNCTION(BlueprintCallable, Category="Editor")
                void RefreshEditorPreview();
            };
            """,
        )
        write(
            self.project / "Source" / "SampleGame" / "Interactable.h",
            """
            #pragma once

            #include "CoreMinimal.h"
            #include "UObject/Interface.h"
            #include "Interactable.generated.h"

            UINTERFACE(BlueprintType)
            class SAMPLEGAME_API UInteractable : public UInterface
            {
                GENERATED_BODY()
            };

            class SAMPLEGAME_API IInteractable
            {
                GENERATED_BODY()

            public:
                UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category="Interaction")
                void Interact(AActor* InstigatorActor);
            };
            """,
        )
        write(self.project / "Content" / "Input" / "IA_Jump.uasset", "binary placeholder")
        write(self.project / "Content" / "UI" / "WBP_Inventory.uasset", "binary placeholder")
        write(self.project / "Content" / "Maps" / "L_Test.umap", "binary placeholder")
        write(
            self.project / "Config" / "DefaultEngine.ini",
            """
            [/Script/EngineSettings.GameMapsSettings]
            GameDefaultMap=/Game/Maps/L_Test

            [/Script/UnrealEd.ProjectPackagingSettings]
            +MapsToCook=(FilePath="/Game/Maps/L_Test")
            """,
        )
        write(
            self.project / "Config" / "DefaultGame.ini",
            """
            [/Script/Engine.AssetManagerSettings]
            +PrimaryAssetTypesToScan=(PrimaryAssetType="Item",AssetBaseClass="/Script/SampleGame.ItemDataAsset",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/Game/Data/Items")))
            """,
        )
        write(
            self.project / "Config" / "DefaultGameplayTags.ini",
            """
            [/Script/GameplayTags.GameplayTagsList]
            +GameplayTagList=(Tag="Ability.Fireball",DevComment="Fireball ability")
            +GameplayTagList=(Tag="UI.Inventory.Open",DevComment="Inventory UI")
            """,
        )
        write(
            self.project / "Saved" / "Logs" / "SampleGame.log",
            """
            LogInit: Display: Running engine for game: SampleGame
            LogCook: Display: Cooking started
            UATHelper: Packaging (Windows): LogWindows: Error: appError called: Assertion failed: InventoryData != nullptr [File:D:/Sample/Source/SampleGame/InventoryComponent.cpp] [Line: 42]
            UATHelper: Packaging (Windows): ERROR: Cook failed.
            LogBlueprint: Error: Blueprint Runtime Error: Accessed None trying to read property InventoryWidget
            AutomationTool exiting with ExitCode=25 (Error_UnknownCookFailure)
            """,
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_project_scan_summarizes_project_structure(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
            "--project",
            str(self.project),
        )

        self.assertEqual(result["project"]["name"], "SampleGame")
        self.assertEqual(result["project"]["engine_association"], "5.6")
        self.assertIn("SampleGame", result["modules"])
        self.assertIn("EnhancedInput", result["enabled_plugins"])
        self.assertIn("InventoryComponent.h", result["source_files"])
        self.assertIn("IA_Jump.uasset", result["assets"]["InputActions"])
        self.assertIn("WBP_Inventory.uasset", result["assets"]["WidgetBlueprints"])
        self.assertIn("ue-project-onboarding", result["recommended_next_skills"])

    def test_project_scan_reports_production_context(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
            "--project",
            str(self.project),
        )

        self.assertIn("Source/SampleGame/SampleGame.Target.cs", result["targets"])
        self.assertIn("Source/SampleEditor.Target.cs", result["targets"])
        self.assertIn("Ability.Fireball", result["gameplay_tags"])
        self.assertTrue(any(entry["type"] == "Item" for entry in result["asset_manager"]["primary_asset_types"]))
        self.assertIn("Runtime module SampleGame depends on editor-like module SampleEditor", result["risks"])

    def test_config_audit_reports_project_settings(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_config_audit.py",
            "--project",
            str(self.project),
        )

        self.assertEqual(result["project"], "SampleGame")
        self.assertEqual(result["checks"]["default_map"]["status"], "PASS")
        self.assertIn("DefaultMap configured", result["checks"]["default_map"]["message"])
        self.assertEqual(result["checks"]["enhanced_input"]["status"], "PASS")
        self.assertEqual(result["checks"]["maps_to_cook"]["status"], "PASS")

        missing = self.project / "Config" / "DefaultEngine.ini"
        missing.unlink()
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_config_audit.py",
            "--project",
            str(self.project),
        )
        self.assertEqual(result["checks"]["default_map"]["status"], "FAIL")
        self.assertEqual(result["checks"]["maps_to_cook"]["status"], "WARN")

    def test_project_scan_filters_module_and_renders_markdown(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
            "--project",
            str(self.project),
            "--filter",
            "SampleGame",
        )

        self.assertEqual(result["modules"], ["SampleGame"])
        self.assertIn("InventoryComponent.h", result["source_files"])
        self.assertIn("Interactable.h", result["source_files"])
        self.assertNotIn("SampleEditorTool.h", result["source_files"])

        markdown = run_text_tool(
            ROOT / "skills" / "ue-project-onboarding" / "scripts" / "ue_project_scan.py",
            "--project",
            str(self.project),
            "--filter",
            "SampleGame",
            "--format",
            "markdown",
        )
        self.assertIn("# UE Project Scan", markdown)
        self.assertIn("- Project: SampleGame", markdown)
        self.assertIn("InventoryComponent.h", markdown)

    def test_log_triage_extracts_first_actionable_failure(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
            "--log",
            str(self.project / "Saved" / "Logs" / "SampleGame.log"),
        )

        self.assertEqual(result["failure_phase"], "Cook")
        self.assertIn("Assertion failed", result["first_actionable_failure"])
        self.assertIn("InventoryComponent.cpp", result["evidence"][0])
        self.assertEqual(result["recommended_next_skill"], "ue-log-crash-triage")
        self.assertNotEqual(result["recommended_next_skill"], "ue-build-release-automation")

    def test_log_triage_extracts_top_n_actionable_failures(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
            "--log",
            str(self.project / "Saved" / "Logs" / "SampleGame.log"),
            "--top-n",
            "2",
        )

        self.assertEqual(len(result["actionable_failures"]), 2)
        self.assertIn("Assertion failed", result["actionable_failures"][0]["message"])
        self.assertIn("Blueprint Runtime Error", result["actionable_failures"][1]["message"])
        self.assertEqual(result["first_actionable_failure"], result["actionable_failures"][0]["message"])

    def test_log_triage_classifies_real_ue_phases(self) -> None:
        cases = [
            ("uht_reflection_error.log", "UHT", "reflection"),
            ("ubt_link_error.log", "Link", "linker"),
            ("cook_asset_error.log", "Cook", "missing asset"),
            ("crash_assert_callstack.log", "Crash", "assertion"),
        ]
        for filename, phase, root_cause_token in cases:
            with self.subTest(filename=filename):
                result = run_tool(
                    ROOT / "skills" / "ue-log-crash-triage" / "scripts" / "ue_log_triage.py",
                    "--log",
                    str(ROOT / "tests" / "fixtures" / "logs" / filename),
                )
                self.assertEqual(result["failure_phase"], phase)
                self.assertIn(root_cause_token, result["probable_root_cause"].lower())
                self.assertTrue(result["evidence"])

    def test_editor_command_report_generates_safe_commands(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-debug-validation" / "scripts" / "ue_editor_command_report.py",
            "--project",
            str(self.project / "SampleGame.uproject"),
            "--engine-cmd",
            "C:/UE/UE_5.6/Engine/Binaries/Win64/UnrealEditor-Cmd.exe",
        )

        self.assertTrue(result["read_only"])
        self.assertIn("-run=DataValidation", result["commands"]["data_validation"])
        self.assertIn("-run=CompileAllBlueprints", result["commands"]["blueprint_compile"])
        self.assertIn("-run=MapCheck", result["commands"]["map_check"])
        self.assertIn("Do not run without user approval", result["safety"])

    def test_blueprint_api_report_finds_reflected_cpp_api(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-cpp-gameplay" / "scripts" / "ue_blueprint_api_report.py",
            "--project",
            str(self.project),
        )

        names = {entry["name"] for entry in result["apis"]}
        self.assertIn("AddItem", names)
        self.assertIn("GetItemCount", names)
        self.assertIn("OnItemAdded", names)
        self.assertIn("OnInventoryChanged", names)
        add_item = next(entry for entry in result["apis"] if entry["name"] == "AddItem")
        self.assertEqual(add_item["kind"], "BlueprintCallable")
        self.assertIn("Search for Add Item", add_item["blueprint_steps"][0])

    def test_blueprint_api_report_filters_module_and_reports_interfaces(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-cpp-gameplay" / "scripts" / "ue_blueprint_api_report.py",
            "--project",
            str(self.project),
            "--module",
            "SampleGame",
            "--interface",
        )

        names = {entry["name"] for entry in result["apis"]}
        self.assertIn("Interact", names)
        self.assertNotIn("RefreshEditorPreview", names)
        interact = next(entry for entry in result["apis"] if entry["name"] == "Interact")
        self.assertEqual(interact["owner_kind"], "UInterface")
        self.assertEqual(interact["module"], "SampleGame")
        self.assertTrue(all(entry["file"].startswith("Source/SampleGame/") for entry in result["apis"]))

    def test_agent_plan_selects_lean_roles_and_boundaries(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-multi-agent-workflow" / "scripts" / "ue_agent_plan.py",
            "--request",
            "用多 Agent 熟悉这个旧 UE 项目，准备二开，并检查 C++ 和蓝图风险",
        )

        self.assertEqual(result["mode"], "lean")
        self.assertIn("Coordinator", result["roles"])
        self.assertIn("Project Explorer", result["roles"])
        self.assertIn("UE Architecture Reviewer", result["roles"])
        self.assertEqual(result["packaging_boundary"], "not relevant")
        self.assertTrue(any("Source/" in boundary for boundary in result["ownership_boundaries"]))
        self.assertIn("ue-project-onboarding", result["recommended_next_skills"])

    def test_dependency_graph_reports_dependencies_and_mermaid(self) -> None:
        result = run_tool(
            ROOT / "skills" / "ue-architecture" / "scripts" / "ue_dependency_graph.py",
            "--project",
            str(self.project),
        )

        modules = {entry["module"]: entry for entry in result["modules"]}
        self.assertIn("SampleGame", modules)
        self.assertIn("SampleEditor", modules)
        self.assertIn("Engine", modules["SampleGame"]["public_dependencies"])
        self.assertIn("UnrealEd", modules["SampleEditor"]["private_dependencies"])
        self.assertTrue(any(issue["type"] == "editor_dependency" for issue in result["issues"]))

        mermaid = run_text_tool(
            ROOT / "skills" / "ue-architecture" / "scripts" / "ue_dependency_graph.py",
            "--project",
            str(self.project),
            "--format",
            "mermaid",
        )
        self.assertIn("graph TD", mermaid)
        self.assertIn("SampleGame --> Engine", mermaid)


if __name__ == "__main__":
    unittest.main()
