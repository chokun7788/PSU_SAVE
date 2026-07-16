from __future__ import annotations

import re

from app.pipeline.semantic_intent import match_semantic_intent
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, PreprocessedInput


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _looks_like_schedule_date_query(q: str) -> bool:
    has_date = _has(q, "วันนี้", "พรุ่งนี้", "มะรืน", "today", "ตอนนี้", "ขณะนี้", "เวลานี้", "วันหยุด", "เทศกาล", "หยุด", "ราชการ", "ปฏิทิน", "เดือนนี้", "เดือนหน้า", "เดือนที่แล้ว", "เดือนก่อน", "ปีนี้", "ปีหน้า", "ปีที่แล้ว", "ปีก่อน", "กรกฎาคม", "กรกฎา", "ก.ค.", "กค") or bool(re.search(r"\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b", q)) or bool(re.search(r"(?:อีก|หลังจากนี้)\s*\d{1,4}\s*(?:วัน|สัปดาห์|อาทิตย์)|\d{1,4}\s*วัน(?:ข้างหน้า|ถัดไป|ก่อน)|(?:ปี|พ\.ศ\.|พศ|ค\.ศ\.|คศ)?\s*\d{4}", q))
    has_schedule = _has(q, "เปิด", "ปิด", "เล่นได้", "ให้บริการ", "เวลา", "กี่โมง", "ช่วงไหน", "วันที่เท่าไหร่", "วันที่เท่าไร", "วันอะไร", "วันหยุดอะไร", "วันหยุดไทยไหม", "เทศกาล", "หยุดไหม", "หยุดบ้าง", "หยุดวันไหน", "เปิดไหม", "เปิดรึเปล่า", "เปิดหรือเปล่า", "กี่วัน", "กี่รายการ", "อะไรบ้าง")
    return has_date and has_schedule


def _looks_like_competition_rule_query(q: str) -> bool:
    if _has(q, "ปุ่ม", "กดปุ่ม", "กดอะไร", "ปุ่มอะไร", "button", "buttons", "controls", "controller"):
        return False
    game_terms = (
        "cs2", "counter-strike", "counter strike", "เคาเตอร์", "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "valo", "rov", "arena of valor",
        "aov", "เกมตีป้อม", "อาโอวี", "เอโอวี", "อาร์โอวี", "tekken", "tekken 8", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน", "blueket", "psu phuket cs2", "psu phuket valorant", "psu esports tekken",
    )
    rule_terms = (
        "กฎ", "กติกา", "รูปแบบ", "การแข่งขัน", "แข่ง", "ทัวร์", "tournament", "rule", "rules",
        "ทีม", "สมาชิก", "ผู้เล่น", "team", "teams", "team size", "player", "players", "member", "members", "bo3", "bo5", "ft2", "แผนที่", "map", "map pool", "mapban",
        "bo", "best of 3", "best-of-3", "รอบรอง", "รอบชิง", "แพ้คัดออก",
        "pause", "timeout", "หยุดเกม", "เวลานอก", "technical", "บัค", "บั๊ก", "bug", "glitch", "disconnect", "หลุดเกม",
        "single elimination", "format", "platform", "round", "1v1", "r3", "playstation 5", "ps5", "กี่ต่อกี่", "วินาที", "dust 2", "train", "ancient", "anubis",
        "บทลงโทษ", "ลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "อุปกรณ์", "สกิน", "skin",
        "บัญชี", "บัญชีส่วนตัว", "บัญชีที่จัดให้", "โปรแกรม", "โปรแกรมช่วยเล่น", "ช่วยเล่น", "ข้อห้าม",
        "ฮีโร่", "agent", "เอเจนท์", "ตัวละคร", "character", "dlc", "stage", "rematch", "remake", "first blood", "เช็คอิน", "checkin", "check in", "รายงานตัว",
        "tablet", "ipad", "customization", "ฝ่ายตรงข้าม", "ยินยอม", "เริ่มใหม่", "เล่นแบบไหน",
        "จำนวนผู้เล่น", "ตัวจริง", "ตัวสำรอง", "5v5", "มาสาย", "late start", "15 นาที", "เกมหลุด", "เริ่ม match", "กดหยุด", "โทรศัพท์มือถือ", "มือถือ",
        "รับเฉพาะ", "เฉพาะ", "คนนอก", "นักศึกษา", "ลงแข่ง", "สมัคร", "ปิดรับสมัคร", "ลงทะเบียน", "ได้ไหม", "ได้หรือเปล่า", "ห้าม", "อนุญาต", "โดนอะไร",
        "ใช้แพลตฟอร์ม", "แพลตฟอร์ม", "เวอร์ชัน", "เวอร์ชั่น", "steam", "ดัดแปลง", "ภาษา", "ประท้วง", "สถานที่", "จัดที่ไหน", "ที่ไหน", "กี่วัน",
        "บัญชี", "บัญชีส่วนตัว", "บัญชีที่จัดให้", "โปรแกรมช่วยเล่น", "ช่วยเล่น", "ข้อห้าม",
        "สื่อสาร", "discord", "check in", "check-in", "เปลี่ยนสมาชิก", "เปลี่ยนตัว", "แทน", "roster", "lineup", "ถอนตัว", "ทีมเดียว", "ประกาศล่วงหน้า", "ยืนยัน", "โหมด", "competitive", "เงินเริ่มต้น", "ระเบิด",
        "ชนะกี่", "สูงสุดกี่", "ต่อเวลา", "overtime", "เลือกฝั่ง", "ดวลมีด", "โยนเหรียญ", "สตรีม", "ไลฟ์", "live", "มาโคร", "macro", "script", "โปรแกรม",
        "โซเชียล", "facebook", "social media", "พื้นที่แข่ง", "match prep", "โน้ต", "เอกสาร", "หัวหน้าทีม", "น้ำดื่ม", "หมากฝรั่ง", "sealed", "แบ่งสาย", "รอบ 5 ทีม",
        "รอบชิงอันดับ", "รอบชิงชนะเลิศ", "hero", "global ban", "global ban/pick", "รูน", "พลังเสริม", "ฮีโร่ซ้ำ", "เครื่องร้อน", "พัก", "เน็ตล่ม",
        "เซิร์ฟเวอร์", "เซิร์ฟเวอร์พัง", "เซิร์ฟเกม", "เซิร์ฟเกมพัง", "เน็ตทั้งโซน", "challenge", "rollback", "round rollback", "round loss", "map forfeit", "match forfeit", "match fixing", "cheating", "hate speech", "เหยียด", "ศาสนา", "เชื้อชาติ", "เกลียดชัง", "ผิดไหม", "damage", "ดาเมจ", "ย้อนรอบ", "ได้เปรียบ", "ถือว่าผิด", "game breaking", "game-breaking", "exploit", "cypher", "ไซเฟอร์", "camera", "กล้อง", "kayo", "kay/o",
        "zero/point", "snap tap", "socd", "assist", "advantage", "random", "สุ่ม", "ด่าน", "blood", "bodies", "เลือด", "ศพ", "ft2", "r3", "เสมอกัน", "เสมอ", "1-1", "เกมตัดสิน", "ตัวต่อตัว", "1 ต่อ 1", "คำตัดสิน", "ข้อโต้แย้ง", "เถียง", "ผู้จัด",
        "ต่อรอบ", "เวลาต่อรอบ", "freeze", "freeze time", "mapban.gg", "mapban", "veto", "เหลือกี่", "เกมแรก", "สีน้ำเงิน", "สีแดง", "ช่วงเตรียมตัว", "เตรียมตัว",
        "คนในพื้นที่", "เกิดปัญหา", "แจ้งใคร", "จัดตรงไหน", "ตรงไหน", "มารยาท", "ข้อยกเว้น", "ออกจากเกม", "เล่นแทน", "ไม่ตรงตามที่ลงทะเบียน", "resume",
    )
    return _has(q, *game_terms) and _has(q, *rule_terms)


