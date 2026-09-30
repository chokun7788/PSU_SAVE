from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.core.normalization import KEYBOARD_EN_TO_THAI, KEYBOARD_THAI_TO_EN  # noqa: E402


SOURCE_PATH = ROOT / "data" / "eval" / "model_benchmark_1500.jsonl"
OUT_JSONL = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.jsonl"
OUT_CSV = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.csv"
OUT_SUMMARY = ROOT / "data" / "eval" / "keyboard_input_anomaly_ground_truth_500_20260830.summary.json"


TARGET_COUNTS = {
    "layout_th_to_en_full": 90,
    "layout_th_to_en_token": 45,
    "layout_th_to_en_suffix": 20,
    "layout_en_to_th_full": 25,
    "repeat_thai_internal": 60,
    "repeat_thai_mark_or_vowel": 40,
    "repeat_latin_internal": 25,
    "repeat_short_token": 15,
    "combined_layout_and_repeat": 60,
    "valid_normal": 50,
    "valid_protected_or_mixed": 30,
    "valid_expressive_repetition": 20,
    "valid_lexical_double": 20,
}


GROUP_ORDER = (
    "service_fee",
    "games",
    "availability_game",
    "game_controls",
    "equipment",
    "schedule",
    "reservation",
    "competition_rules",
    "members",
    "compound",
    "availability_service",
    "game_detail",
    "policy_schedule_rules",
    "ambiguity_no_answer",
    "ambiguous_controls",
    "availability_machine_split",
    "general_llm",
)


THAI_DUPLICATION_TARGETS = (
    "ค่าบริการ",
    "บุคคลทั่วไป",
    "นักศึกษา",
    "อุปกรณ์",
    "การแข่งขัน",
    "สมัคร",
    "ยกเลิก",
    "ชำระเงิน",
    "ตรวจสอบ",
    "เครื่อง",
    "ชั่วโมง",
    "รายละเอียด",
    "ติดต่อ",
    "ราคา",
    "เล่น",
    "จอง",
    "เปิด",
    "ปิด",
    "กติกา",
    "เวลา",
    "โซน",
    "เกม",
    "วันนี้",
    "เท่าไหร่",
    "อย่างไร",
)


PARTIAL_LAYOUT_TARGETS = (
    "ค่าบริการ",
    "ราคา",
    "เล่น",
    "จอง",
    "เปิด",
    "ปิด",
    "อุปกรณ์",
    "เครื่อง",
    "กติกา",
    "แข่งขัน",
    "สมัคร",
    "เวลา",
    "ชั่วโมง",
    "นักศึกษา",
    "บุคคลทั่วไป",
    "เท่าไหร่",
    "กี่บาท",
    "มีไหม",
    "อยู่ไหน",
    "ยังไง",
)


SHORT_THAI_LAYOUT_QUESTIONS = (
    "เล่น",
    "ราคา",
    "จอง",
    "เปิดไหม",
    "ปิดไหม",
    "กี่บาท",
    "มี VR ไหม",
    "PS5 ราคา",
    "เกมอะไร",
    "อยู่ไหน",
    "เปิดกี่โมง",
    "จองยังไง",
    "เล่นได้ไหม",
    "มี PC ไหม",
    "ค่าเล่น",
    "มี Minecraft ไหม",
    "VR ว่างไหม",
    "วันนี้เปิดไหม",
    "ต้องจองไหม",
    "ติดต่อใคร",
)


ENGLISH_LAYOUT_QUESTIONS = (
    "What games are available?",
    "How much is one hour on PC?",
    "Is VR available today?",
    "Can PSU students play for free?",
    "What time does the studio open?",
    "How do I book a PS5?",
    "Where is PSU Esports Studio?",
    "Can I bring my own controller?",
    "Is Minecraft available on PC?",
    "Which zone has Tekken 8?",
    "Can external students use the studio?",
    "What are the competition rules?",
    "How many gaming PCs are there?",
    "Is the studio open on Sunday?",
    "Can I cancel my booking?",
    "How much does Nintendo Switch cost?",
    "Do I need to pay before playing?",
    "What equipment is available in the VR zone?",
    "Can I play Valorant with my friends?",
    "Where can I contact the staff?",
    "Are food and drinks allowed?",
    "What happens if I arrive late?",
    "Can I reserve two machines?",
    "Is there a student discount?",
    "Please show the available game list.",
)


