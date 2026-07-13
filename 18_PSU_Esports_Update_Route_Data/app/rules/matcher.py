from __future__ import annotations

import re

from app.core.normalization import normalize_text
from app.rules.loader import load_rule_files


def is_thai(text: str) -> bool:
    thai_chars = sum(1 for ch in text if "\u0E00" <= ch <= "\u0E7F")
    return thai_chars > 0


class RuleMatcher:
    def __init__(self, rules: list[dict]):
        self.rules = sorted(rules, key=lambda row: int(row.get("priority", 0)), reverse=True)
        self.compiled_rules: list[tuple[dict, list[tuple[str, re.Pattern[str] | None]]]] = []
        for rule in self.rules:
            compiled_patterns: list[tuple[str, re.Pattern[str] | None]] = []
            for pattern in rule.get("patterns", []):
                try:
                    compiled_patterns.append((pattern, re.compile(pattern, flags=re.IGNORECASE)))
                except re.error:
                    compiled_patterns.append((pattern, None))
            self.compiled_rules.append((rule, compiled_patterns))

    @classmethod
    def default(cls) -> "RuleMatcher":
        return cls(load_rule_files())

    def match(self, query: str, category: str | set[str] | None = None) -> dict | None:
        q = normalize_text(query)
        allowed_categories: set[str] | None
        if category is None:
            allowed_categories = None
        elif isinstance(category, str):
            allowed_categories = {category}
        else:
            allowed_categories = set(category)

        candidates: list[tuple[int, dict, str]] = []
        for rule, compiled_patterns in self.compiled_rules:
            if allowed_categories is not None and str(rule.get("category", "")) not in allowed_categories:
                continue
            for pattern, compiled in compiled_patterns:
                if compiled is not None:
                    if compiled.search(q):
                        candidates.append((int(rule.get("priority", 0)), rule, pattern))
                        break
                elif normalize_text(pattern) in q:
                    candidates.append((int(rule.get("priority", 0)), rule, pattern))
                    break

        if not candidates:
            return None
        candidates.sort(key=lambda item: item[0], reverse=True)
        _, rule, matched_pattern = candidates[0]
        answer_key = "answer_th" if is_thai(query) else "answer_en"
        answer = rule.get(answer_key) or rule.get("answer_th") or rule.get("answer_en", "")
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
            "rule_file": rule.get("_rule_file", ""),
        }
