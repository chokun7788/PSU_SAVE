"""Proposition-scoped extraction from one explicitly named source rulebook.

Concept patterns locate clauses, never supply answers, source IDs or policies.
Unrecognized questions continue through the ordinary evidence pipeline.
"""
from __future__ import annotations
import re
from dataclasses import dataclass
from app.knowledge.localization import approved_localization
from app.pipeline.competition_targets import looks_like_competition_rule_query, resolve_competition_targets
from app.pipeline.competition_presentation import render_rule_reply, source_clause_lines

@dataclass(frozen=True)
class DetailConcept:
    name: str
    games: tuple[str, ...]
    question: str
    source: str
    exclude: str = ''

# Small bilingual proposition vocabulary. No typo-to-whole-question aliases.
CONCEPTS = (
    DetailConcept('scope', ('cs2',), r'ขอบเขต|ใช้กับใคร|(?:who|whom|which participants).{0,40}apply to|rulebook scope', r'ขอบเขตการบังคับใช้|Scope of Application'),
    DetailConcept('version', ('cs2',), r'เวอร์ชัน|game version|แพลตฟอร์ม|ดัดแปลงตัวเกม|\bplatform\b|(?:modif|modification).{0,25}(?:game|client)|(?:game|client).{0,25}modif', r'เวอร์ชันของเกม|latest version.*Steam'),
    DetailConcept('event_duration_venue', ('cs2',), r'แข่ง(?:ขัน)?\s*(?:ทั้งหมด|นาน)?\s*กี่วัน|(?:แข่ง(?:ขัน)?|จัดแข่ง(?:ขัน)?)(?:\s*(?:CS2|Counter-Strike 2))?\s*ที่ไหน|(?:รายการ|การแข่งขัน)(?:\s*(?:CS2|นี้))?\s*(?:จัด(?:ขึ้น)?ที่ไหน|สถานที่)|number of days.{0,35}(?:tournament|competition)|(?:tournament|competition)\s+(?:last|runs?)(?=\s*(?:[?.,;]|and\b|or\b|for\b|$))|(?:tournament|competition)\s+held\b|(?:tournament|competition).{0,25}\b(?:venue|take place)\b', r'การแข่งขันจะแข่งขันทั้งหมด 1 วัน|(?:competition|tournament).{0,55}(?:1 day|one day)'),
    DetailConcept('language', ('cs2',), r'ภาษาอะไร|ภาษา.*ประท้วง|ประท้วง.*ภาษา|which language|official language|(?:protest|objection).{0,45}(?:English|Thai|language)|(?:English|Thai|language).{0,45}(?:protest|objection)', r'ภาษาทางการ|official language'),
    DetailConcept('discord', ('cs2',), r'discord', r'เซิร์ฟเวอร์ Discord|Discord server'),
    DetailConcept('roster_change', ('cs2',), r'เปลี่ยน(?:แปลง)?สมาชิก|เปลี่ยนตัว(?!ละคร)|สลับผู้เล่น|เปลี่ยนรายชื่อ|change (?:team )?members|teams? change|member changes|(?:swap|replace|change).{0,20}(?:players?|starters?)', r'เปลี่ยนแปลงสมาชิก|No team member changes'),
    DetailConcept('team_player_count', ('cs2',), r'ผู้เล่น(?:หลัก|ตัวจริง).{0,20}(?:กี่|จำนวน)|(?:ส่ง|ต้องมี).{0,12}ผู้เล่น.{0,12}(?:กี่|คน)|(?:how many|number of).{0,20}(?:starting players|starters)|(?:starting players|starters).{0,20}(?:how many|number)', r'องค์ประกอบทีม.*ผู้เล่น 5 คน|Team composition.*5 players'),
    DetailConcept('withdrawal', ('cs2',), r'ถอนตัว|withdraw', r'สมาชิกคนใดถอนตัว|If any member withdraws'),
    DetailConcept('team_limit', ('cs2',), r'ลงได้กี่ทีม|ลงแข่ง.*กี่ทีม|how many teams.*(?:player|represent)|represent.*teams', r'ทีมเดียวเท่านั้น|only one team'),
    DetailConcept('eligibility', ('cs2',), r'คุณสมบัติผู้สมัคร|ใครสมัคร|who is eligible|eligibility', r'เปิดรับเฉพาะ|General eligibility'),
    DetailConcept('registration', ('cs2',), r'\bregistration\b|การลงทะเบียน', r'ไม่อนุญาตให้ลงทะเบียน|Registration of players is not permitted', r'deadline|วันที่|กำหนดส่ง|ปิดรับ.*เมื่อ'),
    DetailConcept('roster', ('cs2',), r'\broster\b.{0,20}(?:size|composition|how many|กี่คน)|(?:size|composition|how many|กี่คน).{0,25}\broster\b|(?:^|[,;])\s*roster\s*(?=[,;?]|$)|\broster\s+(?:rules|requirements)\b', r'องค์ประกอบทีม.*ผู้เล่น|Team composition.*players', r'substit|starters|สำรอง|ตัวจริง'),
    DetailConcept('late_registration', ('cs2',), r'หลัง.*ปิดรับสมัคร|ปิดรับสมัคร(?:ไป)?แล้ว|after.*registration.*clos|registration\s+(?:(?:has|is|was)\s+)?closed', r'ไม่อนุญาตให้ลงทะเบียน|Registration of players is not permitted'),
    DetailConcept('series', ('cs2',), r'รอบรอง|รอบชิง|\bsemifinals?\b|\bfinals\b|\bfinal (?:match|round|stage)\b', r'รอบรองชนะเลิศ.*BO3|Semifinals and finals.*BO3'),
    DetailConcept('round_time', ('cs2',), r'เวลาต่อรอบ|freeze time|round time', r'เวลาต่อรอบ.*Freeze time|Round time.*Freeze time'),
    DetailConcept('money_bomb', ('cs2',), r'เงินเริ่มต้น|เวลาระเบิด|starting money|bomb time', r'เงินเริ่มต้น.*เวลาของระเบิด|Initial money.*Bomb time', r'overtime|ต่อเวลา'),
    DetailConcept('rounds', ('cs2',), r'จำนวนรอบสูงสุด|ชนะที่กี่รอบ|maximum rounds|winning threshold', r'จำนวนรอบสูงสุด|Maximum of \d+ rounds'),
    DetailConcept('overtime', ('cs2',), r'ต่อเวลา|overtime', r'การต่อเวลา|Overtime:.*rounds'),
    DetailConcept('map_pool', ('cs2',), r'ใช้แผนที่อะไร|map pool|which maps|maps are used', r'ANCIENT.*ANUBIS.*TRAIN', r'เลือก|selection|veto|ban'),
    DetailConcept('map_tool', ('cs2',), r'เลือกแผนที่.*(?:เว็บ|อะไร)|map selection.*(?:website|tool)|(?:website|tool).*map selection|MAPBAN', r'MAPBAN\.GG'),
    DetailConcept('side', ('cs2',), r'เลือกฝั่ง|sides? (?:are |is )?select|sides selected', r'ดวลมีด|knife round'),
    DetailConcept('technical_pause', ('cs2',), r'technical pause|หยุดเกมทางเทคนิค', r'การหยุดเกมทางเทคนิค|Technical game pauses'),
    DetailConcept('tactical_timeout', ('cs2',), r'tactical timeout|เวลานอก', r'การขอเวลานอก.*Freeze|Tactical timeouts:'),
    DetailConcept('own_equipment', ('cs2','valorant'), r'อุปกรณ์ของตัวเอง|อุปกรณ์.*มา.*ได้|personal equipment|own equipment', r'นำคีย์บอร์ด.*มาเองได้|Players may bring|Self-provided equipment:'),
    DetailConcept('provided_equipment', ('cs2','valorant'), r'ผู้จัด.*(?:เตรียม|ให้)|organizers? (?:provide|prepare)|equipment.*organizers', r'ผู้จัดจะจัดเตรียม|organizers? (?:will )?(?:prepare|provide)', r'โซเชียล|social|ติดตั้ง|install|website'),
    DetailConcept('social_media', ('cs2','valorant'), r'โซเชียล|social media|communication websites', r'ห้ามเข้าโซเชียล|(?:Accessing|access|Access to).*social media'),
    DetailConcept('devices', ('cs2','valorant'), r'โทรศัพท์.*(?:เข้า|เขต|พื้นที่)|(?:bring|allowed|permitted).*phones?|phones?.*(?:area|arena)', r'ห้ามนำโทรศัพท์|Electronic devices:|Mobile phones.*(?:prohibited|not)'),
    DetailConcept('notes', ('cs2','valorant'), r'โน้ต|notes|documents', r'ผู้เล่นห้ามนำโน้ต|Documents and notes:|Players are not allowed to bring notes'),
    DetailConcept('protest', ('cs2',), r'ประท้วง|protests?', r'การประท้วง ต้องยื่น|Protests must be submitted', r'ภาษา|language'),
    DetailConcept('rov_format', ('rov',), r'รูปแบบการแข่งขัน|tournament format|competition format', r'แข่งแบบออฟไลน์|แข่ง Best of 3.*ทุกรอบ|Offline Mode|Each round played as Best of 3'),
    DetailConcept('heroes', ('rov',), r'ฮีโร่.*(?:อย่างน้อย|กี่ตัว)|how many heroes|minimum.*heroes', r'ต้องมีฮีโร่อย่างน้อย|participants must have at least.*heroes'),
    DetailConcept('skins', ('rov','tekken8'), r'สกิน|\bskins?\b', r'สกิน.*(?:Default|มาตรฐาน)|only Default skins|Only standard skins', r'customization|ปรับแต่ง'),
    DetailConcept('rematch', ('rov',), r'First Blood|ขอเริ่มเกมใหม่|restart|rematch', r'First Blood.*(?:2 นาที|2 minutes)', r'force majeure|เหตุสุดวิสัย'),
    DetailConcept('disconnect_quota', ('rov',), r'หลุดเกม.*(?:กี่ครั้ง|กี่นาที)|(?:how many|allowance|quota).*disconnect', r'แต่ละทีมสามารถกดหยุดเกมได้ทีมละ|Each team may pause the game up to'),
    DetailConcept('break', ('rov',), r'เวลาพัก|พักระหว่าง|break between|break time', r'พัก 5 นาที หลังจากจบทุกสองเกม|5-minute break follows every two games'),
    DetailConcept('long_pause', ('rov',), r'(?:หยุด|พัก).*(?:เกิน|มากกว่า).*10 นาที|pause exceeds 10 minutes|pause.*more than 10 minutes', r'หากหยุดพักเกมเกินกว่า 10 นาที|เกมถูกหยุด.*10 นาที|เกมหยุด.*10 นาที|game is paused for more than 10 minutes'),
    DetailConcept('overheating', ('rov',), r'เครื่องร้อน|ความร้อน|overheat', r'ทำให้อุปกรณ์พกพาดังกล่าวเย็นลง|cool down the device'),
    DetailConcept('console', ('tekken8',), r'ใช้เครื่องอะไร|console|platform|เล่นบน', r'ใช้เครื่องเกม PlayStation 5|PlayStation 5 console used'),
    DetailConcept('decider', ('tekken8',), r'เสมอ.*1[-:]1|1[-:]1.*tie|deciding game', r'หากเสมอกันที่ 1-1|If tied at 1-1'),
    DetailConcept('dlc', ('tekken8',), r'\bDLC\b', r'สามารถเลือก ตัวละคร.*DLC|Any character.*DLC'),
    DetailConcept('assist', ('tekken8',), r'\bAssist\b|ระบบช่วยเหลือพิเศษ', r'อนุญาตให้ใช้ ปุ่ม Assist|Assist buttons.*allowed'),
    DetailConcept('tekken_round_count', ('tekken8',), r'แต่ละเกม.{0,18}กี่รอบ|เกมละ.{0,18}กี่รอบ|จำนวนรอบต่อเกม|how many rounds|rounds per game', r'จำนวนรอบต่อเกม|Rounds per game'),
    DetailConcept('tekken_settings', ('tekken8',), r'การตั้งค่า(?:ใน)?เกม|in-game settings|match settings|game settings', r'จำนวนรอบต่อเกม|เวลาแข่งขันต่อรอบ|Rounds per game|Time per round|Advantage:|Stage:'),
    DetailConcept('reconsider', ('tekken8',), r'กรรมการ.*เปลี่ยนคำตัดสิน|referees.*reconsider|reconsider.*decisions', r'กรรมการสามารถพิจารณาเปลี่ยนแปลง|Referees may reconsider'),
    DetailConcept('socd', ('valorant',), r'Snap Tap|SOCD', r'อนุญาตให้ใช้เทคโนโลยี.*(?:Snap Tap|SOCD)|Allowed keyboard technology:.*SOCD'),
    DetailConcept('checkin', ('valorant',), r'รายงานตัว|arrive at the venue|how early.*arrive', r'เวลาการรายงานตัว|Check-in: arrive'),
    DetailConcept('new_content', ('valorant',), r'เอเจนท์ใหม่|แผนที่ใหม่|new agents?|new maps?', r'เอเจนท์ใหม่.*สัปดาห์|แผนที่ใหม่.*สัปดาห์|New (?:agents|maps) may not be used'),
    DetailConcept('display_settings', ('valorant',), r'เลือด|ศพ|Blood|Bodies|FPS|Latency', r'ผู้เล่นต้อง ปิด.*เลือด|ห้ามแสดงกราฟ FPS|Turn OFF Blood'),
    DetailConcept('forfeit_score', ('valorant',), r'ปรับแพ้.*(?:คะแนน|บันทึก)|score.*forfeit|forfeit.*score', r'การปรับแพ้.*13-0|If a forfeit.*13-0'),
    DetailConcept('timeout_carry', ('valorant',), r'(?:Tactical Timeout|เวลานอก).*(?:ต่อเวลา|ทบ|overtime)|(?:quotas?|carry).*overtime', r'เมื่อเข้าสู่ช่วงต่อเวลา.*โควตา|In Overtime.*quotas'),
    DetailConcept('emergency_limits', ('valorant',), r'emergency pause.*(?:limits?|requests?|how many|how long)|(?:limits?|requests?|how many|how long).*emergency pause|หยุดกรณีฉุกเฉิน.*(?:กี่ครั้ง|กี่นาที)', r'ขอได้ 1 ครั้งต่อแผนที่|รวมเวลาทั้งหมดไม่เกิน 10 นาที|One request per map is allowed|Total emergency-pause time may not exceed 10 minutes'),
    DetailConcept('rollback_damage', ('valorant',), r'(?:ย้อนรอบ|roll back|rollback).*(?:ดาเมจ|damage)|(?:ดาเมจ|damage).*(?:ย้อนรอบ|rollback|roll back)', r'หากเกิดบั๊กก่อน.*ดาเมจ|หากมีการทำดาเมจ.*Challenge|If a bug occurs before.*damage|If damage has.*Challenge'),
    DetailConcept('kayo', ('valorant',), r'KAY/O|ZERO/POINT', r'ข้อยกเว้นพิเศษ.*ZERO/POINT|Special exception:.*ZERO/POINT'),
    DetailConcept('elimination_format', ('cs2',), r'คัดออก|รูปแบบทัวร์นาเมนต์|elimination format', r'Single Elimination'),
    DetailConcept('competitive_mode', ('cs2',), r'โหมดการแข่งขัน|competitive mode', r'โหมด Competitive|Competitive mode'),
    DetailConcept('bracket_lateness', ('cs2',), r'สาย(?:การแข่งขัน)?(?:ประกาศ|ล่วงหน้า)|ประกาศสาย|มาสาย|bracket|lateness|team is late', r'สายการแข่งขันจะประกาศ|bracket.*announc'),
    DetailConcept('bug_exploitation', ('cs2','tekken8'), r'\bbugs?\b|\bglitch(?:es)?\b|บัค|บั๊ก', r'ห้ามใช้บัค|ห้ามใช้ Bug|Exploiting.*bugs|Bug or Glitch|bugs or glitches'),
    DetailConcept('watch_streams', ('cs2',), r'ดูสตรีม|watch(?:ing)? live streams?', r'ห้ามผู้เล่นดูสตรีม|Watching streams:'),
    DetailConcept('equipment_quality', ('cs2',), r'รับผิดชอบ.*(?:คุณภาพ|ความพร้อม)|(?:quality|readiness).*equipment|responsible.*equipment|responsible.*quality', r'รับผิดชอบต่อคุณภาพ|responsible for the quality'),
    DetailConcept('custom_display', ('cs2',), r'Brightness|Resolution|Crosshair|ความสว่าง|เป้าเล็ง', r'Brightness.*Resolution.*Crosshair'),
    DetailConcept('macros_scripts', ('cs2','valorant'), r'มาโคร|สคริปต์|\bmacros?\b|\bscripts?\b', r'ห้ามใช้สคริปต์|ห้ามใช้มาโคร|No scripts or macros|Macros.*prohibited'),
    DetailConcept('software_install', ('cs2','valorant'), r'ติดตั้งโปรแกรม|ลงโปรแกรม|install(?:ing)? (?:software|programs?)', r'ห้ามติดตั้งโปรแกรม|(?:not|prohibited).*install|install.*prohibited'),
    DetailConcept('prep_personnel', ('cs2','valorant'), r'(?:เตรียมตัว|Match Prep|match preparation).*(?:กี่คน|players)|(?:how many players|players).*(?:prepare|match prep|match preparation)', r'จำนวนบุคลากร.*6|No more than 6 players|preparation.*6'),
    DetailConcept('competition_food', ('cs2','valorant'), r'กินดื่ม|อาหาร|เครื่องดื่ม|food|drinks?|beverages?', r'น้ำดื่ม.*ภาชนะ.*หมากฝรั่ง|drinking water.*sealed.*chewing gum'),
    DetailConcept('final_authority', ('cs2',), r'คำตัดสิน.*(?:ที่สุด|สุดท้าย)|ผู้จัดเปลี่ยนกฎ|decisions? (?:are |is )?final|organizers?.*amend', r'อำนาจตัดสิน.*ที่สิ้นสุด|decisions.*final'),
    DetailConcept('regulation_timeout', ('valorant',), r'(?:Tactical Timeouts?|เวลานอกทางยุทธวิธี).*(?:รอบปกติ|กี่ครั้ง|regulation|how many)|(?:regulation|how many).*(?:Tactical Timeouts?|เวลานอก)', r'ขอได้ 2 ครั้งต่อแผนที่|2 requests per map|Each team may request up to 2 timeouts'),
    DetailConcept('technical_reasons', ('valorant',), r'(?:Technical Pause|หยุดเกมทางเทคนิค).*(?:ปัญหา|เหตุ|qualify|reasons?)|(?:problems|reasons).*(?:Technical Pause|หยุดเกมทางเทคนิค)', r'ใช้เมื่อมีปัญหา|Used when there are.*(?:malfunctions|disconnections|software)'),
    DetailConcept('ability_boundaries', ('valorant',), r'สกิลนอกขอบ|สกิล.*นอก.*แผนที่|abilities.*outside.*(?:map|boundar)', r'ห้ามใช้สกิล.*นอก|Abilities.*not.*outside|ข้อยกเว้นพิเศษ.*KAY/O|Special exception:.*KAY/O'),
    DetailConcept('cypher_camera', ('valorant',), r'กล้อง Cypher|Cypher cameras?', r'ห้ามวางกล้อง Cypher|Cypher cameras.*must not'),
    DetailConcept('player_boosting', ('valorant',), r'ต่อตัว|กระโดด.*(?:เพื่อน|สูง)|teammates.*boost|boost.*(?:normal|jump)', r'การกระโดดต่อตัว|Using teammates to.*(?:jump|boost)'),
    DetailConcept('character_customization', ('tekken8',), r'ปรับ.*(?:ชุด|ทรงผม|ตัวละคร)|แต่งตัวละคร|customiz|outfits?|hairstyles?', r'ห้าม ปรับแต่งตัวละคร|No character customization|customization.*prohibited|customization.*not allowed'),
    DetailConcept('tekken_disputes', ('tekken8',), r'ข้อพิพาท|แจ้งใคร|ตัดสิน.*ที่สุด|(?:who|whom).*(?:notified|problems)|dispute decision.*final', r'แจ้งผู้จัดการแข่งขันทันที|ข้อโต้แย้ง.*ที่สิ้นสุด|notify.*organizer|disputes.*final|objections.*final'),
    DetailConcept('rov_sides', ('rov',), r'ใคร.*(?:สีฟ้า|เลือกฝั่ง)|(?:which team|who).*(?:blue|chooses.*side)', r'เกมแรก ทีม|In the first match'),
    DetailConcept('rov_lateness', ('rov',), r'เริ่ม.*ช้า|มาสาย|starts?.*late|start.*minutes late|(?:arrive|arrival|team is).{0,15}late', r'ช้าเกินกว่า.*15 นาที|starts.*15 minutes'),
    DetailConcept('runes', ('rov',), r'รูน|\brunes\b|enhancement systems', r'ใส่รูน|Runes and enhancement'),
    DetailConcept('global_ban_pick', ('rov',), r'แบนและเลือกฮีโร่|แบนเลือกฮีโร่|hero ban.*pick|Global Ban/Pick', r'Global Ban/Pick'),
    DetailConcept('force_majeure', ('rov',), r'เน็ตล่มทั้ง|เซิร์ฟเวอร์ล่ม|เหตุสุดวิสัย|area.wide ISP|game server failure', r'เหตุสุดวิสัย|force majeure'),

)

