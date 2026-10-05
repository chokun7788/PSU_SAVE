from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BROAD_BANK = ROOT / "data" / "eval" / "broad_usage_eval_v1.jsonl"
OUT_JSONL = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
OUT_JSON = ROOT / "data" / "eval" / "model_benchmark_1500.json"
CURATED = ROOT / "data" / "curated"


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows) + "\n", encoding="utf-8")


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def _game_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\bstandard edition\b|\bremake\b|\bremastered\b", "", clean, flags=re.IGNORECASE)
    return re.sub(r"[^0-9a-z]+", "", clean.lower())


def _short_title(value: str) -> str:
    title = re.sub(r"\s*\([^)]*\)\s*", " ", value or "").strip()
    title = re.sub(r"\s+", " ", title)
    if ":" in title:
        return title.split(":")[0].strip()
    if "/" in title:
        return title.split("/")[0].strip()
    return title


def _case(
    group: str,
    question: str,
    *,
    expected_category: str | list[str] | None = None,
    expected_mode_prefix: str | list[str] | None = None,
    must_contain: list[str] | None = None,
    must_contain_any: list[str] | None = None,
    must_not_contain: list[str] | None = None,
    llm_required: bool = False,
    quality_bucket: str = "psu_fact",
    risk: str = "medium",
    source: str = "generated",
    note: str = "",
) -> dict[str, Any]:
    return {
        "kind": "single",
        "group": group,
        "question": question,
        "expected_category": expected_category,
        "expected_mode_prefix": expected_mode_prefix,
        "must_contain": must_contain or [],
        "must_contain_any": must_contain_any or [],
        "must_not_contain": must_not_contain if must_not_contain is not None else ["Local LLM"],
        "llm_required": llm_required,
        "quality_bucket": quality_bucket,
        "risk": risk,
        "source": source,
        "note": note,
    }


def _normalize_broad_case(row: dict[str, Any]) -> dict[str, Any] | None:
    if row.get("kind") != "single":
        return None
    question = str(row.get("question") or "")
    if str(row.get("group") or "") == "game_controls":
        control_games = {
            _game_key(str(item.get("game") or ""))
            for item in _read_jsonl(CURATED / "game_control_facts.jsonl")
            if item.get("button")
        }
        current_games = {
            str(game)
            for item in _read_jsonl(CURATED / "service_game_availability.jsonl")
            for game in (item.get("games") or [])
            if str(game).strip()
        }
        question_key = _game_key(question)
        unsupported = sorted(
            (
                game
                for game in current_games
                if _game_key(game) not in control_games and _game_key(game) in question_key
            ),
            key=len,
            reverse=True,
        )
        if unsupported:
            game = unsupported[0]
            return _case(
                "game_controls",
                question,
                expected_category=["games", "no_answer"],
                expected_mode_prefix=[
                    "pipeline:structured_game_controls_no_data",
                    "pipeline:no_answer",
                    "pipeline:answer_contract_no_answer",
                ],
                must_contain_any=[game, "ยังไม่พบข้อมูลปุ่ม", "ไม่มีข้อมูลปุ่ม"],
                must_not_contain=["Local LLM"],
                quality_bucket="psu_fact",
                risk=str(row.get("risk") or "medium"),
                source="broad_usage_eval_v1",
                note=f"from {row.get('id') or ''}; corrected to current source coverage",
            )
    return _case(
        str(row.get("group") or "broad_usage"),
        question,
        expected_category=row.get("expected_category"),
        expected_mode_prefix=row.get("expected_mode_prefix"),
        must_contain=list(row.get("must_contain") or []),
        must_contain_any=list(row.get("must_contain_any") or []),
        must_not_contain=list(row.get("must_not_contain") or ["Local LLM"]),
        quality_bucket="psu_fact",
        risk=str(row.get("risk") or "medium"),
        source="broad_usage_eval_v1",
        note=f"from {row.get('id') or ''}".strip(),
    )