SHORT_REPEAT_PAIRS = (
    ("ราคคา", "ราคา", "thai_consonant"),
    ("จออง", "จอง", "thai_vowel"),
    ("เลล่น", "เล่น", "thai_consonant"),
    ("เปปิดไหม", "เปิดไหม", "thai_consonant"),
    ("กี่บบาท", "กี่บาท", "thai_consonant"),
    ("จอองยังไง", "จองยังไง", "thai_vowel"),
    ("เล่่นได้ไหม", "เล่นได้ไหม", "thai_tone_mark"),
    ("มีี VR ไหม", "มี VR ไหม", "thai_vowel_mark"),
    ("PSS5 ราคา", "PS5 ราคา", "latin_letter"),
    ("VVR ว่างไหม", "VR ว่างไหม", "latin_letter"),
    ("Valorrant", "Valorant", "latin_letter"),
    ("Tekkken 8", "Tekken 8", "latin_letter"),
    ("Mineccraft มีไหม", "Minecraft มีไหม", "latin_letter"),
    ("เปิดกี่โมมง", "เปิดกี่โมง", "thai_consonant"),
    ("เกมอะไรร", "เกมอะไร", "thai_consonant"),
)


PROTECTED_OR_MIXED_NEGATIVES = (
    "VR ราคาเท่าไหร่",
    "PS5 มีเกมอะไรบ้าง",
    "PC Zone เปิดกี่โมง",
    "VALORANT เล่นเครื่องไหน",
    "Minecraft มีใน PC #03 ไหม",
    "TEKKEN 8 อยู่โซนไหน",
    "Nintendo Switch OLED ราคาเท่าไหร่",
    "Counter-Strike 2 ใช้ Steam เวอร์ชันไหน",
    "ROV แข่งผ่าน Discord ใช่ไหม",
    "PUBG: BATTLEGROUNDS มีหรือเปล่า",
    "ดูข้อมูลที่ https://esports.phuket.psu.ac.th",
    "ติดต่อ esports@phuket.psu.ac.th ได้ไหม",
    "รหัสนักศึกษา 600584 ใช้สมัครได้ไหม",
    "booking ID BK-2026-000123 เช็คที่ไหน",
    "จองวันที่ 2026-09-01 เวลา 13:30",
    "เปิด 09:00-12:00 และ 13:00-16:00 ใช่ไหม",
    "โทร 076-123-4567 ได้หรือเปล่า",
    "เว็บ local อยู่ที่ http://127.0.0.1:8018/ ใช่ไหม",
    "BGE-M3 ใช้ทำ retrieval ใช่ไหม",
    "โมเดล scb10x/typhoon2.5-qwen3-4b ใช้อยู่หรือเปล่า",
    "ราคา 150 บาท/session ใช่ไหม",
    "PC #01-#02 เล่นเกมอะไรได้บ้าง",
    "QR CODE จากสลิปใช้ซ้ำได้ไหม",
    "API /api/slots ใช้งานได้หรือยัง",
    "WordPress REST API เชื่อมแล้วหรือยัง",
    "booking_id=BK-2026-000456 มีสถานะอะไร",
    "transaction_ref TXN20260830001 ซ้ำหรือเปล่า",
    "หมายเลข 061-234-5678 ติดต่อเจ้าหน้าที่ได้ไหม",
    "eFootball 2026 มีในศูนย์ไหม",
    "ตอบเป็น JSON ได้ไหม เช่น {\"zone\":\"PC\"}",
)


EXPRESSIVE_REPETITION_NEGATIVES = (
    "ราคาเท่าไหร่ครับบบ",
    "เล่นได้ไหมมม",
    "ขอบคุณค่าาา",
    "อยากเล่นมากกก",
    "ช่วยหน่อยยย",
    "ได้มั้ยยย",
    "จริงหรอออ",
    "โอเคคค",
    "ด่วน!!!",
    "วันนี้เปิดไหม???",
    "555555",
    "เยี่ยมมม",
    "อยากจองงง",
    "มีเกมใหม่ไหมมม",
    "ราคาน่ารักกก",
    "เล่น VR สนุกมากกก",
    "ขอรายละเอียดหน่อยยย",
    "ขอบคุณครับบบบ",
    "ได้เลยยย",
    "ว้าววว",
)


