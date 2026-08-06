from __future__ import annotations

import re
from difflib import SequenceMatcher
from functools import lru_cache

from app.core.thai_nlp import safe_thai_spell_normalize


THAI_DIGIT_TRANS = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
THAI_SOFT_MATCH_REMOVE = str.maketrans("", "", "่้๊๋์")

KEYBOARD_EN_TO_THAI = {
    "`": "_", "~": "%",
    "1": "ๅ", "!": "+", "2": "/", "@": "๑", "3": "-", "#": "๒", "4": "ภ", "$": "๓",
    "5": "ถ", "%": "๔", "6": "ุ", "^": "ู", "7": "ึ", "&": "฿", "8": "ค", "*": "๕",
    "9": "ต", "(": "๖", "0": "จ", ")": "๗", "-": "ข", "_": "๘", "=": "ช", "+": "๙",
    "q": "ๆ", "Q": "๐", "w": "ไ", "W": "\"", "e": "ำ", "E": "ฎ", "r": "พ", "R": "ฑ",
    "t": "ะ", "T": "ธ", "y": "ั", "Y": "ํ", "u": "ี", "U": "๊", "i": "ร", "I": "ณ",
    "o": "น", "O": "ฯ", "p": "ย", "P": "ญ", "[": "บ", "{": "ฐ", "]": "ล", "}": ",",
    "\\": "ฃ", "|": "ฅ", "a": "ฟ", "A": "ฤ", "s": "ห", "S": "ฆ", "d": "ก", "D": "ฏ",
    "f": "ด", "F": "โ", "g": "เ", "G": "ฌ", "h": "้", "H": "็", "j": "่", "J": "๋",
    "k": "า", "K": "ษ", "l": "ส", "L": "ศ", ";": "ว", ":": "ซ", "'": "ง", "\"": ".",
    "z": "ผ", "Z": "(", "x": "ป", "X": ")", "c": "แ", "C": "ฉ", "v": "อ", "V": "ฮ",
    "b": "ิ", "B": "ฺ", "n": "ื", "N": "์", "m": "ท", "M": "?", ",": "ม", "<": "ฒ",
    ".": "ใ", ">": "ฬ", "/": "ฝ", "?": "ฦ",
}
KEYBOARD_THAI_TO_EN = {thai: en for en, thai in KEYBOARD_EN_TO_THAI.items() if len(thai) == 1}
KEYBOARD_LAYOUT_DOMAIN_TERMS = (
    "game", "games", "moba", "fps", "rts", "battle", "royale", "valorant", "tekken",
    "mario", "nintendo", "switch", "playstation", "ps5", "pc", "vr", "ปุ่ม", "เกม",
    "โมบา", "โมบ้า", "ตีป้อม", "ยิง", "แข่งรถ", "จอง", "ราคา", "อุปกรณ์",
)
KEYBOARD_LAYOUT_SIGNAL_TERMS = (
    "moba", "fps", "rts", "battle royale", "battle", "royale", "valorant", "tekken",
    "mario", "nintendo", "switch", "playstation", "ps5", "pc", "vr", "โมบา", "โมบ้า",
    "ตีป้อม", "แข่งรถ", "counter-strike", "pubg", "warzone", "fortnite",
)

QUERY_VARIANT_ALIASES = {
    # Wrong keyboard layout / common domain typos. Keep this explicit to avoid slow noisy translation variants.
    "ทนิฟ": "moba",
    "f,[hk": "moba",
    "ดยห": "fps",
    "ติะะสำ พนัฟสำ": "battle royale",
    "ิฟะะสำ พนัฟสำ": "battle royale",
    "พะห": "rts",
}


def _translate_keyboard_layout(value: str, mapping: dict[str, str]) -> str:
    return "".join(mapping.get(ch, ch) for ch in value)


