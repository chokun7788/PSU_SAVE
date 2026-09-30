# English Localization Review Queue

> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.

- Draft input: `data\locales\en\localization_review_drafts_machine_20260909_verified.jsonl`
- Filter: `penalty`
- Review items: **12**

## Review procedure

1. Compare every English draft with its Thai source, especially prices, time limits, exceptions, and prohibitions.
2. Select only accurate records using the selector shown under each item.
3. Create an approval candidate with `approve`, then run `validate`, then `publish`.
4. Do not approve a wording that changes scope, certainty, names, prices, or conditions.

## Commands after review

Create a candidate from explicit, reviewed selectors (replace the reviewer and selectors):

```powershell
py tools/manage_english_localizations.py approve data\locales\en\localization_review_drafts_machine_20260909_verified.jsonl --output data/locales/en/reviewed_candidate.jsonl --reviewer <reviewer-id> --select <content_id:field>
```

Then validate it before publishing. Publishing builds one atomic English release; it never publishes an individual draft directly.

```powershell
py tools/manage_english_localizations.py validate data/locales/en/reviewed_candidate.jsonl
py tools/manage_english_localizations.py publish data/locales/en/reviewed_candidate.jsonl --build-vector
```

## 1. curated_damage_minor / text

- Selector: `curated_damage_minor:text`
- Category: `penalty`
- Title: ค่าปรับความเสียหายเล็กน้อย
- Source hash: `bd0992c78b992acf8f00f07ff66fa4ce47561d2f733454fde0b830c31dce6c31`

**Thai source**

ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100 – 500 บาท

**English draft**

Minor damages such as stains, water marks, scratches, loose lids, or loose buttons incur a fine of 100–500 THB

## 2. curated_damage_minor / title

- Selector: `curated_damage_minor:title`
- Category: `penalty`
- Title: ค่าปรับความเสียหายเล็กน้อย
- Source hash: `75d11b5d95821057fde24b73bdfc709b113209ab4b8e51d582c16196043a9d5d`

**Thai source**

ค่าปรับความเสียหายเล็กน้อย

**English draft**

Minor damage fine

## 3. curated_damage_moderate / text

- Selector: `curated_damage_moderate:text`
- Category: `penalty`
- Title: ค่าปรับความเสียหายปานกลาง
- Source hash: `7bdefdf965fe3dbd62a3cfbae38a9c3afbb4674c52629ff723b6a4b60beb98d4`

**Thai source**

ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500 – 2,000 บาท

**English draft**

Moderate damage such as broken seats, deep scratches, damaged furniture frames, controllers with stuck buttons, or broken headphone cords must be repaired at actual cost, or between THB 500–2,000

## 4. curated_damage_moderate / title

- Selector: `curated_damage_moderate:title`
- Category: `penalty`
- Title: ค่าปรับความเสียหายปานกลาง
- Source hash: `106954844de358f359cdb0cd97b2c70fa564659060c10769c490967e3d0c66c9`

**Thai source**

ค่าปรับความเสียหายปานกลาง

**English draft**

Medium damage fine

## 5. curated_damage_severe / text

- Selector: `curated_damage_severe:text`
- Category: `penalty`
- Title: ความเสียหายร้ายแรง
- Source hash: `7f12bf75df1a7a6b1f42ca8e0b9ba654036f8940a2d8d99fe63016905aee1cbb`

**Thai source**

ความเสียหายร้ายแรง เช่น เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ จอแตก คอมพิวเตอร์พัง หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

**English draft**

Severe damages, such as furniture rendered unusable, broken monitors, damaged computers, or equipment that cannot be used, must be compensated in full for the value of the assets at prevailing market rates.

## 6. curated_damage_severe / title

- Selector: `curated_damage_severe:title`
- Category: `penalty`
- Title: ความเสียหายร้ายแรง
- Source hash: `e5ef9fbd1053d65f1a4dd562aae9ed43319e125543977c3bc874b4a838a9cd55`

**Thai source**

ความเสียหายร้ายแรง

**English draft**

Severe Damage

## 7. curated_penalty_appeal / text

- Selector: `curated_penalty_appeal:text`
- Category: `penalty`
- Title: ยื่นคำร้องขอพิจารณาใหม่
- Source hash: `260ba18930371abb67aeeb06180437c12a214421f3be212de545549fc2d0ac01`

**Thai source**

หากผู้ใช้งานไม่พอใจการตัดสินใจเกี่ยวกับการลงโทษ สามารถยื่นคำร้องขอการพิจารณาใหม่ได้ภายใน 7 วันหลังจากการถูกลงโทษ

**English draft**

If a user is dissatisfied with the penalty decision, they may submit a request for reconsideration within 7 days after being penalized.

## 8. curated_penalty_appeal / title

- Selector: `curated_penalty_appeal:title`
- Category: `penalty`
- Title: ยื่นคำร้องขอพิจารณาใหม่
- Source hash: `4c11f74d9cc269780c7b5e59fc035c5394a675177fec8ad34595fb62417aeb39`

**Thai source**

ยื่นคำร้องขอพิจารณาใหม่

**English draft**

Submit request for reconsideration

## 9. curated_penalty_temp_suspension / text

- Selector: `curated_penalty_temp_suspension:text`
- Category: `penalty`
- Title: ระงับสิทธิ์ชั่วคราว
- Source hash: `193c9c999bb1f9a645114c81d43d6b588e2246ea4ca31ecddae00889923a979a`

**Thai source**

หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

**English draft**

If a user repeatedly violates rules or engages in aggressive behavior, their account privileges may be suspended for a period of 1 to 7 days, depending on the nature of the violation.

## 10. curated_penalty_temp_suspension / title

- Selector: `curated_penalty_temp_suspension:title`
- Category: `penalty`
- Title: ระงับสิทธิ์ชั่วคราว
- Source hash: `4d10c38f411073ef7199ba4c447b5a9ec74c1e9f9c5ffcda21c918dd66c4ae12`

**Thai source**

ระงับสิทธิ์ชั่วคราว

**English draft**

Temporary Suspension

## 11. curated_penalty_warning_suspension / text

- Selector: `curated_penalty_warning_suspension:text`
- Category: `penalty`
- Title: การลงโทษเมื่อละเมิดกฎ
- Source hash: `93f711742b0e015385151846014cd500fcd9a415215bde66e3923c865ad7a132`

**Thai source**

หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง

**English draft**

If a violation is detected, users will receive a warning and may have their account privileges temporarily or permanently suspended, depending on the severity.

## 12. curated_penalty_warning_suspension / title

- Selector: `curated_penalty_warning_suspension:title`
- Category: `penalty`
- Title: การลงโทษเมื่อละเมิดกฎ
- Source hash: `a1176b09857239199f1f6c5310a397d034146e2743ad875c5149d910d01c3924`

**Thai source**

การลงโทษเมื่อละเมิดกฎ

**English draft**

Penalty for violating rules
