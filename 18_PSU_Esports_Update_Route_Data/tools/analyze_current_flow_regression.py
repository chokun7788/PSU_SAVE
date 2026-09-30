"""Offline comparison and per-case diagnostic inventory. Never rewrites raw logs."""
from __future__ import annotations

import argparse
import dataclasses
import json
import math
import os
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
FAQ_BASE = ROOT / "reports/model_benchmark/20260831_current_flow_full1600_llm/llm_scb10x_typhoon2.5-qwen3-4b/results.jsonl"
KB_BASE = ROOT / "reports/keyboard_input_pipeline_eval/20260831_current_flow_guard_llm500/results.jsonl"


def read_rows(path, partial=False):
    rows = []
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    for i, line in enumerate(lines):
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            if not partial or i != len(lines) - 1:
                raise
    return rows


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def latency(rows):
    vals = sorted(float(r.get("wall_sec", 0)) for r in rows)
    return {"n": len(vals), "mean": statistics.mean(vals) if vals else None,
            "median": statistics.median(vals) if vals else None,
            "p95_nearest_rank": vals[math.ceil(.95 * len(vals)) - 1] if vals else None,
            "max_observed": max(vals, default=None), "over_10s": sum(v > 10 for v in vals),
            "right_censored": sum(bool(r.get("right_censored")) for r in rows)}


def frac(n, d):
    return round(100 * n / d, 2) if d else None


def confusion(rows, flag, truth):
    counts = Counter({k: 0 for k in ("TP", "FP", "FN", "TN")})
    unknown = 0
    for r in rows:
        if not r.get("guard"):
            unknown += 1
            continue
        yes = flag in r.get("guard", {}).get("flags", [])
        expected = bool(r["case"].get(truth))
        counts[("T" if yes == expected else "F") + ("P" if yes else "N")] += 1
    return {**counts, "unobserved": unknown, "precision_pct": frac(counts["TP"], counts["TP"] + counts["FP"]),
            "recall_pct": frac(counts["TP"], counts["TP"] + counts["FN"])}