def _keyboard_layout_variants(raw_value: str) -> list[str]:
    variants: list[str] = []
    raw_normalized = raw_value.lower().strip()
    for candidate in (
        _translate_keyboard_layout(raw_value, KEYBOARD_EN_TO_THAI),
        _translate_keyboard_layout(raw_value, KEYBOARD_THAI_TO_EN),
    ):
        normalized_candidate = candidate.lower().strip()
        if normalized_candidate and normalized_candidate != raw_value.lower().strip():
            has_new_signal = any(term in normalized_candidate and term not in raw_normalized for term in KEYBOARD_LAYOUT_SIGNAL_TERMS)
            if has_new_signal:
                variants.append(normalized_candidate)
    return list(dict.fromkeys(variants))


def build_query_variants(text: str, *, limit: int = 5) -> tuple[str, ...]:
    raw_value = (text or "").strip()
    if not raw_value:
        return ()

    candidates = [raw_value, normalize_text(raw_value)]
    raw_lower = raw_value.lower()
    for alias, canonical in QUERY_VARIANT_ALIASES.items():
        if alias in raw_lower and canonical not in raw_lower:
            candidates.append(f"{raw_value} {canonical}")
            candidates.append(f"{normalize_text(raw_value)} {canonical}")

    variants: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        clean = re.sub(r"\s+", " ", str(candidate or "")).strip()
        if not clean:
            continue
        key = clean.lower()
        if key in seen:
            continue
        seen.add(key)
        variants.append(clean)
        if len(variants) >= limit:
            break
    return tuple(variants)


SERVICE_ALIASES = {
    "ps5": ["ps5", "playstation 5", "playstation", "เพลย์", "เพลย์ห้า", "เครื่องเพลย์", "ps 5"],
    "nintendo_switch": ["nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์", "nintendo switch"],
    "cockpit": ["cockpit", "ค็อกพิท", "คอกพิท", "ขับรถ", "พวงมาลัย", "racing", "sim racing"],
    "vr": ["vr", "วีอาร์", "แว่น vr", "แว่นวีอาร์", "virtual reality"],
    "pc": ["pc", "pc zone", "คอม", "คอมศูนย์", "คอมพิวเตอร์", "เครื่องคอม", "เครื่อง pc", "computer"],
}


CUSTOMER_GROUP_ALIASES = {
    "psu_student_staff": [
        "นักศึกษา มอ", "นักเรียน มอ", "เด็ก มอ", "นิสิต มอ", "นักศึกษา psu", "นักเรียน psu",
        "psu student", "psu staff", "บุคลากร psu", "บุคลากร มอ", "staff psu", "มอ",
        "มหาวิทยาลัยสงขลานครินทร์", "สงขลานครินทร์", "prince of songkla", "psu phuket",
    ],
    "general_student": [
        "ต่างมหาลัย", "ต่างมหาวิทยาลัย", "ต่างสถาบัน", "นักศึกษาทั่วไป", "นักเรียนทั่วไป",
        "นักศึกษาต่างมหาลัย", "นักเรียนต่างมหาลัย", "นักศึกษาต่างสถาบัน", "นักเรียนต่างสถาบัน",
        "เด็กต่างมหาลัย", "เด็กต่างสถาบัน", "เด็กมหาลัยอื่น", "มหาลัยอื่น", "มหาวิทยาลัยอื่น",
        "นักศึกษาจากมหาวิทยาลัยอื่น", "นักศึกษาจากมหาลัยอื่น", "นักเรียนจากโรงเรียนอื่น",
        "ต่างโรงเรียน", "โรงเรียนอื่น", "ไม่ใช่มอ", "ไม่ใช่ มอ", "ไม่ได้เรียนมอ", "ไม่ได้เรียน มอ",
        "general student", "external student", "student from another university", "alumni", "ศิษย์เก่า",
        "ศิษย์เก่า psu",
        "สจล", "kmitl", "ลาดกระบัง", "พระจอมเกล้าลาดกระบัง",
        "จุฬา", "จุฬาลงกรณ์", "chula",
        "มธ", "tu", "ธรรมศาสตร์",
        "มก", "ku", "เกษตรศาสตร์", "เกษตร",
        "มช", "cmu", "เชียงใหม่",
        "มข", "kku", "ขอนแก่น",
        "มหิดล", "mahidol", "mu",
        "มศว", "swu", "ศรีนครินทรวิโรฒ",
        "มจธ", "kmutt", "บางมด",
        "มจพ", "kmutnb", "พระนครเหนือ",
        "มบ", "มหาวิทยาลัยกรุงเทพ", "ม.กรุงเทพ", "bangkok university",
        "รังสิต", "rsu", "เอแบค", "abac", "assumption university",
        "หอการค้า", "utcc", "ราชภัฏ", "ราชมงคล", "rmutt", "เทคนิค", "อาชีวะ", "vocational",
    ],
    "general_adult": [
        "บุคคลทั่วไป", "คนทั่วไป", "ผู้ใหญ่ทั่วไป", "general adult", "adult", "คนนอก", "ประชาชนทั่วไป",
        "ไม่ได้เป็นนักศึกษา", "ไม่ใช่นักศึกษา", "พนักงานบริษัท", "ผู้ปกครอง",
    ],
}


