from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "current_chatbot_full_process_flow_th_20260803.png"

WIDTH = 3840
HEIGHT = 2700

BG = "#061426"
PANEL = "#0b1d33"
TEXT = "#f7f9fc"
MUTED = "#b9c8dc"
WHITE = "#eaf1fa"
GREEN = "#80c342"
GREEN_FILL = "#102f2a"
BLUE = "#3f9cff"
BLUE_FILL = "#0d2944"
ORANGE = "#ff9d3d"
ORANGE_FILL = "#352517"
RED = "#ff525c"
RED_FILL = "#351b25"
CYAN = "#45d3c5"
CYAN_FILL = "#0d3035"
GRAY = "#91a5bd"

FONT_REGULAR_PATH = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
FONT_BOLD_PATH = Path(r"C:\Windows\Fonts\leelawdb.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD_PATH if bold and FONT_BOLD_PATH.exists() else FONT_REGULAR_PATH
    return ImageFont.truetype(str(path), size=size)


TITLE_FONT = font(88, True)
SUBTITLE_FONT = font(34)
SECTION_FONT = font(34, True)
BOX_TITLE_FONT = font(36, True)
BOX_BODY_FONT = font(25)
SMALL_FONT = font(22)
LABEL_FONT = font(24, True)
NUMBER_FONT = font(30, True)


def rounded_box(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    *,
    outline: str,
    fill: str = PANEL,
    width: int = 5,
    radius: int = 24,
    shadow: bool = True,
) -> None:
    x1, y1, x2, y2 = rect
    if shadow:
        draw.rounded_rectangle(
            (x1 + 12, y1 + 14, x2 + 12, y2 + 14),
            radius=radius,
            fill="#020914",
        )
    draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)


def draw_text_centered(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    text: str,
    text_font: ImageFont.FreeTypeFont,
    *,
    fill: str = TEXT,
    spacing: int = 8,
) -> None:
    x1, y1, x2, y2 = rect
    bbox = draw.multiline_textbbox((0, 0), text, font=text_font, spacing=spacing, align="center")
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = x1 + (x2 - x1 - tw) / 2
    y = y1 + (y2 - y1 - th) / 2 - bbox[1]
    draw.multiline_text((x, y), text, font=text_font, fill=fill, spacing=spacing, align="center")


def process_box(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    *,
    number: int | str,
    title: str,
    body: str,
    color: str = WHITE,
    fill: str = PANEL,
    title_size: int | None = None,
    body_size: int | None = None,
) -> None:
    rounded_box(draw, rect, outline=color, fill=fill)
    x1, y1, x2, y2 = rect
    circle_x = x1 + 42
    circle_y = y1 + 42
    draw.ellipse((circle_x - 25, circle_y - 25, circle_x + 25, circle_y + 25), fill=color)
    number_fill = BG if color != WHITE else PANEL
    num_font = font(28, True)
    nb = draw.textbbox((0, 0), str(number), font=num_font)
    draw.text(
        (circle_x - (nb[2] - nb[0]) / 2, circle_y - (nb[3] - nb[1]) / 2 - nb[1]),
        str(number),
        font=num_font,
        fill=number_fill,
    )

    title_font = font(title_size or 36, True)
    body_font = font(body_size or 25)
    title_top = y1 + 22
    title_left = x1 + 86
    draw.multiline_text(
        (title_left, title_top),
        title,
        font=title_font,
        fill=TEXT,
        spacing=4,
    )
    body_bbox = draw.multiline_textbbox((0, 0), body, font=body_font, spacing=9, align="center")
    body_w = body_bbox[2] - body_bbox[0]
    body_h = body_bbox[3] - body_bbox[1]
    body_x = x1 + (x2 - x1 - body_w) / 2
    body_y = y1 + 104 + max(0, (y2 - y1 - 116 - body_h) / 2) - body_bbox[1]
    draw.multiline_text(
        (body_x, body_y),
        body,
        font=body_font,
        fill=MUTED,
        spacing=9,
        align="center",
    )


def diamond(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    *,
    text: str,
    color: str = WHITE,
    fill: str = PANEL,
    text_size: int = 31,
) -> None:
    x1, y1, x2, y2 = rect
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    shadow_points = [(x + 12, y + 14) for x, y in points]
    draw.polygon(shadow_points, fill="#020914")
    draw.polygon(points, fill=fill)
    draw.line(points + [points[0]], fill=color, width=5, joint="curve")
    draw_text_centered(draw, rect, text, font(text_size, True), fill=TEXT, spacing=6)


