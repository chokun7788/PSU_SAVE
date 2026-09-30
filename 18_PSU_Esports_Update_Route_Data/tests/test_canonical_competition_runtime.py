"""Release-safety tests for Canonical Competition RAG runtime loading."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.knowledge import canonical_retrieval


def _projection(*, runtime_eligible: bool = True, release_id: str = "release_cs2") -> dict[str, object]:
    return {
        "chunk_id": "canonical_rag::cs2_001",
        "rule_id": "canonical::cs2_001",
        "release_id": release_id,
        "category": "competition_rules",
        "game_id": "cs2",
        "game": "Counter-Strike 2",
        "tournament": "PSU CS2 Test",
        "scope": "tournament_specific",
        "canonical_section": "match_configuration",
        "module": "cs2_map_veto_and_side_selection",
        "facet": "map_pool",
        "conditions": {"game_id": "cs2"},
        "text_th": "เกม: Counter-Strike 2\nรายการแข่งขัน: PSU CS2 Test\nกติกา: ใช้ Ancient และ Anubis",
        "source_locator": {"source_url": "local://test"},
        "runtime_eligible": runtime_eligible,
    }


class CanonicalCompetitionRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.projection_path = self.root / "competition_rule_rag_projections.jsonl"
        self.manifest_path = self.root / "active_release_manifest.json"
        canonical_retrieval.clear_canonical_rag_cache()
        self.original_enabled = os.environ.get("PSU_CANONICAL_COMPETITION_RAG_ENABLED")
        self.original_shadow = os.environ.get("PSU_CANONICAL_COMPETITION_RAG_SHADOW")
        os.environ["PSU_CANONICAL_COMPETITION_RAG_ENABLED"] = "1"
        os.environ["PSU_CANONICAL_COMPETITION_RAG_SHADOW"] = "1"

    def tearDown(self) -> None:
        canonical_retrieval.clear_canonical_rag_cache()
        self.temp_dir.cleanup()
        for name, original in {
            "PSU_CANONICAL_COMPETITION_RAG_ENABLED": self.original_enabled,
            "PSU_CANONICAL_COMPETITION_RAG_SHADOW": self.original_shadow,
        }.items():
            if original is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = original

    def _write(self, row: dict[str, object], active_ids: list[str]) -> None:
        self.projection_path.write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
        self.manifest_path.write_text(json.dumps({"active_release_ids": active_ids}), encoding="utf-8")

    def test_only_manifest_active_and_runtime_eligible_rows_are_adapted(self) -> None:
        self._write(_projection(), ["release_cs2"])

        rows = canonical_retrieval._load_active_competition_projection(
            str(self.projection_path), str(self.manifest_path)
        )

        self.assertEqual(1, len(rows))
        self.assertEqual("competition_rules", rows[0]["category"])
        self.assertEqual("owner_approved_release", rows[0]["trust_level"])
        self.assertEqual("cs2", rows[0]["entity_ids"][0])

    def test_inactive_or_unlisted_rows_never_enter_live_rag(self) -> None:
        self._write(_projection(runtime_eligible=False), ["release_cs2"])
        rows = canonical_retrieval._load_active_competition_projection(
            str(self.projection_path), str(self.manifest_path)
        )
        self.assertEqual((), rows)

    def test_active_release_replaces_legacy_projection_for_the_same_rulebook(self) -> None:
        generic_root = self.root / "generic"
        generic_root.mkdir()
        (generic_root / "rag_th_projection.jsonl").write_text(json.dumps({
            "projection_id": "legacy::cs2",
            "content_id": "competition.competition_rules_cs2_psu_phuket_2026",
            "category": "competition_rules",
            "text": "Legacy CS2 document",
            "status": "published",
            "facts": {"document_id": "release_cs2"},
        }, ensure_ascii=False) + "\n", encoding="utf-8")
        self._write(_projection(), ["release_cs2"])

        with (
            patch.object(canonical_retrieval, "PROJECTION_ROOT", generic_root),
            patch.object(canonical_retrieval, "COMPETITION_CANONICAL_ROOT", self.root),
        ):
            canonical_retrieval.clear_canonical_rag_cache()
            rows = canonical_retrieval.load_canonical_rag_rows(locale="th")

        self.assertEqual(["canonical_rag::cs2_001"], [row["id"] for row in rows])

        canonical_retrieval.clear_canonical_rag_cache()
        self._write(_projection(), [])
        rows = canonical_retrieval._load_active_competition_projection(
            str(self.projection_path), str(self.manifest_path)
        )
        self.assertEqual((), rows)

    def test_shadow_summary_never_adapts_rows_as_live_answers(self) -> None:
        self._write(_projection(runtime_eligible=False), [])
        with patch.object(canonical_retrieval, "COMPETITION_CANONICAL_ROOT", self.root):
            summary = canonical_retrieval.canonical_competition_shadow_summary("CS2 Ancient")

        self.assertTrue(summary["enabled"])
        self.assertEqual(1, summary["candidate_count"])
        self.assertEqual(["Counter-Strike 2"], summary["games"])


if __name__ == "__main__":
    unittest.main()
