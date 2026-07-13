from __future__ import annotations

from app.pipeline.schemas import EntityBundle, PipelineRoute


def _source_urls(hits: list[dict]) -> list[str]:
    urls: list[str] = []
    for hit in hits:
        url = str(hit.get("metadata", {}).get("source_url", "")).strip()
        if url and url not in urls:
            urls.append(url)
    return urls


def format_no_answer(category: str = "general") -> str:
    if category and category != "general":
        return f"ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด {category} ตอนนี้ครับ"
    return "ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ"


def _should_append_sources(text: str) -> bool:
    no_answer_prefixes = (
        "ยังไม่พบข้อมูลปุ่มควบคุม",
        "ยังไม่พบข้อมูลที่ยืนยันได้",
    )
    return not any(text.startswith(prefix) for prefix in no_answer_prefixes)


def format_answer(answer: str, hits: list[dict], route: PipelineRoute, entities: EntityBundle) -> str:
    text = (answer or "").strip()
    if not text:
        return format_no_answer(route.category)

    if entities.short_answer:
        useful_lines = [line.strip() for line in text.splitlines() if line.strip()]
        first = useful_lines[0] if useful_lines else text
        if len(useful_lines) > 1 and useful_lines[1].startswith("-"):
            first = first + "\n" + useful_lines[1]
        urls = _source_urls(hits)
        if urls and _should_append_sources(first):
            return first + "\nแหล่งข้อมูล: " + urls[0]
        return first

    if "แหล่งข้อมูล" not in text and _should_append_sources(text):
        urls = _source_urls(hits)
        if urls:
            text += "\nแหล่งข้อมูล: " + ", ".join(urls)

    return text
