from __future__ import annotations

"""Create Local-LLM English drafts for scalar canonical localization fields.

The output remains review data with status=draft. It never writes back to a
canonical record and can therefore never expose machine text to the chatbot.
"""

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "content" / "review" / "en_localization_drafts.jsonl"
DEFAULT_OUTPUT = ROOT / "data" / "content" / "review" / "en_localization_drafts_machine.jsonl"
DEFAULT_LOG = ROOT / "reports" / "canonical_content" / "english_draft_generation.jsonl"
DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
DEFAULT_ENDPOINT = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
URL_RE = re.compile(r"https?://[^\s]+")
NUMBER_RE = re.compile(r"(?<![A-Za-z])\d+(?:[.,:]\d+)*(?:%|บาท|THB)?")
PLACEHOLDER_TEXTS = {"english translation", "translated english text", "translation"}


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")
    for _ in range(20):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            time.sleep(0.15)
    raise RuntimeError(f"Unable to replace {path}")


def _append_log(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def _is_translatable(value: Any) -> bool:
    return isinstance(value, str) or (isinstance(value, list) and all(isinstance(item, str) for item in value))


def _source_for_prompt(value: Any) -> str:
    if isinstance(value, list):
        return "\n".join(f"- {item}" for item in value)
    return str(value or "")


def _tokens(value: Any, pattern: re.Pattern[str]) -> list[str]:
    return pattern.findall(_source_for_prompt(value))


def _validate_faithful_translation(source: Any, text: str) -> str:
    if text.casefold().strip(" .") in PLACEHOLDER_TEXTS:
        raise ValueError("placeholder translation")
    if _tokens(source, NUMBER_RE) != _tokens(text, NUMBER_RE):
        raise ValueError("numeric tokens changed during translation")
    if _tokens(source, URL_RE) != _tokens(text, URL_RE):
        raise ValueError("URL tokens changed during translation")
    return text


def _prompt(row: dict[str, Any]) -> str:
    return """Translate one Thai PSU Esports content field into clear, faithful English.
Return exactly one JSON object and no Markdown or explanation:
{"text":"English translation"}

Rules:
- Preserve every number, official game title, PSU, product name, time, amount, identifier, URL, and uncertainty.
- Do not add facts, explanations, policies, or claims that are not in the source.
- The output must contain no Thai script.
- This is a review draft, not a public answer.

Metadata:
category: """ + str(row.get("category") or "") + "\nfield: " + str(row.get("field") or "") + "\nsource:\n" + _source_for_prompt(row.get("source_text"))


def _extract_text(raw: str) -> str:
    raw = str(raw or "").strip()
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        if start < 0:
            raise
        value, _end = json.JSONDecoder().raw_decode(raw[start:])
    text = re.sub(r"\s+", " ", str(value.get("text") or "")).strip(" \"")
    if not text:
        raise ValueError("empty translation")
    if THAI_RE.search(text):
        raise ValueError("Thai script remains in translation")
    return text


def _translate(row: dict[str, Any], *, model: str, endpoint: str, timeout_sec: float) -> tuple[str, float]:
    request = urllib.request.Request(
        endpoint + "/api/generate",
        data=json.dumps({
            "model": model,
            "prompt": _prompt(row),
            "stream": False,
            "think": False,
            "keep_alive": "30m",
            "options": {"temperature": 0, "num_predict": 900, "num_ctx": 4096},
        }, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        payload = json.loads(response.read().decode("utf-8"))
    text = _extract_text(payload.get("response"))
    return _validate_faithful_translation(row.get("source_text"), text), time.perf_counter() - started


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate unapproved English drafts for scalar canonical localization fields.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--timeout-sec", type=float, default=45.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    source = _read_jsonl(args.input)
    existing: dict[tuple[str, str], dict[str, Any]] = {}
    if args.resume and args.output.exists():
        for row in _read_jsonl(args.output):
            if str(row.get("text") or "").strip():
                existing[(str(row.get("content_id") or ""), str(row.get("field") or ""))] = row
    output: list[dict[str, Any]] = []
    pending: list[dict[str, Any]] = []
    for row in source:
        key = (str(row.get("content_id") or ""), str(row.get("field") or ""))
        if key in existing:
            output.append(existing[key])
        elif str(row.get("text") or "").strip() or not _is_translatable(row.get("source_text")):
            output.append(dict(row))
        else:
            pending.append(dict(row))
    if args.limit:
        pending = pending[: args.limit]
    run_id = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    failures: list[str] = []
    for index, row in enumerate(pending, 1):
        last_error = ""
        for attempt in range(1, max(1, args.retries) + 1):
            try:
                translated, elapsed = _translate(row, model=args.model, endpoint=args.endpoint, timeout_sec=max(5.0, args.timeout_sec))
                drafted = dict(row)
                drafted.update({
                    "text": translated,
                    "status": "draft",
                    "translation_method": "local_ollama_draft",
                    "translation_model": args.model,
                    "translation_run_id": run_id,
                    "translation_at": datetime.now().astimezone().isoformat(timespec="seconds"),
                })
                output.append(drafted)
                _append_log(args.log, {"event": "drafted", "run_id": run_id, "content_id": row["content_id"], "field": row["field"], "attempt": attempt, "elapsed_sec": round(elapsed, 4)})
                break
            except (OSError, TimeoutError, ValueError, urllib.error.URLError, json.JSONDecodeError) as exc:
                last_error = f"{type(exc).__name__}: {exc}"
        else:
            failures.append(f"{row.get('content_id')}::{row.get('field')}")
            output.append(dict(row))
            _append_log(args.log, {"event": "failed", "run_id": run_id, "content_id": row["content_id"], "field": row["field"], "error": last_error})
        if index % 10 == 0 or index == len(pending):
            _write_jsonl_atomic(args.output, output)
            print(f"progress {index}/{len(pending)} drafted={sum(bool(row.get('text')) for row in output)} failed={len(failures)}", flush=True)
    _write_jsonl_atomic(args.output, output)
    summary = {"run_id": run_id, "total_rows": len(source), "attempted_scalar_drafts": len(pending), "drafted_rows": sum(bool(row.get("text")) for row in output), "failed": failures, "output": str(args.output)}
    _append_log(args.log, {"event": "finished", **summary})
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
