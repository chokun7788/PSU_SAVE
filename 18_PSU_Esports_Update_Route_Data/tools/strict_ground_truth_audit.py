from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"

sys.path.insert(0, str(ROOT))
from app.core.normalization import normalize_text  # noqa: E402


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def direct_answer(answer: str) -> str:
    text = str(answer or "").strip()
    text = text.split("\n\n", 1)[0].strip()
    for prefix in ("คำตอบ:", "Answer:"):
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix):].strip()
            break
    return text


def source_haystack(row: dict[str, Any]) -> str:
    parts: list[str] = []
    parts.extend(as_list(row.get("retrieved_ids")))
    # Some evaluators only persist source URLs inside the answer text, not in hits.
    parts.append(str(row.get("answer", "")))
    for source in as_list(row.get("expected_source_keywords")):
        # Keep expected source out of the actual haystack. This branch only normalizes type.
        _ = source
    for hit in row.get("hits", []) if isinstance(row.get("hits"), list) else []:
        parts.append(str(hit.get("id", "")))
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        parts.extend(str(metadata.get(key, "")) for key in ("source_url", "category", "title", "source_ids"))
    for source in row.get("sources", []) if isinstance(row.get("sources"), list) else []:
        if isinstance(source, dict):
            parts.extend(str(source.get(key, "")) for key in ("id", "url", "category", "source_ids"))
    return normalize_text(" ".join(parts))


def contains_all(text: str, keywords: list[str]) -> tuple[bool, list[str]]:
    haystack = normalize_text(text)
    missing = [keyword for keyword in keywords if normalize_text(keyword) not in haystack]
    return not missing, missing


def infer_expected_route(gt: dict[str, Any], result: dict[str, Any]) -> str | None:
    explicit_route = str(gt.get("expected_route_category") or "").strip()
    category = str(gt.get("category") or result.get("category") or "")
    question = normalize_text(str(gt.get("question") or result.get("question") or ""))
    expected_sources = " ".join(as_list(gt.get("expected_source_keywords") or result.get("expected_source_keywords")))

    schedule_terms = (
        "เปิด", "ปิด", "เวลา", "กี่โมง", "service hours", "hours", "open", "close",
        "morning", "afternoon", "วันนี้", "พรุ่งนี้", "วันจันทร์", "จันทร์", "monday",
        "อังคาร", "tuesday", "พุธ", "wednesday", "พฤหัส", "thursday",
        "ศุกร์", "friday", "หยุด", "holiday", "รอบเช้า", "ช่วงเช้า", "รอบบ่าย",
        "ช่วงบ่าย", "maintenance", "hardware inspection", "cleaning", "09", "12", "13", "16",
        "session time",
    )
    reservation_terms = (
        "จอง", "booking", "book ", "เช็คอิน", "เชคอิน", "checkin", "check in",
        "แก้", "ยกเลิก", "ชำระ", "จ่าย", "โอน", "สลิป", "ก่อนเวลา",
    )
    if category == "reservation" and any(term in question for term in reservation_terms):
        return "reservation"
    if category == "reservation" and any(term in question for term in schedule_terms):
        return "schedule"

    if explicit_route:
        return explicit_route

    if category == "competition_rules" or "competition_rules_" in expected_sources:
        return "competition_rules"
    if category == "service_fee":
        return "service_fee"
    if category == "no_answer":
        return "no_answer"
    if category == "games":
        return "games"
    if category == "equipment":
        return "equipment"
    if category == "contact":
        return "contact"
    if category in {"events_news", "knowledge", "overview", "rules", "penalty"}:
        return category
    if category == "reservation":
        return "reservation"
    return None


