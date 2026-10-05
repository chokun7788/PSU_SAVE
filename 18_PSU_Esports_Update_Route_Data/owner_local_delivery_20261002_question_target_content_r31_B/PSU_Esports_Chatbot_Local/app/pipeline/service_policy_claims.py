from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


POLICY_PATH = Path(__file__).resolve().parents[2] / "data/curated/service_policy_answers.json"
ALLOWED_BASIS = {"site_explicit", "reviewer_interpretation_with_site_context"}


@dataclass(frozen=True)
class ServicePolicyAnswer:
    claim_id: str
    source_id: str
    source_url: str
    basis: str
    answer: str


@lru_cache(maxsize=1)
def _load_claims() -> tuple[str, dict]:
    data = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not str(data.get("source_url", "")).startswith("https://"):
        raise ValueError("invalid service policy registry")
    claims = data.get("claims")
    if not isinstance(claims, dict):
        raise ValueError("service policy claims must be an object")
    for claim_id, claim in claims.items():
        if claim.get("basis") not in ALLOWED_BASIS or not claim.get("source_id") or not claim.get("source_section") or not claim.get("evidence"):
            raise ValueError(f"invalid source provenance for {claim_id}")
        answers = claim.get("answers")
        if not isinstance(answers, dict) or not answers:
            raise ValueError(f"missing answers for {claim_id}")
        for variant, languages in answers.items():
            if not isinstance(languages, dict) or any(not str(languages.get(locale, "")).strip() for locale in ("th", "en")):
                raise ValueError(f"missing bilingual answer for {claim_id}/{variant}")
    return data["source_url"], claims


def get_service_policy_answer(claim_id: str, *, locale: str, variant: str = "general", service: str = "") -> ServicePolicyAnswer | None:
    source_url, claims = _load_claims()
    claim = claims.get(claim_id)
    if claim is None:
        return None
    answer = claim["answers"].get(variant, {}).get("en" if locale == "en" else "th")
    if not answer:
        return None
    return ServicePolicyAnswer(
        claim_id=claim_id,
        source_id=claim["source_id"],
        source_url=source_url,
        basis=claim["basis"],
        answer=answer.replace("{service}", service),
    )