def _looks_like_competition_prize_query(q: str) -> bool:
    game_terms = (
        "cs2", "counter-strike", "counter strike", "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "rov", "arena of valor",
        "aov", "อาโอวี", "เอโอวี", "อาร์โอวี", "tekken", "tekken 8", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน",
    )
    prize_terms = (
        "รางวัล", "เงินรางวัล", "ชนะได้เงิน", "ได้เงินรางวัล", "ได้กี่บาท", "ได้เงินเท่าไหร่",
        "ได้เงินเท่าไร", "prize", "prize money", "reward",
    )
    return _has(q, *game_terms) and _has(q, "แข่ง", "แข่งขัน", "ทัวร์", "tournament") and _has(q, *prize_terms)


def _looks_like_student_fee_query(q: str) -> bool:
    student_terms = ("บัตรนักศึกษา", "นักศึกษา", "นักเรียน", "นิสิต", "student", "บัตร")
    fee_terms = ("ฟรี", "0 บาท", "ไม่เสียเงิน", "ต้องจ่ายไหม", "จ่ายไหม", "เสียเงินไหม", "ค่าใช้จ่าย", "ค่าบริการ")
    usage_terms = ("เล่น", "ใช้บริการ", "เข้าใช้", "จอง")
    return _has(q, *student_terms) and _has(q, *fee_terms) and _has(q, *usage_terms)


def _looks_like_general_knowledge_query(q: str) -> bool:
    cooking_terms = (
        "ทำอาหาร", "ทำกับข้าว", "ข้าวผัด", "อาหารผัด", "สูตร", "เมนู", "วัตถุดิบ",
        "ปรุง", "ทอด", "ต้ม", "ผัด", "แกง", "อบ", "หมัก", "ทำยังไงให้อร่อย",
    )
    explanation_terms = (
        "คืออะไร", "อธิบาย", "สอน", "วิธีทำ", "ทำยังไง", "ทำอย่างไร",
        "หลักการ", "แปลว่า", "ตัวอย่าง", "เปรียบเทียบ",
    )
    psu_terms = (
        "psu", "มอ", "ศูนย์", "esports", "studio", "จอง", "เช็คอิน", "เชคอิน",
        "ค่าบริการ", "ราคา", "โซน", "zone", "pc", "ps5", "playstation",
        "nintendo", "switch", "vr", "cockpit",
    )
    return _has(q, *explanation_terms) and _has(q, *cooking_terms) and not _has(q, *psu_terms)


