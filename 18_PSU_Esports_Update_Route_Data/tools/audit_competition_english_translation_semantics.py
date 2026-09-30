"""Audit Thai-to-English competition-rule drafts with the local model only.

This creates a review queue; it never changes the production localization
registry or marks machine-reviewed text as human-approved.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.manage_english_localizations import source_fields  # noqa: E402


DEFAULT_DRAFTS = ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260915_audited.jsonl"
DEFAULT_MODEL = "scb10x/typhoon2.5-qwen3-4b:latest"
NUMBER_RE = re.compile(r"\d+(?:[.:/,]\d+)*")
OUTLINE_LABEL_RE = re.compile(r"(?m)^\s*(?:\d+(?:\.\d+)*|[•*])\.?(?=\s)")
URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def extract_json(text: str) -> dict[str, Any] | None:
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.IGNORECASE | re.DOTALL)
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        parsed = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def mechanical_issues(source: str, translation: str) -> list[str]:
    issues: list[str] = []
    # Outline labels such as "1." and "2.1." do not change a rule's
    # meaning, and English headings often omit them. Compare factual numbers
    # only, so reviewers are not buried under those harmless differences.
    def factual_numbers(text: str) -> list[str]:
        text = OUTLINE_LABEL_RE.sub("", text)
        # Thai schedules commonly write clock times as 08.30 while English
        # convention uses 08:30. These represent the same factual time.
        text = re.sub(r"\b(\d{1,2})\.(\d{2})\b", r"\1:\2", text)
        cardinal_words = {
            "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
            "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
            "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18",
            "nineteen": "19", "twenty": "20",
        }
        for word, number in cardinal_words.items():
            text = re.sub(rf"\b{word}\b", number, text, flags=re.IGNORECASE)
        return NUMBER_RE.findall(text)

    source_numbers = factual_numbers(source)
    translation_numbers = factual_numbers(translation)
    if source_numbers != translation_numbers:
        issues.append("numeric_tokens_changed")
    if URL_RE.findall(source) != URL_RE.findall(translation):
        issues.append("url_tokens_changed")
    if THAI_RE.search(translation):
        issues.append("thai_script_remaining")
    return issues


def review_with_local_model(source: str, translation: str, *, model: str, endpoint: str, timeout: float) -> tuple[str, list[str], float]:
    prompt = """You are auditing a Thai competition-rule source and its English draft. Do not translate or rewrite.
Return JSON only: {"verdict":"pass"|"review","issues":["short_reason"]}.
Use verdict=review if the English changes a rule, number, time limit, prohibition, condition, actor, or certainty; omits a material condition; or adds a fact. Use pass only if it is faithful.

Thai source:
""" + source + "\n\nEnglish draft:\n" + translation
    request = urllib.request.Request(
        endpoint.rstrip("/") + "/api/generate",
        data=json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "format": "json",
            "keep_alive": "20m",
            "options": {"temperature": 0, "num_predict": 96, "num_ctx": 4096},
        }, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
    except (OSError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        return "review", [f"audit_transport_{type(exc).__name__}"], time.perf_counter() - started
    payload = extract_json(str(data.get("response") or ""))
    if payload is None:
        return "review", ["audit_invalid_json"], time.perf_counter() - started
    verdict = str(payload.get("verdict") or "review").strip().lower()
    if verdict not in {"pass", "review"}:
        verdict = "review"
    issues = payload.get("issues") if isinstance(payload.get("issues"), list) else []
    issues = [str(issue).strip()[:160] for issue in issues if str(issue).strip()][:4]
    return verdict, issues, time.perf_counter() - started


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline semantic audit for English competition-rule localization drafts.")
    parser.add_argument("--drafts", type=Path, default=DEFAULT_DRAFTS)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "reports" / "competition_rules_rag_eval" / "english_semantic_audit")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--endpoint", default="http://127.0.0.1:11434")
    parser.add_argument("--timeout-sec", type=float, default=25.0)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    drafts = {
        (str(row.get("content_id") or ""), str(row.get("field") or "")): row
        for row in read_jsonl(args.drafts)
        if str(row.get("content_id") or "").startswith("competition_rules_") and row.get("text")
    }
    sources = source_fields()
    keys = sorted(key for key in drafts if key[1] == "text" and key in sources)
    if args.limit:
        keys = keys[:args.limit]

    rows: list[dict[str, Any]] = []
    for index, key in enumerate(keys, 1):
        source_row = sources[key]
        source = str(source_row.get(key[1]) or "")
        translation = str(drafts[key].get("text") or "")
        issues = mechanical_issues(source, translation)
        verdict, model_issues, elapsed = review_with_local_model(
            source, translation, model=args.model, endpoint=args.endpoint, timeout=max(1.0, args.timeout_sec)
        )
        issues.extend(model_issues)
        if issues:
            verdict = "review"
        rows.append({
            "content_id": key[0], "field": key[1], "source_text": source,
            "english_draft": translation, "verdict": verdict, "issues": issues,
            "elapsed_sec": round(elapsed, 3), "machine_audit_only": True,
        })
        print(f"[{index}/{len(keys)}] {verdict.upper()} {key[0]}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "semantic_audit.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = Counter(row["verdict"] for row in rows)
    issue_counts = Counter(issue for row in rows for issue in row["issues"])
    markdown = [
        "# Competition English Draft Semantic Audit",
        "",
        "> This is a Local-LLM audit only. It identifies review priorities and never approves or publishes translations.",
        "",
        f"- Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- Draft input: `{args.drafts}`",
        f"- Text fields checked: **{len(rows)}**",
        f"- Verdicts: `{dict(counts)}`",
        f"- Issue counts: `{dict(issue_counts)}`",
        "",
        "## Manual Review Required",
        "",
    ]
    for row in rows:
        if row["verdict"] != "review":
            continue
        markdown.extend([
            f"### {row['content_id']}",
            f"- Issues: `{', '.join(row['issues']) or 'model requested review'}`",
            f"- Thai: {row['source_text']}",
            f"- English: {row['english_draft']}",
            "",
        ])
    (args.output_dir / "semantic_audit.md").write_text("\n".join(markdown), encoding="utf-8")
    print(json.dumps({"checked": len(rows), "verdicts": dict(counts), "issues": dict(issue_counts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
