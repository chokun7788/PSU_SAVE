from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from app.core.keyboard_input_anomaly import AnomalyFeatures, KeyboardInputAnomalyDetector


ROOT_DIR = Path(__file__).resolve().parents[2]
RUNTIME_CORPUS_PATHS = (
    ROOT_DIR / "data" / "curated" / "game_title_aliases.jsonl",
    ROOT_DIR / "data" / "curated" / "game_item_details.jsonl",
    ROOT_DIR / "data" / "curated" / "our_games_scraped_details.jsonl",
    ROOT_DIR / "data" / "curated" / "game_control_facts.jsonl",
    ROOT_DIR / "data" / "curated" / "service_game_availability.jsonl",
    ROOT_DIR / "data" / "curated" / "member_profiles.jsonl",
    ROOT_DIR / "data" / "curated" / "rule_patterns.jsonl",
    ROOT_DIR / "data" / "curated" / "curated_facts.jsonl",
    ROOT_DIR / "data" / "curated" / "curated_competition_rules.jsonl",
    ROOT_DIR / "data" / "competition_rules" / "competition_rule_fact_cards.jsonl",
    ROOT_DIR / "data" / "competition_rules" / "competition_rule_fact_cards_extra.jsonl",
    ROOT_DIR / "data" / "competition_rules" / "competition_rule_fact_cards_round5_challenger_repairs.jsonl",
)
TEXT_FIELDS = (
    "title", "text", "answer", "aliases", "question_patterns", "patterns", "tags",
    "name", "role", "zone", "service_label", "machine_label", "games", "notes",
)
# These are calibrated against the published runtime corpus, not the older
# evaluation-question corpus used by the standalone prototype.
DEFAULT_LAYOUT_THRESHOLD = 0.39
DEFAULT_REPEAT_THRESHOLD = 0.55
PROFILE_FORMAT_VERSION = "keyboard-profile-v1"


