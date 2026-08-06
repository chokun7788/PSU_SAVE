from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import unicodedata
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CURATED = ROOT / "data" / "curated"
BANK_JSONL = ROOT / "data" / "eval" / "broad_usage_eval_v1.jsonl"
BANK_JSON = ROOT / "data" / "eval" / "broad_usage_eval_v1.json"
REPORT_DIR = ROOT / "reports" / "broad_usage_eval"


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def _plain(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def _case(
    group: str,
    question: str,
    *,
    expected_category: str | list[str] | None = None,
    expected_mode_prefix: str | list[str] | None = None,
    must_contain: list[str] | None = None,
    must_contain_any: list[str] | None = None,
    must_not_contain: list[str] | None = None,
    note: str = "",
    risk: str = "medium",
) -> dict[str, Any]:
    return {
        "kind": "single",
        "group": group,
        "question": question,
        "expected_category": expected_category,
        "expected_mode_prefix": expected_mode_prefix,
        "must_contain": must_contain or [],
        "must_contain_any": must_contain_any or [],
        "must_not_contain": must_not_contain or ["Local LLM"],
        "note": note,
        "risk": risk,
    }


def _session_case(
    group: str,
    title: str,
    turns: list[dict[str, Any]],
    *,
    note: str = "",
    risk: str = "high",
) -> dict[str, Any]:
    return {
        "kind": "session",
        "group": group,
        "title": title,
        "turns": turns,
        "note": note,
        "risk": risk,
    }


def _unique_by_game(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for row in rows:
        game = str(row.get("game") or row.get("title") or "").strip()
        if not game or game.lower() in seen:
            continue
        seen.add(game.lower())
        result.append(row)
    return result


def _game_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\bstandard edition\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remake\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremake\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remastered\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremastered\b", "", clean, flags=re.IGNORECASE)
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", clean.lower())


def _current_availability_rows() -> list[dict[str, Any]]:
    return _read_jsonl(CURATED / "service_game_availability.jsonl")


def _current_game_keys() -> set[str]:
    keys: set[str] = set()
    for row in _current_availability_rows():
        for game in row.get("games") or []:
            key = _game_key(str(game))
            if key:
                keys.add(key)
    return keys


def _game_rows() -> list[dict[str, Any]]:
    rows = _unique_by_game(_read_jsonl(CURATED / "game_item_details.jsonl"))
    current_keys = _current_game_keys()
    if not current_keys:
        return rows
    filtered: list[dict[str, Any]] = []
    for row in rows:
        game = str(row.get("game") or row.get("title") or "").strip()
        key = _game_key(game)
        if key in current_keys or game == "The Last of Us Part I / Part II":
            filtered.append(row)
    return filtered


def _control_groups() -> dict[str, list[dict[str, Any]]]:
    current_keys = _current_game_keys()
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in _read_jsonl(CURATED / "game_control_facts.jsonl"):
        game = str(row.get("game") or "").strip()
        if not game:
            continue
        if current_keys and _game_key(game) not in current_keys:
            continue
        grouped.setdefault(game, []).append(row)
    return grouped


def _equipment_rows() -> list[dict[str, Any]]:
    return _read_jsonl(CURATED / "equipment_item_details.jsonl")


def _member_rows() -> list[dict[str, Any]]:
    return _read_jsonl(CURATED / "member_profiles.jsonl")


def _dedupe_cases(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str, str]] = set()
    result: list[dict[str, Any]] = []
    counters: dict[str, int] = {}
    for case in cases:
        if case["kind"] == "session":
            key_text = str(case.get("title") or "")
        else:
            key_text = str(case.get("question") or "")
        key = (case["kind"], case["group"], key_text)
        if key in seen:
            continue
        seen.add(key)
        counters[case["group"]] = counters.get(case["group"], 0) + 1
        prefix = "".join(part[0].upper() for part in case["group"].split("_") if part)[:4]
        case["id"] = f"{prefix}-{counters[case['group']]:03d}"
        result.append(case)
    return result


def build_question_bank() -> list[dict[str, Any]]:
    games = _game_rows()
    control_groups = _control_groups()
    equipment = _equipment_rows()
    members = _member_rows()
    cases: list[dict[str, Any]] = []

    services = [
        ("PC", "PC", ["0 บาท", "25 บาท", "70 บาท"]),
        ("PS5", "PlayStation 5", ["0 บาท", "50 บาท", "150 บาท"]),
        ("Nintendo Switch", "Nintendo Switch", ["0 บาท", "50 บาท", "140 บาท"]),
        ("Cockpit", "Cockpit", ["0 บาท", "65 บาท", "200 บาท"]),
        ("VR", "VR", ["0 บาท", "190 บาท", "525 บาท"]),
    ]
    groups = [
        ("นักศึกษา PSU", "0 บาท"),
        ("นักศึกษาต่างมหาลัย", "General Student"),
        ("บุคคลทั่วไป", "General Adult"),
    ]
    durations = ["30 นาที", "1 ชั่วโมง", "2 ชั่วโมง"]
    for service, answer_label, markers in services:
        cases.append(_case("service_fee", f"{service} ราคาเท่าไหร่", expected_category="service_fee", must_contain=[answer_label, *markers[:2]]))
        for user_group, marker in groups:
            for duration in durations:
                cases.append(_case("service_fee", f"{user_group} เล่น {service} {duration} เสียกี่บาท", expected_category="service_fee", must_contain_any=[marker, "0 บาท"]))
    for question in [
        "ราคา PC กับ PS5 ต่างกันเท่าไหร่",
        "PS5 กับ Nintendo ราคาอันไหนแพงกว่า",
        "VR 30 นาทีกับ VR 1 ชั่วโมงต่างกันยังไง",
        "ถ้าเล่น PC 3 ชั่วโมง บุคคลทั่วไปต้องจ่ายเท่าไหร่",
        "ต่างมหาลัยเล่น Cockpit 2 ชั่วโมงกี่บาท",
        "เด็ก ม.อ. เล่น Nintendo 4 คนเสียเงินไหม",
        "General Adult เล่น VR 1 ชั่วโมงกี่บาท",
        "PSU Staff เล่น PC ต้องเสียเงินไหม",
    ]:
        cases.append(_case("service_fee", question, expected_category="service_fee", must_contain_any=["บาท", "ต่างกัน", "ฟรี", "0 บาท"]))
    for row in games[:30]:
        game = str(row["game"])
        cases.append(_case("service_fee", f"{game} ราคาเท่าไหร่", expected_category="service_fee", must_contain=[game.split(":")[0].split("/")[0].strip()], risk="high"))

    for row in games:
        game = str(row["game"])
        zone = str((row.get("zones") or [""])[0])
        cases.extend([
            _case("games", f"{game} คือเกมอะไร", expected_category="games", must_contain=[game.split(":")[0].strip()]),
            _case("games", f"{game} เล่นได้ที่ไหน", expected_category="games", must_contain_any=[zone.replace(" Zone", ""), "เล่นได้ที่"]),
            _case("games", f"{game} เล่นยังไง", expected_category="games", must_contain_any=[game.split(":")[0].strip(), "วิธีเล่น", "เล่นได้ที่"]),
            _case("games", f"{game} เป็นเกมแนวไหน", expected_category="games", must_contain_any=["แนวเกม", str(row.get("genre") or "").split("/")[0].strip()]),
        ])
    for question in [
        "มีเกมทั้งหมดกี่เกม",
        "ตอนนี้มีเกมอะไรบ้าง",
        "PC มีเกมอะไรบ้าง",
        "PS5 มีเกมอะไรบ้าง",
        "Nintendo Switch มีเกมอะไรบ้าง",
        "VR มีเกมอะไรบ้าง",
        "Cockpit มีเกมอะไรบ้าง",
        "อุปกรณ์ไหนเกมเยอะสุด",
        "เกมไหนเล่นได้หลายโซน",
        "เกมแข่งรถมีอะไรบ้าง",
        "เกมยิงมีอะไรบ้าง",
        "เกมปาร์ตี้มีอะไรบ้าง",
        "Over cook มีเกมไหม",
        "Tekken 8 มีในเครื่องไหน",
    ]:
        cases.append(_case("games", question, expected_category="games", must_contain_any=["เกม", "Zone", "TEKKEN", "Mario", "Gran Turismo"]))

    for game, rows in sorted(control_groups.items()):
        detail_rows = [row for row in rows if row.get("button") or row.get("action_th")]
        cases.append(_case("game_controls", f"{game} ปุ่มทั้งหมดมีอะไรบ้าง", expected_category="games", expected_mode_prefix="pipeline:structured_game_controls", must_contain=[game.split(":")[0].strip(), "ปุ่ม"]))
        cases.append(_case("game_controls", f"{game} ใช้จอยยังไง", expected_category="games", must_contain_any=[game.split(":")[0].strip(), "ปุ่ม", "จอย", "คอนโทรล"]))
        for row in detail_rows[:2]:
            action = str(row.get("action_th") or row.get("action_en") or "").strip()
            button = str(row.get("button") or "").strip()
            if action:
                cases.append(_case("game_controls", f"{game} ปุ่ม{action}กดอะไร", expected_category="games", expected_mode_prefix="pipeline:structured_game_controls", must_contain_any=[button, action]))
    for question in [
        "เกมนี้มีปุ่มอะไรบ้าง",
        "ปุ่ม",
        "เล่นยังไง",
        "ปุ่มยิงกดอะไร",
        "Minecraft มีปุ่มอะไรบ้างในศูนย์",
        "ROV มีปุ่มให้เล่นในศูนย์ไหม",
        "GTA V ปุ่มอะไร",
    ]:
        cases.append(_case("game_controls", question, expected_category=["games", "clarification", "no_answer"], must_contain_any=["ยังไม่แน่ใจ", "ยังไม่พบ", "ขอ", "ไม่มี"], risk="high"))

    zone_labels = ["PC Zone", "PlayStation 5 Zone", "Nintendo Switch Zone", "VR Zone", "Cockpit Zone"]
    for zone in zone_labels:
        cases.extend([
            _case("equipment", f"{zone} มีอุปกรณ์อะไรบ้าง", expected_category="equipment", must_contain_any=[zone.replace("PlayStation 5", "PlayStation"), "อุปกรณ์"]),
            _case("equipment", f"{zone} มีอะไรให้ใช้บ้าง", expected_category=["equipment", "clarification"], must_contain_any=["อุปกรณ์", "หมายถึงเรื่องไหน", "Zone"]),
        ])
    for row in equipment:
        item = str(row.get("item") or "")
        zone = str(row.get("zone") or "")
        if not item:
            continue
        cases.extend([
            _case("equipment", f"{item} คืออะไร", expected_category="equipment", must_contain_any=[item.split()[0], zone.replace(" Zone", "")]),
            _case(
                "equipment",
                f"{item} อยู่โซนไหน",
                expected_category=["equipment", "games"],
                expected_mode_prefix=["pipeline:structured_equipment_item", "pipeline:equipment_item_location_fast_path"],
                must_contain_any=[zone.replace(" Zone", ""), "Zone"],
            ),
            _case("equipment", f"{item} ใช้ทำอะไร", expected_category="equipment", must_contain_any=[item.split()[0], "ใช้", "Zone"]),
        ])

    reservation_questions = [
        "จองยังไง",
        "สรุปขั้นตอนจองให้หน่อย",
        "จอง PS5 ต้องทำยังไง",
        "จอง Nintendo Switch ต้องทำยังไง",
        "จอง VR ต้องทำยังไง",
        "จอง Cockpit ต้องทำยังไง",
        "จอง PC ต้องทำยังไง",
        "ต้องจองล่วงหน้ากี่ชั่วโมง",
        "จองได้สูงสุดกี่ session",
        "หลังจองต้องจ่ายภายในกี่นาที",
        "จองแล้วแก้ไขได้ไหม",
        "จองแล้วโอนสิทธิ์ให้เพื่อนได้ไหม",
        "เช็คอินล่วงหน้าได้กี่นาที",
        "ถ้ายกเลิกต้องทำยังไง",
        "ถ้าไปช้าจะเป็นอะไรไหม",
        "walk in ได้ไหม",
        "ต้องแนบสลิปไหม",
        "จองแล้วไม่สามารถยกเลิกได้ใช่ไหม",
        "ถ้าจองผิดข้อมูลต้องทำยังไง",
        "จ่ายเงินผ่านช่องทางไหน",
    ]
    schedule_questions = [
        "เปิดกี่โมง",
        "ปิดกี่โมง",
        "วันนี้เปิดไหม",
        "วันจันทร์เปิดกี่โมง",
        "วันอาทิตย์เปิดไหม",
        "ช่วงเช้าเล่นได้ไหม",
        "ตอนเย็นเปิดถึงกี่โมง",
        "พรุ่งนี้เปิดไหม",
        "วันหยุดเปิดไหม",
        "ตารางเวลาให้บริการเป็นยังไง",
    ]
    for question in reservation_questions:
        cases.append(_case("reservation", question, expected_category="reservation", must_contain_any=["จอง", "เช็คอิน", "ชำระ", "session", "ยกเลิก"]))
    for question in schedule_questions:
        cases.append(_case("schedule", question, expected_category=["schedule", "reservation"], must_contain_any=["เปิด", "ปิด", "เวลา", "วัน", "ไม่เปิด"]))

    for question in [
        "สมาชิกมีใครบ้าง",
        "สมาชิก PSU Esports มีกี่คน",
        "สมาชิกแบ่งเป็นกี่หมวด",
        "แต่ละหมวดมีใครบ้าง",
        "cooperative education มีใครบ้าง",
        "PSU Phuket Esports Club มีใครบ้าง",
    ]:
        cases.append(_case("members", question, expected_category=["members", "overview"], must_contain_any=["Members", "สมาชิก", "คน", "หมวด"]))
    for row in members:
        name = str(row.get("name") or "")
        role = str(row.get("role") or "")
        if name:
            cases.append(_case("members", f"{name} ทำตำแหน่งอะไร", expected_category=["members", "overview"], must_contain_any=[role, name.split()[0]]))
        if role:
            cases.append(_case("members", f"ใครเป็น{role}", expected_category=["members", "overview"], must_contain_any=[name.split()[0], role]))

    comp_games = ["VALORANT", "CS2", "Counter-Strike 2", "TEKKEN 8", "ROV"]
    comp_aspects = [
        "กติกาการแข่งขันคืออะไร",
        "ใช้ผู้เล่นกี่คน",
        "มาสายจะโดนอะไร",
        "pause ได้ไหม",
        "ถ้าเกมหลุดทำยังไง",
        "ขอ restart ได้ไหม",
        "รูปแบบการแข่งขันเป็นยังไง",
        "รอบชิงเล่นกี่เกม",
        "มีตัวสำรองได้ไหม",
        "มีข้อห้ามอะไรบ้าง",
        "ถ้าใช้ bug จะโดนอะไร",
        "ต้องเช็คอินก่อนแข่งไหม",
        "ใช้บัญชีอะไรแข่ง",
        "แผนที่มีอะไรบ้าง",
        "สรุปกติกาสั้นๆ",
    ]
    for game in comp_games:
        for aspect in comp_aspects:
            cases.append(_case("competition_rules", f"{game} {aspect}", expected_category="competition_rules", must_contain_any=[game.split()[0], "กติกา", "แข่งขัน", "ยังไม่พบ"], risk="high"))

    compound_questions = [
        "Tekken 8 ปุ่มอะไร แล้ว PC ราคาเท่าไหร่",
        "PS5 มีเกมอะไรกับราคาเท่าไหร่",
        "PC มีอุปกรณ์อะไร แล้วมีเกมอะไรบ้าง",
        "Gran Turismo 7 เล่นยังไง แล้วปุ่มเร่งกดอะไร",
        "Nintendo Switch ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง",
        "VR ราคาเท่าไหร่ แล้วจองยังไง",
        "สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี",
        "Tekken 8 กับ Mario Kart 8 Deluxe มีปุ่มอะไรบ้าง",
        "PS5 กับ Nintendo Switch มีเกมอะไรบ้าง",
        "Cockpit มีอุปกรณ์อะไร แล้ว Gran Turismo ปุ่มอะไร",
        "Call of Duty ปุ่มยิงอะไร แล้วเล่นได้ที่ไหน",
        "PC ราคาเท่าไหร่ แล้วจองได้กี่ session",
        "วันนี้เปิดไหม แล้วจอง PS5 ยังไง",
        "VR 30 นาทีราคาเท่าไหร่ แล้ว 1 ชั่วโมงราคาเท่าไหร่",
        "Tekken 8 ราคาเท่าไหร่ แล้วมีปุ่มอะไรบ้าง",
    ]
    for question in compound_questions:
        cases.append(_case("compound", question, expected_category="multi_question", expected_mode_prefix="pipeline:multi_question_splitter", must_contain_any=["คำถามที่", "ราคา", "ปุ่ม", "Zone", "จอง"], risk="high"))

    ambiguous_questions = [
        "PC มีอะไรบ้าง",
        "PS5 มีอะไรบ้าง",
        "Nintendo มีอะไรบ้าง",
        "VR มีอะไรบ้าง",
        "Cockpit มีอะไรบ้าง",
        "เครื่องไหนดีที่สุด",
        "เล่นอะไรดี",
        "มีอะไรแนะนำไหม",
        "ราคา",
        "จอง",
        "เกม",
        "อุปกรณ์",
        "ปุ่ม",
        "อันนี้เล่นยังไง",
        "สรุปคือทำยังไง",
    ]
    for question in ambiguous_questions:
        cases.append(_case("ambiguity_no_answer", question, expected_category=["clarification", "games", "equipment", "service_fee", "reservation", "no_answer"], must_contain_any=["หมายถึง", "พิมพ์", "ยังไม่", "เกม", "อุปกรณ์", "ราคา", "จอง"], risk="high"))
    unsupported = [
        "มี Minecraft ไหม",
        "มี GTA V ไหม",
        "มี ROV ให้เล่นในศูนย์ไหม",
        "Roblox เล่นได้ไหม",
        "เกม Valorant Mobile มีไหม",
        "ขอเบอร์โทรส่วนตัวเจ้าหน้าที่",
        "ขอข้อมูลที่ไม่ได้อยู่ในเว็บ PSU Esports",
        "วันนี้มีข่าว esports อะไรล่าสุด",
        "เพลงฮิตตอนนี้คืออะไร",
        "ช่วยทำการบ้านคณิตให้หน่อย",
    ]
    for question in unsupported:
        cases.append(_case("ambiguity_no_answer", question, expected_category=["no_answer", "games", "general"], must_contain_any=["ยังไม่พบ", "ไม่มี", "ไม่ได้อยู่", "ตอบจากข้อมูล"], risk="high"))

    session_templates = [
        ("Gran Turismo controls follow-up", ["Gran Turismo เล่นยังไง", "ปุ่ม"], ["Gran Turismo 7", "ปุ่ม"]),
        ("Mario Kart 8 controls follow-up", ["Mario Kart 8 Deluxe เล่นยังไง", "ปุ่มเร่งเครื่องกดอะไร"], ["Mario Kart 8 Deluxe", "เร่งเครื่อง"]),
        ("Tekken price follow-up", ["Tekken 8 คือเกมอะไร", "ราคา"], ["TEKKEN 8", "ราคา"]),
        ("PC broad games choice", ["PC มีอะไรบ้าง", "เกม"], ["PC", "เกม"]),
        ("PC broad price choice", ["PC มีอะไรบ้าง", "ราคา"], ["PC", "ราคา"]),
        ("PC broad equipment choice", ["PC มีอะไรบ้าง", "อุปกรณ์"], ["PC", "อุปกรณ์"]),
        ("PC broad booking choice", ["PC มีอะไรบ้าง", "จอง"], ["PC", "จอง"]),
        ("Naruto access follow-up", ["เกม Naruto", "แล้วจะเล่นต้องทำไง"], ["NARUTO", "จอง"]),
        ("Reservation summary follow-up", ["แล้วจองไง", "สรุปคือทำยังไง"], ["ขั้นตอนจอง", "เลือกบริการ"]),
        ("PS5 games follow-up", ["PS5 มีเกมกี่เกม", "แล้วมีเกมอะไรบ้าง"], ["PlayStation 5", "เกม"]),
        ("Member group follow-up", ["สมาชิก PSU Esport มีกี่หมวด", "แล้วแต่ละหมวดมีใครบ้าง"], ["Members", "cooperative"]),
        ("Topic shift should not inherit game", ["Mario Party คือเกมอะไร", "จองเครื่องยังไง"], ["จอง", "เลือกบริการ"]),
    ]
    for title, questions, final_must in session_templates:
        turns = []
        for index, question in enumerate(questions, 1):
            turns.append({
                "question": question,
                "must_contain": final_must if index == len(questions) else [],
                "must_not_contain": ["Local LLM"],
            })
        cases.append(_session_case("session_followup", title, turns))

    return _dedupe_cases(cases)


def _listify(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def _validate_single(case: dict[str, Any], result: Any) -> list[str]:
    problems: list[str] = []
    answer = str(result.answer or "")
    categories = _listify(case.get("expected_category"))
    if categories and result.route.category not in categories:
        problems.append(f"route_category expected {categories}, got {result.route.category}")
    prefixes = _listify(case.get("expected_mode_prefix"))
    if prefixes and not any(str(result.mode).startswith(prefix) for prefix in prefixes):
        problems.append(f"mode expected prefix {prefixes}, got {result.mode}")
    for needle in case.get("must_contain") or []:
        if not _contains(answer, str(needle)):
            problems.append(f"missing '{needle}'")
    any_needles = [str(item) for item in case.get("must_contain_any") or [] if str(item)]
    if any_needles and not any(_contains(answer, needle) for needle in any_needles):
        problems.append(f"missing any of {any_needles}")
    for needle in case.get("must_not_contain") or []:
        if needle and _contains(answer, str(needle)):
            problems.append(f"forbidden '{needle}'")
    if result.validation and not result.validation.ok:
        problems.append("answer_validator_not_ok")
    return problems


def _sources(hits: list[dict[str, Any]]) -> list[str]:
    sources: list[str] = []
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        label = str(hit.get("id") or metadata.get("title") or metadata.get("source_id") or "").strip()
        url = str(metadata.get("source_url") or metadata.get("url") or "").strip()
        source = f"{label}: {url}" if label and url else (url or label)
        if source and source not in sources:
            sources.append(source)
    return sources


def _strategy(mode: str, trace: Any) -> str:
    text = (mode + " " + json.dumps(_plain(trace), ensure_ascii=False)).lower()
    mode_text = mode.lower()
    if "multi_question" in mode_text:
        return "compound"
    if "structured" in mode_text:
        return "structured"
    if "deterministic" in mode_text or "fast_path" in mode_text:
        return "fast/rule"
    if "clarification" in mode_text:
        return "clarification"
    if "vector" in text or "rag" in text or "retrieval" in text:
        return "rag/retrieval"
    if "llm" in mode_text:
        return "llm"
    if "no_answer" in text:
        return "no_answer"
    return "pipeline"


def _result_row(case: dict[str, Any], result: Any, wall_sec: float, problems: list[str], *, turn_index: int | None = None, resolved: Any = None) -> dict[str, Any]:
    return {
        "case_id": case["id"],
        "kind": case["kind"],
        "group": case["group"],
        "turn_index": turn_index,
        "question": case.get("question") or (case.get("turns") or [{}])[(turn_index or 1) - 1].get("question"),
        "resolved_question": getattr(resolved, "resolved_question", ""),
        "used_context": getattr(resolved, "used_context", None),
        "passed": not problems,
        "problems": problems,
        "risk": case.get("risk", ""),
        "mode": result.mode,
        "route_category": result.route.category,
        "route_intent": result.route.intent,
        "strategy": _strategy(result.mode, result.trace),
        "confidence": result.confidence,
        "latency_sec": result.elapsed,
        "wall_sec": wall_sec,
        "answer": result.answer,
        "sources": _sources(result.hits),
        "validation": _plain(result.validation),
        "universal_intent": _plain(result.universal_intent),
    }


def _append_history(history: list[dict[str, Any]], question: str, resolved_question: str, result: Any) -> None:
    history.append({"role": "user", "text": question})
    history.append({
        "role": "assistant",
        "text": result.answer,
        "universal_intent": _plain(result.universal_intent),
        "route_category": result.route.category,
        "route_intent": result.route.intent,
        "resolved_text": resolved_question,
    })
    del history[:-20]


def run_cases(cases: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    from app.runtime.pipeline_answer import answer_question_pipeline_debug
    from app.session.context_resolver import resolve_question_with_context

    rows: list[dict[str, Any]] = []
    total = len(cases)
    for position, case in enumerate(cases, 1):
        if case["kind"] == "single":
            started = time.perf_counter()
            result = answer_question_pipeline_debug(
                case["question"],
                experimental_rag_fallback=args.rag_fallback,
                experimental_allow_llm=args.allow_llm,
            )
            wall_sec = round(time.perf_counter() - started, 4)
            problems = _validate_single(case, result)
            rows.append(_result_row(case, result, wall_sec, problems))
        else:
            history: list[dict[str, Any]] = []
            for turn_index, turn in enumerate(case["turns"], 1):
                question = str(turn["question"])
                resolved = resolve_question_with_context(question, history[-12:])
                started = time.perf_counter()
                result = answer_question_pipeline_debug(
                    resolved.resolved_question,
                    experimental_rag_fallback=args.rag_fallback,
                    experimental_allow_llm=args.allow_llm,
                )
                wall_sec = round(time.perf_counter() - started, 4)
                turn_case = {
                    **case,
                    "question": question,
                    "expected_category": turn.get("expected_category"),
                    "expected_mode_prefix": turn.get("expected_mode_prefix"),
                    "must_contain": turn.get("must_contain", []),
                    "must_contain_any": turn.get("must_contain_any", []),
                    "must_not_contain": turn.get("must_not_contain", ["Local LLM"]),
                }
                problems = _validate_single(turn_case, result)
                rows.append(_result_row(case, result, wall_sec, problems, turn_index=turn_index, resolved=resolved))
                _append_history(history, question, resolved.resolved_question, result)
        if not args.quiet or position == 1 or position == total or position % args.progress_every == 0:
            last = rows[-1]
            status = "PASS" if last["passed"] else "FAIL"
            print(f"[{position}/{total}] {status} {case['id']} {case['group']} {last['strategy']} {last['wall_sec']}s")
    return rows


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "case_id", "kind", "group", "turn_index", "question", "resolved_question", "used_context",
        "passed", "problems", "risk", "mode", "route_category", "route_intent", "strategy",
        "confidence", "latency_sec", "wall_sec", "answer", "sources",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: json.dumps(row.get(field), ensure_ascii=False) if isinstance(row.get(field), (list, dict)) else row.get(field) for field in fields})


def summarize(rows: list[dict[str, Any]], cases: list[dict[str, Any]], started_at: float, args: argparse.Namespace) -> dict[str, Any]:
    group_counts: dict[str, dict[str, int]] = {}
    mode_counts: dict[str, int] = {}
    strategy_counts: dict[str, int] = {}
    problem_counts: dict[str, int] = {}
    for row in rows:
        group = row["group"]
        group_counts.setdefault(group, {"total": 0, "pass": 0, "fail": 0})
        group_counts[group]["total"] += 1
        group_counts[group]["pass" if row["passed"] else "fail"] += 1
        mode_counts[row["mode"]] = mode_counts.get(row["mode"], 0) + 1
        strategy_counts[row["strategy"]] = strategy_counts.get(row["strategy"], 0) + 1
        for problem in row["problems"]:
            head = str(problem).split(":", 1)[0]
            problem_counts[head] = problem_counts.get(head, 0) + 1
    failed_rows = [row for row in rows if not row["passed"]]
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "case_count": len(cases),
        "turn_count": len(rows),
        "passed": len(rows) - len(failed_rows),
        "failed": len(failed_rows),
        "pass_rate": round((len(rows) - len(failed_rows)) / max(1, len(rows)), 4),
        "total_wall_sec": round(time.perf_counter() - started_at, 3),
        "allow_llm": args.allow_llm,
        "rag_fallback": args.rag_fallback,
        "group_counts": group_counts,
        "strategy_counts": strategy_counts,
        "mode_counts": mode_counts,
        "problem_counts": problem_counts,
        "top_failures": [
            {
                "case_id": row["case_id"],
                "group": row["group"],
                "question": row["question"],
                "resolved_question": row["resolved_question"],
                "mode": row["mode"],
                "route": f"{row['route_category']}/{row['route_intent']}",
                "problems": row["problems"],
                "answer_preview": str(row["answer"]).replace("\n", " ")[:240],
            }
            for row in failed_rows[:40]
        ],
        "bank_jsonl": str(BANK_JSONL),
        "bank_json": str(BANK_JSON),
    }


