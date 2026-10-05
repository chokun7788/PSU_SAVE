from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "psu_esports_chatbot_end_to_end_flowchart_20260825.png"
REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")

WIDTH, HEIGHT = 3600, 8700
BG = "#FFFFFF"
INK = "#16212B"
MUTED = "#5E6B78"
LINE = "#AAB6C2"
BLUE = "#2F76B7"
BLUE_TINT = "#EAF3FB"
GREEN = "#248A68"
GREEN_TINT = "#EAF7F1"
ORANGE = "#D66A20"
ORANGE_TINT = "#FFF1E7"
RED = "#C54F57"
RED_TINT = "#FCEBED"
PURPLE = "#7255B5"
PURPLE_TINT = "#F1EDFB"
GRAY_TINT = "#F4F6F8"


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = BOLD if bold and BOLD.exists() else REGULAR
    return ImageFont.truetype(str(path), size=size)


TITLE = get_font(76, True)
SUBTITLE = get_font(38)
SECTION = get_font(34, True)
CARD_TITLE = get_font(46, True)
BODY = get_font(32)
SMALL = get_font(28)
LABEL = get_font(27, True)


def width(draw: ImageDraw.ImageDraw, text: str, active_font: ImageFont.FreeTypeFont) -> int:
    return draw.textbbox((0, 0), text, font=active_font)[2]


