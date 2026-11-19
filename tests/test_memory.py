"""Regression scenarios for contextual memory retrieval."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import memory


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / "source.md").write_text("Synthetic user confirmation for the test.\n", encoding="utf-8")
        self.decision = {
            "id": "lock-before-impact", "category": "decisions", "topic": "cleave-direction",
            "title": "Khóa hướng đòn quét", "summary": "Chừa khoảng né cho người chơi.",
            "context": "Boss hợp tác với vùng cảnh báo.", "exceptions": "Đòn bám mục tiêu là case khác.",
            "scope": "project:tutien", "claim": "PREFERENCE", "confidence": "CONFIRMED",
            "recorded": "2026-11-13", "answer": "lock-at-start",
            "requires": ["multiplayer", "dodge-window"], "excludes": ["tracking-required"],
            "sources": [{"type": "user", "ref": "source.md", "note": "Synthetic test answer."}],
        }
        self.context = {"multiplayer", "dodge-window"}

    def append(self, **overrides):
        record = {**self.decision, **overrides}
        memory.add(self.root, memory.load(self.root), record)
        return record

    def resolved(self, project="tutien", context=None, impact="material"):
        return memory.resolve(memory.load(self.root), "cleave-direction", project,
                              self.context if context is None else context, impact)

    def test_answered_question_and_real_reuse_have_separate_counts(self):
        self.append()
        self.append(id="previous-question", category="questions", claim="FACT", decision="lock-before-impact")
        records = memory.load(self.root)
        for query in ("khóa hướng", "khoa huong"):
            hits = memory.search(records, query, "tutien", ("questions",))
            self.assertEqual([hit["id"] for hit in hits], ["previous-question"])
        result = self.resolved()
        self.assertEqual((result["action"], result["answer"]), ("apply", "lock-at-start"))
        self.assertEqual(result["answered_questions"][0]["id"], "previous-question")
        self.assertEqual(memory.report(records)["questions_reused"], 0)
        for event in ("reuse-one", "reuse-two"):
            self.append(id=event, category="conversations", claim="FACT",
                        result="reused-answer", question="previous-question")
        report = memory.report(memory.load(self.root))
        self.assertEqual((report["questions_reused"], report["answer_reuse_events"]), (1, 2))

    def test_project_preference_does_not_leak(self):
        self.append()
        self.append(id="global-dodge-rule", scope="global", category="preferences", answer="lock-late")
        self.assertEqual(self.resolved(project="survival")["answer"], "lock-late")
        self.assertEqual(self.resolved(project=None)["answer"], "lock-late")
        hits = memory.search(memory.load(self.root), "khóa hướng", "survival")
        self.assertEqual([hit["id"] for hit in hits], ["global-dodge-rule"])

    def test_cli_round_trip_in_separate_processes_and_cleanup(self):
        with TemporaryDirectory() as directory:
            workspace = Path(directory)
            (workspace / "memory").mkdir()
            (workspace / "source.md").write_text("Synthetic evidence only.\n", encoding="utf-8")
            base = [sys.executable, "-B", "-X", "utf8", memory.__file__, "--root", directory]

            def cli(*args, payload=None):
                result = subprocess.run([*base, *args], input=payload, capture_output=True,
                                        encoding="utf-8", check=True)
                return json.loads(result.stdout)

            cli("add", "-", payload=json.dumps(self.decision))
            question = {**self.decision, "id": "answered-cleave", "category": "questions",
                        "claim": "FACT", "decision": self.decision["id"]}
            cli("add", "-", payload=json.dumps(question))
            hits = cli("search", "khoa huong", "--project", "tutien", "--category", "decisions")
            self.assertEqual([hit["id"] for hit in hits], [self.decision["id"]])
            context = ["--context", "multiplayer", "--context", "dodge-window", "--impact", "material"]
            result = cli("resolve", "cleave-direction", "--project", "tutien", *context)
            self.assertEqual((result["action"], result["answer"]), ("apply", "lock-at-start"))
            self.assertEqual(result["answered_questions"][0]["id"], question["id"])
            self.assertEqual(cli("resolve", "cleave-direction", "--project", "survival", *context)["matches"], [])
            self.assertEqual(cli("report")["questions_reused"], 0)
        self.assertFalse(workspace.exists())

    def test_resolved_uncertainty_stays_in_history_but_leaves_review(self):
        self.append(id="open-question", category="uncertainties", claim="FACT", confidence="UNKNOWN")
        self.assertEqual(self.resolved()["review"][0]["id"], "open-question")
        self.append(resolves=["open-question"])
        self.assertEqual(self.resolved()["review"], [])
        self.assertEqual(self.resolved(context={"multiplayer"})["review"][-1]["id"], "open-question")
        self.assertIn("open-question", memory.load(self.root))

    def test_missing_or_excluded_context_does_not_apply_old_decision(self):
        self.append()
        self.assertEqual(self.resolved(context={"multiplayer"})["action"], "review-then-ask-if-needed")
        self.assertEqual(self.resolved(context=self.context | {"tracking-required"}, impact="minor")["action"],
                         "use-reversible-default")

    def test_conflict_requires_review_until_explicit_contextual_replacement(self):
        self.append()
        self.append(id="lock-late", scope="global", category="preferences", answer="lock-late")
        result = self.resolved()
        self.assertEqual(result["action"], "review-conflict")
        self.assertTrue(result["ask_if_unresolved"])
        self.assertFalse(self.resolved(impact="minor")["ask_if_unresolved"])
        self.append(id="lock-start-again", requires=[*self.decision["requires"], "short-windup"],
                    supersedes=["lock-before-impact", "lock-late"])
        self.assertEqual(self.resolved(context=self.context | {"short-windup"})["answer"], "lock-at-start")
        self.assertEqual(self.resolved()["action"], "review-conflict")
        self.assertEqual(self.resolved(project="survival")["answer"], "lock-late")

    def test_replacement_does_not_chain_through_an_out_of_context_answer(self):
        self.append()
        self.append(id="short-windup", requires=[*self.decision["requires"], "short-windup"],
                    answer="lock-late", supersedes=["lock-before-impact"])
        self.append(id="moving-platform", requires=[*self.decision["requires"], "moving-platform"],
                    answer="track-until-hit", supersedes=["short-windup"])
        result = self.resolved(context=self.context | {"moving-platform"})
        self.assertEqual(result["action"], "review-conflict")
        self.assertEqual(self.resolved(context=self.context | {"short-windup", "moving-platform"})["answer"],
                         "track-until-hit")

    def test_inferred_pattern_cannot_answer_or_be_promoted_without_evidence(self):
        self.append(id="pattern", category="patterns", claim="INFERENCE", confidence="INFERRED")
        self.assertEqual(self.resolved()["action"], "review-then-ask-if-needed")
        self.assertEqual(memory.report(memory.load(self.root))["inferred_rules"], 1)
        with self.assertRaisesRegex(ValueError, "inference cannot be observed or confirmed"):
            self.append(id="fake-confirmed", claim="INFERENCE")
        with self.assertRaisesRegex(ValueError, "direct user evidence"):
            self.append(id="unsupported-preference", sources=[{
                "type": "yaml", "ref": "source.md", "note": "YAML does not establish user intent."}])

    def test_correction_retrieval_and_pending_resolution(self):
        self.append(id="open-correction", category="corrections", claim="FACT", status="checking",
                    tags=["unicodeencodeerror", "windows", "yaml"])
        report = memory.report(memory.load(self.root))
        self.assertEqual(report["needs_verification"][0]["id"], "open-correction")
        with self.assertRaisesRegex(ValueError, "needs a regression case"):
            self.append(id="correction-without-test", category="corrections", status="confirmed")
        (self.root / "regression.md").write_text("Synthetic regression scenario.", encoding="utf-8")
        self.append(id="confirmed-correction", category="corrections", claim="FACT", status="confirmed",
                    resolves=["open-correction"], regression="regression.md",
                    tags=["unicodeencodeerror", "windows", "yaml"])
        records = memory.load(self.root)
        self.assertEqual(memory.report(records)["needs_verification"], [])
        hits = memory.search(records, "UnicodeEncodeError", "tutien", ("corrections",))
        self.assertEqual({hit["id"] for hit in hits}, {"open-correction", "confirmed-correction"})

    def test_add_keeps_original_and_rejects_missing_evidence(self):
        first = self.append()
        path = self.root / memory.record_path(first)
        original = path.read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.append(answer="different")
        self.assertEqual(path.read_bytes(), original)
        with self.assertRaises(FileExistsError):
            memory.write_json(path, {"different": True}, replace=False)
        self.assertEqual(path.read_bytes(), original)
        bad = deepcopy(first)
        bad["id"] = "broken-link"
        bad["sources"][0]["ref"] = "missing.md"
        with self.assertRaisesRegex(ValueError, "missing local evidence"):
            memory.add(self.root, memory.load(self.root), bad)
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), first)

    def test_runtime_verification_requires_build_and_result(self):
        source = {"type": "test", "ref": "source.md", "note": "Synthetic game evidence."}
        record = dict(id="gameplay-proof", category="patterns", claim="FACT", verification="verified-in-game")
        with self.assertRaisesRegex(ValueError, "requires test evidence with build and result"):
            self.append(**record, sources=[source])
        self.append(**record, sources=[{**source, "build": "Synthetic server build", "result": "Expected hit observed"}])


if __name__ == "__main__":
    unittest.main()
