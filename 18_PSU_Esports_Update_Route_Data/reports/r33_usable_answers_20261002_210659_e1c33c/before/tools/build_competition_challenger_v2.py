from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
BASE_GT_PATHS = [
    ROOT / "data" / "ground_truth" / "competition_by_game_v2" / "ground_truth_competition_all_games_v2_diverse.jsonl",
    ROOT / "data" / "ground_truth" / "competition_challenger_v1" / "ground_truth_competition_challenger_v1_weird_user_questions.jsonl",
]
OUT_DIR = ROOT / "data" / "ground_truth" / "competition_challenger_v2"
OUT_PATH = OUT_DIR / "ground_truth_competition_challenger_v2_real_competitor_questions.jsonl"
REPORT_PATH = ROOT / "docs" / "27_competition_challenger_ground_truth_v2_20260704.md"


GAME_ALIAS = {
    "Counter-Strike 2": ["CS2", "cs2", "Counter Strike", "เคาเตอร์"],
    "Arena of Valor (RoV)": ["RoV", "rov", "AOV", "เกมตีป้อม"],
    "VALORANT": ["VALORANT", "valorant", "วาโล", "valo"],
    "Tekken 8": ["Tekken 8", "tekken", "เทคเคน", "เทคเคน 8"],
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def compact_question(question: str, game: str, index: int) -> str:
    alias = GAME_ALIAS.get(game, [game])[index % len(GAME_ALIAS.get(game, [game]))]
    text = question.strip()
    replacements = {
        "Counter-Strike 2": alias,
        "CS2": alias,
        "PSU Phuket CS2 2026": alias,
        "Arena of Valor (RoV)": alias,
        "Blueket Games RoV": alias,
        "RoV": alias,
        "VALORANT": alias,
        "PSU Phuket VALORANT 2026": alias,
        "Tekken 8": alias,
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\s+", " ", text).strip()
    if not any(a.lower() in text.lower() for a in GAME_ALIAS.get(game, [])):
        text = f"{alias} {text}"
    return text


def natural_variant(row: dict[str, Any], index: int) -> str:
    game = str(row.get("game", ""))
    base = compact_question(str(row["question"]), game, index)
    style = index % 6
    if style == 0:
        return f"{base} แบบตอบให้เอาไปบอกเพื่อนได้เลย"
    if style == 1:
        return f"ในกติกา {base} เขียนไว้ยังไง"
    if style == 2:
        return f"ถามแบบคนจะไปแข่งจริง: {base}"
    if style == 3:
        return f"{base} ขอคำตอบสั้นๆแต่ต้องอ้างอิงกติกา"
    if style == 4:
        return f"{base} ถ้าผมเป็นผู้เข้าแข่งต้องทำยังไง"
    return f"{base} สรุปให้ตรงประเด็นก่อน"


def make_row(source: dict[str, Any], item_id: str, question: str, variant_type: str) -> dict[str, Any]:
    row = {
        "id": item_id,
        "category": "competition_rules",
        "game": source.get("game"),
        "intent": source.get("intent"),
        "question": question,
        "expected_keywords": source.get("expected_keywords", []),
        "expected_source_keywords": source.get("expected_source_keywords", []),
        "answer_type": source.get("answer_type", "fact"),
        "difficulty": "challenger",
        "variant_type": variant_type,
        "source_fact_key": source.get("source_fact_key"),
        "expected_mode_prefix": "pipeline:",
    }
    return row


def edge(
    rows: list[dict[str, Any]],
    game: str,
    intent: str,
    source: str,
    source_fact_key: str,
    expected_keywords: list[str],
    questions: list[str],
    answer_type: str = "fact",
) -> None:
    for question in questions:
        rows.append(
            {
                "category": "competition_rules",
                "game": game,
                "intent": intent,
                "question": question,
                "expected_keywords": expected_keywords,
                "expected_source_keywords": [source],
                "answer_type": answer_type,
                "difficulty": "challenger",
                "variant_type": "real_competitor_edge",
                "source_fact_key": source_fact_key,
                "expected_mode_prefix": "pipeline:",
            }
        )


def build_edges() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cs2 = "competition_rules_cs2_psu_phuket_2026"
    rov = "competition_rules_rov_blueket_2025_men"
    val = "competition_rules_valorant_psu_phuket_2026"
    tek = "competition_rules_tekken8_psu_esports"

    edge(rows, "Counter-Strike 2", "team_size", cs2, "cs2_team_size", ["5 คน", "CS2"], [
        "CS2 มีคนครบ 4 คนแล้วลงแข่งได้ไหม",
        "ทีม cs2 ขาดคนนึงเหลือ 4 คนพอแข่งได้ปะ",
        "เคาเตอร์ต้องมีตัวจริงกี่คนถึงลงได้",
    ])
    edge(rows, "Counter-Strike 2", "roster_change", cs2, "cs2_roster_lock", ["ไม่มีการเปลี่ยนแปลง", "สมาชิก"], [
        "CS2 เพื่อนมาไม่ได้ ขอเปลี่ยนตัวก่อนแข่งได้ไหม",
        "cs2 ตัวจริงติดธุระ เอาตัวสำรองที่ไม่ได้ลงชื่อมาแทนได้ไหม",
        "Counter Strike เปลี่ยน roster หน้างานได้หรือเปล่า",
    ], "policy")
    edge(rows, "Counter-Strike 2", "registration", cs2, "cs2_no_late_registration", ["ไม่อนุญาต", "ปิดรับสมัคร"], [
        "CS2 สมัครไปแล้วอยากเพิ่มชื่อทีหลังได้ไหม",
        "cs2 หลังปิดรับสมัครเพิ่มเพื่อนเข้าทีมได้ปะ",
        "เคาเตอร์ลงทะเบียนไม่ครบแล้วค่อยเพิ่มได้ไหม",
    ], "policy")
    edge(rows, "Counter-Strike 2", "pause", cs2, "cs2_timeout_freeze", ["Freeze time"], [
        "CS2 กำลังยิงกันอยู่ขอ timeout ได้ไหม",
        "cs2 เวลานอกต้องกดตอนไหน Freeze time ใช่ไหม",
        "Counter Strike tactical timeout ใช้กลางรอบได้หรือเปล่า",
    ])
    edge(rows, "Counter-Strike 2", "pause", cs2, "cs2_pause", ["2 ครั้ง", "10 นาที"], [
        "CS2 คอมหลุด technical pause ได้กี่ครั้ง",
        "cs2 เครื่องมีปัญหาขอ technical pause นานสุดกี่นาที",
        "เคาเตอร์ pause เพราะ hardware ได้ไหมและจำกัดยังไง",
    ])
    edge(rows, "Counter-Strike 2", "penalty", cs2, "cs2_stream_sniping", ["ห้าม", "สตรีม"], [
        "CS2 ระหว่างแข่งเปิดดูไลฟ์ถ่ายทอดสดได้ไหม",
        "cs2 ดูสตรีมคู่ตัวเองระหว่างแมตช์ผิดไหม",
        "Counter Strike stream snipe ในแมตช์โดนอะไร",
    ], "policy")
    edge(rows, "Counter-Strike 2", "penalty", cs2, "cs2_player_conduct", ["ห้าม", "เกลียดชัง"], [
        "CS2 ด่าเหยียดเชื้อชาติในแชทได้ไหม",
        "cs2 พูด hate speech ใส่คู่แข่งผิดกติกาไหม",
        "เคาเตอร์ toxic หรือวาจาเกลียดชังมีบทลงโทษไหม",
    ], "policy")

    edge(rows, "Arena of Valor (RoV)", "format", rov, "rov_format_bo3", ["BO3", "ทุกรอบ"], [
        "แข่ง ROV ต้องเล่นกี่เกมถึงจบ",
        "rov รอบทั่วไปกับรอบชิงเป็น BO อะไร",
        "AOV ถามง่ายๆ แต่ละแมตช์ต้องชนะกี่เกม",
    ])
    edge(rows, "Arena of Valor (RoV)", "late_start", rov, "rov_late_start", ["15 นาที", "ปรับแพ้"], [
        "rov เลทเกิน 15 นาทีแพ้เลยไหม",
        "AOV เริ่มช้ากว่านัด 15 นาทีโดนอะไร",
        "เกมตีป้อมมาสายเกินสิบห้านาทีมีโทษยังไง",
    ], "policy")
    edge(rows, "Arena of Valor (RoV)", "hero_rule", rov, "rov_global_ban_pick", ["Global Ban/Pick"], [
        "RoV ใช้ global ban pick ไหม",
        "rov ฮีโร่ที่เลือกแล้วเกมถัดไปใช้ซ้ำได้ไหม",
        "AOV ระบบแบนฮีโร่เป็น Global Ban/Pick หรือเปล่า",
    ])
    edge(rows, "Arena of Valor (RoV)", "pause", rov, "rov_pause", ["5 ครั้ง", "1 นาที"], [
        "RoV pause ได้กี่ครั้งต่อทีม",
        "rov หลุดเกมขอหยุดได้กี่นาที",
        "AOV กดหยุดเกมได้สูงสุดกี่ครั้ง",
    ])
    edge(rows, "Arena of Valor (RoV)", "pause", rov, "rov_server_down", ["เซิร์ฟเวอร์", "แจ้งทีมงาน"], [
        "RoV เน็ตทั้งโซนล่มต้องทำยังไง",
        "AOV เซิร์ฟเกมพังระหว่างแข่งให้ใครตัดสิน",
        "rov อินเทอร์เน็ตหรือ server มีปัญหาต้องแจ้งใคร",
    ], "policy")
    edge(rows, "Arena of Valor (RoV)", "penalty", rov, "rov_pause_wrong_penalty", ["ตักเตือน", "แบนฮีโร่", "ปรับแพ้"], [
        "RoV แกล้ง pause หลายรอบโดนอะไร",
        "rov pause ผิดครั้งที่ 1 2 3 ต่างกันยังไง",
        "AOV กดหยุดเกมมั่วๆ มีบทลงโทษเป็นขั้นไหม",
    ], "policy")
    edge(rows, "Arena of Valor (RoV)", "break_time", rov, "rov_break_absent", ["ปรับ", "แพ้"], [
        "RoV พักแล้วไม่กลับมาตามเวลาโดนอะไร",
        "AOV หายหลังพักการแข่งขันเสี่ยงโดนปรับแพ้ไหม",
        "rov กลับมาหลังพักช้ามากผู้ตัดสินทำอะไรได้",
    ], "policy")
    edge(rows, "Arena of Valor (RoV)", "schedule_location", rov, "rov_location", ["อาคาร", "5102A"], [
        "RoV แข่งที่อาคารไหน",
        "AOV รายการ Blueket Games จัดตรงไหนของ PSU ภูเก็ต",
        "rov สถานที่แข่งอยู่ห้องหรืออาคารอะไร",
    ])
    edge(rows, "Arena of Valor (RoV)", "penalty", rov, "rov_rude_words", ["ห้าม", "คำหยาบ"], [
        "RoV พูดคำหยาบใส่ทีมอื่นได้ไหม",
        "AOV ด่าหรือใช้คำไม่สุภาพในแข่งโดนอะไร",
        "rov แชทหยาบกับคู่แข่งผิดกติกาไหม",
    ], "policy")

    edge(rows, "VALORANT", "schedule", val, "valorant_checkin", ["30 นาที", "รายงานตัว"], [
        "วาโลต้องไปถึงก่อนแข่งกี่นาที",
        "valorant check in ก่อนแมตช์นานแค่ไหน",
        "VALORANT รายงานตัวก่อนแข่ง 30 นาทีใช่ไหม",
    ])
    edge(rows, "VALORANT", "equipment", val, "valorant_no_install", ["ห้าม", "ติดตั้งโปรแกรม"], [
        "วาโลติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม",
        "valorant ลงโปรแกรมช่วยเล่นในเครื่องแข่งได้หรือเปล่า",
        "VALORANT ขอ install software เองได้ไหม",
    ], "policy")
    edge(rows, "VALORANT", "equipment", val, "valorant_no_social", ["ห้าม", "social media"], [
        "วาโลเปิด Facebook บนคอมแข่งได้ไหม",
        "valorant เข้าเว็บสื่อสารระหว่างแข่งได้หรือเปล่า",
        "VALORANT social media ในเครื่องแข่งห้ามไหม",
    ], "policy")
    edge(rows, "VALORANT", "game_setting", val, "valorant_blood_bodies", ["Blood", "Bodies", "Off"], [
        "วาโลต้องปิดเลือดกับศพไหม",
        "valorant blood bodies ตั้งค่าเป็นอะไร",
        "VALORANT ในแข่งศพกับเลือดต้อง off ใช่ไหม",
    ])
    edge(rows, "VALORANT", "map_pool", val, "valorant_map_ban_until_3", ["แบน", "3 แผนที่"], [
        "วาโล ban map กันจนเหลือกี่แผนที่",
        "valorant แบนแผนที่จนเหลือ 3 maps ใช่ไหม",
        "VALORANT map veto ต้อง ban จนเหลือกี่ map",
    ])
    edge(rows, "VALORANT", "pause", val, "valorant_tactical_first_24", ["24 รอบแรก"], [
        "วาโล tactical timeout ใช้ได้เฉพาะ 24 รอบแรกไหม",
        "VALORANT timeout ต่อแผนที่ใช้ช่วงไหน",
        "valorant tactical timeout หลังครบ 24 รอบใช้ได้ไหม",
    ])
    edge(rows, "VALORANT", "pause", val, "valorant_emergency_over_time", ["หมดสิทธิ์", "ตัวสำรอง"], [
        "วาโล emergency pause เกินเวลาแล้วผู้เล่นยังกลับมาไม่ได้ทำไง",
        "VALORANT ถ้า pause ฉุกเฉินเกิน 10 นาทีต้องใช้ตัวสำรองไหม",
        "valorant หมดเวลาพักฉุกเฉินแล้วคนเล่นยังไม่พร้อมโดนอะไร",
    ], "policy")
    edge(rows, "VALORANT", "bug_rule", val, "valorant_cypher_camera", ["ห้าม", "Cypher"], [
        "วาโลวางกล้อง Cypher มุมที่มองไม่เห็นได้ไหม",
        "VALORANT cypher camera exploit ผิดกติกาไหม",
        "valorant กล้องไซเฟอร์นอกมุมมองใช้ได้หรือเปล่า",
    ], "policy")
    edge(rows, "VALORANT", "penalty", val, "valorant_match_forfeit", ["Match Forfeit", "Cheating", "Match fixing"], [
        "วาโล match fixing โดนโทษอะไร",
        "VALORANT โกงหรือจงใจล็อกผลแข่งโดน Match Forfeit ไหม",
        "valorant cheating ระดับร้ายแรงลงโทษยังไง",
    ], "policy")

    edge(rows, "Tekken 8", "format", tek, "tekken8_1v1", ["1v1"], [
        "เทคเคนแข่ง 1v1 หรือเป็นทีม",
        "tekken เล่นตัวต่อตัวใช่ไหม",
        "Tekken 8 รายการนี้เป็นแบบ 1 ต่อ 1 หรือเปล่า",
    ])
    edge(rows, "Tekken 8", "format", tek, "tekken8_ft2", ["FT2", "ชนะครบ 2 เกม"], [
        "เทคเคนต้องชนะกี่เกมถึงผ่าน",
        "Tekken 8 FT2 แปลว่าชนะกี่เกม",
        "tekken แต่ละแมตช์เล่นจนใครชนะกี่เกม",
    ])
    edge(rows, "Tekken 8", "game_setting", tek, "tekken8_round_3", ["3 รอบ"], [
        "เทคเคนแต่ละเกมแข่งกี่รอบ",
        "Tekken 8 เกมนึงมี 3 rounds ใช่ไหม",
        "tekken ตั้ง R3 หมายถึงอะไร",
    ])
    edge(rows, "Tekken 8", "equipment", tek, "tekken8_platform", ["PlayStation 5"], [
        "เทคเคนเล่นบน PS5 ใช่ไหม",
        "Tekken 8 ใช้เครื่องอะไรแข่ง",
        "tekken แข่งบน PlayStation 5 หรือ PC",
    ])
    edge(rows, "Tekken 8", "game_setting", tek, "tekken8_stage_random", ["Stage", "Random"], [
        "เทคเคนเลือกด่านเองได้ไหม",
        "Tekken 8 stage ต้อง random หรือเปล่า",
        "tekken ด่านแข่งสุ่มใช่ไหม",
    ])
    edge(rows, "Tekken 8", "character", tek, "tekken8_customization_ban", ["ห้าม", "Customization"], [
        "เทคเคนแต่งชุดตัวละครได้ไหม",
        "Tekken 8 ใช้ aura หรือ effect แต่งตัวละครได้หรือเปล่า",
        "tekken customization ทรงผมหรือชุดห้ามไหม",
    ], "policy")
    edge(rows, "Tekken 8", "pause", tek, "tekken8_pause_penalty", ["ปรับแพ้ 1 รอบ"], [
        "เทคเคนตั้งใจกด pause โดนอะไร",
        "Tekken 8 กดหยุดเกมโดยไม่จำเป็นเสีย round ไหม",
        "tekken pause เองหลังเริ่มเกมมีโทษยังไง",
    ], "policy")
    edge(rows, "Tekken 8", "pause", tek, "tekken8_allowed_pause_case", ["ยินยอม", "อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน"], [
        "เทคเคนถ้าจอยมีปัญหาขอหยุดได้ไหม",
        "Tekken 8 อุปกรณ์ขัดข้อง pause ได้กรณีไหน",
        "tekken เหตุฉุกเฉินหยุดเกมได้หรือเปล่า",
    ], "policy")
    edge(rows, "Tekken 8", "format", tek, "tekken8_decider", ["เกมตัดสิน"], [
        "เทคเคนเสมอ 1-1 ต้องทำไง",
        "Tekken 8 ถ้าคะแนนเกมเท่ากันต้องเล่นเกมตัดสินไหม",
        "tekken 1 ต่อ 1 ในเกมรวมต้องมี decider หรือเปล่า",
    ])
    edge(rows, "Tekken 8", "policy", tek, "tekken8_final_decision", ["คำตัดสิน", "สิ้นสุด"], [
        "เทคเคนเถียงคำตัดสินกรรมการได้ไหม",
        "Tekken 8 คำตัดสินของกรรมการถือว่าสิ้นสุดไหม",
        "tekken ถ้ามีข้อโต้แย้งต้องฟังใคร",
    ], "policy")

    return rows


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base_rows: list[dict[str, Any]] = []
    for path in BASE_GT_PATHS:
        base_rows.extend(load_jsonl(path))

    rows: list[dict[str, Any]] = []
    seen_questions: set[str] = set()

    for index, source in enumerate(base_rows, start=1):
        question = natural_variant(source, index)
        key = question.casefold()
        if key in seen_questions:
            continue
        seen_questions.add(key)
        rows.append(make_row(source, f"competition_challenger_v2_derived_{index:03d}", question, "derived_natural_language"))

    edge_rows = build_edges()
    for index, row in enumerate(edge_rows, start=1):
        question = row["question"]
        key = question.casefold()
        if key in seen_questions:
            continue
        seen_questions.add(key)
        row["id"] = f"competition_challenger_v2_edge_{index:03d}"
        rows.append(row)

    with OUT_PATH.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    game_counts = Counter(str(row.get("game", "unknown")) for row in rows)
    intent_counts = Counter(str(row.get("intent", "unknown")) for row in rows)
    lines = [
        "# Competition Challenger Ground Truth V2",
        "",
        "ชุดนี้สร้างเพื่อกดดัน pipeline ด้วยคำถามภาษาคนจริงมากขึ้น โดยยังใช้เฉลย/keyword ที่ตรวจได้จากกติกาเดิม",
        "",
        "## Files",
        "",
        f"- Ground truth: `{OUT_PATH}`",
        "",
        "## Summary",
        "",
        f"- Total: {len(rows)}",
        f"- Derived from stable/previous GT: {len(rows) - len(edge_rows)}",
        f"- New edge-style questions: {len(edge_rows)}",
        "",
        "## Game Distribution",
        "",
    ]
    for game, count in game_counts.most_common():
        lines.append(f"- {game}: {count}")
    lines.extend(["", "## Top Intent Distribution", ""])
    for intent, count in intent_counts.most_common(20):
        lines.append(f"- {intent}: {count}")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    print(f"Wrote {len(rows)} rows")
    print(OUT_PATH)
    print(REPORT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
