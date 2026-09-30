from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.knowledge.localization import source_text_sha256  # noqa: E402
from tools.manage_english_localizations import (  # noqa: E402
    approve_selected_drafts,
    source_fields,
    validate_candidate,
    write_review_queue,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def main() -> int:
    (content_id, field), source = next(iter(source_fields().items()))
    source_text = source[field]
    category = str(source.get("category") or "knowledge")
    draft = {
        "content_id": content_id,
        "field": field,
        "locale": "en",
        "text": "Reviewed English draft.",
        "source_text": source_text,
        "source_text_sha256": source_text_sha256(source_text),
        "status": "draft",
        "version": 1,
        "approved_by": "",
        "approved_at": "",
    }
    selector = f"{content_id}:{field}"

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        draft_path = temp / "drafts.jsonl"
        queue_path = temp / "review.md"
        candidate_path = temp / "candidate.jsonl"
        _write_jsonl(draft_path, [draft])

        assert write_review_queue(draft_path, queue_path, category=category) == 1
        queue = queue_path.read_text(encoding="utf-8")
        assert selector in queue
        assert "Thai source" in queue
        assert "English draft" in queue

        assert approve_selected_drafts(
            draft_path,
            candidate_path,
            selections=[selector],
            reviewer="psu-reviewer",
            approved_at="2026-09-09T12:00:00+07:00",
        ) == 1
        candidate = json.loads(candidate_path.read_text(encoding="utf-8").strip())
        assert candidate["status"] == "approved"
        assert candidate["approved_by"] == "psu-reviewer"
        _rows, errors = validate_candidate(candidate_path)
        assert not errors, errors

        try:
            approve_selected_drafts(draft_path, candidate_path, selections=[], reviewer="psu-reviewer")
        except ValueError as exc:
            assert "at least one" in str(exc)
        else:
            raise AssertionError("approval without an explicit selection must fail")

    print("OK explicit English localization review and approval candidate workflow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
