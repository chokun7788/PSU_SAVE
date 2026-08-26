from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MASTER_OUTPUT = DOCS / "psu_esports_chatbot_full_process_flow_20260824.png"
MODEL_OUTPUT = DOCS / "psu_esports_chatbot_semantic_rag_model_flow_20260824.png"

FONT_REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
FONT_BOLD_CANDIDATES = (
    Path(r"C:\Windows\Fonts\leelawdb.ttf"),
    Path(r"C:\Windows\Fonts\LeelawUIBold.ttf"),
    FONT_REGULAR,
)

BG = "#071019"
PANEL = "#0D1823"
PANEL_ALT = "#101E2A"
INK = "#F4F8FC"
MUTED = "#B5C2D0"
FAINT = "#718094"
LINE = "#395064"
CYAN = "#41C7E8"
BLUE = "#74A7FF"
GREEN = "#52D58A"
GOLD = "#F4CA64"
ORANGE = "#F59B61"
PINK = "#E983B6"
RED = "#F16F78"
PURPLE = "#A99AF7"
WHITE = "#FFFFFF"


def bold_path() -> Path:
    for path in FONT_BOLD_CANDIDATES:
        if path.exists():
            return path
    return FONT_REGULAR


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(bold_path() if bold else FONT_REGULAR), size=size)


F_TITLE = font(88, True)
F_SUBTITLE = font(38)
F_SECTION = font(51, True)
F_CARD_TITLE = font(39, True)
F_CARD_BODY = font(31)
F_CARD_SMALL = font(27)
F_TAG = font(25, True)
F_BADGE = font(29, True)
F_FOOT = font(26)


def text_width(draw: ImageDraw.ImageDraw, value: str, text_font: ImageFont.FreeTypeFont) -> float:
    if not value:
        return 0
    box = draw.textbbox((0, 0), value, font=text_font)
    return box[2] - box[0]


