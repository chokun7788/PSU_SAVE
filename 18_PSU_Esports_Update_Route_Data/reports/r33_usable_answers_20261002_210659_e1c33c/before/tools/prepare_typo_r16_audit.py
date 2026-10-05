"""Freeze file hashes and mechanical triage without modifying the r15 run."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "reports/bilingual_typo_2000_20260929"
FIXTURE = ROOT / "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl"
SPECIAL_REVIEW = {
    "MASTER-GT-EN-02255": "real_word_ambiguity_play_pay",
    "MASTER-GT-TH-04867": "missing_second_subanswer",
    "MASTER-GT-TH-00085": "wrong_operation_price_to_game",
    "MASTER-GT-TH-00890": "live_intent_lost",
    "MASTER-GT-EN-02806": "control_intent_lost",
    "MASTER-GT-EN-03895": "protected_policy_intent_lost",
}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def primary_failure(row: dict) -> str:
    noisy = row["noisy"]
    for key in ("route", "status", "content", "latency"):
        if not noisy.get(f"{key}_ok", True):
            return key
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "baseline_manifest.json"
    triage_path = output_dir / "r15_regression_triage.jsonl"
    if manifest_path.exists() or triage_path.exists():
        parser.error("audit output exists; use a new directory")
    inputs = [
        FIXTURE,
        INPUT_DIR / "paired_th_r15.jsonl",
        INPUT_DIR / "paired_en_r15.jsonl",
        INPUT_DIR / "analysis_r15.json",
        INPUT_DIR / "failure_taxonomy_20260930.json",
    ]
    paired = read_jsonl(inputs[1]) + read_jsonl(inputs[2])
    triage = []
    for row in paired:
        if not row["regression"]:
            continue
        triage.append({
            "id": row["id"], "locale": row["locale"], "domain": row["domain"],
            "edit_recipe": row["edit_recipe"], "primary_failure": primary_failure(row),
            "case_tag": SPECIAL_REVIEW.get(row["id"], "mechanical_failure_needs_semantic_review"),
            "source_review_status": row.get("review_status", ""),
            "owner_confirmed": False,
        })
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "baseline": "r15 frozen",
        "files": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in inputs
        ],
        "paired_cases": len(paired),
        "r15_regressions": len(triage),
        "interpretation": "Mechanical failure classification, not owner-confirmed answer truth.",
    }
    with manifest_path.open("x", encoding="utf-8") as stream:
        json.dump(manifest, stream, ensure_ascii=False, indent=2)
    with triage_path.open("x", encoding="utf-8") as stream:
        for row in triage:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps({"manifest": str(manifest_path), "triage": str(triage_path),
                      "paired_cases": len(paired), "regressions": len(triage)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
