from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import asdict, dataclass
from typing import Iterable, Sequence

from app.core.normalization import KEYBOARD_EN_TO_THAI, KEYBOARD_THAI_TO_EN


THAI_RE = re.compile(r"[\u0E00-\u0E7F]+")
LATIN_WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
ASCII_KEY_RUN_RE = re.compile(r"[A-Za-z0-9`~!@#$%^&*()_\-+=\[\]{}\\|;:'\",.<>/?]+")
REPEATED_RE = re.compile(r"(.)\1+")

PROTECTED_SPAN_RE = re.compile(
    r"(?:https?://|www\.)\S+"
    r"|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    r"|\b(?:booking_id|transaction_ref|request_id)\s*=\s*[^\s]+"
    r"|\b(?:BK|TXN)-?[A-Za-z0-9-]{5,}\b"
    r"|\b(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?\b"
    r"|\b\d{4}-\d{2}-\d{2}\b"
    r"|\b\d{1,2}:\d{2}\b"
    r"|\b\d{2,3}-\d{3}-\d{4}\b"
    r"|\{[^{}]{0,300}\}",
    re.IGNORECASE,
)

THAI_NON_BASE = frozenset("\u0e31\u0e34\u0e35\u0e36\u0e37\u0e38\u0e39\u0e47\u0e48\u0e49\u0e4a\u0e4b\u0e4c\u0e4d")

# This is a language prior, not a list of typo aliases. It protects ordinary
# English prose when the clean Thai benchmark contains few English-only rows.
GENERIC_ENGLISH_WORDS = frozenset(
    """
    a about access after all allowed am an and any are arrive available before
    book booking bring can cancel class competition contact controller cost day
    discount do does drink drinks equipment external fee food for free friends
    game games gaming has have hour how i if in include inside is late list many
    machine machines much my need of on one open own page pay play playing please
    price process reserve rules show staff status student students studio sunday
    successful tell the there this time to today two use version what when where
    which with zone
    football coffee hollow knight assassin creed duty manager minecraft valorant
    tekken nintendo switch playstation esports psu phuket api json local model rag
    retrieval website wordpress rest qr code session request transaction
    """.split()
)


def translate_keyboard_layout(value: str, mapping: dict[str, str]) -> str:
    return "".join(mapping.get(char, char) for char in value)


