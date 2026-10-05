from __future__ import annotations

from app.pipeline.schemas import EntityBundle, PipelineRoute


def _resolved_locale(locale: str | None) -> str:
    if locale in {"th", "en"}:
        return locale
    try:
        from app.pipeline.execution_context import current_locale_decision

        decision = current_locale_decision()
        if decision is not None:
            return decision.effective
    except ImportError:
        pass
    return "th"


def _source_urls(hits: list[dict]) -> list[str]:
    urls: list[str] = []
    for hit in hits:
        url = str(hit.get("metadata", {}).get("source_url", "")).strip()
        if url and url not in urls:
            urls.append(url)
    return urls


def format_no_answer(category: str = "general", locale: str | None = None, *, missing_translation: bool = False) -> str:
    locale = _resolved_locale(locale)
    if locale == "en":
        if missing_translation:
            return (
                "This information does not yet have an approved English localization. "
                "Please open the cited original source or ask a staff member for confirmation."
            )
        if category and category != "general":
            return f"I could not find verified PSU Esports Studio - Phuket information for {category}."
        return "I could not find verified PSU Esports Studio - Phuket information for this question."
    if category and category != "general":
        return f"ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด {category} ตอนนี้ครับ"
    return "ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ"


def format_clarification(reason: str = "target", locale: str | None = None) -> str:
    locale = _resolved_locale(locale)
    if locale == "en":
        if reason == "service":
            return "Which service or zone do you mean: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?"
        if reason == "game":
            return "Which game do you mean? Please provide the game title."
        return "Could you provide a little more detail so I can use the correct verified information?"
    if reason == "service":
        return "หมายถึงบริการหรือโซนไหนครับ: PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR"
    if reason == "game":
        return "หมายถึงเกมไหนครับ กรุณาระบุชื่อเกมเพิ่มเติม"
    return "ขอรายละเอียดเพิ่มอีกเล็กน้อยครับ เพื่อให้เลือกข้อมูลที่ยืนยันแล้วได้ตรงคำถาม"


def format_response_style(answer: str, locale: str | None = None) -> str:
    locale = _resolved_locale(locale)
    text = (answer or "").strip()
    if locale == "en":
        return text
    from app.core.thai_style import format_thai_response_style

    return format_thai_response_style(text)


def _should_append_sources(text: str) -> bool:
    no_answer_prefixes = (
        "ยังไม่พบข้อมูลปุ่มควบคุม",
        "ยังไม่พบข้อมูลที่ยืนยันได้",
        "I could not find verified",
        "This information does not yet have an approved English localization",
    )
    return not any(text.startswith(prefix) for prefix in no_answer_prefixes)


def format_answer(answer: str, hits: list[dict], route: PipelineRoute, entities: EntityBundle, locale: str | None = None) -> str:
    locale = _resolved_locale(locale)
    text = (answer or "").strip()
    if not text:
        return format_no_answer(route.category, locale)

    if entities.short_answer:
        useful_lines = [line.strip() for line in text.splitlines() if line.strip()]
        first = useful_lines[0] if useful_lines else text
        if len(useful_lines) > 1 and useful_lines[1].startswith("-"):
            first = first + "\n" + useful_lines[1]
        urls = _source_urls(hits)
        if urls and _should_append_sources(first):
            source_label = "Source" if locale == "en" else "แหล่งข้อมูล"
            source_note = " (original source in Thai)" if locale == "en" else ""
            return first + f"\n{source_label}: " + urls[0] + source_note
        return first

    source_label = "Source" if locale == "en" else "แหล่งข้อมูล"
    if source_label not in text and _should_append_sources(text):
        urls = _source_urls(hits)
        if urls:
            source_note = " (original source in Thai)" if locale == "en" else ""
            text += f"\n{source_label}: " + ", ".join(urls) + source_note

    return text
