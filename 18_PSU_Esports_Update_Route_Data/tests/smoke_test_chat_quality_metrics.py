from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.report_chat_quality_metrics import summarize  # noqa: E402


def main() -> int:
    records = [
        {
            "wall_sec": 0.4,
            "decision_artifact": {
                "production_metrics": {
                    "outcome": "answered",
                    "quality_gate_status": "pass",
                    "repair_attempted": False,
                    "repair_recovered": False,
                    "llm_call_count": 0,
                    "requires_shadow_review": False,
                    "shadow_review_reasons": [],
                }
            },
        },
        {
            "wall_sec": 1.2,
            "decision_artifact": {
                "production_metrics": {
                    "outcome": "answered",
                    "quality_gate_status": "pass",
                    "repair_attempted": True,
                    "repair_recovered": True,
                    "llm_call_count": 0,
                    "requires_shadow_review": True,
                    "shadow_review_reasons": ["repair_attempted"],
                }
            },
        },
    ]
    summary = summarize(records, max_reject_rate=0.0, max_timeout_rate=0.01, max_p95_sec=8.0)
    assert summary["records_with_metrics"] == 2
    assert summary["repair_attempted"] == 1
    assert summary["repair_recovered"] == 1
    assert summary["shadow_review_reasons"] == {"repair_attempted": 1}
    assert summary["release_gate_passed"] is True
    print("CHAT QUALITY METRICS SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