def _availability_cases() -> list[dict[str, Any]]:
    rows = _read_jsonl(CURATED / "service_game_availability.jsonl")
    cases: list[dict[str, Any]] = []
    for row in rows:
        service = str(row.get("service_label") or row.get("machine_label") or row.get("zone") or "")
        zone = str(row.get("zone") or "")
        capacity = str(row.get("capacity_persons") or "")
        games = [str(game) for game in row.get("games") or []]
        cases.append(_case("availability_service", f"{service} มีเกมอะไรบ้าง", expected_category="games", must_contain_any=games[:3], source="service_game_availability"))
        cases.append(_case("availability_service", f"{service} เล่นได้กี่คน", expected_category=["games", "reservation"], must_contain_any=[capacity, "คน"], source="service_game_availability"))
        cases.append(_case("availability_service", f"{zone} รายการเกมมีอะไรบ้าง", expected_category="games", must_contain_any=games[:3], source="service_game_availability"))
        for game in games:
            short = _short_title(game)
            cases.extend([
                _case("availability_game", f"{game} เล่นได้ที่เครื่องไหน", expected_category="games", must_contain_any=[service, zone.replace(" Zone", ""), short], source="service_game_availability"),
                _case("availability_game", f"มี {game} ไหม", expected_category="games", must_contain_any=[short, service, zone.replace(" Zone", "")], source="service_game_availability"),
                _case("availability_game", f"{short} อยู่โซนไหน", expected_category="games", must_contain_any=[zone.replace(" Zone", ""), service], source="service_game_availability"),
                _case("availability_game", f"ถ้าจะเล่น {short} ต้องจองอะไร", expected_category=["games", "reservation"], must_contain_any=[service, zone.replace(" Zone", ""), short], source="service_game_availability"),
            ])
    pc_negative = [
        ("PC #01", "Call of Duty: Warzone", "PC #03-#10"),
        ("PC #02", "Call of Duty: Warzone", "PC #03-#10"),
        ("PC #03", "TEKKEN 8", "PC #01-#02"),
        ("PC #10", "TEKKEN 8", "PC #01-#02"),
    ]
    for machine, game, should in pc_negative:
        cases.append(_case("availability_machine_split", f"{machine} มี {game} ไหม", expected_category="games", must_contain_any=["ไม่มี", should], source="service_game_availability", risk="high"))
    cases.extend([
        _case(
            "availability_service",
            "PC เครื่อง 1 รายการเกมมีอะไรบ้าง",
            expected_category="games",
            must_contain_any=["TEKKEN 8", "PC #01-#02"],
            source="service_game_availability",
            risk="high",
        ),
        _case(
            "availability_service",
            "PC เครื่อง 3 รายการเกมมีอะไรบ้าง",
            expected_category="games",
            must_contain_any=["Call of Duty: Warzone", "PC #03-#10"],
            source="service_game_availability",
            risk="high",
        ),
    ])
    return cases


def _game_detail_cases() -> list[dict[str, Any]]:
    rows = _read_jsonl(CURATED / "game_item_details.jsonl")
    short_counts = Counter(
        _short_title(str(row.get("game") or row.get("title") or "").strip()).lower()
        for row in rows
        if str(row.get("game") or row.get("title") or "").strip()
    )
    seen: set[str] = set()
    cases: list[dict[str, Any]] = []
    for row in rows:
        game = str(row.get("game") or row.get("title") or "").strip()
        if not game or _game_key(game) in seen:
            continue
        seen.add(_game_key(game))
        short = _short_title(game)
        short_is_family = short.lower() != game.lower() and short_counts[short.lower()] > 1
        genre = str(row.get("genre") or "").strip()
        zones = [str(zone) for zone in row.get("zones") or []]
        short_category: str | list[str] = ["games", "clarification"] if short_is_family else "games"
        short_expectation = [short, "หลายเกม", "ยังไม่ชัด"] if short_is_family else [genre.split("/")[0], short, "แนว"]
        play_expectation = [short, "หลายเกม", "ยังไม่ชัด"] if short_is_family else [short, "วิธีเล่น", "เล่น"]
        cases.extend([
            _case("game_detail", f"{game} คือเกมอะไร", expected_category="games", must_contain_any=[short, genre.split("/")[0], "เกม"], source="game_item_details"),
            _case("game_detail", f"{short} เป็นเกมแนวไหน", expected_category=short_category, must_contain_any=short_expectation, source="game_item_details"),
            _case("game_detail", f"{short} เล่นยังไง", expected_category=short_category, must_contain_any=play_expectation, source="game_item_details"),
        ])
        if zones:
            location_expectation = [short, "หลายเกม", "ยังไม่ชัด"] if short_is_family else [zones[0].replace(" Zone", ""), short]
            cases.append(_case("game_detail", f"{short} เล่นได้ที่ไหน", expected_category=short_category, must_contain_any=location_expectation, source="game_item_details"))
    return cases


