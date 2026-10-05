from __future__ import annotations

"""Translate the Thai FAQ regression corpus with the local Ollama model.

The generated file is test data only.  It is deliberately marked
``machine_translated_unreviewed`` so it can never be confused with human-
approved English knowledge used by the public chatbot.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = ROOT / "data" / "eval" / "english_shadow_1600_20260902.jsonl"
DEFAULT_OUTPUT = ROOT / "data" / "eval" / "english_shadow_1600_machine_20260908.jsonl"
DEFAULT_LOG = ROOT / "reports" / "bilingual_english" / "translation_20260908" / "translation_log.jsonl"
DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)
NUMBER_WORDS = {
    "0": ("0", "zero"), "1": ("1", "one"), "2": ("2", "two"), "3": ("3", "three"),
    "4": ("4", "four"), "5": ("5", "five"), "6": ("6", "six"), "7": ("7", "seven"),
    "8": ("8", "eight"), "9": ("9", "nine"), "10": ("10", "ten"), "15": ("15", "fifteen"),
    "30": ("30", "thirty"), "60": ("60", "sixty"), "70": ("70", "seventy"),
    "100": ("100", "one hundred"), "500": ("500", "five hundred"),
    "1000": ("1000", "one thousand"), "2000": ("2000", "two thousand"),
}
PROTECTED_TERMS = (
    ("นักศึกษา PSU/สตาฟ PSU", "[[PSU_STUDENT_OR_STAFF]]", "PSU student or PSU staff"),
    ("นักศึกษา PSU", "[[PSU_STUDENT]]", "PSU student"),
    ("สตาฟ PSU", "[[PSU_STAFF]]", "PSU staff"),
    ("นักศึกษาต่างมหาลัย", "[[EXTERNAL_UNIVERSITY_STUDENT]]", "student from another university"),
    ("นักศึกษาต่างมหาวิทยาลัย", "[[EXTERNAL_UNIVERSITY_STUDENT]]", "student from another university"),
    ("ศิษย์เก่า PSU", "[[PSU_ALUMNUS]]", "PSU alumnus"),
    ("บุคคลทั่วไป", "[[GENERAL_VISITOR]]", "general visitor"),
)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )
    # Windows Defender, preview panes, and log viewers can hold a short-lived
    # read handle. Keep the checkpoint atomic, but tolerate that transient
    # lock instead of losing an otherwise successful translation batch.
    last_error: OSError | None = None
    for _attempt in range(20):
        try:
            os.replace(temporary, path)
            return
        except PermissionError as exc:
            last_error = exc
            time.sleep(0.15)
    raise last_error or RuntimeError(f"Unable to replace {path}")


def _append_log(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()


def _numbers(text: str) -> list[str]:
    return re.findall(r"\d+(?:[.:/-]\d+)*", text)


def _clean_translation(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip(" \"'")
    # Qwen occasionally translates the Thai pricing phrase "เสียกี่บาท" too
    # literally as "lose". These rewrites only improve question grammar.
    match = re.fullmatch(r"How much does (.+?) lose playing (.+?)\?", text, flags=re.IGNORECASE)
    if match:
        return f"How much does it cost for {match.group(1)} to use {match.group(2)}?"
    match = re.fullmatch(r"(.+?), how much do they lose in baht\?", text, flags=re.IGNORECASE)
    if match:
        text = f"How much does it cost for {match.group(1)}?"
    for _thai, token, english in PROTECTED_TERMS:
        text = text.replace(token, english)
    return text


def _protected_question(text: str) -> str:
    protected = str(text or "")
    # Natural English anchors are more reliable than opaque tokens with the
    # small local model. They are authoritative labels, not new facts.
    for thai, _token, english in PROTECTED_TERMS:
        protected = protected.replace(thai, english)
    # Preserve a format constraint that small local models otherwise tend to
    # paraphrase away when translating broad knowledge questions.
    protected = protected.replace("1 ย่อหน้า", "exactly one paragraph")
    return protected


def _validate_translation(source: str, translation: str) -> str | None:
    if not translation:
        return "empty_translation"
    if THAI_RE.search(translation):
        return "thai_script_remaining"
    for thai, _token, english in PROTECTED_TERMS:
        if thai in source and english.casefold() not in translation.casefold():
            return f"protected_term_missing:{english}"
    lower_translation = translation.casefold()
    missing_numbers = []
    for number in _numbers(source):
        if any(variant in lower_translation for variant in NUMBER_WORDS.get(number, (number,))):
            continue
        # Natural English often uses an article rather than the literal digit.
        # These two forms are semantically specific and retain the source fact.
        if number == "1" and "1 ชั่วโมง" in source and "an hour" in lower_translation:
            continue
        if number == "1" and "ย่อหน้า" in source and any(
            marker in lower_translation for marker in ("paragraph", "brief", "short")
        ):
            continue
        missing_numbers.append(number)
    if missing_numbers:
        return "missing_numbers:" + ",".join(missing_numbers)
    if len(translation) < 3:
        return "translation_too_short"
    return None


def _translation_prompt(batch: list[dict[str, Any]]) -> str:
    payload = [{"id": row["id"], "th": _protected_question(row["question_th"])} for row in batch]
    return """You translate Thai PSU Esports FAQ questions into natural English for an offline test corpus.