def arrow_head(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str) -> None:
    x1, y1 = start
    x2, y2 = end
    angle = math.atan2(y2 - y1, x2 - x1)
    length = 22
    width = 12
    bx = x2 - length * math.cos(angle)
    by = y2 - length * math.sin(angle)
    left = (bx + width * math.sin(angle), by - width * math.cos(angle))
    right = (bx - width * math.sin(angle), by + width * math.cos(angle))
    draw.polygon([(x2, y2), left, right], fill=color)


def arrow(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    *,
    color: str = WHITE,
    width: int = 5,
    label: str = "",
    label_at: tuple[int, int] | None = None,
) -> None:
    draw.line(points, fill=color, width=width, joint="curve")
    arrow_head(draw, points[-2], points[-1], color)
    if label and label_at:
        lb = draw.textbbox((0, 0), label, font=LABEL_FONT)
        pad_x = 12
        pad_y = 6
        x, y = label_at
        draw.rounded_rectangle(
            (x - pad_x, y - pad_y, x + (lb[2] - lb[0]) + pad_x, y + (lb[3] - lb[1]) + pad_y),
            radius=10,
            fill=BG,
        )
        draw.text((x, y - lb[1]), label, font=LABEL_FONT, fill=color)


def section_label(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color: str) -> None:
    draw.rounded_rectangle((x, y, x + 18, y + 44), radius=8, fill=color)
    draw.text((x + 34, y - 4), text, font=SECTION_FONT, fill=TEXT)


def legend_item(draw: ImageDraw.ImageDraw, x: int, y: int, color: str, label: str) -> int:
    draw.rounded_rectangle((x, y, x + 58, y + 34), radius=7, fill=color)
    draw.text((x + 76, y - 6), label, font=SMALL_FONT, fill=MUTED)
    return x + 76 + int(draw.textlength(label, font=SMALL_FONT)) + 80