LEXICAL_DOUBLE_NEGATIVES = (
    "TEKKEN 8 เล่นที่ไหน",
    "Overcooked! 2 มีไหม",
    "Football Manager เล่นได้หรือเปล่า",
    "eFootball 2026 อยู่โซนไหน",
    "Call of Duty มีในศูนย์ไหม",
    "Assassin's Creed มีหรือเปล่า",
    "Hollow Knight เล่นเครื่องไหน",
    "Pool game มีในเครื่องหรือไม่",
    "กรรมการการแข่งขันติดต่อช่องทางไหน",
    "กิจกรรมการแข่งขันเริ่มกี่โมง",
    "บรรยากาศของ PSU Esports Studio เป็นอย่างไร",
    "แพ็กเกจธรรมดากับเหมาจ่ายต่างกันอย่างไร",
    "การแข่งขันมีกรรมการกี่คน",
    "Can I access the booking page?",
    "Is the booking process successful?",
    "Please tell staff about this issue.",
    "Is football available on PlayStation?",
    "Does the class pass include equipment?",
    "Can staff access my booking status?",
    "Is coffee allowed inside the studio?",
)


THAI_COMBINING_OR_VOWEL = set("่้๊๋์ัิีึืุู็ําเแโใไ")
THAI_NON_BASE = set("่้๊๋์ัิีึืุู็ํ")


def load_source_rows() -> list[dict]:
    rows: list[dict] = []
    with SOURCE_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                question = re.sub(r"\s+", " ", str(row.get("question", ""))).strip()
                if question:
                    row["question"] = question
                    rows.append(row)
    return rows


def has_thai(text: str) -> bool:
    return bool(re.search(r"[\u0E00-\u0E7F]", text))


def has_latin(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]", text))


def thai_to_english_keys(text: str) -> str:
    return "".join(KEYBOARD_THAI_TO_EN.get(char, char) for char in text)


def english_to_thai_keys(text: str) -> str:
    return "".join(KEYBOARD_EN_TO_THAI.get(char, char) for char in text)