def audit_one(result: dict[str, Any], gt: dict[str, Any] | None = None) -> dict[str, Any]:
    gt = gt or result
    issues: list[str] = []
    severity = "pass"

    def add(issue: str, level: str = "major") -> None:
        nonlocal severity
        issues.append(issue)
        order = {"pass": 0, "minor": 1, "major": 2}
        if order[level] > order[severity]:
            severity = level

    answer = str(result.get("answer", ""))
    direct = direct_answer(answer)
    route = str(result.get("route_category", ""))
    mode = str(result.get("mode", ""))
    verdict = str(result.get("verdict", ""))
    expected_keywords = as_list(gt.get("expected_keywords") or result.get("expected_keywords"))
    expected_sources = as_list(gt.get("expected_source_keywords") or result.get("expected_source_keywords"))
    expected_mode_prefix = str(gt.get("expected_mode_prefix") or "").strip()
    expected_route = infer_expected_route(gt, result)
    answer_says_no_data = "ไม่พบข้อมูล" in answer or "ยังไม่พบข้อมูล" in answer

    if verdict and verdict != "PASS":
        add(f"auto evaluator เดิมให้ {verdict}", "major")

    route_is_covered_by_mode = bool(expected_route and expected_route in mode)
    no_answer_is_explicit = expected_route == "no_answer" and answer_says_no_data
    mixed_answer_covers_expected = False
    if expected_route == "games" and route == "schedule" and expected_keywords:
        mixed_answer_covers_expected = contains_all(direct, expected_keywords)[0]
    if expected_route and route != expected_route and not route_is_covered_by_mode and not no_answer_is_explicit and not mixed_answer_covers_expected:
        add(f"route ผิด: ควรเป็น `{expected_route}` แต่ได้ `{route}`", "major")

    if expected_mode_prefix and not mode.startswith(expected_mode_prefix):
        add(f"mode ผิด: ควรขึ้นต้น `{expected_mode_prefix}` แต่ได้ `{mode}`", "major")

    if route == "general" and expected_route not in {None, "general", "no_answer"}:
        add("route เป็น general ทั้งที่ Ground Truth มีหมวดชัดเจน", "major")

    if expected_sources:
        source_text = source_haystack(result)
        source_category = str(gt.get("category") or result.get("category") or "")
        missing_sources = []
        for source in expected_sources:
            normalized_source = normalize_text(source)
            if normalized_source in source_text:
                continue
            if normalized_source == "reservation" and source_category == "reservation" and "esports.computing.psu.ac.th" in source_text:
                continue
            missing_sources.append(source)
        if missing_sources:
            add(f"source ไม่ตรงแบบ strict: ไม่พบ {missing_sources} ใน retrieved/source ids", "major")

    if expected_keywords:
        # Keyword in whole answer is weak. Direct answer is stricter and catches many false PASS cases.
        direct_ok, direct_missing = contains_all(direct, expected_keywords)
        whole_ok, whole_missing = contains_all(answer, expected_keywords)
        if not whole_ok:
            add(f"ไม่พบ expected keyword ในคำตอบรวม: {whole_missing}", "major")
        elif not direct_ok:
            add(f"expected keyword อยู่ในคำตอบรวม แต่ไม่อยู่ในคำตอบหลัก/บรรทัดแรก: {direct_missing}", "minor")

    category = str(gt.get("category") or result.get("category") or "")
    if answer_says_no_data and category not in {"no_answer", "unknown"}:
        add("ตอบว่าไม่พบข้อมูล ทั้งที่ Ground Truth คาดว่าควรตอบได้", "major")

    q = normalize_text(str(gt.get("question") or result.get("question") or ""))
    if ("ต่างกัน" in q or "ต่างกันเท่า" in q) and not normalize_text(direct).startswith("ต่างกัน"):
        add("คำถามถามส่วนต่าง แต่คำตอบหลักไม่ได้ขึ้นต้นด้วยส่วนต่าง", "minor")

    if ("ราคา" in q or "กี่บาท" in q or "เท่าไหร่" in q) and category == "service_fee":
        first = normalize_text(direct.splitlines()[0] if direct.splitlines() else direct)
        if "บาท" not in first and "ไม่พบราคา" not in first:
            add("คำถามราคา แต่บรรทัดแรกยังไม่ขึ้นราคาหรือบอกไม่พบราคา", "minor")

    if expected_route == "competition_rules" and route in {"games", "service_fee", "schedule", "knowledge"}:
        add(f"คำถามกติกาการแข่งขันหลุดไป route `{route}` ซึ่งเสี่ยงตอบคนละเรื่อง", "major")

    return {
        "id": result.get("id") or gt.get("id"),
        "question": gt.get("question") or result.get("question"),
        "category": category,
        "expected_route": expected_route,
        "actual_route": route,
        "mode": mode,
        "auto_verdict": verdict,
        "strict_decision": severity,
        "strict_ok": severity == "pass",
        "issues": issues or ["ไม่พบปัญหาจาก strict heuristic"],
        "direct_answer": direct,
        "answer": answer,
        "expected_keywords": expected_keywords,
        "expected_source_keywords": expected_sources,
        "latency_sec": result.get("latency_sec"),
    }


