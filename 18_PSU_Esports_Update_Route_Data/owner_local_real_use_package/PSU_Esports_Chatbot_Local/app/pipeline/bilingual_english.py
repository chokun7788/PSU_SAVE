from __future__ import annotations

import json
import math
import os
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.calculator.service_fee import SERVICE_FEES, SOURCE_URL
from app.calendar.service_calendar import closure_for, holidays_for_date, regular_service_slots, today_bangkok
from app.core.normalization import normalize_text
from app.core.source_registry import (
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
)
from app.knowledge.localization import approved_localization, localization_status
from app.knowledge.english_retrieval import retrieve_approved_english
from app.pipeline.formatter import format_no_answer
from app.pipeline.schemas import EntityBundle, PipelineRoute, ValidationResult
from app.rules.matcher import RuleMatcher


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"
COMPETITION_RULES_DIR = ROOT / "data" / "competition_rules"
HOME_URL = "https://esports.phuket.psu.ac.th/home"
OUR_GAMES_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
MEMBERS_URL = "https://esports.phuket.psu.ac.th/about-us/Members"
RESERVATION_URL = "https://esports.computing.psu.ac.th/"

_TOKEN_RE = re.compile(r"[a-z0-9]+(?:'[a-z]+)?", flags=re.IGNORECASE)
_DAY_TOKENS = {
    "monday": 0,
    "mon": 0,
    "tuesday": 1,
    "tue": 1,
    "wednesday": 2,
    "wed": 2,
    "thursday": 3,
    "thu": 3,
    "friday": 4,
    "fri": 4,
    "saturday": 5,
    "sat": 5,
    "sunday": 6,
    "sun": 6,
}
_GROUP_LABELS_EN = {
    "psu_student_staff": "PSU students and staff",
    "general_student": "PSU alumni and students from other institutions",
    "general_adult": "General adults",
}


@dataclass(frozen=True)
class EnglishSupportResult:
    answer: str
    hits: list[dict[str, Any]]
    mode: str
    confidence: float
    route: PipelineRoute
    validation: ValidationResult


def requires_english_intent_review(result: EnglishSupportResult) -> bool:
    """Whether Local LLM should review English phrasing before verified rendering."""
    enabled = os.getenv("PSU_ENGLISH_STRUCTURED_INTENT_REVIEW", "1").strip().lower()
    if enabled not in {"1", "true", "yes", "y", "on"}:
        return False
    exact_modes = {
        # A rule match already has a reviewed English answer and source. Sending
        # it to intent review only adds Local LLM latency without changing facts.
        "pipeline:rule_en",
        "pipeline:structured_service_fee_en",
        "pipeline:structured_schedule_en",
        "pipeline:structured_games_catalog_en",
        "pipeline:structured_games_count_en",
        "pipeline:structured_game_availability_en",
        "pipeline:structured_equipment_catalog_en",
        "pipeline:structured_equipment_item_en",
        "pipeline:structured_game_controls_en",
        "pipeline:structured_game_detail_en",
        "pipeline:structured_competition_rules_en",
        "pipeline:structured_members_source_th",
        "pipeline:game_controls_no_source_en",
        "pipeline:game_controls_mapping_pending_en",
        "pipeline:chatbot_identity_en",
        "pipeline:chatbot_greeting_en",
        "pipeline:english_no_answer",
        "pipeline:missing_english_localization",
    }
    return result.mode not in exact_modes


def english_no_answer_needs_domain_recovery(query: str) -> bool:
    """Keep Local LLM review for plausible PSU wording, not unrelated chat.

    An unknown phrase with no studio signal previously spent the full intent
    timeout before returning the exact same safe no-answer.  Broad but
    plausible requests (for example informal booking/price/game wording) keep
    their bounded model opportunity.
    """
    tokens = _tokens(query)
    return bool(tokens & {
        "book", "booking", "reserve", "reservation", "cancel", "payment",
        "pay", "price", "fee", "game", "games", "play", "equipment",
        "zone", "pc", "ps5", "switch", "vr", "open", "close", "hours",
        "schedule", "rule", "rules", "member", "staff", "contact", "studio",
        "esports", "psu",
    })


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


@lru_cache(maxsize=1)
def _availability_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "service_game_availability.jsonl"))


def _format_game_catalog(rows: list[dict[str, Any]], zone: str | None = None) -> str:
    """Render the shared game catalogue with the same scan-friendly shape as Thai."""
    grouped: dict[str, list[str]] = {}
    for row in rows:
        zone_name = str(row.get("zone") or "Unknown zone")
        grouped.setdefault(zone_name, []).extend(
            str(game_name) for game_name in row.get("games") or []
        )

    unique_games = {
        game_name.casefold()
        for games in grouped.values()
        for game_name in games
    }
    if zone:
        intro = f"There are currently {len(unique_games)} verified games in {zone}."
    else:
        intro = f"There are currently {len(unique_games)} verified games available."

    lines = [intro]
    for zone_name, games in grouped.items():
        ordered_games = sorted(dict.fromkeys(games), key=str.casefold)
        game_label = "game" if len(ordered_games) == 1 else "games"
        lines.extend(("", f"{zone_name} ({len(ordered_games)} {game_label})"))
        lines.extend(f"•    {game_name}" for game_name in ordered_games)
    lines.append(f"Source: {OUR_GAMES_URL} (original source in Thai)")
    return "\n".join(lines)


@lru_cache(maxsize=1)
def _game_detail_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "game_item_details.jsonl"))


@lru_cache(maxsize=1)
def _equipment_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "equipment_item_details.jsonl"))


@lru_cache(maxsize=1)
def _member_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "member_profiles.jsonl"))


@lru_cache(maxsize=1)
def _competition_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(COMPETITION_RULES_DIR / "competition_rule_chunks.jsonl"))


@lru_cache(maxsize=1)
def _control_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "game_control_facts.jsonl"))


def _hit(source_id: str, category: str, url: str, title: str = "") -> dict[str, Any]:
    return {
        "id": source_id,
        "metadata": {
            "source_url": url,
            "category": category,
            "source_type": category,
            "title": title or source_id,
            "source_ids": [source_id],
            "source_language": "th",
        },
    }


def _route(category: str, intent: str, confidence: float, reason: str, answer_type: str = "fact") -> PipelineRoute:
    return PipelineRoute(category, intent, confidence, answer_type, "low", reason)


def _result(
    answer: str,
    *,
    category: str,
    intent: str,
    mode: str,
    confidence: float,
    hits: list[dict[str, Any]],
    reason: str,
    warnings: tuple[str, ...] = (),
    answer_type: str = "fact",
) -> EnglishSupportResult:
    return EnglishSupportResult(
        answer=answer,
        hits=hits,
        mode=mode,
        confidence=confidence,
        route=_route(category, intent, confidence, reason, answer_type),
        validation=ValidationResult(ok=True, warnings=warnings),
    )


def _tokens(query: str) -> set[str]:
    # Keep accented game titles as one token.  Without accent folding,
    # ``Pokémon`` was split into ``pok`` and ``mon``; ``mon`` then matched the
    # Monday abbreviation and sent a controls question to the schedule route.
    folded = "".join(
        char
        for char in unicodedata.normalize("NFKD", query or "")
        if not unicodedata.combining(char)
    )
    return {token.lower() for token in _TOKEN_RE.findall(folded)}