def _write_markdown(path: Path, summary: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Broad Usage Eval v1",
        "",
        f"- Generated at: {summary['generated_at']}",
        f"- Cases: {summary['case_count']}",
        f"- Turn checks: {summary['turn_count']}",
        f"- Passed: {summary['passed']}",
        f"- Failed: {summary['failed']}",
        f"- Pass rate: {summary['pass_rate']}",
        f"- Total wall sec: {summary['total_wall_sec']}",
        f"- Allow LLM: {summary['allow_llm']}",
        f"- RAG fallback: {summary['rag_fallback']}",
        "",
        "## By Group",
    ]
    for group, counts in sorted(summary["group_counts"].items()):
        lines.append(f"- {group}: {counts['pass']}/{counts['total']} pass, {counts['fail']} fail")
    lines.extend(["", "## By Strategy"])
    for strategy, count in sorted(summary["strategy_counts"].items()):
        lines.append(f"- {strategy}: {count}")
    lines.extend(["", "## Common Problems"])
    for problem, count in sorted(summary["problem_counts"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {problem}: {count}")
    lines.extend(["", "## Top Failures"])
    for row in [item for item in rows if not item["passed"]][:80]:
        preview = str(row["answer"]).replace("\n", " ")
        if len(preview) > 260:
            preview = preview[:260].rstrip() + "..."
        lines.extend([
            "",
            f"### {row['case_id']} {row['group']}",
            f"- Question: {row['question']}",
            f"- Resolved: {row['resolved_question'] or '-'}",
            f"- Mode: `{row['mode']}`",
            f"- Route: `{row['route_category']}/{row['route_intent']}`",
            f"- Problems: {', '.join(row['problems'])}",
            f"- Answer: {preview}",
        ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_eval(args: argparse.Namespace) -> int:
    cases = build_question_bank()
    if args.group != "all":
        cases = [case for case in cases if case["group"] == args.group]
    if args.limit:
        cases = cases[:args.limit]

    _write_jsonl(BANK_JSONL, build_question_bank())
    _write_json(BANK_JSON, build_question_bank())
    if args.export_bank_only:
        print(f"bank jsonl: {BANK_JSONL}")
        print(f"bank json: {BANK_JSON}")
        print(f"cases: {len(build_question_bank())}")
        return 0

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = Path(args.out_dir) if args.out_dir else REPORT_DIR / stamp
    out_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    rows = run_cases(cases, args)
    summary = summarize(rows, cases, started, args)
    _write_jsonl(out_dir / "results.jsonl", rows)
    _write_json(out_dir / "results.json", rows)
    _write_csv(out_dir / "results.csv", rows)
    _write_json(out_dir / "summary.json", summary)
    _write_markdown(out_dir / "report.md", summary, rows)
    print(f"bank jsonl: {BANK_JSONL}")
    print(f"bank json: {BANK_JSON}")
    print(f"results dir: {out_dir}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if args.fail_on_fail and summary["failed"] else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run broad user-like single-turn and session eval for PSU Esports chatbot.")
    parser.add_argument("--group", default="all")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--rag-fallback", action="store_true")
    parser.add_argument("--export-bank-only", action="store_true")
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--fail-on-fail", action="store_true")
    return parser.parse_args()


def main() -> int:
    _configure_stdout()
    return run_eval(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
