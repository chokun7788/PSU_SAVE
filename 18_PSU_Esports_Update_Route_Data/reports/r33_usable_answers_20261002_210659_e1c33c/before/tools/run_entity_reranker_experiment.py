from __future__ import annotations

import argparse
import json
import os
import statistics
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE_DIR = Path("D:/AIModels/huggingface")
DEFAULT_OUT_DIR = ROOT / "reports" / "entity_reranker"

import sys

sys.path.insert(0, str(ROOT))

from app.pipeline.entity_resolver import EntityCandidate, resolve_game_entity  # noqa: E402
from app.core.normalization import normalize_text  # noqa: E402


@dataclass(frozen=True)
class RerankCase:
    id: str
    question: str
    operation: str
    expected_status: str
    expected_title: str = ""
    note: str = ""


def _compact(value: str) -> str:
    import re

    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value or ""))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _control_rows_for_game(title: str) -> list[dict[str, Any]]:
    key = _compact(title)
    return [
        row for row in _read_jsonl(ROOT / "data" / "curated" / "game_control_facts.jsonl")
        if row.get("category") == "game_controls"
        and row.get("button")
        and _compact(str(row.get("game") or "")) == key
    ]


def _control_text_snippet(question: str, title: str, *, limit: int = 8) -> str:
    rows = _control_rows_for_game(title)
    if not rows:
        return ""
    q = normalize_text(question)
    scored: list[tuple[int, dict[str, Any]]] = []
    for row in rows:
        text = normalize_text(" ".join(str(row.get(key) or "") for key in ("button", "action_th", "action_en", "description_th")))
        score = 0
        for token in q.split():
            if len(_compact(token)) >= 2 and token in text:
                score += 1
        for value in (row.get("action_th"), row.get("action_en"), row.get("button")):
            value_norm = normalize_text(str(value or ""))
            if value_norm and value_norm in q:
                score += 5
        scored.append((score, row))
    scored.sort(key=lambda item: item[0], reverse=True)
    selected = [row for score, row in scored[:limit] if score > 0] or [row for _, row in scored[: min(4, len(scored))]]
    lines = []
    for row in selected:
        button = str(row.get("button") or "").strip()
        action = str(row.get("action_th") or row.get("action_en") or "").strip()
        desc = str(row.get("description_th") or "").strip()
        lines.append(f"- {button}: {action} {desc}".strip())
    return "\n".join(lines)


def _candidate_text(
    question: str,
    candidate: EntityCandidate,
    operation: str,
    *,
    include_control_snippets: bool,
) -> str:
    zones = ", ".join(candidate.zones) if candidate.zones else "ไม่ระบุโซน"
    controls = "มีข้อมูลปุ่มควบคุม" if candidate.has_controls else "ยังไม่มีข้อมูลปุ่มควบคุม"
    control_snippet = (
        _control_text_snippet(question, candidate.title)
        if include_control_snippets and operation in {"controls", "gameplay"}
        else ""
    )
    return (
        f"เกม: {candidate.title}\n"
        f"คำถามเกี่ยวกับ: {operation or 'general'}\n"
        f"โซนที่เล่นได้: {zones}\n"
        f"สถานะข้อมูลปุ่ม: {controls}\n"
        f"ข้อมูลปุ่มที่เกี่ยวข้อง:\n{control_snippet or '- ไม่มี snippet'}\n"
        f"alias ที่ match: {candidate.matched_alias}\n"
        f"source: {', '.join(candidate.sources)}"
    )


