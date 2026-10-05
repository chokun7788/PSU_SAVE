from __future__ import annotations

import json
import unittest
from pathlib import Path

from app.pipeline.competition_source_facets import competition_source_facets
from app.pipeline.competition_targets import competition_facet
from app.pipeline.retrieval import competition_hits_cover_intent, retrieve_competition_contract_rows


ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl"


class CompetitionSourceFacetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        rows = [
            json.loads(line)
            for line in CHUNKS.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.rows = {str(row["id"]): row for row in rows}

    def facets(self, row_id: str) -> frozenset[str]:
        return competition_source_facets(self.rows[row_id])

    def test_post_match_result_is_not_in_match_procedure(self) -> None:
        self.assertNotIn(
            "in_match_operations",
            self.facets("competition_rules_valorant_psu_phuket_2026_s19_c01"),
        )

    def test_venue_only_is_not_an_on_site_requirement(self) -> None:
        self.assertNotIn(
            "pre_match_on_site",
            self.facets("competition_rules_rov_blueket_2025_men_s04_c01"),
        )

    def test_direct_before_match_requirement_is_supported(self) -> None:
        self.assertIn(
            "pre_match_on_site",
            self.facets("competition_rules_cs2_psu_phuket_2026_s52_c01"),
        )

    def test_single_substitute_mention_is_not_roster_composition(self) -> None:
        self.assertNotIn(
            "roster_composition",
            self.facets("competition_rules_valorant_psu_phuket_2026_s08_c01"),
        )

    def test_valorant_multi_topic_chunk_exposes_map_pool(self) -> None:
        facets = self.facets("competition_rules_valorant_psu_phuket_2026_s03_c01")
        self.assertIn("map_pool", facets)
        self.assertIn("pre_match_on_site", facets)

    def test_checkin_is_not_registration_or_eligibility(self) -> None:
        facets = self.facets("competition_rules_valorant_psu_phuket_2026_s18_c01")
        self.assertIn("pre_match_on_site", facets)
        self.assertNotIn("registration", facets)
        self.assertNotIn("eligibility_registration", facets)

    def test_penalty_type_section_supports_penalty(self) -> None:
        facets = self.facets("competition_rules_valorant_psu_phuket_2026_s25_c01")
        self.assertIn("penalty", facets)
        self.assertIn("penalty_matrix", facets)

    def test_contract_retrieval_recovers_paraphrased_cs2_procedure(self) -> None:
        hits, _trace = retrieve_competition_contract_rows(
            "Counter-Strike 2 แข่งจริง กฎเกี่ยวกับขั้นตอนระหว่างการแข่งขัน เป็นแบบไหน"
        )
        self.assertTrue(hits)
        self.assertTrue(all(
            row.get("document_id") == "competition_rules_cs2_psu_phuket_2026"
            or "competition_rules_cs2_psu_phuket_2026" in (row.get("source_ids") or [])
            for row in hits
        ))
        self.assertTrue(
            all("in_match_operations" in competition_source_facets(row) for row in hits)
        )

    def test_broad_on_site_question_accepts_direct_area_restrictions(self) -> None:
        question = "กติกา CS2 เรื่องข้อกำหนดก่อนแข่งและหน้างาน ว่าอย่างไร"
        hits, _trace = retrieve_competition_contract_rows(question)
        self.assertTrue(competition_hits_cover_intent(question, hits))

    def test_gold_topic_phrases_resolve_to_canonical_facets(self) -> None:
        cases = {
            "competition format": "competition_format",
            "competition equipment and devices": "equipment",
            "tournament schedule": "schedule",
            "เวอร์ชันเกมและการตั้งค่าแมตช์": "match_configuration",
            "ตารางและเวลาแข่งขัน": "schedule",
            "maps, vetoes, and map selection": "map_pool",
            "How many starting players must a VALORANT team field?": "team_size",
            "Who should a player contact for a general issue during a VALORANT match?": "in_match_operations",
            "What procedure must officials follow for an unspecified incident during a VALORANT match?": "in_match_operations",
        }
        for question, expected in cases.items():
            with self.subTest(question=question):
                self.assertEqual(competition_facet(question), expected)


if __name__ == "__main__":
    unittest.main()