def _looks_like_out_of_domain_query(q: str) -> bool:
    psu_terms = (
        "psu", "มอ", "สงขลานครินทร์", "esports", "studio", "ศูนย์", "ภูเก็ต",
        "จอง", "เช็คอิน", "เชคอิน", "ค่าบริการ", "โซน", "zone",
        "pc zone", "ps5", "playstation", "nintendo", "switch", "vr", "cockpit",
        "อุปกรณ์", "กติกา", "แข่งขัน", "สมาชิกทีม", "team", "member",
        "controller", "คอนโทรลเลอร์", "จอย", "ปุ่ม", "button",
    )
    game_terms = (
        "valorant", "rov", "aov", "cs2", "counter-strike", "counter strike",
        "tekken", "minecraft", "roblox", "fortnite", "warzone", "pubg",
        "league of legends", "mario", "overcooked", "beat saber", "gran turismo",
    )
    if _has(q, *psu_terms) or _has(q, *game_terms):
        return False

    out_terms = (
        "ฝน", "อากาศ", "พยากรณ์", "หุ้น", "ราคาทอง", "ทองวันนี้", "bitcoin", "บิตคอยน์",
        "ค่าเงิน", "usd", "thb", "ข่าวการเมือง", "นายกรัฐมนตรี", "การเมือง",
        "iphone", "ไอโฟน", "โน้ตบุ๊ก", "gmail", "facebook", "เฟซบุ๊ก", "instagram",
        "caption", "bio", "resume", "สัมภาษณ์งาน", "ขอลางาน", "สมัครงาน",
        "ลดน้ำหนัก", "ปวดหัว", "สุขภาพ", "ประกันสุขภาพ", "บัตรเครดิต", "ภาษี",
        "พาสปอร์ต", "สนามบิน", "ร้านอาหาร", "เที่ยว", "ญี่ปุ่น", "ตั๋วเครื่องบิน",
        "ฟุตบอล", "พรีเมียร์ลีก", "nba", "บอล", "ดาวอังคาร", "ระบบสุริยะ", "ทะเล",
        "คณิต", "สมการ", "แกรมมาร์", "แปล", "ภาษาอังกฤษ", "ภาษาญี่ปุ่น",
        "windows update", "คอมเปิดไม่ติด", "wi-fi", "wifi", "รหัสผ่าน", "โดนแฮก",
        "เพลงฮิต", "หนังน่าดู", "หนัง", "นิยาย", "กาแฟ", "ลาเต้", "อาหารเย็น",
        "ข้าวผัด", "วันเกิด", "คำอวยพร", "กลอน", "ร้านกาแฟ", "business model",
        "powerpoint", "infographic", "แบบสอบถาม", "portfolio", "data analyst",
        "machine learning", "deep learning", "prompt engineering", "docker", "git commit",
        "vercel", "neon", "sqlite", "postgres",
    )
    creative_or_help_terms = (
        "ช่วยเขียน", "ช่วยคิด", "ช่วยแต่ง", "ช่วยแปล", "ช่วยสรุป", "สอนทำ",
        "แนะนำ", "วิธี", "ทำไม", "คืออะไร", "ได้ไหม",
    )
    return _has(q, *out_terms) or (_has(q, *creative_or_help_terms) and not _has(q, *psu_terms))


def _looks_like_pc_available_query(q: str) -> bool:
    pc_terms = ("pc", "คอม", "คอมพิวเตอร์", "เครื่องคอม", "pc zone")
    available_terms = ("มี", "ให้เล่น", "เล่นได้", "ใช้ได้", "เข้าใช้", "เปิดให้เล่น")
    game_terms = (
        "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "cs2", "counter-strike", "counter strike", "pubg", "warzone",
        "league of legends", "lol", "tekken", "minecraft", "roblox",
    )
    return (
        _has(q, *pc_terms)
        and _has(q, *available_terms)
        and not _has(q, *game_terms)
        and not _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน")
    )


def _looks_like_zone_equipment_query(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "เสียกี่"):
        return False
    zone_terms = (
        "pc zone", "cockpit zone", "cockpit", "ค็อกพิท", "คอกพิท", "vr zone", "vr", "playstation", "ps5", "nintendo switch", "nintendo", "switch", "switch zone",
        "โซน", "zone",
    )
    equipment_terms = (
        "คืออะไร", "อะไรคือ", "มีอะไร", "ทำอะไร", "ใช้ทำอะไร", "เล่นอะไร", "เล่นยังไง", "เล่นอย่างไร",
        "วิธีเล่น", "วิธีใช้", "วิธีใช้งาน", "ใช้งานยังไง", "ใช้ยังไง", "สอนใช้", "เริ่มเล่น", "เปิดเครื่อง", "ยังไง", "อย่างไร",
        "อุปกรณ์", "เครื่อง", "กี่เครื่อง", "รุ่นอะไร", "สเป็ค", "สเปค", "spec", "specs",
        "ทีวี", "จอ", "พวงมาลัย", "แว่น",
    )
    return _has(q, *zone_terms) and _has(q, *equipment_terms)


def _looks_like_equipment_item_query(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "เสียกี่") and not _has(
        q,
        "ขนาด", "กี่นิ้ว", "นิ้ว", "ทีวี", "tv",
    ):
        return False
    item_terms = (
        "gaming pc", "msi mag infinite", "gaming monitor", "gaming keyboard", "gaming mouse", "gaming headset",
        "gaming chair", "logitech g923", "g923", "trueforce", "driving force shifter", "shifter",
        "racezone", "full cockpit", "cockpit v3", "pulse elite", "wireless headset",
        "nintendo switch oled", "switch oled", "playstation 5 slim", "ps5 slim",
        "sony playstation vr2", "playstation vr2", "ps vr2", "psvr2", "vr2",
        "tv", "tv 65", "tv 86", "sofa", "monitor", "keyboard", "mouse", "headset",
        "เมาส์", "เม้า", "เม้าส์", "คีย์บอร์ด", "แป้นพิมพ์", "หูฟัง", "เฮดเซ็ต", "เก้าอี้",
        "พวงมาลัย", "คันเกียร์", "เบาะขับรถ", "แว่น vr", "แว่นวีอาร์", "แว่น",
        "นินเทนโด", "สวิตช์", "สวิทช์", "เพลย์ห้า", "ทีวี", "ทีวี 65", "ทีวี 86", "โซฟา",
    )
    question_terms = (
        "คืออะไร", "อะไรคือ", "มีอะไร", "ทำอะไร", "ใช้ทำอะไร", "เล่นอะไร", "เล่นยังไง", "เล่นอย่างไร",
        "ใช้ยังไง", "ใช้อย่างไร", "วิธีเล่น", "วิธีใช้", "อุปกรณ์", "รุ่นอะไร",
        "โซนไหน", "อยู่ที่ไหน", "อยู่ไหน", "ขนาดเท่าไหร่", "ขนาดเท่าไร",
    )
    if _has(q, "zone", "โซน") and not _has(
        q,
        "g923", "trueforce", "shifter", "racezone", "pulse elite", "vr2", "psvr2",
        "playstation vr2", "แว่น", "oled", "slim", "เมาส์", "คีย์บอร์ด", "หูฟัง",
        "เก้าอี้", "พวงมาลัย", "คันเกียร์", "ทีวี", "tv",
    ):
        return False
    return _has(q, *item_terms) and _has(q, *question_terms)