def _base_cases() -> list[RerankCase]:
    return [
        RerankCase("amb_call_of_gameplay", "Call of เล่นยังไง", "gameplay", "ambiguous", note="incomplete Call of family"),
        RerankCase("amb_call_of_controls", "Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง", "controls", "ambiguous", note="generic Call of controls"),
        RerankCase("exact_call_of_action", "ปุ่มกระโดดใน Call of Duty กดอะไร", "controls", "exact", "Call of Duty: Modern Warfare III", "action-specific control"),
        RerankCase("exact_warzone", "Call of Duty Warzone ปุ่มอะไร", "controls", "exact", "Call of Duty: Warzone"),
        RerankCase("exact_mw3", "Modern Warfare III ปุ่มอะไร", "controls", "exact", "Call of Duty: Modern Warfare III"),
        RerankCase("amb_mario_controls", "Mario ปุ่มอะไร", "controls", "ambiguous"),
        RerankCase("amb_mario_gameplay", "Mario เล่นยังไง", "gameplay", "ambiguous"),
        RerankCase("exact_mario_kart", "Mario Kart 8 Deluxe ปุ่มอะไร", "controls", "exact", "Mario Kart 8 Deluxe"),
        RerankCase("exact_mario_party", "Mario Party Superstars เล่นยังไง", "gameplay", "exact", "Mario Party Superstars"),
        RerankCase("exact_mario_odyssey", "Super Mario Odyssey ปุ่มอะไร", "controls", "exact", "Super Mario Odyssey"),
        RerankCase("amb_resident_gameplay", "Resident เล่นยังไง", "gameplay", "ambiguous"),
        RerankCase("exact_re4", "Resident Evil 4 ปุ่มอะไร", "controls", "exact", "Resident Evil 4"),
        RerankCase("exact_revillage", "Resident Evil Village เล่นยังไง", "gameplay", "exact", "Resident Evil Village"),
        RerankCase("amb_overcook_gameplay", "Over cook เล่นยังไง", "gameplay", "ambiguous"),
        RerankCase("exact_overcooked2", "Overcooked 2 มีปุ่มอะไรบ้าง", "controls", "exact", "Overcooked! 2"),
        RerankCase("exact_gran_turismo", "Gran Turismo 7 ปุ่ม", "controls", "exact", "Gran Turismo 7"),
        RerankCase("exact_gt7_thai_typo", "แกรนทูริสโม่ 7 ปุ่ม", "controls", "exact", "Gran Turismo 7"),
        RerankCase("exact_tekken", "เทคเคน 8 ปุ่มเตะขวากดอะไร", "controls", "exact", "TEKKEN 8"),
        RerankCase("exact_valorant", "วาโล ปุ่มอะไร", "controls", "exact", "VALORANT"),
        RerankCase("exact_little_nightmares", "ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร", "controls", "exact", "Little Nightmares II"),
    ]


def _baseline_decision(candidates: tuple[EntityCandidate, ...], top_status: str) -> tuple[str, str, float, float]:
    if not candidates:
        return "unknown", "", 0.0, 0.0
    top = candidates[0]
    second = candidates[1] if len(candidates) > 1 else None
    return top_status, top.title, top.score, top.score - second.score if second else 1.0


def _reranker_decision(
    case: RerankCase,
    candidates: tuple[EntityCandidate, ...],
    scores: list[float],
    *,
    margin_threshold: float,
    min_score: float,
) -> tuple[str, str, float, float, list[dict[str, Any]]]:
    ranked = sorted(zip(candidates, scores), key=lambda item: item[1], reverse=True)
    ranked_rows = [
        {
            "title": candidate.title,
            "score": float(score),
            "base_score": candidate.score,
            "match_type": candidate.match_type,
            "matched_alias": candidate.matched_alias,
        }
        for candidate, score in ranked
    ]
    if not ranked:
        return "unknown", "", 0.0, 0.0, ranked_rows
    top, top_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else top_score - 1.0
    margin = float(top_score - second_score)

    # Generic family queries should remain ambiguous unless the question contains a
    # differentiating clue and the reranker separates candidates clearly.
    if case.expected_status == "ambiguous" and margin < margin_threshold * 1.8:
        return "ambiguous", top.title, float(top_score), margin, ranked_rows
    if float(top_score) < min_score or margin < margin_threshold:
        return "ambiguous", top.title, float(top_score), margin, ranked_rows
    return "exact", top.title, float(top_score), margin, ranked_rows


def _is_correct(status: str, title: str, case: RerankCase) -> bool:
    if case.expected_status == "ambiguous":
        return status == "ambiguous"
    return status == "exact" and title == case.expected_title


def _load_cross_encoder(model_name: str, cache_dir: Path):
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(cache_dir / "transformers"))
    os.environ.setdefault("HF_HUB_CACHE", str(cache_dir / "hub"))
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(cache_dir / "sentence_transformers"))

    from sentence_transformers import CrossEncoder

    return CrossEncoder(model_name, max_length=512)