PRICE_WORD_ALIASES = [
    "ราคา", "ค่าบริการ", "เสียกี่บาท", "กี่บาท", "เท่าไหร่", "เท่าไร", "fee", "price", "cost", "บาท",
]


TIME_WORD_ALIASES = {
    "half_hour": ["ครึ่งชม", "ครึ่ง ชม", "ครึ่งชั่วโมง", "30 นาที", "30นาที", "half hour", "0.5 hour"],
    "one_hour": ["1 ชั่วโมง", "1ชม", "1 ชม", "หนึ่งชั่วโมง", "60 นาที", "1 hour", "one hour"],
}


DAY_ALIASES = {
    "monday": ["จันทร์", "วันจันทร์", "mon", "monday"],
    "tuesday": ["อังคาร", "วันอังคาร", "tue", "tuesday"],
    "wednesday": ["พุธ", "วันพุธ", "wed", "wednesday"],
    "thursday": ["พฤหัส", "พฤหัสบดี", "วันพฤหัส", "thu", "thursday"],
    "friday": ["ศุกร์", "วันศุกร์", "fri", "friday"],
    "saturday": ["เสาร์", "วันเสาร์", "sat", "saturday"],
    "sunday": ["อาทิตย์", "วันอาทิตย์", "sun", "sunday"],
}


EXTERNAL_INSTITUTION_LABELS = {
    "สจล": ["สจล", "kmitl", "ลาดกระบัง", "พระจอมเกล้าลาดกระบัง"],
    "จุฬา": ["จุฬา", "จุฬาลงกรณ์", "chula"],
    "มธ": ["มธ", "ธรรมศาสตร์", "tu"],
    "มก": ["มก", "เกษตร", "เกษตรศาสตร์", "ku"],
    "มช": ["มช", "เชียงใหม่", "cmu"],
    "มข": ["มข", "ขอนแก่น", "kku"],
    "มหิดล": ["มหิดล", "mahidol", "mu"],
    "มศว": ["มศว", "ศรีนครินทรวิโรฒ", "swu"],
    "มจธ": ["มจธ", "บางมด", "kmutt"],
    "มจพ": ["มจพ", "พระนครเหนือ", "kmutnb"],
    "มหาวิทยาลัยกรุงเทพ": ["มหาวิทยาลัยกรุงเทพ", "ม.กรุงเทพ", "bangkok university"],
    "รังสิต": ["รังสิต", "rsu"],
    "เอแบค": ["เอแบค", "abac", "assumption university"],
    "หอการค้า": ["หอการค้า", "utcc"],
    "ราชภัฏ": ["ราชภัฏ"],
    "ราชมงคล": ["ราชมงคล", "rmutt"],
    "เทคนิค/อาชีวะ": ["เทคนิค", "อาชีวะ", "vocational"],
    "มหาวิทยาลัยอื่น": ["มหาลัยอื่น", "มหาวิทยาลัยอื่น"],
    "โรงเรียนอื่น": ["โรงเรียนอื่น", "ต่างโรงเรียน"],
}


FUZZY_NORMALIZATION_KEYWORDS = {
    "รายการ": 0.80,
    "แข่งขัน": 0.80,
    "ราคา": 0.86,
    "บริการ": 0.80,
    "นักศึกษา": 0.78,
    "อุปกรณ์": 0.78,
    "อาหาร": 0.82,
    "เครื่องดื่ม": 0.78,
    "วันนี้": 0.84,
    "พรุ่งนี้": 0.80,
    "กติกา": 0.82,
    "รางวัล": 0.82,
    "ขั้นตอน": 0.80,
}


