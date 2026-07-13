from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.schemas import PipelineTrace


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"
COMPETITION_FACT_CARDS_PATH = ROOT / "data" / "competition_rules" / "competition_rule_fact_cards.jsonl"
COMPETITION_FACT_CARD_GLOB = "competition_rule_fact_cards*.jsonl"

STOPWORDS = {
    "คือ", "อะไร", "ไหม", "มั้ย", "ครับ", "ค่ะ", "คะ", "หน่อย", "ได้", "หรือ", "และ",
    "the", "is", "are", "can", "do", "does", "what", "how",
}

GAME_DETAIL_TERMS = (
    "คืออะไร", "อะไรคือ", "เกมอะไร", "แนวอะไร", "เกี่ยวกับอะไร",
    "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "เล่นแบบไหน", "สอนเล่น",
)

GAME_ENTITY_STOPWORDS = {
    "เกม", "เล่น", "วิธี", "สอน", "คือ", "อะไร", "ยังไง", "อย่างไร", "ได้ไหม", "ไหม",
    "game", "games", "how", "what", "play",
}


COMPETITION_GAME_ALIASES = {
    "Counter-Strike 2": ("cs2", "counter-strike", "counter strike", "เคาเตอร์"),
    "VALORANT": ("valorant", "วาโล", "valo"),
    "Arena of Valor (RoV)": ("rov", "arena of valor", "aov", "blueket", "เกมตีป้อม", "อาโอวี"),
    "Tekken 8": ("tekken", "tekken8", "tekken 8", "เทคเคน", "เทคเคน 8"),
}

KNOWN_COMPETITION_MAPS = (
    "Abyss", "Ascent", "Bind", "Corrode", "Haven", "Lotus", "Sunset",
    "Ancient", "Anubis", "Dust 2", "Inferno", "Mirage", "Nuke", "Train",
)

