from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.knowledge.localization import (  # noqa: E402
    _cached_localization_registry,
    approved_localization,
    load_localization_registry,
    localization_status,
    source_text_sha256,
)


def _write(path: Path, row: dict) -> None:
    path.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
    load_localization_registry.cache_clear()
    _cached_localization_registry.cache_clear()


def main() -> int:
    source = {"id": "game_detail_test", "summary_th": "คำอธิบายต้นฉบับ"}
    with tempfile.TemporaryDirectory() as temp_dir:
        registry = Path(temp_dir) / "registry.jsonl"
        base = {
            "content_id": source["id"],
            "field": "summary_th",
            "locale": "en",
            "text": "Approved English summary.",
            "source_text_sha256": source_text_sha256(source["summary_th"]),
            "status": "approved",
            "version": 1,
            "approved_by": "reviewer-1",
            "approved_at": "2026-09-02T10:00:00+07:00",
        }
        _write(registry, base)
        assert approved_localization(source, "summary_th", registry_path=registry) == "Approved English summary."
        assert localization_status(source, "summary_th", registry_path=registry) == "approved"

        changed = dict(source, summary_th="ข้อความต้นฉบับที่แก้แล้ว")
        assert approved_localization(changed, "summary_th", registry_path=registry) is None
        assert localization_status(changed, "summary_th", registry_path=registry) == "stale"

        draft = dict(base, status="draft", approved_by="", approved_at="")
        _write(registry, draft)
        assert approved_localization(source, "summary_th", registry_path=registry) is None
        assert localization_status(source, "summary_th", registry_path=registry) == "draft"

        os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW"] = "1"
        os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH"] = str(registry)
        try:
            assert approved_localization(source, "summary_th") == "Approved English summary."
            assert localization_status(source, "summary_th") == "draft_preview"
        finally:
            os.environ.pop("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW", None)
            os.environ.pop("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH", None)
            load_localization_registry.cache_clear()

        # A narrow preview file must add to the published registry rather
        # than erase every unrelated English localization.
        published = registry.with_name("published.jsonl")
        other = {"id": "game_detail_other", "summary_th": "ข้อมูลอื่น"}
        _write(published, dict(base, content_id=other["id"], source_text_sha256=source_text_sha256(other["summary_th"])))
        preview = registry.with_name("preview.jsonl")
        _write(preview, draft)
        from unittest.mock import patch
        with patch("app.knowledge.localization.active_registry_path", return_value=published):
            os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW"] = "1"
            os.environ["PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH"] = str(preview)
            try:
                assert approved_localization(source, "summary_th") == "Approved English summary."
                assert approved_localization(other, "summary_th") == "Approved English summary."
            finally:
                os.environ.pop("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW", None)
                os.environ.pop("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH", None)
                load_localization_registry.cache_clear()
                _cached_localization_registry.cache_clear()

    print("OK approved overlay, source invalidation, draft rejection, and local draft preview")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
