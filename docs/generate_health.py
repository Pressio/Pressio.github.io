#!/usr/bin/env python3
"""Generate the Pressio ecosystem health page from GitHub metadata.

Curated lifecycle and planning information lives in
``source/_data/ecosystem_health.json``. Volatile repository information is
collected at build time so the published page stays current.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "source" / "_data" / "ecosystem_health.json"
OUTPUT_PATH = ROOT / "source" / "health.rst"
GITHUB_API = "https://api.github.com"
OWNER = "Pressio"

STATUS_LABELS = {
    "healthy": "Healthy",
    "attention": "Needs attention",
    "modernization-planned": "Modernization planned",
    "modernization": "Modernization underway",
    "maintenance": "Maintenance only",
    "unmaintained": "Unmaintained",
}


def request_json(path: str, token: str | None) -> object:
    request = urllib.request.Request(
        f"{GITHUB_API}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "pressio-health-dashboard",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def issue_count(repo: str, qualifier: str, token: str | None) -> int:
    query = urllib.parse.quote(f"repo:{OWNER}/{repo} is:issue is:open {qualifier}")
    result = request_json(f"/search/issues?q={query}&per_page=1", token)
    return int(result["total_count"])


def collect_ci(repo: str, branch: str, workflows: list[str], token: str | None) -> tuple[str, str]:
    """Summarize configured Actions workflows on the current default-branch HEAD."""
    actions_url = f"https://github.com/{OWNER}/{repo}/actions"
    if not workflows:
        return "unknown", actions_url

    branch_path = urllib.parse.quote(branch, safe="")
    head = request_json(f"/repos/{OWNER}/{repo}/branches/{branch_path}", token)["commit"]["sha"]
    wanted = {f".github/workflows/{name}" for name in workflows}
    latest: dict[str, dict[str, object]] = {}
    page = 1
    while True:
        response = request_json(
            f"/repos/{OWNER}/{repo}/actions/runs?head_sha={head}&per_page=100&page={page}",
            token,
        )
        runs = response["workflow_runs"]
        for run in runs:
            path = run.get("path")
            if (run.get("head_sha") != head or path not in wanted
                    or run.get("event") not in {"push", "schedule", "workflow_dispatch"}):
                continue
            previous = latest.get(path)
            if previous is None or (run.get("created_at", ""), run.get("id", 0)) > (
                previous.get("created_at", ""), previous.get("id", 0)
            ):
                latest[path] = run
        if len(runs) < 100:
            break
        page += 1

    selected = list(latest.values())
    if not selected:
        return "unknown", actions_url

    failures = [run for run in selected if run.get("status") == "completed"
                and run.get("conclusion") not in {"success", "neutral", "skipped", None}]
    pending = [run for run in selected if run.get("status") != "completed"
               or run.get("conclusion") is None]
    if failures:
        return "failure", str(failures[0]["html_url"])
    if pending:
        return "pending", str(pending[0]["html_url"])
    if all(run.get("conclusion") == "success" for run in selected):
        return "success", str(selected[0]["html_url"])
    return "unknown", actions_url


def collect_repository(config: dict[str, object], token: str | None) -> dict[str, object]:
    repo = str(config["name"])
    result = dict(config)
    result["github_url"] = f"https://github.com/{OWNER}/{repo}"
    try:
        metadata = request_json(f"/repos/{OWNER}/{repo}", token)
        result["default_branch"] = metadata["default_branch"]
        result["open_issues"] = issue_count(repo, "", token)
        result["priority_issues"] = issue_count(
            repo, str(config.get("priority_query", "label:release-blocker")), token
        )

        try:
            release = request_json(f"/repos/{OWNER}/{repo}/releases/latest", token)
            result["release"] = release["tag_name"]
            result["release_url"] = release["html_url"]
            result["release_date"] = (release.get("published_at") or "")[:10]
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
            result["release"] = "No GitHub release"
            result["release_url"] = f"{result['github_url']}/releases"
            result["release_date"] = ""

        result["ci"], result["ci_url"] = collect_ci(
            repo, str(result["default_branch"]), config.get("ci_workflows", []), token
        )
    except (OSError, KeyError, TypeError, ValueError) as error:
        result["collection_error"] = str(error)
        result.setdefault("open_issues", "—")
        result.setdefault("priority_issues", "—")
        result.setdefault("release", config.get("release_fallback", "—"))
        result.setdefault("release_url", f"{result['github_url']}/releases")
        result.setdefault("release_date", "")
        result.setdefault("ci", "unknown")
        result.setdefault("ci_url", f"{result['github_url']}/actions")
    return result


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def repo_card(repo: dict[str, object]) -> str:
    status = str(repo["lifecycle"])
    status_label = STATUS_LABELS.get(status, status.replace("-", " ").title())
    ci = str(repo["ci"])
    ci_label = ci.replace("_", " ").title()
    issue_url = f"{repo['github_url']}/issues?q=is%3Aissue+is%3Aopen"
    priority_query = urllib.parse.quote_plus(
        f"is:issue is:open {repo.get('priority_query', 'label:release-blocker')}"
    )
    priority_url = f"{repo['github_url']}/issues?q={priority_query}"

    tracking = ""
    if repo.get("tracking_issues"):
        links = [
            f'<a href="{repo["github_url"]}/issues/{number}">#{number}</a>'
            for number in repo["tracking_issues"]
        ]
        tracking = f'<p class="health-tracking">Tracking: {", ".join(links)}</p>'

    return f"""