def wrap_text(
    draw: ImageDraw.ImageDraw,
    value: str,
    text_font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    for raw in value.splitlines() or [""]:
        raw = raw.strip()
        if not raw:
            lines.append("")
            continue
        words = raw.split(" ")
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if text_width(draw, candidate, text_font) <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
                current = ""
            if text_width(draw, word, text_font) <= max_width:
                current = word
                continue
            chunk = ""
            for char in word:
                candidate_chunk = chunk + char
                if text_width(draw, candidate_chunk, text_font) <= max_width:
                    chunk = candidate_chunk
                else:
                    if chunk:
                        lines.append(chunk)
                    chunk = char
            current = chunk
        if current:
            lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    text_font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 10,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrap_text(draw, value, text_font, max_width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines:
            lines[-1] = lines[-1].rstrip(" .") + "..."
    line_height = text_font.size + line_gap
    for line in lines:
        draw.text((x, y), line, font=text_font, fill=fill)
        y += line_height
    return y


def rounded_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str = PANEL,
    outline: str = LINE,
    radius: int = 26,
    width: int = 3,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def section(draw: ImageDraw.ImageDraw, y: int, number: str, title: str, color: str) -> None:
    draw.rounded_rectangle((170, y, 270, y + 66), radius=18, fill=color)
    draw.text((202, y + 7), number, font=F_BADGE, fill=BG)
    draw.text((300, y + 2), title, font=F_SECTION, fill=INK)
    title_end = 300 + int(text_width(draw, title, F_SECTION)) + 36
    draw.line((title_end, y + 38, 4630, y + 38), fill=LINE, width=3)


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    accent: str,
    tag: str | None = None,
    fill: str = PANEL_ALT,
    body_font: ImageFont.FreeTypeFont = F_CARD_BODY,
    max_lines: int | None = None,
) -> None:
    x1, y1, x2, y2 = box
    rounded_panel(draw, box, fill=fill, outline=LINE, radius=24, width=3)
    draw.rounded_rectangle((x1, y1, x1 + 17, y2), radius=9, fill=accent)
    title_y = y1 + 30
    if tag:
        tag_width = int(text_width(draw, tag, F_TAG)) + 38
        draw.rounded_rectangle((x2 - tag_width - 24, y1 + 22, x2 - 24, y1 + 61), radius=12, fill=accent)
        draw.text((x2 - tag_width - 5, y1 + 27), tag, font=F_TAG, fill=BG)
    draw.text((x1 + 47, title_y), title, font=F_CARD_TITLE, fill=INK)
    draw_wrapped(
        draw,
        (x1 + 47, y1 + 91),
        body,
        body_font,
        MUTED,
        max_width=x2 - x1 - 88,
        line_gap=10,
        max_lines=max_lines,
    )


def mini_badge(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    color: str,
    text_color: str = BG,
) -> int:
    x, y = xy
    width = int(text_width(draw, value, F_TAG)) + 38
    draw.rounded_rectangle((x, y, x + width, y + 45), radius=14, fill=color)
    draw.text((x + 19, y + 6), value, font=F_TAG, fill=text_color)
    return width


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = CYAN,
    width: int = 7,
    label: str | None = None,
) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 22
    left = (
        x2 - size * math.cos(angle) + size * 0.65 * math.sin(angle),
        y2 - size * math.sin(angle) - size * 0.65 * math.cos(angle),
    )
    right = (
        x2 - size * math.cos(angle) - size * 0.65 * math.sin(angle),
        y2 - size * math.sin(angle) + size * 0.65 * math.cos(angle),
    )
    draw.polygon((end, left, right), fill=color)
    if label:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        label_w = int(text_width(draw, label, F_TAG)) + 26
        draw.rounded_rectangle((mx - label_w // 2, my - 27, mx + label_w // 2, my + 20), radius=11, fill=BG, outline=color, width=2)
        draw.text((mx - label_w // 2 + 13, my - 20), label, font=F_TAG, fill=INK)


def elbow_arrow(
    draw: ImageDraw.ImageDraw,
    points: Iterable[tuple[int, int]],
    color: str = CYAN,
    width: int = 7,
    label: str | None = None,
) -> None:
    pts = list(points)
    if len(pts) < 2:
        return
    draw.line(pts, fill=color, width=width, joint="curve")
    arrow(draw, pts[-2], pts[-1], color=color, width=width, label=label)


def diamond(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    width: int,
    height: int,
    title: str,
    body: str,
    accent: str,
) -> tuple[int, int, int, int]:
    cx, cy = center
    pts = ((cx, cy - height // 2), (cx + width // 2, cy), (cx, cy + height // 2), (cx - width // 2, cy))
    draw.polygon(pts, fill=PANEL_ALT, outline=accent)
    draw.line(pts + (pts[0],), fill=accent, width=5)
    title_w = text_width(draw, title, F_CARD_TITLE)
    draw.text((cx - title_w / 2, cy - 57), title, font=F_CARD_TITLE, fill=INK)
    body_lines = wrap_text(draw, body, F_CARD_SMALL, width - 160)
    y = cy + 2
    for line in body_lines[:3]:
        line_w = text_width(draw, line, F_CARD_SMALL)
        draw.text((cx - line_w / 2, y), line, font=F_CARD_SMALL, fill=MUTED)
        y += F_CARD_SMALL.size + 8
    return (cx - width // 2, cy - height // 2, cx + width // 2, cy + height // 2)


def canvas(width: int, height: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)
    for y in range(0, height, 240):
        alpha = 18 if (y // 240) % 2 == 0 else 10
        color = (10 + alpha // 3, 20 + alpha // 2, 30 + alpha)
        draw.rectangle((0, y, width, min(height, y + 120)), fill=color)
    return image, draw


def header(
    draw: ImageDraw.ImageDraw,
    title: str,
    subtitle: str,
    labels: list[tuple[str, str]],
) -> None:
    draw.text((170, 100), title, font=F_TITLE, fill=INK)
    draw.text((174, 216), subtitle, font=F_SUBTITLE, fill=MUTED)
    x = 174
    for label, color in labels:
        width = mini_badge(draw, (x, 310), label, color)
        x += width + 18
    draw.line((170, 389, 4630, 389), fill=LINE, width=4)


def render_master() -> None:
    image, draw = canvas(4800, 8740)
    header(
        draw,
        "PSU ESPORTS CHATBOT — CURRENT FULL FLOW",
        "Local-first • จาก Setup/Warmup → Input → Understanding → Execution → Validation → Output",
        [
            ("Default: Fast + Structured", GREEN),
            ("Semantic RAG: Feature Gate", CYAN),
            ("Local LLM: Gated", GOLD),
            ("Backend Deadline: 9s", ORANGE),
            ("User-visible: ≤10s", RED),
        ],
    )

    # 1. Startup
    section(draw, 475, "1", "SETUP / WARMUP — เกิดก่อนรับคำถาม", GREEN)
    startup_boxes = [
        (170, 610, 1230, 1185),
        (1290, 610, 2350, 1185),
        (2410, 610, 3470, 1185),
        (3530, 610, 4630, 1185),
    ]
    card(draw, startup_boxes[0], "โหลด Configuration", "Typhoon 4B • context 2,048/3,072 • LLM calls ≤2 • concurrency 1 • compound workers 2 • deadline 9s + finalizer reserve", GREEN, "ทุกครั้งที่เปิด")
    card(draw, startup_boxes[1], "โหลด Structured Data", "42 เกม • ราคา • ตารางเปิด-ปิด • อุปกรณ์ • วิธีจอง/FAQ • rules • aliases • routing metadata • source trust", BLUE, "แกนหลัก")
    card(draw, startup_boxes[2], "โหลด Search Index", "Curated index • competition index • legacy hash/n-gram vector • semantic vector index 1,024 มิติ • query cache", CYAN, "RAG")
    card(draw, startup_boxes[3], "Warm Models ตาม Feature", "BGE-M3 Q8 embedding • Ollama health/preflight • Typhoon warm call • optional CrossEncoder เฉพาะ profile ที่เปิด • keep_alive 10m", GOLD, "มีเงื่อนไข")

    # 2. Request edge
    section(draw, 1310, "2", "INPUT / REQUEST EDGE — ช่องทางเข้าและด่านควบคุม", CYAN)
    intake_boxes = [
        (170, 1450, 980, 1810),
        (1030, 1450, 1840, 1810),
        (1890, 1450, 2700, 1810),
        (2750, 1450, 3560, 1810),
        (3610, 1450, 4630, 1810),
    ]
    for left, right in zip(intake_boxes, intake_boxes[1:]):
        arrow(draw, (left[2] + 5, (left[1] + left[3]) // 2), (right[0] - 7, (right[1] + right[3]) // 2), CYAN, 6)
    card(draw, intake_boxes[0], "Web / API", "POST /api/chat • JSON • Facebook adapter ยังเป็นงานต่อ", CYAN, "Input", body_font=F_CARD_SMALL)
    card(draw, intake_boxes[1], "Validate Intake", "body ≤128 KiB • question ≤4,000 chars • ตรวจ schema/field", BLUE, body_font=F_CARD_SMALL)
    card(draw, intake_boxes[2], "Identity", "request_id ใหม่ต่อคำขอ • client_session_id แยกบทสนทนา", PURPLE, body_font=F_CARD_SMALL)
    card(draw, intake_boxes[3], "Admission Control", "active requests ≤16/process • session lock 0.10s • 503/409 เมื่อเต็ม", ORANGE, body_font=F_CARD_SMALL)
    card(draw, intake_boxes[4], "Global Deadline", "นาฬิการวม 9s • สำรอง finalizer ~1s • ทุกโมดูลดู remaining time", RED, "เป้าหมาย ≤10s", body_font=F_CARD_SMALL)

    context_boxes = [
        (370, 1910, 1550, 2260),
        (1810, 1910, 2990, 2260),
        (3250, 1910, 4430, 2260),
    ]
    arrow(draw, (960, 2268), (960, 2332), CYAN)
    arrow(draw, (2400, 2268), (2400, 2332), CYAN)
    arrow(draw, (3840, 2268), (3840, 2332), CYAN)
    card(draw, context_boxes[0], "Session Context Resolver", "อ่าน recent history (หน้าเว็บส่งราว 10 messages) • resolve ‘เกมนั้น/อันเดิม’ จาก evidence • ไม่ชัดให้ถามกลับ", PURPLE)
    card(draw, context_boxes[1], "Split Multi-question", "แยกคำถามย่อยด้วย punctuation • คำเชื่อม • intent marker • รักษาลำดับและ reference", BLUE)
    card(draw, context_boxes[2], "Request Context", "เปิด request deadline context • reset LLM budget ≤2 • trace latency/mode/route/source ต่อ request", GREEN)

    # 3. Multi handling
    section(draw, 2380, "3", "MULTI-QUESTION ORCHESTRATION — แยกความซับซ้อนและ dependency", BLUE)
    decision = diamond(draw, (980, 2765), 1220, 560, "Complexity Gate", "Single / Simple independent / Dependent / Broad-complex", BLUE)
    multi_boxes = [
        (1780, 2470, 2700, 3035),
        (2840, 2470, 3760, 3035),
        (3900, 2470, 4630, 3035),
    ]
    arrow(draw, (decision[2] + 10, 2765), (multi_boxes[0][0] - 15, 2765), BLUE, label="Single")
    card(draw, multi_boxes[0], "คำถามเดียว", "ส่งเข้า Single-question Understanding Pipeline โดยตรง", GREEN, "1 task")
    card(draw, multi_boxes[1], "Simple Independent", "ถ้าทุก child deterministic: bounded parallel สูงสุด 2 workers • ปิด child experimental model calls", CYAN, "ขนาน")
    card(draw, multi_boxes[2], "Dependent / Complex", "Optional LLM Query Planner JSON ≤4 tasks (cap 4s) • fail แล้ว fallback deterministic • รันตาม dependency", GOLD, "ตามลำดับ", body_font=F_CARD_SMALL)
    elbow_arrow(draw, [(980, 3045), (980, 3130), (3300, 3130), (3300, 3050)], CYAN, 6, "Independent")
    elbow_arrow(draw, [(980, 3045), (980, 3200), (4265, 3200), (4265, 3050)], GOLD, 6, "Dependent / Complex")

    # 4. Understanding
    section(draw, 3260, "4", "SINGLE-QUESTION UNDERSTANDING — วิเคราะห์ก่อนเลือกเครื่องมือ", PURPLE)
    row_x = [(170, 1210), (1275, 2315), (2380, 3420), (3485, 4630)]
    row1_y = (3400, 3760)
    row2_y = (3840, 4200)
    row3_y = (4280, 4660)
    for row_y in (row1_y, row2_y, row3_y):
        for left, right in zip(row_x, row_x[1:]):
            arrow(draw, (left[1] + 5, (row_y[0] + row_y[1]) // 2), (right[0] - 7, (row_y[0] + row_y[1]) // 2), PURPLE, 5)
    arrow(draw, (4058, row1_y[1] + 6), (4058, row2_y[0] - 8), PURPLE, 5)
    arrow(draw, (722, row2_y[1] + 6), (722, row3_y[0] - 8), PURPLE, 5)
    row_box = lambda column, band: (column[0], band[0], column[1], band[1])
    card(draw, row_box(row_x[0], row1_y), "1) Normalize", "clean text • query variants • ภาษาไทย/อังกฤษ/ผสม", BLUE, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[1], row1_y), "2) Entities", "เกม • บริการ • วัน/เวลา • คน • ระยะเวลา • ราคา", GREEN, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[2], row1_y), "3) Heuristic Route", "keyword + form + priority → pricing/schedule/games/...", ORANGE, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[3], row1_y), "4) Semantic Route Refiner", "ถ้าเปิด BGE: ยืนยัน/ปรับ knowledge • events_news • about_us พร้อม route protection", CYAN, "Optional", body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[0], row2_y), "5) Freshness Gate", "ล่าสุด/วันนี้ → published + verified + valid_until + trust", RED, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[1], row2_y), "6) Missing Input", "operation ขาด target/date/service → clarification", GOLD, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[2], row2_y), "7) Boundary / Scope", "PSU หรือทั่วไป? ป้องกันข้อมูลคนละร้าน/คนละหมวด", ORANGE, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[3], row2_y), "8) Model Preflight", "LLM allowed? quota? queue? health? remaining time? reserve call?", GOLD, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[0], row3_y), "9) Universal Intent", "domain • operation • target • filters • needs • style", PURPLE, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[1], row3_y), "10) Optional LLM Review", "Intent review / Tool Router เป็น JSON • schema + allowlist + deterministic veto", GOLD, "Gated", body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[2], row3_y), "11) Ambiguity Gate", "หลาย target? top scores ใกล้? reference ไม่ชัด? → ถามกลับ", RED, body_font=F_CARD_SMALL)
    card(draw, row_box(row_x[3], row3_y), "12) Frame / Direct Decision", "semantic route locked → direct evidence; ไม่เช่นนั้นสร้าง Question Frame + candidate scoring", CYAN, body_font=F_CARD_SMALL)

    # 5. Execution paths
    section(draw, 4780, "5", "EXECUTION PATHS — เลือกตาม operation, target, evidence และเวลา", ORANGE)
    path_boxes = [
        (170, 4920, 1590, 5350),
        (1690, 4920, 3110, 5350),
        (3210, 4920, 4630, 5350),
        (170, 5440, 1590, 5870),
        (1690, 5440, 3110, 5870),
        (3210, 5440, 4630, 5870),
    ]
    card(draw, path_boxes[0], "A. Fast / Rule / Calculator", "ราคา • ตาราง • identity • check-in/payment FAQ • deterministic draft • เร็วที่สุด", GREEN, "Default")
    card(draw, path_boxes[1], "B. Structured Tools", "42 games • equipment • members • schedule • reservation • service fee • query ตาม field", BLUE, "Default")
    card(draw, path_boxes[2], "C. Competition / Controls", "fact cards แยกหมวด • resolve เกม • verified source ก่อน • guarded retrieval เมื่อจำเป็น", ORANGE)
    card(draw, path_boxes[3], "D. Hybrid RAG", "Curated + lexical/hash + BGE semantic • filter/dedupe • hybrid score • optional CrossEncoder", CYAN, "ตามหมวด")
    card(draw, path_boxes[4], "E. Semantic RAG Direct", "BGE embed → dense search → source/category/freshness/score/margin → grounded evidence", CYAN, "Feature Gate")
    card(draw, path_boxes[5], "F. General / Safe Outcomes", "General LLM เฉพาะ non-PSU facts • clarification • no-answer • out-of-scope • safe timeout", RED, "Gated")

    # 6. Evidence and models
    section(draw, 5990, "6", "RAG + LOCAL LLM — ใช้ Model เฉพาะเมื่อ evidence และ budget เหมาะสม", GOLD)
    rag_boxes = [
        (170, 6140, 1010, 6535),
        (1060, 6140, 1900, 6535),
        (1950, 6140, 2790, 6535),
        (2840, 6140, 3680, 6535),
        (3730, 6140, 4630, 6535),
    ]
    for left, right in zip(rag_boxes, rag_boxes[1:]):
        arrow(draw, (left[2] + 5, 6338), (right[0] - 7, 6338), CYAN, 5)
    card(draw, rag_boxes[0], "Documents", "published chunks • official source • validity metadata", BLUE, body_font=F_CARD_SMALL)
    card(draw, rag_boxes[1], "BGE-M3 Q8", "query vector 1,024 dim • LRU cache • ~333 MiB runtime", CYAN, body_font=F_CARD_SMALL)
    card(draw, rag_boxes[2], "Retrieve / Rerank", "cosine + lexical + priority + trust • threshold + margin", CYAN, body_font=F_CARD_SMALL)
    card(draw, rag_boxes[3], "Evidence + Draft", "claim ที่อนุญาต • source marker • deterministic answer สำรอง", GREEN, body_font=F_CARD_SMALL)
    card(draw, rag_boxes[4], "Model Gateway", "1 high-confidence hit → ไม่เรียก LLM • หลาย hits + ≥6s + quota → Composer", GOLD, body_font=F_CARD_SMALL)

    composer_boxes = [
        (370, 6660, 1550, 7050),
        (1810, 6660, 2990, 7050),
        (3250, 6660, 4430, 7050),
    ]
    arrow(draw, (1558, 6855), (1802, 6855), GOLD, 6)
    arrow(draw, (2998, 6855), (3242, 6855), GOLD, 6)
    card(draw, composer_boxes[0], "Typhoon Facts Composer", "context 3,072 • output ≤192 • timeout 5s • stream • เรียบเรียง evidence เท่านั้น", GOLD)
    card(draw, composer_boxes[1], "Grounding Check", "ห้ามเพิ่มชื่อเกม ราคา เวลา ตัวเลข กฎ • ตรวจ source • done_reason=length → reject", RED)
    card(draw, composer_boxes[2], "Deterministic Fallback", "Composer fail/timeout/unsupported claim → คืน draft ที่ตรวจแล้ว ไม่เรียกซ้ำไม่รู้จบ", GREEN)

    # 7. Validation
    section(draw, 7180, "7", "VALIDATION / REPAIR / FINAL HARD VETO", RED)
    validation_boxes = [
        (170, 7325, 990, 7725),
        (1040, 7325, 1860, 7725),
        (1910, 7325, 2730, 7725),
        (2780, 7325, 3600, 7725),
        (3650, 7325, 4630, 7725),
    ]
    for left, right in zip(validation_boxes, validation_boxes[1:]):
        arrow(draw, (left[2] + 5, 7525), (right[0] - 7, 7525), RED, 5)
    card(draw, validation_boxes[0], "Path Validator", "ตรวจ unit/target/source/completeness ตาม path", ORANGE, body_font=F_CARD_SMALL)
    card(draw, validation_boxes[1], "Answer Contract", "operation + answer type + target + category + evidence", RED, body_font=F_CARD_SMALL)
    card(draw, validation_boxes[2], "Bounded Repair", "ลอง candidate ถัดไป 1 ครั้ง / ตัด source / ใช้ draft / ถามกลับ", GOLD, body_font=F_CARD_SMALL)
    card(draw, validation_boxes[3], "Final Hard Veto", "ยังมี hard error → ไม่ปล่อยคำตอบเดิม → no-answer/clarification", RED, body_font=F_CARD_SMALL)
    card(draw, validation_boxes[4], "Thai Formatter + Result", "answer-first • mode • route • confidence • sources • trace • validation", GREEN, body_font=F_CARD_SMALL)

    # 8. Output
    section(draw, 7845, "8", "OUTPUT / OBSERVABILITY", GREEN)
    output_boxes = [
        (170, 7985, 1230, 8355),
        (1290, 7985, 2350, 8355),
        (2410, 7985, 3470, 8355),
        (3530, 7985, 4630, 8355),
    ]
    card(draw, output_boxes[0], "API Response", "request_id • answer • mode/route • confidence • latency • sources • validation", GREEN)
    card(draw, output_boxes[1], "User Channels", "Web chat พร้อมใช้ • Facebook webhook/send adapter ยังต้องทำ production integration", CYAN)
    card(draw, output_boxes[2], "Async Logs", "request/session trace • stage timing • LLM calls/queue • errors • source • decision artifact", PURPLE)
    card(draw, output_boxes[3], "Product Metrics", "pass rate • average/P95/max • timeout • queue wait • session isolation • unsupported claims", GOLD)

    draw.text((170, 8470), "CURRENT LIMITS", font=F_BADGE, fill=RED)
    draw_wrapped(draw, (465, 8465), "in-process queue/locks • persistent session store ยังไม่มี • Facebook/booking transaction ยังไม่พร้อม • ต้อง rerun full 1,600+ หลัง changes ล่าสุด • ต้อง load test peak users", F_FOOT, MUTED, 4140, line_gap=8)
    draw.text((170, 8665), "Generated from the current code path • 2026-08-24 • Detail: docs/43_current_chatbot_full_process_flow_20260824.md", font=F_FOOT, fill=FAINT)

    DOCS.mkdir(parents=True, exist_ok=True)
    image.save(MASTER_OUTPUT, format="PNG", optimize=True)


def render_model_zoom() -> None:
    image, draw = canvas(4800, 5920)
    header(
        draw,
        "SEMANTIC RAG + LOCAL LLM — DETAIL FLOW",
        "แยก Offline ingestion, Online retrieval, Route discovery, Rerank, Composer และ deterministic fallback",
        [
            ("Embedding: BGE-M3 Q8", CYAN),
            ("Composer: Typhoon 4B", GOLD),
            ("Vector: 1,024 dim", BLUE),
            ("Model calls/request ≤2", ORANGE),
            ("Deadline aware", RED),
        ],
    )

    section(draw, 475, "A", "OFFLINE / UPDATE FLOW — เพิ่มข้อมูลใหม่ก่อนให้ระบบค้น", BLUE)
    offline = [
        (170, 620, 1130, 1110),
        (1210, 620, 2170, 1110),
        (2250, 620, 3210, 1110),
        (3290, 620, 4630, 1110),
    ]
    for left, right in zip(offline, offline[1:]):
        arrow(draw, (left[2] + 5, 865), (right[0] - 7, 865), BLUE, 6)
    card(draw, offline[0], "1) Knowledge Inbox", "ไฟล์ข้อมูลใหม่: id • title • text • category • source_url • trust • updated_at • status", BLUE)
    card(draw, offline[1], "2) Validate + Publish", "schema ครบ? source เชื่อถือได้? draft/published/archived • freshness/validity สำหรับข่าว", RED)
    card(draw, offline[2], "3) Chunk", "แบ่งข้อความประมาณ ≤900 ตัวอักษร • overlap 120 • รักษา metadata ทุก chunk", GREEN)
    card(draw, offline[3], "4) Embed + Build Index", "BGE-M3 Q8 สร้าง vector 1,024 มิติ → data/vector/psu_semantic_vector_index.json • ปัจจุบันราว 112 docs", CYAN)

    section(draw, 1240, "B", "ONLINE QUERY FLOW — เริ่มจากข้อความผู้ใช้", CYAN)
    online = [
        (170, 1385, 990, 1815),
        (1040, 1385, 1860, 1815),
        (1910, 1385, 2730, 1815),
        (2780, 1385, 3600, 1815),
        (3650, 1385, 4630, 1815),
    ]
    for left, right in zip(online, online[1:]):
        arrow(draw, (left[2] + 5, 1600), (right[0] - 7, 1600), CYAN, 5)
    card(draw, online[0], "1) Normalize", "query variants • entities • route hints", BLUE, body_font=F_CARD_SMALL)
    card(draw, online[1], "2) Embed Query", "Ollama BGE-M3 Q8 • context 1,024 • LRU cache", CYAN, body_font=F_CARD_SMALL)
    card(draw, online[2], "3) Dense Search", "cosine similarity กับ document vectors", CYAN, body_font=F_CARD_SMALL)
    card(draw, online[3], "4) Hybrid Signals", "lexical overlap • priority • trust bonus • category/entity", PURPLE, body_font=F_CARD_SMALL)
    card(draw, online[4], "5) Candidate Set", "dedupe • published/valid filter • เก็บ top candidates", GREEN, body_font=F_CARD_SMALL)

    section(draw, 1950, "C", "ROUTE DISCOVERY + EVIDENCE GUARDS", PURPLE)
    route_boxes = [
        (170, 2095, 1260, 2575),
        (1350, 2095, 2440, 2575),
        (2530, 2095, 3620, 2575),
        (3710, 2095, 4630, 2575),
    ]
    for left, right in zip(route_boxes, route_boxes[1:]):
        arrow(draw, (left[2] + 5, 2335), (right[0] - 7, 2335), PURPLE, 6)
    card(draw, route_boxes[0], "Semantic Route Refiner", "อนุญาตหลัก: knowledge • events_news • about_us • ป้องกัน explicit price/game/rules route", PURPLE)
    card(draw, route_boxes[1], "Score + Margin", "top score ต้องผ่าน threshold • top1-top2 margin ต้องพอ • ไม่เชื่อ nearest อย่างเดียว", CYAN)
    card(draw, route_boxes[2], "Source / Freshness", "official/verified • category/target ตรง • published • valid_until • freshness_verified เมื่อถามล่าสุด", RED)
    card(draw, route_boxes[3], "Route Lock / Ambiguity", "ชัด → lock semantic direct • ไม่ชัด → candidate เดิม/clarification/no-answer", GREEN)

    section(draw, 2705, "D", "OPTIONAL DOCUMENT RERANK", ORANGE)
    rerank = [
        (310, 2850, 1650, 3260),
        (1730, 2850, 3070, 3260),
        (3150, 2850, 4490, 3260),
    ]
    arrow(draw, (1658, 3055), (1722, 3055), ORANGE, 6)
    arrow(draw, (3078, 3055), (3142, 3055), ORANGE, 6)
    card(draw, rerank[0], "Lightweight Hybrid Rerank", "semantic + lexical + metadata score • เป็นส่วน online ที่เบากว่า", CYAN)
    card(draw, rerank[1], "CrossEncoder Gate", "เปิด flag? candidates ≥2? ranking ยังไม่ชัด? remaining time พอ? model warm?", ORANGE)
    card(draw, rerank[2], "BAAI/bge-reranker-v2-m3", "อ่าน query-document เป็นคู่ • optional • Python CPU cold ~87-93s จึงข้ามใน request 9s เมื่อยัง cold", RED)

    section(draw, 3390, "E", "MODEL GATEWAY — เลือกว่าจะเรียก Typhoon หรือไม่", GOLD)
    gateway = diamond(draw, (1150, 3800), 1500, 610, "ใช้ Composer หรือไม่?", "LLM allowed • healthy • quota • queue • remaining ≥6s • evidence ไม่ conflict", GOLD)
    no_model = (2130, 3500, 3260, 4085)
    use_model = (3420, 3500, 4630, 4085)
    arrow(draw, (gateway[2] + 10, 3700), (no_model[0] - 12, 3700), GREEN, 6, "ไม่ใช้")
    arrow(draw, (gateway[2] + 10, 3930), (use_model[0] - 12, 3930), GOLD, 6, "ใช้")
    card(draw, no_model, "Deterministic Answer", "ใช้เมื่อ evidence เดียว confidence ≥0.86 • exact fact • source conflict • เวลาไม่พอ • model ปิด/ไม่พร้อม", GREEN, "เร็ว/เสถียร")
    card(draw, use_model, "Typhoon Facts Composer", "หลาย evidence • context 3,072 • output ≤192 • timeout 5s • stream • compact evidence JSON", GOLD, "Gated")

    section(draw, 4215, "F", "GROUNDED COMPOSITION + FALLBACK", RED)
    compose = [
        (170, 4360, 1130, 4830),
        (1210, 4360, 2170, 4830),
        (2250, 4360, 3210, 4830),
        (3290, 4360, 4630, 4830),
    ]
    for left, right in zip(compose, compose[1:]):
        arrow(draw, (left[2] + 5, 4595), (right[0] - 7, 4595), RED, 6)
    card(draw, compose[0], "Evidence + Draft", "model เห็นเฉพาะ claims/source ที่อนุญาต และมี deterministic draft สำรอง", BLUE)
    card(draw, compose[1], "Compose", "เรียบเรียง answer-first • bullet สั้น • ห้ามเพิ่มราคา เวลา ชื่อเกม ตัวเลข หรือกฎ", GOLD)
    card(draw, compose[2], "Grounding Validate", "unsupported claims • numeric/source mismatch • incomplete generation • done_reason=length", RED)
    card(draw, compose[3], "Accept หรือ Fallback", "ผ่าน → ใช้ composed answer • ไม่ผ่าน/timeout → deterministic draft • ไม่มี evidence → no-answer", GREEN)

    section(draw, 4960, "G", "RESOURCE / LATENCY PROFILE และข้อจำกัด", GREEN)
    resources = [
        (170, 5110, 1590, 5580),
        (1690, 5110, 3110, 5580),
        (3210, 5110, 4630, 5580),
    ]
    card(draw, resources[0], "BGE-M3 Q8", "runtime ~333 MiB • avg query benchmark ~0.459s • vector 1,024 dim • keep_alive 10m", CYAN)
    card(draw, resources[1], "Typhoon 4B Q4_K_M", "runtime ~2.74 GiB @ctx2048 • ~2.89 GiB @ctx3072 • warm generation probe ~1.5s สำหรับ prompt สั้น", GOLD)
    card(draw, resources[2], "Product Risk", "LLM concurrency 1 + in-process queue • peak 20 users ยังต้อง load test • cold load • Ollama hard cancel ยัง best effort", RED)

    draw.text((170, 5710), "สำคัญ: RAG หา evidence; BGE ทำ embedding/ranking; Typhoon เรียบเรียงเมื่อจำเป็น — ทั้งสามอย่างไม่ใช่หน้าที่เดียวกัน", font=F_CARD_TITLE, fill=INK)
    draw.text((170, 5810), "Generated 2026-08-24 • Full explanation: docs/43_current_chatbot_full_process_flow_20260824.md", font=F_FOOT, fill=FAINT)

    DOCS.mkdir(parents=True, exist_ok=True)
    image.save(MODEL_OUTPUT, format="PNG", optimize=True)


def main() -> None:
    render_master()
    render_model_zoom()
    print(MASTER_OUTPUT)
    print(MODEL_OUTPUT)


if __name__ == "__main__":
    main()
