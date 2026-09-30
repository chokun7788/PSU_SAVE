from __future__ import annotations

import json
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.keyboard_input_anomaly import (  # noqa: E402
    KeyboardInputAnomalyDetector,
    translate_keyboard_layout,
)
from app.core.normalization import KEYBOARD_EN_TO_THAI, KEYBOARD_THAI_TO_EN  # noqa: E402


def load_clean_questions() -> list[str]:
    path = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
    questions: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                questions.append(str(json.loads(line)["question"]))
    return questions


def assert_greater(left: float, right: float, label: str) -> None:
    if left <= right:
        raise AssertionError(f"{label}: expected {left:.6f} > {right:.6f}")


def main() -> int:
    detector = KeyboardInputAnomalyDetector().fit(load_clean_questions())

    wrong_thai_keys = translate_keyboard_layout("\u0e40\u0e25\u0e48\u0e19", KEYBOARD_THAI_TO_EN)
    if wrong_thai_keys != "g]jo":
        raise AssertionError(f"unexpected Kedmanee mapping: {wrong_thai_keys!r}")
    wrong_thai = detector.analyze(wrong_thai_keys)
    valid_mixed = detector.analyze("VR \u0e23\u0e32\u0e04\u0e32\u0e40\u0e17\u0e48\u0e32\u0e44\u0e2b\u0e23\u0e48")
    assert_greater(wrong_thai.layout_score, valid_mixed.layout_score, "Thai intended / English active")

    english_question = "what games are available"
    wrong_english_keys = translate_keyboard_layout(english_question, KEYBOARD_EN_TO_THAI)
    wrong_english = detector.analyze(wrong_english_keys)
    valid_thai = detector.analyze("\u0e21\u0e35\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07")
    assert_greater(wrong_english.layout_score, valid_thai.layout_score, "English intended / Thai active")

    accidental_repeat = detector.analyze("PC \u0e23\u0e32\u0e04\u0e04\u0e32\u0e40\u0e17\u0e48\u0e32\u0e44\u0e2b\u0e23\u0e48")
    lexical_repeat = detector.analyze("TEKKEN 8 \u0e40\u0e25\u0e48\u0e19\u0e17\u0e35\u0e48\u0e44\u0e2b\u0e19")
    expressive_repeat = detector.analyze("\u0e40\u0e25\u0e48\u0e19\u0e44\u0e14\u0e49\u0e44\u0e2b\u0e21\u0e21\u0e21")
    assert_greater(accidental_repeat.repeat_score, lexical_repeat.repeat_score, "accidental vs lexical repeat")
    assert_greater(accidental_repeat.repeat_score, expressive_repeat.repeat_score, "accidental vs expressive repeat")

    protected = detector.analyze("https://esports.phuket.psu.ac.th")
    if protected.layout_score >= wrong_thai.layout_score:
        raise AssertionError("URL protection did not reduce the layout score")

    print("KEYBOARD INPUT ANOMALY SMOKE TEST OK")
    print(
        f"scores layout_wrong={wrong_thai.layout_score:.4f} layout_valid={valid_mixed.layout_score:.4f} "
        f"repeat_typo={accidental_repeat.repeat_score:.4f} repeat_lexical={lexical_repeat.repeat_score:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
