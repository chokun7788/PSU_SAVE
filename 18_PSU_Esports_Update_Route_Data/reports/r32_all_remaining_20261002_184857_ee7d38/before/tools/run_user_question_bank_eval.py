from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CATEGORY_ORDER = [
    "game_rules",
    "play_booking_controls",
    "equipment_game_inside",
    "out_of_scope",
]


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


def _sources(hits: list[dict[str, Any]]) -> list[str]:
    result: list[str] = []
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_id = str(hit.get("id") or metadata.get("title") or metadata.get("source_id") or "").strip()
        url = str(metadata.get("source_url") or metadata.get("url") or "").strip()
        label = f"{source_id}: {url}" if source_id and url else (url or source_id)
        if label and label not in result:
            result.append(label)
    return result


def _strategy(mode: str, trace: list[Any]) -> str:
    trace_text = json.dumps(_plain(trace), ensure_ascii=False).lower()
    mode_text = mode.lower()
    if "llm" in mode_text:
        return "llm"
    if "game_control_vector" in mode_text or "vector" in trace_text:
        return "rag/vector"
    if "hybrid" in mode_text or "hybrid_retrieval" in trace_text:
        return "rag/hybrid"
    if "fast_path" in mode_text or "rule_fast" in mode_text or "deterministic" in trace_text:
        return "fastpath/rulebase"
    if "no_answer" in mode_text:
        return "no_answer"
    return "pipeline"


def _entry(category: str, index: int, question: str, expected: str, note: str = "") -> dict[str, Any]:
    prefixes = {
        "game_rules": "GR",
        "play_booking_controls": "PBC",
        "equipment_game_inside": "EGI",
        "out_of_scope": "OOS",
    }
    return {
        "id": f"{prefixes[category]}-{index:03d}",
        "category": category,
        "question_no": index,
        "question": question,
        "expected_support": expected,
        "note": note,
    }


def _game_rules_questions() -> list[dict[str, Any]]:
    aspects = [
        "คือเกมอะไร",
        "เป็นเกมแนวไหน",
        "มีข้อมูลกติกาการแข่งขันไหม",
        "แข่งขันใช้ผู้เล่นกี่คน",
        "มีตัวสำรองได้ไหม",
        "ถ้ามาสายจะเกิดอะไรขึ้น",
        "ถ้าเกมหลุดระหว่างแข่งต้องทำยังไง",
        "ขอ pause ระหว่างแข่งได้ไหม",
        "มีบทลงโทษอะไรบ้าง",
        "ใช้โปรแกรมช่วยเล่นได้ไหม",
        "ถ้าทีมไม่ครบลงแข่งได้ไหม",
        "รูปแบบการแข่งขันเป็นแบบไหน",
        "รอบชิงเล่นกี่เกม",
        "มีการแบนตัวละครหรือแผนที่ไหม",
        "ใช้บัญชีส่วนตัวหรือบัญชีที่จัดให้",
        "เปลี่ยนสมาชิกทีมได้ไหม",
        "ถ้าพบ bug ต้องแจ้งใคร",
        "ใช้ voice chat ได้ไหม",
        "ถ้าคู่แข่งไม่มาต้องทำยังไง",
        "ต้องเช็คอินก่อนแข่งไหม",
        "มีข้อห้ามเรื่องอุปกรณ์ไหม",
        "ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม",
        "มีกติกาเรื่อง remake หรือ restart ไหม",
        "ถ้าเน็ตล่มระหว่างแข่งนับผลยังไง",
        "แหล่งข้อมูลกติกามาจากไหน",
    ]
    games = [
        ("ROV", "competition_rules", "มีข้อมูลกติกาการแข่งขัน แต่ไม่ใช่เกมใน catalog เล่นของศูนย์"),
        ("VALORANT", "competition_rules", "มีทั้งข้อมูลเกมและกติกาบางส่วน"),
        ("CS2", "competition_rules", "มีข้อมูลกติกาการแข่งขัน"),
        ("TEKKEN 8", "competition_rules", "มีข้อมูลเกม/ปุ่ม/กติกาบางส่วน"),
    ]
    rows: list[dict[str, Any]] = []
    index = 1
    for game, expected, note in games:
        for aspect in aspects:
            rows.append(_entry("game_rules", index, f"{game} {aspect}", expected, note))
            index += 1
    return rows