def diagnose(row, baseline):
    suite = row["suite"]
    judge = row.get("legacy_judge", {})
    blocked = bool(row.get("guard", {}).get("should_retype"))
    mode = row.get("mode", "")
    tags, evidence, remedies = [], [], []
    errors = judge.get("errors", [])
    if row["status"] != "completed":
        tags.append("infrastructure_or_watchdog_failure")
        evidence.append(row.get("error", row.get("exception", row["status"])))
        remedies.append("Inspect worker stack; bound the blocking stage and transport. The harness watchdog is not a production fix.")
    if row.get("wall_sec", 0) > 10:
        tags.append("latency_over_10s")
        remedies.append("Bound stage work and network reads; reserve finalizer time; prove cancellation and degraded response under load.")
    if suite == "keyboard":
        flags = set(row.get("guard", {}).get("flags", []))
        expected = set(row["case"].get("expected_flags", []))
        observed = bool(row.get("guard"))
        missing = expected - flags if observed else set()
        extra = flags - expected if observed else set()
        if not observed:
            tags.append("guard_not_observed")
        if missing:
            tags.append("detector_false_negative")
            evidence.append("Missing flags: " + ", ".join(sorted(missing)))
            remedies.append("Review short/mixed-script spans, protected tokens and repeated-mark features on a separate held-out set.")
        if extra:
            tags.append("detector_false_positive")
            evidence.append("Extra flags: " + ", ".join(sorted(extra)))
            remedies.append("Review valid Thai combining marks and English names; calibrate thresholds without training on this test set.")
        if observed and bool(row["case"].get("should_block_answer")) != blocked:
            tags.append("legacy_block_policy_disagreement")
            if expected == {"repeated_character_typo"} and blocked:
                evidence.append("Current ask_retype policy blocks repeats; original dataset labels them warn/continue.")
            else:
                evidence.append("Block decision differs from original label; inspect detection vs policy separately.")
        if blocked and not expected:
            tags.append("normal_input_wrongly_blocked")
        if blocked and expected and not missing and not extra:
            tags.append("expected_retype_outcome")
        if not blocked and not row["case"].get("source_case"):
            tags.append("unmapped_answer_needs_manual_review")
            remedies.append("Add independent answer gold; no source case means answer correctness is unscored.")
    elif blocked:
        tags.append("faq_guard_block_requires_review")
        evidence.append(row.get("guard_message", ""))
        remedies.append("Inspect the original FAQ input before treating the flag as an error; restore valid domain vocabulary coverage.")
    if suite == "faq" and mode.startswith("canonical_"):
        tags.append("pilot_catalog_ownership_intercept")
        evidence.append("Legacy question was intercepted by isolated pilot before legacy routing.")
        remedies.append("Build a complete union catalog with coverage metadata before enabling catalog ownership; do not answer totals from partial data.")
    semantic = [t for t in row.get("trace", []) if t.get("stage") == "semantic_route_refiner" and t.get("decision") == "route_refined"]
    if errors and not blocked and not mode.startswith("canonical_"):
        if semantic and any(e.startswith(("category_mismatch", "missing")) for e in errors):
            tags.append("semantic_route_or_scope_mismatch")
            for t in semantic:
                m = t.get("metadata", {})
                evidence.append(f"{t.get('detail')}; top={m.get('top_id')}; score={m.get('top_score')}; margin={m.get('margin')}")
            remedies.append("Enforce requested entity and facet before route locking; similarity and a single-hit margin do not establish relevance.")
        if any(e.startswith("mode_mismatch") for e in errors):
            tags.append("route_contract_mismatch")
        if any(e.startswith(("missing", "forbidden")) for e in errors):
            tags.append("answer_text_contract_mismatch")
            remedies.append("Check required facts and source support manually; exact substring failures may be paraphrases, omissions, or wrong answers.")
        if any("llm_required" in e for e in errors):
            tags.append("model_availability_or_model_contract")
        if any(e.startswith("category_mismatch") for e in errors):
            tags.append("category_contract_mismatch")
    if row.get("validation", {}).get("ok") is False:
        tags.append("runtime_validation_rejected")
    if not tags:
        tags.append("automated_contract_pass" if judge.get("passed") else "unscored_or_review")
    relevant_gold = row["case"].get("source_case") if suite == "keyboard" else row["case"]
    relevant_gold = relevant_gold or {}
    return {"id": row["id"], "suite": suite, "question": row["question"], "answer": row.get("answer", ""),
            "mode": mode, "status": row["status"], "wall_sec": row.get("wall_sec"), "tags": tags,
            "legacy_errors": errors, "evidence": evidence, "suggested_next_steps": list(dict.fromkeys(remedies)),
            "method": "deterministic trace inspection + existing label/substring contracts; not semantic fact verification",
            "expected_contract": {k: v for k, v in relevant_gold.items() if k.startswith(("expected", "must_"))},
            "expected_response_policy": "ask user to retype; do not translate or auto-correct" if suite == "keyboard" and row["case"].get("expected_flags") else "answer the requested target/facet with verified sources",
            "baseline_answer_not_gold": baseline.get("answer") if baseline else None,
            "baseline_judge": (baseline.get("judge") or baseline.get("source_judge")) if baseline else None,
            "needs_manual_review": any(t not in {"automated_contract_pass", "expected_retype_outcome", "legacy_block_policy_disagreement"} for t in tags)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--allow-partial", action="store_true")
    parser.add_argument("--guard-diagnostics", action="store_true", help="Replay detector only after run; never regenerate chatbot answers")
    args = parser.parse_args()
    run = args.run_dir.resolve()
    rows = read_rows(run / "results.jsonl", args.allow_partial)
    if len({r["id"] for r in rows}) != len(rows):
        raise SystemExit("Duplicate case IDs in log")
    if not args.allow_partial:
        summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
        if summary["completed"] != summary["expected"] or len(rows) != summary["expected"]:
            raise SystemExit("Incomplete run; pass --allow-partial only for provisional analysis")
    out = run / ("analysis_partial" if args.allow_partial else "analysis")
    out.mkdir(exist_ok=True)
    base_faq, base_kb = read_rows(FAQ_BASE), read_rows(KB_BASE)
    base = {r["id"]: r for r in base_faq + base_kb}
    faq = [r for r in rows if r["suite"] == "faq"]
    kb = [r for r in rows if r["suite"] == "keyboard"]
    canonical = [r for r in rows if r["suite"] == "canonical"]
    diag = [diagnose(r, base.get(r["id"])) for r in rows]
    with (out / "per_case_analysis.jsonl").open("w", encoding="utf-8") as log:
        for d in diag:
            log.write(json.dumps(d, ensure_ascii=False) + "\n")
    changes = Counter()
    change_ids = defaultdict(list)
    for r in faq:
        previous = base.get(r["id"], {}).get("judge", {}).get("passed")
        now = bool(r.get("legacy_judge", {}).get("passed"))
        label = "both_pass" if previous and now else "regression" if previous else "improvement" if now else "both_fail"
        changes[label] += 1
        change_ids[label].append(r["id"])
    stage_values = defaultdict(list)
    for r in rows:
        per_request = defaultdict(float)
        if r.get("guard"):
            per_request["input_quality_guard"] = float(r["guard"].get("guard_elapsed_ms", 0))
        if r.get("pipeline_executed") and r.get("context_sec") is not None:
            per_request["session_context_resolver"] = float(r["context_sec"]) * 1000
        for t in r.get("stage_timings", []):
            per_request[t["process"]] += float(t.get("elapsed_ms", 0))
        for t in r.get("trace", []):
            if t.get("stage") in {"knowledge_embedding", "knowledge_retrieval", "knowledge_llm_order"}:
                per_request[t["stage"]] += float(t.get("metadata", {}).get("elapsed_ms", 0))
        for stage, ms in per_request.items():
            stage_values[stage].append(ms)
    stages = sorted([{"stage": s, "requests_with_stage": len(v), "observed_total_sec": sum(v) / 1000,
                      "avg_per_request_ms": statistics.mean(v), "p95_ms": sorted(v)[math.ceil(.95 * len(v)) - 1],
                      "max_ms": max(v)} for s, v in stage_values.items()], key=lambda s: -s["observed_total_sec"])
    mapped = [r for r in kb if r.get("pipeline_executed") and r["case"].get("source_case")]
    comparable = [r for r in mapped if base.get(r["id"], {}).get("pipeline_executed")]
    families = []
    for family in sorted({r["case"]["anomaly_family"] for r in kb}):
        group = [r for r in kb if r["case"]["anomaly_family"] == family]
        families.append({"family": family, "n": len(group),
                         "blocked": sum(bool(r.get("guard", {}).get("should_retype")) for r in group),
                         "flag_set_exact": sum(bool(r.get("guard")) and set(r.get("guard", {}).get("flags", [])) == set(r["case"].get("expected_flags", [])) for r in group),
                         "guard_unobserved": sum(not r.get("guard") for r in group),
                         "latency": latency(group)})
    mode_groups = []
    for mode in sorted({r.get("mode", r["status"]) for r in faq}):
        group = [r for r in faq if r.get("mode", r["status"]) == mode]
        mode_groups.append({"mode": mode, "n": len(group), "legacy_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in group), "latency": latency(group)})
    faq_groups = []
    for name in sorted({r["case"].get("group", "unknown") for r in faq}):
        group = [r for r in faq if r["case"].get("group", "unknown") == name]
        faq_groups.append({"group": name, "n": len(group), "old_passed": sum(bool(base.get(r["id"], {}).get("judge", {}).get("passed")) for r in group),
                           "new_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in group)})
    calls = [c for r in rows for c in r.get("llm_calls", [])]
    call_groups = defaultdict(list)
    for c in calls:
        call_groups[c.get("llm_kind", c.get("stage", "unknown"))].append(c)
    model_stats = [{"kind": kind, "logged_entries_including_skips": len(group),
                    "nonempty_responses": sum(int(c.get("llm_response_chars", 0)) > 0 for c in group),
                    "elapsed_logged_sec": sum(float(c.get("llm_elapsed_ms", 0)) for c in group) / 1000,
                    "load_logged_sec": sum(float(c.get("llm_load_duration_ms", 0)) for c in group) / 1000,
                    "decisions": dict(Counter(c.get("decision", "unknown") for c in group))} for kind, group in call_groups.items()]
    canonical_events = [t for r in canonical for t in r.get("canonical_llm_events", [])]
    stats = {"partial": args.allow_partial, "total": len(rows),
        "faq": {"n": len(faq), "legacy_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in faq),
                "strict_passed": sum(bool(r.get("strict_passed")) for r in faq), "latency": latency(faq),
                "llm_required_cases": sum(bool(r["case"].get("llm_required")) for r in faq),
                "without_positive_text_assertions": sum(not r["case"].get("must_contain") and not r["case"].get("must_contain_any") for r in faq),
                "baseline_latency": latency([r for r in base_faq if r["id"] in {x["id"] for x in faq}]),
                "changes": dict(changes), "change_ids": dict(change_ids),
                "guard_blocked": sum(bool(r.get("guard", {}).get("should_retype")) for r in faq),
                "guard_blocked_ids": [r["id"] for r in faq if r.get("guard", {}).get("should_retype")],
                "pilot_intercept_ids": [r["id"] for r in faq if r.get("mode", "").startswith("canonical_")],
                "groups": faq_groups,
                "validation_not_ok": sum(r.get("validation", {}).get("ok") is False for r in faq),
                "modes": mode_groups},
        "keyboard": {"n": len(kb), "layout": confusion(kb, "keyboard_layout_mismatch", "should_detect_keyboard_layout"),
                     "repeat": confusion(kb, "repeated_character_typo", "should_detect_repeated_character"),
                     "families": families, "latency_all": latency(kb),
                     "blocked": sum(bool(r.get("guard", {}).get("should_retype")) for r in kb),
                     "mapped_allowed": len(mapped), "mapped_allowed_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in mapped),
                     "comparable_allowed": len(comparable),
                     "comparable_old_passed": sum(bool(base[r["id"]].get("source_judge", {}).get("passed")) for r in comparable),
                     "comparable_new_passed": sum(bool(r.get("legacy_judge", {}).get("passed")) for r in comparable),
                     "allowed_latency": latency([r for r in kb if r.get("pipeline_executed")]),
                     "normal_wrongly_blocked_ids": [r["id"] for r in kb if not r["case"].get("expected_flags") and r.get("guard", {}).get("should_retype")]},
        "canonical": {"n": len(canonical), "strict_passed": sum(bool(r.get("strict_passed")) for r in canonical),
                      "latency": latency(canonical), "llm_attempts": sum(bool(t.get("metadata", {}).get("model_info", {}).get("attempted")) for t in canonical_events),
                      "llm_order_accepted": sum(t.get("decision") == "accepted" for t in canonical_events)},
        "diagnostic_tags_nonexclusive": dict(Counter(tag for d in diag for tag in d["tags"])),
        "stage_timings_nonadditive": stages, "llm": model_stats,
        "slowest": [{"id": r["id"], "question": r["question"], "wall_sec": r["wall_sec"], "status": r["status"],
                     "mode": r.get("mode"), "largest_stage": max(r.get("stage_timings", []), key=lambda t: t.get("elapsed_ms", 0), default=None)}
                    for r in sorted(rows, key=lambda r: -r.get("wall_sec", 0))[:30]]}
    write_json(out / "metrics.json", stats)
    if not args.allow_partial:
        initial = run / "summary_initial.json"
        if not initial.exists():
            initial.write_bytes((run / "summary.json").read_bytes())
        audited = json.loads(initial.read_text(encoding="utf-8"))
        kb_summary = audited["suites"]["keyboard"]
        kb_summary["keyboard_layout_mismatch"] = stats["keyboard"]["layout"]
        kb_summary["repeated_character_typo"] = stats["keyboard"]["repeat"]
        kb_summary["guard_observed"] = sum(bool(r.get("guard")) for r in kb)
        kb_summary["guard_unobserved"] = len(kb) - kb_summary["guard_observed"]
        kb_summary["legacy_block_agreement"] = sum(bool(r.get("guard")) and bool(r["guard"].get("should_retype")) == bool(r["case"].get("should_block_answer")) for r in kb)
        kb_summary["source_contract_denominator"] = len(mapped)
        kb_summary["text_contract_passed_mapped_allowed"] = sum(bool(r.get("text_contract_passed")) for r in mapped)
        audited["audit_note"] = ("Guard counts exclude an unobserved result instead of treating it as a true negative. "
                                 "Original derived counters retained in summary_initial.json. Raw results.jsonl is unchanged. "
                                 "Keyboard answer quality uses mapped_allowed denominator, not all 500 cases.")
        write_json(run / "summary.json", audited)
    if args.guard_diagnostics:
        if args.allow_partial:
            raise SystemExit("Guard replay must not compete with a running timed benchmark")
        from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
        os.environ.update(PSU_INPUT_QUALITY_GUARD_MODE="enforce", PSU_INPUT_QUALITY_REPEAT_POLICY="ask_retype",
                          PSU_INPUT_QUALITY_LAYOUT_THRESHOLD="0.39", PSU_INPUT_QUALITY_REPEAT_THRESHOLD="0.55")
        guard = RuntimeInputQualityGuard.from_environment()
        changed, unobserved = [], []
        with (out / "guard_span_diagnostics.jsonl").open("w", encoding="utf-8") as log:
            for r in rows:
                decision = guard.inspect(r["question"])
                stable = (list(decision.flags) == r.get("guard", {}).get("flags") and
                          decision.profile_version == r.get("guard", {}).get("profile_version"))
                if not r.get("guard"):
                    unobserved.append(r["id"])
                    stable = None
                elif not stable:
                    changed.append(r["id"])
                log.write(json.dumps({"id": r["id"], "question": r["question"], "matches_recorded_detection": stable,
                    "decision": decision.to_log_dict(), "internal_detector_features": dataclasses.asdict(decision.features),
                    "note": "diagnostic replay only; candidate mappings are never sent as chatbot answers"}, ensure_ascii=False) + "\n")
        write_json(out / "guard_replay_consistency.json", {"n": len(rows), "changed_ids": changed,
                   "no_recorded_guard_ids": unobserved, "profile": guard.startup_status()})
    review = [d for d in diag if d["needs_manual_review"]]
    lines = ["# Per-case diagnostic review", "", "Automatically grouped from actual traces. Tags are hypotheses, not a human-verified accuracy score.",
             "The previous answer is a comparison only, not a ground-truth reference. Expected contracts are constraints, not necessarily a full ideal answer.", ""]
    for d in review:
        lines.extend([f"## {d['id']}", "", "Question: " + d["question"], "", "### Actual answer", d["answer"] or "[No output returned]", "",
                      f"Mode: {d['mode']}; status: {d['status']}; seconds: {d['wall_sec']}",
                      "Tags: " + ", ".join(d["tags"]), "", "### Expected contract", "```json",
                      json.dumps(d["expected_contract"], ensure_ascii=False, indent=2), "```", "",
                      "### Observations", *["- " + e for e in d["evidence"]],
                      "- Judge errors: " + json.dumps(d["legacy_errors"], ensure_ascii=False), "",
                      "### Next checks", *["- " + s for s in d["suggested_next_steps"]], ""])
    (out / "cases_requiring_review.md").write_text("\n".join(lines), encoding="utf-8")
    compact = {k: v for k, v in stats.items() if k not in {"stage_timings_nonadditive", "slowest"}}
    compact["faq"] = {k: v for k, v in stats["faq"].items() if k not in {"modes", "change_ids", "guard_blocked_ids", "pilot_intercept_ids", "groups"}}
    compact["keyboard"] = {k: v for k, v in stats["keyboard"].items() if k != "families"}
    print(json.dumps(compact, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
