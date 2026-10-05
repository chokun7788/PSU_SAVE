"""Hard evidence gates for approved competition-rule V2.1 claims."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
from typing import Any, Iterable

from app.pipeline.competition_taxonomy import canonical_facet


@dataclass(frozen=True)
class ClaimRejection:
    claim_id: str
    codes: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {"claim_id": self.claim_id, "codes": list(self.codes)}


@dataclass(frozen=True)
class CompetitionClaimSelection:
    accepted: tuple[dict[str, Any], ...]
    rejected: tuple[ClaimRejection, ...]

    @property
    def claim_ids(self) -> tuple[str, ...]:
        return tuple(str(row.get("claim_id") or "") for row in self.accepted)


@dataclass(frozen=True)
class SentenceAttributionValidation:
    ok: bool
    errors: tuple[str, ...]
    used_claim_ids: tuple[str, ...]


@dataclass(frozen=True)
class CompletenessValidation:
    ok: bool
    required: bool
    errors: tuple[str, ...]


def _parse_datetime(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def _claim_rejection_codes(
    row: dict[str, Any],
    *,
    release_id: str,
    game_id: str,
    facet: str,
    locale: str,
    effective_at: datetime,
) -> tuple[str, ...]:
    codes: list[str] = []
    retrieval = row.get("retrieval") if isinstance(row.get("retrieval"), dict) else {}
    claim = row.get("claim") if isinstance(row.get("claim"), dict) else {}
    lifecycle = row.get("lifecycle") if isinstance(row.get("lifecycle"), dict) else {}
    quality = row.get("quality") if isinstance(row.get("quality"), dict) else {}
    source = row.get("source") if isinstance(row.get("source"), dict) else {}
    evidence = row.get("evidence") if isinstance(row.get("evidence"), dict) else {}

    if row.get("schema_version") != "competition_rule_claim_v2_1":
        codes.append("unsupported_schema")
    if row.get("release_id") != release_id:
        codes.append("wrong_release")
    if row.get("status") != "approved" or row.get("answerable") is not True:
        codes.append("not_runtime_answerable")
    if retrieval.get("game_id") != game_id:
        codes.append("cross_game")
    requested_facet = canonical_facet(facet) or facet
    claim_facet = canonical_facet(str(retrieval.get("facet") or "")) or retrieval.get("facet")
    if claim_facet != requested_facet:
        codes.append("wrong_facet")
    if quality.get("atomicity") != "verified" or quality.get("heading_clause_relation") != "separated":
        codes.append("unverified_atomicity")
    if not str(source.get("clause_th") or "").strip() or not evidence.get("source_refs"):
        codes.append("missing_exact_evidence")
    if evidence.get("source_span_sha256") != source.get("clause_sha256"):
        codes.append("stale_evidence_hash")
    if locale == "en" and (
        claim.get("english_status") != "approved" or not str(claim.get("answer_en") or "").strip()
    ):
        codes.append("missing_localization")

    effective_from = _parse_datetime(lifecycle.get("effective_from"))
    effective_to = _parse_datetime(lifecycle.get("effective_to"))
    if effective_from is not None and effective_at < effective_from:
        codes.append("not_yet_effective")
    if effective_to is not None and effective_at >= effective_to:
        codes.append("expired")
    if lifecycle.get("conflicts_with"):
        codes.append("unresolved_conflict")
    return tuple(dict.fromkeys(codes))


def select_eligible_claims(
    rows: Iterable[dict[str, Any]],
    *,
    release_id: str,
    game_id: str,
    facet: str,
    locale: str,
    effective_at: datetime | None = None,
) -> CompetitionClaimSelection:
    """Apply mandatory metadata/evidence gates before any semantic ranking."""
    when = effective_at or datetime.now(timezone.utc)
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    accepted: list[dict[str, Any]] = []
    rejected: list[ClaimRejection] = []
    for row in rows:
        codes = _claim_rejection_codes(
            row,
            release_id=release_id,
            game_id=game_id,
            facet=facet,
            locale=locale,
            effective_at=when,
        )
        if codes:
            rejected.append(ClaimRejection(str(row.get("claim_id") or ""), codes))
        else:
            accepted.append(row)
    return CompetitionClaimSelection(tuple(accepted), tuple(rejected))


def validate_sentence_attributions(
    payload: dict[str, Any],
    *,
    allowed_claim_ids: Iterable[str],
) -> SentenceAttributionValidation:
    """Ensure each factual answer sentence points only to selected claims."""
    allowed = {str(value) for value in allowed_claim_ids if str(value)}
    errors: list[str] = []
    used: list[str] = []
    sentences = payload.get("sentences")
    if not isinstance(sentences, list) or not sentences:
        return SentenceAttributionValidation(False, ("sentences_missing",), ())
    for index, sentence in enumerate(sentences):
        if not isinstance(sentence, dict):
            errors.append(f"sentence_{index}_not_object")
            continue
        text = str(sentence.get("text") or "").strip()
        claim_ids = sentence.get("claim_ids")
        factual_values = sentence.get("factual_values")
        if not text:
            errors.append(f"sentence_{index}_text_missing")
        if not isinstance(claim_ids, list):
            errors.append(f"sentence_{index}_claim_ids_invalid")
            continue
        normalized_ids = [str(value) for value in claim_ids if str(value)]
        has_factual_values = isinstance(factual_values, dict) and bool(factual_values)
        if has_factual_values and not normalized_ids:
            errors.append(f"sentence_{index}_factual_claim_missing")
        for claim_id in normalized_ids:
            if claim_id not in allowed:
                errors.append(f"sentence_{index}_claim_not_allowed:{claim_id}")
            else:
                used.append(claim_id)

    declared = payload.get("used_claim_ids")
    if not isinstance(declared, list):
        errors.append("used_claim_ids_invalid")
    else:
        declared_set = {str(value) for value in declared if str(value)}
        if declared_set != set(used):
            errors.append("used_claim_ids_mismatch")
    return SentenceAttributionValidation(
        not errors,
        tuple(errors),
        tuple(dict.fromkeys(used)),
    )


def question_requires_complete_list(query: str) -> bool:
    value = " ".join(str(query or "").casefold().split())
    signals = (
        "ทั้งหมด", "ครบทุก", "ทุกข้อ", "มีอะไรบ้าง", "รายการทั้งหมด",
        "all rules", "all penalties", "complete list", "every rule", "list all",
    )
    return any(signal in value for signal in signals)


def validate_completeness(
    query: str,
    selected_claims: Iterable[dict[str, Any]],
) -> CompletenessValidation:
    required = question_requires_complete_list(query)
    if not required:
        return CompletenessValidation(True, False, ())
    rows = tuple(selected_claims)
    if not rows:
        return CompletenessValidation(False, True, ("complete_list_evidence_missing",))
    complete_claims = [
        row for row in rows
        if isinstance(row.get("quality"), dict) and row["quality"].get("completeness") == "complete_list"
    ]
    if not complete_claims:
        return CompletenessValidation(False, True, ("selected_claims_are_not_a_verified_complete_list",))
    if not any((row.get("claim") or {}).get("structured_values") for row in complete_claims):
        return CompletenessValidation(False, True, ("complete_list_has_no_structured_rows",))
    return CompletenessValidation(True, True, ())


def numeric_tokens(value: str) -> tuple[str, ...]:
    """Extract factual numbers for conservative bilingual parity checks."""
    normalized = str(value or "").replace(",", "")
    return tuple(re.findall(r"(?<![A-Za-z])\d+(?:\.\d+)?(?:[:.]\d+)?", normalized))