def _play_booking_controls_questions() -> list[dict[str, Any]]:
    booking = [
        "จอง PS5 ต้องทำยังไง",
        "จอง Nintendo Switch ต้องเลือกอะไรบ้าง",
        "จอง VR ครึ่งชั่วโมงได้ไหม",
        "จอง Cockpit ต้องจองล่วงหน้ากี่ชั่วโมง",
        "จอง PC ต้องกรอกข้อมูลอะไรบ้าง",
        "หลังจองต้องจ่ายเงินภายในกี่นาที",
        "ถ้าจองผิดเวลาต้องแก้ยังไง",
        "ยกเลิกการจองต้องทำก่อนกี่ชั่วโมง",
        "ตอนเช็คอินต้องใช้บัตรอะไร",
        "เช็คอินล่วงหน้าได้กี่นาที",
        "จองได้สูงสุดกี่ session ต่อครั้ง",
        "ถ้าแนบสลิปผิดต้องทำยังไง",
        "จองแทนเพื่อนได้ไหม",
        "ถ้าไม่จ่ายเงินหลัง booking จะเกิดอะไรขึ้น",
        "อยากจองเครื่องเล่นเกมกับเพื่อนต้องเริ่มตรงไหน",
        "ถ้าไม่มีบัตรนักศึกษาตอนจองทำยังไง",
        "จอง VR 1 ชั่วโมงกับ 30 นาทีต่างกันยังไง",
        "จอง Nintendo สำหรับ 4 คนต้องเลือกแบบไหน",
        "อยากเล่นพวงมาลัยต้องจองโซนอะไร",
        "ถ้าไปถึงช้ากว่าเวลาจองจะยังเล่นได้ไหม",
        "จองแล้วเปลี่ยนคนเล่นได้ไหม",
        "จองแล้วขอเลื่อนวันได้ไหม",
        "ระบบจองออนไลน์อยู่ที่ไหน",
        "ก่อนเข้าใช้บริการต้องทำอะไรบ้าง",
        "ถ้าจะจองหลายอุปกรณ์พร้อมกันต้องทำยังไง",
        "จอง PlayStation 5 ใช้เวลารอบละกี่นาที",
        "จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม",
        "ถ้าระบบจองไม่ขึ้นควรถามใคร",
        "จองแล้วต้องตรวจสอบอีเมลไหม",
        "จ่ายเงินผ่านบัญชีอะไร",
        "สอนขั้นตอนจองแบบสั้นๆ",
        "ถ้าอยากเล่นวันนี้ต้องจองทันทีได้ไหม",
        "walk in ได้ไหมหรือต้องจองก่อน",
        "จองแล้วลืมเช็คอินจะเป็นอะไรไหม",
        "ต้องชำระเงินก่อนเล่นไหม",
        "ถ้าอยากเล่น PS5 กับเพื่อนสองคนต้องจองยังไง",
        "ถ้าอยากเล่น Switch สี่คนต้องจองยังไง",
        "ถ้าอยากลอง VR ครั้งแรกควรจองแบบไหน",
        "ถ้าอยากเล่นเกมขับรถต้องจองอะไร",
        "ถ้าจองผิดชื่อแก้ไขได้ไหม",
    ]
    controls = [
        "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง",
        "TEKKEN 8 ปุ่มเตะขวากดอะไร",
        "TEKKEN 8 ปุ่มต่อยซ้ายคือปุ่มไหน",
        "TEKKEN 8 ปุ่มเปิด Heat คืออะไร",
        "TEKKEN 8 ปุ่ม pause คืออะไร",
        "Mario Kart 8 Deluxe ปุ่มเร่งเครื่องคืออะไร",
        "Mario Kart 8 Deluxe ปุ่มดริฟต์กดอะไร",
        "Mario Kart 8 Deluxe ปุ่มใช้ไอเทมคืออะไร",
        "Mario Kart Live Home Circuit ปุ่มทั้งหมดมีอะไรบ้าง",
        "Mario Kart Live Home Circuit ปุ่มเร่งเครื่องกดอะไร",
        "Call of Duty ปุ่มกระโดดคืออะไร",
        "Call of Duty ปุ่มยิงคือปุ่มไหน",
        "Call of Duty ปุ่มเล็งคืออะไร",
        "Call of Duty ปุ่มรีโหลดคืออะไร",
        "Naruto X Boruto ปุ่มโจมตีคืออะไร",
        "Naruto X Boruto ปุ่มคาถานินจาคืออะไร",
        "Naruto X Boruto ปุ่มสลับร่างคืออะไร",
        "Little Nightmares II ปุ่มวิ่งคืออะไร",
        "Little Nightmares II ปุ่มกระโดดคืออะไร",
        "It Takes Two ปุ่มกระโดดคืออะไร",
        "It Takes Two ปุ่มโต้ตอบคืออะไร",
        "Overcooked 2 ปุ่มหยิบของคืออะไร",
        "Overcooked 2 ปุ่มหั่นของคืออะไร",
        "Super Smash Bros Ultimate ปุ่มโจมตีคืออะไร",
        "Super Smash Bros Ultimate ปุ่มกระโดดคืออะไร",
        "Nintendo Switch Sports ใช้จอยยังไง",
        "Beat Saber เล่นยังไง",
        "Gran Turismo 7 ใช้พวงมาลัยยังไง",
        "เกมนี้มีปุ่มอะไรบ้าง",
        "เล่นยังไง",
        "วิธีใช้จอย",
        "มีปุ่มอะไรบ้างถ้ายังไม่ได้บอกชื่อเกม",
        "ปุ่มทั้งหมดของเกมที่เพิ่งถามคืออะไร",
        "ถ้าถามต่อว่าใช้จอยยังไงระบบจำเกมเดิมไหม",
        "ถามปุ่มเฉพาะของเกมที่ไม่มีข้อมูลจะตอบยังไง",
        "Minecraft มีปุ่มอะไรบ้างในศูนย์",
        "ROV มีปุ่มในเครื่องศูนย์ไหม",
        "เกมที่ไม่มีชื่อชัดเจนควรตอบปุ่มไหม",
        "ถ้าอยากรู้ปุ่มของ PS5 ต้องถามแบบไหน",
        "controller ของ Nintendo ใช้ยังไง",
        "ปุ่ม Options ใน TEKKEN 8 ทำอะไร",
        "ปุ่ม Cross ใน TEKKEN 8 ทำอะไร",
        "ปุ่ม Circle ใน TEKKEN 8 ทำอะไร",
        "ปุ่ม Triangle ใน TEKKEN 8 ทำอะไร",
        "ปุ่ม Square ใน TEKKEN 8 ทำอะไร",
        "D-Pad ใน TEKKEN 8 ใช้ทำอะไร",
        "L1 ใน TEKKEN 8 ใช้ทำอะไร",
        "R1 ใน TEKKEN 8 ใช้ทำอะไร",
        "Mario Kart Live ปุ่มจัดการแผนที่คืออะไร",
        "Mario Kart Live ปุ่มดูข้อมูลรถคืออะไร",
        "Mario Kart 8 ปุ่มเบรกคืออะไร",
        "Mario Kart 8 ปุ่มมองหลังคืออะไร",
        "Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง",
        "Naruto X Boruto ปุ่มทั้งหมดมีอะไรบ้าง",
        "Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง",
        "Super Smash Bros ปุ่มทั้งหมดมีอะไรบ้าง",
        "It Takes Two ปุ่มทั้งหมดมีอะไรบ้าง",
        "Little Nightmares II ปุ่มทั้งหมดมีอะไรบ้าง",
        "ถ้าไม่รู้ชื่อเกมแต่ถามปุ่ม ระบบควรถามกลับไหม",
        "วิธีเล่นเกมที่ไม่อยู่ในรายการต้องตอบยังไง",
    ]
    rows: list[dict[str, Any]] = []
    for index, question in enumerate([*booking, *controls], 1):
        expected = "in_kb" if index <= 40 else "game_controls_or_clarification"
        rows.append(_entry("play_booking_controls", index, question, expected))
    return rows[:100]