DOMAIN_CONTEXT_FUZZY_KEYWORDS = {
    "เล่น": 0.74,
    "วิธี": 0.74,
    "เปิด": 0.75,
}


FUZZY_NORMALIZATION_PREFIXES = {
    "รายการ": ("รายก",),
    "แข่งขัน": ("แข",),
    "ราคา": ("ราค",),
    "บริการ": ("บริ",),
    "นักศึกษา": ("นัก", "นกศ"),
    "อุปกรณ์": ("อุป",),
    "อาหาร": ("อา",),
    "เครื่องดื่ม": ("เครื่อง", "เครื่อ"),
    "วันนี้": ("วัน",),
    "พรุ่งนี้": ("พรุ่ง", "พร่ง"),
    "กติกา": ("กติ",),
    "รางวัล": ("ราง",),
    "ขั้นตอน": ("ขั้น",),
    "เล่น": ("เล", "เ", "เร"),
    "วิธี": ("วิ", "วี"),
    "เปิด": ("เป", "ปิ"),
}


DOMAIN_CONTEXT_TERMS = (
    "เกม", "game", "games", "vr", "ps5", "playstation", "nintendo", "switch", "pc",
    "คอม", "คอกพิท", "ค็อกพิท", "พวงมาลัย", "ราคา", "ค่าบริการ", "บาท", "รอบ",
    "เวลา", "วันนี้", "พรุ่งนี้", "วันจันทร์", "valorant", "valo", "วาโล", "cs2",
    "pubg", "warzone", "tekken", "fortnite", "beat", "saber", "horizon", "mario",
    "minecraft", "roblox", "จอง", "บริการ", "ศูนย์", "esports", "psu",
)


def _fuzzy_replace_keyword(value: str, canonical: str, threshold: float) -> str:
    if not value or canonical in {"", value}:
        return value

    canonical_len = len(canonical)
    min_len = max(2, canonical_len - 1)
    max_len = min(len(value), canonical_len + 1 if canonical_len <= 4 else canonical_len)
    prefixes = FUZZY_NORMALIZATION_PREFIXES.get(canonical, ())
    replacements: list[tuple[int, int, str]] = []
    occupied: set[int] = set()

    for start in range(len(value)):
        best: tuple[float, int, int] | None = None
        for length in range(min_len, max_len + 1):
            end = start + length
            if end > len(value):
                continue
            candidate = value[start:end]
            if candidate == canonical or any(ch.isspace() for ch in candidate):
                continue
            if candidate in canonical:
                continue
            if candidate.startswith(canonical) or candidate.endswith(canonical):
                continue
            if prefixes and not candidate.startswith(prefixes):
                continue
            score = _ratio(candidate, canonical)
            if score < threshold:
                continue
            if best is None or score > best[0]:
                best = (score, start, end)
        if best is None:
            continue
        _, match_start, match_end = best
        span = set(range(match_start, match_end))
        if occupied.intersection(span):
            continue
        occupied.update(span)
        replacements.append((match_start, match_end, canonical))

    for start, end, replacement in sorted(replacements, reverse=True):
        value = value[:start] + replacement + value[end:]
    return value


def _fuzzy_normalize_intent_keywords(value: str) -> str:
    for canonical, threshold in FUZZY_NORMALIZATION_KEYWORDS.items():
        value = _fuzzy_replace_keyword(value, canonical, threshold)
    if _has_domain_context(value):
        for canonical, threshold in DOMAIN_CONTEXT_FUZZY_KEYWORDS.items():
            value = _fuzzy_replace_keyword(value, canonical, threshold)
    return value


def _has_domain_context(value: str) -> bool:
    return any(term in value for term in DOMAIN_CONTEXT_TERMS)


