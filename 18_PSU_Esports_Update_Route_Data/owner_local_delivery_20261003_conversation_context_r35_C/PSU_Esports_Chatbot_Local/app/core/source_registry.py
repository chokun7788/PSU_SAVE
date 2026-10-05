from __future__ import annotations

from dataclasses import dataclass
from typing import Any


SERVICE_FEE_IMAGE_2026_ID = "service_fee_image_2026"
PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID = "pc_service_fee_local_update_20260727"


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    category: str
    title: str
    source_url: str
    source_type: str
    trust_level: str
    updated_at: str
    origin: str
    description: str


SOURCE_REGISTRY: dict[str, SourceRecord] = {
    SERVICE_FEE_IMAGE_2026_ID: SourceRecord(
        source_id=SERVICE_FEE_IMAGE_2026_ID,
        category="service_fee",
        title="Service Fee 2026",
        source_url="https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png",
        source_type="official_image",
        trust_level="official",
        updated_at="2026-01",
        origin="PSU Esports Studio - Phuket public service fee image",
        description="Official service fee image used for PS5, Nintendo Switch, Cockpit, and VR prices.",
    ),
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID: SourceRecord(
        source_id=PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
        category="service_fee",
        title="PC Service Fee Local Update 2026-07-27",
        source_url="local://service_fee/pc_price_update_20260727",
        source_type="local_fact_update",
        trust_level="user_confirmed",
        updated_at="2026-07-27",
        origin="User-provided PC service fee update in local chatbot maintenance session",
        description="PC price facts: PSU Student and Staff 0 THB, PSU Alumni/General Student 25 THB, General Adult 70 THB per 1 hour.",
    ),
}


def get_source(source_id: str) -> SourceRecord:
    try:
        return SOURCE_REGISTRY[source_id]
    except KeyError as exc:
        raise KeyError(f"unknown source_id: {source_id}") from exc


def make_source_hit(source_id: str) -> dict[str, Any]:
    source = get_source(source_id)
    return {
        "id": source.source_id,
        "metadata": {
            "source_url": source.source_url,
            "category": source.category,
            "title": source.title,
            "source_ids": [source.source_id],
            "source_type": source.source_type,
            "trust_level": source.trust_level,
            "updated_at": source.updated_at,
            "origin": source.origin,
            "description": source.description,
        },
    }


def make_source_hits(source_ids: list[str] | tuple[str, ...]) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source_id in source_ids:
        if source_id in seen:
            continue
        seen.add(source_id)
        hits.append(make_source_hit(source_id))
    return hits
