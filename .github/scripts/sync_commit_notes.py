#!/usr/bin/env python3
"""
Sync commit notes from all Mikecranesync repos into the Obsidian vault.

Reads commits via the GitHub API and generates daily markdown note files
in 10_Commit_Notes/. Tracks sync state in .sync-state.json to avoid
re-processing commits on subsequent runs.

Environment variables:
  GH_TOKEN     - GitHub PAT with repo read access
  REPO_FILTER  - (optional) Single repo name to sync
  BACKFILL     - (optional) "true" to walk full history
"""

import json
import os
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone

OWNER = "Mikecranesync"
GH_TOKEN = os.environ["GH_TOKEN"]
REPO_FILTER = os.environ.get("REPO_FILTER", "")
BACKFILL = os.environ.get("BACKFILL", "false") == "true"
NOTES_DIR = "10_Commit_Notes"
STATE_FILE = os.path.join(NOTES_DIR, ".sync-state.json")


def api_get(url):
    """Make authenticated GitHub API request."""
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {GH_TOKEN}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode()), resp.status
    except urllib.error.HTTPError as e:
        return None, e.code


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)


def get_repos():
    """Get all non-archived, non-fork repos for the owner."""
    if REPO_FILTER:
        print(f"Filtering to single repo: {REPO_FILTER}")
        return [REPO_FILTER]

    repos = []
    for endpoint in [f"/orgs/{OWNER}/repos", f"/users/{OWNER}/repos"]:
        page = 1
        while page <= 5:
            url = f"https://api.github.com{endpoint}?per_page=100&page={page}&type=owner"
            data, status = api_get(url)
            if status != 200 or not data:
                break
            for r in data:
                if not r.get("archived") and not r.get("fork"):
                    name = r["name"]
                    if name not in repos:
                        repos.append(name)
            if len(data) < 100:
                break
            page += 1
        if repos:
            break  # org endpoint worked, skip user endpoint

    print(f"Found {len(repos)} repos to sync")
    return repos


def get_commits(repo, last_sha=None):
    """Fetch commits from the GitHub API.

    Returns list of (sha, date, time, message, author) tuples.
    Stops when it hits last_sha (incremental mode).
    """
    max_pages = 50 if BACKFILL else 3
    per_page = 100
    commits = []

    for branch in ["main", "master"]:
        page = 1
        found_last = False
        while page <= max_pages:
            url = (
                f"https://api.github.com/repos/{OWNER}/{repo}/commits"
                f"?per_page={per_page}&page={page}&sha={branch}"
            )
            data, status = api_get(url)
            if status != 200 or not data:
                break

            for c in data:
                sha = c["sha"]
                if last_sha and sha == last_sha:
                    found_last = True
                    break
                date_str = c["commit"]["committer"]["date"]
                date = date_str[:10]
                time_str = date_str[11:16]
                msg = c["commit"]["message"].split("\n")[0][:120].replace("|", "\\|")
                author = c["commit"]["author"]["name"].replace("|", "\\|")
                commits.append((sha, date, time_str, msg, author))

            if found_last or len(data) < per_page:
                break
            page += 1

        if commits or found_last:
            break  # This branch exists

    return commits


def ensure_note_file(filepath, date):
    """Create a note file with frontmatter if it doesn't exist."""
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(
                f'---\ntitle: "Commit Notes - {date}"\ndate: {date}\n'
                f"tags: [type/commit-note]\nstatus: active\n---\n\n"
                f"# Commit Notes - {date}\n"
            )


def append_commit(filepath, repo, date, time_str, sha, msg, author):
    """Append a commit to the daily note file. Idempotent — skips if hash already present."""
    short_sha = sha[:7]

    ensure_note_file(filepath, date)

    with open(filepath, "r") as f:
        content = f.read()

    # Idempotency: skip if hash already in file
    if short_sha in content:
        return False

    # Add project tag if not present
    tag = f"project/{repo}"
    if tag not in content:
        content = content.replace("tags: [", f"tags: [{tag}, ", 1)

    # Check if section header exists for this repo+time
    section_header = f"## {repo} \u2014 Push at {time_str} UTC"
    if section_header not in content:
        content += (
            f"\n{section_header}\n\n"
            f"**Trigger:** `{short_sha}` on `main`\n\n"
            f"| Hash | Message | Author |\n"
            f"|------|---------|--------|\n"
        )

    # Append commit row
    content += f"| `{short_sha}` | {msg} | {author} |\n"

    with open(filepath, "w") as f:
        f.write(content)

    return True


def update_commit_counts(filepath):
    """Update **Commits:** count in each section header."""
    with open(filepath, "r") as f:
        content = f.read()

    sections = re.split(r"(## .+ \u2014 Push at .+ UTC)", content)
    if len(sections) < 2:
        return

    result = sections[0]
    i = 1
    while i < len(sections):
        header = sections[i]
        body = sections[i + 1] if i + 1 < len(sections) else ""
        rows = [line for line in body.strip().split("\n") if line.startswith("| `")]
        count = len(rows)
        body = re.sub(r"\*\*Commits:\*\* \d+", f"**Commits:** {count}", body)
        if "**Commits:**" not in body:
            body = body.replace(
                "**Trigger:**", f"**Commits:** {count}\n**Trigger:**", 1
            )
        result += header + body
        i += 2

    with open(filepath, "w") as f:
        f.write(result)


def main():
    os.makedirs(NOTES_DIR, exist_ok=True)
    state = load_state()
    repos = get_repos()
    total_new = 0
    modified_files = set()

    for repo in repos:
        print(f"::group::Processing {repo}")
        last_sha = state.get(repo, {}).get("last_sha", "")
        mode = "backfill" if BACKFILL else "incremental"
        print(f"  Mode: {mode}, last_sha: {last_sha[:7] if last_sha else 'none'}")

        commits = get_commits(repo, last_sha if not BACKFILL else None)

        if not commits:
            print(f"  No new commits for {repo}")
            print("::endgroup::")
            continue

        newest_sha = commits[0][0]

        for sha, date, time_str, msg, author in commits:
            filepath = os.path.join(NOTES_DIR, f"{date}.md")
            if append_commit(filepath, repo, date, time_str, sha, msg, author):
                total_new += 1
                modified_files.add(filepath)

        # Update state
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        state[repo] = {"last_sha": newest_sha, "last_sync": now}

        print(f"  Processed {len(commits)} commits, {total_new} new notes so far")
        print("::endgroup::")

    # Update commit counts in modified files
    for filepath in modified_files:
        update_commit_counts(filepath)

    save_state(state)
    print(f"\nTotal new commit notes: {total_new}")
    print(f"Modified files: {len(modified_files)}")


if __name__ == "__main__":
    main()