@dataclass(frozen=True)
class CompetitionDetail:
    answer: str
    rows: tuple[dict, ...]
    concepts: tuple[str, ...]
    outcome: str = "answer"
    reasons: tuple[str, ...] = ()

def requested_detail_concepts(query: str, game_id: str) -> tuple[DetailConcept, ...]:
    result = []
    for concept in CONCEPTS:
        concept_query = query
        if concept.name == 'custom_display':
            # Resolution of a dispute is a different proposition from screen
            # resolution. Mask that collocation locally; retain any separately
            # requested display setting elsewhere in the question.
            concept_query = re.sub(r'\b(?:dispute|conflict)\s+resolution\b', '', query, flags=re.I)
        if game_id not in concept.games or not re.search(concept.question, concept_query, re.I):
            continue
        excluded = bool(concept.exclude and re.search(concept.exclude, query, re.I))
        # These qualifiers belong to their proposition. An unrelated requested
        # proposition elsewhere must not suppress a known source clause.
        if concept.name == 'money_bomb' and re.search(r'รอบปกติ|regulation|normal rounds?',query,re.I):
            excluded = False
        if concept.name == 'protest' and re.search(r'ยื่น|ใคร|ภายใน|กี่นาที|file|submit|who|minutes|deadline',query,re.I):
            excluded = False
        if concept.name == 'map_pool' and re.search(r'เว็บอะไร|which website|which tool',query,re.I):
            excluded = False
        if concept.name == 'own_equipment' and re.search(r'รับผิดชอบ|คุณภาพ|ความพร้อม|quality|readiness|responsible',query,re.I):
            if not re.search(r'นำ.*มา.*ได้|มาได้|\bbring\b',query,re.I):
                excluded = True
        if concept.name == 'rematch' and re.search(r'เน็ตล่มทั้ง|เซิร์ฟเวอร์|เหตุสุดวิสัย|ISP|server failure',query,re.I):
            if not re.search(r'First Blood|2 (?:นาที|minutes)',query,re.I):
                excluded = True
        if not excluded:
            result.append(concept)
    return tuple(result)

