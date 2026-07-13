from __future__ import annotations

import json
import re
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
RULES_PATH = PROJECT_DIR / "data" / "curated" / "rule_patterns.jsonl"


def is_thai(text: str) -> bool:
    thai_chars = sum(1 for ch in text if "\u0E00" <= ch <= "\u0E7F")
    return thai_chars > 0


def normalize_query(query: str) -> str:
    query = query.lower().strip()
    query = query.translate(str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789"))
    query = re.sub(r"p\s*\.?\s*s\s*\.?\s*u\.?", "psu", query)
    replacements = {
        "ม.อ.": "มอ",
        "ม.อ": "มอ",
        "ม. อ.": "มอ",
        "กีโมง": "กี่โมง",
        "เช็คอิน": "เชคอิน",
        "check-in": "checkin",
        "check in": "checkin",
        "ช.ม.": "ชม",
        "ชม.": "ชม",
        "ชัวโมง": "ชั่วโมง",
        "น.ท.": "นาที",
    }
    for old, new in replacements.items():
        query = query.replace(old, new)
    query = re.sub(r"\s+", " ", query)
    return query


def adapt_answer_to_query(query: str, rule: dict, answer: str) -> str:
    """Tune deterministic FAQ answers for obvious wording/unit variants."""
    q = normalize_query(query)
    rule_id = rule.get("id", "")

    if rule_id == "rule_checkin_advance":
        if "วินาที" in q or "second" in q:
            if is_thai(query):
                return "เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง"
            return "Check-in is available up to 30 minutes, or 1,800 seconds, before the reserved time slot begins."
        if "ชั่วโมง" in q or "hour" in q:
            if is_thai(query):
                return "เช็คอินได้ล่วงหน้าสูงสุด 0.5 ชั่วโมง หรือ 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง"
            return "Check-in is available up to 0.5 hours, or 30 minutes, before the reserved time slot begins."

    return answer


def load_rules(path: Path = RULES_PATH) -> list[dict]:
    rules: list[dict] = []
    if not path.exists():
        return rules
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rules.append(json.loads(line))
    return sorted(rules, key=lambda r: int(r.get("priority", 0)), reverse=True)


def match_rule(query: str, rules: list[dict] | None = None) -> dict | None:
    rules = rules if rules is not None else load_rules()
    q = normalize_query(query)
    candidates: list[tuple[int, dict, str]] = []
    for rule in rules:
        for pattern in rule.get("patterns", []):
            try:
                if re.search(pattern, q, flags=re.IGNORECASE):
                    candidates.append((int(rule.get("priority", 0)), rule, pattern))
                    break
            except re.error:
                if pattern.lower() in q:
                    candidates.append((int(rule.get("priority", 0)), rule, pattern))
                    break
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0], reverse=True)
    _, rule, matched_pattern = candidates[0]
    answer_key = "answer_th" if is_thai(query) else "answer_en"
    answer = rule.get(answer_key) or rule.get("answer_th") or rule.get("answer_en", "")
    answer = adapt_answer_to_query(query, rule, answer)
    return {
        "mode": "rule",
        "rule_id": rule.get("id"),
        "intent": rule.get("intent"),
        "category": rule.get("category"),
        "matched_pattern": matched_pattern,
        "answer": answer,
        "source_ids": rule.get("source_ids", []),
        "source_url": rule.get("source_url", ""),
        "priority": rule.get("priority", 0),
    }


if __name__ == "__main__":
    import sys

    q = " ".join(sys.argv[1:]) or "เช็คอินล่วงหน้าได้กี่นาที"
    result = match_rule(q)
    print(json.dumps(result, ensure_ascii=False, indent=2))
