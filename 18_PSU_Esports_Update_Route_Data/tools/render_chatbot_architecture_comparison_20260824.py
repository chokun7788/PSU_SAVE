from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "psu_esports_chatbot_architecture_comparison_20260824.png"

FONT_REGULAR = Path(r"C:\Windows\Fonts\LeelawUI.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\leelawdb.ttf")

BG = "#071019"
STRIPE = "#0B1724"
PANEL = "#0D1B29"
PANEL_SOFT = "#102231"
TEXT = "#F3F7FB"
MUTED = "#B6C3D1"
FAINT = "#718195"
LINE = "#334D62"
GREEN = "#56D990"
BLUE = "#79A9FF"
CYAN = "#44CBEA"
GOLD = "#F4C965"
ORANGE = "#F59C62"
RED = "#F16F78"
PURPLE = "#AC9AF7"


def f(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold and FONT_BOLD.exists() else FONT_REGULAR
    return ImageFont.truetype(str(path), size=size)


TITLE = f(90, True)
SUBTITLE = f(40)
SECTION = f(55, True)
CARD_TITLE = f(42, True)
BODY = f(31)
SMALL = f(27)
LABEL = f(27, True)
FOOT = f(26)


def width(draw: ImageDraw.ImageDraw, text: str, text_font: ImageFont.FreeTypeFont) -> int:
    if not text:
        return 0
    return int(draw.textbbox((0, 0), text, font=text_font)[2])


def wrap(draw: ImageDraw.ImageDraw, text: str, text_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            lines.append("")
            continue
        current = ""
        for token in raw.split(" "):
            candidate = token if not current else f"{current} {token}"
            if width(draw, candidate, text_font) <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
            current = token
        if current:
            lines.append(current)
    return lines


def text_block(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    text_font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    max_lines: int | None = None,
    gap: int = 10,
) -> int:
    lines = wrap(draw, text, text_font, max_width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" .") + "..."
    for line in lines:
        draw.text((x, y), line, font=text_font, fill=fill)
        y += text_font.size + gap
    return y


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], accent: str, fill: str = PANEL_SOFT) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=28, fill=fill, outline=LINE, width=3)
    draw.rounded_rectangle((x1, y1, x1 + 18, y2), radius=9, fill=accent)


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    accent: str,
    badge: str | None = None,
    body_font: ImageFont.FreeTypeFont = BODY,
) -> None:
    x1, y1, x2, y2 = box
    panel(draw, box, accent)
    draw.text((x1 + 46, y1 + 28), title, font=CARD_TITLE, fill=TEXT)
    if badge:
        badge_width = width(draw, badge, LABEL) + 40
        draw.rounded_rectangle((x2 - badge_width - 24, y1 + 23, x2 - 24, y1 + 67), radius=13, fill=accent)
        draw.text((x2 - badge_width - 4, y1 + 30), badge, font=LABEL, fill=BG)
    text_block(draw, x1 + 46, y1 + 93, body, body_font, MUTED, x2 - x1 - 86)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str, label: str | None = None) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=7)
    angle = math.atan2(y2 - y1, x2 - x1)
    point_a = (x2 - 24 * math.cos(angle) + 15 * math.sin(angle), y2 - 24 * math.sin(angle) - 15 * math.cos(angle))
    point_b = (x2 - 24 * math.cos(angle) - 15 * math.sin(angle), y2 - 24 * math.sin(angle) + 15 * math.cos(angle))
    draw.polygon((end, point_a, point_b), fill=color)
    if label:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        label_width = width(draw, label, LABEL) + 34
        draw.rounded_rectangle((mid_x - label_width // 2, mid_y - 25, mid_x + label_width // 2, mid_y + 21), radius=12, fill=BG, outline=color, width=2)
        draw.text((mid_x - label_width // 2 + 17, mid_y - 19), label, font=LABEL, fill=TEXT)


def elbow(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], color: str, label: str | None = None) -> None:
    draw.line(points, fill=color, width=7, joint="curve")
    arrow(draw, points[-2], points[-1], color, label)


def section(draw: ImageDraw.ImageDraw, y: int, number: str, title: str, color: str) -> None:
    draw.rounded_rectangle((180, y, 282, y + 68), radius=18, fill=color)
    draw.text((212, y + 8), number, font=LABEL, fill=BG)
    draw.text((315, y + 2), title, font=SECTION, fill=TEXT)
    draw.line((315 + width(draw, title, SECTION) + 36, y + 41, 5020, y + 41), fill=LINE, width=3)


def create() -> None:
    image = Image.new("RGB", (5200, 6980), BG)
    draw = ImageDraw.Draw(image)
    for y in range(0, 6980, 360):
        draw.rectangle((0, y, 5200, y + 160), fill=STRIPE)

    draw.text((180, 105), "PSU ESPORTS CHATBOT — ARCHITECTURE EVOLUTION", font=TITLE, fill=TEXT)
    draw.text((185, 225), "แกน deterministic เดิมยังอยู่ แต่เพิ่ม Semantic RAG และ Gated Local LLM เป็นชั้นเสริม", font=SUBTITLE, fill=MUTED)
    draw.rounded_rectangle((185, 312, 1460, 365), radius=16, fill=GREEN)
    draw.text((215, 320), "BACKBONE: ENGINE + STRUCTURED FACTS + VALIDATION", font=LABEL, fill=BG)
    draw.rounded_rectangle((1490, 312, 2590, 365), radius=16, fill=CYAN)
    draw.text((1520, 320), "NEW DATA PLANE: BGE + VECTOR INDEX", font=LABEL, fill=BG)
    draw.rounded_rectangle((2620, 312, 3700, 365), radius=16, fill=GOLD)
    draw.text((2650, 320), "NEW MODEL PLANE: GATED TYPHOON", font=LABEL, fill=BG)
    draw.rounded_rectangle((3730, 312, 5010, 365), radius=16, fill=RED)
    draw.text((3760, 320), "NOT A FULL LLM-FIRST REWRITE", font=LABEL, fill=BG)

    section(draw, 460, "1", "BACKBONE เปรียบเทียบ: เดิม vs ปัจจุบัน", PURPLE)
    old_box = (180, 610, 2500, 2840)
    new_box = (2700, 610, 5020, 2840)
    panel(draw, old_box, BLUE, fill=PANEL)
    panel(draw, new_box, GREEN, fill=PANEL)
    draw.text((250, 665), "เดิม: Architecture Snapshot 27/07", font=SECTION, fill=TEXT)
    draw.text((2770, 665), "ปัจจุบัน: Website Product Path 24/08", font=SECTION, fill=TEXT)
    text_block(draw, 250, 740, "Deterministic-first pipeline และ LLM อยู่แบบ optional review/fallback ที่ปลายทาง", BODY, MUTED, 2150)
    text_block(draw, 2770, 740, "Deterministic core เดิม + request control + semantic data plane + grounded model assist", BODY, MUTED, 2150)

    old_cards = [
        (260, 915, 2420, 1200),
        (260, 1280, 2420, 1610),
        (260, 1690, 2420, 2040),
        (260, 2120, 2420, 2470),
    ]
    card(draw, old_cards[0], "Entry + Context", "Web / Terminal / Notebook / API -> recent history -> Session Context Resolver", BLUE, "เดิม")
    card(draw, old_cards[1], "Decision Core", "Compound split -> normalize -> entities -> heuristic route -> universal intent -> ambiguity/candidate/preconditions", PURPLE, "เดิม")
    card(draw, old_cards[2], "Execution", "Fast / Rule / Structured / Competition fact cards / curated + lexical/hash-vector hybrid retrieval", GREEN, "แกนหลัก")
    card(draw, old_cards[3], "Optional Model + Assurance", "Intent LLM / Tool Router / facts composer / general fallback -> source contract -> validator -> log", GOLD, "Optional")
    for upper, lower, color in zip(old_cards, old_cards[1:], [BLUE, PURPLE, GOLD]):
        arrow(draw, ((upper[0] + upper[2]) // 2, upper[3] + 8), ((lower[0] + lower[2]) // 2, lower[1] - 10), color)

    new_cards = [
        (2780, 915, 4940, 1200),
        (2780, 1280, 4940, 1610),
        (2780, 1690, 4940, 2040),
        (2780, 2120, 4940, 2470),
    ]
    card(draw, new_cards[0], "Website + Request Control", "Browser -> /api/chat -> JSON validation -> request ID -> admission -> session lock -> outer deadline 9s", CYAN, "เพิ่ม")
    card(draw, new_cards[1], "Decision Core ยังคงเดิม", "Context/compound/normalize/entities/router/intent/ambiguity/candidates แต่เพิ่ม semantic route refiner + model preflight", PURPLE, "คงแกน")
    card(draw, new_cards[2], "Execution Data Plane", "Fast/Structured เดิม + legacy hybrid retrieval + BGE-M3 semantic retrieval + source/freshness/margin guards", GREEN, "ขยาย")
    card(draw, new_cards[3], "Gated Model Assist + Assurance", "Model Gateway -> grounded Typhoon Composer เฉพาะ evidence/time/budget ผ่าน -> contract/repair/hard veto -> async trace log", GOLD, "เพิ่ม")
    for upper, lower, color in zip(new_cards, new_cards[1:], [CYAN, GREEN, GOLD]):
        arrow(draw, ((upper[0] + upper[2]) // 2, upper[3] + 8), ((lower[0] + lower[2]) // 2, lower[1] - 10), color)

    arrow(draw, (2515, 1710), (2685, 1710), ORANGE, "ยกระดับแบบต่อยอด")
    draw.text((220, 2600), "สิ่งที่คงเดิม: Engine เป็นผู้ตัดสินใจ, Structured/Fast เป็น default, evidence/validation บังคับทุก path", font=SMALL, fill=GREEN)
    draw.text((2740, 2600), "สิ่งที่เพิ่ม: BGE semantic index, ingestion, model budget, composer grounding, request deadline/overload control", font=SMALL, fill=CYAN)

    section(draw, 2960, "2", "CURRENT WEBSITE ARCHITECTURE — ชั้นของระบบที่ทำงานร่วมกัน", CYAN)

    # Presentation and API
    top = [(180, 3110, 1290, 3490), (1430, 3110, 2540, 3490), (2680, 3110, 3790, 3490), (3930, 3110, 5020, 3490)]
    card(draw, top[0], "1. Browser Web Chat", "web_chat/app.js • browser session ID • recent history • loading/error UI", BLUE, "Website")
    card(draw, top[1], "2. Web API", "POST /api/chat • JSON request/response • question/body validation", CYAN, "server.py")
    card(draw, top[2], "3. Request Control", "active request cap • per-session lock • deadline/reserve • async log", ORANGE, "9s budget")
    card(draw, top[3], "4. Pipeline Engine", "orchestrator: split/plan/understand/select/validate/finalize", PURPLE, "engine.py")
    for left, right, color in zip(top, top[1:], [CYAN, ORANGE, PURPLE]):
        arrow(draw, (left[2] + 8, (left[1] + left[3]) // 2), (right[0] - 10, (right[1] + right[3]) // 2), color)

    # Control plane
    control = [(180, 3660, 1540, 4075), (1640, 3660, 3000, 4075), (3100, 3660, 4460, 4075)]
    card(draw, control[0], "Context + Compound Control", "resolve reference from evidence -> split multi-question -> complexity gate -> optional dependency planner", PURPLE)
    card(draw, control[1], "Understanding + Route Control", "normalize -> entities -> heuristic route -> semantic route refiner -> boundary/freshness/ambiguity", PURPLE)
    card(draw, control[2], "Capability Selection", "Question Frame + candidate score + preconditions -> select deterministic / RAG / model / safe outcome", PURPLE)
    arrow(draw, (1550, 3868), (1630, 3868), PURPLE)
    arrow(draw, (3010, 3868), (3090, 3868), PURPLE)
    elbow(draw, [(4470, 3868), (4720, 3868), (4720, 4230), (2590, 4230)], PURPLE, "เลือก path")

    # Execution lanes
    section(draw, 4200, "3", "EXECUTION + DATA LAYERS — ไม่ได้ใช้ model ทุกคำถาม", GREEN)
    lanes = [
        (180, 4350, 1640, 4940),
        (1740, 4350, 3200, 4940),
        (3300, 4350, 5020, 4940),
    ]
    card(draw, lanes[0], "A. Deterministic Core", "Fast/Rule/Calculator + Structured Tools + Competition facts\n\nราคา • ตาราง • 42 เกม • อุปกรณ์ • วิธีจอง • กติกาที่ verified\n\nตอบเร็วและ exact โดยไม่ต้องเรียก LLM", GREEN, "Default")
    card(draw, lanes[1], "B. Retrieval / Semantic RAG", "Curated + legacy lexical/hash + BGE-M3 semantic dense search\n\nscore + margin + category/entity + trust + freshness\n\nได้ Evidence/Draft หรือ no-answer", CYAN, "Feature gate")
    card(draw, lanes[2], "C. Local LLM Assist", "Typhoon 4B: planner / intent review / tool router / grounded composer / general non-PSU\n\nModel Gateway ตรวจ quota ≤2, concurrency 1, health, source conflict, remaining time", GOLD, "Gated")
    elbow(draw, [(910, 4950), (910, 5100), (2590, 5100), (2590, 5170)], GREEN)
    elbow(draw, [(2470, 4950), (2470, 5100), (2590, 5100), (2590, 5170)], CYAN)
    elbow(draw, [(4160, 4950), (4160, 5100), (2590, 5100), (2590, 5170)], GOLD)

    # Output assurance and data supporting services
    final_box = (1060, 5190, 4120, 5630)
    card(draw, final_box, "OUTPUT ASSURANCE", "Path validator -> Answer Contract -> claim/numeric/source grounding -> Bounded Repair -> Final Hard Veto -> Thai formatter -> JSON response + trace/log\n\nผลลัพธ์ที่อนุญาต: grounded answer / clarification / no-answer / safe timeout", RED, "ทุก path")

    section(draw, 5780, "4", "OFFLINE KNOWLEDGE + RUNTIME DEPENDENCIES", BLUE)
    bottom = [(180, 5930, 1280, 6420), (1410, 5930, 2510, 6420), (2640, 5930, 3740, 6420), (3870, 5930, 5020, 6420)]
    card(draw, bottom[0], "Structured Sources", "JSON/catalog/routing/rate/schedule/fact cards\n\nCanonical exact data", GREEN)
    card(draw, bottom[1], "Knowledge Ingestion", "knowledge inbox -> metadata validate -> chunk -> publish/validity/freshness", BLUE)
    card(draw, bottom[2], "Ollama Models", "BGE-M3 Q8: embedding/search\nTyphoon 4B: gated generation\nCrossEncoder: optional and cold-heavy", GOLD)
    card(draw, bottom[3], "Indexes + Logs", "semantic vector index • legacy indexes • query cache • chat/trace logs • benchmark reports", CYAN)
    arrow(draw, (1290, 6175), (1400, 6175), BLUE)
    arrow(draw, (2520, 6175), (2630, 6175), CYAN)
    arrow(draw, (3750, 6175), (3860, 6175), CYAN)
    elbow(draw, [(3190, 5920), (3190, 5780), (2470, 5780), (2470, 5650)], CYAN, "semantic evidence")

    draw.text((180, 6570), "CURRENT LIMITS", font=LABEL, fill=RED)
    text_block(draw, 430, 6564, "queue/session lock ยังอยู่ใน process เดียว • persistent memory ยังไม่มี • CrossEncoder ไม่เหมาะกับ cold online request • ต้อง rerun full 1,600+ model-enabled evaluation และ multi-user load test", FOOT, MUTED, 4560)
    draw.text((180, 6870), "Generated 2026-08-24 • Details: docs/44_current_chatbot_architecture_comparison_20260824.md", font=FOOT, fill=FAINT)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)


if __name__ == "__main__":
    create()
    print(OUTPUT)
