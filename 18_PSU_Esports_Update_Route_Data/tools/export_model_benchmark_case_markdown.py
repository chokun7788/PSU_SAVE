from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"Expected object at {path}:{line_no}")
            rows.append(row)
    return rows


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def _safe_name(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return safe.strip("._") or "case"


def _text_block(value: Any) -> str:
    text = "" if value is None else str(value)
    return f"````text\n{text}\n````"


def _json_block(value: Any) -> str:
    return "````json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n````"


def _table_text(value: Any, limit: int = 120) -> str:
    if value is None:
        text = ""
    elif isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    else:
        text = str(value)
    text = text.replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    if len(text) > limit:
        return text[: max(0, limit - 3)] + "..."
    return text


def _list_text(value: Any) -> str:
    if value in (None, "", []):
        return "-"
    if isinstance(value, list):
        return ", ".join(_table_text(item, 300) for item in value) or "-"
    return _table_text(value, 500) or "-"


def _result_status(result: dict[str, Any]) -> str:
    judge = result.get("judge") or {}
    return "PASS" if judge.get("passed") else "FAIL"


def _trace_elapsed_ms(item: dict[str, Any]) -> Any:
    metadata = item.get("metadata") or {}
    for key in ("elapsed_ms", "llm_elapsed_ms", "total_elapsed_ms"):
        if metadata.get(key) is not None:
            return metadata[key]
    return ""


def _collect_source_references(result: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()
    source_keys = {
        "source",
        "sources",
        "source_id",
        "source_ids",
        "source_url",
        "source_urls",
        "url",
        "urls",
        "evidence_id",
        "evidence_ids",
        "document_id",
        "document_ids",
        "fact_id",
        "fact_ids",
    }

    def add(value: Any) -> None:
        if isinstance(value, (str, int, float, bool)):
            text = str(value).strip()
            if text and text not in seen:
                seen.add(text)
                refs.append(text)
        elif isinstance(value, list):
            for item in value:
                add(item)
        elif isinstance(value, dict):
            for key in ("id", "source_id", "url", "title", "name"):
                if key in value:
                    add(value[key])

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                if str(key).lower() in source_keys:
                    add(item)
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(result.get("trace") or [])
    for url in re.findall(r"https?://[^\s)\]}>]+", str(result.get("answer") or "")):
        add(url.rstrip(".,;"))
    return refs


def _trace_table(trace: list[dict[str, Any]]) -> str:
    lines = [
        "| # | Stage | Decision | Confidence | Elapsed ms | Detail |",
        "|---:|---|---|---:|---:|---|",
    ]
    for index, item in enumerate(trace, 1):
        confidence = item.get("confidence")
        confidence_text = "" if confidence is None else str(confidence)
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    _table_text(item.get("stage"), 80),
                    _table_text(item.get("decision"), 120),
                    confidence_text,
                    _table_text(_trace_elapsed_ms(item), 40),
                    _table_text(item.get("detail"), 180),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def _criteria_lines(case: dict[str, Any]) -> list[str]:
    return [
        f"- Expected category: `{_table_text(case.get('expected_category'), 500) or '-'}`",
        f"- Expected mode prefix: `{_table_text(case.get('expected_mode_prefix'), 500) or '-'}`",
        f"- Must contain: `{_list_text(case.get('must_contain'))}`",
        f"- Must contain any: `{_list_text(case.get('must_contain_any'))}`",
        f"- Must not contain: `{_list_text(case.get('must_not_contain'))}`",
        f"- LLM required: `{bool(case.get('llm_required'))}`",
        f"- Dataset source: `{_table_text(case.get('source'), 500) or '-'}`",
        f"- Dataset note: `{_table_text(case.get('note'), 500) or '-'}`",
    ]


def _detail_markdown(
    case: dict[str, Any],
    result: dict[str, Any],
    run_label: str,
    summary: dict[str, Any],
    paired_rel: str,
    index_rel: str,
) -> str:
    judge = result.get("judge") or {}
    trace = result.get("trace") or []
    sources = _collect_source_references(result)
    status = _result_status(result)
    case_id = str(result.get("id") or case.get("id") or "")
    lines = [
        f"# {case_id} - {run_label}",
        "",
        f"[กลับไป Index]({index_rel}) | [เทียบสองโหมด]({paired_rel})",
        "",
        "## สถานะ",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Result | **{status}** |",
        f"| Score | `{judge.get('score', '')}` |",
        f"| Run label | `{run_label}` |",
        f"| Model | `{summary.get('model') or 'No-LLM'}` |",
        f"| Group | `{result.get('group', case.get('group', ''))}` |",
        f"| Quality bucket | `{result.get('quality_bucket', case.get('quality_bucket', ''))}` |",
        f"| Risk | `{result.get('risk', case.get('risk', ''))}` |",
        "",
        "## โจทย์",
        "",
        _text_block(result.get("question", case.get("question", ""))),
        "",
        "## คำตอบที่ระบบตอบ",
        "",
        _text_block(result.get("answer", "")),
        "",
        "## เกณฑ์ของโจทย์",
        "",
        *_criteria_lines(case),
        "",
        "## Route และ Validation",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Mode | `{_table_text(result.get('mode'), 500) or '-'}` |",
        f"| Route category | `{_table_text(result.get('route_category'), 500) or '-'}` |",
        f"| Route intent | `{_table_text(result.get('route_intent'), 500) or '-'}` |",
        f"| Confidence | `{result.get('confidence', '')}` |",
        f"| Validation OK | `{result.get('validation_ok', '')}` |",
        f"| Validation errors | `{_list_text(result.get('validation_errors'))}` |",
        f"| Validation warnings | `{_list_text(result.get('validation_warnings'))}` |",
        f"| Judge errors | `{_list_text(judge.get('errors'))}` |",
        f"| Judge warnings | `{_list_text(judge.get('warnings'))}` |",
        "",
        "## เวลาและการใช้ LLM",
        "",
        "| Field | Value |",
        "|---|---:|",
        f"| Wall time (sec) | `{result.get('wall_sec', '')}` |",
        f"| Pipeline elapsed (sec) | `{result.get('elapsed_sec', '')}` |",
        f"| LLM calls | `{result.get('llm_call_count', 0)}` |",
        f"| LLM elapsed total (ms) | `{result.get('llm_elapsed_ms_total', 0)}` |",
        f"| LLM kinds | `{_list_text(result.get('llm_kinds'))}` |",
        "",
        "## Source / Evidence Reference",
        "",
    ]
    if sources:
        lines.extend(f"- `{_table_text(source, 1000)}`" for source in sources)
    else:
        lines.append("- ไม่พบ source reference แบบ explicit ใน output/trace ของเคสนี้")
    lines.extend(
        [
            "",
            "## Process Trace",
            "",
            _trace_table(trace),
            "",
            "<details>",
            "<summary>Raw evaluation case</summary>",
            "",
            _json_block(case),
            "",
            "</details>",
            "",
            "<details>",
            "<summary>Raw benchmark result และ trace field ที่ output เก็บไว้</summary>",
            "",
            _json_block(result),
            "",
            "</details>",
            "",
        ]
    )
    return "\n".join(lines)


def _paired_markdown(
    case: dict[str, Any],
    entries: list[tuple[str, dict[str, Any], str]],
    index_rel: str,
) -> str:
    case_id = str(case.get("id") or "")
    lines = [
        f"# {case_id}",
        "",
        f"[กลับไป Index]({index_rel})",
        "",
        "## โจทย์",
        "",
        _text_block(case.get("question", "")),
        "",
        "## เกณฑ์ของโจทย์",
        "",
        *_criteria_lines(case),
        "",
    ]
    for run_label, result, detail_rel in entries:
        judge = result.get("judge") or {}
        lines.extend(
            [
                f"## คำตอบ - {run_label}",
                "",
                f"ผล: **{_result_status(result)}** | Score: `{judge.get('score', '')}` | "
                f"Wall: `{result.get('wall_sec', '')}s` | LLM calls: `{result.get('llm_call_count', 0)}` | "
                f"Mode: `{_table_text(result.get('mode'), 500)}`",
                "",
                _text_block(result.get("answer", "")),
                "",
                f"Judge errors: `{_list_text(judge.get('errors'))}`",
                "",
                f"[เปิด log รายละเอียดและ trace จาก raw output]({detail_rel})",
                "",
            ]
        )
    if len(entries) == 2:
        first = entries[0][1]
        second = entries[1][1]
        lines.extend(
            [
                "## เปรียบเทียบย่อ",
                "",
                f"- คำตอบเหมือนกันทุกตัวอักษร: `{first.get('answer') == second.get('answer')}`",
                f"- Wall time ต่างกัน (โหมดที่ 2 - โหมดที่ 1): `{round(float(second.get('wall_sec') or 0) - float(first.get('wall_sec') or 0), 4)}s`",
                f"- Score ต่างกัน (โหมดที่ 2 - โหมดที่ 1): `{round(float((second.get('judge') or {}).get('score') or 0) - float((first.get('judge') or {}).get('score') or 0), 2)}`",
                "",
            ]
        )
    lines.extend(
        [
            "<details>",
            "<summary>Raw evaluation case</summary>",
            "",
            _json_block(case),
            "",
            "</details>",
            "",
        ]
    )
    return "\n".join(lines)


def _run_index_markdown(run_label: str, summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    lines = [
        f"# Case Index - {run_label}",
        "",
        f"- Total: `{len(rows)}`",
        f"- Passed: `{summary.get('passed', '')}`",
        f"- Pass rate: `{summary.get('pass_rate', '')}%`",
        f"- Average wall: `{summary.get('avg_wall_sec', '')}s`",
        f"- P95 wall: `{summary.get('p95_wall_sec', '')}s`",
        f"- Max wall: `{summary.get('max_wall_sec', '')}s`",
        f"- LLM calls: `{summary.get('llm_call_total', 0)}`",
        "",
        "| # | ID | Result | Score | Group | Mode | Wall s | LLM calls | โจทย์ |",
        "|---:|---|---|---:|---|---|---:|---:|---|",
    ]
    for index, row in enumerate(rows, 1):
        case_id = str(row.get("id") or f"case_{index}")
        judge = row.get("judge") or {}
        lines.append(
            f"| {index} | [{_table_text(case_id, 100)}]({_safe_name(case_id)}.md) | "
            f"{_result_status(row)} | {judge.get('score', '')} | {_table_text(row.get('group'), 60)} | "
            f"{_table_text(row.get('mode'), 100)} | {row.get('wall_sec', '')} | "
            f"{row.get('llm_call_count', 0)} | {_table_text(row.get('question'), 120)} |"
        )
    return "\n".join(lines) + "\n"


def _root_index_markdown(
    cases: list[dict[str, Any]],
    run_order: list[str],
    results_by_run: dict[str, dict[str, dict[str, Any]]],
) -> str:
    lines = [
        "# Benchmark Case Markdown Index",
        "",
        "ไฟล์ใน `paired/` แสดงโจทย์เดียวกันพร้อมคำตอบจากทุกโหมด ส่วน `details/` เก็บ log และ trace field จาก raw output แยกตามโหมด",
        "",
        "| # | ID | Group | โจทย์ | " + " | ".join(f"{run}: result / wall / calls" for run in run_order) + " |",
        "|---:|---|---|---|" + "---|" * len(run_order),
    ]
    for index, case in enumerate(cases, 1):
        case_id = str(case.get("id") or f"case_{index}")
        run_cells: list[str] = []
        for run_label in run_order:
            result = results_by_run[run_label][case_id]
            detail = f"details/{run_label}/{_safe_name(case_id)}.md"
            run_cells.append(
                f"[{_result_status(result)}]({detail}) / {result.get('wall_sec', '')}s / {result.get('llm_call_count', 0)}"
            )
        lines.append(
            f"| {index} | [{_table_text(case_id, 100)}](paired/{_safe_name(case_id)}.md) | "
            f"{_table_text(case.get('group'), 60)} | {_table_text(case.get('question'), 140)} | "
            + " | ".join(run_cells)
            + " |"
        )
    return "\n".join(lines) + "\n"


def _discover_runs(benchmark_root: Path) -> list[Path]:
    run_dirs = [
        path
        for path in benchmark_root.iterdir()
        if path.is_dir() and (path / "results.json").is_file() and (path / "summary.json").is_file()
    ]
    run_dirs.sort(key=lambda path: (path.name != "no_llm", path.name.lower()))
    if not run_dirs:
        raise ValueError(f"No benchmark run directories found under {benchmark_root}")
    return run_dirs


def main() -> int:
    parser = argparse.ArgumentParser(description="Export one Markdown log per benchmark case and run mode.")
    parser.add_argument("--benchmark-root", required=True)
    parser.add_argument("--cases", default=str(DEFAULT_CASES))
    parser.add_argument("--output-dir", default="")
    args = parser.parse_args()

    benchmark_root = Path(args.benchmark_root).resolve()
    cases_path = Path(args.cases).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else benchmark_root / "case_markdown"
    details_dir = output_dir / "details"
    paired_dir = output_dir / "paired"
    output_dir.mkdir(parents=True, exist_ok=True)
    details_dir.mkdir(parents=True, exist_ok=True)
    paired_dir.mkdir(parents=True, exist_ok=True)

    cases = _read_jsonl(cases_path)
    case_ids = [str(case.get("id") or "") for case in cases]
    if not case_ids or any(not case_id for case_id in case_ids):
        raise ValueError("Every evaluation case must have a non-empty id")
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("Evaluation case ids are not unique")
    cases_by_id = {str(case["id"]): case for case in cases}

    run_dirs = _discover_runs(benchmark_root)
    run_order: list[str] = []
    summaries: dict[str, dict[str, Any]] = {}
    rows_by_run: dict[str, list[dict[str, Any]]] = {}
    results_by_run: dict[str, dict[str, dict[str, Any]]] = {}
    input_hashes: dict[str, dict[str, str]] = {}

    for run_dir in run_dirs:
        run_label = run_dir.name
        summary = _read_json(run_dir / "summary.json")
        rows = _read_json(run_dir / "results.json")
        if not isinstance(summary, dict) or not isinstance(rows, list):
            raise ValueError(f"Invalid benchmark output in {run_dir}")
        result_ids = [str(row.get("id") or "") for row in rows]
        if len(result_ids) != len(set(result_ids)):
            raise ValueError(f"Duplicate result ids in {run_dir}")
        missing = sorted(set(case_ids) - set(result_ids))
        extra = sorted(set(result_ids) - set(case_ids))
        if missing or extra:
            raise ValueError(f"Case/result mismatch for {run_label}: missing={missing[:5]} extra={extra[:5]}")
        if len(rows) != len(cases):
            raise ValueError(f"Expected {len(cases)} rows for {run_label}, found {len(rows)}")

        run_order.append(run_label)
        summaries[run_label] = summary
        ordered = sorted(rows, key=lambda row: case_ids.index(str(row.get("id") or "")))
        rows_by_run[run_label] = ordered
        results_by_run[run_label] = {str(row["id"]): row for row in rows}
        input_hashes[run_label] = {
            "results_json_sha256": _sha256(run_dir / "results.json"),
            "summary_json_sha256": _sha256(run_dir / "summary.json"),
        }

    for run_label in run_order:
        run_output = details_dir / run_label
        run_output.mkdir(parents=True, exist_ok=True)
        rows = rows_by_run[run_label]
        for row in rows:
            case_id = str(row["id"])
            paired_rel = f"../../paired/{_safe_name(case_id)}.md"
            detail = _detail_markdown(
                cases_by_id[case_id],
                row,
                run_label,
                summaries[run_label],
                paired_rel,
                "INDEX.md",
            )
            (run_output / f"{_safe_name(case_id)}.md").write_text(detail, encoding="utf-8", newline="\n")
        (run_output / "INDEX.md").write_text(
            _run_index_markdown(run_label, summaries[run_label], rows),
            encoding="utf-8",
            newline="\n",
        )

    for case in cases:
        case_id = str(case["id"])
        entries: list[tuple[str, dict[str, Any], str]] = []
        for run_label in run_order:
            entries.append(
                (
                    run_label,
                    results_by_run[run_label][case_id],
                    f"../details/{run_label}/{_safe_name(case_id)}.md",
                )
            )
        paired = _paired_markdown(case, entries, "../INDEX.md")
        (paired_dir / f"{_safe_name(case_id)}.md").write_text(paired, encoding="utf-8", newline="\n")

    root_index = _root_index_markdown(cases, run_order, results_by_run)
    (output_dir / "INDEX.md").write_text(root_index, encoding="utf-8", newline="\n")

    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    manifest = {
        "generated_at": generated_at,
        "benchmark_root": str(benchmark_root),
        "output_dir": str(output_dir),
        "cases_file": str(cases_path),
        "cases_sha256": _sha256(cases_path),
        "case_count": len(cases),
        "run_count": len(run_order),
        "run_order": run_order,
        "detail_markdown_count": len(cases) * len(run_order),
        "paired_markdown_count": len(cases),
        "total_case_markdown_count": len(cases) * len(run_order) + len(cases),
        "runs": {
            run_label: {
                "record_count": len(rows_by_run[run_label]),
                "summary": summaries[run_label],
                **input_hashes[run_label],
            }
            for run_label in run_order
        },
    }
    (output_dir / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    readme_lines = [
        "# Benchmark Markdown Export",
        "",
        f"สร้างเมื่อ: `{generated_at}`",
        "",
        f"- Evaluation cases: `{len(cases)}`",
        f"- Run modes: `{len(run_order)}` ({', '.join(run_order)})",
        f"- Detail Markdown: `{manifest['detail_markdown_count']}` ไฟล์",
        f"- Paired Markdown: `{manifest['paired_markdown_count']}` ไฟล์",
        f"- Case Markdown รวม: `{manifest['total_case_markdown_count']}` ไฟล์",
        f"- Case bank SHA256: `{manifest['cases_sha256']}`",
        "",
        "## ทางเข้าหลัก",
        "",
        "- [Index ทุกโจทย์และทุกโหมด](INDEX.md)",
        "- `paired/`: หนึ่งไฟล์ต่อโจทย์ มีคำตอบทุกโหมดในหน้าเดียว",
        "- `details/<run>/`: หนึ่งไฟล์ต่อโจทย์ต่อโหมด มี raw record และ trace ทุก entry ที่ benchmark output เก็บไว้",
        "- ข้อจำกัด: pipeline output ปัจจุบันจำกัด trace ไว้สูงสุด 12 entries ต่อเคส จึงไม่ใช่ event ledger ครบทุก process ภายใน request",
        "- [Manifest JSON](MANIFEST.json)",
        "",
        "## สรุปแต่ละโหมด",
        "",
        "| Run | Total | Passed | Pass rate | Avg s | P95 s | Max s | LLM calls |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for run_label in run_order:
        summary = summaries[run_label]
        readme_lines.append(
            f"| [{run_label}](details/{run_label}/INDEX.md) | {summary.get('total', '')} | "
            f"{summary.get('passed', '')} | {summary.get('pass_rate', '')}% | "
            f"{summary.get('avg_wall_sec', '')} | {summary.get('p95_wall_sec', '')} | "
            f"{summary.get('max_wall_sec', '')} | {summary.get('llm_call_total', 0)} |"
        )
    (output_dir / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8", newline="\n")

    print(f"Benchmark root: {benchmark_root}")
    print(f"Output: {output_dir}")
    print(f"Cases: {len(cases)}")
    print(f"Runs: {len(run_order)} ({', '.join(run_order)})")
    print(f"Detail Markdown: {manifest['detail_markdown_count']}")
    print(f"Paired Markdown: {manifest['paired_markdown_count']}")
    print(f"Total case Markdown: {manifest['total_case_markdown_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
