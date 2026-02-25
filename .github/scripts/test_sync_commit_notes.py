"""Tests for sync_commit_notes.py"""

import json
import os
from unittest.mock import patch, MagicMock

import pytest


# We need to patch env vars before importing the module
@pytest.fixture(autouse=True)
def _patch_module_globals(tmp_path, monkeypatch):
    """Patch module-level globals so every test uses a temp directory."""
    monkeypatch.setenv("GH_TOKEN", "fake-token")
    monkeypatch.setenv("REPO_FILTER", "")
    monkeypatch.setenv("BACKFILL", "false")

    import sync_commit_notes as mod

    notes_dir = str(tmp_path / "10_Commit_Notes")
    os.makedirs(notes_dir, exist_ok=True)

    monkeypatch.setattr(mod, "NOTES_DIR", notes_dir)
    monkeypatch.setattr(mod, "STATE_FILE", os.path.join(notes_dir, ".sync-state.json"))
    monkeypatch.setattr(mod, "GH_TOKEN", "fake-token")
    monkeypatch.setattr(mod, "BACKFILL", False)
    monkeypatch.setattr(mod, "REPO_FILTER", "")


@pytest.fixture
def mod():
    import sync_commit_notes as m
    return m


# ---------------------------------------------------------------------------
# ensure_note_file
# ---------------------------------------------------------------------------


def test_ensure_note_file_creates_with_frontmatter(mod, tmp_path):
    filepath = str(tmp_path / "2026-02-25.md")
    mod.ensure_note_file(filepath, "2026-02-25")

    content = open(filepath).read()
    assert "title: \"Commit Notes - 2026-02-25\"" in content
    assert "date: 2026-02-25" in content
    assert "tags: [type/commit-note]" in content
    assert "status: active" in content
    assert "# Commit Notes - 2026-02-25" in content


def test_ensure_note_file_no_overwrite(mod, tmp_path):
    filepath = str(tmp_path / "2026-02-25.md")
    with open(filepath, "w") as f:
        f.write("existing content")

    mod.ensure_note_file(filepath, "2026-02-25")

    content = open(filepath).read()
    assert content == "existing content"


# ---------------------------------------------------------------------------
# append_commit
# ---------------------------------------------------------------------------


def test_append_commit_creates_section(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    result = mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "abc1234567890", "feat: add thing", "Mike",
    )

    assert result is True
    content = open(filepath).read()
    assert "project/factorylm" in content
    assert "## factorylm \u2014 Push at 14:30 UTC" in content
    assert "| Hash | Message | Author |" in content
    assert "| `abc1234` | feat: add thing | Mike |" in content


def test_append_commit_idempotent(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "abc1234567890", "feat: add thing", "Mike",
    )
    result = mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "abc1234567890", "feat: add thing", "Mike",
    )

    assert result is False
    content = open(filepath).read()
    # short_sha appears in Trigger line + commit row = 2, but only one commit row
    assert content.count("| `abc1234` |") == 1


def test_append_commit_multiple_repos_same_day(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "aaa1234567890", "feat: one", "Mike",
    )
    mod.append_commit(
        filepath, "factorylm-core", "2026-02-25", "15:00",
        "bbb1234567890", "fix: two", "Mike",
    )

    content = open(filepath).read()
    assert "## factorylm \u2014 Push at 14:30 UTC" in content
    assert "## factorylm-core \u2014 Push at 15:00 UTC" in content
    assert "project/factorylm," in content
    assert "project/factorylm-core," in content


def test_append_commit_multiple_commits_same_section(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "aaa1234567890", "feat: first", "Mike",
    )
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "bbb1234567890", "feat: second", "Mike",
    )

    content = open(filepath).read()
    # Only one section header
    assert content.count("## factorylm \u2014 Push at 14:30 UTC") == 1
    # Both commit rows present
    assert "| `aaa1234` |" in content
    assert "| `bbb1234` |" in content


# ---------------------------------------------------------------------------
# update_commit_counts
# ---------------------------------------------------------------------------


def test_update_commit_counts(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    # Build a file with a section and two commit rows
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "aaa1234567890", "feat: first", "Mike",
    )
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "bbb1234567890", "feat: second", "Mike",
    )

    mod.update_commit_counts(filepath)

    content = open(filepath).read()
    assert "**Commits:** 2" in content


def test_update_commit_counts_inserts_missing(mod):
    filepath = os.path.join(mod.NOTES_DIR, "2026-02-25.md")
    # append_commit doesn't add **Commits:** lines, so they're missing by default
    mod.append_commit(
        filepath, "factorylm", "2026-02-25", "14:30",
        "aaa1234567890", "feat: first", "Mike",
    )

    content_before = open(filepath).read()
    assert "**Commits:**" not in content_before

    mod.update_commit_counts(filepath)

    content = open(filepath).read()
    assert "**Commits:** 1" in content
    # Inserted before **Trigger:**
    trigger_pos = content.index("**Trigger:**")
    commits_pos = content.index("**Commits:** 1")
    assert commits_pos < trigger_pos


