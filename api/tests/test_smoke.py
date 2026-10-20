from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_scope_document_exists():
    assert (ROOT / "docs" / "scope.md").is_file()


def test_monorepo_layout():
    for folder in ("api", "ingest", "eval", "web", "docs"):
        assert (ROOT / folder).is_dir(), folder
