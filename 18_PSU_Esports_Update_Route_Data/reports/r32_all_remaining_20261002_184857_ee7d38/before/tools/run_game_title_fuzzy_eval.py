from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.game_title_correction import detect_game_title_correction  # noqa: E402
from app.pipeline.structured_tools import _game_rows  # noqa: E402


REPORT_DIR = ROOT / "reports" / "game_title_fuzzy_eval"

ASCII_REPLACE = {
    "a": "s",
    "b": "v",
    "c": "x",
    "d": "s",
    "e": "r",
    "f": "d",
    "g": "f",
    "h": "j",
    "i": "o",
    "j": "h",
    "k": "l",
    "l": "k",
    "m": "n",
    "n": "m",
    "o": "p",
    "p": "o",
    "r": "t",
    "s": "a",
    "t": "r",
    "u": "i",
    "v": "b",
    "w": "q",
    "y": "u",
    "z": "x",
}

THAI_REPLACE = {
    "ิ": "ี",
    "ี": "ิ",
    "ุ": "ู",
    "ู": "ุ",
    "ต": "ด",
    "ด": "ต",
    "ท": "ต",
    "ร": "ล",
    "ล": "ร",
    "น": "ม",
    "ม": "น",
    "ค": "ต",
    "ว": "ฟ",
    "ฟ": "ว",
}


def _clean_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def _has_thai(value: str) -> bool:
    return bool(re.search(r"[\u0E00-\u0E7F]", value or ""))


def _compact_title(value: str) -> str:
    clean = _clean_space(value)
    clean = re.sub(r"\s+Standard Edition$", "", clean, flags=re.IGNORECASE)
    return clean


def _preferred_alias(row: dict[str, Any]) -> str:
    aliases = [str(item) for item in row.get("aliases") or [] if str(item).strip()]
    title = str(row.get("game") or "").strip()
    candidates = [_compact_title(alias) for alias in aliases] + [_compact_title(title)]

    thai_candidates = [item for item in candidates if _has_thai(item) and len(item) >= 5]
    if thai_candidates:
        return sorted(thai_candidates, key=len, reverse=True)[0]

    ascii_candidates = [
        item
        for item in candidates
        if re.search(r"[A-Za-z]", item) and len(re.sub(r"[^A-Za-z0-9]+", "", item)) >= 6
    ]
    if ascii_candidates:
        return sorted(ascii_candidates, key=lambda item: (len(item), item.lower()), reverse=True)[0]
    return title


def _make_typo(value: str) -> str:
    chars = list(value)
    if not chars:
        return value

    if _has_thai(value):
        for index in range(len(chars) - 1, -1, -1):
            replacement = THAI_REPLACE.get(chars[index])
            if replacement:
                chars[index] = replacement
                return "".join(chars)
        for index, ch in enumerate(chars):
            if "\u0E00" <= ch <= "\u0E7F":
                return "".join(chars[:index] + chars[index + 1:])

    for index in range(len(chars) - 2, 0, -1):
        lower = chars[index].lower()
        replacement = ASCII_REPLACE.get(lower)
        if replacement and replacement != lower:
            chars[index] = replacement.upper() if chars[index].isupper() else replacement
            return "".join(chars)

    compact_indexes = [index for index, ch in enumerate(chars) if ch.isalnum()]
    if len(compact_indexes) >= 4:
        drop_index = compact_indexes[len(compact_indexes) // 2]
        return "".join(chars[:drop_index] + chars[drop_index + 1:])
    return value


def _answer_passed(answer: str, expected_game: str, correction_game: str | None) -> bool:
    answer_lower = answer.lower()
    expected_lower = expected_game.lower()
    expected_base = re.sub(r"\s*\([^)]*\)\s*", " ", expected_lower)
    expected_base = re.sub(r"\s+", " ", expected_base).strip()
    if expected_lower in answer_lower:
        return True
    if expected_base and expected_base in answer_lower:
        return True
    if correction_game and correction_game.lower() == expected_lower:
        return True
    if correction_game and expected_base and correction_game.lower() == expected_base:
        return True
    family_prefix = expected_lower.split(":", 1)[0]
    return bool(family_prefix and family_prefix in answer_lower and "พบเกมที่เกี่ยวข้อง" in answer)


def _run_case(case_id: str, game: str, alias: str) -> dict[str, Any]:
    typo = _make_typo(alias)
    question = f"เกม {typo} มีข้อมูลไหม"
    started = time.perf_counter()
    correction = detect_game_title_correction(question)
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    elapsed = round(time.perf_counter() - started, 4)
    source_type = "RAG/curated"
    if "fast" in result.mode or "deterministic" in result.mode:
        source_type = "Fast/Rule"
    if "structured" in result.mode:
        source_type = "Structured Tool"
    return {
        "id": case_id,
        "expected_game": game,
        "source_alias": alias,
        "typo_alias": typo,
        "question": question,
        "passed": _answer_passed(result.answer, game, correction.game if correction else None),
        "correction_game": correction.game if correction else "",
        "correction_alias": correction.alias if correction else "",
        "correction_score": round(correction.score, 4) if correction else 0.0,
        "source_type": source_type,
        "mode": result.mode,
        "route": f"{result.route.category}/{result.route.intent}",
        "confidence": round(result.route.confidence, 4),
        "elapsed_sec": elapsed,
        "answer": result.answer,
    }


def run_eval(*, limit: int | None = None) -> dict[str, Any]:
    rows = list(_game_rows())
    cases: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for row in rows:
        game = str(row.get("game") or "").strip()
        if not game or game.lower() in seen:
            continue
        seen.add(game.lower())
        case_id = f"GTF-{len(cases) + 1:03d}"
        cases.append((case_id, game, _preferred_alias(row)))
        if limit and len(cases) >= limit:
            break

    results = [_run_case(case_id, game, alias) for case_id, game, alias in cases]
    passed = sum(1 for item in results if item["passed"])
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "results": results,
    }


def write_report(report: dict[str, Any]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"game_title_fuzzy_eval_{stamp}.json"
    csv_path = REPORT_DIR / f"game_title_fuzzy_eval_{stamp}.csv"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    fields = [
        "id",
        "expected_game",
        "source_alias",
        "typo_alias",
        "question",
        "passed",
        "correction_game",
        "correction_alias",
        "correction_score",
        "source_type",
        "mode",
        "route",
        "confidence",
        "elapsed_sec",
        "answer",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in report["results"]:
            writer.writerow({field: item.get(field, "") for field in fields})
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run game-title typo/fuzzy eval against every known game.")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of cases for quick debugging.")
    args = parser.parse_args()

    report = run_eval(limit=args.limit)
    json_path, csv_path = write_report(report)
    print(f"total={report['total']} passed={report['passed']} failed={report['failed']}")
    print(f"json={json_path}")
    print(f"csv={csv_path}")
    if report["failed"]:
        for item in report["results"]:
            if not item["passed"]:
                print(f"FAIL {item['id']} expected={item['expected_game']} correction={item['correction_game']} q={item['question']}")
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
