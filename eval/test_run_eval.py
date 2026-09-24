"""Offline regression tests; these do not produce an evaluation transcript."""

import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run_eval


class GradeOneTests(unittest.TestCase):
    def grade(self, proc):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp) / "bundle.md"
            bundle.write_text("Frozen evidence", encoding="utf-8")
            with patch.object(run_eval.subprocess, "run", return_value=proc):
                return run_eval.grade_one("sample", bundle, "skill", "rubric", 10)

    def test_stdout_only_failure_is_visible(self):
        message = "You've hit your individual spend limit"
        result = self.grade(subprocess.CompletedProcess([], 1, message, ""))
        self.assertIn(message, result["error"])
        self.assertIsNone(result["verdict"])

    def test_both_error_streams_are_visible(self):
        result = self.grade(subprocess.CompletedProcess(
            [], 1, "Account limit\nAsk your admin", "Request failed"))
        self.assertIn("stderr: Request failed", result["error"])
        self.assertIn("stdout: Account limit Ask your admin", result["error"])

    def test_empty_error_has_explicit_fallback(self):
        result = self.grade(subprocess.CompletedProcess([], 1, "", ""))
        self.assertIn("no output on stdout or stderr", result["error"])

    def test_successful_verdict_is_unchanged(self):
        output = '```json\n{"verdict":"reject","checks":[' \
                 '{"name":"scope","grade":"fail","evidence":"umbrella"}]}\n```'
        result = self.grade(subprocess.CompletedProcess([], 0, output, ""))
        self.assertEqual(result["verdict"], "reject")
        self.assertEqual(result["failed_checks"], ["scope"])
        self.assertIsNone(result["error"])


class SaveRunTests(unittest.TestCase):
    def test_failed_full_run_preserves_existing_file_and_reports_errors(self):
        self.check_saved_file(failed=True)

    def test_successful_partial_run_preserves_existing_file(self):
        self.check_saved_file(failed=False)

    def check_saved_file(self, failed):
        with tempfile.TemporaryDirectory() as tmp:
            rubric = Path(tmp) / "rubric.md"
            rubric.write_text("| scope | body | bounded | required |\n",
                              encoding="utf-8")
            saved = Path(tmp) / "existing-transcript.txt"
            saved.write_text("previous run", encoding="utf-8")
            args = ["run_eval.py", "--rubric", str(rubric),
                    "--save-run", str(saved)]
            if not failed:
                args += ["--limit", "1"]

            def grade(item_id, *args):
                return {"id": item_id, "verdict": None if failed else "accept",
                        "checks": [], "failed_checks": [],
                        "error": "account limit" if failed else None}

            stdout, stderr = io.StringIO(), io.StringIO()
            with patch.object(run_eval.sys, "argv", args), \
                    patch.object(run_eval, "grade_one", side_effect=grade), \
                    contextlib.redirect_stdout(stdout), \
                    contextlib.redirect_stderr(stderr):
                code = run_eval.main()
            self.assertEqual(saved.read_text(encoding="utf-8"), "previous run")
            self.assertEqual(code, 1 if failed else 0)
            if failed:
                self.assertIn("20 item(s) errored: NOT written", stdout.getvalue())
                self.assertNotIn("partial run:", stdout.getvalue())
            else:
                self.assertIn("partial run: NOT written", stdout.getvalue())
            self.assertNotIn(": PASS", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