COMPETITION_INTENT_ALIASES = {
    "team_size": ("กี่คน", "ครบ 4", "เหลือ 4", "ทีมละ", "สมาชิก", "ผู้เล่น", "5v5", "roster", "จำนวนคน", "จำนวนผู้เล่น", "ทีม 5", "5 คน", "team", "teams", "team size", "team 5", "player", "players", "member", "members", "ตัวจริง", "ตัวสำรอง"),
    "map_pool": ("แผนที่", "map", "map pool", "mapban", "mapban.gg", "ban map", "map veto", "veto", "เหลือกี่", "3 maps", "3 map", "3 แผนที่", "เลือกแผนที่", "ancient", "anubis", "dust 2", "inferno", "mirage", "nuke", "train", "abyss", "ascent", "bind", "corrode", "haven", "lotus", "sunset"),
    "pause": ("timeout", "pause", "technical", "emergency", "เวลานอก", "หยุดเกม", "หลุดเกม", "disconnect", "hardware", "เครื่องมีปัญหา", "ขอหยุด", "กดหยุด", "กลางรอบ", "ยิงกัน", "resume", "เน็ตล่ม", "เน็ตทั้งโซน", "เซิร์ฟเวอร์", "server", "อุปกรณ์ขัดข้อง", "จอยมีปัญหา", "ซอฟต์แวร์", "สรุป pause"),
    "skin": ("สกิน", "skin", "default"),
    "equipment": ("เครื่อง", "อุปกรณ์", "ใช้เครื่อง", "โทรศัพท์มือถือ", "มือถือ", "tablet", "ipad", "playstation", "ps5", "platform", "คีย์บอร์ด", "เมาส์", "crosshair", "resolution", "brightness", "macro", "script", "ติดตั้งโปรแกรม", "install", "software", "facebook", "โซเชียล", "social media", "snap tap", "socd"),
    "late_start": ("ช้า", "ล่าช้า", "มาสาย", "เลท", "เกิน 15", "15 นาที", "สิบห้านาที", "late", "เริ่ม match", "เริ่มแข่ง"),
    "format": ("รูปแบบ", "single elimination", "bo3", "bo5", "ft2", "round", "1v1", "1 ต่อ 1", "ตัวต่อตัว", "5v5", "format", "เล่นแบบไหน", "วินาที", "best of 3", "best-of-3", "กี่เกม", "เล่นกี่เกม", "แข่งกี่เกม", "ต้องเล่นกี่เกม", "ชนะกี่เกม", "กี่แมตช์", "กี่แมทช์", "กี่ตา", "bo อะไร", "รอบรอง", "รอบชิง", "แพ้คัดออก", "เกมตัดสิน", "เสมอ", "1-1", "ชนะครบ 2 เกม"),
    "character": ("character", "ตัวละคร", "dlc", "agent", "เอเจนท์", "ฮีโร่", "customization", "แต่งชุด", "ทรงผม", "เอฟเฟกต์", "ออร่า", "new map", "new agent", "restriction", "คอนเทนต์ใหม่"),
    "rematch": ("rematch", "remake", "แข่งใหม่", "เริ่มใหม่", "first blood", "ฝ่ายตรงข้าม", "ยินยอม"),
    "eligibility": ("คุณสมบัติ", "รับเฉพาะ", "เฉพาะนักศึกษา", "คนนอก", "นักศึกษา", "มหาวิทยาลัยสงขลานครินทร์", "ภูเก็ต", "psu", "ลงแข่งได้ไหม", "เล่นให้สองทีม", "ทีมเดียว", "ถอนตัว", "ตัดสิทธิ์"),
    "registration": ("สมัคร", "ลงทะเบียน", "ลงชื่อ", "ปิดรับสมัคร", "หลังปิดรับสมัคร", "ลงทะเบียนเพิ่ม", "เพิ่มชื่อ", "ค่อยเพิ่ม", "ไม่ครบ", "รับสมัคร"),
    "roster_change": ("เปลี่ยนสมาชิก", "สมาชิกทีม", "ระหว่างทัวร์", "ถอนตัว", "เปลี่ยนตัว", "ตัวจริงติดธุระ", "แทน", "ไม่ได้ลงชื่อ", "หน้างาน", "roster", "lineup", "ทีมเดียว"),
    "game_version": ("เวอร์ชัน", "เวอร์ชั่น", "version", "ล่าสุด", "steam", "แพลตฟอร์ม", "ดัดแปลง", "mod", "ตัวเกม"),
    "language": ("ภาษา", "ภาษาทางการ", "ประท้วง", "รายงานผล", "สื่อสาร"),
    "schedule_location": ("กี่วัน", "จัดที่ไหน", "สถานที่", "แข่งที่ไหน", "อาคาร", "ห้อง", "5102a", "psu esports studio", "phuket", "วิทยาเขตภูเก็ต"),
    "schedule": ("ตาราง", "สายการแข่งขัน", "ประกาศล่วงหน้า", "ล่วงหน้า", "วันแข่ง", "กำหนดการแข่งขัน", "ลงทะเบียนช่วง", "check in", "check-in", "รายงานตัว", "แบ่งสาย", "รอบ 5 ทีม", "รอบชิงอันดับ", "รอบชิงชนะเลิศ", "match schedule"),
    "communication": ("discord", "สื่อสาร", "เซิร์ฟเวอร์", "ช่องทาง", "server"),
    "game_setting": ("competitive", "เงินเริ่มต้น", "freeze", "freeze time", "เวลาต่อรอบ", "ต่อรอบ", "ระเบิด", "รอบละ", "ชนะกี่", "สูงสุดกี่", "ต่อเวลา", "overtime", "mr12", "r3", "3 rounds", "3 รอบ", "60 วินาที", "advantage", "stage", "random", "ด่าน", "สุ่ม", "assist", "blood", "bodies", "เลือด", "ศพ", "fps", "latency"),
    "side_selection": ("เลือกฝั่ง", "สีน้ำเงิน", "สีแดง", "ดวลมีด", "โยนเหรียญ", "แพ้เกมก่อนหน้า", "เกมแรก", "ฝ่าย"),
    "area_rules": ("match prep", "พื้นที่แข่ง", "ช่วงเตรียมตัว", "เตรียมตัว", "คนในพื้นที่", "โทรศัพท์", "แท็บเล็ต", "สมาร์ทวอทช์", "โน้ต", "เอกสาร", "หัวหน้าทีม", "น้ำดื่ม", "หมากฝรั่ง", "sealed", "อาหาร", "เครื่องดื่ม"),
    "bug_rule": ("บัค", "บั๊ก", "bug", "glitch", "challenge", "rollback", "round rollback", "damage", "ดาเมจ", "game-breaking", "game breaking", "exploit", "ช่องโหว่", "ได้เปรียบ", "ถือว่าผิด", "cypher", "ไซเฟอร์", "camera", "กล้อง"),
    "penalty": ("บทลงโทษ", "ลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "forfeit", "round loss", "map forfeit", "match forfeit", "warning", "ก่อกวน", "แกล้ง", "เล่นแทน", "ไม่ตรงตามที่ลงทะเบียน", "ออกจากเกม", "เยาะเย้ย", "ดูถูก", "มารยาท", "คำหยาบ", "ด่า", "สตรีม", "ไลฟ์", "stream", "toxic", "hate speech", "เหยียด", "เกลียดชัง", "match fixing", "cheating"),
    "policy": ("สงวนสิทธิ์", "เปลี่ยนแปลงกฎ", "แก้ไขกฎ", "ผู้จัด", "คำตัดสิน", "ข้อโต้แย้ง", "ตัดสิน", "เถียง", "ข้อยกเว้น"),
    "hero_rule": ("ฮีโร่", "hero", "global ban", "global ban/pick", "ban pick", "แบนเลือก", "รูน", "พลังเสริม", "ฮีโร่ซ้ำ", "เลือกฮีโร่", "เกมถัดไป", "ใช้ซ้ำ"),
    "break_time": ("พัก", "เวลาพัก", "พักกี่นาที", "เครื่องร้อน", "ไม่กลับ", "หายหลังพัก"),
    "match_process": ("match process", "match procedure", "กระบวนการแข่งขัน", "ห้อง", "หมายเลขห้อง", "กรรมการ", "รายงานผล", "post-match", "หลังแข่ง", "เกิดปัญหา", "แจ้งใคร", "บันทึกผล"),
}


COMPETITION_INTENT_FOCUS_TERMS = {
    "eligibility": ("รับเฉพาะ", "เปิดรับเฉพาะ", "นักศึกษา", "มหาวิทยาลัยสงขลานครินทร์", "วิทยาเขตภูเก็ต", "ภูเก็ต", "คนนอก", "คุณสมบัติ"),
    "registration": ("ไม่อนุญาต", "ลงทะเบียน", "ลงชื่อ", "ปิดรับสมัคร", "สมัคร", "เพิ่มชื่อ", "ผู้เล่น"),
    "roster_change": ("เปลี่ยนแปลงสมาชิก", "ไม่มีการเปลี่ยนแปลงสมาชิก", "เปลี่ยนสมาชิก", "เปลี่ยนตัว", "แทน", "roster", "ตลอดระยะเวลาการแข่งขัน", "ถอนตัว", "ตัดสิทธิ์", "ทีมเดียว"),
    "game_version": ("เวอร์ชัน", "เวอร์ชั่น", "ล่าสุด", "Steam", "แพลตฟอร์ม", "ดัดแปลง", "ตัวเกม"),
    "language": ("ภาษาทางการ", "ภาษาไทย", "การสื่อสาร", "การประท้วง", "รายงานผล"),
    "schedule_location": ("1 วัน", "แข่งขันทั้งหมด", "PSU Esports Studio", "Phuket", "ภูเก็ต", "สถานที่", "อาคาร", "5102A", "ห้อง"),
    "schedule": ("สายการแข่งขัน", "ประกาศล่วงหน้า", "ล่วงหน้า", "กำหนดการแข่งขัน", "รายงานตัว", "check in", "30 นาที", "แบ่งสาย", "รอบ 5 ทีม", "รอบรอง", "รอบชิง"),
    "communication": ("Discord", "สื่อสาร", "เซิร์ฟเวอร์", "server"),
    "game_setting": ("Competitive", "เงินเริ่มต้น", "Freeze", "ระเบิด", "รอบ", "ชนะ", "ต่อเวลา", "Overtime", "FT2", "R3", "3 รอบ", "60 วินาที", "Advantage", "Random", "Stage", "ด่าน", "สุ่ม", "Blood", "Bodies", "เลือด", "ศพ"),
    "side_selection": ("เลือกฝั่ง", "สีน้ำเงิน", "สีแดง", "ดวลมีด", "โยนเหรียญ", "ผู้ที่แพ้"),
    "area_rules": ("Match Prep", "ไม่เกิน 6", "โทรศัพท์", "แท็บเล็ต", "สมาร์ทวอทช์", "โน้ต", "เอกสาร", "หัวหน้าทีม", "น้ำดื่ม", "หมากฝรั่ง"),
    "bug_rule": ("บั๊ก", "บัค", "Bug", "Challenge", "Round Rollback", "ดาเมจ", "Game Breaking", "Game-Breaking", "Exploit", "ช่องโหว่", "ได้เปรียบ", "ถือว่าผิด", "Cypher", "ไซเฟอร์", "Camera", "กล้อง"),
    "penalty": ("บทลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "Warning", "Round Loss", "Map Forfeit", "Match Forfeit", "สตรีม", "คำหยาบ", "เกลียดชัง", "Match fixing", "Cheating"),
    "policy": ("สงวนสิทธิ์", "ผู้จัด", "คำตัดสิน", "เปลี่ยนแปลงแก้ไข", "ข้อโต้แย้ง"),
    "hero_rule": ("ฮีโร่", "Global Ban/Pick", "รูน", "พลังเสริม", "สกิน", "Default", "เลือกเล่นฮีโร่", "ฮีโร่ซ้ำ", "ใช้ซ้ำ", "เกมถัดไป"),
    "character": ("ตัวละคร", "DLC", "Customization", "Agent", "แผนที่ใหม่", "เอเจนท์ใหม่", "คอนเทนต์ใหม่"),
    "equipment": ("อุปกรณ์", "PlayStation", "PS5", "โทรศัพท์", "Tablet", "iPad", "คีย์บอร์ด", "เมาส์", "Headset", "Snap Tap", "SOCD", "มาโคร", "Macros", "ติดตั้งโปรแกรม", "install", "software", "Facebook", "Social media", "โซเชียล", "ปลั๊กพ่วง", "อุปกรณ์ชาร์จ"),
    "pause": ("Pause", "Timeout", "หยุดเกม", "เวลานอก", "Technical", "Emergency", "หลุดเกม", "ครั้ง", "นาที", "วินาที"),
    "late_start": ("มาสาย", "ล่าช้า", "เลท", "15 นาที", "สิบห้านาที", "ปรับแพ้", "ตัดสิทธิ์", "ยืนยัน"),
    "format": ("รูปแบบ", "Single Elimination", "BO3", "BO5", "Best of 3", "FT2", "1v1", "1 ต่อ 1", "ตัวต่อตัว", "5v5", "ชนะครบ 2", "เกมตัดสิน", "แพ้คัดออก", "ทุกรอบ"),
    "map_pool": ("แผนที่", "Map Pool", "MAPBAN.GG", "Mapban", "Ancient", "Anubis", "Dust 2", "Inferno", "Mirage", "Nuke", "Train", "Abyss", "Ascent", "Bind", "Corrode", "Haven", "Lotus", "Sunset"),
    "skin": ("สกิน", "Skin", "Default"),
    "rematch": ("Rematch", "Remake", "First Blood", "เริ่มใหม่", "ยินยอม"),
    "break_time": ("พัก", "5 นาที", "เครื่องร้อน", "ไม่กลับ", "หายหลังพัก"),
    "match_process": ("กระบวนการแข่งขัน", "หมายเลขห้อง", "กรรมการ", "รายงานผล", "บันทึกผล", "Post-Match", "ผู้จัดการแข่งขัน", "แจ้ง"),
}


def _has_any(q: str, *terms: str) -> bool:
    return any(normalize_text(term) in q for term in terms)


def _competition_game_hint(query: str) -> str | None:
    q = normalize_text(query)
    for game, aliases in COMPETITION_GAME_ALIASES.items():
        if any(alias in q for alias in aliases):
            return game
    return None


def _competition_intent_hint(query: str) -> str | None:
    q = normalize_text(query)
    game_hint = _competition_game_hint(query)

    if _has_any(q, "เวอร์ชัน", "เวอร์ชั่น", "version", "ล่าสุด", "steam", "แพลตฟอร์ม", "ดัดแปลง", "ตัวเกม", "mod"):
        return "game_version"
    if _has_any(q, "ภาษาทางการ", "ภาษาอะไร", "ภาษา", "ประท้วง", "รายงานผล"):
        return "language"
    if _has_any(q, "แข่งกี่วัน", "กี่วัน", "จัดที่ไหน", "แข่งที่ไหน", "สถานที่", "อาคาร", "ห้อง", "5102a", "psu esports studio", "วิทยาเขตภูเก็ต"):
        return "schedule_location"
    if _has_any(q, "เน็ตล่ม", "เน็ตทั้งโซน", "เซิร์ฟเวอร์พัง", "เซิร์ฟเวอร์ล่ม", "server", "เครือข่ายล่ม"):
        return "pause"
    if _has_any(q, "discord", "ช่องทางสื่อสาร", "ใช้ช่องทาง", "เซิร์ฟเวอร์", "server", "สื่อสารหลัก"):
        return "communication"
    if _has_any(q, "ปิดรับสมัคร", "หลังปิดรับสมัคร", "ลงทะเบียนเพิ่ม", "ลงทะเบียนผู้เล่น", "ลงทะเบียนไม่ครบ", "เพิ่มชื่อ", "ค่อยเพิ่ม", "รับสมัคร"):
        return "registration"
    if _has_any(q, "เปลี่ยนสมาชิก", "เปลี่ยนแปลงสมาชิก", "ถอนตัว", "เล่นให้สองทีม", "ทีมเดียว", "เปลี่ยนตัว", "แทน", "roster", "lineup", "หน้างาน", "ไม่ได้ลงชื่อ"):
        return "roster_change"
    if _has_any(q, "โทรศัพท์มือถือ", "มือถือ", "tablet", "ipad", "platform", "playstation", "ps5", "ใช้เครื่อง", "แข่งบน", "คีย์บอร์ด", "เมาส์", "crosshair", "resolution", "brightness", "macro", "script", "ติดตั้งโปรแกรม", "install", "software", "facebook", "โซเชียล", "social media", "snap tap", "socd", "ปลั๊กพ่วง", "อุปกรณ์ชาร์จ"):
        return "equipment"
    if _has_any(q, "ช้า", "ล่าช้า", "เลท", "เริ่ม match", "เริ่มแข่ง", "late start", "เกิน 15", "15 นาที", "สิบห้านาที", "มาสาย"):
        return "late_start"
    if _has_any(q, "รับเฉพาะ", "เฉพาะนักศึกษา", "คนนอก", "ลงแข่งได้ไหม", "คุณสมบัติ", "นักศึกษาแบบไหน"):
        return "eligibility"
    if _has_any(q, "สายการแข่งขัน", "ประกาศล่วงหน้า", "กำหนดการแข่งขัน", "วันแข่ง", "วันไหน", "ช่วงกี่โมง", "กี่โมง", "ลงทะเบียนช่วง", "check in", "check-in", "รายงานตัว", "รอบรองคู่", "แบ่งสาย", "รอบ 5 ทีม", "รอบชิงอันดับ", "รอบชิงชนะเลิศ", "ตาราง"):
        return "schedule"
    if _has_any(q, "competitive", "โหมด", "เงินเริ่มต้น", "freeze", "freeze time", "เวลาต่อรอบ", "ต่อรอบ", "ระเบิด", "ชนะกี่", "สูงสุดกี่", "ต่อเวลา", "overtime", "mr12", "r3", "3 rounds", "3 รอบ", "60 วินาที", "advantage", "stage", "random", "ด่าน", "สุ่ม", "assist", "blood", "bodies", "เลือด", "ศพ", "setting", "settings", "ตั้งค่า", "fps", "latency"):
        return "game_setting"
    if _has_any(q, "เลือกฝั่ง", "สีน้ำเงิน", "สีแดง", "ดวลมีด", "โยนเหรียญ", "แพ้เกมก่อนหน้า", "เกมแรก"):
        return "side_selection"
    if _has_any(q, "match prep", "พื้นที่แข่ง", "ช่วงเตรียมตัว", "เตรียมตัว", "คนในพื้นที่", "โทรศัพท์", "แท็บเล็ต", "สมาร์ทวอทช์", "โน้ต", "เอกสาร", "หัวหน้าทีม", "น้ำดื่ม", "หมากฝรั่ง", "sealed", "อาหาร", "เครื่องดื่ม"):
        return "area_rules"
    if _has_any(q, "บัค", "บั๊ก", "bug", "glitch", "challenge", "rollback", "round rollback", "damage", "ดาเมจ", "game-breaking", "game breaking", "exploit", "ช่องโหว่", "ได้เปรียบ", "ถือว่าผิด", "cypher", "ไซเฟอร์", "camera", "กล้อง", "kayo", "kay/o", "zero/point"):
        return "bug_rule"
    if _has_any(q, "บทลงโทษ", "ลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "forfeit", "round loss", "map forfeit", "match forfeit", "match fixing", "cheating", "warning", "ก่อกวน", "แกล้ง", "เล่นแทน", "ไม่ตรงตามที่ลงทะเบียน", "ออกจากเกม", "เยาะเย้ย", "ดูถูก", "มารยาท", "คำหยาบ", "ด่า", "สตรีม", "ไลฟ์", "stream", "toxic", "hate speech", "เหยียด", "เกลียดชัง"):
        return "penalty"
    if _has_any(q, "สงวนสิทธิ์", "เปลี่ยนแปลงกฎ", "แก้ไขกฎ", "ผู้จัด", "คำตัดสิน", "ข้อโต้แย้ง", "ตัดสิน", "เถียง", "ข้อยกเว้น"):
        return "policy"
    if _has_any(q, "global ban", "global ban/pick", "ban pick", "แบนเลือก", "รูน", "พลังเสริม", "ฮีโร่ซ้ำ", "เลือกฮีโร่", "เกมถัดไป", "ใช้ซ้ำ"):
        return "hero_rule"
    if _has_any(q, "พัก", "พักกี่นาที", "เวลาพัก", "เครื่องร้อน", "ไม่กลับ", "หายหลังพัก"):
        return "break_time"
    if _has_any(q, "กระบวนการแข่งขัน", "หมายเลขห้อง", "กรรมการ", "รายงานผล", "post-match", "หลังแข่ง", "เกิดปัญหา", "แจ้งใคร", "บันทึกผล"):
        return "match_process"
    if _has_any(q, "new map", "new agent", "restriction", "คอนเทนต์ใหม่", "agent ใหม่", "map ใหม่", "เอเจนท์ใหม่", "แผนที่ใหม่"):
        return "character"
    if _has_any(q, "เสมอกัน", "เสมอ", "1-1", "เกมตัดสิน"):
        return "format"
    if game_hint == "Tekken 8" and _has_any(q, "1v1", "1 ต่อ 1", "ตัวต่อตัว", "ft2", "round", "60 วินาที", "เล่นแบบไหน", "กติกาการแข่งขันสรุป", "รูปแบบ"):
        return "format"
    if _has_any(q, "กี่เกม", "เล่นกี่เกม", "แข่งกี่เกม", "ต้องเล่นกี่เกม", "ชนะกี่เกม", "กี่แมตช์", "กี่แมทช์", "กี่ตา", "bo อะไร", "best of", "bo3", "bo5"):
        return "format"
    if game_hint == "Arena of Valor (RoV)" and _has_any(q, "5v5", "ตัวสำรอง", "จำนวนผู้เล่น", "กี่คน", "ทีมละ", "สมาชิก"):
        return "team_size"
    if _has_any(q, "roster", "ตัวจริง", "ตัวสำรอง", "จำนวนผู้เล่น", "จำนวนคน", "กี่คน", "ครบ 4", "เหลือ 4", "ทีมละ", "สมาชิก", "แบบทีม", "ทีม 5", "5 คน", "team", "teams", "team size", "player", "players", "member", "members"):
        return "team_size"
    if game_hint == "Tekken 8" and _has_any(q, "offline", "ออฟไลน์"):
        return "format"
    if _has_any(q, "single elimination", "bo3", "bo5", "best of 3", "best-of-3", "รอบรอง", "รอบชิง", "แพ้คัดออก"):
        return "format"
    if _has_any(q, "emergency", "technical", "hardware", "เครื่องมีปัญหา", "จอยมีปัญหา", "หลุดเกม", "disconnect", "timeout", "pause", "หยุดเกม", "ขอหยุด", "กดหยุด", "กลางรอบ", "ยิงกัน"):
        return "pause"
    if _has_any(q, "มาสาย", "ล่าช้า", "เลท", "เริ่ม match", "เริ่มแข่ง", "late start", "เกิน 15", "15 นาที", "สิบห้านาที"):
        return "late_start"
    if _has_any(q, "โทรศัพท์มือถือ", "มือถือ", "tablet", "ipad", "platform", "playstation", "ps5", "ใช้เครื่อง", "แข่งบน", "คีย์บอร์ด", "เมาส์", "crosshair", "resolution", "brightness", "macro", "script", "ติดตั้งโปรแกรม", "install", "software", "facebook", "โซเชียล", "social media", "snap tap", "socd", "ปลั๊กพ่วง", "อุปกรณ์ชาร์จ"):
        return "equipment"
    if _has_any(q, *KNOWN_COMPETITION_MAPS):
        return "map_pool"

    best_intent: str | None = None
    best_score = 0
    for intent, aliases in COMPETITION_INTENT_ALIASES.items():
        score = sum(1 for alias in aliases if normalize_text(alias) in q)
        if score > best_score:
            best_intent = intent
            best_score = score
    return best_intent


def _competition_row_specific_boost(query: str, row: dict[str, Any]) -> float:
    q = normalize_text(query)
    row_id = normalize_text(str(row.get("id", "")))
    intent = str(row.get("intent", ""))
    score = 0.0

    if "cs2_format" in row_id and _has_any(q, "single elimination", "bo3", "best of 3", "best-of-3", "รอบรอง", "รอบชิง", "แพ้คัดออก", "bo อะไร"):
        score += 14.0
    if "cs2_team_size" in row_id and _has_any(q, "จำนวนผู้เล่น", "จำนวนคน", "กี่คน", "ทีมละ", "สมาชิก", "แบบทีม", "ทีม 5", "5 คน", "ผู้เล่น 5", "team", "teams", "team size", "player", "players", "member", "members"):
        score += 18.0
    if "cs2_format" in row_id and _has_any(q, "จำนวนผู้เล่น", "จำนวนคน", "กี่คน", "ทีมละ", "สมาชิก", "แบบทีม", "ทีม 5", "5 คน", "ผู้เล่น 5", "team", "teams", "team size", "player", "players", "member", "members"):
        score -= 10.0
    if "cs2_pause" in row_id and _has_any(q, "technical", "tactical", "timeout", "pause", "หยุดเกม", "เครื่องมีปัญหา", "กี่วินาที", "กี่ครั้ง"):
        score += 14.0

    if "valorant_emergency_pause" in row_id and _has_any(q, "emergency", "technical", "hardware", "เครื่องมีปัญหา", "หลุดเกม", "10 นาที"):
        score += 18.0
    if "valorant_tactical_timeout" in row_id and _has_any(q, "tactical", "timeout", "เวลานอก", "overtime", "ต่อแผนที่"):
        score += 14.0
    if "valorant_tactical_timeout" in row_id and _has_any(q, "emergency", "technical", "hardware", "เครื่องมีปัญหา"):
        score -= 10.0
    if "valorant_map_pool" in row_id and _has_any(q, "sunset", "abyss", "ascent", "bind", "corrode", "haven", "lotus", "map pool", "แผนที่"):
        score += 14.0
    if "valorant_agent_map_restriction" in row_id and _has_any(q, "new map", "new agent", "restriction", "agent ใหม่", "map ใหม่", "แผนที่ใหม่", "เอเจนท์ใหม่"):
        score += 16.0

    if "rov_team_size" in row_id and _has_any(q, "5v5", "ตัวสำรอง", "จำนวนผู้เล่น", "กี่คน", "ทีมละ", "team", "teams", "team size", "player", "players", "member", "members"):
        score += 16.0
    if "rov_format" in row_id and _has_any(q, "รูปแบบ", "bo3", "bo5", "best of 3", "best-of-3", "กี่เกม", "เล่นกี่เกม", "แข่งกี่เกม", "ต้องเล่นกี่เกม", "กี่แมตช์", "กี่แมทช์", "กี่ตา", "bo อะไร"):
        score += 20.0
    if intent in {"team_size", "pause", "late_start", "equipment", "skin", "rematch"} and _has_any(q, "กี่เกม", "เล่นกี่เกม", "แข่งกี่เกม", "ต้องเล่นกี่เกม", "กี่แมตช์", "กี่แมทช์", "กี่ตา", "bo อะไร"):
        score -= 10.0
    if "rov_late_start" in row_id and _has_any(q, "มาสาย", "ล่าช้า", "เริ่ม match", "เริ่มแข่ง", "เกิน 15", "15 นาที", "ปรับแพ้"):
        score += 16.0
    if "rov_pause" in row_id and _has_any(q, "หลุดเกม", "disconnect", "หยุด", "pause", "ขอหยุด"):
        score += 16.0
    if "rov_device" in row_id and _has_any(q, "โทรศัพท์มือถือ", "มือถือ", "tablet", "ipad", "อุปกรณ์", "ใช้เครื่อง"):
        score += 16.0

    if "tekken8_format" in row_id and _has_any(q, "1v1", "ft2", "round", "60 วินาที", "เล่นแบบไหน", "รูปแบบ", "กติกาการแข่งขันสรุป", "offline", "ออฟไลน์"):
        score += 16.0
    if "tekken8_format" in row_id and _has_any(q, "pause", "หยุดเกม", "กดหยุด", "ตั้งใจกด", "แพ้ 1 round", "แพ้ 1 Round"):
        score -= 18.0
    if "tekken8_equipment" in row_id and _has_any(q, "platform", "playstation", "ps5", "ใช้ playstation", "เล่นบน"):
        score += 16.0
    if "tekken8_pause" in row_id and _has_any(q, "pause", "หยุดเกม", "กดหยุด", "ตั้งใจกด", "ปรับแพ้", "แพ้ 1 round", "แพ้ 1 Round", "1 round"):
        score += 16.0
    if "tekken8_character" in row_id and _has_any(q, "dlc", "customization", "ตัวละคร"):
        score += 16.0

    if intent == "map_pool" and _has_any(q, "new map", "restriction"):
        score -= 8.0
    return score


def _tokens(text: str) -> set[str]:
    q = normalize_text(text)
    tokens = {tok for tok in re.split(r"[\s,./|()\[\]{}:;!?\"']+", q) if len(tok) >= 2}
    expanded = {tok for tok in tokens if tok not in STOPWORDS}
    thai_spans = re.findall(r"[\u0E00-\u0E7F]{3,}", q)
    for span in thai_spans:
        if len(span) > 40:
            continue
        for size in (2, 3, 4):
            for index in range(0, len(span) - size + 1):
                expanded.add(span[index:index + size])
    return expanded


def _game_entity_terms(text: str) -> set[str]:
    q = normalize_text(text)
    terms = {
        tok
        for tok in re.split(r"[\s,./|()\[\]{}:;!?\"']+", q)
        if len(tok) >= 3 and tok not in GAME_ENTITY_STOPWORDS
    }
    compact = q.replace(" ", "")
    if len(compact) >= 4:
        terms.add(compact)
    return terms


def _looks_like_game_detail_text(query: str) -> bool:
    q = normalize_text(query)
    return any(term in q for term in GAME_DETAIL_TERMS)


def _game_row_entity_match(query: str, row: dict[str, Any]) -> bool:
    q = normalize_text(query)
    query_terms = _game_entity_terms(query)
    candidates = [
        str(row.get("title", "")),
        str(row.get("game", "")),
        *[str(alias) for alias in row.get("aliases", []) if alias],
    ]
    for candidate in candidates:
        value = normalize_text(candidate)
        if not value:
            continue
        compact = value.replace(" ", "")
        if value in q or compact in q.replace(" ", ""):
            return True
        value_terms = _game_entity_terms(value)
        for term in query_terms:
            if term in value_terms:
                return True
            if len(term) >= 4 and (term in compact or term in value):
                return True
    return False


@lru_cache(maxsize=1)
def load_curated_rows() -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for path in sorted(CURATED_DIR.glob("*.jsonl")):
        if path.name == "rule_patterns.jsonl":
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                row["_source_file"] = path.name
                rows.append(row)
    return tuple(rows)


@lru_cache(maxsize=1)
def load_competition_fact_cards() -> tuple[dict[str, Any], ...]:
    fact_card_paths = sorted((ROOT / "data" / "competition_rules").glob(COMPETITION_FACT_CARD_GLOB))
    if not fact_card_paths:
        return ()
    rows: list[dict[str, Any]] = []
    for path in fact_card_paths:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                row["_source_file"] = path.name
                rows.append(row)
    return tuple(rows)


def retrieve_competition_fact_cards(query: str, limit: int = 3) -> tuple[list[dict[str, Any]], PipelineTrace]:
    query_tokens = _tokens(query)
    normalized_query = normalize_text(query)
    game_hint = _competition_game_hint(query)
    intent_hint = _competition_intent_hint(query)
    scored: list[tuple[float, dict[str, Any]]] = []

    for row in load_competition_fact_cards():
        if game_hint and row.get("game") != game_hint:
            continue

        patterns = [str(item) for item in row.get("question_patterns", [])]
        haystack = " ".join([
            str(row.get("id", "")),
            str(row.get("game", "")),
            str(row.get("tournament", "")),
            str(row.get("intent", "")),
            str(row.get("answer_type", "")),
            str(row.get("answer", "")),
            str(row.get("evidence", "")),
            " ".join(patterns),
            " ".join(str(tag) for tag in row.get("tags", [])),
        ])
        row_tokens = _tokens(haystack)
        overlap = len(query_tokens & row_tokens)
        score = float(overlap) + float(row.get("priority", 0)) / 100.0

        if game_hint and row.get("game") == game_hint:
            score += 8.0
        if intent_hint and row.get("intent") == intent_hint:
            score += 8.0
        elif intent_hint:
            score -= 3.0

        matched_pattern = False
        for pattern in patterns:
            normalized_pattern = normalize_text(pattern)
            if normalized_pattern and (normalized_pattern in normalized_query or normalized_query in normalized_pattern):
                score += 12.0
                matched_pattern = True
                break

        if (row.get("exact_only") or row.get("_source_file") == "competition_rule_fact_cards_round3_fixes.jsonl") and not matched_pattern:
            continue

        score += _competition_row_specific_boost(query, row)

        if not game_hint:
            score -= 4.0
        if score <= 0:
            continue
        scored.append((score, {**row, "_matched_pattern": matched_pattern}))

    scored.sort(key=lambda item: item[0], reverse=True)
    hits = [{**row, "_score": round(score, 3)} for score, row in scored[:limit]]
    confidence = min(0.95, 0.45 + (hits[0]["_score"] / 25 if hits else 0.0))
    detail = f"hits={len(hits)} game={game_hint or '-'} intent={intent_hint or '-'}"
    return hits, PipelineTrace("fact_card_retrieval", "competition_fact_cards", confidence, detail, {"category": "competition_rules", "game": game_hint, "intent": intent_hint})


def retrieve_curated(query: str, category: str | None = None, limit: int = 3) -> tuple[list[dict[str, Any]], PipelineTrace]:
    query_tokens = _tokens(query)
    normalized_query = normalize_text(query)
    competition_game = _competition_game_hint(query) if category == "competition_rules" else None
    competition_intent = _competition_intent_hint(query) if category == "competition_rules" else None
    focus_terms = COMPETITION_INTENT_FOCUS_TERMS.get(competition_intent or "", ())
    scored: list[tuple[float, dict[str, Any]]] = []
    for row in load_curated_rows():
        if category and category not in {"general", "unknown"} and row.get("category") != category:
            continue
        if competition_game and row.get("game") != competition_game:
            continue
        haystack = " ".join([
            str(row.get("title", "")),
            str(row.get("text", "")),
            " ".join(str(tag) for tag in row.get("tags", [])),
            str(row.get("category", "")),
        ])
        row_tokens = _tokens(haystack)
        overlap = len(query_tokens & row_tokens)
        if overlap <= 0:
            continue
        priority = float(row.get("priority", 0)) / 100.0
        score = overlap + priority
        if category == "competition_rules":
            haystack_norm = normalize_text(haystack)
            haystack_lower = haystack.lower()
            row_tags = {normalize_text(str(tag)) for tag in row.get("tags", [])}
            row_id = normalize_text(str(row.get("id", "")))
            if competition_intent:
                if competition_intent in row_tags or competition_intent in row_id:
                    score += 6.0
                focus_overlap = sum(
                    1
                    for term in focus_terms
                    if normalize_text(term) in normalized_query and normalize_text(term) in haystack_norm
                )
                score += min(10.0, focus_overlap * 2.5)
                if focus_terms and not any(normalize_text(term) in haystack_norm for term in focus_terms):
                    score -= 2.0
                if competition_intent != "penalty" and ("penalty" in row_tags or "บทลงโทษ" in haystack_norm or "ตารางบทลงโทษ" in haystack_norm):
                    score -= 8.0
                if competition_intent == "eligibility" and any(term in normalized_query for term in ("คนนอก", "ลงแข่ง", "ได้ไหม", "รับเฉพาะ")) and any(term in haystack_norm for term in ("เปิดรับเฉพาะ", "รับเฉพาะ", "คุณสมบัติทั่วไป")):
                    score += 14.0
                if competition_intent == "schedule_location" and "กี่วัน" in normalized_query and "1 วัน" in haystack_norm:
                    score += 12.0
                if competition_intent == "schedule_location" and any(term in normalized_query for term in ("ที่ไหน", "สถานที่", "แข่งที่ไหน")) and any(term in haystack_norm for term in ("psu esports studio", "phuket", "ภูเก็ต", "มหาวิทยาลัยสงขลานครินทร์")):
                    score += 10.0
                if competition_intent == "roster_change" and any(term in normalized_query for term in ("เปลี่ยนสมาชิก", "เปลี่ยนแปลงสมาชิก")) and any(term in haystack_norm for term in ("ไม่มีการเปลี่ยนแปลงสมาชิก", "เปลี่ยนแปลงสมาชิก")):
                    score += 14.0
                if competition_intent == "roster_change":
                    if "ถอนตัว" in normalized_query and any(term in haystack_norm for term in ("ถอนตัว", "ตัดสิทธิ์")):
                        score += 14.0
                    if any(term in normalized_query for term in ("สองทีม", "ทีมเดียว")) and "ทีมเดียว" in haystack_norm:
                        score += 28.0
                if competition_intent == "side_selection" and any(term in normalized_query for term in ("เลือกฝั่ง", "วิธีอะไร")) and any(term in haystack_norm for term in ("โยนเหรียญ", "ดวลมีด", "ผู้ที่แพ้")):
                    score += 10.0
                if competition_intent == "game_setting" and any(term in normalized_query for term in ("setting", "ตั้งค่า", "ปิด")) and any(term in haystack_norm for term in ("blood", "bodies", "เลือด", "ศพ", "fps", "latency")):
                    score += 12.0
                if competition_intent == "game_setting" and "โหมด" in normalized_query and any(term in haystack_norm for term in ("competitive", "5v5")):
                    score += 14.0
                if competition_intent == "game_setting" and any(term in normalized_query for term in ("ต่อรอบ", "freeze", "เวลาต่อรอบ")) and any(term in haystack_norm for term in ("1:55", "freeze", "15 วินาที")):
                    score += 14.0
                if competition_intent == "game_setting" and "overtime" in normalized_query and any(term in haystack_norm for term in ("overtime", "$10,000", "ฝั่งละ 3", "4 ใน 6")):
                    score += 14.0
                if competition_intent == "map_pool" and any(term in normalized_query for term in ("เลือกแผนที่ผ่าน", "ผ่านอะไร")) and any(term in haystack_norm for term in ("mapban", "mapban.gg")):
                    score += 14.0
                if competition_intent == "equipment":
                    if any(term in normalized_query for term in ("คีย์บอร์ด", "เมาส์")) and any(term in haystack_norm for term in ("คีย์บอร์ด", "เมาส์", "มาเองได้")):
                        score += 14.0
                    if any(term in normalized_query for term in ("crosshair", "resolution", "brightness")) and any(term in haystack_norm for term in ("crosshair", "resolution", "brightness")):
                        score += 14.0
                    if any(term in normalized_query for term in ("macro", "script", "มาโคร", "สคริปต์")) and any(term in haystack_norm for term in ("macro", "macros", "script", "มาโคร", "สคริปต์", "ห้าม")):
                        score += 14.0
                    if "ติดตั้งโปรแกรม" in normalized_query and "ติดตั้งโปรแกรม" in haystack_norm:
                        score += 14.0
                    if any(term in normalized_query for term in ("โซเชียล", "social media")) and any(term in haystack_norm for term in ("โซเชียล", "social media", "เว็บไซต์สื่อสาร")):
                        score += 14.0
                    if any(term in normalized_query for term in ("snap tap", "socd")) and any(term in haystack_norm for term in ("snap tap", "socd")):
                        score += 14.0
                    if any(term in normalized_query for term in ("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ")) and any(term in haystack_norm for term in ("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ")):
                        score += 14.0
                if competition_intent == "area_rules":
                    if any(term in normalized_query for term in ("เตรียมตัว", "คนในพื้นที่")) and any(term in haystack_norm for term in ("ไม่เกิน 6", "6 คน", "match prep")):
                        score += 14.0
                    if any(term in normalized_query for term in ("อาหาร", "เครื่องดื่ม")) and any(term in haystack_norm for term in ("น้ำดื่ม", "หมากฝรั่ง", "ปิดสนิท")):
                        score += 14.0
                if competition_intent == "pause":
                    if any(term in normalized_query for term in ("resume", "เกิน 1 นาที")) and "resume" in haystack_norm:
                        score += 14.0
                    if any(term in normalized_query for term in ("เน็ตล่ม", "เซิร์ฟเวอร์")) and any(term in haystack_norm for term in ("แจ้งทีมงาน", "เซิร์ฟเวอร์", "อินเตอร์เน็ตล่ม")):
                        score += 30.0
                    if any(term in normalized_query for term in ("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน", "ซอฟต์แวร์")) and any(term in haystack_norm for term in ("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน", "ซอฟต์แวร์", "technical")):
                        score += 12.0
                    if "3 ประเภท" in normalized_query and any(term in haystack_norm for term in ("tactical", "technical", "emergency")):
                        score += 12.0
                if competition_intent == "penalty":
                    if any(term in normalized_query for term in ("ก่อกวน", "เล่นแทน", "ไม่ตรงตามที่ลงทะเบียน", "ออกจากเกม", "เยาะเย้ย", "ดูถูก", "มารยาท")) and any(term in haystack_norm for term in ("ปรับแพ้", "ตัดสิทธิ์", "ปรับแพ้ทันที", "ไม่มีข้อยกเว้น")):
                        score += 14.0
                    if any(term in normalized_query for term in ("map forfeit", "match forfeit")) and any(term in haystack_norm for term in ("map forfeit", "match forfeit", "cheating", "match fixing", "ร้ายแรง", "ซ้ำ")):
                        score += 14.0
                if competition_intent == "format":
                    if any(term in normalized_query for term in ("เสมอกัน", "เกมตัดสิน")) and "เกมตัดสิน" in haystack_norm:
                        score += 14.0
                    if any(term in normalized_query for term in ("แข่งกี่เกม", "ถามว่าแข่งกี่เกม")) and any(term in haystack_norm for term in ("ชนะครบ 2", "ft2", "first to 2")):
                        score += 12.0
                if competition_intent == "character" and any(term in normalized_query for term in ("เอฟเฟกต์", "ออร่า")) and any(term in haystack_norm for term in ("เอฟเฟกต์", "ออร่า", "customization")):
                    score += 14.0
                if competition_intent == "match_process" and any(term in normalized_query for term in ("แจ้งใคร", "เกิดปัญหา", "บันทึกผล")) and any(term in haystack_norm for term in ("กรรมการ", "ผู้จัดการแข่งขัน", "แจ้ง", "บันทึกผล")):
                    score += 14.0
            if any(term in normalized_query for term in ("กี่คน", "ทีมละ", "ผู้เล่นกี่", "สมาชิก")) and re.search(r"\d+\s*คน", haystack_lower):
                score += 10.0
            if any(term in normalized_query for term in ("กี่คน", "ทีมละ", "ผู้เล่นกี่", "สมาชิก")) and "5v5" in haystack_lower:
                score += 10.0
            if any(term in normalized_query for term in ("timeout", "pause", "เวลานอก", "หยุดเกม")) and any(term in haystack_lower for term in ("timeout", "pause", "เวลานอก", "หยุดเกม")):
                score += 4.0
            if any(term in normalized_query for term in ("สกิน", "skin", "default")) and any(term in haystack_lower for term in ("สกิน", "skin", "default")):
                score += 4.0
            if any(term in normalized_query for term in ("เครื่อง", "อุปกรณ์", "ใช้อะไร")) and any(term in haystack_lower for term in ("playstation", "pc", "โทรศัพท์", "อุปกรณ์")):
                score += 3.0
            if any(term in normalized_query for term in ("ช้า", "ล่าช้า", "เกิน 15", "15 นาที", "มาสาย")) and any(term in haystack_lower for term in ("15 นาที", "ล่าช้า", "ปรับแพ้", "มาสาย")):
                score += 5.0
        scored.append((score, row))
    scored.sort(key=lambda item: item[0], reverse=True)
    hits = [{**row, "_score": round(score, 3)} for score, row in scored[:limit]]
    confidence = min(0.84, 0.45 + (hits[0]["_score"] / 10 if hits else 0.0))
    detail = f"hits={len(hits)}"
    if category == "competition_rules":
        detail += f" game={competition_game or '-'} intent={competition_intent or '-'}"
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent})


def hit_from_curated(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": row.get("id", "curated_hit"),
        "metadata": {
            "source_url": row.get("source_url", ""),
            "category": row.get("category", ""),
            "title": row.get("title", row.get("id", "curated_hit")),
            "source_ids": row.get("source_ids", [row.get("id", "curated_hit")]),
        },
    }


def hit_from_competition_fact_card(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": row.get("id", "competition_fact_card"),
        "metadata": {
            "source_url": row.get("source_url", ""),
            "category": "competition_rules",
            "title": row.get("id", "competition_fact_card"),
            "source_ids": row.get("source_ids", [row.get("id", "competition_fact_card")]),
            "game": row.get("game", ""),
            "intent": row.get("intent", ""),
            "answer_type": row.get("answer_type", ""),
        },
    }


def _clean_answer_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line not in lines:
            lines.append(line)
    return lines


def _lines_matching(lines: list[str], *terms: str) -> list[str]:
    matched: list[str] = []
    lowered_terms = tuple(term.lower() for term in terms)
    for line in lines:
        lower = line.lower()
        if any(term in lower for term in lowered_terms):
            matched.append(line)
    return matched


def _best_focus_lines(query: str, lines: list[str], intent: str | None, limit: int = 6) -> list[str]:
    if not intent:
        return []
    terms = COMPETITION_INTENT_FOCUS_TERMS.get(intent, ())
    if not terms:
        return []
    norm_query = normalize_text(query)
    query_tokens = _tokens(query)
    scored: list[tuple[float, str]] = []
    for line in lines:
        norm_line = normalize_text(line)
        if len(norm_line) < 4:
            continue
        score = 0.0
        for term in terms:
            norm_term = normalize_text(term)
            if norm_term in norm_line:
                score += 4.0 if norm_term in norm_query else 0.75
        shared = len(query_tokens & _tokens(line))
        score += min(4.0, float(shared) / 2.0)
        if any(term in norm_query for term in ("กี่คน", "ได้กี่คน", "ไม่เกินกี่คน")) and re.search(r"\d+\s*คน", line):
            score += 8.0
        if any(term in norm_query for term in ("กี่", "เท่าไหร่", "กี่ครั้ง", "กี่นาที", "กี่วินาที")) and re.search(r"\d+", line):
            score += 3.0
        if any(term in norm_query for term in ("ได้ไหม", "ได้หรือเปล่า", "ห้าม", "อนุญาต")) and any(term in norm_line for term in ("ห้าม", "ไม่อนุญาต", "อนุญาต", "ได้")):
            score += 4.0
        if intent == "eligibility" and any(term in norm_query for term in ("คนนอก", "รับเฉพาะ", "นักศึกษาแบบไหน", "ลงแข่ง")) and any(term in norm_line for term in ("เปิดรับเฉพาะ", "รับเฉพาะ", "นักศึกษา")):
            score += 10.0
        if intent == "schedule_location":
            if "กี่วัน" in norm_query and "1 วัน" in norm_line:
                score += 8.0
            if any(term in norm_query for term in ("ที่ไหน", "สถานที่", "แข่งที่ไหน")) and any(term in norm_line for term in ("psu esports studio", "phuket", "ภูเก็ต", "มหาวิทยาลัยสงขลานครินทร์")):
                score += 8.0
        if intent == "roster_change" and any(term in norm_query for term in ("เปลี่ยนสมาชิก", "เปลี่ยนแปลงสมาชิก")) and any(term in norm_line for term in ("ไม่มีการเปลี่ยนแปลงสมาชิก", "เปลี่ยนแปลงสมาชิก")):
            score += 10.0
        if intent == "roster_change":
            if "ถอนตัว" in norm_query and any(term in norm_line for term in ("ถอนตัว", "ตัดสิทธิ์")):
                score += 12.0
            if any(term in norm_query for term in ("สองทีม", "ทีมเดียว")) and "ทีมเดียว" in norm_line:
                score += 24.0
        if intent == "side_selection" and any(term in norm_query for term in ("วิธีอะไร", "เลือกฝั่ง")) and any(term in norm_line for term in ("โยนเหรียญ", "ดวลมีด", "ผู้ที่แพ้")):
            score += 8.0
        if intent == "schedule":
            if "วันไหน" in norm_query and any(term in norm_line for term in ("วันที่", "11 กันยายน", "2568", "2025")):
                score += 10.0
            if any(term in norm_query for term in ("กี่โมง", "ช่วงกี่โมง", "ลงทะเบียน")) and any(term in norm_line for term in ("ลงทะเบียน", "เวลา")):
                score += 8.0
        if intent == "game_setting":
            if "โหมด" in norm_query and any(term in norm_line for term in ("competitive", "5v5")):
                score += 12.0
            if any(term in norm_query for term in ("setting", "ตั้งค่า", "ปิด")) and any(term in norm_line for term in ("ปิด", "off", "blood", "bodies", "เลือด", "ศพ")):
                score += 12.0
            if any(term in norm_query for term in ("ต่อรอบ", "freeze", "เวลาต่อรอบ")) and any(term in norm_line for term in ("1:55", "freeze", "15 วินาที")):
                score += 12.0
            if "overtime" in norm_query and any(term in norm_line for term in ("overtime", "$10,000", "ฝั่งละ 3", "4 ใน 6")):
                score += 12.0
            if any(term in norm_line for term in ("บั๊ก", "bug", "challenge", "rollback", "ดาเมจ")) and not any(term in norm_query for term in ("บัค", "bug", "challenge", "rollback", "ดาเมจ")):
                score -= 6.0
        if intent == "equipment":
            if any(term in norm_query for term in ("คีย์บอร์ด", "เมาส์")) and any(term in norm_line for term in ("คีย์บอร์ด", "เมาส์")):
                score += 10.0
            if any(term in norm_query for term in ("crosshair", "resolution", "brightness")) and any(term in norm_line for term in ("crosshair", "resolution", "brightness")):
                score += 10.0
            if any(term in norm_query for term in ("macro", "script", "มาโคร", "สคริปต์")) and any(term in norm_line for term in ("macro", "macros", "script", "มาโคร", "สคริปต์", "ห้าม")):
                score += 12.0
            if "ติดตั้งโปรแกรม" in norm_query and any(term in norm_line for term in ("ติดตั้งโปรแกรม", "ห้าม")):
                score += 12.0
            if any(term in norm_query for term in ("โซเชียล", "social media")) and any(term in norm_line for term in ("โซเชียล", "social media", "เว็บไซต์สื่อสาร", "ห้าม")):
                score += 12.0
            if any(term in norm_query for term in ("snap tap", "socd")) and any(term in norm_line for term in ("snap tap", "socd", "อนุญาต", "permitted")):
                score += 12.0
            if any(term in norm_query for term in ("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ")) and any(term in norm_line for term in ("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ")):
                score += 12.0
        if intent == "area_rules":
            if any(term in norm_query for term in ("เตรียมตัว", "คนในพื้นที่")) and any(term in norm_line for term in ("ไม่เกิน 6", "6 คน", "match prep")):
                score += 12.0
            if any(term in norm_query for term in ("อาหาร", "เครื่องดื่ม")) and any(term in norm_line for term in ("น้ำดื่ม", "หมากฝรั่ง", "ปิดสนิท")):
                score += 12.0
        if intent == "pause":
            if any(term in norm_query for term in ("resume", "เกิน 1 นาที")) and "resume" in norm_line:
                score += 12.0
            if any(term in norm_query for term in ("เน็ตล่ม", "เซิร์ฟเวอร์")) and any(term in norm_line for term in ("แจ้งทีมงาน", "เซิร์ฟเวอร์", "อินเตอร์เน็ตล่ม")):
                score += 24.0
            if any(term in norm_query for term in ("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน", "ซอฟต์แวร์")) and any(term in norm_line for term in ("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน", "ซอฟต์แวร์", "technical")):
                score += 10.0
        if intent == "penalty" and any(term in norm_query for term in ("ก่อกวน", "เล่นแทน", "ไม่ตรงตามที่ลงทะเบียน", "ออกจากเกม", "เยาะเย้ย", "ดูถูก", "มารยาท", "map forfeit", "match forfeit")) and any(term in norm_line for term in ("ปรับแพ้", "ตัดสิทธิ์", "ปรับแพ้ทันที", "ไม่มีข้อยกเว้น", "map forfeit", "match forfeit", "cheating", "match fixing")):
            score += 12.0
        if intent == "format":
            if any(term in norm_query for term in ("เสมอกัน", "เกมตัดสิน")) and "เกมตัดสิน" in norm_line:
                score += 12.0
            if any(term in norm_query for term in ("แข่งกี่เกม", "ถามว่าแข่งกี่เกม")) and any(term in norm_line for term in ("ชนะครบ 2", "ft2", "first to 2")):
                score += 10.0
        if intent == "map_pool" and any(term in norm_query for term in ("เลือกแผนที่ผ่าน", "ผ่านอะไร")) and any(term in norm_line for term in ("mapban", "mapban.gg")):
            score += 12.0
        if intent == "match_process" and any(term in norm_query for term in ("แจ้งใคร", "เกิดปัญหา", "บันทึกผล")) and any(term in norm_line for term in ("กรรมการ", "ผู้จัดการแข่งขัน", "แจ้ง", "บันทึกผล")):
            score += 12.0
        if len(line) <= 28 and not re.search(r"\d", line) and not any(term in norm_line for term in ("ห้าม", "ไม่อนุญาต", "อนุญาต", "ได้", "ใช้", "คือ", "เป็น", "โยนเหรียญ", "ดวลมีด", "สูงสุด", "ต้อง")):
            score -= 3.0
        if re.fullmatch(r"\d+\.\s*[\u0E00-\u0E7FA-Za-z ()/-]{1,45}", line) and score < 4.0:
            score -= 2.0
        if score > 0:
            scored.append((score, line))
    scored.sort(key=lambda item: item[0], reverse=True)
    picked: list[str] = []
    for _, line in scored:
        if line not in picked:
            picked.append(line)
        if len(picked) >= limit:
            break
    return picked


def _fact_card_misses_specific_detail(query: str, row: dict[str, Any]) -> bool:
    q = normalize_text(query)
    blob = normalize_text(" ".join([
        str(row.get("answer", "")),
        str(row.get("evidence", "")),
        " ".join(str(tag) for tag in row.get("tags", [])),
    ]))
    checks = (
        (("ถอนตัว",), ("ถอนตัว", "ตัดสิทธิ์")),
        (("สองทีม", "ทีมเดียว"), ("ทีมเดียว",)),
        (("โหมด",), ("competitive", "5v5")),
        (("ต่อรอบ", "เวลาต่อรอบ", "freeze", "freeze time"), ("1:55", "freeze", "15 วินาที")),
        (("overtime", "ต่อเวลา"), ("overtime", "$10,000", "ฝั่งละ 3")),
        (("เลือกแผนที่ผ่าน", "ผ่านอะไร"), ("mapban", "mapban.gg")),
        (("กรรมการ", "แจ้งใคร"), ("กรรมการ", "เจ้าหน้าที่")),
        (("สตรีม",), ("สตรีม",)),
        (("เหยียด", "เกลียดชัง"), ("เกลียดชัง", "เหยียด")),
        (("คีย์บอร์ด", "เมาส์"), ("คีย์บอร์ด", "เมาส์")),
        (("crosshair", "resolution", "brightness"), ("crosshair", "resolution", "brightness")),
        (("macro", "script", "มาโคร", "สคริปต์"), ("macro", "macros", "script", "มาโคร", "สคริปต์")),
        (("ติดตั้งโปรแกรม",), ("ติดตั้งโปรแกรม",)),
        (("โซเชียล", "social media"), ("โซเชียล", "social media")),
        (("เตรียมตัว", "คนในพื้นที่"), ("ไม่เกิน 6", "6 คน")),
        (("อาหาร", "เครื่องดื่ม"), ("น้ำดื่ม", "หมากฝรั่ง", "ปิดสนิท")),
        (("รอบรองคู่ที่ 2",), ("12.30", "14.00")),
        (("เกมแรก", "สีน้ำเงิน"), ("สีน้ำเงิน", "ด้านบน")),
        (("resume", "เกิน 1 นาที"), ("resume",)),
        (("เน็ตล่ม", "เน็ตทั้งโซน", "เซิร์ฟเวอร์", "เซิร์ฟเกม"), ("แจ้งทีมงาน", "ดุลยพินิจ", "กรรมการ")),
        (("ก่อกวน",), ("ปรับแพ้", "ตัดสิทธิ์")),
        (("ไม่กลับมา", "ไม่กลับ", "หลังพัก"), ("ปรับ", "แพ้")),
        (("10 นาที",), ("10 นาที", "เริ่มเกมใหม่")),
        (("snap tap", "socd"), ("snap tap", "socd", "permitted", "อนุญาต")),
        (("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ"), ("ปลั๊กพ่วง", "อุปกรณ์ชาร์จ")),
        (("บันทึกผล",), ("บันทึกผล", "เจ้าหน้าที่")),
        (("3 ประเภท",), ("tactical", "technical", "emergency")),
        (("เว้นแต่", "สื่อสาร"), ("เว้นแต่", "สื่อสาร")),
        (("หมดสิทธิ์", "พักฉุกเฉิน", "emergency pause"), ("หมดสิทธิ์", "ตัวสำรอง")),
        (("map forfeit",), ("map forfeit", "ร้ายแรง", "ซ้ำ")),
        (("match forfeit",), ("match forfeit", "cheating", "match fixing")),
        (("เกมตัดสิน", "เสมอกัน"), ("เกมตัดสิน",)),
        (("stage",), ("stage", "random")),
        (("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน"), ("อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน")),
        (("ออกจากเกม",), ("ปรับแพ้ทันที",)),
        (("เยาะเย้ย", "ดูถูก", "มารยาท"), ("ปรับแพ้ทันที", "ไม่มีข้อยกเว้น")),
        (("เอฟเฟกต์", "ออร่า"), ("เอฟเฟกต์", "ออร่า")),
        (("ชนะครบ 2", "แข่งกี่เกม"), ("ชนะครบ 2", "ft2", "first to 2")),
    )
    for query_terms, required_terms in checks:
        if any(term in q for term in query_terms) and not any(term in blob for term in required_terms):
            return True
    return False


def _first_useful_line(text: str) -> str:
    for line in _clean_answer_lines(text):
        if len(line) > 4:
            return line
    return text.strip()


def _is_team_size_query(q: str) -> bool:
    return any(term in q for term in ("กี่คน", "ทีมละ", "ผู้เล่นกี่", "สมาชิก", "team", "teams", "team size", "player", "players", "member", "members"))


def _competition_answer_from_hits(query: str, hits: list[dict[str, Any]]) -> str | None:
    if not hits:
        return None

    q = normalize_text(query)
    intent_hint = _competition_intent_hint(query)
    best = hits[0]
    game = str(best.get("game", "การแข่งขัน")).strip() or "การแข่งขัน"
    tournament = str(best.get("tournament", "")).strip()
    source_url = str(best.get("source_url", "")).strip()

    candidate_lines: list[str] = []
    for row in hits[:3]:
        candidate_lines.extend(_clean_answer_lines(str(row.get("text", ""))))

    focus: list[str] = []
    answer_first = ""

    if intent_hint:
        focus = _best_focus_lines(query, candidate_lines, intent_hint)
        if focus:
            answer_first = focus[0]

    if answer_first:
        pass
    elif _is_team_size_query(q):
        focus = [
            line for line in candidate_lines
            if (
                (re.search(r"\d+\s*คน", line) and any(term in line for term in ("ผู้เล่น", "ทีม", "คน")))
                or "5v5" in line.lower()
            )
        ]
        if "Arena of Valor" in game and any("5v5" in line.lower() for line in focus):
            answer_first = "ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้"
        else:
            answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("timeout", "pause", "เวลานอก", "หยุดเกม", "technical")):
        focus = _lines_matching(candidate_lines, "timeout", "pause", "เวลานอก", "หยุดเกม", "technical", "ครั้ง", "วินาที", "นาที")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("สกิน", "skin", "default")):
        focus = _lines_matching(candidate_lines, "สกิน", "skin", "default")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("เครื่อง", "อุปกรณ์", "ใช้อะไร", "อุปกรณ์อะไร")):
        focus = _lines_matching(candidate_lines, "เครื่อง", "อุปกรณ์", "playstation", "pc", "โทรศัพท์", "keyboard", "mouse", "headset")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("แผนที่", "map", "map pool", "mapban")):
        joined = "\n".join(candidate_lines)
        found_maps = [name for name in KNOWN_COMPETITION_MAPS if re.search(rf"\b{re.escape(name)}\b", joined, flags=re.IGNORECASE)]
        focus = _lines_matching(candidate_lines, "map pool", "การเลือกแผนที่", "แผนที่ในการแข่งขัน", "แผนที่", "abyss", "ascent", "bind", "ancient", "mirage", "ban map")
        if found_maps:
            answer_first = f"แผนที่ที่ใช้แข่งมี {len(found_maps)} แผนที่ ได้แก่ {', '.join(found_maps)}"
            focus = [line for line in focus if "แผนที่ใหม่" not in line and "จำกัดห้ามใช้" not in line]
        else:
            answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("บทลงโทษ", "ลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "penalty", "forfeit")):
        focus = _lines_matching(candidate_lines, "บทลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "forfeit", "penalty", "warning")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("ช้า", "ล่าช้า", "เกิน 15", "15 นาที", "มาสาย")):
        focus = _lines_matching(candidate_lines, "15 นาที", "ล่าช้า", "ปรับแพ้", "มาสาย", "ไม่กลับมา")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("รูปแบบ", "bo3", "bo5", "ft2", "single elimination", "1v1", "5v5", "กี่เกม", "เล่นกี่เกม", "แข่งกี่เกม", "กี่แมตช์", "กี่แมทช์")):
        focus = _lines_matching(candidate_lines, "รูปแบบ", "bo3", "bo5", "ft2", "single elimination", "1v1", "5v5", "best of 3", "best-of-3", "ทุกรอบ")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    elif any(term in q for term in ("เช็คอิน", "รายงานตัว", "มาถึง", "ก่อนเวลา")):
        focus = _lines_matching(candidate_lines, "เช็คอิน", "รายงานตัว", "มาถึง", "ก่อนเวลา", "30 นาที")
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))
    else:
        focus = _clean_answer_lines(str(best.get("text", "")))[:5]
        answer_first = focus[0] if focus else _first_useful_line(str(best.get("text", "")))

    detail_lines = [line for line in focus if line != answer_first][:5]
    lines = [f"คำตอบ: {answer_first}"]
    if detail_lines:
        lines.append("")
        lines.append("รายละเอียดที่เกี่ยวข้อง:")
        lines.extend(f"- {line.lstrip('*-· ')}" for line in detail_lines)
    lines.append("")
    label = f"{game}"
    if tournament:
        label += f" / {tournament}"
    lines.append(f"อ้างอิงจากกติกา: {label}")
    if source_url:
        lines.append(f"แหล่งข้อมูล: {source_url}")
    return "\n".join(lines)