def _equipment_game_inside_questions() -> list[dict[str, Any]]:
    zone_questions = [
        "PC Zone มีอุปกรณ์อะไรบ้าง",
        "PC Zone มีคอมกี่เครื่อง",
        "PC Zone ใช้จออะไร",
        "PC Zone มีเมาส์กับคีย์บอร์ดไหม",
        "PC Zone มีหูฟังไหม",
        "Cockpit Zone มีอุปกรณ์อะไรบ้าง",
        "Cockpit Zone มีพวงมาลัยรุ่นอะไร",
        "Cockpit Zone มีทีวีกี่เครื่อง",
        "Cockpit Zone เหมาะกับเกมอะไร",
        "Cockpit Zone มีชุดขับรถกี่ชุด",
        "Nintendo Switch Zone มีอะไรบ้าง",
        "Nintendo Switch Zone มีทีวีขนาดเท่าไหร่",
        "Nintendo Switch Zone มีโซฟากี่ตัว",
        "Nintendo Switch Zone มีเครื่อง Switch กี่เครื่อง",
        "Nintendo Switch Zone เล่นกับเพื่อนได้ไหม",
        "PlayStation 5 Zone มีอะไรบ้าง",
        "PS5 Zone มีเครื่องกี่เครื่อง",
        "PS5 Zone ใช้รุ่นอะไร",
        "PS5 Zone มีเกมอะไรบ้าง",
        "PS5 Zone เหมาะกับเกมแนวไหน",
        "VR Zone มีอะไรบ้าง",
        "VR Zone มี PS5 กี่เครื่อง",
        "VR Zone ใช้แว่นรุ่นอะไร",
        "VR Zone มีเกมอะไรบ้าง",
        "VR Zone เหมาะกับมือใหม่ไหม",
        "หน้า Home มีอุปกรณ์ทั้งหมดอะไรบ้าง",
        "อุปกรณ์บนหน้า Home แยกตามโซนให้หน่อย",
        "โซนไหนมีทีวีขนาด 86 นิ้ว",
        "โซนไหนมีทีวี 65 นิ้ว",
        "โซนไหนมี PlayStation VR2",
        "โซนไหนมี Logitech G923",
        "โซนไหนมี Gaming PC",
        "โซนไหนมีโซฟา",
        "โซนไหนมี Racezone Full Cockpit",
        "โซนไหนมี Pulse Elite Headset",
        "ถ้าอยากเล่นเกมขับรถควรใช้โซนไหน",
        "ถ้าอยากเล่นเกมกับเพื่อนหลายคนควรใช้โซนไหน",
        "ถ้าอยากลอง VR ต้องใช้อุปกรณ์อะไร",
        "ถ้าอยากเล่นเกม PC/FPS มีโซนไหน",
        "ถ้าอยากเล่นเกมปาร์ตี้มีโซนไหน",
    ]
    game_inside = [
        "PS5 มีเกมอะไรบ้าง",
        "Nintendo Switch มีเกมอะไรบ้าง",
        "PC มีเกมอะไรบ้าง",
        "VR มีเกมอะไรบ้าง",
        "Cockpit มีเกมอะไรบ้าง",
        "เกมทั้งหมดในศูนย์มีอะไรบ้าง",
        "เกมทั้งหมดมีกี่เกม",
        "เกมแนว Racing มีอะไรบ้าง",
        "เกมแนว MOBA มีอะไรบ้าง",
        "เกมแนว FPS มีอะไรบ้าง",
        "เกมแนว Fighting มีอะไรบ้าง",
        "เกมแนว Party มีอะไรบ้าง",
        "เกมแนว Rhythm มีอะไรบ้าง",
        "เกมแนว Survival มีไหม",
        "VALORANT เล่นได้ที่ไหน",
        "CS2 เล่นได้ที่ไหน",
        "PUBG เล่นได้ที่ไหน",
        "Warzone เล่นได้ที่ไหน",
        "League of Legends เล่นได้ที่ไหน",
        "TEKKEN 8 เล่นได้ที่ไหน",
        "Spider-Man 2 เล่นได้ที่ไหน",
        "Fortnite เล่นได้ที่ไหน",
        "God of War Ragnarok เล่นได้ที่ไหน",
        "Overcooked 2 เล่นได้ที่ไหน",
        "Gran Turismo 7 เล่นได้ที่ไหน",
        "Beat Saber เล่นได้ที่ไหน",
        "It Takes Two เล่นได้ที่ไหน",
        "Little Nightmares II เล่นได้ที่ไหน",
        "Monster Hunter Rise เล่นได้ที่ไหน",
        "EA Sports FC 24 เล่นได้ที่ไหน",
        "Final Fantasy XVI เล่นได้ที่ไหน",
        "Hogwarts Legacy เล่นได้ที่ไหน",
        "Naruto X Boruto เล่นได้ที่ไหน",
        "Resident Evil 4 เล่นได้ที่ไหน",
        "Resident Evil Village เล่นได้ที่ไหน",
        "The Last of Us มีไหม",
        "Uncharted มีไหม",
        "Mario Kart 8 Deluxe มีไหม",
        "Mario Kart Live Home Circuit มีไหม",
        "Super Smash Bros Ultimate มีไหม",
        "Nintendo Switch Sports มีไหม",
        "Animal Crossing มีไหม",
        "Luigi's Mansion 3 มีไหม",
        "Mario Party Superstars มีไหม",
        "Moving Out 2 มีไหม",
        "Super Mario Odyssey มีไหม",
        "Zelda Breath of the Wild มีไหม",
        "Ring Fit Adventure มีไหม",
        "Minecraft มีไหม",
        "Roblox มีไหม",
        "ROV มีให้เล่นในศูนย์ไหม",
        "เกมไหนยังไม่มีข้อมูลบ้าง",
        "เกมไหนมีข้อมูลปุ่มครบ",
        "เกมที่เล่นได้บนทั้ง PS5 และ Nintendo มีอะไรบ้าง",
        "เกมไหนเล่นได้ทั้ง PC และ PS5",
        "เกมสำหรับเล่นกับเพื่อนมีอะไรบ้าง",
        "เกมสำหรับเด็กหรือมือใหม่มีอะไรบ้าง",
        "เกมที่ใช้พวงมาลัยมีอะไร",
        "เกมที่ต้องใช้ VR มีอะไร",
        "เกมที่ใช้จอย PS5 มีอะไร",
    ]
    rows: list[dict[str, Any]] = []
    for index, question in enumerate([*zone_questions, *game_inside], 1):
        rows.append(_entry("equipment_game_inside", index, question, "in_kb_or_catalog"))
    return rows[:100]