def _clean_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def _bounded(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class SpanEvidence:
    direction: str
    source_span: str
    mapped_span: str
    start: int
    end: int
    score: float
    source_quality: float
    target_quality: float
    target_seen: bool
    source_protected: bool
    reason: str


@dataclass(frozen=True)
class RepeatEvidence:
    source_span: str
    candidate_span: str
    repeated_char: str
    run_length: int
    start: int
    end: int
    token: str
    score: float
    original_quality: float
    candidate_quality: float
    original_seen: bool
    candidate_seen: bool
    interpretation: str
    reason: str


@dataclass(frozen=True)
class AnomalyFeatures:
    input_text: str
    layout_score: float
    layout_direction: str | None
    layout_candidate_preview: str | None
    layout_reason: str
    layout_spans: tuple[SpanEvidence, ...]
    repeat_score: float
    repeat_candidate_preview: str | None
    repeat_reason: str
    repeat_spans: tuple[RepeatEvidence, ...]

    def to_dict(self) -> dict:
        payload = asdict(self)
        payload["layout_spans"] = [asdict(item) for item in self.layout_spans]
        payload["repeat_spans"] = [asdict(item) for item in self.repeat_spans]
        return payload


class CharacterNgramProfile:
    def __init__(self, *, language: str, max_n: int = 4) -> None:
        if language not in {"th", "en"}:
            raise ValueError(f"unsupported language: {language}")
        self.language = language
        self.max_n = max_n
        self.counts: dict[int, Counter[str]] = {n: Counter() for n in range(1, max_n + 1)}
        self.max_count: dict[int, int] = {n: 1 for n in range(1, max_n + 1)}
        self.sequence_count = 0

    def normalize(self, value: str) -> str:
        if self.language == "th":
            return "".join(THAI_RE.findall(value or ""))
        return "".join(char.lower() for char in (value or "") if "a" <= char.lower() <= "z")

    def fit(self, sequences: Iterable[str]) -> None:
        for raw in sequences:
            sequence = self.normalize(raw)
            if not sequence:
                continue
            self.sequence_count += 1
            padded = f"^{sequence}$"
            for n in range(1, self.max_n + 1):
                if len(padded) < n:
                    continue
                self.counts[n].update(padded[index : index + n] for index in range(len(padded) - n + 1))
        for n, counts in self.counts.items():
            self.max_count[n] = max(counts.values(), default=1)

    def quality(self, value: str) -> float:
        sequence = self.normalize(value)
        if not sequence:
            return 0.0
        padded = f"^{sequence}$"
        weighted_score = 0.0
        weight_total = 0.0
        for n in range(1, self.max_n + 1):
            if len(padded) < n:
                continue
            grams = [padded[index : index + n] for index in range(len(padded) - n + 1)]
            seen_counts = [self.counts[n].get(gram, 0) for gram in grams]
            coverage = sum(count > 0 for count in seen_counts) / len(seen_counts)
            frequency = sum(
                math.log1p(count) / math.log1p(self.max_count[n]) if count else 0.0
                for count in seen_counts
            ) / len(seen_counts)
            n_score = (0.82 * coverage) + (0.18 * frequency)
            weight = {1: 0.10, 2: 0.22, 3: 0.30, 4: 0.38}[n]
            weighted_score += weight * n_score
            weight_total += weight
        return _bounded(weighted_score / weight_total if weight_total else 0.0)


class KeyboardInputAnomalyDetector:
    """Feature-only detector for keyboard-layout and adjacent-repeat anomalies.

    The mapped candidates are diagnostic hypotheses. Callers must not replace
    the user's input or pass a candidate to an answer route automatically.
    """

    def __init__(self) -> None:
        self.thai_profile = CharacterNgramProfile(language="th")
        self.english_profile = CharacterNgramProfile(language="en")
        self.clean_texts: set[str] = set()
        self.thai_blob = ""
        self.latin_counts: Counter[str] = Counter()
        self.fitted = False

    def fit(self, clean_texts: Sequence[str]) -> "KeyboardInputAnomalyDetector":
        self.thai_profile = CharacterNgramProfile(language="th")
        self.english_profile = CharacterNgramProfile(language="en")
        self.latin_counts = Counter()
        normalized_texts = [_clean_space(str(text)) for text in clean_texts if _clean_space(str(text))]
        self.clean_texts = {text.lower() for text in normalized_texts}

        thai_sequences: list[str] = []
        latin_sequences: list[str] = []
        for text in normalized_texts:
            thai_sequences.extend(THAI_RE.findall(text))
            words = [match.group(0).lower() for match in LATIN_WORD_RE.finditer(text)]
            latin_sequences.extend(words)
            self.latin_counts.update(words)

        self.latin_counts.update({word: 2 for word in GENERIC_ENGLISH_WORDS})
        latin_sequences.extend(GENERIC_ENGLISH_WORDS)
        self.thai_profile.fit(thai_sequences)
        self.english_profile.fit(latin_sequences)
        self.thai_blob = "\n".join(thai_sequences)
        self.fitted = True
        return self

    def _assert_fitted(self) -> None:
        if not self.fitted:
            raise RuntimeError("KeyboardInputAnomalyDetector.fit() must be called first")

    def _protected_ranges(self, text: str) -> list[tuple[int, int]]:
        return [(match.start(), match.end()) for match in PROTECTED_SPAN_RE.finditer(text)]

    @staticmethod
    def _overlaps(start: int, end: int, ranges: Sequence[tuple[int, int]]) -> bool:
        return any(start < right and end > left for left, right in ranges)

    def _latin_known(self, value: str) -> bool:
        words = [match.group(0).lower() for match in LATIN_WORD_RE.finditer(value)]
        if not words:
            return False
        # Isolated keyboard fragments such as `u` or `s` are common when valid
        # Thai text is projected onto English keys. Only real one-letter words
        # receive lexical support.
        if any(len(word) == 1 and word not in {"a", "i"} for word in words):
            return False
        return all(self.latin_counts.get(word, 0) > 0 for word in words)

    def _thai_seen(self, value: str) -> bool:
        sequence = self.thai_profile.normalize(value)
        return len(sequence) >= 2 and sequence in self.thai_blob

    def _is_protected_ascii(self, value: str) -> bool:
        stripped = value.strip(".,!?;:()[]{}<>\"'")
        if not stripped:
            return True
        if re.fullmatch(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", stripped) and self._latin_known(stripped):
            return True
        if re.fullmatch(r"[A-Z]{2,8}(?:[#-]?\d+)?", stripped):
            return True
        if re.fullmatch(r"#\d+", stripped):
            return True
        if re.fullmatch(r"\d{1,4}(?::\d{2}|[-/.]\d{1,4})+", stripped):
            return True
        if re.fullmatch(r"\d+(?:\.\d+)?", stripped):
            return True
        return False

    def _score_en_to_th_span(self, text: str, match: re.Match[str], protected: Sequence[tuple[int, int]]) -> SpanEvidence:
        source = match.group(0)
        range_protected = self._overlaps(match.start(), match.end(), protected)
        source_protected = range_protected or self._is_protected_ascii(source)
        mapped = translate_keyboard_layout(source, KEYBOARD_EN_TO_THAI)
        source_quality = self.english_profile.quality(source)
        target_quality = self.thai_profile.quality(mapped)
        target_seen = self._thai_seen(mapped)
        non_letters = sum(not char.isalpha() for char in source) / max(1, len(source))
        gain = max(0.0, target_quality - source_quality)
        score = (0.57 * target_quality) + (0.22 * gain) + (0.08 * non_letters)
        if target_seen:
            score += 0.16
        if len(source) <= 2:
            score *= 0.78 if target_seen else 0.45
        if source_protected:
            score *= 0.08
        if target_quality < 0.24:
            score *= 0.45
        reason = (
            "protected ASCII/entity span"
            if source_protected
            else f"English-key span maps to Thai quality={target_quality:.3f}, gain={gain:.3f}, seen={target_seen}"
        )
        return SpanEvidence(
            direction="thai_intended_english_active",
            source_span=source,
            mapped_span=mapped,
            start=match.start(),
            end=match.end(),
            score=round(_bounded(score), 6),
            source_quality=round(source_quality, 6),
            target_quality=round(target_quality, 6),
            target_seen=target_seen,
            source_protected=source_protected,
            reason=reason,
        )

    def _score_th_to_en_span(self, match: re.Match[str], protected: Sequence[tuple[int, int]]) -> SpanEvidence:
        source = match.group(0)
        range_protected = self._overlaps(match.start(), match.end(), protected)
        mapped = translate_keyboard_layout(source, KEYBOARD_THAI_TO_EN)
        source_quality = self.thai_profile.quality(source)
        target_quality = self.english_profile.quality(mapped)
        target_seen = self._latin_known(mapped)
        gain = max(0.0, target_quality - source_quality)
        score = (0.57 * target_quality) + (0.22 * gain)
        if target_seen:
            score += 0.20
        # A short, legitimate Thai span can map to punctuation that the
        # English profile scores highly ("โมง" -> "F,'"). With no known
        # English target and almost no quality gain, this is not evidence
        # strong enough to reject an otherwise readable Thai request.
        if not target_seen and source_quality >= 0.55 and gain < 0.08:
            score *= 0.40
        if len(source) <= 2:
            score *= 0.78 if target_seen else 0.45
        if range_protected:
            score *= 0.08
        if target_quality < 0.24:
            score *= 0.45
        reason = (
            "protected span"
            if range_protected
            else f"Thai-key span maps to English quality={target_quality:.3f}, gain={gain:.3f}, known={target_seen}"
        )
        return SpanEvidence(
            direction="english_intended_thai_active",
            source_span=source,
            mapped_span=mapped,
            start=match.start(),
            end=match.end(),
            score=round(_bounded(score), 6),
            source_quality=round(source_quality, 6),
            target_quality=round(target_quality, 6),
            target_seen=target_seen,
            source_protected=range_protected,
            reason=reason,
        )

    @staticmethod
    def _aggregate_span_score(spans: Sequence[SpanEvidence], text: str) -> float:
        if not spans:
            return 0.0
        ranked = sorted(spans, key=lambda item: item.score, reverse=True)
        top = ranked[0].score
        supporting = [item for item in spans if item.score >= max(0.42, top - 0.16)]
        covered = sum(item.end - item.start for item in supporting)
        nonspace = max(1, sum(not char.isspace() for char in text))
        coverage = min(1.0, covered / nonspace)
        support_bonus = min(0.10, max(0, len(supporting) - 1) * 0.025)
        return round(_bounded(top + support_bonus + (0.07 * coverage)), 6)

    @staticmethod
    def _preview_candidate(text: str, spans: Sequence[SpanEvidence], top_score: float) -> str | None:
        selected = [item for item in spans if item.score >= max(0.42, top_score - 0.16) and not item.source_protected]
        if not selected:
            return None
        candidate = text
        for item in sorted(selected, key=lambda value: value.start, reverse=True):
            candidate = candidate[: item.start] + item.mapped_span + candidate[item.end :]
        return candidate if candidate != text else None

    def _layout_features(self, text: str) -> tuple[float, str | None, str | None, str, tuple[SpanEvidence, ...]]:
        protected = self._protected_ranges(text)
        en_to_th = tuple(
            self._score_en_to_th_span(text, match, protected)
            for match in ASCII_KEY_RUN_RE.finditer(text)
        )
        th_to_en = tuple(
            self._score_th_to_en_span(match, protected)
            for match in THAI_RE.finditer(text)
        )
        score_en_to_th = self._aggregate_span_score(en_to_th, text)
        score_th_to_en = self._aggregate_span_score(th_to_en, text)
        if score_en_to_th <= 0 and score_th_to_en <= 0:
            return 0.0, None, None, "no keyboard-layout evidence", ()
        selected = en_to_th if score_en_to_th >= score_th_to_en else th_to_en
        direction = selected[0].direction if selected else None
        score = max(score_en_to_th, score_th_to_en)
        preview = self._preview_candidate(text, selected, max((item.score for item in selected), default=0.0))
        top = max(selected, key=lambda item: item.score) if selected else None
        reason = top.reason if top else "no keyboard-layout evidence"
        return score, direction, preview, reason, tuple(sorted(selected, key=lambda item: item.score, reverse=True))

    @staticmethod
    def _token_around(text: str, index: int) -> tuple[str, int, int]:
        for pattern in (THAI_RE, ASCII_KEY_RUN_RE, re.compile(r"[A-Za-z0-9][A-Za-z0-9'_-]*")):
            for match in pattern.finditer(text):
                if match.start() <= index < match.end():
                    return match.group(0), match.start(), match.end()
        return text[index : index + 1], index, index + 1

    def _form_evidence(self, token: str) -> tuple[float, bool]:
        candidates: list[tuple[float, bool]] = []
        if THAI_RE.search(token):
            candidates.append((self.thai_profile.quality(token), self._thai_seen(token)))
            mapped = translate_keyboard_layout(token, KEYBOARD_THAI_TO_EN)
            candidates.append((self.english_profile.quality(mapped), self._latin_known(mapped)))
        if re.search(r"[A-Za-z0-9]", token):
            candidates.append((self.english_profile.quality(token), self._latin_known(token)))
            mapped = translate_keyboard_layout(token, KEYBOARD_EN_TO_THAI)
            candidates.append((self.thai_profile.quality(mapped), self._thai_seen(mapped)))
        if not candidates:
            return 0.0, False
        return max(candidates, key=lambda item: (item[1], item[0]))

    def _score_repeat(
        self,
        text: str,
        match: re.Match[str],
        protected: Sequence[tuple[int, int]],
    ) -> RepeatEvidence:
        repeated_char = match.group(0)[0]
        run_length = len(match.group(0))
        token, token_start, token_end = self._token_around(text, match.start())
        local_start = match.start() - token_start
        candidate_token = token[:local_start] + token[local_start + 1 :]
        candidate_text = text[: match.start()] + text[match.start() + 1 :]
        original_quality, original_seen = self._form_evidence(token)
        candidate_quality, candidate_seen = self._form_evidence(candidate_token)
        at_token_end = match.end() == token_end
        mapped_repeated_char = KEYBOARD_EN_TO_THAI.get(repeated_char, repeated_char)
        maps_to_thai = bool(THAI_RE.fullmatch(mapped_repeated_char))

        if self._overlaps(match.start(), match.end(), protected):
            score = 0.0
            interpretation = "protected"
            reason = "repetition occurs inside a protected URL, ID, date, time or contact span"
        elif run_length >= 3 and at_token_end and repeated_char not in THAI_NON_BASE:
            score = 0.06
            interpretation = "expressive"
            reason = "three-or-more repeated characters at token end are treated as expressive"
        elif repeated_char.isspace() or (
            (repeated_char.isdigit() or not repeated_char.isalnum())
            and repeated_char not in THAI_NON_BASE
            and not maps_to_thai
        ):
            score = 0.0
            interpretation = "punctuation_or_numeric"
            reason = "repetition does not map to a Thai character and is not a spelling typo"
        elif original_seen and (not candidate_seen or original_quality >= candidate_quality - 0.03):
            score = 0.04
            interpretation = "lexical"
            reason = "the original repeated form is present in the clean corpus or lexicon"
        elif repeated_char in THAI_NON_BASE:
            score = 0.98
            interpretation = "accidental"
            reason = "duplicated Thai combining mark or vowel mark"
        else:
            gain = max(0.0, candidate_quality - original_quality)
            score = 0.24 + (0.28 * candidate_quality) + (0.34 * gain)
            if candidate_seen and not original_seen:
                score += 0.34
            elif candidate_seen:
                score += 0.13
            # Thai has no reliable space-delimited word boundary. An adjacent
            # duplicate inside a long Thai span is evidence only when deleting
            # it improves the form; otherwise ordinary words such as "ระบบ"
            # and "กรรมการ" would receive an unjustified boost.
            if (
                match.start() > token_start
                and match.end() < token_end
                and (gain >= 0.01 or candidate_seen)
            ):
                score += 0.08
            if run_length >= 3:
                score += 0.05
            interpretation = "accidental_candidate"
            reason = (
                f"removing one repeated character improves quality {original_quality:.3f}->{candidate_quality:.3f}; "
                f"seen {original_seen}->{candidate_seen}"
            )

        return RepeatEvidence(
            source_span=match.group(0),
            candidate_span=candidate_text,
            repeated_char=repeated_char,
            run_length=run_length,
            start=match.start(),
            end=match.end(),
            token=token,
            score=round(_bounded(score), 6),
            original_quality=round(original_quality, 6),
            candidate_quality=round(candidate_quality, 6),
            original_seen=original_seen,
            candidate_seen=candidate_seen,
            interpretation=interpretation,
            reason=reason,
        )

    def _repeat_features(self, text: str) -> tuple[float, str | None, str, tuple[RepeatEvidence, ...]]:
        protected = self._protected_ranges(text)
        spans = tuple(
            self._score_repeat(text, match, protected)
            for match in REPEATED_RE.finditer(text)
            if not match.group(0)[0].isspace()
        )
        if not spans:
            return 0.0, None, "no adjacent repeated character", ()
        ranked = tuple(sorted(spans, key=lambda item: item.score, reverse=True))
        top = ranked[0]
        return top.score, top.candidate_span, top.reason, ranked

    def analyze(self, text: str) -> AnomalyFeatures:
        self._assert_fitted()
        clean = _clean_space(text)
        layout_score, direction, layout_preview, layout_reason, layout_spans = self._layout_features(clean)
        repeat_score, repeat_preview, repeat_reason, repeat_spans = self._repeat_features(clean)
        return AnomalyFeatures(
            input_text=clean,
            layout_score=layout_score,
            layout_direction=direction,
            layout_candidate_preview=layout_preview,
            layout_reason=layout_reason,
            layout_spans=layout_spans,
            repeat_score=repeat_score,
            repeat_candidate_preview=repeat_preview,
            repeat_reason=repeat_reason,
            repeat_spans=repeat_spans,
        )

    @staticmethod
    def classify(features: AnomalyFeatures, *, layout_threshold: float, repeat_threshold: float) -> dict:
        layout_detected = features.layout_score >= layout_threshold
        repeat_detected = features.repeat_score >= repeat_threshold
        flags: list[str] = []
        if layout_detected:
            flags.append("keyboard_layout_mismatch")
        if repeat_detected:
            flags.append("repeated_character_typo")
        if layout_detected:
            action = "request_retype"
        elif repeat_detected:
            action = "soft_flag_typo"
        else:
            action = "continue"
        return {
            "predicted_flags": flags,
            "predicted_keyboard_layout": layout_detected,
            "predicted_repeated_character": repeat_detected,
            "predicted_should_block": layout_detected,
            "predicted_action": action,
        }
