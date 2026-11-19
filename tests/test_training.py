from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from training import CURRICULUM, check_files, pending_assessments, review_candidates, verification


class TrainingTests(unittest.TestCase):
    def test_missing_skill_and_duplicate_id_fail_check(self):
        with TemporaryDirectory() as temp:
            folder = Path(temp)
            mobs = folder / "Mobs"
            mobs.mkdir()
            mob = "Dummy:\n  Skills:\n    - skill{s=Missing} @trigger ~onDamaged\n"
            (mobs / "one.yml").write_text(mob, encoding="utf-8")
            (mobs / "two.yml").write_text(mob, encoding="utf-8")
            _, _, _, errors = check_files(folder)
            self.assertTrue(any("ID trùng: mob/Dummy" in error for error in errors))
            self.assertTrue(any("thiếu metaskill/Missing" in error for error in errors))

    def test_gameplay_status_requires_artifacts_and_current_yaml(self):
        with TemporaryDirectory() as temp:
            folder = Path(temp)
            mobs = folder / "Mobs"
            mobs.mkdir()
            yaml_file = mobs / "dummy.yml"
            yaml_file.write_text("Dummy:\n  Type: HUSK\n", encoding="utf-8")
            rows, ids, _, errors = check_files(folder)
            self.assertEqual(errors, [])
            runtime = {
                "yaml_sha256": {row["path"]: row["sha256"] for row in rows},
                "environment": {
                    "minecraft": "test", "server_build": "test",
                    "mythicmobs_build": "test", "edition": "test",
                },
                "load": {"result": "pass", "registered": ["mob/Dummy"], "artifact": "load.log"},
                "scenarios": {"spawn": {
                    "result": "pass", "observed": "fixture", "artifact": "observed.txt",
                }},
            }
            case = {"dependencies": [], "required_scenarios": ["spawn"], "runtime": runtime}
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "syntax-checked")
            (folder / "load.log").write_text("test fixture", encoding="utf-8")
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "server-loaded")
            (folder / "observed.txt").write_text("test fixture", encoding="utf-8")
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "verified-in-game")
            case["program"] = CURRICULUM
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "server-loaded")
            runtime["user_confirmation"] = {
                "date": "2026-11-15", "statement": "Test fixture", "artifact": "confirmation.md",
            }
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "server-loaded")
            (folder / "confirmation.md").write_text("test fixture", encoding="utf-8")
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "verified-in-game")
            yaml_file.write_text("Dummy:\n  Type: ZOMBIE\n", encoding="utf-8")
            rows, ids, _, errors = check_files(folder)
            self.assertEqual(verification(folder, case, rows, ids, errors)[0], "syntax-checked")

    def test_milestones_exclude_unverified_practice_and_assessments(self):
        practice = {"kind": "practice"}
        assessment = {"kind": "assessment", "after_completed": 5}
        verified = (practice, "verified-in-game")
        records = [verified] * 4 + [(practice, "server-loaded")]
        self.assertEqual(pending_assessments(records), (4, []))
        records.extend([verified, (assessment, "syntax-checked")])
        self.assertEqual(pending_assessments(records), (5, [5]))
        records.extend([verified] * 5 + [(assessment, "verified-in-game")])
        self.assertEqual(pending_assessments(records), (10, [10]))

    def test_review_lists_only_distinct_verified_practices_after_threshold(self):
        def record(number, kind="practice", status="verified-in-game"):
            return {"id": f"{number:03}", "kind": kind}, status

        records = [record(n) for n in range(10, 0, -1)]
        records += [record(1), record(11, "assessment"), record(12, status="server-loaded")]
        all_verified = [f"{n:03}" for n in range(1, 11)]
        self.assertEqual(review_candidates(records, 5), (10, all_verified))
        self.assertEqual(review_candidates(records, 10), (10, all_verified))
        self.assertEqual(review_candidates(records, 15), (10, []))