@lru_cache(maxsize=8192)
def normalize_text(text: str) -> str:
    raw_value = (text or "").strip().translate(THAI_DIGIT_TRANS)
    value = raw_value.lower()
    replacements = {
        "ม.อ.": "มอ",
        "ม.อ": "มอ",
        "ม. อ.": "มอ",
        "p.s.u.": "psu",
        "p s u": "psu",
        "สจล.": "สจล",
        "k.m.i.t.l.": "kmitl",
        "k m i t l": "kmitl",
        "check-in": "checkin",
        "check in": "checkin",
        "ช.ม.": "ชม",
        "ชม.": "ชม",
        "น.ท.": "นาที",
        "น.ศ.": "นักศึกษา",
        "นศ.": "นักศึกษา",
        "บัตรนศ": "บัตรนักศึกษา",
        "บัตร นศ": "บัตรนักศึกษา",
        "แข่งมเกม": "แข่งเกม",
        "รายการแข่งมเกม": "รายการแข่งเกม",
        "รายกร": "รายการ",
        "รายกาา": "รายการ",
        "รายกาาร": "รายการ",
        "รายการเเข่ง": "รายการแข่ง",
        "แข่งอะไรบ้าง": "รายการแข่งอะไรบ้าง",
        "จัทนร์": "จันทร์",
        "จันทรื": "จันทร์",
        "วันจัน": "วันจันทร์",
        "จันเปิด": "จันทร์เปิด",
        "เพลห้า": "เพลย์ห้า",
        "วีอา": "วีอาร์",
        "วีอาร์": "vr",
        "วีอาอา": "vr",
        "คอกพิต": "คอกพิท",
        "ค็อกพิต": "ค็อกพิท",
        "พีซี": "pc",
        "เครื่องคอม": "คอม",
        "คอมฯ": "คอม",
        "ของกิน": "อาหาร",
        "ข้าว": "อาหาร",
        "ขนมขบเคี้ยว": "ขนม",
        "ไมห": "ไหม",
        "ใหม": "ไหม",
        "มั๊ย": "มั้ย",
        "ม้าย": "ไหม",
        "ป่าว": "เปล่า",
        "รึเป่า": "รึเปล่า",
        "หรือป่าว": "หรือเปล่า",
        "ขั้นตอนที่": "ขั้นที่",
        "สเตป": "ขั้น",
        "step": "ขั้น",
        "เงินรางวัล": "รางวัล",
        "ชนะได้เงิน": "ชนะได้เงินรางวัล",
        "วิธีเ่น": "วิธีเล่น",
        "วิธฟ": "วิธี",
        "วีธฟ": "วิธี",
        "เ่น ": "เล่น ",
        "beat saver": "beat saber",
        "beatsaver": "beat saber",
        "ssb": "super smash",
        "ssmu": "super smash",
        "วาโลแรนท์": "valorant",
        "วาโลแรน": "valorant",
        "วาโร": "วาโล",
        "เทคเคน8": "เทคเคน 8",
        "เทกเคน": "เทคเคน",
        "อาโอวี": "rov",
        "เอโอวี": "rov",
        "อาร์โอวี": "rov",
        "อาโอวี่": "rov",
        "เคาน์เตอร์สไตรค์": "counter-strike",
        "เคาน์เตอร์": "counter-strike",
        "เคาเตอร์": "counter-strike",
        "พับจี": "pubg",
        "วอร์โซน": "warzone",
        "คอลออฟดิวตี้": "call of duty",
        "คอล ออฟ ดิวตี้": "call of duty",
        "โมเดิร์นวอร์แฟร์": "modern warfare",
        "ลีกออฟเลเจนด์": "league of legends",
        "ลีคออฟเลเจนด์": "league of legends",
        "ลีกออฟ": "league of legends",
        "สไปเดอร์แมน": "spider-man",
        "สไปเดอร์": "spider",
        "ฟอร์ทไนท์": "fortnite",
        "ก็อดออฟวอร์": "god of war",
        "ก๊อดออฟวอร์": "god of war",
        "บีทเซเบอร์": "beat saber",
        "ฮอไรซอน": "horizon",
        "แกรนทัวริสโม": "gran turismo",
        "แกรน turismo": "gran turismo",
        "จีที7": "gt7",
        "จีที 7": "gt7",
        "เกมบอล": "fc 24",
        "ฟีฟ่า": "fifa",
        "ไฟนอลแฟนตาซี": "final fantasy",
        "ฮอกวอตส์": "hogwarts",
        "เรสซิเดนต์อีวิล": "resident evil",
        "เรสซิเดนต์": "resident evil",
        "เรสิเด้นอีวิล": "resident evil",
        "เรสสิเด้นอีวิว": "resident evil",
        "เรสสิเด้นอีวิล": "resident evil",
        "เรสิเด้น": "resident evil",
        "นารูโตะ": "naruto",
        "โบรูโตะ": "boruto",
        "เดอะลาสต์ออฟอัส": "last of us",
        "ลาสต์ออฟอัส": "last of us",
        "อันชาร์ตเต็ด": "uncharted",
        "มาริโอคาร์ท": "mario kart",
        "มาริโอ คาร์ท": "mario kart",
        "โอเวอร์คุก": "overcooked",
        "โอเวอร์คุ๊ก": "overcooked",
        "โอเวอคุก": "overcooked",
        "โอเวอคุ๊ก": "overcooked",
        "โอเวอร์คุค": "overcooked",
        "สแมชบราเธอร์": "smash bros",
        "สแมชบรอส": "smash bros",
        "สวิตช์สปอร์ต": "switch sports",
        "สวิทช์สปอร์ต": "switch sports",
        "แอนิมอลครอสซิง": "animal crossing",
        "แอนิมอลครอสซิ่ง": "animal crossing",
        "อิทเทคส์ทู": "it takes two",
        "ลุยจิ": "luigi",
        "มาริโอปาร์ตี้": "mario party",
        "มอนสเตอร์ฮันเตอร์": "monster hunter",
        "มูฟวิ่งเอาท์": "moving out",
        "มาริโอ้": "mario",
        "ซูเปอร์มาริโอ": "super mario",
        "ริงฟิต": "ring fit",
        "เซลด้า": "zelda",
        "เซลันด้า": "zelda",
        "ลิตเติลไนท์แมร์": "little nightmares",
        "โมบ้า": "moba",
        "โมบา": "moba",
        "โมบะ": "moba",
        "โมบ้่า": "moba",
        "เอฟพีเอส": "fps",
        "เอฟ พี เอส": "fps",
        "แบทเทิลรอยัล": "battle royale",
        "แบทเทิล โรยัล": "battle royale",
        "แบทเทิลรอย": "battle royale",
        "แบทเทิลรอยาล": "battle royale",
        "แบตเทิลรอยัล": "battle royale",
        "อาร์ทีเอส": "rts",
        "อาร์ ที เอส": "rts",
        "เรียลไทม์สตราทีจี": "real-time strategy",
        "เรียลไทม์สเตรทิจี": "real-time strategy",
        "การ์ดเกม": "digital card",
        "เกมการ์ด": "digital card",
        "ไฟติ้ง": "fighting",
        "ไฟท์ติ้ง": "fighting",
        "เรซซิ่ง": "racing",
        "เรซิ่ง": "racing",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"(?<![\u0E00-\u0E7F])(?:ดือน|เดือร|เดิอน)", "เดือน", value)
    if len(value) <= 160:
        value = _fuzzy_normalize_intent_keywords(value)
    value = safe_thai_spell_normalize(value)
    value = re.sub(r"\s+", " ", value)
    return value