def _truthy(value: str | None, *, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def _env_float(name: str, default: float) -> float:
    try:
        return min(1.0, max(0.0, float(os.getenv(name, str(default)))))
    except ValueError:
        return default


def keyboard_guard_enabled() -> bool:
    return _truthy(os.getenv("PSU_INPUT_QUALITY_GUARD_ENABLED"), default=True)


def _iter_strings(value: object) -> Iterable[str]:
    if isinstance(value, str) and value.strip():
        yield value.strip()
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _iter_strings(item)


def load_runtime_clean_texts() -> list[str]:
    """Build the detector corpus from published chatbot knowledge, not eval cases."""
    texts: list[str] = []
    seen: set[str] = set()
    for path in RUNTIME_CORPUS_PATHS:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(row, dict):
                    continue
                for field in TEXT_FIELDS:
                    for value in _iter_strings(row.get(field)):
                        key = value.casefold()
                        if key not in seen:
                            seen.add(key)
                            texts.append(value)
    if not texts:
        raise RuntimeError("No published knowledge text was available for the input-quality guard")
    return texts


def profile_version_for_texts(texts: Iterable[str]) -> str:
    """Return a stable identifier for the exact published text used to fit a profile."""
    digest = hashlib.sha256()
    for text in texts:
        digest.update(text.casefold().encode("utf-8"))
        digest.update(b"\n")
    return f"{PROFILE_FORMAT_VERSION}:{digest.hexdigest()[:16]}"


@dataclass(frozen=True)
class InputQualityDecision:
    detected_action: str
    applied_action: str
    should_short_circuit: bool
    message: str
    features: AnomalyFeatures
    flags: tuple[str, ...]
    guard_mode: str
    repeat_policy: str
    profile_version: str
    elapsed_ms: float

    @property
    def action(self) -> str:
        """Compatibility name for the detector's recommended action."""
        return self.detected_action

    @property
    def mode(self) -> str:
        if "keyboard_layout_mismatch" in self.flags:
            return "input_guard_layout_retype"
        if "repeated_character_typo" in self.flags:
            return "input_guard_repeat_retype"
        return "input_guard_continue"

    def to_public_dict(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "action": self.action,
            "detected_action": self.detected_action,
            "applied_action": self.applied_action,
            "should_retype": self.should_short_circuit,
            "flags": list(self.flags),
            "layout_score": self.features.layout_score,
            "repeat_score": self.features.repeat_score,
            "guard_status": "flagged" if self.flags else "passed",
            "guard_mode": self.guard_mode,
            "repeat_policy": self.repeat_policy,
            "profile_version": self.profile_version,
            "guard_elapsed_ms": self.elapsed_ms,
        }
        if self.applied_action == "warn_and_continue" and self.message:
            payload["notice"] = self.message
        return payload

    def to_log_dict(self) -> dict[str, object]:
        return {
            **self.to_public_dict(),
            "layout_direction": self.features.layout_direction,
            "layout_reason": self.features.layout_reason,
            "repeat_reason": self.features.repeat_reason,
        }


class RuntimeInputQualityGuard:
    """Detect suspicious input before routing without mutating the user's text."""

    def __init__(
        self,
        detector: KeyboardInputAnomalyDetector,
        *,
        layout_threshold: float = DEFAULT_LAYOUT_THRESHOLD,
        repeat_threshold: float = DEFAULT_REPEAT_THRESHOLD,
        mode: str = "shadow",
        repeat_policy: str = "ask_retype",
        corpus_size: int = 0,
        profile_version: str = "",
    ) -> None:
        if mode not in {"shadow", "enforce"}:
            raise ValueError("mode must be 'shadow' or 'enforce'")
        if repeat_policy not in {"ask_retype", "warn_and_continue"}:
            raise ValueError("repeat_policy must be 'ask_retype' or 'warn_and_continue'")
        self.detector = detector
        self.layout_threshold = layout_threshold
        self.repeat_threshold = repeat_threshold
        self.mode = mode
        self.repeat_policy = repeat_policy
        self.corpus_size = corpus_size
        self.profile_version = profile_version

    @classmethod
    def from_environment(cls) -> "RuntimeInputQualityGuard":
        mode = os.getenv("PSU_INPUT_QUALITY_GUARD_MODE", "shadow").strip().lower()
        repeat_policy = os.getenv("PSU_INPUT_QUALITY_REPEAT_POLICY", "ask_retype").strip().lower()
        texts = load_runtime_clean_texts()
        detector = KeyboardInputAnomalyDetector().fit(texts)
        return cls(
            detector,
            layout_threshold=_env_float("PSU_INPUT_QUALITY_LAYOUT_THRESHOLD", DEFAULT_LAYOUT_THRESHOLD),
            repeat_threshold=_env_float("PSU_INPUT_QUALITY_REPEAT_THRESHOLD", DEFAULT_REPEAT_THRESHOLD),
            mode=mode if mode in {"shadow", "enforce"} else "shadow",
            repeat_policy=repeat_policy if repeat_policy in {"ask_retype", "warn_and_continue"} else "ask_retype",
            corpus_size=len(texts),
            profile_version=profile_version_for_texts(texts),
        )

    def inspect(self, text: str) -> InputQualityDecision:
        started = time.perf_counter()
        features = self.detector.analyze(text)
        classified = self.detector.classify(
            features,
            layout_threshold=self.layout_threshold,
            repeat_threshold=self.repeat_threshold,
        )
        flags = tuple(str(flag) for flag in classified["predicted_flags"])
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)

        def decision(
            *,
            detected_action: str,
            applied_action: str,
            should_short_circuit: bool,
            message: str,
        ) -> InputQualityDecision:
            return InputQualityDecision(
                detected_action=detected_action,
                applied_action=applied_action,
                should_short_circuit=should_short_circuit,
                message=message,
                features=features,
                flags=flags,
                guard_mode=self.mode,
                repeat_policy=self.repeat_policy,
                profile_version=self.profile_version,
                elapsed_ms=elapsed_ms,
            )

        if "keyboard_layout_mismatch" in flags:
            should_short_circuit = self.mode == "enforce"
            return decision(
                detected_action="request_retype",
                applied_action="request_retype" if should_short_circuit else "continue",
                should_short_circuit=should_short_circuit,
                message="เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ",
            )
        if "repeated_character_typo" in flags:
            should_short_circuit = self.mode == "enforce" and self.repeat_policy == "ask_retype"
            should_warn = self.mode == "enforce" and self.repeat_policy == "warn_and_continue"
            return decision(
                detected_action="request_retype",
                applied_action="request_retype" if should_short_circuit else ("warn_and_continue" if should_warn else "continue"),
                should_short_circuit=should_short_circuit,
                message="ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ",
            )
        return decision(
            detected_action="continue",
            applied_action="continue",
            should_short_circuit=False,
            message="",
        )

    def startup_status(self) -> dict[str, object]:
        return {
            "enabled": True,
            "mode": self.mode,
            "repeat_policy": self.repeat_policy,
            "layout_threshold": self.layout_threshold,
            "repeat_threshold": self.repeat_threshold,
            "corpus_size": self.corpus_size,
            "profile_version": self.profile_version,
        }
