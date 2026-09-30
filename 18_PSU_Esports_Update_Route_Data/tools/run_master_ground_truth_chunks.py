#!/usr/bin/env python3
"""Stream an isolated, reproducible chunk of the bilingual master evaluation."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_master_ground_truth_eval import (  # noqa: E402
    DEFAULT_CORPUS,
    choose_cases,
    evaluate,
    read_jsonl,
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--runtime-version", default="2026.09.28-owner-review-candidate-r8")
    args = parser.parse_args()
    if args.offset < 0 or args.limit <= 0:
        parser.error("offset must be nonnegative and limit must be positive")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    run_dir = args.run_dir.resolve()
    run_dir.mkdir(parents=True, exist_ok=False)
    corpus = args.corpus.resolve()
    cases = choose_cases(
        read_jsonl(corpus), locale="", domains=set(),
        sample_per_domain=0, offset=args.offset, limit=args.limit,
    )
    manifest = {
        "started_at": datetime.now().astimezone().isoformat(),
        "project_root": str(ROOT),
        "corpus": str(corpus),
        "corpus_sha256": _sha256(corpus),
        "offset": args.offset,
        "limit": args.limit,
        "selected": len(cases),
        "allow_llm": False,
        "rag_fallback": False,
        "runtime_version": args.runtime_version,
        "engine_sha256": _sha256(ROOT / "app/pipeline/engine.py"),
        "english_sha256": _sha256(ROOT / "app/pipeline/bilingual_english.py"),
        "router_sha256": _sha256(ROOT / "app/pipeline/router.py"),
    }
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    counts: Counter[str] = Counter()
    started = time.perf_counter()
    with (run_dir / "results.jsonl").open("x", encoding="utf-8") as output:
        for index, case in enumerate(cases, 1):
            try:
                row = evaluate(case, allow_llm=False, rag_fallback=False)
            except Exception as exc:  # Keep the rest of the corpus reviewable.
                row = {
                    "id": case.get("id"), "locale": case.get("locale"),
                    "domain": case.get("domain"), "question": case.get("question"),
                    "passed": False, "evaluation_error": f"{type(exc).__name__}: {exc}",
                    "failures": ["evaluation_error"],
                }
            output.write(json.dumps(row, ensure_ascii=False) + "\n")
            output.flush()
            counts["passed" if row.get("passed") else "failed"] += 1
            counts[f"locale_{row.get('locale')}"] += 1
            if row.get("evaluation_error"):
                counts["evaluation_errors"] += 1
            if index % 100 == 0 or index == len(cases):
                print(
                    f"{index}/{len(cases)} pass={counts['passed']} "
                    f"fail={counts['failed']} elapsed={time.perf_counter()-started:.1f}s",
                    flush=True,
                )
    summary = {
        **manifest,
        "finished_at": datetime.now().astimezone().isoformat(),
        "counts": dict(counts),
        "elapsed_sec": round(time.perf_counter() - started, 3),
        "results": str(run_dir / "results.jsonl"),
    }
    (run_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"COMPLETE {run_dir}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