def _out_of_scope_questions() -> list[dict[str, Any]]:
    questions = [
        "สอนทำข้าวผัดแบบง่ายๆ",
        "วันนี้ฝนจะตกไหม",
        "ช่วยแปลประโยคนี้เป็นอังกฤษได้ไหม",
        "สูตรคำนวณพื้นที่วงกลมคืออะไร",
        "ขอไอเดียตั้งชื่อร้านกาแฟ",
        "ช่วยเขียนคำอวยพรวันเกิดให้เพื่อน",
        "วิธีลดน้ำหนักที่ปลอดภัยควรเริ่มยังไง",
        "อาการปวดหัวบ่อยควรทำยังไง",
        "หุ้นตัวไหนดีวันนี้",
        "ราคาทองวันนี้เท่าไหร่",
        "ข่าวการเมืองล่าสุดคืออะไร",
        "ใครเป็นนายกรัฐมนตรีตอนนี้",
        "ช่วยแต่งกลอนสั้นๆ เรื่องทะเล",
        "Python list comprehension คืออะไร",
        "JavaScript promise คืออะไร",
        "ช่วยเขียน SQL select เบื้องต้น",
        "วิธีสมัคร Gmail ทำยังไง",
        "แนะนำโน้ตบุ๊กเล่นเกมหน่อย",
        "iPhone รุ่นไหนคุ้มสุด",
        "เที่ยวภูเก็ต 1 วันไปไหนดี",
        "ร้านอาหารใกล้ฉันมีอะไรบ้าง",
        "แผนที่ไปสนามบินภูเก็ต",
        "วิธีทำพาสปอร์ต",
        "ต่อภาษีรถต้องทำยังไง",
        "ยื่นภาษีบุคคลธรรมดายังไง",
        "เขียน resume ภาษาอังกฤษยังไง",
        "ช่วยซ้อมสัมภาษณ์งานหน่อย",
        "คำว่า resilience แปลว่าอะไร",
        "ทำไมท้องฟ้าถึงเป็นสีฟ้า",
        "โลกร้อนเกิดจากอะไร",
        "AI คืออะไรแบบง่ายๆ",
        "LLM ทำงานยังไง",
        "RAG คืออะไร",
        "Docker คืออะไร",
        "Git commit กับ push ต่างกันยังไง",
        "Vercel คืออะไร",
        "Neon database คืออะไร",
        "SQLite ต่างจาก Postgres ยังไง",
        "ช่วยวางแผนอ่านหนังสือสอบ",
        "วิธีจัดการเวลาให้ดีขึ้น",
        "วิธีนอนให้หลับง่าย",
        "ควรดื่มน้ำวันละเท่าไหร่",
        "อาหารเช้าควรกินอะไร",
        "วิธีปลูกต้นไม้ในห้อง",
        "วิธีดูแลกล้องถ่ายรูปเบื้องต้น",
        "วิธีดูแลคอมไม่ให้ช้า",
        "ทำไม Wi-Fi ช้า",
        "วิธีตั้งรหัสผ่านให้ปลอดภัย",
        "phishing คืออะไร",
        "ช่วยคิด caption ลง Instagram",
        "เขียน bio โปรไฟล์ให้หน่อย",
        "ช่วยสรุปนิยายที่ฉันชอบได้ไหม",
        "วิธีทำบันทึกรายรับรายจ่าย",
        "ขอไอเดียของขวัญรับปริญญา",
        "ช่วยตั้งชื่อช่อง YouTube",
        "วิธีฝึกวาดรูปเบื้องต้น",
        "วันนี้มีบอลคู่ไหน",
        "ตาราง NBA วันนี้",
        "ผลพรีเมียร์ลีกล่าสุด",
        "ค่าเงิน USD เป็น THB เท่าไหร่",
        "Bitcoin ราคาเท่าไหร่",
        "ช่วยวางแผนเที่ยวญี่ปุ่น",
        "ขอ checklist จัดกระเป๋าเดินทาง",
        "วิธีจองตั๋วเครื่องบินราคาถูก",
        "ประกันสุขภาพเลือกยังไง",
        "บัตรเครดิตใบไหนดี",
        "กู้ซื้อบ้านต้องเตรียมอะไร",
        "ดอกเบี้ยทบต้นคืออะไร",
        "วิธีเริ่มลงทุนกองทุนรวม",
        "ช่วยเขียนอีเมลขอลางาน",
        "ช่วยเขียนประกาศรับสมัครงาน",
        "ช่วยทำสคริปต์นำเสนอ 3 นาที",
        "สอนทำ PowerPoint ให้น่าสนใจ",
        "วิธีอ่านงบการเงินเบื้องต้น",
        "เศรษฐกิจเงินเฟ้อคืออะไร",
        "ประวัติศาสตร์สงครามโลกครั้งที่สอง",
        "ดาวอังคารอยู่ไกลแค่ไหน",
        "ระบบสุริยะมีดาวอะไรบ้าง",
        "ทำไมทะเลถึงเค็ม",
        "ช่วยแก้โจทย์คณิตสมการกำลังสอง",
        "วิธีจำศัพท์อังกฤษ",
        "ฝึกพูดอังกฤษด้วยตัวเองยังไง",
        "แปลไทยเป็นญี่ปุ่นได้ไหม",
        "ช่วยตรวจแกรมมาร์ประโยคอังกฤษ",
        "ทำไมคอมเปิดไม่ติด",
        "Windows update ค้างทำยังไง",
        "ลืมรหัสผ่าน Facebook ทำยังไง",
        "บัญชีโดนแฮกควรทำยังไง",
        "ทำ portfolio สมัครงานยังไง",
        "เรียนสาย data ต้องเริ่มจากอะไร",
        "Data analyst ใช้เครื่องมืออะไร",
        "Machine learning ต่างจาก deep learning ยังไง",
        "Prompt engineering คืออะไร",
        "ช่วยคิด business model ร้านชา",
        "วิธีทำแบบสอบถามออนไลน์",
        "ทำ infographic ด้วยเครื่องมืออะไร",
        "เพลงฮิตตอนนี้มีอะไรบ้าง",
        "หนังน่าดูปีนี้มีเรื่องอะไร",
        "ช่วยคิดเมนูอาหารเย็น",
        "ทำกาแฟลาเต้เองที่บ้านยังไง",
    ]
    return [_entry("out_of_scope", index, question, "general_llm_or_decline") for index, question in enumerate(questions, 1)]


