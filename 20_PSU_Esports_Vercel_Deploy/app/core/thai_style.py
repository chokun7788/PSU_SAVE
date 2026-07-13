from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any


_PROTECTED_PATTERN = re.compile(r"`[^`\n]+`|https?://\S+|local://\S+")
_PLACEHOLDER = "__PSU_PROTECTED_{index}__"
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_STYLE_RULES_PATH = _PROJECT_ROOT / "data" / "style" / "thai_style_rules.jsonl"

_FALLBACK_STYLE_RULES: tuple[dict[str, Any], ...] = (
    {
        "rule_id": "thai_repeat_mark_spacing",
        "enabled": True,
        "kind": "regex_sub",
        "pattern": r"\s*ๆ\s*",
        "replacement": " ๆ ",
    },
    {
        "rule_id": "thai_number_spacing",
        "enabled": True,
        "kind": "regex_sub_pair",
        "patterns": [
            {"pattern": r"([\u0E00-\u0E7F])(\d)", "replacement": r"\1 \2"},
            {"pattern": r"(\d)([\u0E00-\u0E7F])", "replacement": r"\1 \2"},
        ],
    },
    {
        "rule_id": "collapse_repeated_spaces",
        "enabled": True,
        "kind": "regex_sub",
        "pattern": r"[ \t]{2,}",
        "replacement": " ",
    },
)


@lru_cache(maxsize=1)
def load_thai_style_rules() -> tuple[dict[str, Any], ...]:
    """Load local answer-style rules with source metadata.

    The chatbot must not call external style APIs at runtime. Keeping these
    rules in data/style lets us cite official rules where available and keep
    project-only readability rules clearly separated.
    """
    if not _STYLE_RULES_PATH.exists():
        return _FALLBACK_STYLE_RULES

    rules: list[dict[str, Any]] = []
    for line in _STYLE_RULES_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rule = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(rule, dict) and rule.get("enabled", True):
            rules.append(rule)
    return tuple(rules) or _FALLBACK_STYLE_RULES


def _protect_segments(text: str) -> tuple[str, list[str]]:
    protected: list[str] = []

    def replace(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return _PLACEHOLDER.format(index=len(protected) - 1)

    return _PROTECTED_PATTERN.sub(replace, text), protected


def _restore_segments(text: str, protected: list[str]) -> str:
    for index, segment in enumerate(protected):
        text = text.replace(_PLACEHOLDER.format(index=index), segment)
    return text


def _apply_regex_rule(text: str, rule: dict[str, Any]) -> str:
    pattern = rule.get("pattern")
    replacement = rule.get("replacement", "")
    if not isinstance(pattern, str) or not isinstance(replacement, str):
        return text
    try:
        return re.sub(pattern, replacement, text)
    except re.error:
        return text


def _apply_configured_rules(text: str) -> str:
    for rule in load_thai_style_rules():
        kind = rule.get("kind")
        if kind == "regex_sub":
            text = _apply_regex_rule(text, rule)
            continue
        if kind == "regex_sub_pair":
            patterns = rule.get("patterns", [])
            if not isinstance(patterns, list):
                continue
            for pattern_rule in patterns:
                if isinstance(pattern_rule, dict):
                    text = _apply_regex_rule(text, pattern_rule)
    return text


def _style_line(line: str) -> str:
    if not line.strip():
        return ""

    prefix = ""
    body = line
    match = re.match(r"^(\s*(?:[-*]|\d+[.)])\s+)(.*)$", line)
    if match:
        prefix = match.group(1)
        body = match.group(2)

    body = _apply_configured_rules(body)
    body = re.sub(r"\s+([,.:;!?%>\)\]\}])", r"\1", body)
    body = re.sub(r"\s+([，。：；！？、])", r"\1", body)
    body = re.sub(r"([(\[\{<])\s+", r"\1", body)
    return (prefix + body).rstrip()


def format_thai_response_style(text: str) -> str:
    """Apply safe Thai presentation fixes without changing facts or sources."""
    if not text:
        return text

    protected_text, protected = _protect_segments(text)
    styled = "\n".join(_style_line(line) for line in protected_text.splitlines())
    styled = re.sub(r"\n{3,}", "\n\n", styled).strip()
    return _restore_segments(styled, protected)