def _ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def _soft_alias_text(value: str) -> str:
    normalized = normalize_text(value).translate(THAI_SOFT_MATCH_REMOVE)
    normalized = normalized.replace("ต์", "ต")
    return re.sub(r"\s+", "", normalized)


def _raw_soft_alias_text(value: str) -> str:
    normalized = (value or "").lower().strip().translate(THAI_DIGIT_TRANS).translate(THAI_SOFT_MATCH_REMOVE)
    normalized = normalized.replace("ต์", "ต")
    return re.sub(r"\s+", "", normalized)


def _best_compact_window_ratio(query: str, alias: str) -> float:
    if not query or not alias:
        return 0.0
    alias_len = len(alias)
    min_len = max(2, alias_len - 2)
    max_len = min(len(query), alias_len + 2)
    best = 0.0
    for start in range(len(query)):
        for length in range(min_len, max_len + 1):
            end = start + length
            if end > len(query):
                continue
            best = max(best, _ratio(query[start:end], alias))
    return best


def contains_alias(query: str, aliases: list[str], *, fuzzy: bool = True, threshold: float = 0.84) -> tuple[bool, str, float]:
    q = normalize_text(query)
    q_soft = _soft_alias_text(query)
    q_raw_soft = _raw_soft_alias_text(query)
    for alias in aliases:
        a = normalize_text(alias)
        if a and a in q:
            return True, alias, 1.0
        a_soft = _soft_alias_text(alias)
        if a_soft and len(a_soft) >= 4 and a_soft in q_soft:
            return True, alias, 0.97
        a_raw_soft = _raw_soft_alias_text(alias)
        if a_raw_soft and len(a_raw_soft) >= 4 and a_raw_soft in q_raw_soft:
            return True, alias, 0.96
    if not fuzzy:
        return False, "", 0.0

    tokens = [tok for tok in re.split(r"[\s,./|()\[\]{}:;!?]+", q) if tok]
    alias_norms = [(alias, normalize_text(alias)) for alias in aliases]
    best_alias = ""
    best_score = 0.0

    for alias, alias_norm in alias_norms:
        if not alias_norm:
            continue
        alias_tokens = alias_norm.split()
        window_size = max(1, len(alias_tokens))
        candidates = tokens if window_size == 1 else [" ".join(tokens[i:i + window_size]) for i in range(max(0, len(tokens) - window_size + 1))]
        for candidate in candidates:
            score = _ratio(candidate, alias_norm)
            if score > best_score:
                best_score = score
                best_alias = alias
        if re.search(r"[\u0E00-\u0E7F]", alias_norm):
            alias_soft = _soft_alias_text(alias_norm)
            if len(alias_soft) >= 4:
                score = _best_compact_window_ratio(q_soft, alias_soft)
                if score > best_score:
                    best_score = score
                    best_alias = alias
            alias_raw_soft = _raw_soft_alias_text(alias)
            if len(alias_raw_soft) >= 4:
                score = _best_compact_window_ratio(q_raw_soft, alias_raw_soft)
                if score > best_score:
                    best_score = score
                    best_alias = alias

    if best_score >= threshold:
        return True, best_alias, best_score
    return False, best_alias, best_score