def build_question_bank() -> list[dict[str, Any]]:
    groups = [
        _game_rules_questions(),
        _play_booking_controls_questions(),
        _equipment_game_inside_questions(),
        _out_of_scope_questions(),
    ]
    rows = [entry for group in groups for entry in group]
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    expected_counts = {
        "game_rules": 100,
        "play_booking_controls": 100,
        "equipment_game_inside": 100,
        "out_of_scope": 100,
    }
    if counts != expected_counts:
        raise RuntimeError(f"question bank counts mismatch: {counts}")
    return rows


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def _group_by_category(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row.get("category", "unknown")), []).append(row)
    return grouped


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "category",
        "question_no",
        "question",
        "expected_support",
        "mode",
        "route",
        "strategy",
        "latency_sec",
        "wall_sec",
        "sources",
        "answer",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _write_markdown(path: Path, rows: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# User Question Bank Evaluation",
        "",
        f"- Generated at: {summary['generated_at']}",
        f"- Total questions: {summary['total']}",
        f"- Total wall time: {summary['total_wall_sec']}s",
        "",
        "## Summary By Strategy",
    ]
    for strategy, count in sorted(summary["strategy_counts"].items()):
        lines.append(f"- {strategy}: {count}")
    lines.extend(["", "## Results"])
    for row in rows:
        answer_preview = str(row.get("answer", "")).replace("\n", " ")
        if len(answer_preview) > 260:
            answer_preview = answer_preview[:260].rstrip() + "..."
        lines.extend([
            "",
            f"### {row['id']} {row['category']} ข้อ {row['question_no']}",
            f"- Question: {row['question']}",
            f"- Expected: {row['expected_support']}",
            f"- Mode: `{row['mode']}`",
            f"- Route: `{row['route']}`",
            f"- Strategy: `{row['strategy']}`",
            f"- Latency: {row['latency_sec']}s | Wall: {row['wall_sec']}s",
            f"- Sources: {row['sources'] or '-'}",
            f"- Answer: {answer_preview}",
        ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _filter_bank(rows: list[dict[str, Any]], category: str, start: int, limit: int | None) -> list[dict[str, Any]]:
    if category != "all":
        rows = [row for row in rows if row["category"] == category]
    if start > 1:
        rows = rows[start - 1:]
    if limit is not None:
        rows = rows[:limit]
    return rows


def _run_questions(rows: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    from app.runtime.pipeline_answer import answer_question_pipeline_debug

    results: list[dict[str, Any]] = []
    for position, item in enumerate(rows, 1):
        question = item["question"]
        started = time.perf_counter()
        result = answer_question_pipeline_debug(
            question,
            experimental_rag_fallback=not args.no_rag_fallback,
            experimental_allow_llm=args.allow_llm,
        )
        wall = round(time.perf_counter() - started, 4)
        strategy = _strategy(result.mode, result.trace)
        row = {
            **item,
            "run_position": position,
            "mode": result.mode,
            "route": f"{result.route.category}/{result.route.intent}",
            "strategy": strategy,
            "latency_sec": result.elapsed,
            "wall_sec": wall,
            "sources": " | ".join(_sources(result.hits)),
            "answer": result.answer,
            "trace": _plain(result.trace) if args.include_trace else None,
            "validation": _plain(result.validation),
        }
        results.append(row)
        if not args.quiet:
            print(f"[{position}/{len(rows)}] {row['id']} {strategy} {result.mode} {wall}s")
            print(f"Q: {question}")
            preview = str(result.answer or "")[:args.answer_preview_chars].replace(chr(10), " ")
            print(f"A: {preview}")
            print()
        elif position == 1 or position == len(rows) or position % args.progress_every == 0:
            print(f"[{position}/{len(rows)}] {row['id']} {strategy} {wall}s")
    return results


def _summarize_results(
    results: list[dict[str, Any]],
    started_at: float,
    args: argparse.Namespace,
    export_jsonl_path: Path,
    export_json_path: Path,
) -> dict[str, Any]:
    strategy_counts: dict[str, int] = {}
    mode_counts: dict[str, int] = {}
    route_counts: dict[str, int] = {}
    for row in results:
        strategy_counts[row["strategy"]] = strategy_counts.get(row["strategy"], 0) + 1
        mode_counts[row["mode"]] = mode_counts.get(row["mode"], 0) + 1
        route_counts[row["route"]] = route_counts.get(row["route"], 0) + 1
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total": len(results),
        "total_wall_sec": round(time.perf_counter() - started_at, 3),
        "strategy_counts": strategy_counts,
        "mode_counts": mode_counts,
        "route_counts": route_counts,
        "allow_llm": args.allow_llm,
        "rag_fallback": not args.no_rag_fallback,
        "question_bank_jsonl": str(export_jsonl_path),
        "question_bank_json": str(export_json_path),
    }


def _write_run_outputs(out_dir: Path, results: list[dict[str, Any]], summary: dict[str, Any]) -> None:
    _write_jsonl(out_dir / "results.jsonl", results)
    _write_json(out_dir / "results.json", results)
    _write_json(out_dir / "results_by_category.json", _group_by_category(results))
    _write_csv(out_dir / "results.csv", results)
    _write_markdown(out_dir / "report.md", results, summary)
    _write_json(out_dir / "summary.json", summary)


def run_eval(args: argparse.Namespace) -> int:
    bank = build_question_bank()
    suffix = "_by_category" if args.split_category_dirs else ""
    out_dir = Path(args.out_dir) if args.out_dir else ROOT / "data" / "eval" / "question_bank_runs" / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}{suffix}"
    export_jsonl_path = ROOT / "data" / "eval" / "user_question_bank_400.jsonl"
    export_json_path = ROOT / "data" / "eval" / "user_question_bank_400.json"
    _write_jsonl(export_jsonl_path, bank)
    _write_json(export_json_path, bank)

    selected = _filter_bank(bank, args.category, args.start, args.limit)
    if args.export_bank_only:
        print(f"exported question bank jsonl: {export_jsonl_path}")
        print(f"exported question bank json: {export_json_path}")
        return 0

    started_all = time.perf_counter()
    if args.split_category_dirs:
        all_results: list[dict[str, Any]] = []
        category_summaries: dict[str, Any] = {}
        categories = CATEGORY_ORDER if args.category == "all" else [args.category]
        for category in categories:
            category_rows = _filter_bank(bank, category, args.start, args.limit)
            category_dir = out_dir / category
            print(f"category: {category} -> {category_dir}")
            category_started = time.perf_counter()
            category_results = _run_questions(category_rows, args)
            category_summary = _summarize_results(
                category_results,
                category_started,
                args,
                export_jsonl_path,
                export_json_path,
            )
            category_summary["category"] = category
            _write_run_outputs(category_dir, category_results, category_summary)
            all_results.extend(category_results)
            category_summaries[category] = category_summary
        summary = _summarize_results(all_results, started_all, args, export_jsonl_path, export_json_path)
        summary["split_category_dirs"] = True
        summary["category_summaries"] = category_summaries
        _write_json(out_dir / "summary.json", summary)
    else:
        results = _run_questions(selected, args)
        summary = _summarize_results(results, started_all, args, export_jsonl_path, export_json_path)
        _write_run_outputs(out_dir, results, summary)
    print(f"question bank jsonl: {export_jsonl_path}")
    print(f"question bank json: {export_json_path}")
    print(f"results dir: {out_dir}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run 400 user-like questions against the PSU Esports chatbot pipeline.")
    parser.add_argument("--category", choices=["all", "game_rules", "play_booking_controls", "equipment_game_inside", "out_of_scope"], default="all")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--allow-llm", action="store_true", help="enable Local LLM fallback for general/out-of-scope questions")
    parser.add_argument("--no-rag-fallback", action="store_true")
    parser.add_argument("--include-trace", action="store_true")
    parser.add_argument("--export-bank-only", action="store_true")
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--split-category-dirs", action="store_true", help="save each category into its own folder")
    parser.add_argument("--quiet", action="store_true", help="print compact progress while saving full answers to files")
    parser.add_argument("--progress-every", type=int, default=10)
    parser.add_argument("--answer-preview-chars", type=int, default=500)
    return parser.parse_args()


def main() -> int:
    _configure_stdout()
    return run_eval(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