Return exactly one JSON object and no Markdown, explanation, or analysis:
{"translations":[{"id":"same input id","en":"English question"}]}

Requirements:
- Translate every Thai word; the English output must contain no Thai script.
- Preserve every product name, game title, PSU, zone name, number, duration, currency amount, and identifier exactly.
- Do not answer the question. Do not add facts. Do not remove uncertainty, negation, or comparison.
- Keep the question concise and natural. Keep one output row per input id.
- For Thai pricing wording such as "เสียกี่บาท", use "How much does it cost..."; never use "lose".
- Translate "นักศึกษาต่างมหาลัย" as "a student from another university", and "บุคคลทั่วไป" as "a general visitor".
- Some input already contains official English labels such as "PSU student". Copy those labels without changing their meaning.

Input:
""" + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def _extract_json(text: str) -> dict[str, Any]:
    raw = str(text or "").strip()
    if raw.startswith("```"):
        raw = raw.strip("`").strip()
        raw = re.sub(r"^json\s*", "", raw, flags=re.IGNORECASE)
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        if start < 0:
            raise
        value, _end = json.JSONDecoder().raw_decode(raw[start:])
    if not isinstance(value, dict) or not isinstance(value.get("translations"), list):
        raise ValueError("response must contain a translations array")
    return value


def _call_ollama(
    prompt: str,
    *,
    model: str,
    endpoint: str,
    timeout_sec: float,
) -> tuple[dict[str, Any], float]:
    request = urllib.request.Request(
        endpoint + "/api/generate",
        data=json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
            "think": False,
            "keep_alive": "30m",
            "options": {"temperature": 0, "num_predict": 512, "num_ctx": 4096},
        }, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        payload = json.loads(response.read().decode("utf-8"))
    elapsed = time.perf_counter() - started
    return _extract_json(payload.get("response")), elapsed


def _translate_batch(
    batch: list[dict[str, Any]],
    *,
    model: str,
    endpoint: str,
    timeout_sec: float,
    retries: int,
) -> tuple[dict[str, str], list[dict[str, Any]]]:
    last_error = ""
    for attempt in range(1, retries + 1):
        try:
            payload, elapsed = _call_ollama(
                _translation_prompt(batch),
                model=model,
                endpoint=endpoint,
                timeout_sec=timeout_sec,
            )
            values = {
                str(item.get("id") or ""): _clean_translation(item.get("en"))
                for item in payload["translations"]
                if isinstance(item, dict)
            }
            expected_ids = {str(row["id"]) for row in batch}
            if set(values) != expected_ids:
                raise ValueError(f"response ids mismatch expected={sorted(expected_ids)} got={sorted(values)}")
            errors = {
                row["id"]: _validate_translation(row["question_th"], values[row["id"]])
                for row in batch
            }
            invalid = {key: value for key, value in errors.items() if value}
            if invalid:
                raise ValueError("invalid translations: " + json.dumps(invalid, ensure_ascii=False))
            return values, [{
                "event": "batch_translated",
                "attempt": attempt,
                "elapsed_sec": round(elapsed, 4),
                "count": len(batch),
            }]
        except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
    return {}, [{"event": "batch_failed", "attempts": retries, "error": last_error, "count": len(batch)}]


def _translated_row(source: dict[str, Any], translation: str, *, run_id: str, model: str) -> dict[str, Any]:
    row = dict(source)
    row.update({
        "question_en": translation,
        "translation_status": "machine_translated_unreviewed",
        "translation_method": "local_ollama_batch",
        "translation_model": model,
        "translation_run_id": run_id,
        "translation_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "translation_question_sha256": hashlib.sha256(translation.encode("utf-8")).hexdigest(),
    })
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate the 1,600 Thai FAQ cases to an unreviewed English test corpus with local Ollama.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--endpoint", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--batch-size", type=int, default=6)
    parser.add_argument("--timeout-sec", type=float, default=45.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    source_rows = _read_jsonl(args.input)
    if len(source_rows) != 1600:
        raise SystemExit(f"Expected exactly 1,600 source rows, got {len(source_rows)}")
    if len({str(row.get('id') or '') for row in source_rows}) != len(source_rows):
        raise SystemExit("Source corpus contains duplicate IDs")
    for row in source_rows:
        question = str(row.get("question_th") or "").strip()
        if not question:
            raise SystemExit(f"Missing question_th for {row.get('id')}")
        expected_hash = str(row.get("source_question_sha256") or "")
        if expected_hash and expected_hash != hashlib.sha256(question.encode("utf-8")).hexdigest():
            raise SystemExit(f"Source question hash changed for {row.get('id')}")

    existing: dict[str, dict[str, Any]] = {}
    if args.resume and args.output.exists():
        for row in _read_jsonl(args.output):
            if row.get("translation_status") == "machine_translated_unreviewed" and str(row.get("question_en") or "").strip():
                existing[str(row.get("id") or "")] = row

    requested_rows = source_rows[: args.limit] if args.limit > 0 else source_rows
    pending = [row for row in requested_rows if str(row.get("id") or "") not in existing]
    run_id = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    _append_log(args.log, {
        "event": "run_started",
        "run_id": run_id,
        "input": str(args.input),
        "output": str(args.output),
        "model": args.model,
        "total_source_rows": len(source_rows),
        "requested_rows": len(requested_rows),
        "resumed_rows": len(existing),
        "pending_rows": len(pending),
        "batch_size": args.batch_size,
    })

    translated = dict(existing)
    failures: list[str] = []
    batch_size = max(1, min(12, args.batch_size))
    for offset in range(0, len(pending), batch_size):
        batch = pending[offset:offset + batch_size]
        values, events = _translate_batch(
            batch,
            model=args.model,
            endpoint=args.endpoint,
            timeout_sec=max(5.0, args.timeout_sec),
            retries=max(1, args.retries),
        )
        for event in events:
            _append_log(args.log, {"run_id": run_id, "offset": offset, "ids": [row["id"] for row in batch], **event})
        if not values and len(batch) > 1:
            # One malformed item should not discard the entire batch. Retry each
            # question independently and preserve a failure record if it remains
            # invalid, so a later --resume is deterministic.
            for row in batch:
                single_values, single_events = _translate_batch(
                    [row],
                    model=args.model,
                    endpoint=args.endpoint,
                    timeout_sec=max(5.0, args.timeout_sec),
                    retries=max(1, args.retries),
                )
                for event in single_events:
                    _append_log(args.log, {"run_id": run_id, "offset": offset, "ids": [row["id"]], **event})
                if single_values:
                    translated[row["id"]] = _translated_row(row, single_values[row["id"]], run_id=run_id, model=args.model)
                else:
                    failures.append(str(row["id"]))
            _write_jsonl_atomic(args.output, [translated[row["id"]] for row in source_rows if row["id"] in translated])
            continue
        if not values:
            failures.extend(str(row["id"]) for row in batch)
            continue
        for row in batch:
            translated[row["id"]] = _translated_row(row, values[row["id"]], run_id=run_id, model=args.model)
        _write_jsonl_atomic(args.output, [translated[row["id"]] for row in source_rows if row["id"] in translated])
        print(f"progress {min(offset + len(batch), len(pending))}/{len(pending)} translated={len(translated)} failed={len(failures)}", flush=True)

    output_rows = [translated[row["id"]] for row in requested_rows if row["id"] in translated]
    _write_jsonl_atomic(args.output, output_rows)
    summary = {
        "run_id": run_id,
        "input": str(args.input),
        "output": str(args.output),
        "log": str(args.log),
        "model": args.model,
        "requested_rows": len(requested_rows),
        "translated_rows": len(output_rows),
        "failed_rows": len(failures),
        "failure_ids": failures,
        "status": "complete" if len(output_rows) == len(requested_rows) and not failures else "incomplete",
    }
    _append_log(args.log, {"event": "run_finished", **summary})
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
