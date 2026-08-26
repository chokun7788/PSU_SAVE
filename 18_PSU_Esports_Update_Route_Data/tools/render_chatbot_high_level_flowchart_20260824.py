from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "psu_esports_chatbot_high_level_flowchart_20260824.png"
REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")

BG = "#071019"
STRIPE = "#0B1724"
PANEL = "#0E1D2B"
TEXT = "#F3F7FB"
MUTED = "#B8C5D2"
LINE = "#385266"
GREEN = "#57D990"
BLUE = "#7CAAFF"
CYAN = "#43CAE9"
GOLD = "#F4C965"
ORANGE = "#F59B61"
RED = "#F16F78"
PURPLE = "#AB9AF7"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold and BOLD.exists() else REGULAR), size=size)


TITLE = font(88, True)
SUBTITLE = font(39)
CARD_TITLE = font(43, True)
BODY = font(31)
LABEL = font(28, True)
FOOT = font(27)


def text_width(draw: ImageDraw.ImageDraw, value: str, text_font: ImageFont.FreeTypeFont) -> int:
    return int(draw.textbbox((0, 0), value, font=text_font)[2])


def wrap(draw: ImageDraw.ImageDraw, value: str, text_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in value.split(" "):
        candidate = word if not current else f"{current} {word}"
        if text_width(draw, candidate, text_font) <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        current = word
    if current:
        lines.append(current)
    return lines


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    accent: str,
    tag: str | None = None,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=28, fill=PANEL, outline=LINE, width=4)
    draw.rounded_rectangle((x1, y1, x1 + 19, y2), radius=10, fill=accent)
    draw.text((x1 + 52, y1 + 31), title, font=CARD_TITLE, fill=TEXT)
    if tag:
        tag_width = text_width(draw, tag, LABEL) + 40
        draw.rounded_rectangle((x2 - tag_width - 26, y1 + 26, x2 - 26, y1 + 74), radius=13, fill=accent)
        draw.text((x2 - tag_width - 6, y1 + 36), tag, font=LABEL, fill=BG)
    y = y1 + 112
    for line in wrap(draw, body, BODY, x2 - x1 - 96):
        draw.text((x1 + 52, y), line, font=BODY, fill=MUTED)
        y += 46