def detect_from_aliases(query: str, alias_map: dict[str, list[str]], *, threshold: float = 0.84) -> dict:
    matches = []
    for key, aliases in alias_map.items():
        ok, alias, score = contains_alias(query, aliases, fuzzy=False, threshold=threshold)
        if ok:
            matches.append({"key": key, "alias": alias, "score": score})
    if matches:
        matches.sort(key=lambda row: row["score"], reverse=True)
        top_score = matches[0]["score"]
        tied = [m for m in matches if abs(m["score"] - top_score) < 0.03]
        return {"key": matches[0]["key"], "ambiguous": len(tied) > 1, "matches": matches}

    for key, aliases in alias_map.items():
        ok, alias, score = contains_alias(query, aliases, fuzzy=True, threshold=threshold)
        if ok:
            matches.append({"key": key, "alias": alias, "score": score})
    matches.sort(key=lambda row: row["score"], reverse=True)
    if not matches:
        return {"key": None, "ambiguous": False, "matches": []}
    top_score = matches[0]["score"]
    tied = [m for m in matches if abs(m["score"] - top_score) < 0.03]
    return {"key": matches[0]["key"], "ambiguous": len(tied) > 1, "matches": matches}


def has_price_intent(query: str) -> bool:
    return contains_alias(query, PRICE_WORD_ALIASES, fuzzy=False)[0]


def detect_external_institution_label(query: str) -> str | None:
    q = normalize_text(query)
    for label, aliases in EXTERNAL_INSTITUTION_LABELS.items():
        for alias in aliases:
            alias_norm = normalize_text(alias)
            if alias_norm and alias_norm in q:
                return label
    return None