def _looks_like_equipment_game_catalog_query(q: str) -> bool:
    if _has(
        q,
        "\u0e23\u0e32\u0e04\u0e32", "\u0e04\u0e48\u0e32\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23", "\u0e01\u0e35\u0e48\u0e1a\u0e32\u0e17", "\u0e40\u0e17\u0e48\u0e32\u0e44\u0e2b\u0e23\u0e48", "\u0e40\u0e2a\u0e35\u0e22\u0e40\u0e07\u0e34\u0e19",
    ):
        return False
    if _has(q, "\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c") and not _has(q, "\u0e40\u0e01\u0e21", "\u0e40\u0e25\u0e48\u0e19", "game", "games"):
        return False
    equipment_terms = (
        "\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c", "\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", "\u0e42\u0e0b\u0e19", "zone",
        "pc", "\u0e04\u0e2d\u0e21", "cockpit", "\u0e04\u0e47\u0e2d\u0e01\u0e1e\u0e34\u0e17", "\u0e04\u0e2d\u0e01\u0e1e\u0e34\u0e17", "\u0e1e\u0e27\u0e07\u0e21\u0e32\u0e25\u0e31\u0e22",
        "vr", "\u0e41\u0e27\u0e48\u0e19", "ps5", "playstation", "\u0e40\u0e1e\u0e25\u0e22\u0e4c", "nintendo", "switch", "\u0e19\u0e34\u0e19\u0e40\u0e17\u0e19\u0e42\u0e14", "\u0e2a\u0e27\u0e34\u0e15\u0e0a\u0e4c", "\u0e2a\u0e27\u0e34\u0e17\u0e0a\u0e4c",
    )
    game_list_terms = (
        "\u0e40\u0e25\u0e48\u0e19\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23", "\u0e40\u0e25\u0e48\u0e19\u0e40\u0e01\u0e21\u0e44\u0e23", "\u0e21\u0e35\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23", "\u0e21\u0e35\u0e40\u0e01\u0e21\u0e44\u0e23",
        "\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e01\u0e21\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e25\u0e48\u0e19\u0e2d\u0e30\u0e44\u0e23\u0e44\u0e14\u0e49\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e25\u0e48\u0e19\u0e44\u0e23\u0e44\u0e14\u0e49\u0e1a\u0e49\u0e32\u0e07",
        "\u0e40\u0e25\u0e48\u0e19\u0e2d\u0e30\u0e44\u0e23", "\u0e40\u0e25\u0e48\u0e19\u0e44\u0e23", "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e40\u0e25\u0e48\u0e19", "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e01\u0e21\u0e1a\u0e19", "\u0e40\u0e01\u0e21\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", "list game", "games",
    )
    return _has(q, *equipment_terms) and _has(q, *game_list_terms)


def _looks_like_competition_game_list_query(q: str) -> bool:
    if _has(q, "ประเภทเกม", "แนวเกม", "genre", "genres"):
        return False
    return _has(
        q,
        "เกมแข่งอะไรบ้าง", "เกมแข่งขันอะไรบ้าง", "เกมที่แข่ง", "มีเกมแข่ง", "มีเกมแข่งขัน",
        "รายการแข่งขันอะไรบ้าง", "รายการแข่งอะไรบ้าง", "รายการแข่งมีอะไรบ้าง", "รายการแข่งขันมีอะไรบ้าง", "แข่งเกมอะไร", "แข่งขันเกมอะไร",
        "ทัวร์นาเมนต์อะไรบ้าง", "tournament อะไรบ้าง",
    ) or (
        _has(q, "รายการแข่ง", "รายการแข่งขัน", "แข่ง", "แข่งขัน", "ทัวร์", "tournament")
        and (_has(q, "เกม") or _has(q, "รายการแข่ง", "รายการแข่งขัน"))
        and _has(q, "อะไรบ้าง", "เกมอะไร", "เกมไหน")
    )


def _looks_like_related_guidance_query(q: str) -> bool:
    if _has(
        q,
        "กติกา", "กฎ", "เข้าแข่ง", "ผู้เข้าแข่ง", "แมตช์", "match", "มาสาย", "ไม่ยืนยัน",
        "แบ่งสาย", "การแข่งขัน", "แข่งก่อน", "ตัดสิทธิ์", "ปรับแพ้", "โทษ", "ลงโทษ",
        "รอบ", "round", "map", "ทีม", "สมาชิก", "ตัวจริง", "ตัวสำรอง", "สมัคร",
        "ลงทะเบียน", "เช็คอิน", "checkin", "check in",
    ):
        return False
    guidance_terms = (
        "แนะนำ", "ควรเลือก", "เลือกอะไร", "เลือกโซน", "เหมาะกับ", "เหมาะไหม", "เหมาะมั้ย",
        "ต่างกันยังไง", "ต่างกันอย่างไร", "เปรียบเทียบ", "เทียบให้", "ไปกับเพื่อน",
        "มากับเพื่อน", "ไปกัน", "เล่นกับเพื่อน", "สาย", "แนว", "ควรเล่น", "โซนไหน",
        "มือใหม่", "มือไหม่", "เด็ก", "สำหรับเด็ก", "ครั้งแรก", "ไม่เคยเล่น",
    )
    domain_terms = (
        "ศูนย์", "โซน", "zone", "เกม", "เล่น", "เพื่อน", "นักเรียน", "นักศึกษา",
        "vr", "วีอาร์", "ps5", "เพลย์", "cockpit", "คอกพิท", "ค็อกพิท", "ขับรถ",
        "nintendo", "switch", "pc", "คอม", "beat saber", "gran turismo", "จังหวะ",
        "ขยับตัว", "ออกกำลัง", "ครอบครัว",
    )
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน"):
        return False
    return _has(q, *guidance_terms) and _has(q, *domain_terms)


