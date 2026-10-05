from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
OUT_PATH = OUT_DIR / "answer_quality_pipeline_diagram.png"


W, H = 1800, 1180
BG = "#f6f8fb"
INK = "#162033"
MUTED = "#64748b"
BLUE = "#2563eb"
TEAL = "#0f766e"
GREEN = "#16a34a"
AMBER = "#d97706"
RED = "#dc2626"
PURPLE = "#7c3aed"
LINE = "#cbd5e1"
WHITE = "#ffffff"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/tahomabd.ttf" if bold else "C:/Windows/Fonts/tahoma.ttf"),
        Path("C:/Windows/Fonts/leelawdb.ttf" if bold else "C:/Windows/Fonts/leelawui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


TITLE = font(42, True)
SUBTITLE = font(24)
HEAD = font(24, True)
BODY = font(20)
SMALL = font(17)
TINY = font(15)


def rounded_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: str,
    outline: str,
    radius: int = 18,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    body: str = "",
    accent: str = BLUE,
    title_font: ImageFont.FreeTypeFont = HEAD,
    body_font: ImageFont.FreeTypeFont = SMALL,
) -> None:
    x1, y1, x2, y2 = xy
    cx = (x1 + x2) // 2
    title_lines = wrap(title, width=26)
    body_lines = wrap(body, width=34) if body else []
    total_h = len(title_lines) * 30 + len(body_lines) * 24 + (10 if body_lines else 0)
    y = y1 + ((y2 - y1) - total_h) // 2
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        draw.text((cx - (bbox[2] - bbox[0]) // 2, y), line, font=title_font, fill=accent)
        y += 30
    if body_lines:
        y += 8
    for line in body_lines:
        bbox = draw.textbbox((0, 0), line, font=body_font)
        draw.text((cx - (bbox[2] - bbox[0]) // 2, y), line, font=body_font, fill=MUTED)
        y += 24


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = "#475569") -> None:
    draw.line((start, end), fill=color, width=4)
    ex, ey = end
    sx, sy = start
    if abs(ex - sx) >= abs(ey - sy):
        direction = 1 if ex > sx else -1
        pts = [(ex, ey), (ex - 16 * direction, ey - 9), (ex - 16 * direction, ey + 9)]
    else:
        direction = 1 if ey > sy else -1
        pts = [(ex, ey), (ex - 9, ey - 16 * direction), (ex + 9, ey - 16 * direction)]
    draw.polygon(pts, fill=color)


def pill(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fill: str, fg: str = WHITE) -> int:
    bbox = draw.textbbox((0, 0), text, font=TINY)
    width = bbox[2] - bbox[0] + 26
    draw.rounded_rectangle((x, y, x + width, y + 30), radius=15, fill=fill)
    draw.text((x + 13, y + 5), text, font=TINY, fill=fg)
    return width


def draw_branch_card(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    items: list[tuple[str, str]],
    accent: str,
) -> None:
    rounded_box(draw, xy, WHITE, accent, radius=20, width=3)
    x1, y1, x2, _ = xy
    draw.rounded_rectangle((x1, y1, x2, y1 + 58), radius=20, fill=accent)
    draw.rectangle((x1, y1 + 30, x2, y1 + 58), fill=accent)
    draw.text((x1 + 24, y1 + 15), title, font=HEAD, fill=WHITE)
    y = y1 + 82
    for label, desc in items:
        draw.ellipse((x1 + 24, y + 3, x1 + 38, y + 17), fill=accent)
        draw.text((x1 + 50, y - 2), label, font=BODY, fill=INK)
        for line in wrap(desc, width=43):
            draw.text((x1 + 50, y + 24), line, font=SMALL, fill=MUTED)
            y += 22
        y += 36


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw.text((70, 50), "PSU Esports Chatbot: Answer Quality Pipeline", font=TITLE, fill=INK)
    draw.text(
        (72, 104),
        "โครงสร้างตอบคำถามแบบเร็ว แม่น ไม่มั่ว และตอบประเด็นหลักก่อนรายละเอียด",
        font=SUBTITLE,
        fill=MUTED,
    )
    pill(draw, 72, 145, "Ground Truth v2: 360/360 PASS", GREEN)
    pill(draw, 345, 145, "Avg latency ~0.0002s", BLUE)
    pill(draw, 555, 145, "LLM ใช้เมื่อจำเป็น", PURPLE)

    # Main top flow.
    boxes = [
        ((70, 230, 330, 335), "User Input", "คำถามจากลูกค้า / Facebook", BLUE),
        ((390, 230, 650, 335), "Preprocess", "clean text + normalize + alias", TEAL),
        ((710, 230, 970, 335), "Entity Extract", "วัน / เวลา / service / กลุ่ม / ราคา", PURPLE),
        ((1030, 230, 1290, 335), "Scope Guard", "นอกขอบเขตหรือไม่มีข้อมูลจริง?", RED),
        ((1350, 230, 1610, 335), "Intent Router", "เลือกหมวดคำถามหลัก", AMBER),
    ]
    for xy, title, body, accent in boxes:
        rounded_box(draw, xy, WHITE, LINE)
        centered_text(draw, xy, title, body, accent)

    for i in range(len(boxes) - 1):
        x1 = boxes[i][0][2]
        y1 = (boxes[i][0][1] + boxes[i][0][3]) // 2
        x2 = boxes[i + 1][0][0]
        y2 = (boxes[i + 1][0][1] + boxes[i + 1][0][3]) // 2
        arrow(draw, (x1 + 12, y1), (x2 - 12, y2))

    # Router category strip.
    rounded_box(draw, (70, 380, 1610, 455), "#eef2ff", "#c7d2fe", radius=18)
    draw.text((96, 402), "Route Categories:", font=HEAD, fill=PURPLE)
    x = 320
    for label, color in [
        ("schedule", BLUE),
        ("service_fee", GREEN),
        ("reservation", AMBER),
        ("rules", RED),
        ("games", TEAL),
        ("equipment", PURPLE),
        ("contact", "#0ea5e9"),
        ("no_answer", "#475569"),
    ]:
        x += pill(draw, x, 402, label, color) + 12

    # Branch cards.
    fast_xy = (70, 520, 560, 910)
    rag_xy = (650, 520, 1140, 910)
    quality_xy = (1230, 520, 1720, 910)

    draw_branch_card(
        draw,
        fast_xy,
        "1) Fast / Deterministic Path",
        [
            ("Service Fee Calculator", "ตอบราคาและคำนวณส่วนต่าง เช่น VR 30 นาที vs 1 ชั่วโมง"),
            ("Schedule Handler", "ตอบเวลาเปิดปิดและ maintenance โดยไม่ใส่ข้อมูลที่ไม่ได้ถาม"),
            ("Category Rule Base", "กฎจอง เช็คอิน จ่ายเงิน เกม อุปกรณ์ ติดต่อ และ penalty"),
            ("No-answer Guard", "ถ้าไม่มีข้อมูลยืนยัน ให้บอกว่าไม่พบข้อมูล ไม่เดา"),
        ],
        GREEN,
    )

    draw_branch_card(
        draw,
        rag_xy,
        "2) RAG Fallback",
        [
            ("Curated Facts", "ค้นข้อมูลที่จัดหมวดแล้ว เช่น schedule, service_fee, rules"),
            ("Hybrid Retrieval", "ใช้ keyword + semantic ใน phase ถัดไป สำหรับ PDF/Facebook/web"),
            ("LLM Rewrite", "ให้ LLM เรียบเรียงเฉพาะเมื่อข้อมูลถูกดึงมาแล้ว"),
            ("Source Grounding", "คำตอบต้องมีแหล่งอ้างอิงที่ตรวจกลับได้"),
        ],
        BLUE,
    )

    draw_branch_card(
        draw,
        quality_xy,
        "3) Quality Gate",
        [
            ("Answer-first Formatter", "ตอบสิ่งที่ถามก่อน เช่น ราคา/เวลา/ส่วนต่าง แล้วค่อยรายละเอียด"),
            ("Validation", "เช็ค keyword, source, must-not-contain และความเสี่ยงหลุดประเด็น"),
            ("Human Review", "ให้คนให้คะแนน 0-4 และตัดสิน pass/minor/major/needs_data"),
            ("Final Answer", "ส่งคำตอบสั้น ชัด สุภาพ พร้อมแหล่งข้อมูล"),
        ],
        PURPLE,
    )

    # Branch arrows.
    router_center = ((boxes[-1][0][0] + boxes[-1][0][2]) // 2, boxes[-1][0][3] + 10)
    split_y = 485
    draw.line((router_center[0], router_center[1], router_center[0], split_y), fill="#475569", width=4)
    draw.line((315, split_y, 1475, split_y), fill="#475569", width=4)
    arrow(draw, (315, split_y), ((fast_xy[0] + fast_xy[2]) // 2, fast_xy[1] - 12))
    arrow(draw, (895, split_y), ((rag_xy[0] + rag_xy[2]) // 2, rag_xy[1] - 12))
    arrow(draw, (1475, split_y), ((quality_xy[0] + quality_xy[2]) // 2, quality_xy[1] - 12))

    # Flow from fast/rag to quality.
    arrow(draw, (fast_xy[2] + 16, 715), (rag_xy[0] - 18, 715), "#334155")
    arrow(draw, (rag_xy[2] + 16, 715), (quality_xy[0] - 18, 715), "#334155")

    # Output band.
    rounded_box(draw, (70, 980, 1720, 1090), "#ecfdf5", "#86efac", radius=24, width=3)
    draw.text((100, 1012), "Output:", font=HEAD, fill=GREEN)
    draw.text(
        (205, 1012),
        "คำตอบที่ตอบตรงคำถามก่อน + รายละเอียดเท่าที่จำเป็น + แหล่งข้อมูล + ไม่ตอบมั่วเมื่อข้อมูลไม่พอ",
        font=BODY,
        fill=INK,
    )
    draw.text(
        (100, 1050),
        "ตัวอย่าง: “ต่างกัน 185 บาท ...” / “วันจันทร์ Morning เล่นไม่ได้ ... Afternoon เปิด 13:00-16:00”",
        font=SMALL,
        fill=MUTED,
    )

    draw.text(
        (70, 1135),
        f"Generated from: {ROOT}",
        font=TINY,
        fill="#94a3b8",
    )

    img.save(OUT_PATH, quality=95)
    print(OUT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