def diamond(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    size: tuple[int, int],
    title: str,
    body: str,
    accent: str,
) -> tuple[int, int, int, int]:
    cx, cy = center
    width, height = size
    points = ((cx, cy - height // 2), (cx + width // 2, cy), (cx, cy + height // 2), (cx - width // 2, cy))
    draw.polygon(points, fill=PANEL)
    draw.line(points + (points[0],), fill=accent, width=5)
    title_width = text_width(draw, title, CARD_TITLE)
    draw.text((cx - title_width // 2, cy - 68), title, font=CARD_TITLE, fill=TEXT)
    y = cy - 8
    for line in wrap(draw, body, BODY, width - 210)[:2]:
        line_width = text_width(draw, line, BODY)
        draw.text((cx - line_width // 2, y), line, font=BODY, fill=MUTED)
        y += 44
    return (cx - width // 2, cy - height // 2, cx + width // 2, cy + height // 2)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, label: str | None = None) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=8)
    angle = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - 26 * math.cos(angle) + 17 * math.sin(angle), y2 - 26 * math.sin(angle) - 17 * math.cos(angle))
    right = (x2 - 26 * math.cos(angle) - 17 * math.sin(angle), y2 - 26 * math.sin(angle) + 17 * math.cos(angle))
    draw.polygon((end, left, right), fill=color)
    if label:
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        label_width = text_width(draw, label, LABEL) + 38
        draw.rounded_rectangle((mid_x - label_width // 2, mid_y - 27, mid_x + label_width // 2, mid_y + 23), radius=12, fill=BG, outline=color, width=2)
        draw.text((mid_x - label_width // 2 + 19, mid_y - 17), label, font=LABEL, fill=TEXT)


def elbow(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], color: str, label: str | None = None) -> None:
    draw.line(points, fill=color, width=8, joint="curve")
    arrow(draw, points[-2], points[-1], color, label)


def main() -> None:
    image = Image.new("RGB", (5200, 5200), BG)
    draw = ImageDraw.Draw(image)
    for y in range(0, 5200, 360):
        draw.rectangle((0, y, 5200, y + 150), fill=STRIPE)

    draw.text((180, 100), "PSU ESPORTS CHATBOT — HIGH-LEVEL FLOWCHART", font=TITLE, fill=TEXT)
    draw.text((185, 220), "ภาพย่อ: รูปข้าวหลามตัดคือจุดตัดสินใจ, สี่เหลี่ยมคือ Process", font=SUBTITLE, fill=MUTED)

    start = (1900, 380, 3300, 555)
    draw.rounded_rectangle(start, radius=80, fill=GREEN)
    start_text = "START: USER พิมพ์คำถามบน WEBSITE"
    draw.text(((5200 - text_width(draw, start_text, LABEL)) // 2, 426), start_text, font=LABEL, fill=BG)

    intake = (1320, 680, 3880, 1060)
    understand = (1320, 1215, 3880, 1595)
    card(draw, intake, "1. Web API + Request Guard", "รับ JSON ตรวจ input, session, request overload และงบเวลารวม 9 วินาที", CYAN, "API")
    card(draw, understand, "2. Context + Understanding", "อ่าน history แยกคำถาม ดึง intent/target แล้วเลือก route ที่เหมาะสม", PURPLE, "Pipeline")
    arrow(draw, (2600, 565), (2600, 670), GREEN)
    arrow(draw, (2600, 1070), (2600, 1205), CYAN)

    decision_route = diamond(draw, (2600, 1970), (1750, 620), "ข้อมูลมี Path ชัดไหม?", "ราคา ตาราง เกม อุปกรณ์ กฎ หรือ FAQ ที่ structured รองรับ", ORANGE)
    arrow(draw, (2600, 1605), (2600, 1655), PURPLE)

    fast = (180, 2470, 1770, 3040)
    rag = (3430, 2470, 5020, 3040)
    card(draw, fast, "A. Fast / Structured", "ใช้ Rule, Calculator และ Structured Tool ตอบข้อมูล exact โดยไม่เรียก LLM", GREEN, "ใช่")
    card(draw, rag, "B. Semantic RAG", "BGE ค้นเอกสาร แล้วตรวจ source, freshness, target, score และ margin", CYAN, "ไม่ชัด/ต้องค้น")
    elbow(draw, [(1725, 1970), (970, 1970), (970, 2460)], GREEN, "ใช่")
    elbow(draw, [(3475, 1970), (4225, 1970), (4225, 2460)], CYAN, "ไม่ใช่")

    evidence = diamond(draw, (4225, 3510), (1450, 580), "Evidence เพียงพอไหม?", "เอกสารตรง target และผ่าน source/freshness guard", CYAN)
    arrow(draw, (4225, 3050), (4225, 3210), CYAN)

    draft = (1840, 3860, 3410, 4400)
    safe = (3590, 3860, 5020, 4400)
    card(draw, draft, "C. Draft / LLM Composer", "มี evidence: ตอบ Draft ได้ทันที หรือให้ Typhoon เรียบเรียงเมื่อหลาย evidence และเวลาเหลือ", GOLD, "ผ่าน")
    card(draw, safe, "D. Safe Outcome", "ถามกลับเมื่อกำกวม, no-answer เมื่อไม่มีข้อมูล PSU, หรือ General LLM เฉพาะคำถามทั่วไปที่อนุญาต", RED, "ไม่ผ่าน")
    elbow(draw, [(3500, 3510), (2625, 3510), (2625, 3850)], GOLD, "ใช่")
    arrow(draw, (4225, 3810), (4225, 3850), RED, "ไม่")

    validation = (880, 4590, 4320, 4920)
    elbow(draw, [(970, 3050), (970, 4500), (2600, 4500), (2600, 4580)], GREEN)
    elbow(draw, [(2625, 4410), (2625, 4580)], GOLD)
    elbow(draw, [(4225, 4410), (4225, 4500), (2600, 4500), (2600, 4580)], RED)
    card(draw, validation, "3. Validation & Final Answer", "ตรวจ target, claim, ตัวเลข, evidence/source และรูปแบบภาษาไทย ก่อนส่ง JSON กลับ Website พร้อม trace/log", RED, "ทุก path")
    draw.text((180, 5050), "หลักการ: ข้อมูลชัดใช้ Fast/Structured • ข้อมูลเอกสารใช้ RAG • LLM เป็นผู้ช่วยแบบ gated • ทุก path ต้องผ่าน validation", font=FOOT, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