def _looks_like_game_detail_query(q: str) -> bool:
    if _has(
        q,
        "กติกา", "กฎ", "ผู้เข้าแข่ง", "คนจะไปแข่ง", "แข่งจริง", "overtime", "map pool", "mapban",
        "bo3", "bo5", "รอบรอง", "รอบชิง", "กี่รอบ", "เวลาแข่ง", "เวลาการแข่งขัน", "pause", "timeout",
        "บทลงโทษ", "ลงโทษ", "ปรับแพ้",
    ):
        return False
    game_terms = (
        "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "cs2", "counter-strike", "counter strike", "pubg", "warzone", "league of legends",
        "lol", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน", "rov", "aov", "arena of valor", "อาโอวี", "เอโอวี", "อาร์โอวี", "spider-man", "spider man", "fortnite", "god of war", "beat saber", "horizon",
        "gran turismo", "gt7", "modern warfare", "mw3", "call of duty", "fc 24", "fifa", "เกมบอล", "final fantasy", "hogwarts", "resident evil",
        "naruto", "boruto", "last of us", "uncharted", "mario kart", "overcooked", "super smash", "smash bros",
        "switch sports", "animal crossing", "it takes two", "luigi", "mario party", "monster hunter",
        "moving out", "super mario", "ring fit", "zelda", "little nightmares",
    )
    detail_terms = (
        "คืออะไร", "อะไรคือ", "เกมอะไร", "แนวอะไร", "แนวไหน", "เป็นเกมแนวไหน", "เกี่ยวกับอะไร",
        "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "เล่นแบบไหน",
        "สอนเล่น", "สอนเล่นเกม", "สอนหน่อย", "เล่นยังไงดี", "เล่นเกมยังไง",
    )
    if _has(q, *game_terms) and _has(q, *detail_terms):
        return True
    if _has(q, *detail_terms):
        blocked = {
            "psu", "esports", "studio", "phuket", "pc", "vr", "ps5", "playstation",
            "nintendo", "switch", "game", "games", "zone",
        }
        for token in re.findall(r"\b[a-z][a-z0-9'’:-]{2,}\b", q):
            if token not in blocked:
                return True
    return False


def _looks_like_game_catalog_query(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "service fee"):
        return False
    if _has(
        q,
        "กติกา", "กฎ", "แข่ง", "แข่งขัน", "การแข่งขัน", "ลงแข่ง", "ทัวร์", "tournament",
        "ทีม", "สมาชิก", "ผู้เล่น", "ตัวจริง", "ตัวสำรอง", "ลงทะเบียน", "สมัคร",
    ):
        return False
    known_or_likely_games = (
        "minecraft", "roblox", "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "rov", "aov", "arena of valor", "อาโอวี", "เอโอวี", "อาร์โอวี", "cs2", "counter-strike", "counter strike", "pubg", "warzone",
        "league of legends", "lol", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน", "fortnite", "god of war", "spider", "spider-man", "mario",
        "มาริโอ", "overcooked", "super smash", "smash bros", "switch sports", "beat saber", "horizon", "gran turismo",
        "modern warfare", "mw3", "call of duty", "fifa", "เกมบอล", "animal crossing", "it takes two", "luigi", "mario party",
        "monster hunter", "moving out", "super mario", "ring fit", "pokemon", "zelda", "little nightmares",
        "resident evil", "เรสซิเดนต์", "final fantasy", "hogwarts", "naruto", "boruto", "last of us", "uncharted", "efootball", "fc 24",
    )
    if _has(q, *known_or_likely_games):
        return False
    catalog_terms = (
        "มีเกมอะไร", "มีเกมไร", "เกมอะไรบ้าง", "เกมไรบ้าง", "เกมอะไรให้เล่น",
        "เกมทั้งหมด", "รายชื่อเกม", "รายการเกม", "list game", "games",
        "มีอะไรให้เล่น", "เล่นเกมอะไรได้บ้าง", "เล่นเกมไรได้บ้าง",
        "เล่นอะไรได้บ้าง", "เล่นไรได้บ้าง",
    )
    return _has(q, *catalog_terms)