def _control_cases() -> list[dict[str, Any]]:
    rows = _read_jsonl(CURATED / "game_control_facts.jsonl")
    current_games = {
        str(game)
        for item in _read_jsonl(CURATED / "service_game_availability.jsonl")
        for game in (item.get("games") or [])
        if str(game).strip()
    }
    current_game_keys = {_game_key(game) for game in current_games}
    current_short_counts = Counter(_short_title(game).lower() for game in current_games)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        game = str(row.get("game") or "").strip()
        if game:
            grouped.setdefault(game, []).append(row)
    cases: list[dict[str, Any]] = []
    for game, facts in sorted(grouped.items()):
        short = _short_title(game)
        buttons = [str(row.get("button") or "").strip() for row in facts if row.get("button")]
        actions = [str(row.get("action_th") or row.get("action_en") or "").strip() for row in facts if row.get("action_th") or row.get("action_en")]
        if _game_key(game) not in current_game_keys:
            unavailable_questions = [
                f"{game} ปุ่มทั้งหมดมีอะไรบ้าง",
                f"{short} ใช้จอยยังไง",
                f"ปุ่มของ {short} มีอะไรบ้าง",
                *(f"{short} ถ้าจะ{action}ต้องกดอะไร" for action in actions[:4] if action),
            ]
            for question in unavailable_questions:
                cases.append(_case(
                    "game_controls",
                    question,
                    expected_category=["games", "no_answer"],
                    expected_mode_prefix=[
                        "pipeline:structured_game_controls_no_current_game",
                        "pipeline:no_answer",
                    ],
                    must_contain_any=[game, "รายการเกมปัจจุบัน", "ยังไม่พบ"],
                    source="game_control_facts",
                    note="historical control source; game is not in current service availability",
                ))
            continue

        short_is_family = short.lower() != game.lower() and current_short_counts[short.lower()] > 1
        short_category: str | list[str] = ["games", "clarification"] if short_is_family else "games"
        short_expectation = [short, "หลายเกม", "ยังไม่ชัด"] if short_is_family else [short, "ปุ่ม", "controller", "จอย"]
        cases.extend([
            _case("game_controls", f"{game} ปุ่มทั้งหมดมีอะไรบ้าง", expected_category="games", expected_mode_prefix="pipeline:structured_game_controls", must_contain_any=[short, "ปุ่ม", *(buttons[:2])], source="game_control_facts"),
            _case("game_controls", f"{short} ใช้จอยยังไง", expected_category=short_category, must_contain_any=short_expectation, source="game_control_facts"),
            _case("game_controls", f"ปุ่มของ {short} มีอะไรบ้าง", expected_category=short_category, must_contain_any=short_expectation if short_is_family else [short, "ปุ่ม", *(buttons[:2])], source="game_control_facts"),
        ])
        for action, button in zip(actions[:4], buttons[:4]):
            if action and button:
                cases.append(_case(
                    "game_controls",
                    f"{short} ถ้าจะ{action}ต้องกดอะไร",
                    expected_category=short_category,
                    must_contain_any=short_expectation if short_is_family else [button, action],
                    source="game_control_facts",
                ))
    for question in [
        "ปุ่ม",
        "เล่นยังไง",
        "เกมนี้กดอะไร",
        "ปุ่มยิงคืออะไร",
        "อยากรู้ปุ่มของเกม",
        "เมื่อกี้ถาม Gran Turismo แล้ว ตอนนี้ขอปุ่ม",
        "Call of เล่นยังไง",
        "Mario Kart Live เล่นยังไง",
    ]:
        cases.append(_case("ambiguous_controls", question, expected_category=["games", "clarification", "no_answer"], must_contain_any=["ขอ", "เกม", "ปุ่ม", "ยังไม่"], quality_bucket="ambiguity", risk="high", source="handwritten"))
    return cases