def lookup_competition_detail(query: str, locale: str) -> CompetitionDetail | None:
    target = resolve_competition_targets(query)
    if target.status != 'exact' or not looks_like_competition_rule_query(query):
        return None
    if re.search(r'minimum age|age requirement|อายุขั้นต่ำ|อายุอย่างน้อย',query,re.I):
        return None  # Eligibility is not evidence of an age threshold.
    concepts = requested_detail_concepts(query, target.targets[0].game_id)
    if not concepts:
        return None
    from app.pipeline.retrieval import load_curated_rows
    rows = sorted((r for r in load_curated_rows() if not r.get('_canonical_projection') and str(r.get('id','')).startswith(target.targets[0].rulebook_id + '_s')), key=lambda r: (int(r.get('section_index') or 0),int(r.get('chunk_index') or 0)))
    selected = []; used = []
    for concept in concepts:
        matches = []
        for row in rows:
            # Never translate at runtime or use hash-stale English text.
            text = approved_localization(row,'text') if locale == 'en' else str(row.get('text') or '')
            clauses = [line for line in source_clause_lines(text or '') if re.search(concept.source,line,re.I)]
            if clauses:
                matches.append((row,clauses))
        if not matches:
            # Partial answers to a multi-proposition request are not accepted.
            return None
        # A settings section with four explicit values is more complete than
        # one reference to R3/60S embedded in a format section.
        row, clauses = max(matches, key=lambda pair: len(pair[1]))
        selected.extend(clauses)
        if row not in used: used.append(row)
    selected = list(dict.fromkeys(selected))
    first = selected[0]
    if target.reason == 'unique_registered_rulebook_edition':
        label = target.targets[0].label
        first = (f'In the recorded {label} rulebook: ' if locale == 'en' else f'ตามเอกสารกติกา {label} ที่มี: ') + first
    if any(c.name == 'event_duration_venue' for c in concepts) and target.reason != 'unique_registered_rulebook_edition':
        label = target.targets[0].label
        first = (f'According to the recorded {label} rulebook: ' if locale == 'en' else f'ตามเอกสารกติกา {label} ที่มี: ') + first
    answer = render_rule_reply(first, selected[1:], used[0], locale)
    if any(c.name == 'rov_lateness' for c in concepts) and re.search(r'มาสาย|arriv', query, re.I):
        # The source regulates a delayed match start, not an independent
        # arrival deadline. Preserve that condition rather than inventing one.
        note = ("This clause applies when the match starts more than 15 minutes after the scheduled time. It does not establish a separate arrival deadline."
                if locale == 'en' else "ข้อนี้กำหนดกรณีเริ่มการแข่งขันช้ากว่าเวลาที่กำหนดเกิน 15 นาที ไม่ได้ระบุเส้นตายการมาถึงแยกต่างหากครับ")
        marker = '\nRulebook:' if locale == 'en' else '\nอ้างอิงจากกติกา:'
        answer = answer.replace(marker, '\n' + note + marker, 1)
    return CompetitionDetail(answer,tuple(used),tuple(c.name for c in concepts))
