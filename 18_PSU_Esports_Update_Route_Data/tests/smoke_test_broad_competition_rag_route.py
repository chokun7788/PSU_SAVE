from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.hybrid_retrieval import answer_from_hybrid_hits, should_use_hybrid_retrieval
from app.pipeline.retrieval import looks_like_broad_competition_rules_query
from app.pipeline.schemas import PipelineRoute


def main() -> int:
    broad = "กฎการแข่งขัน Counter-Strike 2 มีอะไรบ้าง"
    precise = "Counter-Strike 2 ใช้แผนที่อะไร"
    assert looks_like_broad_competition_rules_query(broad)
    assert not looks_like_broad_competition_rules_query(precise)
    route = PipelineRoute("competition_rules", "competition_rules_lookup", 0.9, "fact", "medium", "test")
    assert should_use_hybrid_retrieval(route)
    answer, _raw_hits, _confidence = answer_from_hybrid_hits([
        {"category": "competition_rules", "_hybrid_score": 12.0, "_score": 8.0, "game": "Counter-Strike 2", "tournament": "Test", "source_url": "local://test", "text": "1. ขอบเขต ใช้กับผู้เล่นทุกคน"},
        {"category": "competition_rules", "_hybrid_score": 11.0, "_score": 7.0, "game": "Counter-Strike 2", "tournament": "Test", "source_url": "local://test", "text": "2. ตารางแข่งต้องยืนยันก่อนเริ่ม"},
    ], broad)
    assert answer is not None
    assert "ขอบเขต" in answer and "ตารางแข่ง" in answer
    print("OK broad competition rules requests select multi-evidence Hybrid RAG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
