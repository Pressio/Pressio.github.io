"""Regression tests for the health dashboard's CI summary."""

import unittest
from unittest.mock import patch

import generate_health


HEAD = "a" * 40
OLD = "b" * 40
REPO = "rom-tools-and-workflows"
TEST_PATH = ".github/workflows/install-and-test.yaml"


def run(path, conclusion, *, sha=HEAD, status="completed", created="2026-09-24T00:00:00Z", ident=1):
    return {
        "path": path,
        "head_sha": sha,
        "event": "push",
        "status": status,
        "conclusion": conclusion,
        "created_at": created,
        "id": ident,
        "html_url": f"https://github.com/Pressio/{REPO}/actions/runs/{ident}",
    }


class CollectCiTests(unittest.TestCase):
    def collect(self, runs, workflows=("install-and-test.yaml",)):
        def response(path, token):
            if "/branches/" in path:
                return {"commit": {"sha": HEAD}}
            if "/actions/runs" in path:
                return {"workflow_runs": runs}
            raise AssertionError(path)

        with patch.object(generate_health, "request_json", side_effect=response) as request:
            result = generate_health.collect_ci(REPO, "develop", list(workflows), None)
        return result, [call.args[0] for call in request.call_args_list]

    def test_failed_test_workflow_overrides_successful_publishing_and_docs(self):
        runs = [
            run(".github/workflows/publish_pypi_package.yaml", "success", ident=3),
            run(TEST_PATH, "failure", ident=2),
            run(".github/workflows/deploy_docs.yaml", "success", ident=4),
            run(TEST_PATH, "success", sha=OLD, ident=5),
        ]
        (status, url), requests = self.collect(runs)
        self.assertEqual(status, "failure")
        self.assertTrue(url.endswith("/runs/2"))
        self.assertIn(f"head_sha={HEAD}", requests[1])

    def test_pending_workflow_is_not_reported_as_passing(self):
        (status, _), _ = self.collect([run(TEST_PATH, None, status="in_progress")])
        self.assertEqual(status, "pending")

    def test_newer_run_replaces_older_failure_for_same_workflow(self):
        runs = [
            run(TEST_PATH, "failure", created="2026-09-23T00:00:00Z", ident=1),
            run(TEST_PATH, "success", created="2026-09-24T00:00:00Z", ident=2),
        ]
        (status, url), _ = self.collect(runs)
        self.assertEqual(status, "success")
        self.assertTrue(url.endswith("/runs/2"))

    def test_no_matching_ci_run_is_unknown(self):
        (status, url), _ = self.collect([run(".github/workflows/deploy_docs.yaml", "success")])
        self.assertEqual(status, "unknown")
        self.assertTrue(url.endswith("/actions"))

    def test_skipped_workflow_does_not_count_as_passing(self):
        runs = [
            run(TEST_PATH, "success", ident=1),
            run(".github/workflows/other-test.yml", "skipped", ident=2),
        ]
        (status, _), _ = self.collect(runs, workflows=("install-and-test.yaml", "other-test.yml"))
        self.assertEqual(status, "unknown")

    def test_publishing_can_be_explicitly_configured_as_ci(self):
        (status, _), _ = self.collect(
            [run(".github/workflows/publish_pypi_package.yaml", "failure")],
            workflows=("publish_pypi_package.yaml",),
        )
        self.assertEqual(status, "failure")

    def test_failure_takes_precedence_over_another_pending_ci_workflow(self):
        runs = [
            run(TEST_PATH, "failure", ident=1),
            run(".github/workflows/other-test.yml", None, status="queued", ident=2),
        ]
        (status, url), _ = self.collect(runs, workflows=("install-and-test.yaml", "other-test.yml"))
        self.assertEqual(status, "failure")
        self.assertTrue(url.endswith("/runs/1"))

    def test_reads_all_pages_before_summarizing(self):
        unrelated = [run(".github/workflows/deploy_docs.yaml", "success", ident=i) for i in range(100)]

        def response(path, token):
            if "/branches/" in path:
                return {"commit": {"sha": HEAD}}
            return {"workflow_runs": unrelated if "&page=1" in path else [run(TEST_PATH, "failure", ident=101)]}

        with patch.object(generate_health, "request_json", side_effect=response) as request:
            status, _ = generate_health.collect_ci(REPO, "develop", ["install-and-test.yaml"], None)
        self.assertEqual(status, "failure")
        self.assertEqual(request.call_count, 3)


if __name__ == "__main__":
    unittest.main()