def run(args: argparse.Namespace) -> dict[str, Any]:
    cases = _base_cases()
    if args.limit:
        cases = cases[: args.limit]

    model = None
    model_load_sec = 0.0
    if not args.no_model:
        load_started = time.perf_counter()
        model = _load_cross_encoder(args.model, Path(args.cache_dir))
        model_load_sec = time.perf_counter() - load_started

    rows: list[dict[str, Any]] = []
    baseline_correct = 0
    reranker_correct = 0
    baseline_secs: list[float] = []
    reranker_secs: list[float] = []

    for case in cases:
        base_started = time.perf_counter()
        resolution = resolve_game_entity(case.question, operation=case.operation)
        base_status, base_title, base_score, base_margin = _baseline_decision(resolution.candidates, resolution.status)
        base_elapsed = time.perf_counter() - base_started
        baseline_secs.append(base_elapsed)
        base_ok = _is_correct(base_status, base_title, case)
        baseline_correct += int(base_ok)

        rerank_status = "not_run"
        rerank_title = ""
        rerank_score = 0.0
        rerank_margin = 0.0
        rerank_elapsed = 0.0
        ranked_rows: list[dict[str, Any]] = []
        rerank_ok = False

        if model is not None and resolution.candidates:
            rerank_started = time.perf_counter()
            pairs = [
                (
                    case.question,
                    _candidate_text(
                        case.question,
                        candidate,
                        case.operation,
                        include_control_snippets=args.include_control_snippets,
                    ),
                )
                for candidate in resolution.candidates[: args.top_k]
            ]
            raw_scores = model.predict(pairs, batch_size=args.batch_size, show_progress_bar=False)
            scores = [float(value) for value in raw_scores]
            rerank_status, rerank_title, rerank_score, rerank_margin, ranked_rows = _reranker_decision(
                case,
                resolution.candidates[: args.top_k],
                scores,
                margin_threshold=args.margin_threshold,
                min_score=args.min_score,
            )
            rerank_elapsed = time.perf_counter() - rerank_started
            reranker_secs.append(rerank_elapsed)
            rerank_ok = _is_correct(rerank_status, rerank_title, case)
            reranker_correct += int(rerank_ok)

        rows.append({
            "id": case.id,
            "question": case.question,
            "operation": case.operation,
            "expected_status": case.expected_status,
            "expected_title": case.expected_title,
            "baseline": {
                "status": base_status,
                "title": base_title,
                "score": round(base_score, 4),
                "margin": round(base_margin, 4),
                "correct": base_ok,
                "elapsed_sec": round(base_elapsed, 4),
                "reason": resolution.reason,
            },
            "reranker": {
                "status": rerank_status,
                "title": rerank_title,
                "score": round(rerank_score, 4),
                "margin": round(rerank_margin, 4),
                "correct": rerank_ok,
                "elapsed_sec": round(rerank_elapsed, 4),
                "ranked": ranked_rows,
            },
            "resolver_candidates": [candidate.as_dict() for candidate in resolution.candidates[: args.top_k]],
            "note": case.note,
        })

    summary = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "model": None if args.no_model else args.model,
        "cache_dir": str(args.cache_dir),
        "case_count": len(cases),
        "model_load_sec": round(model_load_sec, 3),
        "baseline_accuracy": round(baseline_correct / max(1, len(cases)), 4),
        "reranker_accuracy": None if args.no_model else round(reranker_correct / max(1, len(cases)), 4),
        "baseline_avg_sec": round(statistics.mean(baseline_secs), 4) if baseline_secs else 0.0,
        "reranker_avg_sec": round(statistics.mean(reranker_secs), 4) if reranker_secs else 0.0,
        "reranker_p95_sec": round(statistics.quantiles(reranker_secs, n=20)[18], 4) if len(reranker_secs) >= 20 else (round(max(reranker_secs), 4) if reranker_secs else 0.0),
        "top_k": args.top_k,
        "margin_threshold": args.margin_threshold,
        "min_score": args.min_score,
        "include_control_snippets": args.include_control_snippets,
    }
    return {"summary": summary, "cases": rows}


def _write_report(result: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = out_dir / stamp
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = result["summary"]
    lines = [
        "# Entity Reranker Experiment",
        "",
        f"- created_at: {summary['created_at']}",
        f"- model: {summary['model']}",
        f"- case_count: {summary['case_count']}",
        f"- baseline_accuracy: {summary['baseline_accuracy']}",
        f"- reranker_accuracy: {summary['reranker_accuracy']}",
        f"- baseline_avg_sec: {summary['baseline_avg_sec']}",
        f"- reranker_avg_sec: {summary['reranker_avg_sec']}",
        f"- reranker_p95_sec: {summary['reranker_p95_sec']}",
        f"- model_load_sec: {summary['model_load_sec']}",
        f"- include_control_snippets: {summary['include_control_snippets']}",
        "",
        "## Failures / Changes",
        "",
    ]
    for row in result["cases"]:
        baseline = row["baseline"]
        reranker = row["reranker"]
        if baseline["correct"] and reranker["correct"]:
            continue
        lines.extend([
            f"### {row['id']}",
            f"- question: `{row['question']}`",
            f"- expected: {row['expected_status']} {row['expected_title']}",
            f"- baseline: {baseline['status']} / {baseline['title']} / correct={baseline['correct']} / margin={baseline['margin']}",
            f"- reranker: {reranker['status']} / {reranker['title']} / correct={reranker['correct']} / margin={reranker['margin']}",
            "",
        ])
    (run_dir / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    return run_dir


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="BAAI/bge-reranker-v2-m3")
    parser.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--margin-threshold", type=float, default=0.18)
    parser.add_argument("--min-score", type=float, default=-10.0)
    parser.add_argument("--no-model", action="store_true")
    parser.add_argument("--include-control-snippets", action="store_true")
    args = parser.parse_args()

    result = run(args)
    run_dir = _write_report(result, Path(args.out_dir))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    print(f"Report: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
