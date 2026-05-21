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
                    PrivateDependencyModuleNames.AddRange(new string[] { "EnhancedInput", "GameplayAbilities", "UMG" });
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
        write(self.project / "Content" / "Input" / "IA_Jump.uasset", "binary placeholder")
        write(self.project / "Content" / "UI" / "WBP_Inventory.uasset", "binary placeholder")
        write(self.project / "Content" / "Maps" / "L_Test.umap", "binary placeholder")
        write(
            self.project / "Saved" / "Logs" / "SampleGame.log",
            """
            LogInit: Display: Running engine for game: SampleGame
            LogCook: Display: Cooking started
            UATHelper: Packaging (Windows): LogWindows: Error: appError called: Assertion failed: InventoryData != nullptr [File:D:/Sample/Source/SampleGame/InventoryComponent.cpp] [Line: 42]
            UATHelper: Packaging (Windows): ERROR: Cook failed.
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


if __name__ == "__main__":
    unittest.main()