def main() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)

    # Quiet grid improves scanning without competing with the flow.
    for x in range(80, WIDTH, 160):
        draw.line((x, 190, x, 2300), fill="#0a2038", width=1)
    for y in range(220, 2300, 120):
        draw.line((60, y, WIDTH - 60, y), fill="#0a2038", width=1)

    title = "PSU Esports Chatbot: Flow ปัจจุบัน"
    subtitle = "Architecture และ Process จริง ณ วันที่ 3 สิงหาคม 2026  |  correctness_control_flow_v2"
    title_bbox = draw.textbbox((0, 0), title, font=TITLE_FONT)
    title_x = (WIDTH - (title_bbox[2] - title_bbox[0])) / 2
    draw.text((title_x, 30), title, font=TITLE_FONT, fill=TEXT)
    sub_bbox = draw.textbbox((0, 0), subtitle, font=SUBTITLE_FONT)
    sub_x = (WIDTH - (sub_bbox[2] - sub_bbox[0])) / 2
    draw.text((sub_x, 132), subtitle, font=SUBTITLE_FONT, fill=MUTED)
    draw.line((80, 192, WIDTH - 80, 192), fill="#294864", width=3)

    section_label(draw, 80, 225, "รับคำถามและทำความเข้าใจ", CYAN)

    row1_y1, row1_y2 = 300, 610
    process_box(
        draw,
        (80, row1_y1, 500, row1_y2),
        number=1,
        title="User Input",
        body="Local CLI / Web API / Notebook\nคำถามไทย อังกฤษ หรือผสม",
        color=WHITE,
    )
    process_box(
        draw,
        (560, row1_y1, 1130, row1_y2),
        number=2,
        title="Session Context",
        body="เติม target/operation จาก history\nTTL + topic-shift guard\ntarget ใหม่ชนะ context เก่า",
        color=CYAN,
        fill=CYAN_FILL,
    )
    process_box(
        draw,
        (1190, row1_y1, 1810, row1_y2),
        number=3,
        title="Deadline + Compound",
        body="Global budget เดียวไม่เกิน 20s\nแยกหลายคำถามเป็น child\nรวมคำตอบและ source เป็นข้อ",
        color=CYAN,
        fill=CYAN_FILL,
    )
    process_box(
        draw,
        (1870, row1_y1, 2520, row1_y2),
        number=4,
        title="Preprocess + Entity",
        body="normalize / alias / typo / variants\nเกม โซน วัน เวลา กลุ่ม ราคา\nเลือก query variant ที่ route ดีสุด",
        color=CYAN,
        fill=CYAN_FILL,
    )
    process_box(
        draw,
        (2580, row1_y1, 3760, row1_y2),
        number=5,
        title="Router Stack",
        body="Scope Guard -> Heuristic Router -> Priority Matrix\nSemantic char n-gram -> Universal Intent\nroute ชัดใช้ heuristic | route อ่อนค่อย review",
        color=WHITE,
    )

    arrow(draw, [(500, 455), (560, 455)])
    arrow(draw, [(1130, 455), (1190, 455)])
    arrow(draw, [(1810, 455), (1870, 455)])
    arrow(draw, [(2520, 455), (2580, 455)])

    section_label(draw, 80, 685, "ควบคุมความกำกวมและเลือกความสามารถ", GREEN)

    row2_y1, row2_y2 = 760, 1085
    process_box(
        draw,
        (2840, row2_y1, 3760, row2_y2),
        number=6,
        title="Adaptive Review",
        body="IF weak / mixed / risky\nOptional Intent LLM + Tool Router\nเลือกจาก candidate JSON เท่านั้น\nfail/timeout -> กลับ heuristic",
        color=ORANGE,
        fill=ORANGE_FILL,
    )
    process_box(
        draw,
        (1930, row2_y1, 2760, row2_y2),
        number=7,
        title="Ambiguity Gate v2",
        body="intent candidate scoring\nnegative guard + margin threshold\nขาด target -> clarify + preview\nไม่เดาชื่อเกมหรือ operation",
        color=RED,
        fill=RED_FILL,
    )
    process_box(
        draw,
        (1010, row2_y1, 1850, row2_y2),
        number=8,
        title="Question Frame + Target",
        body="operation-first + expected answer type\nexact / alias / compact / fuzzy / family\nOptional gated BGE entity reranker\nlow margin ยังคง ambiguous",
        color=BLUE,
        fill=BLUE_FILL,
        title_size=34,
    )
    process_box(
        draw,
        (80, row2_y1, 930, row2_y2),
        number=9,
        title="Capability Scoring",
        body="จัดอันดับ 17 capabilities\ndomain + operation + answer type\npolicy veto + tool preconditions\nscore ต่ำหรือ margin สูสี -> abstain",
        color=GREEN,
        fill=GREEN_FILL,
    )

    # Router can skip the orange box when confident.
    arrow(draw, [(3170, 610), (3170, 760)], color=ORANGE, label="IF route อ่อน", label_at=(3192, 665))
    arrow(draw, [(2840, 920), (2760, 920)], color=ORANGE)
    arrow(draw, [(1930, 920), (1850, 920)], color=WHITE)
    arrow(draw, [(1010, 920), (930, 920)], color=WHITE)
    arrow(
        draw,
        [(2860, 610), (2800, 610), (2800, 710), (2380, 710), (2380, 760)],
        color=GREEN,
        label="IF route ชัด ข้าม LLM",
        label_at=(2420, 664),
    )

    section_label(draw, 80, 1155, "Execute เฉพาะเส้นทางที่ผ่าน precondition", GREEN)

    diamond(
        draw,
        (90, 1260, 600, 1580),
        text="เลือก capability\nได้อย่างปลอดภัย?",
        color=WHITE,
        fill=PANEL,
        text_size=30,
    )
    arrow(draw, [(500, 1085), (500, 1160), (345, 1160), (345, 1260)])

    process_box(
        draw,
        (740, 1215, 1640, 1655),
        number=10,
        title="Structured / Fast",
        body="Early price calculator\nMembers / Games / Controls / Equipment\nReservation / Schedule / Service Fee\nDeterministic domain handlers + rules",
        color=GREEN,
        fill=GREEN_FILL,
    )
    process_box(
        draw,
        (1740, 1215, 2640, 1655),
        number=11,
        title="Retrieval / RAG",
        body="Game-control vector-first\nCompetition fact cards\nGuarded hybrid -> curated -> vector\ncategory + entity + source thresholds",
        color=BLUE,
        fill=BLUE_FILL,
    )
    process_box(
        draw,
        (2740, 1215, 3640, 1655),
        number=12,
        title="Optional Model Path",
        body="Facts Composer: verified facts เท่านั้น\nGeneral Local LLM: non-PSU เท่านั้น\nHealth Manager + Circuit Breaker\nทุก call ถูกจำกัดด้วย deadline",
        color=ORANGE,
        fill=ORANGE_FILL,
    )
    process_box(
        draw,
        (80, 1650, 650, 1870),
        number="S",
        title="Safe Abstain",
        body="Clarification / No-answer\nTimeout-safe result\nห้าม LLM เดาข้อมูล PSU",
        color=RED,
        fill=RED_FILL,
        title_size=32,
        body_size=23,
    )

    arrow(draw, [(600, 1420), (740, 1420)], color=GREEN, label="ผ่าน", label_at=(635, 1376))
    arrow(draw, [(520, 1530), (520, 1650)], color=RED, label="ไม่ผ่าน", label_at=(540, 1582))
    arrow(draw, [(600, 1360), (660, 1360), (660, 1180), (1690, 1180), (1690, 1420), (1740, 1420)], color=BLUE)
    arrow(draw, [(600, 1300), (690, 1300), (690, 1120), (2690, 1120), (2690, 1420), (2740, 1420)], color=ORANGE)

    section_label(draw, 740, 1745, "Quality Gate ก่อนส่งคำตอบ", RED)

    process_box(
        draw,
        (740, 1820, 1740, 2180),
        number=13,
        title="Format + Validate",
        body="Answer Validator v2\nAnswer-Type + Target + Source Contract\nถามราคาแต่ตอบเกม = reject\nถามปุ่มแต่ตอบเกมอื่น = reject",
        color=RED,
        fill=RED_FILL,
    )
    diamond(
        draw,
        (1840, 1840, 2300, 2160),
        text="คำตอบ\nผ่าน Contract?",
        color=WHITE,
        fill=PANEL,
        text_size=29,
    )
    process_box(
        draw,
        (2400, 1765, 2970, 1945),
        number="R",
        title="Bounded Repair",
        body="ลอง next deterministic candidate\nสูงสุด 1 ครั้ง ไม่วนไม่สิ้นสุด",
        color=ORANGE,
        fill=ORANGE_FILL,
        title_size=31,
        body_size=22,
    )
    process_box(
        draw,
        (2400, 2080, 2970, 2250),
        number="V",
        title="Final Hard Veto",
        body="ยังผิดหรือ evidence ไม่พอ\nเปลี่ยนเป็น Safe No-answer",
        color=RED,
        fill=RED_FILL,
        title_size=31,
        body_size=22,
    )
    process_box(
        draw,
        (3070, 1820, 3760, 2180),
        number=14,
        title="Final Answer",
        body="Thai response style + source links\nDecision Artifact + trace + timings\nquality metrics + JSONL/SQLite log",
        color=GREEN,
        fill=GREEN_FILL,
    )

    # All execution paths converge at the quality gate.
    arrow(draw, [(1190, 1655), (1190, 1820)], color=GREEN)
    arrow(draw, [(2190, 1655), (2190, 1740), (1480, 1740), (1480, 1820)], color=BLUE)
    arrow(draw, [(3190, 1655), (3190, 1740), (1650, 1740), (1650, 1820)], color=ORANGE)
    arrow(draw, [(650, 1760), (700, 1760), (700, 2000), (740, 2000)], color=RED)
    arrow(draw, [(1740, 2000), (1840, 2000)])
    arrow(draw, [(2300, 1930), (2350, 1930), (2350, 1855), (2400, 1855)], color=ORANGE, label="ไม่ผ่าน", label_at=(2305, 1788))
    arrow(draw, [(2685, 1945), (2685, 2080)], color=RED, label="ยังผิด/ครบครั้ง", label_at=(2710, 1990))
    arrow(draw, [(2970, 2165), (3020, 2165), (3020, 2100), (3070, 2100)], color=RED)
    arrow(draw, [(2300, 2000), (3070, 2000)], color=GREEN, label="ผ่าน", label_at=(2650, 1960))

    # Repair loops to validation; hard veto is the bounded terminal branch.
    arrow(
        draw,
        [(2400, 1815), (2360, 1815), (2360, 1690), (1540, 1690), (1540, 1820)],
        color=ORANGE,
    )

    legend_y = 2390
    rounded_box(draw, (80, 2340, 3760, 2635), outline="#6f88a4", fill="#08192c", width=3, radius=22, shadow=False)
    draw.text((120, 2360), "คำอธิบายสี", font=SECTION_FONT, fill=TEXT)
    x = 120
    y = legend_y + 50
    x = legend_item(draw, x, y, GREEN, "Structured / deterministic fast path")
    x = legend_item(draw, x, y, BLUE, "Retrieval / RAG / vector")
    x = legend_item(draw, x, y, ORANGE, "Optional model path")
    legend_item(draw, x, y, RED, "Clarification / safety / veto")
    footer = "หลักสำคัญ: PSU facts ต้องมีหลักฐาน | LLM ไม่ใช่ผู้ตอบหลักทุกคำถาม | ไม่มั่นใจให้ถามกลับหรือ no-answer"
    fb = draw.textbbox((0, 0), footer, font=SMALL_FONT)
    draw.text(((WIDTH - (fb[2] - fb[0])) / 2, 2580), footer, font=SMALL_FONT, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(OUTPUT)


if __name__ == "__main__":
    main()