def answer_from_curated_hits(hits: list[dict[str, Any]], query: str = "") -> tuple[str | None, list[dict[str, Any]], float]:
    if not hits:
        return None, [], 0.0
    best = hits[0]
    score = float(best.get("_score", 0.0))
    category = str(best.get("category", ""))
    minimum_score = 3.0
    if category in {"events_news", "knowledge"}:
        minimum_score = 4.0
    if category == "games":
        if _looks_like_game_detail_text(query) and not _game_row_entity_match(query, best):
            return None, [], min(0.55, score / 10)
    if category == "games" and best.get("_source_file") == "game_item_details.jsonl":
        minimum_score = 2.5
    if score < minimum_score:
        return None, [], min(0.60, score / 5)
    if best.get("category") == "competition_rules":
        answer = _competition_answer_from_hits(query, hits) or str(best.get("text", "")).strip()
    else:
        answer = str(best.get("text", "")).strip()
    if not answer:
        return None, [], 0.0
    raw_hits = [hit_from_curated(row) for row in hits]
    confidence = min(0.84, 0.50 + score / 12)
    return answer, raw_hits, confidence


def answer_from_competition_fact_hits(hits: list[dict[str, Any]], query: str = "") -> tuple[str | None, list[dict[str, Any]], float]:
    if not hits:
        return None, [], 0.0

    best = hits[0]
    score = float(best.get("_score", 0.0))
    intent_hint = _competition_intent_hint(query)
    minimum_score = 10.0 if intent_hint else 14.0
    if score < minimum_score:
        return None, [], min(0.60, score / 20)
    best_intent = str(best.get("intent", "")).strip()
    matched_exact_pattern = bool(best.get("_matched_pattern"))
    if intent_hint and best_intent != intent_hint and not matched_exact_pattern:
        return None, [], min(0.60, score / 20)
    if _fact_card_misses_specific_detail(query, best):
        return None, [], min(0.60, score / 20)

    answer = str(best.get("answer", "")).strip()
    if not answer:
        return None, [], 0.0

    evidence = str(best.get("evidence", "")).strip()
    internal_evidence_markers = (
        "เพิ่มจาก",
        "audit",
        "regression",
        "repair",
        "Ground Truth",
        "Challenger",
    )
    if evidence and any(marker.lower() in evidence.lower() for marker in internal_evidence_markers):
        evidence = ""
    game = str(best.get("game", "การแข่งขัน")).strip() or "การแข่งขัน"
    tournament = str(best.get("tournament", "")).strip()
    source_url = str(best.get("source_url", "")).strip()
    answer_type = str(best.get("answer_type", "")).strip()

    lines = [f"คำตอบ: {answer}"]
    if evidence:
        lines.append("")
        lines.append("หลักฐานจากกติกา:")
        lines.append(f"- {evidence}")
    if answer_type == "inferred_fact":
        lines.append("")
        lines.append("หมายเหตุ: คำตอบนี้เป็นการสรุปจากข้อมูลที่มีในไฟล์กติกา ไม่ใช่ข้อมูล roster/ตัวสำรองที่ระบุเป็นตัวเลขแยกไว้")
    lines.append("")
    label = game
    if tournament:
        label += f" / {tournament}"
    lines.append(f"อ้างอิงจากกติกา: {label}")
    if source_url:
        lines.append(f"แหล่งข้อมูล: {source_url}")

    raw_hits = [hit_from_competition_fact_card(row) for row in hits[:1]]
    confidence = min(0.96, 0.72 + score / 40)
    return "\n".join(lines), raw_hits, confidence
