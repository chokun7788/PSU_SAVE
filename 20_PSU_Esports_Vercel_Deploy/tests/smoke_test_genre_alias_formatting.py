from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.normalization import normalize_text  # noqa: E402
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.preprocess import preprocess_input  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item not in text]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item in text]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def main() -> int:
    variants = preprocess_input("เกมทนิฟยอดนิยมมีอะไรบ้าง").query_variants
    if len(variants) < 2 or not any("moba" in variant for variant in variants):
        raise AssertionError(f"query variants should include a moba-friendly variant\n{variants}")

    variants = preprocess_input("เกม F,[hk ยอดนิยมมีอะไรบ้าง").query_variants
    if len(variants) < 2 or not any("moba" in normalize_text(variant) for variant in variants):
        raise AssertionError(f"query variants should include a moba-friendly variant\n{variants}")

    moba = answer_question_pipeline_debug("เกมโมบ้ายอดนิยมมีอะไรบ้าง").answer
    assert_contains(
        moba,
        [
            "MOBA",
            "• League of Legends",
            "• Dota 2",
            "• Mobile Legends: Bang Bang",
            "แหล่งข้อมูล:",
        ],
        "moba popular games formatting",
    )
    assert_not_contains(moba, ["ได้แก่ League of Legends, Dota 2"], "moba old inline format")

    typo = answer_question_pipeline_debug("เกมทนิฟยอดนิยมมีอะไรบ้าง").answer
    assert_contains(typo, ["MOBA", "• League of Legends", "• Arena of Valor"], "keyboard typo moba route")

    popular = answer_question_pipeline_debug("เกมยอดนิยมแต่ละหมวดมีอะไรบ้าง").answer
    assert_contains(
        popular,
        [
            "MOBA",
            "FPS",
            "Battle Royale",
            "Fighting",
            "Sports",
            "Racing",
            "Digital Card",
            "Real-Time Strategy (RTS)",
            "• VALORANT",
            "• StarCraft II",
        ],
        "popular games by genre formatting",
    )
    assert_not_contains(popular, ["- MOBA:"], "popular games old inline format")

    print("GENRE ALIAS FORMATTING SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