def _service_fee_cases() -> list[dict[str, Any]]:
    services = [
        ("PC", ["0 บาท", "25 บาท", "70 บาท"]),
        ("PS5", ["0 บาท", "50 บาท", "150 บาท"]),
        ("Nintendo Switch", ["0 บาท", "50 บาท", "140 บาท"]),
        ("Cockpit", ["0 บาท", "65 บาท", "200 บาท"]),
        ("VR 30 นาที", ["0 บาท", "190 บาท", "525 บาท"]),
        ("VR 1 ชั่วโมง", ["0 บาท", "375 บาท", "1,050 บาท"]),
    ]
    users = [
        ("PSU Student", "0 บาท"),
        ("PSU Staff", "0 บาท"),
        ("Alumni", "บาท"),
        ("General Student", "บาท"),
        ("General Adult", "บาท"),
        ("คนทั่วไป", "บาท"),
        ("นักศึกษา PSU", "0 บาท"),
        ("นักศึกษาต่างมหาลัย", "บาท"),
    ]
    durations = ["30 นาที", "1 ชั่วโมง", "2 ชั่วโมง", "3 ชั่วโมง"]
    cases: list[dict[str, Any]] = []
    for service, markers in services:
        cases.append(_case("service_fee", f"{service} ราคาเท่าไหร่", expected_category="service_fee", must_contain=[service.split()[0], *markers[:2]], source="service_fee"))
        for user, marker in users:
            for duration in durations:
                cases.append(_case("service_fee", f"{user} เล่น {service} {duration} เสียกี่บาท", expected_category="service_fee", must_contain_any=[marker, "บาท", "ฟรี"], source="service_fee"))
    return cases


def _equipment_member_schedule_rule_cases() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for row in _read_jsonl(CURATED / "equipment_item_details.jsonl"):
        item = str(row.get("item") or "").strip()
        zone = str(row.get("zone") or "").strip()
        if not item:
            continue
        cases.extend([
            _case("equipment", f"{item} คืออะไร", expected_category="equipment", must_contain_any=[item.split()[0], zone.replace(" Zone", "")], source="equipment_item_details"),
            _case("equipment", f"{item} อยู่โซนไหน", expected_category="equipment", must_contain_any=[zone.replace(" Zone", ""), "Zone"], source="equipment_item_details"),
            _case("equipment", f"{item} ใช้ทำอะไร", expected_category="equipment", must_contain_any=[item.split()[0], "ใช้", zone.replace(" Zone", "")], source="equipment_item_details"),
        ])
    for row in _read_jsonl(CURATED / "member_profiles.jsonl"):
        name = str(row.get("name_th") or row.get("name") or "").strip()
        role = str(row.get("role") or row.get("position") or "").strip()
        if not name:
            continue
        cases.append(_case("members", f"{name} ทำตำแหน่งอะไร", expected_category="overview", must_contain_any=[name, role.split("/")[0]], source="member_profiles"))
        if role:
            cases.append(_case("members", f"ตำแหน่ง {role} คือใคร", expected_category="overview", must_contain_any=[name, role.split("/")[0]], source="member_profiles"))
    for question in [
        "วันจันทร์เปิดกี่โมง",
        "ศุกร์บ่ายเปิดไหม",
        "วันนี้เปิดไหม",
        "พรุ่งนี้เปิดไหม",
        "ช่วงเช้าวันจันทร์เปิดไหม",
        "วันศุกร์ช่วงบ่ายปิดใช่ไหม",
        "จองยังไง",
        "จองแล้วแก้ไขได้ไหม",
        "จองแล้วไม่สามารถยกเลิกได้ใช่ไหม",
        "ต้องจ่ายภายในกี่นาที",
        "เอาอาหารเข้าได้ไหม",
        "ทำจอยพังโดนปรับเท่าไหร่",
        "ของหายต้องทำยังไง",
        "กติกาในศูนย์มีอะไรบ้าง",
    ]:
        expected = "schedule" if "เปิด" in question or "ปิด" in question else ("reservation" if "จอง" in question or "จ่าย" in question else ["rules", "penalty"])
        cases.append(_case("policy_schedule_rules", question, expected_category=expected, must_contain_any=["เปิด", "ปิด", "จอง", "ยกเลิก", "นาที", "อาหาร", "ปรับ", "กติกา"], source="handwritten"))
    return cases


