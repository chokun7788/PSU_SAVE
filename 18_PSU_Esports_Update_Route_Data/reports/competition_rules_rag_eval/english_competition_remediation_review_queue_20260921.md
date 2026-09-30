# English Localization Review Queue

> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.

- Draft input: `data\locales\en\localization_review_drafts_competition_remediation_20260921.jsonl`
- Filter: `competition_rules`
- Review items: **8**

## Review procedure

1. Compare every English draft with its Thai source, especially prices, time limits, exceptions, and prohibitions.
2. Select only accurate records using the selector shown under each item.
3. Create an approval candidate with `approve`, then run `validate`, then `publish`.
4. Do not approve a wording that changes scope, certainty, names, prices, or conditions.

## Commands after review

Create a candidate from explicit, reviewed selectors (replace the reviewer and selectors):

```powershell
py tools/manage_english_localizations.py approve data\locales\en\localization_review_drafts_competition_remediation_20260921.jsonl --output data/locales/en/reviewed_candidate.jsonl --reviewer <reviewer-id> --select <content_id:field>
```

Then validate it before publishing. Publishing builds one atomic English release; it never publishes an individual draft directly.

```powershell
py tools/manage_english_localizations.py validate data/locales/en/reviewed_candidate.jsonl
py tools/manage_english_localizations.py publish data/locales/en/reviewed_candidate.jsonl --build-vector
```

## 1. competition_rules_cs2_psu_phuket_2026_s15_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s15_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Source hash: `e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb`

**Thai source**

7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

**English draft**

7. Match schedule

## 2. competition_rules_cs2_psu_phuket_2026_s15_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s15_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Source hash: `e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb`

**Thai source**

7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

**English draft**

7. Match schedule: The bracket will be announced at least one day in advance. Teams must confirm participation before the match begins. Late arrival may result in disqualification.

## 3. competition_rules_cs2_psu_phuket_2026_s36_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s36_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- Source hash: `3975d0dbc770b828fcffc74124f3b8f2e8fee69d4142949f1400ba40c2014c65`

**Thai source**

1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

**English draft**

1. Player conduct

## 4. competition_rules_cs2_psu_phuket_2026_s36_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s36_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- Source hash: `3975d0dbc770b828fcffc74124f3b8f2e8fee69d4142949f1400ba40c2014c65`

**Thai source**

1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

**English draft**

1. Player conduct: Aggressive behaviour, hateful speech (including racial or religious discrimination), and unsportsmanlike conduct are prohibited.

## 5. competition_rules_cs2_psu_phuket_2026_s54_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s54_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 8. ตารางบทลงโทษ (Penalties)
- Source hash: `843f16469f8292351e20a7cee023a3b97b2f7a7410ed37d3f4574f14eb11e887`

**Thai source**

8. ตารางบทลงโทษ (Penalties)

**English draft**

8. Penalty table

## 6. competition_rules_cs2_psu_phuket_2026_s54_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s54_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 8. ตารางบทลงโทษ (Penalties)
- Source hash: `0a758860b24394b8fcb6197d287d26ddd0ee5953a20f3dd531f55f38561833c4`

**Thai source**

8. ตารางบทลงโทษ (Penalties)
การละเมิด
บทลงโทษ
การด่าทอ/ใช้ความรุนแรงทางวาจา
ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
การโกงทุกรูปแบบ
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
ดูสตรีมระหว่างแข่ง
ปรับแพ้ในแมตช์นั้น
หยุดเกมโดยไม่ได้รับอนุญาต
ปรับแพ้ในรอบนั้น
การใช้บัค
ปรับแพ้ในรอบหรือแมตช์นั้น
พฤติกรรมผิดจริยธรรม
ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
เพิกเฉยต่อคำตัดสินของเจ้าหน้าที่
ปรับแพ้ในรอบนั้น / ตัดสิทธิ์
การพิมพ์แชทในเกมที่ไม่เหมาะสม
ปรับแพ้ในรอบหรือแมตช์นั้น
การหมิ่นศาสนา

**English draft**

8. Penalty table:
Violation | Penalty
Abusive or violent language | Warning, then round loss, then disqualification
Cheating of any kind | Round loss or disqualification
Watching a stream during a match | Match loss
Pausing without permission | Round loss
Using a bug | Round or match loss
Unethical conduct | Round loss, then disqualification
Ignoring an official decision | Round loss or disqualification
Inappropriate in-game chat | Round or match loss

## 7. competition_rules_rov_blueket_2025_men_s06_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `a07203d34db7116335af5ea8ac1a610ce04187f6b6c4899cb6d00e15447003a0`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน

**English draft**

4. Competition rules and regulations

## 8. competition_rules_rov_blueket_2025_men_s06_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s06_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน
4.1. กติกาพื้นฐาน
4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น
4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้
* ฝ่ายทีมสีฟ้าอยู่ด้านบน
* ฝ่ายทีมสีเเดงอยู่ข้างล่าง
4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที
4.2. กติกาการแข่งขัน
4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)
4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick
4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ
4.2.4.ในการแข่งขัน ผู้เข้าแข่งขันทุกคนสามารถเลือกเล่นฮีโร่ได้ทั้งหมด
4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น
4.2.6.ห้ามเลือกฮีโร่ซ้ำในการแข่งขัน หรือการกระทำอื่นใดอันทำให้เกิดปัญหาในระบบทุกกรณี
4.3. การหลุดออกจากเกม (Disconnect) และการเริ่มเกมใหม่ (Rematch)
4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ

**English draft**

4. Competition rules and regulations
4.3 Disconnect and rematch
4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one minute each. After that limit, the other team may resume play immediately.