# ---------------------------------------------------------------------------
# load_state / save_state
# ---------------------------------------------------------------------------


def test_load_state_empty(mod):
    result = mod.load_state()
    assert result == {}


def test_save_and_load_state_roundtrip(mod):
    state = {
        "factorylm": {"last_sha": "abc123", "last_sync": "2026-02-25T14:30:00Z"},
        "factorylm-core": {"last_sha": "def456", "last_sync": "2026-02-25T15:00:00Z"},
    }
    mod.save_state(state)
    loaded = mod.load_state()
    assert loaded == state


# ---------------------------------------------------------------------------
# get_commits (mocked API)
# ---------------------------------------------------------------------------


def _make_commit(sha, date, msg, author="Mike"):
    return {
        "sha": sha,
        "commit": {
            "committer": {"date": f"{date}T12:00:00Z"},
            "author": {"name": author},
            "message": msg,
        },
    }


def test_get_commits_stops_at_last_sha(mod):
    commits_data = [
        _make_commit("new111", "2026-02-25", "feat: new"),
        _make_commit("old222", "2026-02-24", "fix: old"),
        _make_commit("last33", "2026-02-23", "chore: last"),
    ]

    with patch.object(mod, "api_get", return_value=(commits_data, 200)):
        result = mod.get_commits("factorylm", last_sha="last33")

    shas = [r[0] for r in result]
    assert "new111" in shas
    assert "old222" in shas
    assert "last33" not in shas


def test_get_commits_falls_back_to_master(mod):
    commits_data = [_make_commit("abc123", "2026-02-25", "feat: thing")]

    def fake_api_get(url):
        if "sha=main" in url:
            return None, 404
        return commits_data, 200

    with patch.object(mod, "api_get", side_effect=fake_api_get):
        result = mod.get_commits("factorylm")

    assert len(result) == 1
    assert result[0][0] == "abc123"


# ---------------------------------------------------------------------------
# get_repos (mocked env)
# ---------------------------------------------------------------------------


def test_get_repos_with_filter(mod, monkeypatch):
    monkeypatch.setattr(mod, "REPO_FILTER", "factorylm-core")
    result = mod.get_repos()
    assert result == ["factorylm-core"]


# ---------------------------------------------------------------------------
# main() integration (mocked API)
# ---------------------------------------------------------------------------


def test_main_incremental_flow(mod, monkeypatch):
    commits_data = [
        _make_commit("sha_aaa", "2026-02-25", "feat: alpha", "Mike"),
        _make_commit("sha_bbb", "2026-02-24", "fix: beta", "Mike"),
    ]
    repos_data = [{"name": "factorylm", "archived": False, "fork": False}]

    def fake_api_get(url):
        if "/repos?" in url or "/repos?" in url:
            return repos_data, 200
        if "/commits" in url:
            return commits_data, 200
        return None, 404

    monkeypatch.setattr(mod, "REPO_FILTER", "")
    with patch.object(mod, "api_get", side_effect=fake_api_get):
        mod.main()

    # Note files created
    assert os.path.exists(os.path.join(mod.NOTES_DIR, "2026-02-25.md"))
    assert os.path.exists(os.path.join(mod.NOTES_DIR, "2026-02-24.md"))

    # State file updated
    state = mod.load_state()
    assert "factorylm" in state
    assert state["factorylm"]["last_sha"] == "sha_aaa"

    # Content correct
    content = open(os.path.join(mod.NOTES_DIR, "2026-02-25.md")).read()
    assert "sha_aaa" in content
    assert "feat: alpha" in content


def test_main_idempotent_rerun(mod, monkeypatch):
    commits_data = [
        _make_commit("sha_aaa", "2026-02-25", "feat: alpha", "Mike"),
    ]
    repos_data = [{"name": "factorylm", "archived": False, "fork": False}]

    def fake_api_get(url):
        if "/repos?" in url:
            return repos_data, 200
        if "/commits" in url:
            return commits_data, 200
        return None, 404

    monkeypatch.setattr(mod, "REPO_FILTER", "")
    with patch.object(mod, "api_get", side_effect=fake_api_get):
        mod.main()
        # Reset state's last_sha so main() fetches same commits again
        state = mod.load_state()
        state["factorylm"]["last_sha"] = ""
        mod.save_state(state)
        mod.main()

    content = open(os.path.join(mod.NOTES_DIR, "2026-02-25.md")).read()
    # Commit row should appear only once despite two runs
    # (sha also appears in Trigger line, so check the row specifically)
    assert content.count("| `sha_aaa` |") == 1