def _phrase(query: str, phrase: str) -> bool:
    q = re.sub(r"\s+", " ", normalize_text(query)).strip()
    escaped = re.escape(normalize_text(phrase)).replace(r"\ ", r"\s+")
    return bool(re.search(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", q, flags=re.IGNORECASE))


def _source_suffix(url: str) -> str:
    return f"\nSource: {url} (original source in Thai)"


def _game_title_key(value: object) -> str:
    """Compare game titles independent of accents and display punctuation."""
    decomposed = unicodedata.normalize("NFKD", str(value or ""))
    plain = "".join(char for char in decomposed if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "", plain.casefold())


def _compact_english_excerpt(text: str, *, limit: int = 360) -> str:
    """Keep a preview answer readable without cutting a sentence mid-way."""
    clean = re.sub(r"\s+", " ", text or "").strip()
    if len(clean) <= limit:
        return clean
    visible = clean[:limit]
    sentence_ends = list(re.finditer(r"[.!?](?=\s|$)", visible))
    if sentence_ends:
        return visible[: sentence_ends[-1].end()].strip()
    return visible.rsplit(" ", 1)[0].strip() + "..."


def _rule_answer(query: str, matcher: RuleMatcher) -> EnglishSupportResult | None:
    matched = matcher.match(query, locale="en")
    if matched is None:
        return None
    answer = str(matched.get("answer") or "").strip()
    if not answer:
        return None
    url = str(matched.get("source_url") or "").strip()
    if url and "Source:" not in answer:
        answer += _source_suffix(url)
    category = str(matched.get("category") or "general")
    return _result(
        answer,
        category=category,
        intent=str(matched.get("intent") or "rule_match"),
        mode="pipeline:rule_en",
        confidence=0.99,
        hits=[_hit(str(matched.get("rule_id") or "rule"), category, url, str(matched.get("rule_id") or "rule"))] if url else [],
        reason=f"approved bilingual rule {matched.get('rule_id')}",
    )


def _detect_service(query: str, entities: EntityBundle) -> str | None:
    tokens = _tokens(query)
    q = normalize_text(query)
    if entities.service:
        return entities.service
    if "pc" in tokens or "computer" in tokens:
        return "pc"
    if "ps5" in tokens or _phrase(q, "playstation 5") or "playstation" in tokens:
        return "ps5"
    if "nintendo" in tokens or "switch" in tokens:
        return "nintendo_switch"
    if "cockpit" in tokens or _phrase(q, "racing wheel"):
        return "cockpit"
    if "vr" in tokens or "psvr2" in tokens:
        return "vr"
    return None


def _services_for_game(game: str) -> tuple[str, ...]:
    """Resolve a game's bookable service only from verified availability rows."""
    zone_to_service = {
        "pc zone": "pc",
        "playstation 5 zone": "ps5",
        "nintendo switch zone": "nintendo_switch",
        "cockpit zone": "cockpit",
        "vr zone": "vr",
    }
    def compact(value: object) -> str:
        return re.sub(r"[^a-z0-9]+", "", normalize_text(str(value or "")))

    def matches_verified_title(candidate: object) -> bool:
        candidate_key = compact(candidate)
        game_key = compact(game)
        return bool(candidate_key and game_key and candidate_key == game_key)

    services: list[str] = []
    for row in _availability_rows():
        if not any(matches_verified_title(candidate) for candidate in row.get("games") or []):
            continue
        service = zone_to_service.get(normalize_text(str(row.get("zone") or "")))
        if service and service not in services:
            services.append(service)
    # Some profile records combine editions while the booking catalog lists
    # them separately. A verified profile zone is a safe service fallback.
    if not services:
        detail = next(
            (
                row for row in _game_detail_rows()
                if compact(row.get("game") or row.get("title")) == compact(game)
            ),
            None,
        )
        for zone in (detail or {}).get("zones") or []:
            service = zone_to_service.get(normalize_text(str(zone)))
            if service and service not in services:
                services.append(service)
    return tuple(services)


def _detect_group(query: str) -> str | None:
    q = normalize_text(query)
    if _phrase(q, "psu student") or _phrase(q, "psu staff") or _phrase(q, "psu personnel"):
        return "psu_student_staff"
    if "alumni" in _tokens(q) or _phrase(q, "external student") or _phrase(q, "other university"):
        return "general_student"
    if _phrase(q, "general adult") or _phrase(q, "general public") or "adult" in _tokens(q):
        return "general_adult"
    if "student" in _tokens(q):
        return "general_student"
    return None


def _duration_minutes(query: str) -> int | None:
    q = normalize_text(query)
    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
    }
    hour = re.search(r"\b(\d+(?:\.\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s*(?:hours?|hrs?)\b", q)
    if hour:
        raw = hour.group(1)
        hours = float(number_words[raw]) if raw in number_words else float(raw)
        return int(hours * 60)
    minute = re.search(r"\b(\d+)\s*(?:minutes?|mins?)\b", q)
    if minute:
        return int(minute.group(1))
    if _phrase(q, "one hour") or _phrase(q, "an hour"):
        return 60
    if _phrase(q, "half hour") or _phrase(q, "half an hour"):
        return 30
    return None


def _people(query: str) -> int | None:
    match = re.search(r"\b(\d+)\s*(?:people|persons?|players?)\b", normalize_text(query))
    return int(match.group(1)) if match else None


def _price_package_keys(service: str, query: str) -> list[str]:
    minutes = _duration_minutes(query)
    people = _people(query)
    if service == "vr":
        if minutes is None:
            return ["vr_30", "vr_60"]
        return ["vr_30" if minutes <= 30 else "vr_60"]
    if service == "nintendo_switch":
        if people is None:
            return ["nintendo_switch_1_2", "nintendo_switch_3_4"]
        return ["nintendo_switch_3_4" if people >= 3 else "nintendo_switch_1_2"]
    return [{"pc": "pc", "ps5": "ps5", "cockpit": "cockpit"}[service]]


def _answer_price(query: str, entities: EntityBundle) -> EnglishSupportResult | None:
    tokens = _tokens(query)
    comparison_signal = bool(tokens & {"expensive", "cheaper", "cheapest", "difference", "differences", "different", "compare", "comparison"})
    control_signal = bool(tokens & {"button", "buttons", "key", "keys", "controller", "controllers", "control", "controls"})
    explicit_price_signal = bool(tokens & {
        "price", "cost", "fee", "charge", "charges", "pay", "free", "much",
        "expensive", "cheaper", "cheapest",
    })
    # ``comparison`` on its own is common in game-control questions. Treat it
    # as a fee comparison only when the question also names billable services.
    service_comparison = (
        comparison_signal
        and not control_signal
        and bool(tokens & {"pc", "ps5", "playstation", "nintendo", "switch", "cockpit", "vr"})
    )
    price_signal = explicit_price_signal or service_comparison or entities.price_intent
    service = _detect_service(query, entities)
    game = _known_game(query) if price_signal else None
    if price_signal and not service and game:
        compatible_services = _services_for_game(game)
        if len(compatible_services) == 1:
            service = compatible_services[0]
        elif len(compatible_services) > 1:
            options = ", ".join({
                "pc": "PC",
                "ps5": "PlayStation 5",
                "nintendo_switch": "Nintendo Switch",
                "cockpit": "Cockpit",
                "vr": "VR",
            }[item] for item in compatible_services)
            return _result(
                f"{game} is available on more than one service ({options}). Which service and duration should I price?"
                + _source_suffix(RESERVATION_URL),
                category="service_fee",
                intent="service_fee_query",
                mode="pipeline:price_service_clarification_en",
                confidence=0.96,
                hits=[_hit("service_game_availability", "games", RESERVATION_URL, game)],
                reason="game title maps to multiple verified billable services",
                answer_type="clarification",
            )
    if not price_signal or not service:
        return None
    package_keys = _price_package_keys(service, query)
    if service == "vr" and comparison_signal:
        package_keys = ["vr_30", "vr_60"]
    group = _detect_group(query)
    requested_minutes = _duration_minutes(query)
    lines: list[str] = []
    for package_key in package_keys:
        fee = SERVICE_FEES[package_key]
        sessions = max(1, math.ceil(requested_minutes / int(fee["minutes_per_session"]))) if requested_minutes else 1
        unit = "30 minutes" if int(fee["minutes_per_session"]) == 30 else "1 hour"
        capacity = str(fee["capacity"]).replace("คน", "people")
        lines.append(f"{fee['label']} - {unit} ({capacity})")
        groups = [group] if group else ["psu_student_staff", "general_student", "general_adult"]
        for group_key in groups:
            base_price = int(fee["prices"][group_key])
            total = base_price * sessions
            calculation = f" ({base_price:,} THB x {sessions} sessions)" if sessions > 1 else ""
            lines.append(f"- {_GROUP_LABELS_EN[group_key]}: {total:,} THB{calculation}")
        if requested_minutes:
            lines.append(f"- Requested duration: {requested_minutes} minutes, charged as {sessions} session(s).")
    if len(package_keys) > 1:
        missing = "duration" if service == "vr" else "number of players"
        lines.insert(0, f"The question does not specify the {missing}, so both verified packages are shown.")
    lines.append("Prices are calculated deterministically from the Service Fee 2026 table.")
    lines.append(f"Source: {SOURCE_URL} (original source in Thai)")
    source_ids = [SERVICE_FEE_IMAGE_2026_ID]
    if service == "pc":
        source_ids.append(PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID)
    return _result(
        "\n".join(lines),
        category="service_fee",
        intent="service_fee_query",
        mode="pipeline:structured_service_fee_en",
        confidence=0.98 if group else 0.90,
        hits=[_hit(source_id, "service_fee", SOURCE_URL, "Service Fee 2026") for source_id in source_ids],
        reason="shared deterministic service fee record with English template",
        answer_type="calculation" if requested_minutes else "fact",
    )


def _weekday_from_query(query: str, entities: EntityBundle) -> int | None:
    tokens = _tokens(query)
    # Entity extraction is shared with Thai and may retain a legacy substring
    # match (for example ``mon`` inside an accented game title).  Only trust
    # its weekday value after the current English tokenization independently
    # sees an explicit day word.
    if entities.day and any(day in tokens for day in _DAY_TOKENS):
        return {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4}.get(entities.day)
    for token, weekday in _DAY_TOKENS.items():
        if token in tokens:
            return weekday
    if "today" in tokens:
        return today_bangkok().weekday()
    if "tomorrow" in tokens:
        return (today_bangkok().weekday() + 1) % 7
    return None


def _schedule_summary(weekday: int) -> str:
    if weekday == 0:
        return "Monday: 09:00-12:00 is maintenance; the studio is open for play from 13:00-16:00."
    if weekday in {1, 2, 3}:
        name = ("Tuesday", "Wednesday", "Thursday")[weekday - 1]
        return f"{name}: the studio is open from 09:00-12:00 and 13:00-16:00."
    if weekday == 4:
        return "Friday: the studio is open from 09:00-12:00; 13:00-16:00 is maintenance."
    name = "Saturday" if weekday == 5 else "Sunday"
    return f"{name}: no regular service period is listed. Please confirm with the studio before travelling."


_WEEKDAY_NAMES_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def _english_date_label(value: date) -> str:
    return f"{_WEEKDAY_NAMES_EN[value.weekday()]}, {value.strftime('%d/%m/%Y')}"


def _english_holiday_context(value: date) -> str:
    holidays = holidays_for_date(value)
    if not holidays:
        return "No Thai public holiday or recorded calendar festival was found for this date."
    lines = []
    for holiday in holidays:
        title = str(getattr(holiday, "title", "") or "Thai calendar entry")
        kind = str(getattr(holiday, "type", "") or "calendar entry")
        lines.append(f"•    {title} ({kind}; original entry may be in Thai)")
    return "\n".join(lines)


def _date_aware_schedule_text(target: date, *, relative_label: str) -> str:
    """Render the same calendar facts as Thai, with an approved English template."""
    display_date = _english_date_label(target)
    reference_date = _english_date_label(today_bangkok())
    closure = closure_for(target)
    if closure and closure.status == "closed":
        headline = f"{relative_label}, {display_date}: the studio is closed due to a registered special closure."
        closure_detail = "A special closure overrides the regular service schedule."
    else:
        slots = regular_service_slots(target)
        if not slots:
            headline = f"{relative_label}, {display_date}: no regular service period is listed."
            closure_detail = "Please confirm with the studio before travelling or making a booking."
        else:
            slot_lines: list[str] = []
            for slot in slots:
                period = str(slot.get("time_range") or "")
                if slot.get("state") == "open":
                    slot_lines.append(f"{period} is open for play and booking")
                else:
                    slot_lines.append(
                        f"{period} is a maintenance period for equipment inspection and cleaning; play and booking are unavailable"
                    )
            headline = f"{relative_label}, {display_date}: " + "; ".join(slot_lines) + "."
            closure_detail = ""

    lines = [
        headline,
        closure_detail,
        f"System reference date: today is {reference_date} (Asia/Bangkok).",
        "",
        "Thai calendar for this date:",
        _english_holiday_context(target),
        "",
        "Regular schedule details:",
        "•    Monday 09:00-12:00 is maintenance; 13:00-16:00 is open for play.",
        "•    Tuesday-Thursday are open from 09:00-12:00 and 13:00-16:00.",
        "•    Friday 09:00-12:00 is open; 13:00-16:00 is maintenance.",
        "•    A registered public-holiday or special-closure record takes precedence over the regular schedule.",
    ]
    return "\n".join(line for line in lines if line)


def _answer_schedule(query: str, entities: EntityBundle) -> EnglishSupportResult | None:
    tokens = _tokens(query)
    signal = bool(tokens & {"open", "opening", "close", "closing", "hours", "schedule", "time", "maintenance", "morning", "afternoon", "today", "tomorrow"})
    weekday = _weekday_from_query(query, entities)
    if not signal and weekday is None:
        return None
    target_date: date | None = None
    relative_label = ""
    if "today" in tokens:
        target_date = today_bangkok()
        relative_label = "Today"
    elif "tomorrow" in tokens:
        from datetime import timedelta

        target_date = today_bangkok() + timedelta(days=1)
        relative_label = "Tomorrow"

    if target_date is not None:
        text = _date_aware_schedule_text(target_date, relative_label=relative_label)
    elif weekday is None and (re.search(r"\b24\s*(?:hours?|hrs?)\b", normalize_text(query)) or _phrase(query, "24/7")):
        text = "The studio is not open 24 hours. Regular service periods are listed between 09:00 and 16:00 on weekdays, with maintenance periods on Monday morning and Friday afternoon."
    elif weekday is None and "morning" in tokens:
        text = "The morning service period is 09:00-12:00. Monday morning is reserved for maintenance."
    elif weekday is None and "afternoon" in tokens:
        text = "The afternoon service period is 13:00-16:00. Friday afternoon is reserved for maintenance."
    elif weekday is None:
        text = (
            "Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. "
            "Please specify a day for the exact play window."
        )
    else:
        text = _schedule_summary(weekday)
        if "morning" in tokens:
            if weekday == 0:
                text = "Monday morning, 09:00-12:00, is a maintenance period and is not a regular play session."
            elif weekday == 4:
                text = "Friday morning is open for play from 09:00-12:00."
        elif "afternoon" in tokens:
            if weekday == 4:
                text = "Friday afternoon, 13:00-16:00, is a maintenance period and is not a regular play session."
            elif weekday == 0:
                text = "Monday afternoon is open for play from 13:00-16:00."
    text += _source_suffix(RESERVATION_URL)
    return _result(
        text,
        category="schedule",
        intent="schedule_query",
        mode="pipeline:structured_schedule_en",
        confidence=0.98,
        hits=[_hit("service_schedule", "schedule", RESERVATION_URL, "Service schedule")],
        reason="token-aware weekday and shared service calendar",
    )


def _answer_booking_intent(query: str, matcher: RuleMatcher) -> EnglishSupportResult | None:
    """Bridge natural English booking verbs to the approved booking FAQ.

    The rule file deliberately keeps a small exact pattern set. This handler
    accepts ordinary wording such as ``how do I book PC`` but renders the same
    verified booking procedure; it never creates a reservation or a price.
    """
    tokens = _tokens(query)
    booking_signal = bool(tokens & {"book", "booking", "reserve", "reservation"})
    payment_signal = bool(tokens & {"pay", "payment", "paid", "minutes", "minute"})
    cancellation_signal = bool(tokens & {"cancel", "cancellation", "modify", "change", "edit", "walk"})
    # These are intent patterns, rendered by the existing approved rule rather
    # than an ad-hoc English answer. They cover natural questions whose wording
    # does not happen to reproduce the rule-file regex exactly.
    if payment_signal and (booking_signal or _phrase(query, "after booking")):
        return _rule_answer("payment timeout", matcher)
    if tokens & {"modify", "change", "edit"} and booking_signal:
        return _rule_answer("edit booking", matcher)
    if cancellation_signal and booking_signal:
        return _rule_answer("cancel advance", matcher)
    if tokens & {"summarize", "summary", "steps", "step"} and booking_signal:
        return _rule_answer("How do I make a booking?", matcher)
    if "advance" in tokens and booking_signal:
        return _rule_answer("booking advance", matcher)
    if "advance" in tokens and _phrase(query, "check in") and _known_game(query) is None:
        return _rule_answer("booking advance", matcher)
    if _phrase(query, "arrive late") and _known_game(query) is None and not _competition_target(query):
        return _rule_answer("late check in", matcher)
    if tokens & {"cancel", "cancellation"} and _known_game(query) is None and not _competition_target(query):
        return _rule_answer("cancel advance", matcher)
    if "walk" in tokens and "in" in tokens and _known_game(query) is None:
        return _rule_answer("booking advance", matcher)
    if tokens & {"slip", "receipt"} and (booking_signal or tokens & {"attach", "upload"}):
        return _rule_answer("user info slip", matcher)
    excluded = {
        "cancel", "cancellation", "change", "modify", "payment", "pay",
        "refund", "checkin", "check", "in", "status", "slot", "available",
    }
    if not booking_signal or tokens & excluded:
        return None
    if not any(token in tokens for token in {"how", "can", "do", "want", "need", "make"}):
        return None
    return _rule_answer("How do I make a booking?", matcher)


@lru_cache(maxsize=1)
def _game_aliases() -> tuple[tuple[str, str], ...]:
    aliases: dict[str, str] = {}
    for row in _game_detail_rows():
        game = str(row.get("game") or row.get("title") or "").strip()
        for value in [game, *(row.get("aliases") or [])]:
            alias = normalize_text(str(value or "")).strip()
            if alias:
                aliases.setdefault(alias, game)
    for row in _availability_rows():
        for game in row.get("games") or []:
            alias = normalize_text(str(game)).strip()
            aliases.setdefault(alias, str(game))
    return tuple(sorted(aliases.items(), key=lambda item: len(item[0]), reverse=True))


def _known_game(query: str) -> str | None:
    q = normalize_text(query)
    for alias, game in _game_aliases():
        escaped = re.escape(alias).replace(r"\ ", r"\s+")
        if re.search(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", q, flags=re.IGNORECASE):
            return game
    return None


def _unknown_game_candidate(query: str) -> str | None:
    patterns = (
        r"\b(?:an?\s+)?(?:unknown\s+)?game\s+called\s+(.+?)(?:[?.]|$)",
        r"\bis\s+(.+?)\s+(?:available|installed|supported)\b",
        r"\bdo\s+you\s+have\s+(.+?)(?:\?|$)",
        r"\bcan\s+i\s+play\s+(.+?)(?:\s+(?:at|on|in)\b|\?|$)",
        r"\bwhere\s+can\s+i\s+play\s+(.+?)(?:\?|$)",
    )
    q = re.sub(r"\s+", " ", query or "").strip()
    for pattern in patterns:
        match = re.search(pattern, q, flags=re.IGNORECASE)
        if not match:
            continue
        candidate = match.group(1).strip(" ?.,")
        if candidate and candidate.lower() not in {"it", "this", "games", "a game", "pc", "vr"}:
            return candidate
    return None


def _zone_filter(query: str, entities: EntityBundle) -> str | None:
    service = _detect_service(query, entities)
    return {
        "pc": "PC Zone",
        "ps5": "PlayStation 5 Zone",
        "nintendo_switch": "Nintendo Switch Zone",
        "cockpit": "Cockpit Zone",
        "vr": "VR Zone",
    }.get(service or "")


def _game_availability_answer(game: str) -> EnglishSupportResult:
    matches = [row for row in _availability_rows() if game in (row.get("games") or [])]
    def english_label(row: dict[str, Any]) -> str:
        label = str(row.get("service_label") or row.get("zone") or "")
        label = re.sub(r"(\d+)\s*นาที", lambda match: f"{match.group(1)} minutes", label)
        label = re.sub(r"1\s*ชั่วโมง", "1 hour", label)
        label = re.sub(r"(\d+)\s*ชั่วโมง", lambda match: f"{match.group(1)} hours", label)
        label = re.sub(r"(\d+(?:-\d+)?)\s*คน", lambda match: f"{match.group(1)} people", label)
        return label

    labels = list(dict.fromkeys(english_label(row) for row in matches))
    if not matches:
        return _result(
            f"I could not find {game} in the verified PSU game records. I will not substitute another game." + _source_suffix(RESERVATION_URL),
            category="games",
            intent="unknown_game",
            mode="pipeline:games_unknown_target_en",
            confidence=0.99,
            hits=[_hit("service_game_availability", "games", RESERVATION_URL, "Game availability")],
            reason="exact game target absent from verified catalog",
            warnings=("unknown_game_target",),
            answer_type="no_answer",
        )
    return _result(
        f"{game} is available on: {', '.join(labels)}." + _source_suffix(RESERVATION_URL),
        category="games",
        intent="game_availability",
        mode="pipeline:structured_game_availability_en",
        confidence=0.99,
        hits=[_hit(str(row.get("id")), "games", str(row.get("source_url") or RESERVATION_URL), game) for row in matches],
        reason="exact game title matched shared availability records",
    )


def _answer_game_controls(query: str, game: str, *, route_intent: str = "") -> EnglishSupportResult | None:
    tokens = _tokens(query)
    if not (tokens & {"button", "buttons", "control", "controls", "controller", "key", "keys", "press"}) and "control" not in route_intent:
        return None
    game_key = _game_title_key(game)
    game_rows = [
        row
        for row in _control_rows()
        if _game_title_key(row.get("game")) == game_key
    ]
    rows = [row for row in game_rows if row.get("button") and row.get("action_en")]
    if not rows:
        if not game_rows:
            return _result(
                f"I could not find a verified control mapping for {game}. I will not reuse controls from a different game."
                + _source_suffix(OUR_GAMES_URL),
                category="games",
                intent="game_control_lookup",
                mode="pipeline:game_controls_no_source_en",
                confidence=0.98,
                hits=[_hit("game_controls", "game_controls", OUR_GAMES_URL, game)],
                reason="the verified control catalog has no source mapping for the requested game",
                answer_type="no_answer",
            )
        unavailable = next(
            (row for row in game_rows if str(row.get("coverage_status") or "").startswith("mapping_unavailable")),
            None,
        )
        if unavailable is not None:
            url = str(unavailable.get("source_url") or OUR_GAMES_URL)
            return _result(
                f"A verified default button map for {game} has not been published in the knowledge base yet. "
                "The source confirms the game/support page, but not a button-by-button layout, so I will not guess the controls."
                + f"\nSource: {url}",
                category="games",
                intent="game_control_lookup",
                mode="pipeline:game_controls_mapping_pending_en",
                confidence=0.98,
                hits=[_hit(str(unavailable.get("id") or "game_controls"), "game_controls", url, game)],
                reason="source is present but does not provide a verified default button mapping",
                warnings=("control_mapping_pending_staff_capture",),
                answer_type="no_answer",
            )
        return _result(
            format_no_answer("game controls", "en", missing_translation=True) + _source_suffix(OUR_GAMES_URL),
            category="games",
            intent="game_control_lookup",
            mode="pipeline:missing_english_localization",
            confidence=0.95,
            hits=[_hit("game_controls", "game_controls", OUR_GAMES_URL, game)],
            reason="no approved English control mapping",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )

    def english_button_label(value: Any) -> str:
        # The control dataset preserves source labels such as
        # ``Cross (กากบาท)``. Keep the actual button while removing Thai-only
        # explanatory parentheses so the English answer contract is not vetoed.
        text = str(value or "").strip()
        text = re.sub(r"\s*\([^)]*[\u0E00-\u0E7F][^)]*\)", "", text)
        return re.sub(r"\s+", " ", text).strip()

    lines = [f"{game} controls:"]
    for row in rows[:20]:
        lines.append(f"- {english_button_label(row['button'])}: {row['action_en']}")
    if len(rows) > 20:
        lines.append(f"- ...and {len(rows) - 20} more verified mappings.")
    url = str(rows[0].get("source_url") or OUR_GAMES_URL)
    lines.append(f"Source: {url}")
    return _result(
        "\n".join(lines),
        category="games",
        intent="game_control_lookup",
        mode="pipeline:structured_game_controls_en",
        confidence=0.96,
        hits=[_hit(str(rows[0].get("id")), "game_controls", url, game)],
        reason="existing curated action_en fields",
    )


def _answer_game_detail(game: str) -> EnglishSupportResult:
    row = next((item for item in _game_detail_rows() if str(item.get("game") or item.get("title") or "").casefold() == game.casefold()), None)
    if row is None:
        return _game_availability_answer(game)
    summary = approved_localization(row, "summary_th")
    how_to = approved_localization(row, "how_to_play_th")
    genre = approved_localization(row, "genre")
    missing_fields = [field for field, value in (("summary_th", summary), ("how_to_play_th", how_to), ("genre", genre)) if value is None]
    url = str(row.get("source_url") or OUR_GAMES_URL)
    if missing_fields:
        statuses = ", ".join(f"{field}={localization_status(row, field)}" for field in missing_fields)
        return _result(
            format_no_answer("game details", "en", missing_translation=True) + _source_suffix(url),
            category="games",
            intent="game_detail_lookup",
            mode="pipeline:missing_english_localization",
            confidence=0.99,
            hits=[_hit(str(row.get("id")), "games", url, game)],
            reason=f"English localization unavailable: {statuses}",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )
    zones = ", ".join(str(value) for value in row.get("zones") or [])
    is_draft_preview = any(
        localization_status(row, field) == "draft_preview"
        for field in ("summary_th", "how_to_play_th", "genre")
    )
    heading = "English draft translation (based on the verified Thai record):" if is_draft_preview else "Verified English information:"
    text = f"{heading}\n{game}\nGenre: {genre}\nOverview: {summary}\nHow to play: {how_to}\nAvailable at: {zones}" + _source_suffix(url)
    return _result(
        text,
        category="games",
        intent="game_detail_lookup",
        mode="pipeline:structured_game_detail_en",
        confidence=0.98,
        hits=[_hit(str(row.get("id")), "games", url, game)],
        reason="draft English localization matched current Thai source hash" if is_draft_preview else "approved localization overlay matched current Thai source hash",
        warnings=("english_draft_preview",) if is_draft_preview else (),
    )


def _answer_games(query: str, entities: EntityBundle, *, route: PipelineRoute) -> EnglishSupportResult | None:
    tokens = _tokens(query)
    game = _known_game(query)
    if game:
        # A named game normally means game availability/details. Competition
        # vocabulary is the explicit exception, so a broad route label cannot
        # turn "Tell me about VALORANT" into a tournament-rule lookup.
        if _is_competition_query(query, route):
            return None
        controls = _answer_game_controls(query, game, route_intent=route.intent)
        if controls is not None:
            return controls
        if (
            tokens & {"what", "genre", "about", "describe", "details", "detail"}
            or _phrase(query, "how to play")
            or _phrase(query, "how do i play")
            or _phrase(query, "how can i play")
            or "detail" in route.intent
        ):
            return _answer_game_detail(game)
        return _game_availability_answer(game)
    if _phrase(query, "across multiple zones") or _phrase(query, "in multiple zones"):
        zones_by_game: dict[str, set[str]] = {}
        for row in _availability_rows():
            zone = str(row.get("zone") or "")
            for title in row.get("games") or []:
                zones_by_game.setdefault(str(title), set()).add(zone)
        shared = sorted(
            (title, sorted(zones))
            for title, zones in zones_by_game.items()
            if len(zones) > 1
        )
        if shared:
            lines = ["Verified games available in multiple zones:"]
            lines.extend(f"- {title}: {', '.join(zones)}" for title, zones in shared)
            lines.append(_source_suffix(RESERVATION_URL).strip())
            return _result(
                "\n".join(lines),
                category="games",
                intent="game_multi_zone_lookup",
                mode="pipeline:structured_games_multi_zone_en",
                confidence=0.98,
                hits=[_hit("service_game_availability", "games", RESERVATION_URL, "multi-zone")],
                reason="verified availability records grouped by canonical game title and distinct zone",
            )
    # Support natural short questions such as "what game u have" without
    # treating a specific-title question (for example "what game is Beat
    # Saber?") as a request for the entire catalog.
    count_signal = bool(re.search(r"\bhow\s+many\s+games?\b", query, flags=re.IGNORECASE)) or bool(re.search(
        r"\b(?:number|count)\s+of\s+games?\b", query, flags=re.IGNORECASE
    ))
    catalog_signal = (
        count_signal
        or bool(tokens & {"games", "catalog", "titles"})
        or _phrase(query, "which games")
        or _phrase(query, "what games")
        or _phrase(query, "available games")
        or bool(re.search(
            r"\bwhat\s+games?\s+(?:do\s+)?(?:you|u)\s+hav+e\b",
            query,
            flags=re.IGNORECASE,
        ))
        or bool(re.search(
            r"\b(?:do\s+)?(?:you|u)\s+hav+e\s+(?:any\s+)?games?\b",
            query,
            flags=re.IGNORECASE,
        ))
        or bool(re.search(
            r"\b(?:show|list)\s+(?:me\s+)?(?:the\s+)?games?\b",
            query,
            flags=re.IGNORECASE,
        ))
    )
    unknown = None if catalog_signal else _unknown_game_candidate(query)
    if unknown:
        return _game_availability_answer(unknown)
    knowledge_request = bool(tokens & {"announcement", "document", "guidance", "knowledge", "policy"})
    if knowledge_request and not catalog_signal:
        return None
    if not catalog_signal and route.category != "games":
        return None
    zone = _zone_filter(query, entities)
    rows = [row for row in _availability_rows() if not zone or str(row.get("zone")) == zone]
    if not rows:
        return None
    if count_signal:
        unique_games = list(dict.fromkeys(
            str(game_name)
            for row in rows
            for game_name in row.get("games") or []
        ))
        scope = f" in {zone}" if zone else ""
        return _result(
            f"There are {len(unique_games)} verified game titles{scope}." + _source_suffix(RESERVATION_URL),
            category="games",
            intent="count",
            mode="pipeline:structured_games_count_en",
            confidence=0.98,
            hits=[_hit(str(row.get("id")), "games", str(row.get("source_url") or RESERVATION_URL), str(row.get("zone"))) for row in rows],
            reason="English count intent rendered from shared verified availability records",
        )
    return _result(
        _format_game_catalog(rows, zone),
        category="games",
        intent="games_lookup",
        mode="pipeline:structured_games_catalog_en",
        confidence=0.98,
        hits=[_hit(str(row.get("id")), "games", str(row.get("source_url") or RESERVATION_URL), str(row.get("zone"))) for row in rows],
        reason="shared game availability records rendered by English template",
    )


def _answer_equipment(query: str, entities: EntityBundle, *, route: PipelineRoute) -> EnglishSupportResult | None:
    tokens = _tokens(query)
    # Policy/problem questions mention equipment but belong to verified rules,
    # not the equipment catalog route.
    if tokens & {
        "break",
        "broken",
        "damage",
        "damaged",
        "fine",
        "issue",
        "penalties",
        "penalty",
        "problem",
        "report",
        "responsible",
    }:
        return None
    if tokens & {"game", "games", "play"} or _known_game(query):
        return None
    q = normalize_text(query)
    # A bare technical concept is not an inventory request. Without this gate,
    # questions such as "What is a GPU?" received every device in the studio.
    explanation_request = any(
        _phrase(query, phrase)
        for phrase in (
            "what is", "what are", "simple terms", "brief definition",
            "how do", "how does", "how are", "difference between", "differ",
        )
    )
    inventory_context = bool(tokens & {"available", "have", "inventory", "studio", "zone", "zones", "spec", "specs", "quantity", "many", "offer", "offers", "provided"}) or any(
        _phrase(query, phrase)
        for phrase in ("at the studio", "in the studio", "do you have", "what equipment")
    )
    zone = _zone_filter(query, entities)
    all_rows = list(_equipment_rows())
    if not all_rows:
        return None

    def aliases_for_item(row: dict[str, Any]) -> tuple[str, ...]:
        """Derive stable English lookup forms from one verified equipment record."""
        item = normalize_text(str(row.get("item") or "")).strip()
        if not item:
            return ()
        values = {item}
        if "รุ่น" in item:
            values.add(item.split("รุ่น", 1)[0].strip())
        english_unit = re.sub(r"\b(\d+)\s*นิ้ว\b", r"\1 inch", item)
        english_unit = re.sub(r"\bรุ่น\b", "model", english_unit).strip()
        values.add(english_unit)
        tv_match = re.fullmatch(r"tv\s+(\d+)\s+inch", english_unit, flags=re.IGNORECASE)
        if tv_match:
            size = tv_match.group(1)
            values.update({f"{size} inch tv", f"{size}-inch tv", f"tv {size}-inch"})
        sofa_match = re.fullmatch(r"sofa\s+(\d+)\s+seats?", english_unit, flags=re.IGNORECASE)
        if sofa_match:
            size = sofa_match.group(1)
            number_word = {"1": "one", "2": "two", "3": "three", "4": "four"}.get(size, size)
            values.update({
                f"{size} seat sofa", f"{size}-seat sofa", f"sofa with {size} seats",
                f"sofa with {number_word} seats",
            })
        return tuple(sorted((value for value in values if value), key=len, reverse=True))

    def matches_item(row: dict[str, Any]) -> bool:
        return any(
            alias and re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", q)
            for alias in aliases_for_item(row)
        )

    # Resolve a full item name before applying a broad zone filter. For
    # example, ``Sony PlayStation VR2`` contains "PlayStation" but belongs to
    # VR Zone rather than the PlayStation 5 catalog.
    specific = next((row for row in all_rows if matches_item(row)), None)
    rows = [row for row in all_rows if not zone or zone in str(row.get("zone"))]
    if not rows and specific is None:
        return None
    if explanation_request and not inventory_context and specific is None:
        return None
    signal = bool(tokens & {"equipment", "device", "devices", "hardware", "spec", "specs", "monitor", "keyboard", "mouse", "headset", "chair", "console", "offer", "offers", "provided"})
    if not signal and route.category != "equipment" and specific is None:
        return None
    asks_for_usage = bool(tokens & {"purpose", "details", "detail"}) or any(
        _phrase(query, phrase)
        for phrase in ("used for", "how to use", "what is it for")
    )
    if specific is not None and asks_for_usage:
        translated = approved_localization(specific, "what_th")
        if translated is None:
            url = str(specific.get("source_url") or HOME_URL)
            return _result(
                format_no_answer("equipment details", "en", missing_translation=True) + _source_suffix(url),
                category="equipment",
                intent="equipment_item_lookup",
                mode="pipeline:missing_english_localization",
                confidence=0.99,
                hits=[_hit(str(specific.get("id")), "equipment", url, str(specific.get("item")))],
                reason=f"what_th={localization_status(specific, 'what_th')}",
                warnings=("missing_translation",),
                answer_type="no_answer",
            )
    if specific is not None:
        item = str(specific.get("item") or "equipment")
        item_label = re.sub(r"\b(\d+)\s*นิ้ว\b", r"\1-inch", item).replace("รุ่น", "model")
        location = str(specific.get("zone") or "the studio")
        url = str(specific.get("source_url") or HOME_URL)
        return _result(
            f"Verified equipment record: {item_label} is listed in {location}." + _source_suffix(url),
            category="equipment",
            intent="equipment_item_lookup",
            mode="pipeline:structured_equipment_item_en",
            confidence=0.98,
            hits=[_hit(str(specific.get("id")), "equipment", url, item)],
            reason="exact verified equipment item matched through record-derived English forms",
        )
    lines = [f"Verified equipment{f' in {zone}' if zone else ''}:"]
    for row in rows:
        quantity = str(row.get("quantity") or "").strip()
        suffix = f" - {quantity}" if quantity else ""
        item_label = str(row.get("item") or "").replace("รุ่น", "model").replace("นิ้ว", "inch")
        lines.append(f"- {item_label} ({row.get('zone')}){suffix}")
    url = str(rows[0].get("source_url") or HOME_URL)
    lines.append(f"Source: {url} (original source in Thai)")
    return _result(
        "\n".join(lines),
        category="equipment",
        intent="equipment_catalog",
        mode="pipeline:structured_equipment_catalog_en",
        confidence=0.97,
        hits=[_hit(str(row.get("id")), "equipment", str(row.get("source_url") or HOME_URL), str(row.get("item"))) for row in rows],
        reason="shared equipment records rendered without translating Thai descriptions",
    )


def _is_member_query(query: str, route: PipelineRoute) -> bool:
    tokens = _tokens(query)
    position_pattern = bool(re.search(r"\b(?:what\s+)?(?:position|role)\s+(?:does|do|is)\b", query, flags=re.IGNORECASE))
    holds_pattern = bool(re.search(r"\b(?:what\s+position\s+does|who)\b.*\bhold\b", query, flags=re.IGNORECASE))
    return bool(
        (route.category in {"overview", "about_us"} and "member" in route.intent)
        or tokens & {"member", "members", "staff", "manager", "director", "dean", "president", "rector", "secretary", "treasurer", "chairperson", "captain", "ambassador", "referee"}
        or _has_requested_member_role(query)
        or _phrase(query, "main character")
        or position_pattern
        or holds_pattern
    )


_MEMBER_ROLE_QUERY_ALIASES = {
    "manager": ("ผู้จัดการ",),
    "director": ("ผู้อำนวยการ",),
    "dean": ("คณบดี",),
    "president": ("อธิการบดี",),
    "rector": ("อธิการบดี",),
    "vice chancellor": ("รองอธิการบดี",),
    "deputy vice chancellor": ("รองอธิการบดี",),
    "assistant vice chancellor": ("ผู้ช่วยอธิการบดีฝ่ายวิชาการ",),
    "computer academic": ("นักวิชาการคอมพิวเตอร์",),
    "computer scientist": ("นักวิชาการคอมพิวเตอร์",),
    "chairperson": ("ประธาน",),
    "deputy chairperson": ("รองประธาน",),
    "deputy chair": ("รองประธาน",),
    "secretary": ("เลขานุการ",),
    "treasurer": ("เหรัญญิก",),
    "public relations": ("ประชาสัมพันธ์",),
    "pr": ("ประชาสัมพันธ์",),
    "committee member": ("กรรมการ",),
    "board member": ("กรรมการ",),
    "internship student": ("นักศึกษาฝึกงาน",),
    "game and 3d developer": ("นักศึกษาสหกิจ Game and 3D Developer",),
    "web and ai developer": ("นักศึกษาสหกิจ Web & AI Developer",),
    "ai chat bot developer": ("AI Chat Bot Developer",),
}

_UNVERIFIED_MEMBER_ROLE_TERMS = {"captain", "ambassador", "referee"}


def _requested_member_role_terms(query: str) -> set[str]:
    q = normalize_text(query)
    tokens = _tokens(q)
    return {
        thai_term
        for english_role, thai_terms in _MEMBER_ROLE_QUERY_ALIASES.items()
        if (" " in english_role and all(word in tokens for word in english_role.split())) or (" " not in english_role and english_role in tokens)
        for thai_term in thai_terms
    }


def _has_requested_member_role(query: str) -> bool:
    return bool(_requested_member_role_terms(query))


def _member_rows_for_requested_role(query: str) -> tuple[dict[str, Any], ...]:
    requested_terms = _requested_member_role_terms(query)
    rows = _member_rows()
    if not requested_terms:
        return rows
    selected = tuple(
        row for row in rows
        if any(term in str(row.get("role") or "") for term in requested_terms)
    )
    return selected


def _answer_members(query: str, *, route: PipelineRoute) -> EnglishSupportResult | None:
    # A game-control question can naturally include "main character". A known
    # catalog title is stronger evidence than that generic member-like phrase.
    if _known_game(query) is not None and _phrase(query, "main character"):
        return None
    if not _is_member_query(query, route):
        return None
    tokens = _tokens(query)
    if tokens & _UNVERIFIED_MEMBER_ROLE_TERMS or _phrase(query, "main character"):
        return _result(
            "I could not find a verified PSU Esports Studio - Phuket member record for that requested role.",
            category="overview",
            intent="members_lookup",
            mode="pipeline:member_role_not_found_en",
            confidence=0.96,
            hits=[_hit("Members", "members", MEMBERS_URL, "Members")],
            reason="unverified English role was not mapped to an official member record",
            answer_type="no_answer",
        )
    member_rows = _member_rows_for_requested_role(query)
    role_requested = _has_requested_member_role(query)
    if not member_rows:
        return _result(
            "I could not find a verified member record for the requested role.",
            category="overview",
            intent="members_lookup",
            mode="pipeline:member_role_not_found_en",
            confidence=0.96,
            hits=[_hit("Members", "members", MEMBERS_URL, "Members")],
            reason="requested English role did not match an official member role",
            answer_type="no_answer",
        )
    translated_rows: list[tuple[str, str, str, dict[str, Any]]] = []
    source_language_rows: list[dict[str, Any]] = []
    for row in member_rows:
        name = approved_localization(row, "name")
        role = approved_localization(row, "role")
        affiliation = approved_localization(row, "affiliation") or ""
        if role is None:
            source_language_rows.append(row)
            continue
        official_name = name or str(row.get("name") or "").strip()
        translated_rows.append((official_name, role, affiliation, row))

    # Names and titles are official identifiers rather than prose to be
    # improvised by a model. When an English overlay is not yet approved, show
    # the exact Thai source record with an explicit label and its source link.
    # The final validator permits Thai only for this tightly scoped mode.
    if source_language_rows:
        lines = [
            "Official Thai source member record(s):",
            "Names and role titles below are shown exactly as published by PSU.",
        ]
        for row in member_rows:
            name = str(row.get("name") or "").strip()
            role = str(row.get("role") or "").strip()
            affiliation = str(row.get("affiliation") or "").strip()
            suffix = f" - {affiliation}" if affiliation else ""
            lines.append(f"- {name}: {role}{suffix}")
        lines.append(f"Source: {MEMBERS_URL} (official Thai source)")
        return _result(
            "\n".join(lines),
            category="overview",
            intent="members_lookup",
            mode="pipeline:structured_members_source_th",
            confidence=0.98,
            hits=[_hit("Members", "members", MEMBERS_URL, "Members")],
            reason="official member names and roles are rendered exactly as published in the Thai source",
            warnings=("english_member_directory_uses_original_thai_source",),
        )
    if not translated_rows:
        return None
    lines = [
        "Verified PSU Esports Studio - Phuket member record(s) for the requested role:"
        if role_requested
        else "Verified PSU Esports Studio - Phuket member directory:"
    ]
    for name, role, affiliation, _row in translated_rows:
        suffix = f" - {affiliation}" if affiliation else ""
        lines.append(f"- {name}: {role}{suffix}")
    lines.append(f"Source: {MEMBERS_URL} (original source in Thai)")
    return _result(
        "\n".join(lines),
        category="overview",
        intent="members_lookup",
        mode="pipeline:structured_members_en",
        confidence=0.98,
        hits=[_hit("Members", "members", MEMBERS_URL, "Members")],
        reason="English member localization overlay matched current Thai source hashes",
    )


def _is_competition_query(query: str, route: PipelineRoute) -> bool:
    tokens = _tokens(query)
    explicit_signals = {
        "competition", "tournament", "bracket", "match", "round", "pause", "ban",
        "penalty", "forfeit", "cheating", "substitute", "substitutes", "late",
        "checkin", "reporting", "map", "maps", "veto", "paused", "crash",
        "crashes", "restart", "restarted", "final", "finals", "backup",
        "restrictions", "bug", "account",
    }
    known_game = _known_game(query)
    competition_target = _competition_target(query)
    # ``FINAL FANTASY XVI`` is a verified catalog title. Its literal title
    # must not turn an ordinary game/control question into a finals question.
    if known_game == "FINAL FANTASY XVI":
        tokens.discard("final")
        tokens.discard("finals")
    # Bare "finals" is usually the verified title THE FINALS. Only let it
    # choose the competition path when a tournament target or another clear
    # competition signal is present.
    if not competition_target and not (tokens & {"competition", "tournament", "bracket", "match", "round", "veto"}):
        tokens.discard("final")
        tokens.discard("finals")
    # These frames are rule-oriented only when attached to a named game. A
    # bare player-count question can still be ordinary prose, while a request
    # to restart or handle a leaked match is a competition operation.
    if (known_game or competition_target) and tokens & {"lost", "leaked", "restart", "restrictions", "account", "late", "player", "players"}:
        return True
    if (known_game or competition_target) and any(
        _phrase(query, phrase)
        for phrase in ("short intro", "short overview", "short summary", "quick facts")
    ):
        return True
    player_support_question = "support" in tokens and bool(tokens & {"player", "players"})
    if tokens & explicit_signals or player_support_question or _phrase(query, "check in") or _phrase(query, "check-in"):
        return True
    # Semantic retrieval may assign a broad competition route merely because
    # a title appears in a competition document. Do not trust that route over
    # a known game entity unless the user also asked a competition question.
    return route.category == "competition_rules" and known_game is None


def _competition_target(query: str) -> str:
    tokens = _tokens(query)
    if "cs2" in tokens or {"counter", "strike"}.issubset(tokens):
        return "Counter-Strike 2"
    if "valorant" in tokens:
        return "VALORANT"
    if tokens & {"rov", "aov"} or _phrase(query, "arena of valor"):
        return "ROV"
    return ""


def _competition_target_matches(target: str, candidate_game: str) -> bool:
    """Match a canonical competition target against its published game title."""
    if not target:
        return True
    candidate = normalize_text(candidate_game)
    if candidate == normalize_text(target):
        return True
    aliases = {
        "Counter-Strike 2": ("counter strike 2", "counter-strike 2", "cs2"),
        "VALORANT": ("valorant",),
        "ROV": ("rov", "arena of valor"),
    }
    return any(alias in candidate for alias in aliases.get(target, ()))


def _answer_competition(query: str, *, route: PipelineRoute) -> EnglishSupportResult | None:
    if not _is_competition_query(query, route):
        return None
    target = _competition_target(query)
    query_tokens = _tokens(query)
    candidates: list[tuple[float, str, str, dict[str, Any]]] = []
    for row in _competition_rows():
        game = str(row.get("game") or "")
        if not _competition_target_matches(target, game):
            continue
        text = approved_localization(row, "text")
        section = approved_localization(row, "section_title") or str(row.get("section_title") or "")
        if text is None:
            continue
        searchable = _tokens(" ".join((game, section, text, " ".join(str(tag) for tag in row.get("tags") or []))))
        score = len(query_tokens & searchable) / max(1, len(query_tokens))
        if target and game.casefold() == target.casefold():
            score += 1.0
        # A broad competition route is not proof that every competition chunk
        # answers the question. Require lexical support unless a verified game
        # target itself selected the candidate.
        if score <= 0.0:
            continue
        candidates.append((score, section, text, row))
    if not candidates:
        # The Thai competition corpus is verified but most English overlays
        # await approval. Never replace an explicit competition operation with
        # an unrelated games catalog merely because English text is pending.
        return _result(
            format_no_answer("competition rules", "en", missing_translation=True) + _source_suffix(RESERVATION_URL),
            category="competition_rules",
            intent="competition_rule_lookup",
            mode="pipeline:missing_english_localization",
            confidence=0.96,
            hits=[_hit("competition_rules", "competition_rules", "data/competition_rules", target or "Competition rules")],
            reason="no approved English competition evidence matched the verified target",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )
    candidates.sort(key=lambda item: (-item[0], int(item[3].get("section_index") or 0), int(item[3].get("chunk_index") or 0)))
    draft_preview_used = any(localization_status(row, "text") == "draft_preview" for *_values, row in candidates)
    heading = (
        f"English draft translation of {target + ' ' if target else ''}competition rules:"
        if draft_preview_used
        else f"Verified {target + ' ' if target else ''}competition rules:"
    )
    lines = [heading]
    hits: list[dict[str, Any]] = []
    seen: set[str] = set()
    for _score, section, text, row in candidates[:3]:
        rendered = _compact_english_excerpt(text)
        if not rendered or rendered in seen:
            continue
        seen.add(rendered)
        prefix = f"{section}: " if section and section.casefold() not in rendered.casefold() else ""
        lines.append(f"- {prefix}{rendered}")
        hits.append(_hit(str(row.get("id") or "competition_rules"), "competition_rules", RESERVATION_URL, section or target or "Competition rules"))
    if len(lines) == 1:
        return None
    lines.append(_source_suffix(RESERVATION_URL).strip())
    return _result(
        "\n".join(lines),
        category="competition_rules",
        intent="competition_rule_lookup",
        mode="pipeline:structured_competition_rules_en",
        confidence=0.94,
        hits=hits,
        reason="draft English competition localization matched current Thai source hashes" if draft_preview_used else "English competition localization overlay matched current Thai source hashes",
        warnings=("english_draft_preview",) if draft_preview_used else (),
    )


def _answer_missing_localized_domain(query: str, *, route: PipelineRoute) -> EnglishSupportResult | None:
    tokens = _tokens(query)
    if _is_member_query(query, route):
        return _result(
            format_no_answer("members", "en", missing_translation=True) + _source_suffix(MEMBERS_URL),
            category="overview",
            intent="members_lookup",
            mode="pipeline:missing_english_localization",
            confidence=0.98,
            hits=[_hit("Members", "about_us", MEMBERS_URL, "Members")],
            reason=f"official English member names/roles are not approved ({len(_member_rows())} source records)",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )
    if _is_competition_query(query, route):
        return _result(
            format_no_answer("competition rules", "en", missing_translation=True) + _source_suffix(RESERVATION_URL),
            category="competition_rules",
            intent="competition_rule_lookup",
            mode="pipeline:missing_english_localization",
            confidence=0.96,
            hits=[_hit("competition_rules", "competition_rules", "data/competition_rules", "Competition rules")],
            reason="English competition RAG projection has no approved chunks",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )
    knowledge_signal = bool(tokens & {"announcement", "document", "guidance", "knowledge", "policy"}) and bool(
        tokens & {"explain", "latest", "summarize", "summary", "verified", "detailed", "detail"}
    )
    if route.category in {"knowledge", "events_news"} or knowledge_signal:
        category = route.category if route.category in {"knowledge", "events_news"} else "knowledge"
        return _result(
            format_no_answer("knowledge-base content", "en", missing_translation=True) + _source_suffix(HOME_URL),
            category=category,
            intent="knowledge_localization_unavailable",
            mode="pipeline:missing_english_localization",
            confidence=0.95,
            hits=[_hit("english_rag_projection", category, HOME_URL, "Knowledge base")],
            reason="no approved English RAG evidence matched this knowledge request",
            warnings=("missing_translation",),
            answer_type="no_answer",
        )
    return None


def _answer_approved_rag(query: str, *, route: PipelineRoute) -> EnglishSupportResult | None:
    categories_by_route = {
        "competition_rules": {"competition_rules"},
        "knowledge": {"knowledge"},
        "events_news": {"events_news"},
        "overview": {"overview", "about_us", "members"},
        "about_us": {"overview", "about_us", "members"},
    }
    categories = categories_by_route.get(route.category)
    if not categories:
        return None
    target = _known_game(query) or ""
    evidence = retrieve_approved_english(query, categories=categories, target=target, limit=4)
    if not evidence:
        return None
    lines = ["Verified information:"]
    seen_text: set[str] = set()
    for item in evidence:
        text = item.text.strip()
        if not text or text in seen_text:
            continue
        seen_text.add(text)
        lines.append(f"- {text}")
    urls = list(dict.fromkeys(item.source_url for item in evidence if item.source_url))
    if urls:
        lines.append("Sources: " + ", ".join(urls) + " (original sources in Thai)")
    hits = [
        _hit(
            f"{item.content_id}:{item.field}",
            item.category,
            item.source_url,
            item.title,
        )
        for item in evidence
    ]
    return _result(
        "\n".join(lines),
        category=route.category,
        intent=route.intent,
        mode="pipeline:approved_english_semantic_rag",
        confidence=min(0.96, max(item.score for item in evidence)),
        hits=hits,
        reason=f"approved English projection; retrieval={evidence[0].method}",
        warnings=(),
    )


def answer_english_supported(
    query: str,
    *,
    entities: EntityBundle,
    route: PipelineRoute,
    matcher: RuleMatcher,
) -> EnglishSupportResult | None:
    if route.intent == "chatbot_identity":
        return _result(
            "I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.",
            category="knowledge",
            intent="chatbot_identity",
            mode="pipeline:chatbot_identity_en",
            confidence=0.98,
            hits=[],
            reason="fixed bilingual chatbot identity response",
            answer_type="summary",
        )
    if route.intent == "chatbot_greeting":
        return _result(
            "Hello. I am PSU Esports Assistant for PSU Esports Studio - Phuket. Ask me about games, equipment, booking, opening hours, fees, rules, or studio contacts.",
            category="knowledge",
            intent="chatbot_greeting",
            mode="pipeline:chatbot_greeting_en",
            confidence=0.99,
            hits=[],
            reason="fixed bilingual chatbot greeting response",
            answer_type="summary",
        )
    tokens = _tokens(query)
    # These requests either ask for personal data, explicitly state that no
    # source exists, or require fresh news the local catalog cannot verify.
    # Return a clear safe outcome instead of routing shared words such as
    # "today" to the opening-hours handler.
    if _phrase(query, "personal phone") or _phrase(query, "personal phone number"):
        return _result(
            "I cannot provide personal phone numbers. Please use the official studio contact channels.",
            category="no_answer",
            intent="personal_contact_not_available",
            mode="pipeline:english_no_answer",
            confidence=0.99,
            hits=[],
            reason="personal contact information is outside the approved public knowledge scope",
            answer_type="no_answer",
        )
    if _phrase(query, "information not available") or _phrase(query, "not available on the psu esports website"):
        return _result(
            format_no_answer("this request", "en"),
            category="no_answer",
            intent="verified_information_unavailable",
            mode="pipeline:english_no_answer",
            confidence=0.98,
            hits=[],
            reason="request explicitly has no approved source evidence",
            answer_type="no_answer",
        )
    if tokens & {"news", "announcement"} and tokens & {"latest", "today", "current"}:
        return _result(
            "I do not have a verified live news feed for that request. Please check the official PSU Esports Studio - Phuket channels.",
            category="no_answer",
            intent="live_news_unavailable",
            mode="pipeline:english_no_answer",
            confidence=0.98,
            hits=[],
            reason="fresh news requires a live verified source that is not connected to this chatbot",
            answer_type="no_answer",
        )
    # Exact calculations and token-sensitive schedule checks take priority over
    # broad legacy regex rules so ordinary words cannot be mistaken for days or games.
    for resolver in (
        lambda: _answer_price(query, entities),
        lambda: _answer_booking_intent(query, matcher),
        lambda: _answer_schedule(query, entities),
        lambda: _answer_members(query, route=route),
        # Targeted game/equipment facts must be resolved before broad semantic
        # domains. Their data is verified and does not require an LLM rewrite.
        lambda: _answer_equipment(query, entities, route=route),
        # Competition operations have stronger intent than a broad catalog
        # route, including targets such as ROV that are not studio game titles.
        lambda: _answer_competition(query, route=route),
        lambda: _answer_games(query, entities, route=route),
        lambda: _rule_answer(query, matcher),
        lambda: _answer_approved_rag(query, route=route),
        lambda: _answer_missing_localized_domain(query, route=route),
    ):
        result = resolver()
        if result is not None:
            return result
    return _result(
        format_no_answer(route.category or "this question", "en"),
        category="no_answer",
        intent="english_verified_evidence_unavailable",
        mode="pipeline:english_no_answer",
        confidence=0.52,
        hits=[],
        reason="English requests never fall through to Thai-only runtime paths",
        answer_type="no_answer",
    )