def duplicate_thai_internal(text: str) -> tuple[str, str] | None:
    for term in THAI_DUPLICATION_TARGETS:
        start = text.find(term)
        if start < 0:
            continue
        candidate_indexes = [
            index
            for index, char in enumerate(term)
            if "\u0E00" <= char <= "\u0E7F" and char not in THAI_NON_BASE
        ]
        if not candidate_indexes:
            continue
        local_index = candidate_indexes[len(candidate_indexes) // 2]
        absolute_index = start + local_index
        char = text[absolute_index]
        mutated = text[:absolute_index] + char + text[absolute_index:]
        if mutated != text:
            return mutated, f"duplicated Thai base character {char!r} inside {term!r}"

    indexes = [
        index
        for index, char in enumerate(text)
        if "\u0E01" <= char <= "\u0E2E"
        and (index == 0 or text[index - 1] != char)
        and (index + 1 >= len(text) or text[index + 1] != char)
    ]
    if not indexes:
        return None
    index = indexes[len(indexes) // 2]
    char = text[index]
    return text[:index] + char + text[index:], f"duplicated Thai base character {char!r}"


def duplicate_thai_mark_or_vowel(text: str) -> tuple[str, str] | None:
    indexes = [index for index, char in enumerate(text) if char in THAI_COMBINING_OR_VOWEL]
    if not indexes:
        return None
    index = indexes[len(indexes) // 2]
    char = text[index]
    return text[:index] + char + text[index:], f"duplicated Thai vowel/tone character {char!r}"


def duplicate_latin_internal(text: str) -> tuple[str, str] | None:
    tokens = sorted(
        (match for match in re.finditer(r"[A-Za-z]{4,}", text)),
        key=lambda match: (-len(match.group(0)), match.start()),
    )
    for match in tokens:
        token = match.group(0)
        if any(left.lower() == right.lower() for left, right in zip(token, token[1:])):
            continue
        local_index = max(1, min(len(token) - 2, len(token) // 2))
        absolute_index = match.start() + local_index
        char = text[absolute_index]
        mutated = text[:absolute_index] + char + text[absolute_index:]
        return mutated, f"duplicated Latin character {char!r} inside {token!r}"
    return None


def map_one_thai_span(text: str) -> tuple[str, str] | None:
    for term in PARTIAL_LAYOUT_TARGETS:
        if term not in text:
            continue
        mapped = thai_to_english_keys(term)
        if mapped == term:
            continue
        return text.replace(term, mapped, 1), f"mapped only Thai span {term!r} to English keys"
    return None


def map_thai_suffix(text: str) -> tuple[str, str] | None:
    candidates = [text.find(term) for term in PARTIAL_LAYOUT_TARGETS if text.find(term) > 0]
    if candidates:
        start = sorted(candidates)[len(candidates) // 2]
    else:
        thai_indexes = [index for index, char in enumerate(text) if "\u0E00" <= char <= "\u0E7F"]
        if len(thai_indexes) < 4:
            return None
        start = thai_indexes[len(thai_indexes) // 2]
    suffix = text[start:]
    mapped = thai_to_english_keys(suffix)
    if mapped == suffix:
        return None
    return text[:start] + mapped, f"mapped Thai suffix beginning at character {start} to English keys"


def has_adjacent_repeat(text: str) -> bool:
    return any(left == right and not left.isspace() for left, right in zip(text, text[1:]))


def length_band(text: str) -> str:
    length = len(text)
    if length <= 3:
        return "01_03"
    if length <= 7:
        return "04_07"
    if length <= 15:
        return "08_15"
    if length <= 40:
        return "16_40"
    return "41_plus"


class SourcePool:
    def __init__(self, rows: Iterable[dict]) -> None:
        grouped: dict[str, list[dict]] = defaultdict(list)
        for row in rows:
            grouped[str(row.get("group", "unknown"))].append(row)
        for values in grouped.values():
            values.sort(key=lambda row: str(row.get("id", "")))
        self.grouped = grouped
        self.positions = defaultdict(int)
        self.used_ids: set[str] = set()
        self.next_group = 0

    def take(self, predicate: Callable[[dict], bool]) -> dict:
        for group_offset in range(len(GROUP_ORDER) * 4):
            group_index = (self.next_group + group_offset) % len(GROUP_ORDER)
            group = GROUP_ORDER[group_index]
            values = self.grouped.get(group, [])
            position = self.positions[group]
            while position < len(values):
                row = values[position]
                position += 1
                self.positions[group] = position
                source_id = str(row.get("id", ""))
                if source_id in self.used_ids or not predicate(row):
                    continue
                self.used_ids.add(source_id)
                self.next_group = (group_index + 1) % len(GROUP_ORDER)
                return row
        raise RuntimeError("No unused source row satisfied the requested predicate")


def make_source_metadata(row: dict | None) -> dict:
    if row is None:
        return {
            "source_group": "manual_edge_case",
            "source_case_id": None,
            "source_expected_category": None,
        }
    return {
        "source_group": row.get("group"),
        "source_case_id": row.get("id"),
        "source_expected_category": row.get("expected_category"),
    }


def build_cases(rows: list[dict]) -> list[dict]:
    manual_questions = {
        *SHORT_THAI_LAYOUT_QUESTIONS,
        *ENGLISH_LAYOUT_QUESTIONS,
        *PROTECTED_OR_MIXED_NEGATIVES,
        *EXPRESSIVE_REPETITION_NEGATIVES,
        *LEXICAL_DOUBLE_NEGATIVES,
        *(canonical for _, canonical, _ in SHORT_REPEAT_PAIRS),
    }
    pool = SourcePool(row for row in rows if row["question"] not in manual_questions)
    cases: list[dict] = []
    family_seen = Counter()
    observed_seen: set[str] = set()

    def add_case(
        *,
        family: str,
        observed_input: str,
        canonical_question: str,
        keyboard_mismatch: bool,
        repeated_typo: bool,
        expected_action: str,
        layout_direction: str | None,
        corruption_scope: str,
        repeat_interpretation: str,
        difficulty: str,
        label_confidence: str,
        generation_note: str,
        source_row: dict | None = None,
    ) -> None:
        observed = re.sub(r"\s+", " ", observed_input).strip()
        canonical = re.sub(r"\s+", " ", canonical_question).strip()
        if not observed or not canonical:
            raise AssertionError(f"empty case for {family}")
        if observed in observed_seen:
            raise AssertionError(f"duplicate observed input: {observed!r}")
        observed_seen.add(observed)
        family_seen[family] += 1
        within_family = family_seen[family]
        flags: list[str] = []
        if keyboard_mismatch:
            flags.append("keyboard_layout_mismatch")
        if repeated_typo:
            flags.append("repeated_character_typo")
        case = {
            "id": f"KIA-{len(cases) + 1:04d}",
            "split": "calibration" if within_family % 5 == 0 else "test",
            "observed_input": observed,
            "canonical_question": canonical,
            "expected_flags": flags,
            "should_detect_keyboard_layout": keyboard_mismatch,
            "should_detect_repeated_character": repeated_typo,
            "should_block_answer": keyboard_mismatch,
            "expected_action": expected_action,
            "anomaly_family": family,
            "layout_direction": layout_direction,
            "corruption_scope": corruption_scope,
            "repeat_interpretation": repeat_interpretation,
            "contains_adjacent_repeat": has_adjacent_repeat(observed),
            "length_band": length_band(observed),
            "difficulty": difficulty,
            "label_confidence": label_confidence,
            "generation_note": generation_note,
            **make_source_metadata(source_row),
        }
        cases.append(case)

    # Full Thai -> English-layout mismatch, including intentionally short inputs.
    for canonical in SHORT_THAI_LAYOUT_QUESTIONS:
        add_case(
            family="layout_th_to_en_full",
            observed_input=thai_to_english_keys(canonical),
            canonical_question=canonical,
            keyboard_mismatch=True,
            repeated_typo=False,
            expected_action="request_retype",
            layout_direction="thai_intended_english_active",
            corruption_scope="full_thai_script",
            repeat_interpretation="none",
            difficulty="hard" if len(canonical) <= 4 else "medium",
            label_confidence="high",
            generation_note="manual short-query layout mismatch",
        )
    for _ in range(TARGET_COUNTS["layout_th_to_en_full"] - len(SHORT_THAI_LAYOUT_QUESTIONS)):
        row = pool.take(lambda item: has_thai(item["question"]) and len(item["question"]) >= 8)
        canonical = row["question"]
        add_case(
            family="layout_th_to_en_full",
            observed_input=thai_to_english_keys(canonical),
            canonical_question=canonical,
            keyboard_mismatch=True,
            repeated_typo=False,
            expected_action="request_retype",
            layout_direction="thai_intended_english_active",
            corruption_scope="full_thai_script",
            repeat_interpretation="none",
            difficulty="easy" if len(canonical) >= 20 else "medium",
            label_confidence="high",
            generation_note="mapped every Thai character to its English-key position; existing Latin domain tokens were preserved",
            source_row=row,
        )

    for _ in range(TARGET_COUNTS["layout_th_to_en_token"]):
        while True:
            row = pool.take(lambda item: has_thai(item["question"]) and any(term in item["question"] for term in PARTIAL_LAYOUT_TARGETS))
            result = map_one_thai_span(row["question"])
            if result is not None:
                observed, note = result
                break
        add_case(
            family="layout_th_to_en_token",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=True,
            repeated_typo=False,
            expected_action="request_retype",
            layout_direction="thai_intended_english_active",
            corruption_scope="single_span",
            repeat_interpretation="none",
            difficulty="hard",
            label_confidence="high",
            generation_note=note,
            source_row=row,
        )

    for _ in range(TARGET_COUNTS["layout_th_to_en_suffix"]):
        while True:
            row = pool.take(lambda item: has_thai(item["question"]) and len(item["question"]) >= 14)
            result = map_thai_suffix(row["question"])
            if result is not None:
                observed, note = result
                break
        add_case(
            family="layout_th_to_en_suffix",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=True,
            repeated_typo=False,
            expected_action="request_retype",
            layout_direction="thai_intended_english_active",
            corruption_scope="suffix_after_mid_query_switch",
            repeat_interpretation="none",
            difficulty="hard",
            label_confidence="high",
            generation_note=note,
            source_row=row,
        )

    for canonical in ENGLISH_LAYOUT_QUESTIONS:
        add_case(
            family="layout_en_to_th_full",
            observed_input=english_to_thai_keys(canonical),
            canonical_question=canonical,
            keyboard_mismatch=True,
            repeated_typo=False,
            expected_action="request_retype",
            layout_direction="english_intended_thai_active",
            corruption_scope="full_english_script",
            repeat_interpretation="none",
            difficulty="medium",
            label_confidence="high",
            generation_note="mapped English-US QWERTY keystrokes to Thai Kedmanee output",
        )

    for _ in range(TARGET_COUNTS["repeat_thai_internal"]):
        while True:
            row = pool.take(lambda item: has_thai(item["question"]) and len(item["question"]) >= 6)
            result = duplicate_thai_internal(row["question"])
            if result is not None:
                observed, note = result
                break
        add_case(
            family="repeat_thai_internal",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=False,
            repeated_typo=True,
            expected_action="soft_flag_typo",
            layout_direction=None,
            corruption_scope="single_character_inside_thai_span",
            repeat_interpretation="accidental",
            difficulty="medium",
            label_confidence="high",
            generation_note=note,
            source_row=row,
        )

    for _ in range(TARGET_COUNTS["repeat_thai_mark_or_vowel"]):
        while True:
            row = pool.take(lambda item: has_thai(item["question"]) and any(char in THAI_COMBINING_OR_VOWEL for char in item["question"]))
            result = duplicate_thai_mark_or_vowel(row["question"])
            if result is not None:
                observed, note = result
                break
        add_case(
            family="repeat_thai_mark_or_vowel",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=False,
            repeated_typo=True,
            expected_action="soft_flag_typo",
            layout_direction=None,
            corruption_scope="thai_vowel_or_tone_mark",
            repeat_interpretation="accidental",
            difficulty="hard",
            label_confidence="high",
            generation_note=note,
            source_row=row,
        )

    for _ in range(TARGET_COUNTS["repeat_latin_internal"]):
        while True:
            row = pool.take(lambda item: has_latin(item["question"]) and bool(re.search(r"[A-Za-z]{4,}", item["question"])))
            result = duplicate_latin_internal(row["question"])
            if result is not None:
                observed, note = result
                break
        add_case(
            family="repeat_latin_internal",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=False,
            repeated_typo=True,
            expected_action="soft_flag_typo",
            layout_direction=None,
            corruption_scope="single_character_inside_latin_token",
            repeat_interpretation="accidental",
            difficulty="medium",
            label_confidence="high",
            generation_note=note,
            source_row=row,
        )

    for observed, canonical, subtype in SHORT_REPEAT_PAIRS:
        add_case(
            family="repeat_short_token",
            observed_input=observed,
            canonical_question=canonical,
            keyboard_mismatch=False,
            repeated_typo=True,
            expected_action="soft_flag_typo",
            layout_direction=None,
            corruption_scope="short_query_or_token",
            repeat_interpretation="accidental",
            difficulty="hard",
            label_confidence="high",
            generation_note=f"manual short repeated-character case: {subtype}",
        )

    for _ in range(TARGET_COUNTS["combined_layout_and_repeat"]):
        while True:
            row = pool.take(lambda item: has_thai(item["question"]) and len(item["question"]) >= 8)
            repeated = duplicate_thai_internal(row["question"])
            if repeated is not None:
                repeated_question, repeat_note = repeated
                observed = thai_to_english_keys(repeated_question)
                if observed != row["question"]:
                    break
        add_case(
            family="combined_layout_and_repeat",
            observed_input=observed,
            canonical_question=row["question"],
            keyboard_mismatch=True,
            repeated_typo=True,
            expected_action="request_retype",
            layout_direction="thai_intended_english_active",
            corruption_scope="full_thai_script_plus_repeated_key",
            repeat_interpretation="accidental",
            difficulty="hard",
            label_confidence="high",
            generation_note=f"{repeat_note}; then mapped Thai characters to English-key positions",
            source_row=row,
        )

    for _ in range(TARGET_COUNTS["valid_normal"]):
        row = pool.take(lambda item: len(item["question"]) >= 3)
        canonical = row["question"]
        add_case(
            family="valid_normal",
            observed_input=canonical,
            canonical_question=canonical,
            keyboard_mismatch=False,
            repeated_typo=False,
            expected_action="continue",
            layout_direction=None,
            corruption_scope="none",
            repeat_interpretation="none",
            difficulty="medium",
            label_confidence="high",
            generation_note="unchanged clean benchmark question used as a false-positive control",
            source_row=row,
        )

    for canonical in PROTECTED_OR_MIXED_NEGATIVES:
        add_case(
            family="valid_protected_or_mixed",
            observed_input=canonical,
            canonical_question=canonical,
            keyboard_mismatch=False,
            repeated_typo=False,
            expected_action="continue",
            layout_direction=None,
            corruption_scope="none",
            repeat_interpretation="none",
            difficulty="hard",
            label_confidence="high",
            generation_note="valid mixed-language, entity, URL, identifier, time, or technical-token control",
        )

    for canonical in EXPRESSIVE_REPETITION_NEGATIVES:
        add_case(
            family="valid_expressive_repetition",
            observed_input=canonical,
            canonical_question=canonical,
            keyboard_mismatch=False,
            repeated_typo=False,
            expected_action="continue",
            layout_direction=None,
            corruption_scope="none",
            repeat_interpretation="expressive",
            difficulty="hard",
            label_confidence="medium",
            generation_note="intentional chat-style elongation or repeated punctuation; must not be treated as an accidental key repeat",
        )

    for canonical in LEXICAL_DOUBLE_NEGATIVES:
        add_case(
            family="valid_lexical_double",
            observed_input=canonical,
            canonical_question=canonical,
            keyboard_mismatch=False,
            repeated_typo=False,
            expected_action="continue",
            layout_direction=None,
            corruption_scope="none",
            repeat_interpretation="lexical",
            difficulty="hard",
            label_confidence="high",
            generation_note="contains a legitimate adjacent repeated character inside a valid Thai or English word",
        )

    if len(cases) != 500:
        raise AssertionError(f"expected 500 cases, got {len(cases)}")
    if family_seen != Counter(TARGET_COUNTS):
        raise AssertionError(f"family count mismatch: {family_seen}")
    if len({case["id"] for case in cases}) != len(cases):
        raise AssertionError("duplicate case ID")
    if len({case["observed_input"] for case in cases}) != len(cases):
        raise AssertionError("duplicate observed input")
    if sum(case["split"] == "calibration" for case in cases) != 100:
        raise AssertionError("calibration split must contain exactly 100 cases")
    if sum(case["split"] == "test" for case in cases) != 400:
        raise AssertionError("test split must contain exactly 400 cases")
    return cases


def write_outputs(cases: list[dict]) -> None:
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8", newline="\n") as handle:
        for case in cases:
            handle.write(json.dumps(case, ensure_ascii=False, separators=(",", ":")) + "\n")

    csv_fields = list(cases[0].keys())
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        for case in cases:
            csv_case = dict(case)
            csv_case["expected_flags"] = "|".join(case["expected_flags"])
            writer.writerow(csv_case)

    summary = {
        "dataset": OUT_JSONL.name,
        "generated_from": SOURCE_PATH.name,
        "total": len(cases),
        "split_counts": dict(sorted(Counter(case["split"] for case in cases).items())),
        "family_counts": dict(sorted(Counter(case["anomaly_family"] for case in cases).items())),
        "flag_counts": {
            "keyboard_layout_mismatch": sum(case["should_detect_keyboard_layout"] for case in cases),
            "repeated_character_typo": sum(case["should_detect_repeated_character"] for case in cases),
            "no_flag": sum(not case["expected_flags"] for case in cases),
        },
        "action_counts": dict(sorted(Counter(case["expected_action"] for case in cases).items())),
        "length_band_counts": dict(sorted(Counter(case["length_band"] for case in cases).items())),
        "source_group_counts": dict(sorted(Counter(case["source_group"] for case in cases).items())),
        "quality_checks": {
            "unique_ids": len({case["id"] for case in cases}) == len(cases),
            "unique_observed_inputs": len({case["observed_input"] for case in cases}) == len(cases),
            "exactly_500_cases": len(cases) == 500,
            "calibration_100_test_400": Counter(case["split"] for case in cases) == {"calibration": 100, "test": 400},
        },
    }
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows = load_source_rows()
    cases = build_cases(rows)
    write_outputs(cases)
    print(f"Wrote {len(cases)} cases")
    print(OUT_JSONL)
    print(OUT_CSV)
    print(OUT_SUMMARY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