def wrap(draw: ImageDraw.ImageDraw, text: str, active_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split(" "):
        candidate = word if not current else f"{current} {word}"
        if width(draw, candidate, active_font) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, active_font: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text(((WIDTH - width(draw, text, active_font)) // 2, y), text, font=active_font, fill=fill)


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    color: str,
    tint: str,
    tag: str | None = None,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=30, fill=tint, outline=color, width=4)
    draw.rounded_rectangle((x1, y1, x1 + 18, y2), radius=8, fill=color)
    draw.text((x1 + 46, y1 + 28), title, font=CARD_TITLE, fill=INK)
    if tag:
        tag_w = width(draw, tag, LABEL) + 42
        draw.rounded_rectangle((x2 - tag_w - 28, y1 + 26, x2 - 28, y1 + 76), radius=18, fill=color)
        draw.text((x2 - tag_w - 7, y1 + 35), tag, font=LABEL, fill="#FFFFFF")
    text_y = y1 + 102
    for line in wrap(draw, body, BODY, x2 - x1 - 92):
        draw.text((x1 + 46, text_y), line, font=BODY, fill=MUTED)
        text_y += 45


def diamond(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    size: tuple[int, int],
    title: str,
    body: str,
    color: str,
    tint: str,
) -> tuple[int, int, int, int]:
    cx, cy = center
    w, h = size
    points = ((cx, cy - h // 2), (cx + w // 2, cy), (cx, cy + h // 2), (cx - w // 2, cy))
    draw.polygon(points, fill=tint)
    draw.line(points + (points[0],), fill=color, width=5)
    centered_title = width(draw, title, CARD_TITLE)
    draw.text((cx - centered_title // 2, cy - 60), title, font=CARD_TITLE, fill=INK)
    text_y = cy + 5
    for line in wrap(draw, body, BODY, w - 350)[:2]:
        draw.text((cx - width(draw, line, BODY) // 2, text_y), line, font=BODY, fill=MUTED)
        text_y += 44
    return cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = LINE, label: str | None = None, dashed: bool = False) -> None:
    x1, y1 = start
    x2, y2 = end
    if dashed:
        length = math.dist(start, end)
        step = 22
        for offset in range(0, int(length), step):
            ratio1 = offset / length
            ratio2 = min(offset + 12, length) / length
            draw.line((x1 + (x2 - x1) * ratio1, y1 + (y2 - y1) * ratio1, x1 + (x2 - x1) * ratio2, y1 + (y2 - y1) * ratio2), fill=color, width=6)
    else:
        draw.line((x1, y1, x2, y2), fill=color, width=7)
    angle = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - 25 * math.cos(angle) + 15 * math.sin(angle), y2 - 25 * math.sin(angle) - 15 * math.cos(angle))
    right = (x2 - 25 * math.cos(angle) - 15 * math.sin(angle), y2 - 25 * math.sin(angle) + 15 * math.cos(angle))
    draw.polygon(((x2, y2), left, right), fill=color)
    if label:
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        tag_w = width(draw, label, LABEL) + 30
        draw.rounded_rectangle((mid_x - tag_w // 2, mid_y - 26, mid_x + tag_w // 2, mid_y + 22), radius=12, fill=BG, outline=color, width=2)
        draw.text((mid_x - tag_w // 2 + 15, mid_y - 16), label, font=LABEL, fill=INK)


def elbow(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], color: str, label: str | None = None, dashed: bool = False) -> None:
    for start, end in zip(points, points[1:]):
        draw.line((*start, *end), fill=color, width=6)
    arrow(draw, points[-2], points[-1], color, label=label, dashed=dashed)


def section_line(draw: ImageDraw.ImageDraw, y: int, label: str) -> None:
    draw.line((260, y, 3340, y), fill=LINE, width=3)
    label_w = width(draw, label, SECTION) + 50
    draw.rounded_rectangle((1800 - label_w // 2, y - 30, 1800 + label_w // 2, y + 30), radius=16, fill=BG)
    draw.text((1800 - label_w // 2 + 25, y - 20), label, font=SECTION, fill=MUTED)


def main() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)

    centered(draw, 115, "PSU ESPORTS CHATBOT", TITLE, INK)
    centered(draw, 220, "End-to-End Answering Flow", SUBTITLE, MUTED)

    section_line(draw, 390, "STARTUP: ทำครั้งเดียวเมื่อเปิดระบบ")
    startup = (650, 480, 2950, 780)
    card(draw, startup, "Setup + Warmup", "โหลดข้อมูล Cache และ Index พร้อม warm BGE / Local LLM ตาม policy", BLUE, BLUE_TINT, "ONCE")

    section_line(draw, 940, "REQUEST FLOW: ทำทุกครั้งที่ผู้ใช้ส่งข้อความ")
    web = (1050, 1030, 2550, 1240)
    card(draw, web, "Web Chat", "ผู้ใช้พิมพ์คำถามบนเว็บไซต์", BLUE, BLUE_TINT)
    api = (770, 1340, 2830, 1610)
    card(draw, api, "Web API / JSON Request", "รับข้อความและ Session ID จากหน้าเว็บ", BLUE, BLUE_TINT)
    intake = (520, 1710, 3080, 2020)
    card(draw, intake, "Request ID + Global Deadline", "สร้าง UUID สำหรับ trace และเริ่มงบเวลารวมของ request", PURPLE, PURPLE_TINT)
    admission = (690, 2130, 2910, 2400)
    card(draw, admission, "Admission Control", "ตรวจ capacity, session ที่กำลังทำงาน และคิวก่อนรับ request", PURPLE, PURPLE_TINT)
    context = (580, 2510, 3020, 2800)
    card(draw, context, "Session Context Resolver", "อ่าน history ที่มี evidence เพื่อแก้คำอ้างอิง เช่น เกมนั้น / อันเดิม", PURPLE, PURPLE_TINT)
    split = (760, 2900, 2840, 3170)
    card(draw, split, "Split Multi-question", "แยกคำถามย่อยเมื่อผู้ใช้ถามหลายเรื่องในข้อความเดียว", PURPLE, PURPLE_TINT)
    for top, bottom in ((1240, 1340), (1610, 1710), (2020, 2130), (2400, 2510), (2800, 2900)):
        arrow(draw, (1800, top), (1800, bottom))

    multi = diamond(draw, (1800, 3400), (1500, 410), "มีหลายคำถามไหม?", "1 ข้อไปเข้าใจคำถามต่อ  |  หลายข้อไปประเมินความซับซ้อน", PURPLE, PURPLE_TINT)
    arrow(draw, (1800, 3170), (1800, 3195), PURPLE)
    complexity = (2050, 3690, 3450, 3980)
    card(draw, complexity, "Complexity Gate", "ดู dependency, คำถามกว้าง และจำนวน task", ORANGE, ORANGE_TINT, "หลายข้อ")
    simple = (2050, 4100, 2720, 4350)
    complex = (2780, 4100, 3450, 4350)
    card(draw, simple, "Simple", "ทำ task อิสระแบบ bounded parallel", GREEN, GREEN_TINT)
    card(draw, complex, "Complex", "Query Planner สร้าง task ย่อยแบบจำกัด", ORANGE, ORANGE_TINT)
    elbow(draw, [(2550, 3400), (2750, 3400), (2750, 3680)], ORANGE, "หลายข้อ")
    arrow(draw, (2750, 3980), (2385, 4090), ORANGE, "อิสระ")
    arrow(draw, (2750, 3980), (3115, 4090), ORANGE, "พึ่งกัน")

    understanding = (560, 4550, 3040, 4960)
    card(draw, understanding, "Single-question Understanding Pipeline", "Normalize + Entity Extraction  |  Boundary Guard + Ambiguity Gate  |  Intent / Route Understanding", BLUE, BLUE_TINT, "ทุก task")
    elbow(draw, [(1050, 3400), (600, 3400), (600, 4515), (1800, 4515)], PURPLE, "1 ข้อ")
    elbow(draw, [(2385, 4350), (2385, 4420), (1800, 4420), (1800, 4540)], GREEN)
    elbow(draw, [(3115, 4350), (3115, 4420), (1800, 4420), (1800, 4540)], ORANGE)

    frame = (700, 5080, 2900, 5320)
    score = (700, 5430, 2900, 5670)
    precondition = (700, 5780, 2900, 6020)
    card(draw, frame, "Question Frame", "สรุป intent, target, filter และชนิดคำตอบที่คาดหวัง", BLUE, BLUE_TINT)
    card(draw, score, "Candidate Scoring", "จัดอันดับ route / capability ที่น่าจะตอบคำถามได้ตรงที่สุด", BLUE, BLUE_TINT)
    card(draw, precondition, "Tool Preconditions", "กันไม่ให้ tool ที่ไม่ตรงคำถามหรือ target ไม่ชัดถูกเรียกใช้", BLUE, BLUE_TINT)
    arrow(draw, (1800, 4960), (1800, 5080), BLUE)
    arrow(draw, (1800, 5320), (1800, 5430), BLUE)
    arrow(draw, (1800, 5670), (1800, 5780), BLUE)

    execution = (500, 6140, 3100, 6430)
    card(draw, execution, "Execution Path Selection", "เลือก path จาก score, policy, precondition, evidence และเวลาที่เหลือ", GREEN, GREEN_TINT)
    arrow(draw, (1800, 6020), (1800, 6140), GREEN)

    fast = (190, 6570, 1110, 6930)
    rag = (1340, 6570, 2260, 6930)
    safe = (2490, 6570, 3410, 6930)
    card(draw, fast, "Fast / Structured", "ราคา ตาราง เกม และข้อมูล exact", GREEN, GREEN_TINT)
    card(draw, rag, "Semantic RAG", "BGE Retrieval + optional rerank + source guard", BLUE, BLUE_TINT)
    card(draw, safe, "Safe Outcome", "Clarification, no-answer หรือ general-safe fallback", RED, RED_TINT)
    elbow(draw, [(1100, 6430), (650, 6430), (650, 6560)], GREEN)
    arrow(draw, (1800, 6430), (1800, 6560), BLUE)
    elbow(draw, [(2500, 6430), (2950, 6430), (2950, 6560)], RED)

    evidence = (550, 7100, 3050, 7380)
    card(draw, evidence, "Evidence + Draft", "รวมหลักฐานจาก path ที่เลือก แล้วสร้างคำตอบตั้งต้นที่ตรวจสอบย้อนกลับได้", GREEN, GREEN_TINT)
    elbow(draw, [(650, 6930), (650, 7040), (1800, 7040), (1800, 7090)], GREEN)
    arrow(draw, (1800, 6930), (1800, 7090), BLUE)
    elbow(draw, [(2950, 6930), (2950, 7040), (1800, 7040), (1800, 7090)], RED)

    composer = (550, 7490, 3050, 7750)
    card(draw, composer, "Optional Local LLM Composer", "เรียบเรียงจาก Evidence / Draft เท่านั้น ห้ามเพิ่มข้อมูล PSU ใหม่", ORANGE, ORANGE_TINT, "GATED")
    arrow(draw, (1800, 7380), (1800, 7490), ORANGE)

    validation = (500, 7860, 3100, 8150)
    card(draw, validation, "Format + Validation + Answer Contract", "ตรวจ target, claim, source, evidence และรูปแบบคำตอบก่อนส่ง", RED, RED_TINT)
    arrow(draw, (1800, 7750), (1800, 7860), RED)

    repair = (280, 8280, 1420, 8530)
    veto = (1620, 8280, 2700, 8530)
    final = (2840, 8280, 3500, 8530)
    card(draw, repair, "Bounded Repair", "แก้ได้จำกัด เช่นใช้ Draft หรือ candidate ถัดไป", ORANGE, ORANGE_TINT)
    card(draw, veto, "Final Hard Veto", "ยังไม่ผ่าน: clarification / no-answer", RED, RED_TINT)
    card(draw, final, "Final Answer", "Thai + JSON", GREEN, GREEN_TINT)
    elbow(draw, [(1200, 8150), (850, 8150), (850, 8270)], ORANGE, "ไม่ผ่าน")
    # Repair is deliberately bounded, then the repaired draft must go through
    # the same validator again before the final veto can allow it to leave.
    elbow(draw, [(280, 8405), (150, 8405), (150, 8005), (490, 8005)], ORANGE, "ตรวจซ้ำ")
    elbow(draw, [(1800, 8150), (2160, 8150), (2160, 8270)], RED, "ผ่านรอบตรวจ")
    arrow(draw, (2700, 8405), (2830, 8405), GREEN, "ผ่าน")

    llm_box = (80, 5320, 550, 5940)
    draw.rounded_rectangle(llm_box, radius=28, fill=ORANGE_TINT, outline=ORANGE, width=4)
    centered_x = 315
    for y, text, active_font in ((5380, "GATED", LABEL), (5445, "LOCAL", LABEL), (5495, "LLM", LABEL), (5580, "Intent Review", SMALL), (5630, "Query Planner", SMALL), (5680, "Tool Router", SMALL), (5730, "Composer", SMALL)):
        draw.text((centered_x - width(draw, text, active_font) // 2, y), text, font=active_font, fill=ORANGE if y < 5550 else MUTED)
    elbow(draw, [(550, 5530), (620, 5530), (620, 5550), (690, 5550)], ORANGE, dashed=True)
    elbow(draw, [(550, 5790), (620, 5790), (620, 7620), (540, 7620)], ORANGE, dashed=True)

    draw.text((120, 8610), "Trace / Metrics / Logs เก็บตลอดทุก stage ด้วย Request ID", font=SMALL, fill=MUTED)
    draw.text((2060, 8610), "LLM เป็นชั้นช่วยงาน ไม่ใช่แหล่งข้อมูลจริง", font=SMALL, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
