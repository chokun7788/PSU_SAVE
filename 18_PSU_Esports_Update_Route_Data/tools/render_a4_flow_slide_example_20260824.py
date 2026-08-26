from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "psu_esports_chatbot_a4_flow_slide_example_20260824.png"
REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")

WHITE = "#FFFFFF"
INK = "#172033"
MUTED = "#6B7482"
LINE = "#B9C2CE"
BLUE = "#1769AA"
BLUE_SOFT = "#EDF5FC"
GREEN = "#23835E"
GREEN_SOFT = "#EEF8F3"
ORANGE = "#D87522"
ORANGE_SOFT = "#FFF4E9"
GRAY_SOFT = "#F7F8FA"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold and BOLD.exists() else REGULAR), size=size)


TITLE = font(76, True)
SUBTITLE = font(32)
BOX_TITLE = font(34, True)
BODY = font(25)
SMALL = font(22)
TAG = font(22, True)


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


def box(
    draw: ImageDraw.ImageDraw,
    area: tuple[int, int, int, int],
    number: str,
    title: str,
    body: str,
    accent: str,
    fill: str,
) -> None:
    x1, y1, x2, y2 = area
    draw.rounded_rectangle(area, radius=24, fill=fill, outline=LINE, width=3)
    draw.rounded_rectangle((x1 + 28, y1 + 28, x1 + 83, y1 + 83), radius=14, fill=accent)
    number_width = text_width(draw, number, TAG)
    draw.text((x1 + 56 - number_width // 2, y1 + 37), number, font=TAG, fill=WHITE)
    draw.text((x1 + 105, y1 + 33), title, font=BOX_TITLE, fill=INK)
    y = y1 + 94
    for line in wrap(draw, body, BODY, x2 - x1 - 72):
        draw.text((x1 + 36, y), line, font=BODY, fill=MUTED)
        y += 37


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = INK, dashed: bool = False) -> None:
    x1, y1 = start
    x2, y2 = end
    if dashed:
        distance = math.hypot(x2 - x1, y2 - y1)
        steps = max(1, int(distance // 30))
        for index in range(0, steps, 2):
            t1 = index / steps
            t2 = min(1.0, (index + 1) / steps)
            draw.line((x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1, x1 + (x2 - x1) * t2, y1 + (y2 - y1) * t2), fill=color, width=4)
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=5)
    angle = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - 20 * math.cos(angle) + 12 * math.sin(angle), y2 - 20 * math.sin(angle) - 12 * math.cos(angle))
    right = (x2 - 20 * math.cos(angle) - 12 * math.sin(angle), y2 - 20 * math.sin(angle) + 12 * math.cos(angle))
    draw.polygon((end, left, right), fill=color)


def pill(draw: ImageDraw.ImageDraw, area: tuple[int, int, int, int], value: str, fill: str, text_fill: str = INK) -> None:
    x1, y1, x2, y2 = area
    draw.rounded_rectangle(area, radius=(y2 - y1) // 2, fill=fill)
    value_width = text_width(draw, value, TAG)
    draw.text(((x1 + x2 - value_width) // 2, y1 + 12), value, font=TAG, fill=text_fill)


def main() -> None:
    image = Image.new("RGB", (3508, 2480), WHITE)
    draw = ImageDraw.Draw(image)

    draw.text((150, 132), "Flow", font=TITLE, fill=INK)
    draw.text((154, 236), "PSU Esports Chatbot: High-Level Answering Workflow", font=SUBTITLE, fill=MUTED)
    draw.line((150, 320, 3358, 320), fill=LINE, width=3)
    draw.text((2790, 150), "ใช้โลโก้เดิมของโครงการวางบริเวณนี้", font=SMALL, fill=MUTED)

    boxes = [
        (150, 820, 690, 1170),
        (810, 820, 1420, 1170),
        (1540, 820, 2300, 1170),
        (2420, 820, 3080, 1170),
    ]
    box(draw, boxes[0], "1", "User Input", "ผู้ใช้พิมพ์คำถามใน Website", BLUE, BLUE_SOFT)
    box(draw, boxes[1], "2", "Understand & Route", "Context, Intent, Target และเลือกเส้นทาง", BLUE, BLUE_SOFT)
    box(draw, boxes[2], "3", "Find Evidence", "Fast / Structured หรือ Semantic RAG", GREEN, GREEN_SOFT)
    box(draw, boxes[3], "4", "Answer & Verify", "Draft, validation และคำตอบภาษาไทย", GREEN, GREEN_SOFT)
    output = (3160, 860, 3358, 1130)
    draw.rounded_rectangle(output, radius=24, fill=GRAY_SOFT, outline=LINE, width=3)
    output_title = "Website"
    output_w = text_width(draw, output_title, BOX_TITLE)
    draw.text((3259 - output_w // 2, 914), output_title, font=BOX_TITLE, fill=INK)
    output_sub = "Output"
    output_sub_w = text_width(draw, output_sub, BODY)
    draw.text((3259 - output_sub_w // 2, 982), output_sub, font=BODY, fill=MUTED)

    for left, right in zip(boxes, boxes[1:]):
        arrow(draw, (left[2] + 18, 995), (right[0] - 18, 995))
    arrow(draw, (3098, 995), (3142, 995))

    pill(draw, (880, 1450, 1510, 1522), "LLM ASSIST (GATED)", ORANGE_SOFT, ORANGE)
    draw.text((888, 1565), "Intent Review  •  Query Planner", font=SMALL, fill=MUTED)
    arrow(draw, (1195, 1630), (1195, 1188), ORANGE, dashed=True)

    pill(draw, (2350, 1450, 3050, 1522), "LLM COMPOSER (GATED)", ORANGE_SOFT, ORANGE)
    draw.text((2377, 1565), "สรุปหลาย evidence ให้เป็นคำตอบ", font=SMALL, fill=MUTED)
    arrow(draw, (2700, 1630), (2700, 1188), ORANGE, dashed=True)

    draw.line((150, 1800, 3358, 1800), fill=LINE, width=2)
    draw.text((150, 1870), "หลักการตอบ", font=BOX_TITLE, fill=INK)
    draw.text((150, 1942), "ข้อมูลชัด: ตอบตรงจาก Structured/Fast   |   ต้องค้นเอกสาร: Semantic RAG   |   ต้องสรุปหลายข้อมูล: LLM Composer", font=BODY, fill=MUTED)
    draw.text((150, 2040), "ไม่มีข้อมูลยืนยันหรือคำถามกำกวม: Clarification / No-answer", font=BODY, fill=MUTED)
    draw.text((150, 2300), "หมายเหตุ: LLM เป็นชั้นช่วยเข้าใจและเรียบเรียง ไม่ใช่แหล่งข้อมูลจริงของราคา เวลา เกม หรือกฎ", font=SMALL, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
