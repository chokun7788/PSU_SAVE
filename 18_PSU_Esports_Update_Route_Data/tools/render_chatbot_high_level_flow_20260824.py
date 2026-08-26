from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "psu_esports_chatbot_high_level_flow_20260824.png"
REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")

BG = "#071019"
STRIPE = "#0B1724"
PANEL = "#0E1D2B"
TEXT = "#F3F7FB"
MUTED = "#B8C5D2"
LINE = "#344E63"
GREEN = "#57D990"
BLUE = "#7CAAFF"
CYAN = "#43CAE9"
GOLD = "#F4C965"
ORANGE = "#F59B61"
RED = "#F16F78"
PURPLE = "#AB9AF7"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold and BOLD.exists() else REGULAR), size=size)


TITLE = font(90, True)
SUBTITLE = font(40)
CARD_TITLE = font(47, True)
BODY = font(33)
TAG = font(27, True)
FOOT = font(28)


def text_width(draw: ImageDraw.ImageDraw, value: str, text_font: ImageFont.FreeTypeFont) -> int:
    return int(draw.textbbox((0, 0), value, font=text_font)[2])


def wrapped(draw: ImageDraw.ImageDraw, value: str, text_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in value.split(" "):
        candidate = word if not current else f"{current} {word}"
        if text_width(draw, candidate, text_font) <= max_width:
            current = candidate
        else:
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
    draw.rounded_rectangle(box, radius=30, fill=PANEL, outline=LINE, width=4)
    draw.rounded_rectangle((x1, y1, x1 + 20, y2), radius=10, fill=accent)
    draw.text((x1 + 55, y1 + 34), title, font=CARD_TITLE, fill=TEXT)
    if tag:
        tag_width = text_width(draw, tag, TAG) + 42
        draw.rounded_rectangle((x2 - tag_width - 28, y1 + 28, x2 - 28, y1 + 76), radius=14, fill=accent)
        draw.text((x2 - tag_width - 7, y1 + 37), tag, font=TAG, fill=BG)
    y = y1 + 116
    for line in wrapped(draw, body, BODY, x2 - x1 - 104):
        draw.text((x1 + 55, y), line, font=BODY, fill=MUTED)
        y += 47


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
        label_width = text_width(draw, label, TAG) + 36
        draw.rounded_rectangle((mid_x - label_width // 2, mid_y - 28, mid_x + label_width // 2, mid_y + 22), radius=13, fill=BG, outline=color, width=2)
        draw.text((mid_x - label_width // 2 + 18, mid_y - 18), label, font=TAG, fill=TEXT)


def elbow(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], color: str, label: str | None = None) -> None:
    draw.line(points, fill=color, width=8, joint="curve")
    arrow(draw, points[-2], points[-1], color, label)


def main() -> None:
    image = Image.new("RGB", (4800, 3600), BG)
    draw = ImageDraw.Draw(image)
    for y in range(0, 3600, 360):
        draw.rectangle((0, y, 4800, y + 150), fill=STRIPE)

    draw.text((180, 100), "PSU ESPORTS CHATBOT — HIGH-LEVEL FLOW", font=TITLE, fill=TEXT)
    draw.text((184, 225), "ภาพย่อ: เห็นเส้นทางหลักตั้งแต่ User Input จนถึง Final Answer", font=SUBTITLE, fill=MUTED)

    top = [
        (180, 470, 1160, 900),
        (1320, 470, 2300, 900),
        (2460, 470, 3440, 900),
        (3600, 470, 4620, 900),
    ]
    card(draw, top[0], "1. User Input", "ผู้ใช้พิมพ์คำถามใน Website", BLUE, "Browser")
    card(draw, top[1], "2. Web API + Guard", "รับ JSON ตรวจ input, session, overload และ deadline", CYAN, "9s budget")
    card(draw, top[2], "3. Understand", "อ่าน context แยกคำถาม ดึง target และ intent", PURPLE, "Pipeline")
    card(draw, top[3], "4. Choose Path", "เลือกวิธีตอบจาก route, evidence และความกำกวม", ORANGE, "Decision")
    for left, right, color in zip(top, top[1:], [CYAN, PURPLE, ORANGE]):
        arrow(draw, (left[2] + 10, 685), (right[0] - 12, 685), color)

    draw.text((180, 1060), "EXECUTION PATHS", font=CARD_TITLE, fill=TEXT)
    draw.text((610, 1070), "ระบบไม่ได้เรียก Local LLM ทุกคำถาม", font=BODY, fill=MUTED)
    lanes = [
        (180, 1160, 1500, 1830),
        (1740, 1160, 3060, 1830),
        (3300, 1160, 4620, 1830),
    ]
    card(draw, lanes[0], "A. Fast / Structured", "ราคา ตารางเวลา 42 เกม อุปกรณ์ วิธีจอง และข้อมูลที่มีช่องชัดเจน", GREEN, "Default")
    card(draw, lanes[1], "B. Semantic RAG", "ค้นเอกสารด้วย BGE และเลือก evidence ที่ source/freshness ผ่าน", CYAN, "เมื่อจำเป็น")
    card(draw, lanes[2], "C. Local LLM Assist", "Typhoon ช่วยวางแผน ตรวจ intent หรือเรียบเรียงหลาย evidence", GOLD, "Gated")

    elbow(draw, [(4110, 910), (4110, 1055), (840, 1055), (840, 1150)], GREEN, "ข้อมูลชัด")
    elbow(draw, [(4110, 910), (4110, 1055), (2400, 1055), (2400, 1150)], CYAN, "ต้องค้นเอกสาร")
    elbow(draw, [(4110, 910), (4110, 1055), (3960, 1055), (3960, 1150)], GOLD, "ต้องช่วยเรียบเรียง")

    final_box = (740, 2120, 4060, 2680)
    elbow(draw, [(840, 1840), (840, 2020), (2400, 2020), (2400, 2110)], GREEN)
    elbow(draw, [(2400, 1840), (2400, 2110)], CYAN)
    elbow(draw, [(3960, 1840), (3960, 2020), (2400, 2020), (2400, 2110)], GOLD)
    card(draw, final_box, "5. Validation & Safety", "ตรวจว่า target ถูกไหม, evidence/source ครบไหม, ตัวเลขไม่เพี้ยนไหม ถ้าผิดให้ใช้ Draft, clarification หรือ no-answer", RED, "ทุก path")

    output = (1220, 2890, 3580, 3290)
    arrow(draw, (2400, 2690), (2400, 2880), RED)
    card(draw, output, "6. Final Answer", "จัดคำตอบภาษาไทยแบบ answer-first -> ส่ง JSON กลับ Website -> เก็บ trace และ log", GREEN, "Output")
    draw.text((180, 3430), "Safe outcomes: clarification เมื่อกำกวม • no-answer เมื่อไม่มีข้อมูลยืนยัน • safe timeout เมื่อเวลาไม่พอ", font=FOOT, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