def build_markdown(rows: list[dict[str, Any]], results_path: Path, ground_truth_path: Path | None, out_jsonl: Path) -> str:
    counts = Counter(row["strict_decision"] for row in rows)
    by_category: dict[str, Counter] = defaultdict(Counter)
    for row in rows:
        by_category[str(row.get("category", "-"))][row["strict_decision"]] += 1

    lines = [
        "# Strict Ground Truth Audit",
        "",
        f"Created: {datetime.now().isoformat(timespec='seconds')}",
        f"Results: `{results_path}`",
        f"Ground truth: `{ground_truth_path or '-'}`",
        f"Audit JSONL: `{out_jsonl}`",
        "",
        "## Summary",
        "",
        f"- Total: {len(rows)}",
        f"- pass: {counts.get('pass', 0)}",
        f"- minor: {counts.get('minor', 0)}",
        f"- major: {counts.get('major', 0)}",
        "",
        "## By Category",
        "",
        "| Category | pass | minor | major |",
        "|---|---:|---:|---:|",
    ]
    for category, counter in sorted(by_category.items()):
        lines.append(f"| {category} | {counter.get('pass', 0)} | {counter.get('minor', 0)} | {counter.get('major', 0)} |")

    attention = [row for row in rows if row["strict_decision"] != "pass"]
    lines.extend(["", "## Items To Review", ""])
    if not attention:
        lines.append("No suspicious items found by strict heuristic.")
    else:
        for row in attention:
            lines.extend([
                f"### {row['id']} - {row['strict_decision']}",
                "",
                f"- Category: `{row['category']}`",
                f"- Expected route: `{row['expected_route']}`",
                f"- Actual route: `{row['actual_route']}`",
                f"- Mode: `{row['mode']}`",
                f"- Auto verdict: `{row['auto_verdict']}`",
                f"- Question: {row['question']}",
                "- Direct answer:",
                "",
                "```text",
                row["direct_answer"],
                "```",
                "- Issues:",
            ])
            for issue in row["issues"]:
                lines.append(f"  - {issue}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--ground-truth", default=None)
    parser.add_argument("--label", default="strict_audit")
    args = parser.parse_args()

    results_path = Path(args.results)
    gt_path = Path(args.ground_truth) if args.ground_truth else None
    results = load_jsonl(results_path)
    gt_map = {row.get("id"): row for row in load_jsonl(gt_path)} if gt_path else {}

    rows = [audit_one(result, gt_map.get(result.get("id"))) for result in results]
    out_jsonl = REPORT_DIR / f"strict_ground_truth_audit_{args.label}.jsonl"
    out_md = REPORT_DIR / f"strict_ground_truth_audit_{args.label}.md"
    write_jsonl(out_jsonl, rows)
    out_md.write_text(build_markdown(rows, results_path, gt_path, out_jsonl), encoding="utf-8", newline="\n")

    counts = Counter(row["strict_decision"] for row in rows)
    print(f"Strict audit rows: {len(rows)}")
    print(dict(counts))
    print(out_md)
    print(out_jsonl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