def _compound_cases(seed_questions: list[str]) -> list[dict[str, Any]]:
    games = ["TEKKEN 8", "Gran Turismo 7", "Beat Saber", "Mario Kart 8 Deluxe", "VALORANT", "Overcooked! 2", "Resident Evil Village"]
    services = ["PC", "PS5", "Nintendo Switch", "VR", "Cockpit"]
    cases: list[dict[str, Any]] = []
    for service in services:
        cases.append(_case("compound", f"{service} ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง", expected_category="multi_question", must_contain_any=[service, "บาท", "เกม"], quality_bucket="compound", source="handwritten"))
        cases.append(_case("compound", f"{service} จองยังไง แล้วเปิดวันไหนบ้าง", expected_category="multi_question", must_contain_any=[service, "จอง", "เปิด"], quality_bucket="compound", source="handwritten"))
    for left, right in zip(games, reversed(games)):
        cases.append(_case("compound", f"{left} กับ {right} มีปุ่มอะไรบ้าง", expected_category=["games", "multi_question"], must_contain_any=[_short_title(left), _short_title(right), "ปุ่ม"], quality_bucket="compound", source="handwritten"))
        cases.append(_case("compound", f"{left} เล่นที่ไหน แล้ว {right} ปุ่มอะไร", expected_category="multi_question", must_contain_any=[_short_title(left), _short_title(right)], quality_bucket="compound", source="handwritten"))
    for question in seed_questions[:80]:
        if "ราคา" not in question and "ปุ่ม" not in question:
            cases.append(_case("compound", f"{question} แล้วจองยังไง", expected_category=["multi_question", "reservation", "games", "equipment"], must_contain_any=["จอง", "เลือก", "บริการ"], quality_bucket="compound", source="broad_seed"))
    return cases


