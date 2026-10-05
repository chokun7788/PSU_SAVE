"""Read frozen r20 results and replay residual failures with full decision traces.

Analysis only: does not edit runtime, GT, owner data, or prior logs.
Outputs use exclusive creation and the frozen source manifest must still match.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
OLD = ROOT / "reports/reliability_flow_20261001"
NEW = ROOT / "reports/r20_deep_failure_analysis_20261001"

CLEAN_PROBES = {
    "MASTER-GT-TH-00032", "MASTER-GT-TH-00024", "MASTER-GT-TH-02083",
    "MASTER-GT-TH-04611", "MASTER-GT-TH-03829", "MASTER-GT-TH-01667",
    "MASTER-GT-TH-02611", "MASTER-GT-TH-01622", "MASTER-GT-TH-04896",
    "MASTER-GT-TH-02213", "MASTER-GT-TH-04785", "MASTER-GT-TH-02476",
    "MASTER-GT-TH-03957", "MASTER-GT-TH-04944",
    "MASTER-GT-EN-04874", "MASTER-GT-EN-04820", "MASTER-GT-EN-00531",
    "MASTER-GT-EN-01405", "MASTER-GT-EN-04469", "MASTER-GT-EN-03401",
    "MASTER-GT-EN-01715", "MASTER-GT-EN-02394", "MASTER-GT-EN-04891",
    "MASTER-GT-EN-00143",
}


def read_rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def assert_frozen_source():
    manifest = json.loads((OLD / "final_gate_manifest.json").read_text(encoding="utf-8-sig"))
    for row in manifest["files"]:
        if hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() != row["sha256"]:
            raise RuntimeError(f"Source no longer matches frozen r20: {row['path']}")
    return manifest


def statistics(rows):
    failed = [row for row in rows if not row["noisy"]["passed"]]
    fields = ["route_ok", "status_ok", "content_ok", "latency_ok"]
    positive = lambda row: any((row.get("answer_contract") or {}).get(key) for key in ("must_contain", "must_contain_any", "must_contain_all_groups"))
    return {
        "count": len(rows), "noisy_failed": len(failed),
        "pair_outcomes": dict(Counter(f"clean={r['clean']['passed']},noisy={r['noisy']['passed']}" for r in rows)),
        "failure_gate_combinations": dict(Counter(",".join(key[:-3] for key in fields if not r["noisy"][key]) for r in failed)),
        "failure_domains": dict(Counter(r["domain"] for r in failed)),
        "failure_modes": dict(Counter(r["noisy"]["mode"] for r in failed)),
        "failure_expected_status": dict(Counter(r["expected_answer_status"] for r in failed)),
        "failure_review_status": dict(Counter(r["review_status"] for r in failed)),
        "positive_contract_count_legacy": sum(positive(r) for r in rows),
        "failure_localization_domains": dict(Counter(r["domain"] for r in failed if r["noisy"]["mode"] == "pipeline:missing_english_localization")),
        "localization_pair_outcomes": dict(Counter(f"clean={r['clean']['passed']},noisy={r['noisy']['passed']}" for r in failed if r["noisy"]["mode"] == "pipeline:missing_english_localization")),
        "notes": "Gate symptoms are not semantic error counts. Replay traces support case-specific causality; no owner approval or live oracle is inferred.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=("th", "en"))
    args = parser.parse_args()
    manifest = assert_frozen_source()
    NEW.mkdir(parents=True, exist_ok=True)
    if not args.locale:
        rows = [r for locale in ("th", "en") for r in read_rows(OLD / f"paired_{locale}_r20_gate.jsonl")]
        output = NEW / "failure_statistics.json"
        summary = {"all": statistics(rows), "by_locale": {locale: statistics([r for r in rows if r["locale"] == locale]) for locale in ("th", "en")}, "source_manifest": manifest}
        with output.open("x", encoding="utf-8") as stream:
            json.dump(summary, stream, ensure_ascii=False, indent=2)
        print(json.dumps(summary["all"], ensure_ascii=False))
        return

    os.environ.update({"PSU_PERFORMANCE_TRACE": "0", "PSU_LIVE_BOOKING_ENABLED": "0"})
    from app.pipeline.engine import answer_question_pipeline_debug
    rows = read_rows(OLD / f"paired_{args.locale}_r20_gate.jsonl")
    output = NEW / f"traces_{args.locale}.jsonl"
    selected = [(row, "noisy") for row in rows if not row["noisy"]["passed"]]
    selected += [(row, "clean") for row in rows if row["id"] in CLEAN_PROBES]
    same_mode = same_answer = 0
    with output.open("x", encoding="utf-8") as stream:
        for index, (row, variant) in enumerate(selected, 1):
            question = row[f"{variant}_question"]
            result = answer_question_pipeline_debug(question, locale=row["locale"], experimental_allow_llm=False, experimental_rag_fallback=False, global_timeout_sec=20.0)
            replay = asdict(result)
            replay.pop("language", None)
            mode_same = row[variant]["mode"] == result.mode
            answer_same = row[variant]["answer"] == result.answer
            same_mode += mode_same
            same_answer += answer_same
            record = {
                "id": row["id"], "locale": row["locale"], "domain": row["domain"], "variant": variant,
                "question": question, "expected_route_categories": row["expected_route_categories"],
                "expected_answer_status": row["expected_answer_status"], "answer_contract": row["answer_contract"],
                "review_status": row["review_status"], "original_evaluation": row[variant],
                "mode_same_as_final_gate": mode_same, "answer_same_as_final_gate": answer_same,
                "replay": replay,
            }
            stream.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
            stream.flush()
            if index % 25 == 0 or index == len(selected):
                print(args.locale, index, "/", len(selected), "same_mode", same_mode, "same_answer", same_answer, flush=True)
    assert_frozen_source()
    summary = {"locale": args.locale, "replay_count": len(selected), "failed_noisy_count": sum(v == "noisy" for _, v in selected), "clean_probe_count": sum(v == "clean" for _, v in selected), "same_mode_count": same_mode, "same_answer_count": same_answer, "config": {"allow_llm": False, "rag_fallback": False, "live_booking_enabled": False, "performance_trace": False}, "source_matches_frozen_gate": True}
    with output.with_suffix(".summary.json").open("x", encoding="utf-8") as stream:
        json.dump(summary, stream, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
