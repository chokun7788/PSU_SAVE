from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.shadow_critic import analyze_failures, review_case  # noqa: E402


DEFAULT_INPUT = ROOT / "data" / "eval" / "real_usage_golden_v1.jsonl"
DEFAULT_OUTPUT_ROOT = ROOT / "reports" / "shadow_critic"


def _read_cases(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(text)
        return value if isinstance(value, list) else [value]
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    columns = [
        "case_id", "question", "category", "group", "verdict", "score", "severity",
        "labels", "reason", "suggested_fix", "critic_status", "critic_used_llm",
        "pipeline_mode", "pipeline_route", "pipeline_intent", "pipeline_elapsed_sec",
        "pipeline_validation_ok", "llm_call_count", "answer",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["labels"] = ",".join(row.get("labels", []))
            writer.writerow(output)


def _write_report(path: Path, summary: dict[str, Any], rows: list[dict[str, Any]], *, input_path: Path, args: argparse.Namespace) -> None:
    failures = [row for row in rows if row.get("verdict") != "pass"]
    lines = [
        "# LLM Shadow Critic + Failure Analyst Report",
        "",
        f"- Generated: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Input: `{input_path}`",
        f"- Cases: `{summary['total_cases']}`",
        f"- Chatbot LLM enabled: `{args.chatbot_llm}`",
        f"- Shadow Critic LLM enabled: `{args.critic_llm}`",
        f"- Shadow Critic model: `{args.model}`",
        "",
        "## Summary",
        "",
        f"- Pass rate: **{summary['pass_rate']:.2%}**",
        f"- Hard failure rate: **{summary['hard_failure_rate']:.2%}**",
        f"- Needs-review rate: **{summary['review_rate']:.2%}**",
        f"- Verdicts: `{json.dumps(summary['verdicts'], ensure_ascii=False)}`",
        f"- Average latency: `{summary['latency']['avg_sec']:.4f}s`",
        f"- P95 latency: `{summary['latency']['p95_sec']:.4f}s`",
        f"- Max latency: `{summary['latency']['max_sec']:.4f}s`",
        f"- Pipeline LLM calls: `{summary['llm_call_count_total']}`",
        f"- Cases reviewed by Critic LLM: `{summary['critic_llm_cases']}`",
        "",
        "## Failure Labels",
        "",
    ]
    if summary["labels"]:
        lines.extend(f"- `{label}`: {count}" for label, count in sorted(summary["labels"].items(), key=lambda item: (-item[1], item[0])))
    else:
        lines.append("- ไม่พบ failure label จากชุดตรวจนี้")
    lines.extend(["", "## Failure Cases (สูงสุด 30 ข้อ)", ""])
    if not failures:
        lines.append("ไม่พบเคสที่ต้องตรวจเพิ่ม")
    else:
        for row in failures[:30]:
            lines.extend([
                f"### `{row.get('case_id')}` - {row.get('question')}",
                f"- Verdict: `{row.get('verdict')}` / Severity: `{row.get('severity')}`",
                f"- Labels: `{', '.join(row.get('labels', []))}`",
                f"- Route: `{row.get('pipeline_route')}` | Mode: `{row.get('pipeline_mode')}`",
                f"- Reason: {row.get('reason')}",
                f"- Suggested fix: {row.get('suggested_fix') or '-'}",
                f"- Answer: {str(row.get('answer') or '').replace(chr(10), ' ')[:500]}",
                "",
            ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PSU chatbot cases and review them with a shadow critic")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--chatbot-llm", action="store_true", help="allow LLM inside the chatbot pipeline")
    parser.add_argument("--critic-llm", action="store_true", help="call local LLM as a second-opinion critic")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--model", default=os.getenv("PSU_SHADOW_CRITIC_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b"))
    parser.add_argument("--critic-timeout", type=float, default=8.0)
    parser.add_argument("--global-timeout", type=float, default=20.0)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    cases = _read_cases(input_path)
    if args.limit > 0:
        cases = cases[:args.limit]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = args.output_dir or DEFAULT_OUTPUT_ROOT / f"{timestamp}_{input_path.stem}"
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for index, case in enumerate(cases, 1):
        question = str(case.get("question") or "").strip()
        if not question:
            continue
        result = answer_question_pipeline_debug(
            question,
            experimental_allow_llm=args.chatbot_llm,
            experimental_rag_fallback=args.rag_fallback,
            global_timeout_sec=args.global_timeout,
        )
        critic = review_case(
            case,
            result,
            use_llm=args.critic_llm,
            model=args.model,
            timeout_sec=args.critic_timeout,
        )
        row = {
            **{key: case.get(key) for key in ("id", "group", "category", "expected_category", "expected_intent", "expected_mode_prefix")},
            **critic.as_dict(),
            "case_id": critic.case_id or f"case_{index:04d}",
            "category": case.get("group") or case.get("category") or case.get("expected_category") or "unknown",
            "answer": result.answer,
            "source_ids": [str(hit.get("id") or "") for hit in result.hits if isinstance(hit, dict)],
        }
        rows.append(row)
        if index % 25 == 0 or index == len(cases):
            print(f"processed={index}/{len(cases)}")

    summary = analyze_failures(rows)
    summary.update({
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input": str(input_path),
        "output_dir": str(output_dir),
        "chatbot_llm": args.chatbot_llm,
        "critic_llm": args.critic_llm,
        "critic_model": args.model,
    })
    _write_jsonl(output_dir / "results.jsonl", rows)
    _write_csv(output_dir / "results.csv", rows)
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_report(output_dir / "REPORT.md", summary, rows, input_path=input_path, args=args)
    print(f"output_dir={output_dir}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
