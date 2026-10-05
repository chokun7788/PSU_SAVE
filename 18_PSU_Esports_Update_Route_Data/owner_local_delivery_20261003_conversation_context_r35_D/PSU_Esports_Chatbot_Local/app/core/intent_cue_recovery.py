"""Bounded recovery of task words; never rewrites names, dates or numbers.

This complements the existing phrase and keyboard recoverers. Its lexicon is
made of operations the bot already supports, not whole user questions.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

from app.core.typo_similarity import osa_distance


_TIME = re.compile(r"\b\d{1,2}:\d{2}\b")
_RESOURCE = re.compile(r"\b(?:pc(?:[ -]?#?\d+)?|ps5|vr|cockpit|nintendo|switch|playstation)\b|โซน|เครื่อง", re.I)
_EN_TOKEN = re.compile(r"[A-Za-z]+")
_POLITE = ("ครับ", "ค่ะ", "คับ", "คะ")
_VALID_THAI_PRICE = ("ราคาเท่าไหร่", "ราคาเท่าไร", "ราคากี่บาท")
_VALID_ENGLISH_WORDS = {
    "score", "scores",
    "play", "pay", "book", "look", "free", "game", "games", "gates", "names",
    "times", "came", "same", "name", "gear", "tone", "done", "looking", "cooking",
    "drink", "drinks", "allowed", "permitted", "booking", "information", "equipment",
    "zone", "zones", "session", "sessions", "member", "members", "afternoon", "competition", "competitions",
    "team", "teams", "steam", "teal", "term", "seam", "age", "are", "ace", "axe", "policy", "official", "scope", "identity", "rulebook", "rulebooks", "tournament", "tournaments", "requirement", "requirements",
}
_EN_KEY_POSITIONS = {
    key: (row, column + offset)
    for row, (keys, offset) in enumerate((("qwertyuiop", 0.5), ("asdfghjkl", 0.75), ("zxcvbnm", 1.25)))
    for column, key in enumerate(keys)
}


def _short_grammar_edit_allowed(observed: str, target: str) -> bool:
    """Short same-length substitutions must also agree with key geometry."""
    if len(observed) != len(target):
        return True  # insertion/deletion, already bounded by OSA
    differences = [(a, b) for a, b in zip(observed, target) if a != b]
    if len(differences) != 1:
        return True  # adjacent transposition, already bounded by OSA
    left, right = differences[0]
    if left not in _EN_KEY_POSITIONS or right not in _EN_KEY_POSITIONS:
        return False
    row1, col1 = _EN_KEY_POSITIONS[left]
    row2, col2 = _EN_KEY_POSITIONS[right]
    return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1.25


@dataclass(frozen=True)
class CueRecovery:
    raw: str
    recovered: str
    observed: str
    intended: str
    start: int
    distance: int
    reason: str


def _contextual_task_cue(text: str) -> CueRecovery | None:
    """One-edit task words inside syntax frames, not a global spellchecker."""
    lower = text.casefold()
    tokens = list(_EN_TOKEN.finditer(text))

    def near(word: str) -> bool:
        return any(
            abs(len(token.group()) - len(word)) <= 1
            and osa_distance(token.group().casefold(), word) <= 1
            for token in tokens
        )

    # A location interrogative is recoverable with a surviving modal frame.
    for token in tokens:
        observed=token.group().casefold()
        if observed not in _VALID_ENGLISH_WORDS and osa_distance(observed,'where') == 1 and re.match(r'\s+can\s+(?:i|we|you)\s+',lower[token.end():]):
            return CueRecovery(text,text[:token.start()]+'where'+text[token.end():],token.group(),'where',token.start(),1,'location interrogative plus modal frame')
    if re.search(r'อยู่|มี',text) and re.search(r'ไหน|อะไร',text):
        for token in re.finditer(r'โซ[\u0e00-\u0e7f]{1,4}(?=ไหน|อะไร)',text):
            if osa_distance(token.group(),'โซน') == 1:
                return CueRecovery(text,text[:token.start()]+'โซน'+text[token.end():],token.group(),'โซน',token.start(),1,'Thai zone location frame')
    booking_context = near("booking") or bool(re.search(r"\b(?:book|reserve|reservation)\b", lower))
    permission_context = near("allowed") or bool(re.search(r"\b(?:permitted|bring)\b", lower))
    drink_context = near("drinks") or bool(re.search(r"\b(?:food|snacks|water|alcoholic)\b", lower))
    rule_context = bool(re.search(r"\b(?:rule|rules|cite|tournament)\b", lower)) or near("rulebook")
    schedule_context = bool(re.search(r"\b(?:open|opening|hours?|schedule|session|monday|tuesday|wednesday|thursday|friday)\b", lower))
    price_frame = bool(re.search(r"\bhow\s+much\b|\b(?:price|cost|fee)\b", lower))
    price_resource = bool(_RESOURCE.search(text))
    for match in tokens:
        observed = match.group().casefold()
        before, after = lower[:match.start()], lower[match.end():]
        grammar_targets = []
        if observed not in {"play", "pay", "book", "look", "cook", "hook", "say", "far", "or", "nor", "not", "no", "an", "ant", "end"}:
            if re.search(r"\bavailable\s+$", before) and re.match(
                r"\s+(?:the\s+)?(?:pc|ps5|playstation|nintendo|vr|cockpit)\b", after,
            ) and re.search(r"\bgames?\b", lower):
                grammar_targets.append("for")
            if re.search(r"\bhow\s+many\s+sessions?\s+$", before) and re.match(r"\s+be\s+booked\b", after):
                grammar_targets.append("can")
            verb_frame = bool(re.search(r"\bhow\s+(?:do|can)\s+(?:i|we|they|you)\s+$", before))
            if verb_frame and (_RESOURCE.search(text) or booking_context):
                grammar_targets.append("book")
            if re.search(r"\bwhat\s+do\s+(?:you|i|we)\s+need\s+to\s+$", before) and re.match(r"\s+to\s+play\b", after):
                grammar_targets.append("book")
            if price_resource and re.search(r"\bhow\s+$", before) and re.match(r"\s+(?:does|do|is)\b", after):
                grammar_targets.append("much")
            if price_resource and re.search(r"\bhow\s+much\s+does\s+it\s+$", before) and re.match(r"\s+(?:for|to)\b", after) and observed not in {"cast", "coat", "post", "host", "lost", "most", "coast"}:
                grammar_targets.append("cost")
            if price_resource and re.search(r"\bhow\s+much\s+does\s+(?:pc|ps5|playstation(?:\s+5)?|nintendo\s+switch|cockpit|vr)\s+$", before) and re.match(r"\s+(?:for|to)\b", after) and observed not in {"cast", "coat", "post", "host", "lost", "most", "coast"}:
                grammar_targets.append("cost")
            if (verb_frame or re.search(r"\bhave\s+to\s+$", before)) and (
                booking_context or re.match(r"\s*(?:[?.]|$)", after)
            ):
                grammar_targets.append("pay")
            if re.match(r"\s+(?:what|how|which|who|where|is|can)\b", after) and re.search(
                r"\b(?:how\s+(?:much|to\s+book|do\s+i\s+book)|where\s+can|what\s+(?:are|is))\b", before,
            ):
                grammar_targets.append("and")
        grammar_winners = sorted({
            target for target in grammar_targets
            if abs(len(observed) - len(target)) <= 1 and osa_distance(observed, target) == 1
            and _short_grammar_edit_allowed(observed, target)
        })
        if len(grammar_winners) == 1:
            target = grammar_winners[0]
            return CueRecovery(
                text, text[:match.start()] + target + text[match.end():],
                match.group(), target, match.start(), 1, "operation-anchored English grammar recovery",
            )
        if observed in _VALID_ENGLISH_WORDS or len(observed) < 4:
            continue
        targets = []
        # Eligibility labels require an independent price/resource frame.
        # Recover the label only; negation and institution identifiers stay raw.
        if price_frame and price_resource:
            if re.search(r"\bpsu\s+$", before) and observed not in {"studied", "students"}:
                targets.append("student")
            if not before.strip() and re.match(r"\s+(?:play|book|use)\b", after):
                targets.append("alumni")
        if re.search(r"\bhow\s+many\s+$", before) and booking_context:
            targets.extend(("session", "sessions"))
        if re.search(r"\bhow\s+many\s+$", before) and re.match(r"\s+are\s+there\b", after):
            targets.append("members")
        if schedule_context:
            targets.append("afternoon")
        if rule_context:
            targets.extend(("competition", "equipment", "tournament", "rulebook", "policy", "official", "scope", "identity"))
            if re.match(r"\s+size\b", after):
                targets.append("team")
            if re.search(r"\b(?:minimum|maximum)\b", before) and near("age"):
                targets.append("requirement")
        # The object immediately following a list interrogative is catalog
        # vocabulary. "Available" alone is not evidence for live slots.
        if re.search(r"\b(?:what|which|many|list|show)(?:\s+(?:me|the|pc|studio|any))*\s+$", before):
            if re.match(r"\s+(?:(?:is|are)\s+)?(?:available|in|for|on|does|do)\b", after):
                targets.extend(("games", "equipment"))
        if booking_context and re.search(r"\b(?:what|which)(?:\s+(?:user|required))*\s+$", before):
            targets.append("information")
        if (near("information") or re.search(r"\b(?:how|when|pay|payment|after|make)\b", lower)):
            if re.search(r"\b(?:a|after|for|make|my|the)\s+$", before):
                targets.append("booking")
        if re.search(r"\bwhich(?:\s+studio)?\s+$", before) and re.match(r"\s+(?:has|have|is)\b", after):
            targets.append("zone")
        if re.match(r"\s*(?:are|is|can|may)\b", lower) and permission_context:
            targets.append("drinks")
        if re.match(r"\s*(?:are|is|can|may)\b", lower) and drink_context:
            targets.append("allowed")
        winners = sorted({
            target for target in targets
            if abs(len(observed) - len(target)) <= 1 and osa_distance(observed, target) == 1
        })
        if len(winners) != 1:
            continue
        target = winners[0]
        return CueRecovery(
            text, text[:match.start()] + target + text[match.end():],
            match.group(), target, match.start(), 1, "syntax-anchored task-word recovery",
        )

    # A Thai conjunction is recoverable only as a bridge between operations.
    # This deliberately does not correct short Thai words anywhere in input.
    if _RESOURCE.search(text):
        right_operations = r"(?:จอง(?:ยังไง|อย่างไร)|มีเกม|มีอุปกรณ์|เปิดกี่โมง)"
        for right in re.finditer(right_operations, text):
            prefix = text[:right.start()].rstrip()
            if prefix.endswith(("แล้ว", "และ", "ส่วน")):
                continue
            candidates = []
            for length in (3, 4, 5):
                observed = prefix[-length:]
                preceding = prefix[:-length]
                if not re.fullmatch(r"[\u0e00-\u0e7f]+", observed):
                    continue
                if not any(cue in preceding for cue in ("ราคา", "กี่บาท", "เสียกี่บาท", "มีเกม", "มีอุปกรณ์")):
                    continue
                if osa_distance(observed, "แล้ว") == 1:
                    candidates.append((abs(length - 4), length, observed))
            if candidates:
                _, length, observed = min(candidates)
                start = len(prefix) - length
                return CueRecovery(
                    text, text[:start] + "แล้ว" + text[start + length:],
                    observed, "แล้ว", start, 1, "operation-anchored Thai conjunction recovery",
                )
    return None


def _thai_span(text: str, target: str, anchor: str, max_distance: int,
               start_after: str = "") -> CueRecovery | None:
    if not start_after and target in text:
        return None
    starts: list[int] = []
    if start_after:
        pos = text.find(start_after)
        if pos >= 0:
            start = pos + len(start_after)
            while start < len(text) and text[start].isspace():
                start += 1
            if text[start:].startswith(target):
                return None
            starts.append(start)
    else:
        pos = 0
        while True:
            pos = text.find(anchor, pos)
            if pos < 0:
                break
            starts.append(pos)
            pos += 1
    possibilities: list[tuple[int, int, int, int, str]] = []
    for start in starts:
        if start >= len(text):
            continue
        for length in range(max(2, len(target) - max_distance), len(target) + max_distance + 1):
            observed = text[start:start + length]
            if len(observed) != length or not all("\u0e00" <= ch <= "\u0e7f" for ch in observed):
                continue
            distance = osa_distance(observed, target)
            if 0 < distance <= max_distance:
                # Do not prefer a substitution that leaves the intended final
                # vowel behind: กติกก + า would otherwise become กติกาา.
                leaves_final = int(observed[-1:] != target[-1:] and any(candidate[-1:] == target[-1:] for candidate in (text[start:start + size] for size in range(max(2, len(target) - max_distance), len(target) + max_distance + 1)) if osa_distance(candidate, target) <= max_distance))
                possibilities.append((distance, leaves_final, abs(length - len(target)), start, observed))
    if not possibilities:
        return None
    possibilities.sort()
    best = possibilities[0]
    # Equal best candidates at different positions are ambiguous.
    if any(item[:3] == best[:3] and item[3] != best[3] for item in possibilities[1:]):
        return None
    distance, _, _, start, observed = best
    return CueRecovery(
        raw=text, recovered=text[:start] + target + text[start + len(observed):],
        observed=observed, intended=target, start=start, distance=distance,
        reason="bounded task-cue edit distance",
    )


def detect_intent_cue_recovery(value: str) -> CueRecovery | None:
    if os.getenv("PSU_INTENT_CUE_RECOVERY", "1").casefold() in {"0", "false", "off", "no"}:
        return None
    text = str(value or "")
    if not text or len(text) > 180 or "://" in text:
        return None
    lower = text.casefold()
    from app.pipeline.competition_targets import looks_like_competition_rule_query
    if not looks_like_competition_rule_query(text) and 'คำพูดไม่' not in text:
        candidates = []
        for match in re.finditer(r'คำพู[\u0e00-\u0e7f]{3,6}(?=เหมาะสม)', text):
            observed = match.group()
            if osa_distance(observed, 'คำพูดไม่') == 1:
                candidates.append(match)
        if len(candidates) == 1:
            match = candidates[0]
            return CueRecovery(text, text[:match.start()]+'คำพูดไม่'+text[match.end():],
                               match.group(), 'คำพูดไม่', match.start(), 1,
                               'unique speech-fragment transposition before exact appropriateness topic')
    from app.pipeline.competition_facet_recovery import recover_facet_cue
    facet = recover_facet_cue(text)
    if facet is not None:
        return CueRecovery(text, facet[0], facet[1].original, facet[1].canonical,
                           facet[1].start, facet[1].edits,
                           'unique registered facet span; exact rulebook context')
    # A known rulebook target anchors edits to task words. This cannot invent
    # a game, change its number, or reuse an evaluation question as a phrase.
    from app.pipeline.competition_targets import resolve_competition_targets

    competition_targeted = resolve_competition_targets(text).status in {"exact", "multiple", "unknown_explicit"}
    if resolve_competition_targets(text).status in {'exact', 'multiple'} and re.search(r'กติกา|แข่ง|\b(?:rules?|tournament|competition)\b', text, re.I):
        # Recover a proposition word only when an independent syntax/context
        # anchor survives. Correct real words, negation and game names stay raw.
        anchored_words = (
            ('players', r'\b(?:per\s+team|team\s+size)\b'),
            ('protest', r'\b(?:coach|captain|file|submit|submits|deadline|minutes)\b'),
            ('notes', r'\b(?:bring|hand|leader|captain|referee)\b'),
            ('social', r'\bmedia\b'),
            ('heroes', r'\b(?:minimum|number|many|required)\b'),
            ('settings', r'in.game|\b(?:Stage|Advantage|Timer)\b'),
            ('score', r'\bforfeit\w*\b.*\brecord\w*|\brecord\w*\b.*\bforfeit\w*'),
        )
        for match in _EN_TOKEN.finditer(text):
            observed = match.group().casefold()
            if observed in _VALID_ENGLISH_WORDS or observed in {'no','not','nor','protest','notes','social','heroes','settings'}:
                continue
            winners = {word for word, anchor in anchored_words if re.search(anchor,text,re.I) and osa_distance(observed,word) == 1}
            if len(winners) == 1:
                word = winners.pop()
                return CueRecovery(text,text[:match.start()]+word+text[match.end():],match.group(),word,match.start(),1,'rulebook and syntax anchored proposition-word recovery')
        thai_words = (
            ('ประท้วง','ประ',r'โค้ช|กัปตัน|ยื่น|หลังจบ|ภายใน'),
            ('โน้ต','โน',r'หัวหน้าทีม|กรรมการ|นำ|เอกสาร'),
            ('โซเชียล','โซ',r'เว็บไซต์|คอม|เครื่อง|เข้า|เปิด'),
            ('อุปกรณ์','อุป',r'ตัวเอง|ผู้จัด|เตรียม|นำ'),
            ('ฮีโร่','ฮี',r'อย่างน้อย|กี่ตัว|ต้องมี'),
            ('การตั้งค่า','การต',r'เกม|Round|Timer|Stage|Advantage'),
        )
        for word, anchor, context in thai_words:
            if re.search(context,text,re.I):
                recovered = _thai_span(text,word,anchor,1)
                if recovered is not None:
                    return recovered
    if resolve_competition_targets(text).status == 'exact' and 'อ้างอิง' in text and not re.search(r'ไม่ใช่(?:กฎ|กฏ|กติกา)|not (?:competition |tournament )?rules', text, re.I):
        # A reference verb and exact registered target survive independently.
        # Bootstrap the rule cue before the separate facet pass on the next step.
        recovery = _thai_span(text, 'กติกา', '', 1, start_after='อ้างอิง')
        if recovery is not None:
            return recovery
    if resolve_competition_targets(text).status in {'exact', 'multiple'}:
        # The registered target anchors a long task word, even if no other
        # intact rule cue survives. No game alias, number or real word is edited.
        for match in _EN_TOKEN.finditer(text):
            observed = match.group().casefold()
            if observed not in _VALID_ENGLISH_WORDS and abs(len(observed) - len('tournament')) <= 1 and osa_distance(observed, 'tournament') == 1:
                return CueRecovery(text, text[:match.start()] + 'tournament' + text[match.end():], match.group(), 'tournament', match.start(), 1, 'registered-game-anchored tournament task recovery')
    if competition_targeted or re.search(r"\b(?:timeout|tournament|competition|rulebook)\b", lower):
        recovery = _thai_span(text, "กติกา", "กต", 1)
        if recovery is not None:
            return recovery
    if competition_targeted or re.search(r"\b(?:tournament|competition|overview|timeout|roster)\b", lower):
        for match in _EN_TOKEN.finditer(text):
            observed = match.group().casefold()
            if observed in _VALID_ENGLISH_WORDS or observed in {"rule", "rules", "ruse", "rues", "runes"}:
                continue
            if osa_distance(observed, "rules") == 1 and (len(observed) != 5 or sorted(observed) == sorted("rules")):
                return CueRecovery(text, text[:match.start()] + "rules" + text[match.end():], match.group(), "rules", match.start(), 1, "competition-anchored rule task recovery")
    from app.core.task_frame_recovery import recover_task_frame
    framed = recover_task_frame(text)
    if framed is not None:
        start, observed, target, edits, reason = framed
        return CueRecovery(text, text[:start] + target + text[start + len(observed):], observed, target, start, edits, reason)
    contextual = _contextual_task_cue(text)
    if contextual is not None:
        return contextual
    if re.search(r"\b(?:minimum|maximum)\b", lower) and (
        re.search(r"\b(?:tournament|competition|enter)\b", lower)
    ):
        for match in _EN_TOKEN.finditer(text):
            token = match.group().casefold()
            if token not in _VALID_ENGLISH_WORDS and osa_distance(token, "age") == 1 and _short_grammar_edit_allowed(token, "age"):
                return CueRecovery(text, text[:match.start()] + "age" + text[match.end():],
                                   match.group(), "age", match.start(), 1, "minimum/maximum competition-age qualifier")
    if re.search(r"(?:นาย|นาง|รศ\.|ผศ\.)", text) and "ตำแหน่ง" not in text:
        for match in re.finditer(r"[\u0e00-\u0e7f]{5,9}(?=อะไร)", text):
            token=match.group()
            if 0 < osa_distance(token,"ตำแหน่ง") <= 2:
                return CueRecovery(text,text[:match.start()]+"ตำแหน่ง"+text[match.end():],
                                   token,"ตำแหน่ง",match.start(),osa_distance(token,"ตำแหน่ง"),"person-anchored role operation")
    # Thai task spans need an intact operation anchor. The small lexicon is
    # independent of individual games; dates, resource numbers and names stay raw.
    thai_tasks = []
    if _RESOURCE.search(text):
        thai_tasks.append(("แพงกว่า", "แพง", 1, ""))
        if any(cue in text for cue in ("บาท", "ราคา", "เสีย", "ค่าบริการ")):
            thai_tasks.append(("กี่บาท", "กี่", 1, ""))
    if "เล่นได้" in text:
        thai_tasks.append(("ที่ไหน", "", 1, "เล่นได้"))
    if "คือ" in text and not re.search(r"คือ\s*(?:อะไร|เกมแนว|แนว)", text):
        thai_tasks.append(("เกมอะไร", "", 3, "คือ"))
    if "รอบละ" in text:
        thai_tasks.append(("กี่นาที", "", 3, "รอบละ"))
    if any(word in text for word in ("ส่วนตัว", "สูญหาย", "รับผิดชอบ")):
        thai_tasks.append(("ทรัพย์สิน", "ทรัพย์", 1, ""))
    for target, anchor, distance, after in thai_tasks:
        recovery = _thai_span(text, target, anchor, distance, start_after=after)
        if recovery is not None:
            return recovery
    live_time_context = bool(
        _TIME.search(text)
        or re.search(r"\b(?:right\s+now|now|\d{1,2}\s*(?:am|pm))\b", lower)
    )
    live_resource_context = bool(
        _RESOURCE.search(text)
        or re.search(r"\bslots?\b", lower)
        or any(
            len(token.group()) >= 6 and osa_distance(token.group().casefold(), "cockpit") == 1
            for token in _EN_TOKEN.finditer(text)
        )
    )
    live_context = live_time_context and live_resource_context

    # English tokens have explicit boundaries. A real word with another
    # plausible meaning (for example pay/play) is not silently changed.
    control_context = bool(
        re.search(r"\b(?:what|wat|hat|wht|wha|whar|whay)\b", lower)
        or "confirmation" in lower
    ) and bool(re.search(r"\b(?:does|do|are|for|all|in)\b", lower))
    for match in _EN_TOKEN.finditer(text):
        observed = match.group().casefold()
        if observed in _VALID_ENGLISH_WORDS or observed in {"button", "buttons", "control", "controls", "temporary", "available", "availability", "free", "booked", "vacant"}:
            continue
        target = ""
        if control_context and len(observed) >= 5:
            for control_word in ("button", "buttons", "controls"):
                if observed != control_word and osa_distance(observed, control_word) == 1:
                    target = control_word
                    break
        if not target and live_context and len(observed) >= 3:
            for live_word in ("available", "availability", "free", "booked", "vacant"):
                if osa_distance(observed, live_word) == 1:
                    target = live_word
                    break
        if not target and (
            "temporary" not in lower
            and "suspension" in lower
            and osa_distance(observed, "temporary") == 1
        ):
            target = "temporary"
        if not target:
            continue
        return CueRecovery(
            raw=text,
            recovered=text[:match.start()] + target + text[match.end():],
            observed=match.group(), intended=target, start=match.start(),
            distance=1, reason="bounded English task-cue edit distance",
        )

    if "ปุ่ม" not in text and ("ใช้" in text or "กด" in text or "เคลื่อนที่" in text or "ทำอะไร" in text):
        if "เกม" in text or _RESOURCE.search(text) or "กด" in text:
            for match in re.finditer(r"(?<!\S)[\u0e00-\u0e7f]{2,6}", text):
                for length in (2, 3, 4):
                    observed = match.group()[:length]
                    if not observed or observed[0] not in {"ป", "ุ", "แ"}:
                        continue
                    if osa_distance(observed, "ปุ่ม") == 1:
                        return CueRecovery(
                            raw=text,
                            recovered=text[:match.start()] + "ปุ่ม" + text[match.start() + length:],
                            observed=observed, intended="ปุ่ม", start=match.start(),
                            distance=1, reason="bounded Thai control-cue edit distance",
                        )

    if "เกมอะไรบ้าง" not in text and "มีเกม" in text:
        candidate = _thai_span(text, "เกมอะไรบ้าง", "เกม", 1)
        if candidate and text[:candidate.start].endswith("มี"):
            return candidate

    if (
        not any(term in text for term in _VALID_THAI_PRICE)
        and "ราค" in text
    ):
        candidate = _thai_span(text, "ราคาเท่าไหร่", "ราค", 2)
        if candidate and "เท่า" in candidate.observed:
            return candidate

    if _TIME.search(text) and _RESOURCE.search(text) and "ว่างบ้าง" not in text:
        for anchor in ("เครื่องไหน", "ช่องไหน"):
            if anchor in text:
                candidate = _thai_span(text, "ว่างบ้าง", "", 1, start_after=anchor)
                if candidate and candidate.observed.startswith("ว"):
                    return candidate
    if (
        _RESOURCE.search(text)
        and (_TIME.search(text) or any(term in text for term in ("ตอนนี้", "ตอนี้", "โมง", "บ่าย")))
        and "ว่างไหม" not in text
    ):
        for match in re.finditer(r"ว[\u0e00-\u0e7f]{1,5}(?=\s*(?:ไหม|มั้ย|หรือเปล่า|รึเปล่า|หรือไม่|รึป่าว|หรือป่าว))", text):
            observed = match.group()
            if observed != "ว่า" and osa_distance(observed, "ว่าง") == 1:
                return CueRecovery(
                    raw=text,
                    recovered=text[:match.start()] + "ว่าง" + text[match.end():],
                    observed=observed, intended="ว่าง", start=match.start(),
                    distance=1, reason="bounded Thai live-availability cue edit distance",
                )
    return None


def recover_intent_cue_sequence(value: str) -> tuple[str, tuple[CueRecovery, ...]]:
    """At most three contextual edits, with positions relative to each step."""
    current = value
    recoveries: list[CueRecovery] = []
    edit_budget = 4
    for _ in range(3):
        recovery = detect_intent_cue_recovery(current)
        if recovery is None or recovery.distance > edit_budget:
            break
        recoveries.append(recovery)
        edit_budget -= recovery.distance
        current = recovery.recovered
    return current, tuple(recoveries)


def recover_intent_cues(value: str) -> str:
    return recover_intent_cue_sequence(value)[0]