def _looks_like_game_availability_query(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "service fee"):
        return False
    if _has(q, "วันนี้", "พรุ่งนี้", "มะรืน", "วันจัน", "จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เวลา", "กี่โมง", "เปิด", "ปิด"):
        return False
    if _has(
        q,
        "กติกา", "กฎ", "แข่ง", "แข่งขัน", "การแข่งขัน", "ลงแข่ง", "ทัวร์", "tournament",
        "ทีม", "สมาชิก", "ผู้เล่น", "ตัวจริง", "ตัวสำรอง", "ลงทะเบียน", "สมัคร",
        "แผนที่", "map", "pause", "timeout", "technical", "บทลงโทษ", "ปรับแพ้",
        "ข้อห้าม", "อุปกรณ์", "โปรแกรม", "โปรแกรมช่วยเล่น", "บัญชี", "บัญชีส่วนตัว", "บัญชีที่จัดให้",
        "round", "rounds", "รอบ", "1 ต่อ 1", "1v1", "ft2", "r3", "decider", "เกมตัดสิน",
    ):
        return False
    play_terms = (
        "เล่นได้ไหม", "เล่นได้มั้ย", "เล่นได้รึเปล่า", "เล่นได้หรือเปล่า",
        "มีให้เล่นไหม", "มีให้เล่นมั้ย", "มีเกม", "เกมอะไร", "list game",
        "อยากเล่น", "อยากลองเล่น", "จะเล่น", "ขอเล่น",
    )
    known_or_likely_games = (
        "minecraft", "roblox", "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "rov", "aov", "arena of valor", "อาโอวี", "เอโอวี", "อาร์โอวี", "cs2", "counter-strike", "counter strike", "pubg", "warzone",
        "league of legends", "lol", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน", "fortnite", "god of war", "spider", "spider-man", "mario",
        "มาริโอ", "overcooked", "super smash", "smash bros", "switch sports", "beat saber", "horizon", "gran turismo",
        "modern warfare", "mw3", "call of duty", "fifa", "เกมบอล", "animal crossing", "it takes two", "luigi", "mario party",
        "monster hunter", "moving out", "super mario", "ring fit", "pokemon", "zelda", "little nightmares",
        "resident evil", "เรสซิเดนต์", "final fantasy", "hogwarts", "naruto", "boruto", "last of us", "uncharted", "efootball", "fc 24",
    )
    has_play_question = _has(q, *play_terms) or (_has(q, "เล่น") and _has(q, "ได้ไหม", "ได้มั้ย", "ได้รึเปล่า", "ได้หรือเปล่า", "มีไหม", "มีมั้ย"))
    has_known_or_named_game = _has(q, *known_or_likely_games) or re.search(r"\b[a-z][a-z0-9'’:-]{2,}\b", q)
    has_presence_question = _has(q, "มี") and _has(q, "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "ปะ")
    has_location_question = _has(q, "อยู่เครื่อง", "อยู่โซน", "เครื่องไหน", "โซนไหน", "zone ไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน", "อยู่ที่ไหน")
    if has_known_or_named_game and (has_play_question or has_presence_question or has_location_question):
        return True
    return False


def route_intent(pre: PreprocessedInput, entities: EntityBundle) -> tuple[PipelineRoute, PipelineTrace]:
    q = pre.normalized_query
    semantic_match = match_semantic_intent(q)

    # Put specific/high-risk intents before broad terms such as "เวลา", "อุปกรณ์", or game names.
    if _looks_like_out_of_domain_query(q) or _looks_like_general_knowledge_query(q):
        route = PipelineRoute("general", "general_knowledge_query", 0.86, "general", "low", "general knowledge terms found without PSU domain")
    elif _has(q, "ชำระ", "จ่ายภายใน", "โอนเงิน", "สลิป", "เลขบัญชี", "ธนาคาร", "ไม่จ่าย", "ลืมจ่าย", "payment timeout", "หลังจองต้องจ่าย", "จ่ายภายในกี่นาที", "จ่ายเงินผ่านบัญชี"):
        route = PipelineRoute("reservation", "payment_policy", 0.93, "fact", "medium", "payment terms found")
    elif _has(q, "จองผิด", "แก้เวลา", "แก้ไข", "ยกเลิก", "จองใหม่", "booking", "จอง", "book", "ล่วงหน้า", "กรอกข้อมูล", "เลือกอะไร", "ก่อนเข้าใช้บริการ", "เข้าใช้บริการต้องทำอะไร"):
        route = PipelineRoute("reservation", "booking_policy", 0.92, "fact", "medium", "reservation/edit terms found")
    elif _looks_like_equipment_item_query(q):
        route = PipelineRoute("equipment", "equipment_item_lookup", 0.96, "fact", "low", "specific equipment item terms found")
    elif _looks_like_equipment_game_catalog_query(q):
        route = PipelineRoute("equipment", "equipment_game_catalog", 0.96, "list", "low", "equipment game catalog terms found")
    elif _looks_like_student_fee_query(q):
        route = PipelineRoute("service_fee", "service_fee_query", 0.96, "fact", "medium", "student/free service fee terms found")
    elif _looks_like_pc_available_query(q):
        route = PipelineRoute("equipment", "pc_availability", 0.95, "fact", "low", "PC availability terms found")
    elif _has(q, "25 เมษายน", "25 เม.ย.", "25 april", "25 apr"):
        route = PipelineRoute("events_news", "news_lookup", 0.91, "fact", "medium", "specific news date terms found")
    elif _looks_like_competition_game_list_query(q):
        route = PipelineRoute("games", "competition_game_list", 0.95, "list", "medium", "competition game list terms found")
    elif _looks_like_game_availability_query(q):
        route = PipelineRoute("games", "game_availability_lookup", 0.94, "fact", "low", "game availability terms found")
    elif _looks_like_game_detail_query(q):
        route = PipelineRoute("games", "game_detail_lookup", 0.95, "fact", "low", "specific game detail terms found")
    elif _looks_like_schedule_date_query(q):
        route = PipelineRoute("schedule", "schedule_query", 0.96, "fact", "medium", "date/opening schedule terms found")
    elif _looks_like_related_guidance_query(q):
        route = PipelineRoute("equipment", "related_guidance", 0.90, "summary", "medium", "related guidance terms found")
    elif _looks_like_game_catalog_query(q):
        route = PipelineRoute("games", "game_catalog_lookup", 0.95, "list", "low", "game catalog list terms found")
    elif _looks_like_zone_equipment_query(q):
        route = PipelineRoute("equipment", "zone_equipment_lookup", 0.94, "fact", "low", "zone/equipment terms found")
    elif _looks_like_competition_prize_query(q):
        route = PipelineRoute("no_answer", "competition_prize_unknown", 0.94, "no_answer", "medium", "competition prize terms found but no verified prize data")
    elif _looks_like_competition_rule_query(q):
        route = PipelineRoute("competition_rules", "competition_rules_lookup", 0.94, "fact", "medium", "competition rule terms found")
    elif semantic_match is not None:
        route = PipelineRoute(
            semantic_match.category,
            semantic_match.intent_id,
            semantic_match.confidence,
            semantic_match.answer_type,
            semantic_match.risk,
            semantic_match.reason,
        )
    elif _has(q, "คอมพัง", "คอมพิวเตอร์พัง", "จอแตก", "เมาส์พัง", "เมาส์เสีย", "คีย์บอร์ดพัง", "จอยพัง", "หูฟังพัง", "อุปกรณ์พัง", "อุปกรณ์เสีย", "mouse พัง", "keyboard พัง", "เสียหาย", "ค่าปรับ", "ชดเชย", "เต็มจำนวน", "แบน", "ระงับสิทธิ์", "อุทธรณ์"):
        route = PipelineRoute("penalty", "penalty_policy", 0.94, "fact", "high", "damage/penalty terms found")
    elif _has(q, "เช็คอิน", "เชคอิน", "checkin", "check in"):
        route = PipelineRoute("reservation", "checkin_policy", 0.94, "fact", "medium", "checkin terms found")
    elif _has(q, "อีเมล", "email", "facebook", "เฟส", "เบอร์", "โทร", "เบอร์ติดต่อ", "ติดต่อ", "ที่ตั้ง", "อยู่ที่ไหน", "อยู่ตรงไหน", "ตรงไหน"):
        route = PipelineRoute("contact", "contact_lookup", 0.92, "fact", "low", "contact terms found")
    elif _has(q, "ชำระ", "จ่ายภายใน", "โอนเงิน", "สลิป", "เลขบัญชี", "ธนาคาร", "ไม่จ่าย", "ลืมจ่าย", "payment timeout", "หลังจองต้องจ่าย", "จ่ายภายในกี่นาที"):
        route = PipelineRoute("reservation", "payment_policy", 0.93, "fact", "medium", "payment terms found")
    elif _has(q, "รอยขีดข่วน", "เบาะขาด", "ปุ่มหลวม", "สายขาด", "โครงเฟอร์นิเจอร์", "ฝาปิดหลุด", "คราบน้ำ", "รอยเปื้อน", "ปรับเท่าไหร่", "โดนปรับ", "ค่าซ่อม"):
        route = PipelineRoute("penalty", "penalty_policy", 0.93, "fact", "high", "damage/penalty terms found")
    elif entities.price_intent or (entities.service and _has(q, "แพงกว่า", "ต่างกัน", "ต้องจ่าย", "ฟรีไหม", "ค่าใช้จ่าย", "คำนวณ", "คิดเงิน")):
        route = PipelineRoute("service_fee", "service_fee_query", 0.95, "calculation" if entities.comparison_intent else "fact", "medium", "price/service entity found")
    elif _has(q, "จองผิด", "แก้เวลา", "แก้ไข", "ยกเลิก", "จองใหม่", "booking", "จอง", "book", "ล่วงหน้า"):
        route = PipelineRoute("reservation", "booking_policy", 0.90, "fact", "medium", "reservation/edit terms found")
    elif _has(q, "ชำระ", "จ่ายภายใน", "โอนเงิน", "สลิป", "เลขบัญชี", "ธนาคาร", "ไม่จ่าย", "ลืมจ่าย", "payment timeout"):
        route = PipelineRoute("reservation", "payment_policy", 0.92, "fact", "medium", "payment terms found")
    elif _has(q, "ของหาย", "อุปกรณ์เปียก", "ย้ายอุปกรณ์", "เคลื่อนย้ายอุปกรณ์", "แผ่นเกม", "ไม่คืน", "สูบบุหรี่", "แอลกอฮอล์", "มีด", "พนัน", "ปลั๊ก", "เสียงดัง", "เสียดสี", "ทิ้งขยะ", "ฝากสัมภาระ", "ฝากกระเป๋า", "ขนม", "กินน้ำ", "อาหาร", "เครื่องดื่ม", "พบปัญหา", "ปัญหาเครื่อง", "เอาอาหารเข้า", "นำอาหารเข้า"):
        route = PipelineRoute("rules", "studio_rules", 0.93, "fact", "medium", "specific rules terms found")
    elif _has(q, "ข่าว", "กิจกรรม", "การแข่งขัน", "แข่ง", "จัดวัน", "จัดให้ใคร", "2569", "2026", "game on", "valorant 2026", "cs 2 2026", "25 เมษายน", "21 กุมภาพันธ์", "surat smash", "ตัวแทน", "นักศึกษาชาวจีน") and not _has(q, "วันเกิด", "birthday", "ปาร์ตี้", "party", "วันหยุด", "เทศกาล", "ปฏิทิน", "ราชการ", "เดือนนี้", "เดือนหน้า", "เดือนที่แล้ว", "ปีนี้", "ปีหน้า", "ปีที่แล้ว", "กี่วัน", "ประเภทเกม", "แนวเกม"):
        route = PipelineRoute("events_news", "news_lookup", 0.86, "summary", "medium", "news/event terms found")
    elif _has(
        q,
        "member", "members", "สมาชิก", "สมาชิกทีม", "ทีมงาน", "บุคลากร", "ตำแหน่ง",
        "อธิการบดี", "รองอธิการบดี", "คณบดี", "ผู้ช่วยอธิการบดี", "ผู้จัดการ", "ผู้จัดการศูนย์",
        "นักวิชาการคอมพิวเตอร์", "สหกิจ", "ฝึกงาน", "internship", "intern", "cooperative",
        "psu phuket esports club", "esports club", "ชมรม", "ประธาน psu", "ประธานชมรม",
        "รองประธาน", "เลขานุการ", "เหรัญญิก", "ประชาสัมพันธ์", "กรรมการ", "gallery",
    ):
        route = PipelineRoute("overview", "members_lookup", 0.88, "fact", "low", "members/gallery terms found")
    elif _has(q, "อีสปอร์ตคือ", "esports", "moba", "multiplayer online battle arena", "เกมตีป้อม", "ประเภทเกม", "แนวเกม", "เกมยอดนิยม", "เกมที่นิยม", "เกมนิยม", "อาชีพ", "spacewar", "ประวัติ", "เริ่มครั้งแรก") or (_has(q, "ฝึก", "ทักษะ") and _has(q, "overcooked", "mario kart")):
        route = PipelineRoute("knowledge", "knowledge_lookup", 0.88, "summary", "low", "knowledge terms found")
    elif _has(q, "เปิด", "ปิด", "เล่นได้", "เล่นกี่โมง", "กี่โมง", "ช่วงไหน", "เวลา", "service hours", "opening", "closing", "morning", "afternoon", "รอบเช้า", "ช่วงเช้า", "รอบบ่าย", "ช่วงบ่าย", "24 ชั่วโมง", "24 ชม", "maintenance", "ศุกร์", "friday", "fri", "จันทร์", "วันจัน", "monday", "mon", "อังคาร", "tuesday", "tue", "พุธ", "wednesday", "wed", "พฤหัส", "พฤหัสบดี", "thursday", "thu", "วันนี้", "พรุ่งนี้", "มะรืน", "today", "วันหยุด", "เทศกาล", "หยุด", "หยุดบ้าง", "หยุดวันไหน", "ราชการ", "ปฏิทิน", "เดือนนี้", "เดือนหน้า", "เดือนที่แล้ว", "เดือนก่อน", "ปีนี้", "ปีหน้า", "ปีที่แล้ว", "ปีก่อน", "กรกฎาคม", "กรกฎา", "ก.ค.", "กค", "ตรวจอุปกรณ์", "ทำความสะอาด", "cleaning", "hardware inspection") or re.search(r"(?:อีก|หลังจากนี้)\s*\d{1,4}\s*(?:วัน|สัปดาห์|อาทิตย์)|\d{1,4}\s*วัน(?:ข้างหน้า|ถัดไป|ก่อน)", q):
        route = PipelineRoute("schedule", "schedule_query", 0.95, "fact", "medium", "schedule terms found")
    elif _has(q, "เกม", "valorant", "วาโล", "วาโลแรนท์", "วาโลแรน", "rov", "aov", "อาโอวี", "เอโอวี", "อาร์โอวี", "cs2", "pubg", "warzone", "minecraft", "roblox", "mario", "overcooked", "gran turismo", "beat saber", "tekken", "เทคเคน", "เทคเคน8", "เพลย์ห้า", "spider", "spider-man", "fortnite", "god of war", "super smash", "smash bros", "switch sports", "pc games", "horizon", "modern warfare", "mw3", "call of duty", "fc 24", "fifa", "final fantasy", "hogwarts", "resident evil", "naruto", "boruto", "last of us", "uncharted", "animal crossing", "it takes two", "luigi", "mario party", "monster hunter", "moving out", "super mario", "ring fit", "zelda", "little nightmares"):
        route = PipelineRoute("games", "games_lookup", 0.88, "list", "low", "game terms found")
    elif _has(q, "กฎ", "ห้าม", "อาหาร", "อาวุธ", "ขยะ", "สัมภาระ"):
        route = PipelineRoute("rules", "studio_rules", 0.88, "fact", "medium", "rules terms found")
    elif _has(q, "อุปกรณ์", "โซน", "zone", "กี่เครื่อง", "รุ่นอะไร", "สเป็ค", "สเปค", "spec", "specs", "cpu", "gpu", "การ์ดจอ", "แรม", "ram", "ทีวี", "จออะไร", "monitor", "เก้าอี้", "เมาส์", "หูฟัง"):
        route = PipelineRoute("equipment", "equipment_lookup", 0.88, "list", "low", "equipment terms found")
    elif _has(q, "อีเมล", "email", "facebook", "เฟส", "เบอร์", "โทร", "ที่ตั้ง", "อยู่ที่ไหน", "อยู่ตรงไหน", "ตรงไหน"):
        route = PipelineRoute("contact", "contact_lookup", 0.90, "fact", "low", "contact terms found")
    elif _has(q, "ศูนย์นี้", "คืออะไร", "mission", "ก่อตั้ง", "หน่วยงาน"):
        route = PipelineRoute("overview", "overview_lookup", 0.78, "summary", "low", "overview terms found")
    else:
        route = PipelineRoute("general", "unknown_domain_query", 0.55, "fact", "medium", "domain query but no strong category")

    trace_stage = "semantic_intent_router" if semantic_match is not None and route.intent == semantic_match.intent_id else "router"
    metadata = {"intent": route.intent, "answer_type": route.answer_type}
    if trace_stage == "semantic_intent_router":
        metadata.update(semantic_match.metadata)
        metadata["matched_example"] = semantic_match.matched_example
        metadata["margin"] = semantic_match.margin
    return route, PipelineTrace(trace_stage, route.category, route.confidence, route.reason, metadata)