def _general_llm_cases() -> list[dict[str, Any]]:
    topics = [
        ("อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ", ["latency", "หน่วง"]),
        ("เฟรมเรตกับความละเอียดต่างกันยังไง", ["เฟรม", "ความละเอียด"]),
        ("API คืออะไร", ["API", "เชื่อมต่อ"]),
        ("JSON คืออะไร", ["JSON", "ข้อมูล"]),
        ("ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค", ["ขอบคุณ"]),
        ("แปลคำว่า reservation เป็นภาษาไทย", ["จอง"]),
        ("เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค", ["กิจกรรม"]),
        ("คีย์บอร์ด mechanical คืออะไรแบบสั้น", ["คีย์บอร์ด", "mechanical"]),
        ("GPU คืออะไรแบบเข้าใจง่าย", ["GPU", "กราฟิก"]),
        ("server กับ client ต่างกันยังไง", ["server", "client"]),
    ]
    cases: list[dict[str, Any]] = []
    variants = [
        "",
        "ตอบสั้น ๆ",
        "ขอแบบเข้าใจง่าย",
        "ตอบเป็นภาษาไทย",
        "ไม่ต้องยาว",
        "ขอ 1 ย่อหน้า",
        "อธิบายให้มือใหม่เข้าใจ",
        "ตอบแบบเด็กปีหนึ่งเข้าใจได้",
        "ขอแบบไม่ใช้ศัพท์ยาก",
        "ขอสรุปเป็น 2 ข้อ",
        "ขอคำตอบไม่เกิน 3 บรรทัด",
        "อธิบายแบบใช้ในงาน chatbot",
        "อธิบายแบบใช้กับวงการเกม",
        "ช่วยยกตัวอย่างสั้น ๆ",
        "เปรียบเทียบแบบสั้น",
        "ตอบแบบสุภาพ",
        "ตอบให้เหมาะกับนักศึกษา",
        "เขียนเป็นภาษาไทยธรรมชาติ",
        "ขอแบบไม่เป็นทางการมาก",
        "ขอแบบเป็นทางการ",
        "ช่วยสรุปใจความสำคัญ",
        "ตอบแบบ bullet สั้น ๆ",
        "ตอบแบบประโยคเดียว",
        "อธิบายข้อดีข้อเสียสั้น ๆ",
        "ให้คำจำกัดความแบบสั้น",
        "อธิบายด้วยคำง่าย ๆ",
        "ตอบแบบไม่ต้องมีตัวอย่างยาว",
        "ขอแบบใช้พูดกับผู้ใช้บริการ",
        "ช่วยปรับให้เป็นภาษาคนทั่วไป",
        "ขอคำตอบที่ไม่เกิน 50 คำ",
    ]
    for i in range(30):
        for question, tokens in topics:
            suffix = variants[i % len(variants)]
            full_question = f"{question} {suffix}".strip()
            cases.append(_case(
                "general_llm",
                full_question,
                expected_category=["general", "knowledge"],
                must_contain_any=tokens,
                must_not_contain=[],
                llm_required=True,
                quality_bucket="general_llm",
                risk="low",
                source="handwritten_general",
                note="No-LLM baseline should decline; LLM runs should answer.",
            ))
    game_concepts = [
        ("อธิบายคำว่า latency ในเกมแบบสั้น ๆ", ["latency", "หน่วง"]),
        ("FPS กับ TPS ต่างกันยังไงในวงการเกม", ["FPS", "TPS"]),
        ("MOBA คืออะไร", ["MOBA", "ทีม"]),
        ("battle royale คือเกมแนวไหน", ["battle royale", "เอาตัวรอด"]),
        ("ping สูงมีผลกับเกมออนไลน์ยังไง", ["ping", "หน่วง"]),
    ]
    for question, tokens in game_concepts:
        cases.append(_case(
            "general_game_concepts",
            question,
            expected_category=["general", "knowledge"],
            must_contain_any=tokens,
            must_not_contain=[],
            llm_required=True,
            quality_bucket="router_vs_general_llm",
            risk="high",
            source="handwritten_general",
            note="Should go to general LLM, not PSU game catalog.",
        ))
    return cases


def _dedupe_and_id(cases: list[dict[str, Any]], target: int) -> list[dict[str, Any]]:
    seen: set[str] = set()
    output: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    for case in cases:
        question = " ".join(str(case.get("question") or "").split())
        if not question or question.lower() in seen:
            continue
        seen.add(question.lower())
        case["question"] = question
        counters[str(case.get("group") or "case")] += 1
        prefix = re.sub(r"[^A-Z0-9]", "", "".join(part[:1].upper() for part in str(case["group"]).split("_")))[:5] or "MB"
        case["id"] = f"MB-{len(output) + 1:04d}-{prefix}-{counters[str(case['group'])]:03d}"
        output.append(case)
        if len(output) >= target:
            break
    return output


def build_cases(target: int) -> list[dict[str, Any]]:
    broad = [_normalize_broad_case(row) for row in _read_jsonl(BROAD_BANK)]
    broad_cases = [row for row in broad if row is not None]
    seed_questions = [str(row.get("question") or "") for row in broad_cases]
    generated = [
        *broad_cases,
        *_availability_cases(),
        *_game_detail_cases(),
        *_control_cases(),
        *_service_fee_cases(),
        *_equipment_member_schedule_rule_cases(),
        *_compound_cases(seed_questions),
        *_general_llm_cases(),
    ]
    return _dedupe_and_id(generated, target)


def main() -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(description="Generate 1,500+ deterministic benchmark questions for PSU model comparison.")
    parser.add_argument("--target", type=int, default=1600)
    parser.add_argument("--jsonl", default=str(OUT_JSONL))
    parser.add_argument("--json", default=str(OUT_JSON))
    args = parser.parse_args()

    rows = build_cases(max(args.target, 1500))
    _write_jsonl(Path(args.jsonl), rows)
    _write_json(Path(args.json), rows)
    counts = Counter(str(row.get("group")) for row in rows)
    print(f"Wrote {len(rows)} cases -> {args.jsonl}")
    for group, count in sorted(counts.items()):
        print(f"- {group}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