<article class="health-card" data-status="{escape(status)}">
  <div class="health-card__header">
    <div>
      <h2><a href="{escape(repo['github_url'])}">{escape(repo['display_name'])}</a></h2>
      <p class="health-role">{escape(repo['role'])}</p>
    </div>
    <span class="health-status health-status--{escape(status)}">{escape(status_label)}</span>
  </div>
  <div class="health-metrics">
    <a class="health-metric" href="{escape(repo['release_url'])}">
      <span>Latest release</span><strong>{escape(repo['release'])}</strong>
      <small>{escape(repo['release_date']) or 'Date unavailable'}</small>
    </a>
    <a class="health-metric" href="{escape(repo['ci_url'])}">
      <span>Default-branch CI</span><strong class="ci-{escape(ci)}">{escape(ci_label)}</strong>
      <small>Current default-branch commit</small>
    </a>
    <a class="health-metric" href="{escape(issue_url)}">
      <span>Open issues</span><strong>{escape(repo['open_issues'])}</strong>
      <small>Pull requests excluded</small>
    </a>
    <a class="health-metric" href="{escape(priority_url)}">
      <span>Release blockers</span><strong>{escape(repo['priority_issues'])}</strong>
      <small>Curated by label</small>
    </a>
  </div>
  <div class="health-next">
    <span>Next objective</span>
    <p>{escape(repo['next_goal'])}</p>
    {tracking}
  </div>
  <div class="health-card__footer">
    <span>{escape(repo['lifecycle_note'])}</span>
    <a href="{escape(repo['documentation'])}">Documentation <span aria-hidden="true">→</span></a>
  </div>
</article>"""


def render(repositories: list[dict[str, object]], collected_at: str) -> str:
    counts = {key: 0 for key in STATUS_LABELS}
    for repo in repositories:
        counts[str(repo["lifecycle"])] = counts.get(str(repo["lifecycle"]), 0) + 1

    cards = "\n".join(repo_card(repo) for repo in repositories)
    indented_cards = "".join(f"   {line}\n" for line in cards.splitlines())
    return f""".. This file is generated by docs/generate_health.py. Edit the JSON config instead.

Pressio ecosystem health
========================

This dashboard gives maintainers a shared view of release readiness and the
most important work across the core Pressio repositories. Repository data was
last collected **{collected_at} UTC**. Lifecycle assessments and next objectives
are curated by the Pressio team; releases, CI, and issue counts come from GitHub.

.. raw:: html

   <div class="health-summary" aria-label="Ecosystem summary">
     <div><strong>{len(repositories)}</strong><span>Repositories tracked</span></div>
     <div><strong>{counts.get('healthy', 0)}</strong><span>Healthy</span></div>
     <div><strong>{counts.get('attention', 0)}</strong><span>Need attention</span></div>
     <div><strong>{counts.get('modernization-planned', 0)}</strong><span>Modernization planned</span></div>
   </div>

Repository health
-----------------

.. raw:: html

   <div class="health-grid">
{indented_cards}   </div>

How to read this page
---------------------

``Healthy`` means the repository is actively maintained and expected to work
on its supported platforms. ``Needs attention`` identifies a usable repository
with specific maintenance work. ``Modernization planned`` identifies an
approved recovery or migration that has not necessarily begun, while
``Modernization underway`` means that implementation is active. These lifecycle
assessments are deliberately separate from the latest CI result: a passing
build alone does not establish project health.

The dashboard does not treat a large issue count as inherently unhealthy.
Release blockers are issues explicitly classified by maintainers and are the
most useful starting point for release planning.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Generate the page without requesting volatile GitHub metadata.",
    )
    args = parser.parse_args()

    with CONFIG_PATH.open(encoding="utf-8") as stream:
        config = json.load(stream)

    token = os.environ.get("GITHUB_TOKEN")
    repositories = []
    for item in config["repositories"]:
        if args.offline:
            repo = dict(item)
            repo.update(
                {
                    "github_url": f"https://github.com/{OWNER}/{item['name']}",
                    "open_issues": "—",
                    "priority_issues": "—",
                    "release": item.get("release_fallback", "—"),
                    "release_url": f"https://github.com/{OWNER}/{item['name']}/releases",
                    "release_date": "",
                    "ci": "unknown",
                    "ci_url": f"https://github.com/{OWNER}/{item['name']}/actions",
                }
            )
        else:
            repo = collect_repository(item, token)
        repositories.append(repo)

    collected_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
    OUTPUT_PATH.write_text(render(repositories, collected_at), encoding="utf-8")


if __name__ == "__main__":
    main()
