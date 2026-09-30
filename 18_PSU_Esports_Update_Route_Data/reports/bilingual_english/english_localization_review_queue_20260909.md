# English Localization Review Queue

> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.

- Draft input: `data\locales\en\localization_review_drafts_machine_20260909_verified.jsonl`
- Filter: `all categories`
- Review items: **615**

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

## 1. competition_rules_cs2_psu_phuket_2026_s01_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s01_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: ภาพรวมเอกสาร
- Source hash: `fa88e9d3bfec10aad1ecdd09982166ee672fbb3680827323abb6b32f5c8c50a3`

**Thai source**

ภาพรวมเอกสาร

**English draft**

Overview of Document

## 2. competition_rules_cs2_psu_phuket_2026_s01_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s01_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: ภาพรวมเอกสาร
- Source hash: `d4f24b1bc5dbe9375fef898ac425dc5f450bede6398205109b8cfcfd5e1a6b6c`

**Thai source**

กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2

**English draft**

Competition Rules and Format for Counter-Strike 2

## 3. competition_rules_cs2_psu_phuket_2026_s01_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s01_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: ภาพรวมเอกสาร
- Source hash: `df6aad2b148f060a177b5ff6e55a4e0e316f146e9ddfdb0b586c2655347f4a50`

**Thai source**

Counter-Strike 2: ภาพรวมเอกสาร

**English draft**

Counter-Strike 2: Overview Document

## 4. competition_rules_cs2_psu_phuket_2026_s02_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s02_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: รายการ PSU Phuket CS2 2026 Tournament
- Source hash: `93685fac4747d8d898370a4b4f7eef687fe8d4363471614906bcb7cd04e6528a`

**Thai source**

รายการ PSU Phuket CS2 2026 Tournament

**English draft**

PSU Phuket CS2 2026 Tournament

## 5. competition_rules_cs2_psu_phuket_2026_s02_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s02_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: รายการ PSU Phuket CS2 2026 Tournament
- Source hash: `93685fac4747d8d898370a4b4f7eef687fe8d4363471614906bcb7cd04e6528a`

**Thai source**

รายการ PSU Phuket CS2 2026 Tournament

**English draft**

PSU Phuket CS2 2026 Tournament

## 6. competition_rules_cs2_psu_phuket_2026_s02_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s02_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: รายการ PSU Phuket CS2 2026 Tournament
- Source hash: `2c308f1284401e59e144789180aa0c924d45a33c142e4794b976981be488d52f`

**Thai source**

Counter-Strike 2: รายการ PSU Phuket CS2 2026 Tournament

**English draft**

Counter-Strike 2: PSU Phuket CS2 2026 Tournament

## 7. competition_rules_cs2_psu_phuket_2026_s03_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s03_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ข้อมูลทั่วไป (General Information)
- Source hash: `9685437ee69604ff2422c2f4645e78b5fa213d940782a20d98a26417ddc924ba`

**Thai source**

1. ข้อมูลทั่วไป (General Information)

**English draft**

General Information

## 8. competition_rules_cs2_psu_phuket_2026_s03_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s03_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ข้อมูลทั่วไป (General Information)
- Source hash: `9685437ee69604ff2422c2f4645e78b5fa213d940782a20d98a26417ddc924ba`

**Thai source**

1. ข้อมูลทั่วไป (General Information)

**English draft**

1. General Information

## 9. competition_rules_cs2_psu_phuket_2026_s03_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s03_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ข้อมูลทั่วไป (General Information)
- Source hash: `b0e93bda3f8336146e84b6034bf92950cdfc9685d8ff0915c98c8e5d2fd6b06b`

**Thai source**

Counter-Strike 2: 1. ข้อมูลทั่วไป (General Information)

**English draft**

Counter-Strike 2: 1. General Information

## 10. competition_rules_cs2_psu_phuket_2026_s04_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s04_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- Source hash: `80114f6fde3b5244569ffb7850f8f177337a9a318ed44914186af5c718fc6c6d`

**Thai source**

1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

**English draft**

Scope of Application

## 11. competition_rules_cs2_psu_phuket_2026_s04_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s04_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- Source hash: `80114f6fde3b5244569ffb7850f8f177337a9a318ed44914186af5c718fc6c6d`

**Thai source**

1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

**English draft**

Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.

## 12. competition_rules_cs2_psu_phuket_2026_s04_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s04_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
- Source hash: `4b8f29a8ad650d11cbb53e3ca82f5c3eb974c4731d556ed763b4f5f9330125da`

**Thai source**

Counter-Strike 2: 1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket

**English draft**

Counter-Strike 2: 1. Scope of Application This rule applies to all players, teams, and staff members participating officially in any Counter-Strike 2 competition organized by PSU Esports Studio - Phuket

## 13. competition_rules_cs2_psu_phuket_2026_s05_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s05_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด
- Source hash: `ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210`

**Thai source**

2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**English draft**

Game Version

## 14. competition_rules_cs2_psu_phuket_2026_s05_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s05_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด
- Source hash: `ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210`

**Thai source**

2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**English draft**

The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

## 15. competition_rules_cs2_psu_phuket_2026_s05_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s05_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด
- Source hash: `512cf27f73f76489507dd768c71c1365955eced1a590a18efdfe7e84dde7fc2a`

**Thai source**

Counter-Strike 2: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

**English draft**

Counter-Strike 2: Version 2. All competitions will use the latest version of CS2 on the Steam platform. Unauthorized game modifications are strictly prohibited.

## 16. competition_rules_cs2_psu_phuket_2026_s06_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s06_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- Source hash: `9dcde01cab2df6545d94263708252debad7085517b5eaefa68e7eba05d6b4f0a`

**Thai source**

3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

**English draft**

Language: The official language of competition is Thai. All communication, protests, and reporting must be in Thai, unless otherwise specified.

## 17. competition_rules_cs2_psu_phuket_2026_s06_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s06_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- Source hash: `9dcde01cab2df6545d94263708252debad7085517b5eaefa68e7eba05d6b4f0a`

**Thai source**

3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

**English draft**

Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.

## 18. competition_rules_cs2_psu_phuket_2026_s06_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s06_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- Source hash: `821c1620b9dbd124345318d746cd1e72cc3f70c7e9e0844f4008e16dd142ce5a`

**Thai source**

Counter-Strike 2: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

**English draft**

Counter-Strike 2: 3. The official language of competition is Thai. All communication, protests, and reporting must be in Thai, unless otherwise specified

## 19. competition_rules_cs2_psu_phuket_2026_s07_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s07_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การจับฉลากและตารางเวลา
- Source hash: `03c83895f535584c982114afd06036c01c4aeaa52eff053de35c59eb97fa5abd`

**Thai source**

4. การจับฉลากและตารางเวลา

**English draft**

Drawing of lots and schedule

## 20. competition_rules_cs2_psu_phuket_2026_s07_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s07_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การจับฉลากและตารางเวลา
- Source hash: `03c83895f535584c982114afd06036c01c4aeaa52eff053de35c59eb97fa5abd`

**Thai source**

4. การจับฉลากและตารางเวลา

**English draft**

Drawing of lots and schedule

## 21. competition_rules_cs2_psu_phuket_2026_s07_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s07_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การจับฉลากและตารางเวลา
- Source hash: `562ed3dfaf2b0a644e8c322cbc58eb790686a328b4f502fb23dd78212df98c2b`

**Thai source**

Counter-Strike 2: 4. การจับฉลากและตารางเวลา

**English draft**

Counter-Strike 2: 4. Draw and Schedule

## 22. competition_rules_cs2_psu_phuket_2026_s08_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s08_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Source hash: `856af72e828b9f8d8aa425f433a1bb58838eb4a64c64d10434bdab7774510086`

**Thai source**

1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Competition will be held for one day at PSU Esports Studio - Phuket, Chulalongkorn University Phuket Campus

## 23. competition_rules_cs2_psu_phuket_2026_s08_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s08_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Source hash: `856af72e828b9f8d8aa425f433a1bb58838eb4a64c64d10434bdab7774510086`

**Thai source**

1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

The competition will be held for a total of 1 day at the PSU Esports Studio - Phuket, King Chulalongkorn Memorial University Phuket Campus.

## 24. competition_rules_cs2_psu_phuket_2026_s08_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s08_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Source hash: `58055b0606ce8255fe880f9b56506a1d579e1c6cb486f5aa67e2fe4615809cb2`

**Thai source**

Counter-Strike 2: 1. การแข่งขันจะแข่งขันทั้งหมด 1 วัน แข่งขัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Counter-Strike 2: 1. The competition will be held for a total of 1 day at the PSU Esports Studio - Phuket, Songklanagarindr University Phuket Campus

## 25. competition_rules_cs2_psu_phuket_2026_s09_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s09_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- Source hash: `f4222e5830380a50c2d1d694553511373cefe0a334f2021a96834a69c29b58f4`

**Thai source**

5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

**English draft**

Communication: All participants must use the Discord server designated by the Center

## 26. competition_rules_cs2_psu_phuket_2026_s09_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s09_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- Source hash: `f4222e5830380a50c2d1d694553511373cefe0a334f2021a96834a69c29b58f4`

**Thai source**

5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

**English draft**

Communication: All participants must use the Discord server designated by the Center.

## 27. competition_rules_cs2_psu_phuket_2026_s09_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s09_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด
- Source hash: `4ca49da3b3c31b9a8bf397ab377cce01e41a819bd1aa534b414c81f85781b099`

**Thai source**

Counter-Strike 2: 5. การสื่อสาร ผู้เข้าร่วมทุกคนต้องใช้เซิร์ฟเวอร์ Discord ที่ทางศูนย์เป็นผู้กำหนด

**English draft**

Counter-Strike 2: 5. Communication All participants must use the Discord server set by the Center

## 28. competition_rules_cs2_psu_phuket_2026_s10_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s10_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. ข้อจำกัด
- Source hash: `4fdd0fc36366c621e15e0f5eb228d8d7406541875a84f5bb5c853dce943af066`

**Thai source**

6. ข้อจำกัด

**English draft**

Limitations

## 29. competition_rules_cs2_psu_phuket_2026_s10_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s10_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. ข้อจำกัด
- Source hash: `4fdd0fc36366c621e15e0f5eb228d8d7406541875a84f5bb5c853dce943af066`

**Thai source**

6. ข้อจำกัด

**English draft**

Limitations

## 30. competition_rules_cs2_psu_phuket_2026_s10_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s10_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. ข้อจำกัด
- Source hash: `005141afa47a304c8d44ac7c6a0bef1e77d3fd6090fe21a836b3b832a8be2393`

**Thai source**

Counter-Strike 2: 6. ข้อจำกัด

**English draft**

Counter-Strike 2: 6. Limitations

## 31. competition_rules_cs2_psu_phuket_2026_s11_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s11_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน
- Source hash: `8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f`

**Thai source**

1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

**English draft**

Must not change team members during the competition period

## 32. competition_rules_cs2_psu_phuket_2026_s11_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s11_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน
- Source hash: `8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f`

**Thai source**

1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

**English draft**

No team member changes are allowed during the competition period

## 33. competition_rules_cs2_psu_phuket_2026_s11_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s11_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน
- Source hash: `c10b467746c225b280e962d885b32fa316bfe5b7fe801e908be6e6fe77438321`

**Thai source**

Counter-Strike 2: 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

**English draft**

Counter-Strike 2: 1. No team member changes are allowed during the competition period

## 34. competition_rules_cs2_psu_phuket_2026_s12_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s12_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร
- Source hash: `56f159165124fb5c433d9da536d3669eebff814160d8989db967a037ee80dbb5`

**Thai source**

2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**English draft**

Registration of players not permitted after enrollment closes

## 35. competition_rules_cs2_psu_phuket_2026_s12_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s12_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร
- Source hash: `56f159165124fb5c433d9da536d3669eebff814160d8989db967a037ee80dbb5`

**Thai source**

2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**English draft**

Registration of players is not permitted after the registration period has closed.

## 36. competition_rules_cs2_psu_phuket_2026_s12_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s12_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร
- Source hash: `d1d4878d103cd1eb6c786db303680b421574b3b15f607db74ab5e51f30c69c67`

**Thai source**

Counter-Strike 2: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

**English draft**

Counter-Strike 2: 2. No registration of players allowed after enrollment closes

## 37. competition_rules_cs2_psu_phuket_2026_s13_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s13_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์
- Source hash: `80cdf54fbecd40b57ce50273a1e091c2af8c5c36e6c6ce1deb5d89890a3c088c`

**Thai source**

3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์

**English draft**

If any member withdraws, the team may be disqualified

## 38. competition_rules_cs2_psu_phuket_2026_s13_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s13_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์
- Source hash: `80cdf54fbecd40b57ce50273a1e091c2af8c5c36e6c6ce1deb5d89890a3c088c`

**Thai source**

3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์

**English draft**

If any member withdraws, the team may be disqualified.

## 39. competition_rules_cs2_psu_phuket_2026_s13_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s13_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์
- Source hash: `7bb284b1d63b27559e8804ab7996d61cff8a69e66f1eecc3127d9b85b99435bb`

**Thai source**

Counter-Strike 2: 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์

**English draft**

Counter-Strike 2: 3. If any member withdraws, the team may be disqualified

## 40. competition_rules_cs2_psu_phuket_2026_s14_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s14_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น
- Source hash: `70397e8766f670250215c8ecd5e313130b39aeda90d082e5c18c61c45fabd667`

**Thai source**

4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

**English draft**

Players may compete under only one team name.

## 41. competition_rules_cs2_psu_phuket_2026_s14_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s14_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น
- Source hash: `70397e8766f670250215c8ecd5e313130b39aeda90d082e5c18c61c45fabd667`

**Thai source**

4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

**English draft**

Players may compete under only one team.

## 42. competition_rules_cs2_psu_phuket_2026_s14_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s14_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น
- Source hash: `6d8043fbd03e94c7403d5ef14ad02c6bfc6fd37b991d638e66f6d52756848f94`

**Thai source**

Counter-Strike 2: 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

**English draft**

Counter-Strike 2: 4. Players may compete under only one team at a time

## 43. competition_rules_cs2_psu_phuket_2026_s15_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s15_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Source hash: `e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb`

**Thai source**

7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

**English draft**

Competition Time

## 44. competition_rules_cs2_psu_phuket_2026_s15_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s15_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Source hash: `e8cd893c7817cfc261bf0b10f845b2163be1141c04905b8bc974872008a17deb`

**Thai source**

7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

**English draft**

Competition time: The tournament schedule will be announced at least one day in advance. Participants must confirm their attendance before each match begins. Late arrivals may be disqualified.

## 45. competition_rules_cs2_psu_phuket_2026_s15_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s15_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Source hash: `48d84f965bb299a7a88296478b597d84d7f65ee0aee35bd965a3261205082e0f`

**Thai source**

Counter-Strike 2: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

**English draft**

Counter-Strike 2: 7. Match Time: The tournament schedule will be announced at least one day in advance. Participants must confirm their attendance before each match begins. Being late may result in disqualification.

## 46. competition_rules_cs2_psu_phuket_2026_s16_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s16_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. คุณสมบัติของทีมและผู้เล่น
- Source hash: `5527f8f9efba00fdbbf9aff633f4d46208fbb2931630780f6c58ded968189053`

**Thai source**

2. คุณสมบัติของทีมและผู้เล่น

**English draft**

Team and Player Qualifications

## 47. competition_rules_cs2_psu_phuket_2026_s16_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s16_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. คุณสมบัติของทีมและผู้เล่น
- Source hash: `5527f8f9efba00fdbbf9aff633f4d46208fbb2931630780f6c58ded968189053`

**Thai source**

2. คุณสมบัติของทีมและผู้เล่น

**English draft**

Team and player qualifications

## 48. competition_rules_cs2_psu_phuket_2026_s16_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s16_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. คุณสมบัติของทีมและผู้เล่น
- Source hash: `63e20264d85637edb7d03161d5b21ca8658a0d4ee7481d3b69ca28b9afcb3fc3`

**Thai source**

Counter-Strike 2: 2. คุณสมบัติของทีมและผู้เล่น

**English draft**

Counter-Strike 2: Team and Player Qualifications

## 49. competition_rules_cs2_psu_phuket_2026_s17_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s17_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น
- Source hash: `f4e9682157dee0ebab12248f2c3523189e2aaf9e51e1be010b1e795ab100cf1d`

**Thai source**

1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

**English draft**

General Qualifications: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus

## 50. competition_rules_cs2_psu_phuket_2026_s17_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s17_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น
- Source hash: `f4e9682157dee0ebab12248f2c3523189e2aaf9e51e1be010b1e795ab100cf1d`

**Thai source**

1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

**English draft**

General eligibility: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus.

## 51. competition_rules_cs2_psu_phuket_2026_s17_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s17_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น
- Source hash: `cc8dc135aed18a9ac60e840bf6ee9d4aefcc1255aa9ce5d5fd046a68670a640a`

**Thai source**

Counter-Strike 2: 1. คุณสมบัติทั่วไป เปิดรับเฉพาะนักศึกษาที่กำลังศึกษาอยู่ในมหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ตเท่านั้น

**English draft**

Counter-Strike 2: 1. General Requirements Open only to undergraduate students currently enrolled at Prince of Songkla University, Phuket Campus

## 52. competition_rules_cs2_psu_phuket_2026_s18_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s18_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Source hash: `66a82e8d6dc8fafb953a8b0eb1128e4eefc7c5e02579843c9eb55241e107b0b2`

**Thai source**

2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**English draft**

Team Composition Each team consists of 5 players

## 53. competition_rules_cs2_psu_phuket_2026_s18_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s18_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Source hash: `66a82e8d6dc8fafb953a8b0eb1128e4eefc7c5e02579843c9eb55241e107b0b2`

**Thai source**

2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**English draft**

Team composition Each team consists of 5 players

## 54. competition_rules_cs2_psu_phuket_2026_s18_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s18_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Source hash: `283fd05e931f39f9ad75bb0029305ef8cd547854d13bcbee72968b5da0469d7f`

**Thai source**

Counter-Strike 2: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

**English draft**

Counter-Strike 2: Team Composition Each team consists of 5 players

## 55. competition_rules_cs2_psu_phuket_2026_s19_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s19_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. รูปแบบการแข่งขัน
- Source hash: `ecdce670141f9ba53c27893ec8aed3c23c14ffa1ab4ad331e8e73c1292260680`

**Thai source**

3. รูปแบบการแข่งขัน

**English draft**

Competition Format

## 56. competition_rules_cs2_psu_phuket_2026_s19_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s19_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. รูปแบบการแข่งขัน
- Source hash: `ecdce670141f9ba53c27893ec8aed3c23c14ffa1ab4ad331e8e73c1292260680`

**Thai source**

3. รูปแบบการแข่งขัน

**English draft**

Competition Format

## 57. competition_rules_cs2_psu_phuket_2026_s19_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s19_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. รูปแบบการแข่งขัน
- Source hash: `d11f57dc8380b2710bff327735bdb65c98b525860bfe6112306b5fbc9d20c84b`

**Thai source**

Counter-Strike 2: 3. รูปแบบการแข่งขัน

**English draft**

Counter-Strike 2: Format 3

## 58. competition_rules_cs2_psu_phuket_2026_s20_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s20_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รูปแบบทัวร์นาเมนต์ Single Elimination
- Source hash: `1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32`

**Thai source**

1. รูปแบบทัวร์นาเมนต์ Single Elimination

**English draft**

Tournament Format: Single Elimination

## 59. competition_rules_cs2_psu_phuket_2026_s20_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s20_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รูปแบบทัวร์นาเมนต์ Single Elimination
- Source hash: `1339343b43374e1293d695f53415de6d06a32ce61c5f4d51802f6fc081f16f32`

**Thai source**

1. รูปแบบทัวร์นาเมนต์ Single Elimination

**English draft**

Tournament format: Single Elimination

## 60. competition_rules_cs2_psu_phuket_2026_s20_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s20_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รูปแบบทัวร์นาเมนต์ Single Elimination
- Source hash: `b41f5800fd7bdc96753f2c1595f28a37e6cee89f1e135a9ddb096241d44a9b67`

**Thai source**

Counter-Strike 2: 1. รูปแบบทัวร์นาเมนต์ Single Elimination

**English draft**

Counter-Strike 2: Tournament Format - Single Elimination

## 61. competition_rules_cs2_psu_phuket_2026_s21_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s21_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)
- Source hash: `ddfb563ee4319316fdedc158e803a02e81599fd7b5f4f5b6b9a01bef88afa9da`

**Thai source**

1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)

**English draft**

Semifinals and Finals: Best of 3 (BO3)

## 62. competition_rules_cs2_psu_phuket_2026_s21_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s21_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)
- Source hash: `ddfb563ee4319316fdedc158e803a02e81599fd7b5f4f5b6b9a01bef88afa9da`

**Thai source**

1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)

**English draft**

Semifinals and finals: Best of 3 (BO3)

## 63. competition_rules_cs2_psu_phuket_2026_s21_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s21_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)
- Source hash: `7240050525904d2345ec05f0eace6929562a8623e374e24a92f61ee93977e714`

**Thai source**

Counter-Strike 2: 1. รอบรองชนะเลิศ และชิงชนะเลิศ: Best of 3 (BO3)

**English draft**

Counter-Strike 2: Round 1 - Semi-Finals and Finals: Best of 3 (BO3)

## 64. competition_rules_cs2_psu_phuket_2026_s22_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s22_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าในเกม
- Source hash: `a07af242c0fd76fe2f4cb00c1e403900559ef23e5cf9843ed1f0e3069330b8c9`

**Thai source**

2. การตั้งค่าในเกม

**English draft**

Game Settings

## 65. competition_rules_cs2_psu_phuket_2026_s22_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s22_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าในเกม
- Source hash: `a07af242c0fd76fe2f4cb00c1e403900559ef23e5cf9843ed1f0e3069330b8c9`

**Thai source**

2. การตั้งค่าในเกม

**English draft**

Game Settings

## 66. competition_rules_cs2_psu_phuket_2026_s22_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s22_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าในเกม
- Source hash: `ed7cb1acda68cfbaa1719b22c5141fe068c6488f4c196ca0387c9ecfe3128651`

**Thai source**

Counter-Strike 2: 2. การตั้งค่าในเกม

**English draft**

Counter-Strike 2: 2. Game Settings

## 67. competition_rules_cs2_psu_phuket_2026_s23_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s23_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. โหมด Competitive (5v5)
- Source hash: `224e078d0eac7d0f4c746c53e478ee4cf6d6c30d3be8ce224c0088dd309e6470`

**Thai source**

1. โหมด Competitive (5v5)

**English draft**

Competitive Mode (5v5)

## 68. competition_rules_cs2_psu_phuket_2026_s23_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s23_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. โหมด Competitive (5v5)
- Source hash: `224e078d0eac7d0f4c746c53e478ee4cf6d6c30d3be8ce224c0088dd309e6470`

**Thai source**

1. โหมด Competitive (5v5)

**English draft**

Competitive mode (5v5)

## 69. competition_rules_cs2_psu_phuket_2026_s23_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s23_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. โหมด Competitive (5v5)
- Source hash: `4c2e668f4a08ee39e8b2135eed458db367f4188265a5f140ae23c2141dc0ff37`

**Thai source**

Counter-Strike 2: 1. โหมด Competitive (5v5)

**English draft**

Counter-Strike 2: 1. Competitive Mode (5v5)

## 70. competition_rules_cs2_psu_phuket_2026_s24_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s24_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- Source hash: `84e20b2eaecd14edd6f3af44e35bc7f028c75f09ea0ac0e8476a42e416dfb0d6`

**Thai source**

2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที

**English draft**

Round duration: 1 minute and 55 seconds | Freeze time: 15 seconds

## 71. competition_rules_cs2_psu_phuket_2026_s24_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s24_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- Source hash: `84e20b2eaecd14edd6f3af44e35bc7f028c75f09ea0ac0e8476a42e416dfb0d6`

**Thai source**

2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที

**English draft**

Match duration per round: 1 minute and 55 seconds | Freeze time: 15 seconds

## 72. competition_rules_cs2_psu_phuket_2026_s24_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s24_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที
- Source hash: `22d3f6f69c58d341348fd2e3ae24711f0cf992a2963b68a570f5843c47efa0c8`

**Thai source**

Counter-Strike 2: 2. เวลาต่อรอบ 1:55 นาที | Freeze time: 15 วินาที

**English draft**

Counter-Strike 2: Round duration 1:55 minutes | Freeze time: 15 seconds

## 73. competition_rules_cs2_psu_phuket_2026_s25_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s25_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที
- Source hash: `a067fdf5bfb6523fe9f699bba90b621043a0ff3b1d3684c40c5a104175ec46c8`

**Thai source**

3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

**English draft**

Initial Money: $800 | Bomb Duration: 40 seconds

## 74. competition_rules_cs2_psu_phuket_2026_s25_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s25_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที
- Source hash: `a067fdf5bfb6523fe9f699bba90b621043a0ff3b1d3684c40c5a104175ec46c8`

**Thai source**

3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

**English draft**

Initial money: $800 | Bomb time: 40 seconds

## 75. competition_rules_cs2_psu_phuket_2026_s25_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s25_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที
- Source hash: `dc857ccf582cc9ae069868b76e97ea34f30e201094bea5ea22a9965188fea659`

**Thai source**

Counter-Strike 2: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

**English draft**

Counter-Strike 2: Starting money $800 | Bomb timer: 40 seconds

## 76. competition_rules_cs2_psu_phuket_2026_s26_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s26_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- Source hash: `da8de3baffba27c188f5111ff8755d23059849bf8c05a7fa1f9755a91c04afee`

**Thai source**

4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน

**English draft**

Maximum of 24 rounds (12 rounds per team). Winner is the team that reaches 13 rounds first.

## 77. competition_rules_cs2_psu_phuket_2026_s26_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s26_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- Source hash: `da8de3baffba27c188f5111ff8755d23059849bf8c05a7fa1f9755a91c04afee`

**Thai source**

4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน

**English draft**

Maximum of 24 rounds (12 rounds per team). The winner is the team that reaches 13 rounds first.

## 78. competition_rules_cs2_psu_phuket_2026_s26_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s26_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน
- Source hash: `8b26d50cb783c1b4cd32bd46cdb5d1d1547c842b4b0a6d9e0566b4d642c494dc`

**Thai source**

Counter-Strike 2: 4. จำนวนรอบสูงสุด 24 รอบ (ฝั่งละ 12 รอบ) | ผู้ชนะคือทีมที่ได้ 13 รอบก่อน

**English draft**

Counter-Strike 2: 4. Maximum rounds of 24 (12 rounds per team) | The winning team is the first to win 13 rounds

## 79. competition_rules_cs2_psu_phuket_2026_s27_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s27_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง
- Source hash: `28b1fe38d88dc3f6e98e68f82175486d7bfc34469b99a405a3e9dff2a4b736ee`

**Thai source**

5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

**English draft**

Time Extension: 3 rounds per team (total of 6), whoever wins 4 out of 6 rounds first wins. Starting prize pool of $10,000 per time slot with no limit on number of slots.

## 80. competition_rules_cs2_psu_phuket_2026_s27_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s27_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง
- Source hash: `28b1fe38d88dc3f6e98e68f82175486d7bfc34469b99a405a3e9dff2a4b736ee`

**Thai source**

5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

**English draft**

Time extension: 3 rounds per side (total of 6). The team winning 4 out of 6 rounds first wins. Starting prize pool: $10,000 per match, unlimited number of matches.

## 81. competition_rules_cs2_psu_phuket_2026_s27_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s27_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง
- Source hash: `8ef7b863d7e4b819b62e385b791dd39c0540022686bac597f6cb4feb95e80177`

**Thai source**

Counter-Strike 2: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

**English draft**

Counter-Strike 2: 5. Time Extension - 3 rounds per team (total of 6), first to win 4 out of 6 rounds wins; starting prize pool of $10,000 with unlimited number of extensions

## 82. competition_rules_cs2_psu_phuket_2026_s28_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s28_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. แผนที่ในการแข่งขัน
- Source hash: `bd9c1ea4485ea301d72964266d4703b55264b5df61090be10c0196b7a1a68d2e`

**Thai source**

3. แผนที่ในการแข่งขัน

**English draft**

Map in Competition

## 83. competition_rules_cs2_psu_phuket_2026_s28_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s28_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. แผนที่ในการแข่งขัน
- Source hash: `bd9c1ea4485ea301d72964266d4703b55264b5df61090be10c0196b7a1a68d2e`

**Thai source**

3. แผนที่ในการแข่งขัน

**English draft**

Map rotation

## 84. competition_rules_cs2_psu_phuket_2026_s28_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s28_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. แผนที่ในการแข่งขัน
- Source hash: `3d29803f6498ee92ae1f667d9fb95e328af9bf7f6897f5f78f04f747863fe75e`

**Thai source**

Counter-Strike 2: 3. แผนที่ในการแข่งขัน

**English draft**

Counter-Strike 2: 3. Maps in Competition

## 85. competition_rules_cs2_psu_phuket_2026_s29_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s29_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN
- Source hash: `ccc38b2b2e1565a6c6b166892f74b035bf75c1968fad122bd170e0f74f95da2d`

**Thai source**

1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

**English draft**

Map Rotation Rules

## 86. competition_rules_cs2_psu_phuket_2026_s29_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s29_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN
- Source hash: `ccc38b2b2e1565a6c6b166892f74b035bf75c1968fad122bd170e0f74f95da2d`

**Thai source**

1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

**English draft**

ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

## 87. competition_rules_cs2_psu_phuket_2026_s29_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s29_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN
- Source hash: `de7c3b3d8600351464bc89508ceb6fbabad54a12000911b4f37d1e5808e89e10`

**Thai source**

Counter-Strike 2: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

**English draft**

Counter-Strike 2: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

## 88. competition_rules_cs2_psu_phuket_2026_s30_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s30_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ขั้นตอนการดำเนินการแข่งขัน
- Source hash: `6df864ca679cc01f16e23b1fdd670fbe215d25b5b03cb89d0118c7bc8f2dfb93`

**Thai source**

4. ขั้นตอนการดำเนินการแข่งขัน

**English draft**

Section Title

## 89. competition_rules_cs2_psu_phuket_2026_s30_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s30_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ขั้นตอนการดำเนินการแข่งขัน
- Source hash: `6df864ca679cc01f16e23b1fdd670fbe215d25b5b03cb89d0118c7bc8f2dfb93`

**Thai source**

4. ขั้นตอนการดำเนินการแข่งขัน

**English draft**

Step-by-step competition procedure

## 90. competition_rules_cs2_psu_phuket_2026_s30_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s30_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ขั้นตอนการดำเนินการแข่งขัน
- Source hash: `1386378a3724c6a2454c9709c042e3555f1480d47e65830e6ee244e0b9564545`

**Thai source**

Counter-Strike 2: 4. ขั้นตอนการดำเนินการแข่งขัน

**English draft**

Counter-Strike 2: Step-by-step Competition Procedure

## 91. competition_rules_cs2_psu_phuket_2026_s31_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s31_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การเลือกแผนที่ ใช้ MAPBAN.GG
- Source hash: `6fa3c51fd60f143c256813850494c33ff552e59d7c1693ef6d4771d5bc2c8988`

**Thai source**

1. การเลือกแผนที่ ใช้ MAPBAN.GG

**English draft**

Map Selection: Use MAPBAN.GG

## 92. competition_rules_cs2_psu_phuket_2026_s31_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s31_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การเลือกแผนที่ ใช้ MAPBAN.GG
- Source hash: `6fa3c51fd60f143c256813850494c33ff552e59d7c1693ef6d4771d5bc2c8988`

**Thai source**

1. การเลือกแผนที่ ใช้ MAPBAN.GG

**English draft**

Map selection uses MAPBAN.GG

## 93. competition_rules_cs2_psu_phuket_2026_s31_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s31_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. การเลือกแผนที่ ใช้ MAPBAN.GG
- Source hash: `42f3173d7b53f670f78b5dfde2deb131537d771ff56695978aababd3e4130ee9`

**Thai source**

Counter-Strike 2: 1. การเลือกแผนที่ ใช้ MAPBAN.GG

**English draft**

Counter-Strike 2: 1. Map Selection Using MAPBAN.GG

## 94. competition_rules_cs2_psu_phuket_2026_s32_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s32_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง
- Source hash: `eecbf0e707257b697af7e64abd8914ae317396b422f39aa525551ad6cb63650c`

**Thai source**

2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง

**English draft**

Side Selection: Use a blade duel to determine sides

## 95. competition_rules_cs2_psu_phuket_2026_s32_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s32_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง
- Source hash: `eecbf0e707257b697af7e64abd8914ae317396b422f39aa525551ad6cb63650c`

**Thai source**

2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง

**English draft**

Team selection uses a duel with swords to determine sides

## 96. competition_rules_cs2_psu_phuket_2026_s32_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s32_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง
- Source hash: `bb7efddb2c19b9fa5b201abe8a014dd61278c0a289289d8f0397a53abd6df24d`

**Thai source**

Counter-Strike 2: 2. การเลือกฝั่ง ใช้การแข่งดวลมีดเพื่อเลือกฝั่ง

**English draft**

Counter-Strike 2: 2. Team Selection Using Sword Duel

## 97. competition_rules_cs2_psu_phuket_2026_s33_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s33_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
- Source hash: `9ebd1ac76d24288a84613462f125dd9ac105d4ee5797eb263280fffc11163539`

**Thai source**

3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

**English draft**

Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

## 98. competition_rules_cs2_psu_phuket_2026_s33_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s33_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
- Source hash: `9ebd1ac76d24288a84613462f125dd9ac105d4ee5797eb263280fffc11163539`

**Thai source**

3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

**English draft**

Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

## 99. competition_rules_cs2_psu_phuket_2026_s33_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s33_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
- Source hash: `d3414ef42f54d8590aabddc7ae86c9a41fb9c884fb4e16257e8e1ebd22288b8a`

**Thai source**

Counter-Strike 2: 3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที

**English draft**

Counter-Strike 2: 3. Technical game pause - each team may pause the game up to two times, each for no more than 10 minutes. If any technical issues arise, teams must immediately notify the referees.

## 100. competition_rules_cs2_psu_phuket_2026_s34_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s34_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- Source hash: `3e86c57a164675158ddcf0d58b78e6a108bd74abedd97a4bb03a7757a849f8e1`

**Thai source**

4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

**English draft**

Requesting Extra Time - Each team may request up to 4 extensions, each lasting 30 seconds, during Freeze time

## 101. competition_rules_cs2_psu_phuket_2026_s34_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s34_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- Source hash: `3e86c57a164675158ddcf0d58b78e6a108bd74abedd97a4bb03a7757a849f8e1`

**Thai source**

4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

**English draft**

Team requests for extra time: 4 times per team, each lasting 30 seconds, valid during Freeze time

## 102. competition_rules_cs2_psu_phuket_2026_s34_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s34_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
- Source hash: `9eabea82084752530b459770e766a2fc76b4232648da46f69fa8499e94239a48`

**Thai source**

Counter-Strike 2: 4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time

**English draft**

Counter-Strike 2: 4. Out-of-turn Requests – Each team may request up to four 30-second extensions during Freeze time

## 103. competition_rules_cs2_psu_phuket_2026_s35_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s35_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. พฤติกรรมและบทลงโทษ
- Source hash: `7a0cf31003131e098cae07fd5a6f5e85fc4bb5a0e2b7e381e791ad24d085fb43`

**Thai source**

5. พฤติกรรมและบทลงโทษ

**English draft**

Behavior and Penalties

## 104. competition_rules_cs2_psu_phuket_2026_s35_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s35_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. พฤติกรรมและบทลงโทษ
- Source hash: `7a0cf31003131e098cae07fd5a6f5e85fc4bb5a0e2b7e381e791ad24d085fb43`

**Thai source**

5. พฤติกรรมและบทลงโทษ

**English draft**

Behavior and Penalties

## 105. competition_rules_cs2_psu_phuket_2026_s35_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s35_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. พฤติกรรมและบทลงโทษ
- Source hash: `7d65e7b5d3057b0f2cd9b9e4401cba9b616f48a0095a4d9f74b0d9bae1a21e7c`

**Thai source**

Counter-Strike 2: 5. พฤติกรรมและบทลงโทษ

**English draft**

Counter-Strike 2: 5. Behavior and Penalties

## 106. competition_rules_cs2_psu_phuket_2026_s36_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s36_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- Source hash: `3975d0dbc770b828fcffc74124f3b8f2e8fee69d4142949f1400ba40c2014c65`

**Thai source**

1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

**English draft**

Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship

## 107. competition_rules_cs2_psu_phuket_2026_s36_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s36_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- Source hash: `3975d0dbc770b828fcffc74124f3b8f2e8fee69d4142949f1400ba40c2014c65`

**Thai source**

1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

**English draft**

Player etiquette: Prohibited behaviors include aggression, offensive language (including racial or religious slurs), and actions lacking sportsmanship.

## 108. competition_rules_cs2_psu_phuket_2026_s36_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s36_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
- Source hash: `6a0c784a5cdee5c3983e299c89d7a2f78de80c2e03d49ea0745822a1b8db7252`

**Thai source**

Counter-Strike 2: 1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา

**English draft**

Counter-Strike 2: Player etiquette - Prohibited behavior includes aggression, offensive language (including racial or religious slurs), and unsportsmanlike conduct

## 109. competition_rules_cs2_psu_phuket_2026_s37_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s37_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- Source hash: `63ee9b7e8d210a8cdc1bd2cc3c12472b87d602b907379e91b93e8d75a3afa93c`

**Thai source**

2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

**English draft**

No use of hacks: Strictly prohibited to use hacks related to map or game engine. Violators will be penalized with a loss in the round/map or disqualified.

## 110. competition_rules_cs2_psu_phuket_2026_s37_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s37_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- Source hash: `63ee9b7e8d210a8cdc1bd2cc3c12472b87d602b907379e91b93e8d75a3afa93c`

**Thai source**

2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

**English draft**

No use of hacks is allowed, including map or game engine hacks. Violators will be penalized with a loss in the round/map or disqualified.

## 111. competition_rules_cs2_psu_phuket_2026_s37_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s37_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- Source hash: `8d9a8163bcff174388c64621e4de43644d9bf784be3dc559525d20a47738465b`

**Thai source**

Counter-Strike 2: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

**English draft**

Counter-Strike 2: 2. Using hacks is strictly prohibited. Players must not use map or game engine hacks. Violators will be penalized with a loss in the round/map or disqualified.

## 112. competition_rules_cs2_psu_phuket_2026_s38_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s38_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- Source hash: `0ab8caead98cfa1db461a6e579766ce0d728680b2b5125cfefd550444b0d14c4`

**Thai source**

3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

**English draft**

Watching Streams - Players are prohibited from watching live streams during matches

## 113. competition_rules_cs2_psu_phuket_2026_s38_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s38_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- Source hash: `0ab8caead98cfa1db461a6e579766ce0d728680b2b5125cfefd550444b0d14c4`

**Thai source**

3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

**English draft**

Watching streams: Players are prohibited from watching live streams during competition.

## 114. competition_rules_cs2_psu_phuket_2026_s38_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s38_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง
- Source hash: `a6a29bb89bd37fab4849ad56caf7ff14903faa9b9b7d1ce2d459c337ace1db4c`

**Thai source**

Counter-Strike 2: 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

**English draft**

Counter-Strike 2: 3. Watching live streams - Players are not allowed to watch live streams during competition

## 115. competition_rules_cs2_psu_phuket_2026_s39_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s39_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. อุปกรณ์และการตั้งค่าเกม
- Source hash: `f956325298f94e6af3ae336a8156e679b387b9e19b80073fb879602455c3c0e4`

**Thai source**

6. อุปกรณ์และการตั้งค่าเกม

**English draft**

Equipment and Game Setup

## 116. competition_rules_cs2_psu_phuket_2026_s39_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s39_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. อุปกรณ์และการตั้งค่าเกม
- Source hash: `f956325298f94e6af3ae336a8156e679b387b9e19b80073fb879602455c3c0e4`

**Thai source**

6. อุปกรณ์และการตั้งค่าเกม

**English draft**

Equipment and Game Settings

## 117. competition_rules_cs2_psu_phuket_2026_s39_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s39_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 6. อุปกรณ์และการตั้งค่าเกม
- Source hash: `7dd8d7dbdc17ef30375657b3c8f6d73b288287870349a94ad7d751733f054c5b`

**Thai source**

Counter-Strike 2: 6. อุปกรณ์และการตั้งค่าเกม

**English draft**

Counter-Strike 2: Equipment and Game Settings

## 118. competition_rules_cs2_psu_phuket_2026_s40_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s40_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อุปกรณ์ที่อนุญาต
- Source hash: `143cd8715c040cbc27b64be8309d14ead131bfa92f2eea863672867a48271963`

**Thai source**

1. อุปกรณ์ที่อนุญาต

**English draft**

Permitted Equipment

## 119. competition_rules_cs2_psu_phuket_2026_s40_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s40_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อุปกรณ์ที่อนุญาต
- Source hash: `143cd8715c040cbc27b64be8309d14ead131bfa92f2eea863672867a48271963`

**Thai source**

1. อุปกรณ์ที่อนุญาต

**English draft**

Permitted Equipment

## 120. competition_rules_cs2_psu_phuket_2026_s40_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s40_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อุปกรณ์ที่อนุญาต
- Source hash: `c2613836b2e46bfb6af4ec5f4f30692f06342d17eeb78221bbe8a03f2910e458`

**Thai source**

Counter-Strike 2: 1. อุปกรณ์ที่อนุญาต

**English draft**

Counter-Strike 2: 1. Allowed Equipment

## 121. competition_rules_cs2_psu_phuket_2026_s41_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s41_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- Source hash: `60f584178fc7e234dfa11ede15e4ddc0ad9c8dda7509d3619ad7fb521c8d97ae`

**Thai source**

1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**English draft**

Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

## 122. competition_rules_cs2_psu_phuket_2026_s41_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s41_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- Source hash: `60f584178fc7e234dfa11ede15e4ddc0ad9c8dda7509d3619ad7fb521c8d97ae`

**Thai source**

1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**English draft**

Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

## 123. competition_rules_cs2_psu_phuket_2026_s41_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s41_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- Source hash: `d4fe301debc18187f8263d1ef47d63b1b1c21e5e80c8d49dd37ded3a0a351bfc`

**Thai source**

Counter-Strike 2: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

**English draft**

Counter-Strike 2: Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

## 124. competition_rules_cs2_psu_phuket_2026_s42_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s42_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง
- Source hash: `d0140a708b5f9a8e1037b0ec8e43ef247ec3a6a0e6b7dd6a3208acfcf65c1298`

**Thai source**

2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

**English draft**

Players are responsible for the quality and availability of their own equipment

## 125. competition_rules_cs2_psu_phuket_2026_s42_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s42_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง
- Source hash: `d0140a708b5f9a8e1037b0ec8e43ef247ec3a6a0e6b7dd6a3208acfcf65c1298`

**Thai source**

2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

**English draft**

Players are responsible for the quality and availability of their own equipment.

## 126. competition_rules_cs2_psu_phuket_2026_s42_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s42_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง
- Source hash: `8baa2c9e9de86632489d8abdb6d1a3adb72fa7f02bf7b21794b546f7e02ce1b2`

**Thai source**

Counter-Strike 2: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

**English draft**

Counter-Strike 2: 2. Players are responsible for the quality and availability of their own equipment

## 127. competition_rules_cs2_psu_phuket_2026_s43_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s43_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
- Source hash: `75d79cae19236490edfb47bb5ab9f59b2a447bf31a9060e3ca085ae481ad2974`

**Thai source**

3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้

**English draft**

The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.

## 128. competition_rules_cs2_psu_phuket_2026_s43_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s43_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
- Source hash: `75d79cae19236490edfb47bb5ab9f59b2a447bf31a9060e3ca085ae481ad2974`

**Thai source**

3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้

**English draft**

The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.

## 129. competition_rules_cs2_psu_phuket_2026_s43_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s43_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
- Source hash: `8f74c3e1f11aa824e29851512bbeadf7f472c449b94022e0c551ece26258b701`

**Thai source**

Counter-Strike 2: 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้

**English draft**

Counter-Strike 2: 3. The organizers will provide PCs, monitors, headphones with microphones, tables, and chairs

## 130. competition_rules_cs2_psu_phuket_2026_s44_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s44_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าเกม
- Source hash: `3745fce9c1c0ca18180fe310871a2e98f4e3f9697cbd80772f225d9f6d7a96e1`

**Thai source**

2. การตั้งค่าเกม

**English draft**

Game Settings

## 131. competition_rules_cs2_psu_phuket_2026_s44_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s44_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าเกม
- Source hash: `3745fce9c1c0ca18180fe310871a2e98f4e3f9697cbd80772f225d9f6d7a96e1`

**Thai source**

2. การตั้งค่าเกม

**English draft**

Game Setup

## 132. competition_rules_cs2_psu_phuket_2026_s44_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s44_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การตั้งค่าเกม
- Source hash: `ae369b0a15dededc64568d7c1dd77c0da1c4c7c8452d036d8d572233136e0d40`

**Thai source**

Counter-Strike 2: 2. การตั้งค่าเกม

**English draft**

Counter-Strike 2: Game Settings

## 133. competition_rules_cs2_psu_phuket_2026_s45_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s45_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- Source hash: `2f7dacf9fc0f7c5c90c4f546a2a994287a5e88b831ab3d54abe4007b43aecb20`

**Thai source**

1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

**English draft**

Players may customize brightness, resolution, and crosshair settings only within the game and computer display

## 134. competition_rules_cs2_psu_phuket_2026_s45_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s45_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- Source hash: `2f7dacf9fc0f7c5c90c4f546a2a994287a5e88b831ab3d54abe4007b43aecb20`

**Thai source**

1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

**English draft**

Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.

## 135. competition_rules_cs2_psu_phuket_2026_s45_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s45_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- Source hash: `a34cb63001364ccf79bd80c0ef3ad0852b15fe12465426ff7301470db3e4fa7d`

**Thai source**

Counter-Strike 2: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

**English draft**

Counter-Strike 2: Players may adjust brightness, resolution, and crosshair settings only within the game and on their computer monitor.

## 136. competition_rules_cs2_psu_phuket_2026_s46_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s46_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด
- Source hash: `d44058d682ddb09529a125bfe49ac404917fe0f3bfbad6d1650bd92c41a63c10`

**Thai source**

3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

**English draft**

Prohibited to use scripts or macros at all costs

## 137. competition_rules_cs2_psu_phuket_2026_s46_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s46_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด
- Source hash: `d44058d682ddb09529a125bfe49ac404917fe0f3bfbad6d1650bd92c41a63c10`

**Thai source**

3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

**English draft**

No scripts or macros are allowed at all.

## 138. competition_rules_cs2_psu_phuket_2026_s46_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s46_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด
- Source hash: `dc9e1572e0afed62d9dc7d06277d07cc3730a9215b3d34ed40221f23998ddeed`

**Thai source**

Counter-Strike 2: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

**English draft**

Counter-Strike 2: 3. Strictly prohibited to use scripts or macros

## 139. competition_rules_cs2_psu_phuket_2026_s47_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s47_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
- Source hash: `1f0f7e21d3bf419bf1390635723d7483a96091a3cac84ce1ceefe0f7b35cdfc3`

**Thai source**

4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

**English draft**

4. Prohibited to install any programs on the designated computers

## 140. competition_rules_cs2_psu_phuket_2026_s47_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s47_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
- Source hash: `1f0f7e21d3bf419bf1390635723d7483a96091a3cac84ce1ceefe0f7b35cdfc3`

**Thai source**

4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

**English draft**

4. No installing programs on the computers provided

## 141. competition_rules_cs2_psu_phuket_2026_s47_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s47_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
- Source hash: `ed508c23917c826ac8d857cb94478c189323585e906b55d99c7a5a5511c1dbb7`

**Thai source**

Counter-Strike 2: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

**English draft**

Counter-Strike 2: 4. Prohibited to install any software on the designated computers

## 142. competition_rules_cs2_psu_phuket_2026_s48_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s48_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้
- Source hash: `f5456082703d2b72c1aeadfff149c1a32e3b5b9bafc4bfa74f1e749b7779fa70`

**Thai source**

5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

**English draft**

5. Prohibited to access any social media or communication websites on the competition computers except for the programs provided by the organizers

## 143. competition_rules_cs2_psu_phuket_2026_s48_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s48_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้
- Source hash: `f5456082703d2b72c1aeadfff149c1a32e3b5b9bafc4bfa74f1e749b7779fa70`

**Thai source**

5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

**English draft**

5. Participants must not access any social media or communication websites on the competition computers except for the programs provided by the organizers.

## 144. competition_rules_cs2_psu_phuket_2026_s48_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s48_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้
- Source hash: `27a1250019fc1b45284fe0d5c4aa6a9b43d2258344bafab29ecab6c9706a7cc7`

**Thai source**

Counter-Strike 2: 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

**English draft**

Counter-Strike 2: 5. Prohibited to access any social media or communication websites on the competition computers other than the programs provided by the organizers

## 145. competition_rules_cs2_psu_phuket_2026_s49_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s49_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `28f02f3c8548c9e2937f04cb363d74c5cfc40fda9eac07b3c708c54648d3f706`

**Thai source**

7. พื้นที่การแข่งขันและกฎระเบียบ

**English draft**

Competition Venue and Regulations

## 146. competition_rules_cs2_psu_phuket_2026_s49_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s49_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `28f02f3c8548c9e2937f04cb363d74c5cfc40fda9eac07b3c708c54648d3f706`

**Thai source**

7. พื้นที่การแข่งขันและกฎระเบียบ

**English draft**

Competition Venue and Regulations

## 147. competition_rules_cs2_psu_phuket_2026_s49_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s49_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 7. พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `ea960ab7b499b71b7d9b7affbf6755272b0f8b60da5272fd90e69f25873ee232`

**Thai source**

Counter-Strike 2: 7. พื้นที่การแข่งขันและกฎระเบียบ

**English draft**

Counter-Strike 2: Competition Area and Rules

## 148. competition_rules_cs2_psu_phuket_2026_s50_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s50_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- Source hash: `14d1bdead3c32af2a333e429f29dfa6be3bde489a4b89dde189a3fec73edb7e2`

**Thai source**

1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

**English draft**

Number of personnel during preparation phase: maximum of 6 players

## 149. competition_rules_cs2_psu_phuket_2026_s50_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s50_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- Source hash: `14d1bdead3c32af2a333e429f29dfa6be3bde489a4b89dde189a3fec73edb7e2`

**Thai source**

1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

**English draft**

During preparation phase, the number of personnel shall not exceed 6 players.

## 150. competition_rules_cs2_psu_phuket_2026_s50_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s50_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- Source hash: `1ab85bc7b015798a10eefda7ea7053687469b7c8926826c5ce833ea1aa9548a9`

**Thai source**

Counter-Strike 2: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

**English draft**

Counter-Strike 2: 1. Number of personnel during preparation phase is limited to a maximum of 6 players

## 151. competition_rules_cs2_psu_phuket_2026_s51_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s51_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- Source hash: `c63a83dc1dc90386ce5524180c505e363e7e170dbac25bb5b7120c3b3a6510f0`

**Thai source**

2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**English draft**

Prohibited to bring mobile phones, tablets, or smartwatches into the competition area until the match ends

## 152. competition_rules_cs2_psu_phuket_2026_s51_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s51_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- Source hash: `c63a83dc1dc90386ce5524180c505e363e7e170dbac25bb5b7120c3b3a6510f0`

**Thai source**

2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**English draft**

Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

## 153. competition_rules_cs2_psu_phuket_2026_s51_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s51_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
- Source hash: `3360fe219383f6c5179c6fbfa8730db79e1b1bca47d78bd43de45bf1f2270340`

**Thai source**

Counter-Strike 2: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

**English draft**

Counter-Strike 2: 2. Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes

## 154. competition_rules_cs2_psu_phuket_2026_s52_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s52_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- Source hash: `5b56fcd859dee25143fe2219804ba2d24f7d0ea4a41174e1f848edfe8892dd01`

**Thai source**

3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

**English draft**

Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match

## 155. competition_rules_cs2_psu_phuket_2026_s52_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s52_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- Source hash: `5b56fcd859dee25143fe2219804ba2d24f7d0ea4a41174e1f848edfe8892dd01`

**Thai source**

3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

**English draft**

Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match.

## 156. competition_rules_cs2_psu_phuket_2026_s52_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s52_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
- Source hash: `c6729717b4cb4565198fa93690dee78c55bdae3402f403f900edb5da0cc6d546`

**Thai source**

Counter-Strike 2: 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

**English draft**

Counter-Strike 2: 3. Players are not allowed to bring notes or documents into the arena, but team captains may bring them in and must provide all documents to the referees prior to every match

## 157. competition_rules_cs2_psu_phuket_2026_s53_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s53_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- Source hash: `43cfcc2b450cded275886445b23b871ce17f5c93cb6719cfe48940ea033efabb`

**Thai source**

4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

**English draft**

Only sealed containers of beverages and checkers are permitted

## 158. competition_rules_cs2_psu_phuket_2026_s53_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s53_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- Source hash: `43cfcc2b450cded275886445b23b871ce17f5c93cb6719cfe48940ea033efabb`

**Thai source**

4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

**English draft**

Only sealed containers of beverages and checkers are permitted

## 159. competition_rules_cs2_psu_phuket_2026_s53_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s53_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
- Source hash: `36dba7a3202d9c8412bfb7b2da5883ba538eca7f5fe2d7a98c15263934c3a5e4`

**Thai source**

Counter-Strike 2: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

**English draft**

Counter-Strike 2: Only sealed containers of beverages and checkers are permitted

## 160. competition_rules_cs2_psu_phuket_2026_s54_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s54_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 8. ตารางบทลงโทษ (Penalties)
- Source hash: `843f16469f8292351e20a7cee023a3b97b2f7a7410ed37d3f4574f14eb11e887`

**Thai source**

8. ตารางบทลงโทษ (Penalties)

**English draft**

Section Title

## 161. competition_rules_cs2_psu_phuket_2026_s54_c01 / text

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

8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match Unethical behavior Loss in that round → Disqualification Disregarding officials' decisions Loss in that round / Disqualification Sending inappropriate chat messages in-game Loss in that round or match Offensive religious remarks

## 162. competition_rules_cs2_psu_phuket_2026_s54_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s54_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 8. ตารางบทลงโทษ (Penalties)
- Source hash: `096f1b9d0db927f4bb533b384d964595c701032dbb463ed34d7d59de2c8ce09b`

**Thai source**

Counter-Strike 2: 8. ตารางบทลงโทษ (Penalties)

**English draft**

Counter-Strike 2: 8. Penalty Table

## 163. competition_rules_cs2_psu_phuket_2026_s55_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s55_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: แบนถาวร
- Source hash: `6f3519af2d265544bbedb7f3d2bf46635be0324d81e6383dfc10ea44610ef665`

**Thai source**

แบนถาวร

**English draft**

Permanent ban

## 164. competition_rules_cs2_psu_phuket_2026_s55_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s55_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: แบนถาวร
- Source hash: `6f3519af2d265544bbedb7f3d2bf46635be0324d81e6383dfc10ea44610ef665`

**Thai source**

แบนถาวร

**English draft**

Permanent ban

## 165. competition_rules_cs2_psu_phuket_2026_s55_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s55_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: แบนถาวร
- Source hash: `17bb71d0fdd413c6857345949abc7b6df0ded1b36930525676d0082fcb519cd9`

**Thai source**

Counter-Strike 2: แบนถาวร

**English draft**

Counter-Strike 2: Permanent Ban

## 166. competition_rules_cs2_psu_phuket_2026_s56_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s56_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 9. การบริหารจัดการและผู้ตัดสิน
- Source hash: `b681cdef7fd2065f4df8ae2f5ef2b5dff7e43440b59c1a541b734edfd4f6cbeb`

**Thai source**

9. การบริหารจัดการและผู้ตัดสิน

**English draft**

Administration and Officials

## 167. competition_rules_cs2_psu_phuket_2026_s56_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s56_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 9. การบริหารจัดการและผู้ตัดสิน
- Source hash: `b681cdef7fd2065f4df8ae2f5ef2b5dff7e43440b59c1a541b734edfd4f6cbeb`

**Thai source**

9. การบริหารจัดการและผู้ตัดสิน

**English draft**

Administration and Officials

## 168. competition_rules_cs2_psu_phuket_2026_s56_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s56_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 9. การบริหารจัดการและผู้ตัดสิน
- Source hash: `85f304c0b1c26c3c3e847809b51ffefbe926a986b03194a8a29318dc28fdb7b1`

**Thai source**

Counter-Strike 2: 9. การบริหารจัดการและผู้ตัดสิน

**English draft**

Counter-Strike 2: 9. Management and Officials

## 169. competition_rules_cs2_psu_phuket_2026_s57_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s57_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม
- Source hash: `2a8c5086be8276687d1d067924fb3f1888833aafa53b7aafe75cd4aefd0d4f32`

**Thai source**

1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

**English draft**

Judicial Authority: Officials' Decisions and Organizer's Verdict Are Final. The Organizer Reserves the Right to Amend Rules as Necessary for Fairness

## 170. competition_rules_cs2_psu_phuket_2026_s57_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s57_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม
- Source hash: `2a8c5086be8276687d1d067924fb3f1888833aafa53b7aafe75cd4aefd0d4f32`

**Thai source**

1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

**English draft**

Judgment authority: The referees' decisions and the organizers' rulings are final. The organizing side reserves the right to amend rules as appropriate for fairness.

## 171. competition_rules_cs2_psu_phuket_2026_s57_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s57_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม
- Source hash: `acc34c7fe177ee9cc7e62a59291a5db31defdaee481192ace93b3cb307d7c8f3`

**Thai source**

Counter-Strike 2: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

**English draft**

Counter-Strike 2: 1. Final authority rests with the referees' decisions and organizers; organizers may amend rules as appropriate for fairness

## 172. competition_rules_cs2_psu_phuket_2026_s58_c01 / section_title

- Selector: `competition_rules_cs2_psu_phuket_2026_s58_c01:section_title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- Source hash: `623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d`

**Thai source**

2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

**English draft**

Complaints must be submitted within 15 minutes after match completion by the team captain or coach only

## 173. competition_rules_cs2_psu_phuket_2026_s58_c01 / text

- Selector: `competition_rules_cs2_psu_phuket_2026_s58_c01:text`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- Source hash: `623c43aa2f79f6a6e1bbbecdff08845436dc50a9e857876d46d53cabd094f09d`

**Thai source**

2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

**English draft**

Complaints must be submitted within 15 minutes after the match ends, by the team captain or coach only.

## 174. competition_rules_cs2_psu_phuket_2026_s58_c01 / title

- Selector: `competition_rules_cs2_psu_phuket_2026_s58_c01:title`
- Category: `competition_rules`
- Title: Counter-Strike 2: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น
- Source hash: `f743d753153a1d752680894560e80c356884ddc0713408645c1fd179c2cf4af1`

**Thai source**

Counter-Strike 2: 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

**English draft**

Counter-Strike 2: 2. Appeal must be submitted within 15 minutes after match end by team captain or coach only

## 175. competition_rules_rov_blueket_2025_men_s01_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s01_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ภาพรวมเอกสาร
- Source hash: `fa88e9d3bfec10aad1ecdd09982166ee672fbb3680827323abb6b32f5c8c50a3`

**Thai source**

ภาพรวมเอกสาร

**English draft**

Overview of Document

## 176. competition_rules_rov_blueket_2025_men_s01_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s01_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ภาพรวมเอกสาร
- Source hash: `c3c5b4e468351240ff6765b3c41fc756df078caf73f3a42b0de4526dae57a96b`

**Thai source**

กติกาการแข่งขัน Blueket Games 2025
รายการอีสปอร์ต
เกม Arena of Valor (RoV)

**English draft**

Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)

## 177. competition_rules_rov_blueket_2025_men_s01_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s01_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ภาพรวมเอกสาร
- Source hash: `73323acdff1eaa693829b43d76e72c2e1a4c1adac9c4563746efe27046ff9fed`

**Thai source**

Arena of Valor (RoV): ภาพรวมเอกสาร

**English draft**

Arena of Valor (RoV): Overview Document

## 178. competition_rules_rov_blueket_2025_men_s02_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s02_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ประเภททีมชาย
- Source hash: `02dcd8170425f14ae2845cecd939e2a242e7708658388896ca28d54f53ff32d9`

**Thai source**

ประเภททีมชาย

**English draft**

Men's Team Category

## 179. competition_rules_rov_blueket_2025_men_s02_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s02_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ประเภททีมชาย
- Source hash: `02dcd8170425f14ae2845cecd939e2a242e7708658388896ca28d54f53ff32d9`

**Thai source**

ประเภททีมชาย

**English draft**

Male Team Category

## 180. competition_rules_rov_blueket_2025_men_s02_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s02_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): ประเภททีมชาย
- Source hash: `6a6a7479209339c2ffe9ae8b943bfcbc0a3f0f67a613c71cdee3384e8bb4168b`

**Thai source**

Arena of Valor (RoV): ประเภททีมชาย

**English draft**

Arena of Valor (RoV): Men's Team Category

## 181. competition_rules_rov_blueket_2025_men_s03_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s03_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 1. กำหนดการแข่งขัน
- Source hash: `ffa7fa40cf65f68a39395585f40f4083066c8ce282d0e5e68e9793b33f046860`

**Thai source**

1. กำหนดการแข่งขัน

**English draft**

Competition Schedule

## 182. competition_rules_rov_blueket_2025_men_s03_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s03_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 1. กำหนดการแข่งขัน
- Source hash: `d69e40b6c43d664109fae13b7bed144408dda208d832ffda5f4d0578e9f5dbab`

**Thai source**

1. กำหนดการแข่งขัน
1.1. แข่งขันออฟไลน์ วันที่ 11 กันยายน 2568
· เวลา 8.00-8.30 ลงทะเบียน
· เวลา 8.30-8.40 แบ่งสายการแข่งขัน
· เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
· เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
· เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
· เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
· เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3

**English draft**

Competition Schedule 1.1. Offline event on September 11, 2068 · Registration: 8:00–8:30 AM · Draw of brackets: 8:30–8:40 AM · Round of 5 teams, Single Elimination BO3: 8:40–10:00 AM · Semifinal Match 1, Single Elimination BO3: 10:00–11:30 AM · Semifinal Match 2, Single Elimination BO3: 12:30–2:00 PM · Bronze Medal Match, Single Elimination BO3: 2:00–3:30 PM · Grand Final, Single Elimination BO3: 3:30–5:00 PM

## 183. competition_rules_rov_blueket_2025_men_s03_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s03_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 1. กำหนดการแข่งขัน
- Source hash: `2aadbaeed92dd5427d444070f2798195f6b0ac76ce4a646e22bf2feb5a3aa3c3`

**Thai source**

Arena of Valor (RoV): 1. กำหนดการแข่งขัน

**English draft**

Arena of Valor (RoV): 1. Competition Schedule

## 184. competition_rules_rov_blueket_2025_men_s04_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s04_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 2. สถานที่แข่งขัน
- Source hash: `8024265bd40311f7fcab96241eaa6f0663329ad409039f2a5097a4e36365dbdf`

**Thai source**

2. สถานที่แข่งขัน

**English draft**

Venue

## 185. competition_rules_rov_blueket_2025_men_s04_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s04_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 2. สถานที่แข่งขัน
- Source hash: `ca8d2cd59482387f34d743505f853365c8b7a325b345bbd33c2e38b2ec8cc75e`

**Thai source**

2. สถานที่แข่งขัน
2.1. PSU Esports Studio – Phuket (อาคาร 5 ชั้น 1)

**English draft**

Competition Venue 2.1. PSU Esports Studio – Phuket (Building Level 5, Floor 1)

## 186. competition_rules_rov_blueket_2025_men_s04_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s04_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 2. สถานที่แข่งขัน
- Source hash: `91b41e6392a75be0362df8f6a6a855c2a4f6eda73c776e54728d8c6fe0971396`

**Thai source**

Arena of Valor (RoV): 2. สถานที่แข่งขัน

**English draft**

Arena of Valor (RoV): 2. Competition Venue

## 187. competition_rules_rov_blueket_2025_men_s05_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s05_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 3. รูปแบบการแข่งขัน
- Source hash: `ecdce670141f9ba53c27893ec8aed3c23c14ffa1ab4ad331e8e73c1292260680`

**Thai source**

3. รูปแบบการแข่งขัน

**English draft**

Competition Format

## 188. competition_rules_rov_blueket_2025_men_s05_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s05_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 3. รูปแบบการแข่งขัน
- Source hash: `dc3f6e3f0d769b3951f496c7064772367bc3d3144bb9a0f8f0813a6e59c12248`

**Thai source**

3. รูปแบบการแข่งขัน
3.1. แข่งแบบออฟไลน์
3.2. แข่ง Best of 3 (BO3) ทุกรอบ

**English draft**

Competition Format 3.1. Offline Mode 3.2. Each round played as Best of 3 (BO3)

## 189. competition_rules_rov_blueket_2025_men_s05_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s05_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 3. รูปแบบการแข่งขัน
- Source hash: `67faa2e649f42e37263c4d308392453036ef317e14cbc68b3358adf5cf0298a6`

**Thai source**

Arena of Valor (RoV): 3. รูปแบบการแข่งขัน

**English draft**

Arena of Valor (RoV): 3. Competition Format

## 190. competition_rules_rov_blueket_2025_men_s06_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `a07203d34db7116335af5ea8ac1a610ce04187f6b6c4899cb6d00e15447003a0`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน

**English draft**

Competition Rules

## 191. competition_rules_rov_blueket_2025_men_s06_c01 / text

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

Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others. 4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side. 4.1.3. The referees will announce the room number so both teams can enter the designated room. * The blue team is on top * The red team is on bottom 4.1.4. If a team starts the match more than 15 minutes after the scheduled time, the delayed team will be immediately forfeited. 4.2. Competition Rules 4.2.1. All participants must have at least 18 heroes for the "5v5" mode (formerly known as Tournament Mode). 4.2.2. Use Global Ban/Pick hero selection. 4.2.3. Runes and item bonuses may be used as desired. 4.2.4. In competition, all participants may choose any hero they wish. 4.2.5. Regarding skins, only Default skins may be used. 4.2.6. No duplicate hero selection or any other actions that cause system issues are permitted under any circumstances. 4.3. Disconnection and Rematch 4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.

## 192. competition_rules_rov_blueket_2025_men_s06_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `af273949eee995524b7dca177cc1202da8d80e4c1fdab938cacb9e6be4def956`

**Thai source**

Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน

**English draft**

Arena of Valor (RoV): 4. Competition Rules

## 193. competition_rules_rov_blueket_2025_men_s06_c02 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c02:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `a07203d34db7116335af5ea8ac1a610ce04187f6b6c4899cb6d00e15447003a0`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน

**English draft**

Competition Rules

## 194. competition_rules_rov_blueket_2025_men_s06_c02 / text

- Selector: `competition_rules_rov_blueket_2025_men_s06_c02:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `f36218979545a6145121aa48bd869186a2aa7168c47ee92bb813ab4b33ae6ad1`

**Thai source**

4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ
4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
4.4. เวลาพัก
4.4.1.ผู้ตัดสินจะแจ้งให้ผู้เข้าแข่งขันทราบถึงระยะเวลาที่เหลือก่อนที่เกมถัดไปจะเริ่มขึ้น
4.4.2.หากผู้เข้าแข่งขันไม่กลับมาภายในเวลาที่กำหนด ผู้ตัดสินอาจปรับให้ทีมดังกล่าวแพ้จากการแข่งขัน
4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม
4.5. การหยุดพักเกมในการแข่งขัน
4.5.1.การหยุดพักเกมทั่วไป
4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ

**English draft**

4.3.2. If a competitor is disqualified due to unforeseen circumstances (such as an entire area internet service provider outage or server errors in the game), the affected team must notify the staff, and whether to allow a replay will be at the discretion of the referees. 4.3.3. In cases where no First Blood has occurred and the game time has not exceeded 2 minutes, the team whose competitor was disqualified may immediately request a new game start with all players selecting their hero and role as they did in the first game before requesting a restart. 4.3.4. Once First Blood has occurred or the game has started beyond 2 minutes, neither team may request a new game start unless granted permission by the opponent and/or deemed appropriate by the referees. 4.3.5. If evidence is found that a competitor intentionally halted the game, whether during a critical moment or for disruption purposes, the offending player will be penalized immediately with a loss in that match, and the team of the offending competitor will be immediately disqualified from the competition. 4.4. Break Time 4.4.1. The referee shall inform competitors of the remaining time before the next game starts. 4.4.2. If a competitor fails to return within the specified time, the referee may declare that team to have lost the match. 4.4.3. A 5-minute break after every two games. 4.5. Game Interruptions During Competition 4.5.1. General Game Interruptions 4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee has the right to deny that interruption request.

## 195. competition_rules_rov_blueket_2025_men_s06_c02 / title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c02:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `af273949eee995524b7dca177cc1202da8d80e4c1fdab938cacb9e6be4def956`

**Thai source**

Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน

**English draft**

Arena of Valor (RoV): 4. Competition Rules

## 196. competition_rules_rov_blueket_2025_men_s06_c03 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c03:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `a07203d34db7116335af5ea8ac1a610ce04187f6b6c4899cb6d00e15447003a0`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน

**English draft**

Competition Rules

## 197. competition_rules_rov_blueket_2025_men_s06_c03 / text

- Selector: `competition_rules_rov_blueket_2025_men_s06_c03:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `01acace8187569211ae28e863776dc4decf7c5f8d29d289c89ae7bc16dc4b0d2`

**Thai source**

4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งให้หยุดพักเกมดังกล่าว และให้ผู้เข้าแข่งขันกลับเข้าสู่การแข่งขันใหม่อีกครั้งภายหลังจากผู้เข้าแข่งขันที่ไม่ได้เชื่อมต่อได้กลับเข้ามาในเกมแล้ว
4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร
4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไป ทั้งนี้เป็นไปตามที่ทางทีมงานเห็นควรการหยุดพักเกมโดยผู้ตัดสิน
4.5.4.ผู้ตัดสินอาจสั่งให้หยุดพักเกมได้ ไม่ว่าด้วยเหตุใดก็ตาม
4.5.5.การหลุดการเชื่อมต่อโดยไม่เจตนา
4.5.5.1. หากผู้เข้าแข่งขันรายใดตกอยู่ในสภาวะที่เป็นอันตรายต่อชีวิต กล่าวคือ ไม่มีความปลอดภัยในการบริเวณการแข่งขัน หรือตกอยู่ในสถานการณ์อื่นใดที่ทำให้เกิดปัญหาในการดำเนินเกมต่อไป
4.5.5.2. ภัยธรรมชาติที่ทำให้เกมหยุดชะงัก
4.5.6.การหยุดพักเกมโดยผู้เข้าแข่งขัน
4.5.6.1. ผู้เข้าแข่งขันอาจหยุดพักเกมการแข่งขันได้ภายหลังจากเกิดเหตุการณ์ใดเหตุการณ์หนึ่งดังต่อไปนี้ โดยผู้เข้าแข่งขันดังกล่าวจะต้องส่งสัญญาณให้ผู้ตัดสินทราบโดยทันทีภายหลังจากการหยุดเกมและชี้แจงเหตุผลแห่งการหยุดเกมดังกล่าว

**English draft**

4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected. 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game. 4.5.3 After reconnection, the event staff may order both competing teams to immediately restart the game and/or continue playing anew, as they deem appropriate. 4.5.4 The referee may pause the game for any reason. 4.5.5 Unintentional disconnections. 4.5.5.1 If a player is in a life-threatening situation, such as being unsafe in the competition area or facing other circumstances that prevent continued gameplay. 4.5.5.2 Natural disasters causing game interruptions. 4.5.6 Player-initiated game pauses. 4.5.6.1 A player may pause the game following any of the following events, and must immediately signal the referee upon pausing the game to explain the reason for the pause.

## 198. competition_rules_rov_blueket_2025_men_s06_c03 / title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c03:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `af273949eee995524b7dca177cc1202da8d80e4c1fdab938cacb9e6be4def956`

**Thai source**

Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน

**English draft**

Arena of Valor (RoV): 4. Competition Rules

## 199. competition_rules_rov_blueket_2025_men_s06_c04 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c04:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `a07203d34db7116335af5ea8ac1a610ce04187f6b6c4899cb6d00e15447003a0`

**Thai source**

4. ระเบียบและกติกาการแข่งขัน

**English draft**

Competition Rules

## 200. competition_rules_rov_blueket_2025_men_s06_c04 / text

- Selector: `competition_rules_rov_blueket_2025_men_s06_c04:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `bea166fb055836153ebc30df1f0005e562b8d54d2bf9e24c12982a9b28b16e0d`

**Thai source**

4.5.6.1.1. มีการรบกวนทางกายภาพระหว่างผู้เข้าแข่งขัน เช่น การก่อความวุ่นวาย ความโกลาหล และเสียงดังซึ่งรบกวนเกม เป็นต้น
4.5.6.1.2. อุปกรณ์พกพาหรือซอฟต์แวร์ทำงานผิดปกติ
4.5.6.1.3. การลดลงของเฟรมหรือ การเพิ่มขึ้นของ PING อันนอกเหนือจากการควบคุม
4.5.6.1.4. เมื่อผู้เข้าแข่งขันฝ่ายตรงข้ามโกงหรือดูถูกอย่างร้ายแรง เป็นต้น
4.6. ความเจ็บป่วยบาดเจ็บ หรือปัญหาทางกายภาพของผู้เข้าแข่งขันไม่เป็นเหตุที่สามารถยอมรับได้สำหรับการหยุดพักของผู้เข้าแข่งขัน
4.6.1.การหยุดพักเกมอันเนื่องมากจากปัญหาเครื่องร้อนของอุปกรณ์พกพา
4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
4.6.2.การหยุดพักเกมตามการตัดสินใจของผู้เข้าร่วมการแข่งขัน โดยไม่ได้รับอนุญาตจากผู้ตัดสิน
4.6.2.1. ทางทีมงานมีสิทธิเตือนและ/หรือปรับทีมผู้เข้าร่วมการแข่งขันดังกล่าวแพ้ทันที
4.6.2.2. ห้ามมิให้ผู้เข้าร่วมการแข่งขันพูดคุย ติดต่อสื่อสาร หรือดำเนินการใดๆ อันเป็นการสื่อสารในระหว่างการหยุดพักเกม
4.6.3.บทลงโทษ:
4.6.3.1. ครั้งที่ 1: ตักเตือน
4.6.3.2. ครั้งที่ 2: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 1 ครั้ง
4.6.3.3. ครั้งที่ 3: เพิ่มสิทธิการแบนฮีโร่ให้ฝั่งตรงข้ามเป็นจำนวน 2 ครั้ง

**English draft**

4.5.6.1.1 Physical disturbances between competitors, such as causing chaos, noise, and loud sounds that interfere with gameplay. 4.5.6.1.2 Portable devices or software malfunctioning. 4.5.6.1.3 Frame drops or increased ping outside of player control. 4.5.6.1.4 When the opposing team engages in severe cheating or disrespect. 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay. 4.6.1. Game pauses due to portable device overheating. 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay. 4.6.2. Game pauses made by competitors without referee authorization. 4.6.2.1 Staff have the right to warn and/or immediately penalize the offending team by awarding a loss. 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication. 4.6.3. Penalties: 4.6.3.1 First offense: Warning. 4.6.3.2 Second offense: Award the opposing team one hero ban. 4.6.3.3 Third offense: Award the opposing team two hero bans.

## 201. competition_rules_rov_blueket_2025_men_s06_c04 / title

- Selector: `competition_rules_rov_blueket_2025_men_s06_c04:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
- Source hash: `af273949eee995524b7dca177cc1202da8d80e4c1fdab938cacb9e6be4def956`

**Thai source**

Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน

**English draft**

Arena of Valor (RoV): 4. Competition Rules

## 202. competition_rules_rov_blueket_2025_men_s07_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s07_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
- Source hash: `f81f490bcf46d56d33bfd576970b262b67069e60a3b3c330f3dd7d6688697001`

**Thai source**

5. ชุดแข่งขันและอุปกรณ์การแข่งขัน

**English draft**

Match Sets and Competition Equipment

## 203. competition_rules_rov_blueket_2025_men_s07_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s07_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
- Source hash: `333ee96305cd26f5580a412350e054a59b0cb6e5c4573ba223b29b63d3ba4e59`

**Thai source**

5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
5.1. อุปกรณ์โทรศัพท์มือถือและอินเตอร์เน็ตส่วนตัว และ/หรืออินเทอร์เน็ตของทางมหาวิทยาลัย
5.2. ปลั๊กพ่วงและอุปกรณ์ชาร์จแบตส่วนตัว
5.3. ไม่อนุญาตให้ใช้ Tablet หรือ iPad รวมถึงอุปกรณ์อื่นใดที่มิใช่โทรศัพท์มือถือ (Mobile Phone) ในการแข่งขัน หากตรวจสอบพบ ทีมงานจะตัดสิทธิ์ทันที

**English draft**

5. Match sets and competition equipment 5.1. Personal mobile phones and internet, and/or university internet 5.2. Power adapters and personal charging devices 5.3. Tablets and iPads are not permitted for use during competition, nor any other equipment other than a mobile phone (Mobile Phone). If detected, the team will be disqualified immediately.

## 204. competition_rules_rov_blueket_2025_men_s07_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s07_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน
- Source hash: `d2acbfdb3b3b697116b064966c8e8f88804f57e877ebb0ab158c6a9eb0248e38`

**Thai source**

Arena of Valor (RoV): 5. ชุดแข่งขันและอุปกรณ์การแข่งขัน

**English draft**

Arena of Valor (RoV): 5. Competition Sets and Equipment

## 205. competition_rules_rov_blueket_2025_men_s08_c01 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s08_c01:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `8fb284ce4ece5b0fbefb09876dfee2df7b0a72b250aba064c0bfad58dd9b2fa7`

**Thai source**

6. การกระทำความผิดและบทลงโทษ

**English draft**

Offenses and Penalties

## 206. competition_rules_rov_blueket_2025_men_s08_c01 / text

- Selector: `competition_rules_rov_blueket_2025_men_s08_c01:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `92ebcc6a88ca7486dda118de87f33f526c2a915384974575bf70f7daba4f3bd2`

**Thai source**

6. การกระทำความผิดและบทลงโทษ
6.1. ห้ามมิให้ผู้เข้าแข่งขันทุกคนกระทำการอย่างหนึ่งอย่างใดดังต่อไปนี้
6.1.1.ห้ามใช้คำพูดหรือแสดงกิริยาไม่สุภาพ หรือเสียดสีผู้อื่น
6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที
6.1.2.ห้ามส่งผลการแข่งขันอันเป็นเท็จ หรือบิดเบือน
6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.3.ห้ามทีมผู้เข้าแข่งขันทุกทีมอนุญาตให้บุคคลอื่นที่ไม่ได้อยู่ในรายชื่อผู้เข้าแข่งขันในทีมของตนตามที่ได้ลงทะเบียนไว้เข้าแข่งขันโดยเด็ดขาด หากพบว่ามีชื่อผู้เข้าแข่งขันไม่ตรงตามที่ลงทะเบียนไว้ ให้ทำการบันทึกภาพหลักฐานและยุติการแข่งขันในทันที แต่หากมีการแข่งขันจนจบเกม จะถือว่าทั้งสองทีมยินยอมให้เกิดการแข่งขันขึ้น ทางทีมงานจะไม่รับฟังข้อโต้แย้งใด ๆ ทั้งสิ้น
6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.4.ห้ามมิให้ผู้เข้าแข่งขันทุกคนอนุญาตให้บุคคลอื่นเล่นแทนตนเองในขณะทำการแข่งขัน
6.1.4.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
6.1.5.ห้ามมิให้ผู้เข้าแข่งขันเสพ ค้า หรือดำเนินการใด ๆ อันเกี่ยวกับยาเสพติด บุหรี่ และอาวุธ และอื่น ๆ ที่ต้องห้ามตามกฎหมายการแข่งขันทันที
6.1.5.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจาก

**English draft**

6. Misconduct and Penalties 6.1. No competitor shall engage in any of the following acts: 6.1.1. No player shall use inappropriate language or display disrespectful behavior or make offensive remarks about others. 6.1.1.1. Penalty: Immediate loss of game upon detection of misconduct. 6.1.2. No competitor shall submit false results or manipulate outcomes. 6.1.2.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.3. No team may allow any individual not listed on their official roster to participate in the competition. If it is discovered that a competitor’s name does not match the registered list, evidence must be recorded and the match shall be terminated immediately. However, if the match proceeds to completion, both teams shall be deemed to have consented to the competition, and no appeals will be entertained by the organizing team. 6.1.3.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.4. No competitor may allow any other individual to play in their place during a match. 6.1.4.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition. 6.1.5. No competitor shall consume, trade, or engage in any activity involving prohibited substances such as narcotics, tobacco, weapons, or other items banned under competition regulations. 6.1.5.1. Penalty: Immediate loss of game upon detection of misconduct and immediate disqualification of the offending team from the competition.

## 207. competition_rules_rov_blueket_2025_men_s08_c01 / title

- Selector: `competition_rules_rov_blueket_2025_men_s08_c01:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `df68af15dcbe4167e27c61538c8c3fa6b823ceeff968c1b80cd87c3b96d014d0`

**Thai source**

Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ

**English draft**

Arena of Valor (RoV): 6. Misconduct and Penalties

## 208. competition_rules_rov_blueket_2025_men_s08_c02 / section_title

- Selector: `competition_rules_rov_blueket_2025_men_s08_c02:section_title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `8fb284ce4ece5b0fbefb09876dfee2df7b0a72b250aba064c0bfad58dd9b2fa7`

**Thai source**

6. การกระทำความผิดและบทลงโทษ

**English draft**

Offenses and Penalties

## 209. competition_rules_rov_blueket_2025_men_s08_c02 / text

- Selector: `competition_rules_rov_blueket_2025_men_s08_c02:text`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `9f44ba70a9661972292e25612c1be713bbb49feafa0ac37e3af698b8ab559eb7`

**Thai source**

6.2. การใช้โปรแกรมช่วยเหลือในการเล่น และ/หรือ การกระทำใด ๆ อันเป็นการทำให้เกิดการได้เปรียบหรือเสียเปรียบต่อตนเองหรือผู้เข้าแข่งขันคนอื่น
6.2.1.ห้ามผู้เข้าแข่งขันทุกคนใช้โปรแกรมช่วยหรือในการเล่นใด ๆ ทั้งสิ้น
6.2.2.ห้ามผู้เข้าแข่งขันทุกคนกระทำการอย่างหนึ่งอย่างใดอันมีลักษณะเป็นการใช้ข้อผิดพลาดที่เกิดขึ้นภายในตัวเกม
6.2.3.ห้ามผู้เข้าแข่งขันทุกคนกระทำการจงใจหลุดจากการแข่งขัน
6.2.4.ห้ามผู้เข้าแข่งขันทุกคนกระทำการใด ๆ อันเป็นการยินยอมให้ทีมฝ่ายตรงข้ามชนะ
6.2.4.1. บทลงโทษ: หากทางทีมงานตรวจสอบพบ หรือได้รับการร้องเรียนจากผู้อื่น ทีมงานจะมีมาตรการลงโทษผู้เข้าแข่งขันที่ฝ่าฝืนกติกา โดยตัดสิทธิ์การเข้าร่วมแข่งขัน

**English draft**

6.2. Use of assistive software during gameplay, and/or any action that creates an advantage or disadvantage to oneself or another competitor 6.2.1. No competitor may use any assistive software or tools during gameplay. 6.2.2. No competitor may perform any action involving exploiting in-game errors. 6.2.3. No competitor may intentionally disengage from the competition. 6.2.4. No competitor may take any action that constitutes allowing the opposing team to win. 6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

## 210. competition_rules_rov_blueket_2025_men_s08_c02 / title

- Selector: `competition_rules_rov_blueket_2025_men_s08_c02:title`
- Category: `competition_rules`
- Title: Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ
- Source hash: `df68af15dcbe4167e27c61538c8c3fa6b823ceeff968c1b80cd87c3b96d014d0`

**Thai source**

Arena of Valor (RoV): 6. การกระทำความผิดและบทลงโทษ

**English draft**

Arena of Valor (RoV): 6. Misconduct and Penalties

## 211. competition_rules_tekken8_psu_esports_s01_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s01_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: ภาพรวมเอกสาร
- Source hash: `fa88e9d3bfec10aad1ecdd09982166ee672fbb3680827323abb6b32f5c8c50a3`

**Thai source**

ภาพรวมเอกสาร

**English draft**

Overview of Document

## 212. competition_rules_tekken8_psu_esports_s01_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s01_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: ภาพรวมเอกสาร
- Source hash: `5728fa3f1ad0dbaedaf16410b179159c4185d512680bd72c82f5e9876f5918dc`

**Thai source**

กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ

**English draft**

Competition Rules and Format for Tekken 8 Event PSU Esports Clash

## 213. competition_rules_tekken8_psu_esports_s01_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s01_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: ภาพรวมเอกสาร
- Source hash: `91d2622e303dc6d3e06ce52051af31c46cb2039531f4743f8816ad377a5e3075`

**Thai source**

Tekken 8: ภาพรวมเอกสาร

**English draft**

Tekken 8: Overview Document

## 214. competition_rules_tekken8_psu_esports_s02_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s02_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: กติกาการแข่งขัน
- Source hash: `f11e59557a88f29a2760e0dc7a21cfe9d405e2fb95685fa37c8eb5bf1ef7c634`

**Thai source**

กติกาการแข่งขัน

**English draft**

Competition Rules

## 215. competition_rules_tekken8_psu_esports_s02_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s02_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: กติกาการแข่งขัน
- Source hash: `edc60f7da178b29666c874f1ae9471889b4f874bc64a4e49624c1df11bfa4aad`

**Thai source**

กติกาการแข่งขัน
* แข่งขันแบบ ออฟไลน์ (Offline)
* ใช้เครื่องเกม PlayStation 5
* แข่งขันแบบ เดี่ยว (1v1)
* รูปแบบการแข่งขัน:
* FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน
* ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)
* หากเสมอกันที่ 1-1 จะต้องแข่งขัน เกมตัดสิน

**English draft**

Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played

## 216. competition_rules_tekken8_psu_esports_s02_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s02_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: กติกาการแข่งขัน
- Source hash: `04de97826eeb29c8bbd77bf507d430f0553233fb21b45767877ed40f76e2df2e`

**Thai source**

Tekken 8: กติกาการแข่งขัน

**English draft**

Tekken 8: Competition Rules

## 217. competition_rules_tekken8_psu_esports_s03_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s03_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: ตัวละครและการตั้งค่า
- Source hash: `6b77afb7682b98d4f58fabfbd56a51171f5eed7d1746dea06d0b463a910eb1cc`

**Thai source**

ตัวละครและการตั้งค่า

**English draft**

Characters and Setup

## 218. competition_rules_tekken8_psu_esports_s03_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s03_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: ตัวละครและการตั้งค่า
- Source hash: `8bd844d467a1b0ff7b47b68610e5a8dc605d07fc097e9113b9daa01c0a949f57`

**Thai source**

ตัวละครและการตั้งค่า
* สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)
* ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
* ต้องใช้ สกินมาตรฐาน เท่านั้น
* อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ
* ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ
* เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
* หากมีการกดหยุดเกมโดยเจตนา จะถูก ปรับแพ้ 1 รอบทันที

**English draft**

Characters and Setup * Any character can be selected (except DLC characters) * No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) * Only standard skins are permitted * Assist buttons or special assist systems are allowed * No use of bugs or glitches that provide an advantage * Once the game starts, no game pausing for any reason is permitted * Any intentional game pause will result in a penalty of losing one round immediately

## 219. competition_rules_tekken8_psu_esports_s03_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s03_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: ตัวละครและการตั้งค่า
- Source hash: `d5fc76095ad5aab8eed70290b34fe3bfc12ea820e4c14463051b9f5cea008fec`

**Thai source**

Tekken 8: ตัวละครและการตั้งค่า

**English draft**

Tekken 8: Characters and Settings

## 220. competition_rules_tekken8_psu_esports_s04_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s04_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: การตั้งค่าเกม
- Source hash: `98bb91b29b2cc850f47db8eccf08e24a447ba2035d39852865e457a419da9cd0`

**Thai source**

การตั้งค่าเกม

**English draft**

Game Settings

## 221. competition_rules_tekken8_psu_esports_s04_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s04_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: การตั้งค่าเกม
- Source hash: `757924c102ab2e9450d63834286ebe88d01ffa05d697c3fd1d0e9544d07cc18c`

**Thai source**

การตั้งค่าเกม
* จำนวนรอบต่อเกม (Round): 3
* เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
* Advantage: No advantage
* Stage: Random

**English draft**

Game Settings * Rounds per game: 3 * Timer per round: 60 seconds * Advantage: None * Stage: Random

## 222. competition_rules_tekken8_psu_esports_s04_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s04_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: การตั้งค่าเกม
- Source hash: `db5f1fd9d39048e9d8b6891b4e300bc56297cbf5d8151bf2ab0dc84db71404b8`

**Thai source**

Tekken 8: การตั้งค่าเกม

**English draft**

Tekken 8: Game Settings

## 223. competition_rules_tekken8_psu_esports_s05_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s05_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: มารยาทในการแข่งขัน
- Source hash: `7a14ca77304c16c0883ea5fbb5c89533c2a055e3c0a2c89b4481c358972afd53`

**Thai source**

มารยาทในการแข่งขัน

**English draft**

Etiquette in Competition

## 224. competition_rules_tekken8_psu_esports_s05_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s05_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: มารยาทในการแข่งขัน
- Source hash: `7ad303f72be0e44c0d7f8d83ee6d0ee04e0c395c25e9654e16f19159655cda40`

**Thai source**

มารยาทในการแข่งขัน
* ห้ามแสดงพฤติกรรมที่ขาดน้ำใจนักกีฬา เช่น การเยาะเย้ย ถากถาง หรือแสดงความไม่สุภาพทั้งทางวาจาและการกระทำต่อผู้อื่น ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น
* ผู้เข้าแข่งขันต้องให้เกียรติผู้ตัดสินและผู้เข้าแข่งขันคนอื่น ห้ามแสดงพฤติกรรมดูถูกหรือไม่ให้เกียรติในทุกกรณี ผู้ที่ฝ่าฝืนจะถูกปรับแพ้ทันทีโดยไม่มีข้อยกเว้น

**English draft**

Etiquette in competition * Prohibited to display behavior lacking sportsmanship, such as mocking, belittling, or showing unsuitable language or actions toward others. Any violation will result in immediate disqualification without exception. * Participants must show respect to referees and other competitors. No conduct showing disrespect or lack of courtesy is allowed. Any violation will result in immediate disqualification without exception.

## 225. competition_rules_tekken8_psu_esports_s05_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s05_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: มารยาทในการแข่งขัน
- Source hash: `6d4b6c7007bf17e3b7b0705238af9147d19dcf2e4d258e923d32e5a3a2af4414`

**Thai source**

Tekken 8: มารยาทในการแข่งขัน

**English draft**

Tekken 8: Etiquette in Competition

## 226. competition_rules_tekken8_psu_esports_s06_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s06_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: ข้อตกลงและข้อปฏิบัติ
- Source hash: `9d204d1d4b919b379811cfff5d0c2ef416fb0b07b479958f84b9fb001b7f6aa0`

**Thai source**

ข้อตกลงและข้อปฏิบัติ

**English draft**

Agreements and Conduct

## 227. competition_rules_tekken8_psu_esports_s06_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s06_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: ข้อตกลงและข้อปฏิบัติ
- Source hash: `41cc3adfea22bd6f466cfa4f7c773000db213c18f1fda6065af55bba2f7c6209`

**Thai source**

ข้อตกลงและข้อปฏิบัติ
* ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
* ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
* คำตัดสินของกรรมการถือเป็นที่สิ้นสุด
* กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม

**English draft**

Agreements and Conduct * All participants must accept and abide by the rules, regulations, and decisions of the judges without exception. * The organizers reserve the right to modify competition rules at any time without prior notice. * The judges' decisions are final. * Judges may revise their decisions as appropriate to ensure fairness.

## 228. competition_rules_tekken8_psu_esports_s06_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s06_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: ข้อตกลงและข้อปฏิบัติ
- Source hash: `d70698d57b831f200e10d043d78ff355eef9c731201de6b75e3fb4a33a3cb070`

**Thai source**

Tekken 8: ข้อตกลงและข้อปฏิบัติ

**English draft**

Tekken 8: Agreement and Conduct

## 229. competition_rules_tekken8_psu_esports_s07_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s07_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: การหยุดเกม
- Source hash: `6f95c3f63c188843350a460a2b75e9f41d998af7928d0d84abbcae846d3656a3`

**Thai source**

การหยุดเกม

**English draft**

Game Pause

## 230. competition_rules_tekken8_psu_esports_s07_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s07_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: การหยุดเกม
- Source hash: `5f08492ed42e855386f704fbd7d536d6eae672be5854e828efd6cac9c3697ca8`

**Thai source**

การหยุดเกม
* ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ
* หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที
* การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน
* หากกดหยุดเกมโดยไม่จำเป็น จะได้รับโทษเช่นเดียวกับการออกจากเกมก่อนจบ

**English draft**

Game Pause * Players must not leave the game before the competition ends unless authorized by the referees. * If a player leaves the game without authorization, they will be forfeited immediately. * The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency. * Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

## 231. competition_rules_tekken8_psu_esports_s07_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s07_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: การหยุดเกม
- Source hash: `9799a0f8ef57ad441f6149d27a68dfe2bb1004a7be3bdb85aed78cb85d091a79`

**Thai source**

Tekken 8: การหยุดเกม

**English draft**

Tekken 8: Game Pause

## 232. competition_rules_tekken8_psu_esports_s08_c01 / section_title

- Selector: `competition_rules_tekken8_psu_esports_s08_c01:section_title`
- Category: `competition_rules`
- Title: Tekken 8: การแก้ปัญหาข้อพิพาท
- Source hash: `4495d194b75bd5d11158c605f1419250d3d6207e2caeb0ffa3a4d6fff795d64c`

**Thai source**

การแก้ปัญหาข้อพิพาท

**English draft**

Dispute Resolution

## 233. competition_rules_tekken8_psu_esports_s08_c01 / text

- Selector: `competition_rules_tekken8_psu_esports_s08_c01:text`
- Category: `competition_rules`
- Title: Tekken 8: การแก้ปัญหาข้อพิพาท
- Source hash: `879a81ab88af94d7fd0fd8ade6bc1cc6a8282da49e36f1c9245893f1648bb7a2`

**Thai source**

การแก้ปัญหาข้อพิพาท
* หากเกิดปัญหาใด ๆ ต้องแจ้งผู้จัดการแข่งขันทันที
* ในกรณีเกิดข้อโต้แย้งหรือการประท้วง คำตัดสินของผู้ดูแลหรือกรรมการจะถือเป็นที่สิ้นสุด
หมายเหตุ: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า

**English draft**

Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.

## 234. competition_rules_tekken8_psu_esports_s08_c01 / title

- Selector: `competition_rules_tekken8_psu_esports_s08_c01:title`
- Category: `competition_rules`
- Title: Tekken 8: การแก้ปัญหาข้อพิพาท
- Source hash: `cb8124fca628fb80ed93d7cb97bfbab0b47ba71033d39bc1968675fd70d4ab63`

**Thai source**

Tekken 8: การแก้ปัญหาข้อพิพาท

**English draft**

Tekken 8: Dispute Resolution

## 235. competition_rules_valorant_psu_phuket_2026_s01_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s01_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: ภาพรวมเอกสาร
- Source hash: `fa88e9d3bfec10aad1ecdd09982166ee672fbb3680827323abb6b32f5c8c50a3`

**Thai source**

ภาพรวมเอกสาร

**English draft**

Overview of Document

## 236. competition_rules_valorant_psu_phuket_2026_s01_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s01_c01:text`
- Category: `competition_rules`
- Title: VALORANT: ภาพรวมเอกสาร
- Source hash: `674c9ce58eb0c261812bf2704777282083065b135a7b75dde5b9660fca6dc1ef`

**Thai source**

กฎระเบียบและรูปแบบการแข่งขัน VALORANT
รายการ PSU Phuket VALORANT 2026 Tournament
Update: 17/02/2026
English below
อุปกรณ์และอุปกรณ์ต่อพ่วง
ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม
* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)
* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้
* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น
* ข้อห้ามสำคัญ
* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้
* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

**English draft**

Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. * Self-provided equipment: Keyboard (wired/wireless), Mouse (wired/wireless), Mouse bungee, Mouse pad, In-ear headset (wired), Wired headset * Equipment provided by organizers: Organizers will provide PCs, monitors, headsets with microphones, tables, and chairs. * Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials. * Prohibited items: * Macros (both software- and hardware-based) are strictly prohibited. * Installing any unauthorized programs on the provided computers is strictly prohibited. * Accessing social media or any communication websites on competition computers is strictly prohibited, except for programs provided by organizers.

## 237. competition_rules_valorant_psu_phuket_2026_s01_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s01_c01:title`
- Category: `competition_rules`
- Title: VALORANT: ภาพรวมเอกสาร
- Source hash: `2ff25317c38e7ca0fec3ad70f4d3bc6100584d3644fd15f61c80b9144fecaba7`

**Thai source**

VALORANT: ภาพรวมเอกสาร

**English draft**

VALORANT: Overview Document

## 238. competition_rules_valorant_psu_phuket_2026_s02_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s02_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `303388cb0027d1b6ce5c96e3f7767aa6ba537fbdb8bf2fdd055cb2f1e3a1d891`

**Thai source**

พื้นที่การแข่งขันและกฎระเบียบ

**English draft**

Competition Venue and Regulations

## 239. competition_rules_valorant_psu_phuket_2026_s02_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s02_c01:text`
- Category: `competition_rules`
- Title: VALORANT: พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `5057afc56c92f944deea6b41c4b7ccb4a2a82970a05146896b3d8cb6ef2a7282`

**Thai source**

พื้นที่การแข่งขันและกฎระเบียบ
* จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
* อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์
* เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง
* อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น
กระบวนการแข่งขัน

**English draft**

Competition Venue and Regulations * During Match Prep, the number of personnel allowed on-site shall not exceed six players. * Electronic devices: Mobile phones, tablets, or smartwatches are prohibited in the competition venue until the match concludes. * Documents and notes: Players are not permitted to bring notes or documents into the venue. However, team captains may enter documents and must submit them to the referees prior to each match. * Food and beverages: Only sealed bottled water and checkers are allowed.

## 240. competition_rules_valorant_psu_phuket_2026_s02_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s02_c01:title`
- Category: `competition_rules`
- Title: VALORANT: พื้นที่การแข่งขันและกฎระเบียบ
- Source hash: `ab591f015f922d567704cc77df4c65fc80000f7a028e4bdf6f1aa16a3989819b`

**Thai source**

VALORANT: พื้นที่การแข่งขันและกฎระเบียบ

**English draft**

VALORANT: Match Area and Rules

## 241. competition_rules_valorant_psu_phuket_2026_s03_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s03_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร
- Source hash: `9d801d149f373f84f00c761bc4373e9546833c9ced15f62e944bcf9ba5524450`

**Thai source**

ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร

**English draft**

Steps from before the game starts to character selection

## 242. competition_rules_valorant_psu_phuket_2026_s03_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s03_c01:text`
- Category: `competition_rules`
- Title: VALORANT: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร
- Source hash: `cbe6576e922fbf445aebde18945b6dcffe4265a988342cb8df7bd14fa7d4e19a`

**Thai source**

ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร
* เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง
* ข้อจำกัดเนื้อหาใหม่
* เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
* แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
* การตั้งค่าเกม (Settings)
* ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
* ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน
* การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่
* Abyss
* Ascent
* Bind
* Corrode
* Haven
* Lotus
* Sunset
* การเลือกฝั่ง
* ใช้วิธีการโยนเหรียญ
* การ Ban map
* แบนจนเหลือ 3 แผนที่

**English draft**

Steps from before the game starts until character selection * Reporting time: players must arrive at the venue at least 30 minutes before the scheduled start time. * New content restrictions * New agents will be restricted and unavailable for approximately 2 weeks after being released in Competitive mode. * New maps will be restricted and unavailable for approximately 4 weeks after being released in Competitive mode. * Game settings * Players must turn OFF Blood and Bodies visuals. * FPS or Latency display during gameplay is prohibited. * Map Pool: consists of 7 maps as specified, namely: * Abyss * Ascent * Bind * Corrode * Haven * Lotus * Sunset * Team selection * Coin toss method will be used. * Map banning * Ban until only 3 maps remain.

## 243. competition_rules_valorant_psu_phuket_2026_s03_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s03_c01:title`
- Category: `competition_rules`
- Title: VALORANT: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร
- Source hash: `6b0649e87c135cba3c16b0e6af90e8948141998575659fcc782338094098ce65`

**Thai source**

VALORANT: ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร

**English draft**

VALORANT: Steps from before the game starts to agent selection

## 244. competition_rules_valorant_psu_phuket_2026_s04_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s04_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: กระบวนการหลังจบแมตช์
- Source hash: `e9ae6b5b6c30ca41243b8edaf414f87b2cdf70b576348f699fd45986fcc0577e`

**Thai source**

กระบวนการหลังจบแมตช์

**English draft**

Post-Match Process

## 245. competition_rules_valorant_psu_phuket_2026_s04_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s04_c01:text`
- Category: `competition_rules`
- Title: VALORANT: กระบวนการหลังจบแมตช์
- Source hash: `4b950c859236fc859ab97f761864fda9b9f698bf26c341a9694ef52a35c036a0`

**Thai source**

กระบวนการหลังจบแมตช์
* การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที
* การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0
การหยุดเกม

**English draft**

Post-match process * Result recording: Officials will confirm and record the match result immediately. * Forfeiture: If a team forfeits, the map result will be recorded as 13-0. Game pause

## 246. competition_rules_valorant_psu_phuket_2026_s04_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s04_c01:title`
- Category: `competition_rules`
- Title: VALORANT: กระบวนการหลังจบแมตช์
- Source hash: `49cba2605498e23d3cd7469116b2c560d8415a43ad96da2c4954192e40f46524`

**Thai source**

VALORANT: กระบวนการหลังจบแมตช์

**English draft**

VALORANT: Post-Match Process

## 247. competition_rules_valorant_psu_phuket_2026_s05_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s05_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- Source hash: `afa4da7782a47d9c1a50a7660d74046a0e957adeb70df5094947c7994274cecb`

**Thai source**

การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน

**English draft**

Game pauses are divided into three main types for different reasons

## 248. competition_rules_valorant_psu_phuket_2026_s05_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s05_c01:text`
- Category: `competition_rules`
- Title: VALORANT: การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- Source hash: `afa4da7782a47d9c1a50a7660d74046a0e957adeb70df5094947c7994274cecb`

**Thai source**

การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน

**English draft**

Game pauses are divided into three main types for different reasons.

## 249. competition_rules_valorant_psu_phuket_2026_s05_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s05_c01:title`
- Category: `competition_rules`
- Title: VALORANT: การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน
- Source hash: `714af8b23d2a85eee83a29a74842df8f52c5574829c26207a4e6dad9462229f4`

**Thai source**

VALORANT: การหยุดเกมแบ่งออกเป็น 3 ประเภทหลัก เพื่อเหตุผลที่แตกต่างกัน

**English draft**

VALORANT: Game pauses are divided into three main types for different reasons

## 250. competition_rules_valorant_psu_phuket_2026_s06_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s06_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- Source hash: `1dc62ad40c9cc4de3dceb5580c50d56396a7edb5dc0341fbb7a10fef03620aa5`

**Thai source**

1. เวลานอกทางยุทธวิธี (Tactical Timeout)

**English draft**

Strategic Timeout

## 251. competition_rules_valorant_psu_phuket_2026_s06_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s06_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- Source hash: `0077e93003a4ce3d7c7f8d6bf3cc422adf1132ddb5bb957f7648d97268828087`

**Thai source**

1. เวลานอกทางยุทธวิธี (Tactical Timeout)
* ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
* เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

**English draft**

Tactical Timeout * Requested twice per map during regular rounds (first 24 rounds), each lasting 60 seconds. * During Overtime, an additional timeout is granted to each team, with quotas from regular rounds not carried over.

## 252. competition_rules_valorant_psu_phuket_2026_s06_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s06_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)
- Source hash: `f07028d28207f56bf28cd6024fe842b8a7d63833ca1a9c4db3d954b1b45f3630`

**Thai source**

VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)

**English draft**

VALORANT: 1. Tactical Timeout

## 253. competition_rules_valorant_psu_phuket_2026_s07_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s07_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 2. การหยุดเกมทางเทคนิค (Technical Pause)
- Source hash: `f0c18873ae9d863469d313aa115c1d5bdec282d782defc444e9fea4dc3540efc`

**Thai source**

2. การหยุดเกมทางเทคนิค (Technical Pause)

**English draft**

Technical Pause

## 254. competition_rules_valorant_psu_phuket_2026_s07_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s07_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 2. การหยุดเกมทางเทคนิค (Technical Pause)
- Source hash: `2d2bc4219a36a37c08e5426e41f7fcc54beca1fcb6f581fa748c109a2bd8ba8c`

**Thai source**

2. การหยุดเกมทางเทคนิค (Technical Pause)
* ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์
* ห้ามผู้เล่นสื่อสารกัน (ทั้งเสียงและข้อความ) เว้นแต่ได้รับอนุญาต

**English draft**

Technical Pause * Used when there are device malfunctions, disconnections, or software issues * Players must not communicate with each other (either verbally or in text) unless authorized

## 255. competition_rules_valorant_psu_phuket_2026_s07_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s07_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 2. การหยุดเกมทางเทคนิค (Technical Pause)
- Source hash: `9aa00919cdefd17fe836abf29bc20f6c3e07edd128225738e0fa7df218d2313d`

**Thai source**

VALORANT: 2. การหยุดเกมทางเทคนิค (Technical Pause)

**English draft**

VALORANT: 2. Technical Pause

## 256. competition_rules_valorant_psu_phuket_2026_s08_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s08_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- Source hash: `018d6f2b67488add245a0bd365ff8ad2dc8ccdce22ae8091f97e84777778f3cb`

**Thai source**

3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)

**English draft**

Emergency Pause Clause (Player Emergency Pause)

## 257. competition_rules_valorant_psu_phuket_2026_s08_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s08_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- Source hash: `cce855d13600dc1c7b7526393ed2bb5e19ef57e637ae4282eff86b1da617c80f`

**Thai source**

3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
* ขอได้ 1 ครั้งต่อแผนที่
* รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน
กฎเกี่ยวกับบั๊ก
บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้
* Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
* Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
* Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้
* การย้อนรอบ (Round Rollback)
* หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
* หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge
* หากเป็น Game Breaking Bug เจ้าหน้าที่จะสั่งย้อนรอบไปยังจุดเริ่มต้นของรอบนั้นทันที
การใช้ช่องโหว่ (Exploit Adjudication)

**English draft**

Emergency Pause (Player Emergency Pause) * One emergency pause allowed per map * Total duration per match cannot exceed 10 minutes. If exceeded, the player may be disqualified and must be replaced by a backup player. Bug Rules A bug is an unintended game outcome caused by an error in gameplay. Bugs are categorized to determine appropriate procedures as follows: * Play Through Bug: A bug that does not significantly affect fairness. The player must continue playing and cannot request a challenge. * Major Bug: A bug that severely impacts gameplay or game mechanics and has no immediate fix. The team may request a challenge for review. * Game Breaking Bug: A bug that undermines the fairness of the round to the point where match outcome cannot be determined. Round Rollback * If a bug occurs before any damage is dealt, officials may perform a rollback. * If damage has already been dealt, no rollback will occur unless through a challenge process. * If it is a Game Breaking Bug, officials will immediately roll back the round to its starting point.

## 258. competition_rules_valorant_psu_phuket_2026_s08_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s08_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)
- Source hash: `fa005b17243ded8a0edf2ae4e60347992b60f8c4539a28e9f0e2d1aaf19400b4`

**Thai source**

VALORANT: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)

**English draft**

VALORANT: Emergency Pause Rule

## 259. competition_rules_valorant_psu_phuket_2026_s09_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s09_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด
- Source hash: `36f7585203cdcb1ce65a8b62a2500b3b4241c2cd8dcd3d64ac5046d3ec7e1d64`

**Thai source**

การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด

**English draft**

Using bugs caused by the player themselves to gain unintended advantages is considered a violation

## 260. competition_rules_valorant_psu_phuket_2026_s09_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s09_c01:text`
- Category: `competition_rules`
- Title: VALORANT: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด
- Source hash: `67c9eaa2e70e0c7f1d94ef479709d68909d76215a32046bfd4c7d03437d90eee`

**Thai source**

การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด
* การใช้สกิลเอเจนท์
* ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่
* ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
* ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง
* การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ
บทลงโทษ
เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact)

**English draft**

Using bugs caused by the player themselves to gain unintended advantages is considered a violation. * Using agent skills * Prohibited from placing Cypher's camera in invisible spots or areas that cannot be destroyed through texture penetration on the map * Prohibited from using skills outside the map boundaries (Out of boundaries) to gather information or create an advantage * Exception: KAY/O's ZERO/POINT skill can be used outside the map or in destructible areas, but the character's blade is prohibited from penetrating textures that should be solid * Jumping on teammates: Prohibited from using teammates' characters to jump to points higher than normal jump range Penalties Officials will assess penalties based on intent and impact.

## 261. competition_rules_valorant_psu_phuket_2026_s09_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s09_c01:title`
- Category: `competition_rules`
- Title: VALORANT: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด
- Source hash: `ef9f24f12bb3ef4705b1331b937286a558a991aa7ef594a868781777bb2df864`

**Thai source**

VALORANT: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด

**English draft**

VALORANT: Using bugs caused by the player themselves to gain an unintended advantage is considered a violation

## 262. competition_rules_valorant_psu_phuket_2026_s10_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s10_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: ประเภทบทลงโทษในเกม
- Source hash: `50c124a7ac5374f8061289fbf8d183b2191e83546cbe7a48437bf161a4d385d9`

**Thai source**

ประเภทบทลงโทษในเกม

**English draft**

Penalty Types in the Game

## 263. competition_rules_valorant_psu_phuket_2026_s10_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s10_c01:text`
- Category: `competition_rules`
- Title: VALORANT: ประเภทบทลงโทษในเกม
- Source hash: `50c124a7ac5374f8061289fbf8d183b2191e83546cbe7a48437bf161a4d385d9`

**Thai source**

ประเภทบทลงโทษในเกม

**English draft**

Penalty types in the game

## 264. competition_rules_valorant_psu_phuket_2026_s10_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s10_c01:title`
- Category: `competition_rules`
- Title: VALORANT: ประเภทบทลงโทษในเกม
- Source hash: `54c20553fb6f874b14d2b514613ff209e618e50ef204cb6c523fe6d9cb670e79`

**Thai source**

VALORANT: ประเภทบทลงโทษในเกม

**English draft**

VALORANT: Types of In-Game Penalties

## 265. competition_rules_valorant_psu_phuket_2026_s11_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s11_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ
- Source hash: `cf91b5ed6c474d57f375c1c122945857f991bab651132025bfbaf0a30cbd7859`

**Thai source**

1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ

**English draft**

Warning for first offense with minimal impact

## 266. competition_rules_valorant_psu_phuket_2026_s11_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s11_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ
- Source hash: `cf91b5ed6c474d57f375c1c122945857f991bab651132025bfbaf0a30cbd7859`

**Thai source**

1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ

**English draft**

Warning for the first offense with minimal impact

## 267. competition_rules_valorant_psu_phuket_2026_s11_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s11_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ
- Source hash: `400a8ef00d316fea54cd33dc77f9d751fcc605cd95140af24568b8c2cd87341e`

**Thai source**

VALORANT: 1. การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ

**English draft**

VALORANT: 1. First offense warning for minor infractions

## 268. competition_rules_valorant_psu_phuket_2026_s12_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s12_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้
- Source hash: `0bd8502cf35d0b7ed57a159f636758758ad88470620a03b1ef9fb8c07f1048f2`

**Thai source**

2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้

**English draft**

Round Rollback when exploiting a vulnerability clearly affects the round but intent is not identifiable

## 269. competition_rules_valorant_psu_phuket_2026_s12_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s12_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้
- Source hash: `0bd8502cf35d0b7ed57a159f636758758ad88470620a03b1ef9fb8c07f1048f2`

**Thai source**

2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้

**English draft**

Round Rollback when exploiting a vulnerability clearly affects the round but intent cannot be determined

## 270. competition_rules_valorant_psu_phuket_2026_s12_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s12_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้
- Source hash: `137f1163e39da7b8e7b56559b6a6e0672f0bd69a09cad7d2a150f7bbe58311e3`

**Thai source**

VALORANT: 2. การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้

**English draft**

VALORANT: Round Rollback Rule 2. When exploiting a vulnerability clearly affects the round but intent cannot be determined

## 271. competition_rules_valorant_psu_phuket_2026_s13_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s13_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ
- Source hash: `2c862fa3f25582c95c9406920ca68e3891e21b74d7475f2b38d04b96df9ea9b1`

**Thai source**

3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

**English draft**

Adjustment for Round Loss: When it is found that a player or team intentionally exploits a vulnerability to gain an advantage

## 272. competition_rules_valorant_psu_phuket_2026_s13_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s13_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ
- Source hash: `2c862fa3f25582c95c9406920ca68e3891e21b74d7475f2b38d04b96df9ea9b1`

**Thai source**

3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

**English draft**

Adjustment for Round Loss when it is found that a player or team intentionally exploits a vulnerability to gain an advantage

## 273. competition_rules_valorant_psu_phuket_2026_s13_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s13_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ
- Source hash: `62f6b73f309b1b75e54ecfac66a223da6d2386bdba7361db0a5818306cd2ff28`

**Thai source**

VALORANT: 3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

**English draft**

VALORANT: 3. Round Loss Adjustment for exploiting vulnerabilities to gain an advantage

## 274. competition_rules_valorant_psu_phuket_2026_s14_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s14_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น
- Source hash: `22c5ed1702ee1264b504b7e5ffde603ec63cff56a03c58e4e57528e8b1de835e`

**Thai source**

4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น

**English draft**

Section Title: Map Forfeit for Serious or Repeated Violations Affecting Match Outcome

## 275. competition_rules_valorant_psu_phuket_2026_s14_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s14_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น
- Source hash: `22c5ed1702ee1264b504b7e5ffde603ec63cff56a03c58e4e57528e8b1de835e`

**Thai source**

4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น

**English draft**

Map Forfeit for serious violations or repeated infractions that negatively impact the outcome of a map

## 276. competition_rules_valorant_psu_phuket_2026_s14_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s14_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น
- Source hash: `56e446122598ba5cbe446d2922a4321c7f338e9dd3e3544faba24ddc2fe811bc`

**Thai source**

VALORANT: 4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น

**English draft**

VALORANT: 4. Map Forfeit for Serious Violations or Repeated Offenses That Affect Match Results

## 277. competition_rules_valorant_psu_phuket_2026_s15_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s15_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)
- Source hash: `ac6c35cff29998f8f02d5fcba8f3b585a41eeaf45630072379be42dce4393b46`

**Thai source**

5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)

**English draft**

Section Title: Match Forfeit Due to Cheating or Match Fixing

## 278. competition_rules_valorant_psu_phuket_2026_s15_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s15_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)
- Source hash: `ac6c35cff29998f8f02d5fcba8f3b585a41eeaf45630072379be42dce4393b46`

**Thai source**

5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)

**English draft**

5. Match Forfeit in cases of cheating or match fixing

## 279. competition_rules_valorant_psu_phuket_2026_s15_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s15_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)
- Source hash: `2119bcdfd62597a5db050401f636c39a693bbbe5f8a26c9b05c5bd0b6b391560`

**Thai source**

VALORANT: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)

**English draft**

VALORANT: 5. Match Forfeit due to Cheating or Match Fixing

## 280. competition_rules_valorant_psu_phuket_2026_s16_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s16_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- Source hash: `2fb1362784472ec115ffe255982f84168b89afe937d99cb43a06992c534c4623`

**Thai source**

ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า

**English draft**

Organizers reserve the right to amend or modify competition rules without prior notice

## 281. competition_rules_valorant_psu_phuket_2026_s16_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s16_c01:text`
- Category: `competition_rules`
- Title: VALORANT: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- Source hash: `0772f4cb0c7b73a84f0a44fc0a951c2b1187b509d1ca776254fd003bbdb03c97`

**Thai source**

ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
--------------------------------------------------------------------------------------
English
Equipment and Peripherals
In LAN competitions, players must strictly comply with equipment regulations to ensure fair play.
* Allowed personal equipment
* Players may bring and use their own keyboard (wired/wireless), mouse (wired/wireless), mouse bungee, mouse pad, In-ear earphones (wired), headset (wired).
* Equipment provided by the organizer
* The organizer will provide PCs, monitors, headsets with microphones, desks, and chairs.
* Keyboard technology
* The use of Snap Tap, SOCD, or equivalent technologies is permitted, unless otherwise instructed by officials.
* Key Prohibitions
* The use of macros (configured via software or hardware) is strictly prohibited.
* Players may not install any software on the provided competition computers.
* Access to any social media or communication websites on the competition computers is strictly prohibited, except for the programs provided by the organizers.

**English draft**

The Organizer reserves the right to modify or amend the regulations without prior notice.

## 282. competition_rules_valorant_psu_phuket_2026_s16_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s16_c01:title`
- Category: `competition_rules`
- Title: VALORANT: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
- Source hash: `b88d6d281d3d1cb203be7b092e4f8c15c7c7471bdddfcc76c0b9c7912436b01e`

**Thai source**

VALORANT: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า

**English draft**

VALORANT: The competition organizers reserve the right to amend or modify rules without prior notice

## 283. competition_rules_valorant_psu_phuket_2026_s17_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s17_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: Competition Area and Regulations
- Source hash: `20a150ba66db37b4d49ea13e4cb7f7ce5561c9fe0820d9dd6b9a2561ff4b9028`

**Thai source**

Competition Area and Regulations

**English draft**

Competition Area and Regulations

## 284. competition_rules_valorant_psu_phuket_2026_s17_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s17_c01:text`
- Category: `competition_rules`
- Title: VALORANT: Competition Area and Regulations
- Source hash: `64e6a86dd6162e721aa9a143e276eb5339a93623c7a2e17b7f51c8156462e54c`

**Thai source**

Competition Area and Regulations
* Personnel during Match Preparation
* No more than 6 players are allowed in the match preparation area.
* Electronic devices
* Mobile phones, tablets, and smartwatches are strictly prohibited in the competition area until the match has concluded.
* Documents and notes
* Players may not bring notes or documents into the competition area.
* The team captain is allowed to bring documents, which must be submitted to the referee before the match.
* Food and beverages
* Only drinking water in a sealed container and chewing gum are permitted.
Match Procedure

**English draft**

Competition Area and Regulations * Personnel during Match Preparation * No more than 6 players are allowed in the match preparation area. * Electronic devices * Mobile phones, tablets, and smartwatches are strictly prohibited in the competition area until the match has concluded. * Documents and notes * Players may not bring notes or documents into the competition area. * The team captain is allowed to bring documents, which must be submitted to the referee before the match. * Food and beverages * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure

## 285. competition_rules_valorant_psu_phuket_2026_s17_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s17_c01:title`
- Category: `competition_rules`
- Title: VALORANT: Competition Area and Regulations
- Source hash: `047d87a4da249edd62a0804d6e4f5f012a737c307ff7cf0daf6a0e7179c7279c`

**Thai source**

VALORANT: Competition Area and Regulations

**English draft**

VALORANT: Competition Area and Regulations

## 286. competition_rules_valorant_psu_phuket_2026_s18_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s18_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: Pre-Game Process (Before Game Start to Agent Selection)
- Source hash: `512fd746dde460f2e39455a7110da17380589707413e27e87ace0c177ddf8431`

**Thai source**

Pre-Game Process (Before Game Start to Agent Selection)

**English draft**

Pre-Game Process (Before Game Start to Agent Selection)

## 287. competition_rules_valorant_psu_phuket_2026_s18_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s18_c01:text`
- Category: `competition_rules`
- Title: VALORANT: Pre-Game Process (Before Game Start to Agent Selection)
- Source hash: `e6e6253566f51565a0b1524151ea77d9b15a54e05f78e09c3283541e940b21fe`

**Thai source**

Pre-Game Process (Before Game Start to Agent Selection)
* Check-in time
* Teams must arrive at the venue at least 30 minutes before the scheduled match time.
* New Content Restrictions
* New agents are restricted for approximately 2 weeks after being released in Competitive mode.
* New maps are restricted for approximately 4 weeks after being released in Competitive mode.
* Game Settings
* Players must turn OFF blood and body displays.
* Displaying FPS or latency graphs during competition is prohibited.
* Map Pool
* The map pool consists of the following 7 maps
- Abyss
- Ascent
- Bind
- Corrode
- Haven
- Lotus
- Sunset
* Map Ban
* Ban maps until 3 maps remain

**English draft**

Pre-Game Process (Before Game Start to Agent Selection) * Check-in time * Teams must arrive at the venue at least 30 minutes before the scheduled match time. * New Content Restrictions * New agents are restricted for approximately 2 weeks after being released in Competitive mode. * New maps are restricted for approximately 4 weeks after being released in Competitive mode. * Game Settings * Players must turn OFF blood and body displays. * Displaying FPS or latency graphs during competition is prohibited. * Map Pool * The map pool consists of the following 7 maps - Abyss - Ascent - Bind - Corrode - Haven - Lotus - Sunset * Map Ban * Ban maps until 3 maps remain

## 288. competition_rules_valorant_psu_phuket_2026_s18_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s18_c01:title`
- Category: `competition_rules`
- Title: VALORANT: Pre-Game Process (Before Game Start to Agent Selection)
- Source hash: `925b77fcbeece07d9ab576db2562e1e3bc89f80ce0bc349190025d3ab73edbdd`

**Thai source**

VALORANT: Pre-Game Process (Before Game Start to Agent Selection)

**English draft**

VALORANT: Pre-Game Process (Before Game Start to Agent Selection)

## 289. competition_rules_valorant_psu_phuket_2026_s19_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s19_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: Post-Match Procedure
- Source hash: `af0387a8a1f2fbd20d32341a22ba6e7938fceb8e872b335741ad5d787d757718`

**Thai source**

Post-Match Procedure

**English draft**

Post-Match Procedure

## 290. competition_rules_valorant_psu_phuket_2026_s19_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s19_c01:text`
- Category: `competition_rules`
- Title: VALORANT: Post-Match Procedure
- Source hash: `1ede57ccd6a1eb35c4e9d41ca750dcb7315448f76ec564a254be525537d5ee80`

**Thai source**

Post-Match Procedure
* Result recording
* Officials will immediately verify and record match results.
* Forfeiture
* If a forfeit occurs, the result for that map will be recorded as 13-0.
Match Pauses

**English draft**

Post-Match Procedure * Result recording * Officials will immediately verify and record match results. * Forfeiture * If a forfeit occurs, the result for that map will be recorded as 13-0. Match Pauses

## 291. competition_rules_valorant_psu_phuket_2026_s19_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s19_c01:title`
- Category: `competition_rules`
- Title: VALORANT: Post-Match Procedure
- Source hash: `29b9e1d0b0214061aa0cc07833379b38e0f1e96647a20bfcb284ee6be1d537b2`

**Thai source**

VALORANT: Post-Match Procedure

**English draft**

VALORANT: Post-Match Procedure

## 292. competition_rules_valorant_psu_phuket_2026_s20_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s20_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: There are three main types of pauses, each for different purposes
- Source hash: `a81253c365c4f262aa4a0011124b71c5cf99b72a6ff45027c2b2ce812b690b16`

**Thai source**

There are three main types of pauses, each for different purposes

**English draft**

There are three main types of pauses, each for different purposes

## 293. competition_rules_valorant_psu_phuket_2026_s20_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s20_c01:text`
- Category: `competition_rules`
- Title: VALORANT: There are three main types of pauses, each for different purposes
- Source hash: `a81253c365c4f262aa4a0011124b71c5cf99b72a6ff45027c2b2ce812b690b16`

**Thai source**

There are three main types of pauses, each for different purposes

**English draft**

There are three main types of pauses, each for different purposes

## 294. competition_rules_valorant_psu_phuket_2026_s20_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s20_c01:title`
- Category: `competition_rules`
- Title: VALORANT: There are three main types of pauses, each for different purposes
- Source hash: `c117b4735b816e49f91623355509405f751a8e102893e11c37f2ff3f9a6de3dc`

**Thai source**

VALORANT: There are three main types of pauses, each for different purposes

**English draft**

VALORANT: There are three main types of pauses, each for different purposes

## 295. competition_rules_valorant_psu_phuket_2026_s21_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s21_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 1. Tactical Timeout
- Source hash: `d954961b591be8d7f369e8e2eb438bbfec80ee1517f2a15a47686554049a303c`

**Thai source**

1. Tactical Timeout

**English draft**

Tactical Timeout

## 296. competition_rules_valorant_psu_phuket_2026_s21_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s21_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 1. Tactical Timeout
- Source hash: `7412ed7c0d184967d23c70b66649c259400865311bf8dac38e6cacb89014bda2`

**Thai source**

1. Tactical Timeout
* Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds.
* During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over.

**English draft**

Tactical Timeout * Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds. * During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over.

## 297. competition_rules_valorant_psu_phuket_2026_s21_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s21_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 1. Tactical Timeout
- Source hash: `465cf90de52871b256b552052274c04d5064b0990a80569d3f32d66570ee24f8`

**Thai source**

VALORANT: 1. Tactical Timeout

**English draft**

VALORANT: 1. Tactical Timeout

## 298. competition_rules_valorant_psu_phuket_2026_s22_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s22_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 2. Technical Pause
- Source hash: `f339886b96c0de9d190c5f003189072012865ed3907256e55eef892be42d294a`

**Thai source**

2. Technical Pause

**English draft**

Technical Pause

## 299. competition_rules_valorant_psu_phuket_2026_s22_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s22_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 2. Technical Pause
- Source hash: `9a632dbafaf6cbe954ae5e5c7bab37ee1d47aff12a4ee2231691ef55d3cee022`

**Thai source**

2. Technical Pause
* Used in cases of hardware malfunction, disconnection, or software issues.
* Players may not communicate (voice or text) unless permitted by officials.

**English draft**

Technical Pause * Used in cases of hardware malfunction, disconnection, or software issues. * Players may not communicate (voice or text) unless permitted by officials.

## 300. competition_rules_valorant_psu_phuket_2026_s22_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s22_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 2. Technical Pause
- Source hash: `527b96085115f1804f6c4f5e43ad70abf9753f377eb08eaf89fdc999460d97af`

**Thai source**

VALORANT: 2. Technical Pause

**English draft**

VALORANT: 2. Technical Pause

## 301. competition_rules_valorant_psu_phuket_2026_s23_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s23_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: 3. Player Emergency Pause
- Source hash: `3ff60bbe04ff568430ba998ce11a5b922e069de99928cf3c8e7bdbb1c5a27783`

**Thai source**

3. Player Emergency Pause

**English draft**

Player Emergency Pause

## 302. competition_rules_valorant_psu_phuket_2026_s23_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s23_c01:text`
- Category: `competition_rules`
- Title: VALORANT: 3. Player Emergency Pause
- Source hash: `89cb621412f77546390c36f721c8167017e4424bd3e4458488de3ad8446b33c3`

**Thai source**

3. Player Emergency Pause
* Each team may request 1 pause per map.
* Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute
Bug Regulations

**English draft**

English translation 3. Player Emergency Pause * Each team may request one pause per map. * Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute Bug Regulations

## 303. competition_rules_valorant_psu_phuket_2026_s23_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s23_c01:title`
- Category: `competition_rules`
- Title: VALORANT: 3. Player Emergency Pause
- Source hash: `3907cd2114dc8d34ba830e74e5fcf3da456145714b9906ed8df8417b6268c8df`

**Thai source**

VALORANT: 3. Player Emergency Pause

**English draft**

VALORANT: 3. Player Emergency Pause

## 304. competition_rules_valorant_psu_phuket_2026_s24_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `291ae73667db1d0446f2115512efa559007511aa79da742c07c8aadbf387ef96`

**Thai source**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

**English draft**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

## 305. competition_rules_valorant_psu_phuket_2026_s24_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c01:text`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `088756069f6a4a1df7f709a90cc46579fb2fe3bff072516ad0670e997012efac`

**Thai source**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
* Play-Through Bug
Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested.
* Major Bug
Bugs that significantly affect gameplay or core mechanics and cannot be immediately resolved. Teams may request a challenge for review.
* Game-Breaking Bug
Bugs that completely compromise the fairness of a round, making it impossible to determine a legitimate outcome.
* Round Rollback
* If a bug occurs before any damage is dealt, officials may roll back the round.
* If damage has already been dealt, a rollback will not occur unless approved through the challenge process.
* In the case of a Game-Breaking Bug, officials will immediately roll back to the start of the round.
Exploit Adjudication
Intentionally using bugs or unintended mechanics to gain an unfair advantage is considered an offense.
* Agent Ability Usage
* Cypher cameras may not be placed in locations where they are invisible or indestructible due to clipping through map textures.
* Abilities may not be used outside map boundaries to gain information or an advantage.
* Special exception
* KAY/O’s ZERO/POINT ability may be used outside the map or in indestructible areas; however, the knife must not pass through textures that should be solid.
* Player Boosting

**English draft**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows * Play-Through Bug Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested. * Major Bug Bugs that significantly affect gameplay or core mechanics and cannot be immediately resolved. Teams may request a challenge for review. * Game-Breaking Bug Bugs that completely compromise the fairness of a round, making it impossible to determine a legitimate outcome. * Round Rollback * If a bug occurs before any damage is dealt, officials may roll back the round. * If damage has already been dealt, a rollback will not occur unless approved through the challenge process. * In the case of a Game-Breaking Bug, officials will immediately roll back to the start of the round. Exploit Adjudication Intentionally using bugs or unintended mechanics to gain an unfair advantage is considered an offense. * Agent Ability Usage * Cypher cameras may not be placed in locations where they are invisible or indestructible due to clipping through map textures. * Abilities may not be used outside map boundaries to gain information or an advantage. * Special exception * KAY/O’s ZERO/POINT ability may be used outside the map or in indestructible areas; however, the knife must not pass through textures that should be solid. * Player Boosting

## 306. competition_rules_valorant_psu_phuket_2026_s24_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c01:title`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `1f38f9b5491e1deeefda4eac4282bb9c19db0592ff116df586af9347f3a70d7f`

**Thai source**

VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

**English draft**

VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

## 307. competition_rules_valorant_psu_phuket_2026_s24_c02 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c02:section_title`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `291ae73667db1d0446f2115512efa559007511aa79da742c07c8aadbf387ef96`

**Thai source**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

**English draft**

A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

## 308. competition_rules_valorant_psu_phuket_2026_s24_c02 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c02:text`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `d6699ca5bf3ee2d136e48342a8820b06397ce31703eabe9c8faff966e31085c5`

**Thai source**

* Using teammates to boost to locations higher than normal jump height is prohibited.
Penalties
Officials will assess penalties based on intent and impact.

**English draft**

Using teammates to boost to locations higher than normal jump height is prohibited. Penalties Officials will assess penalties based on intent and impact.

## 309. competition_rules_valorant_psu_phuket_2026_s24_c02 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s24_c02:title`
- Category: `competition_rules`
- Title: VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows
- Source hash: `1f38f9b5491e1deeefda4eac4282bb9c19db0592ff116df586af9347f3a70d7f`

**Thai source**

VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

**English draft**

VALORANT: A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows

## 310. competition_rules_valorant_psu_phuket_2026_s25_c01 / section_title

- Selector: `competition_rules_valorant_psu_phuket_2026_s25_c01:section_title`
- Category: `competition_rules`
- Title: VALORANT: In-Game Penalty Types
- Source hash: `a16c32b279207261f5d0a0d1d58e8baf79f66d7a57475f3190e819398fca420a`

**Thai source**

In-Game Penalty Types

**English draft**

In-Game Penalty Types

## 311. competition_rules_valorant_psu_phuket_2026_s25_c01 / text

- Selector: `competition_rules_valorant_psu_phuket_2026_s25_c01:text`
- Category: `competition_rules`
- Title: VALORANT: In-Game Penalty Types
- Source hash: `75a57c7ee025abca43ae6157bb6ce82d7195ae78ce8222011b128b904e9aeaf5`

**Thai source**

In-Game Penalty Types
* Warning - For first offenses with low impact.
* Round Rollback - When an exploit clearly affects a round but intent cannot be determined.
* Round Loss - When a player or team is found to have intentionally used an exploit for advantage.
* Map Forfeit - For severe offenses or repeated violations that affect the map result.
* Match Forfeit - In cases of cheating or match fixing.
Final Clause
The tournament organizer reserves the right to modify or amend these rules at any time without prior notice.

**English draft**

In-Game Penalty Types * Warning - For first offenses with low impact. * Round Rollback - When an exploit clearly affects a round but intent cannot be determined. * Round Loss - When a player or team is found to have intentionally used an exploit for advantage. * Map Forfeit - For severe offenses or repeated violations that affect the map result. * Match Forfeit - In cases of cheating or match fixing. Final Clause The tournament organizer reserves the right to modify or amend these rules at any time without prior notice.

## 312. competition_rules_valorant_psu_phuket_2026_s25_c01 / title

- Selector: `competition_rules_valorant_psu_phuket_2026_s25_c01:title`
- Category: `competition_rules`
- Title: VALORANT: In-Game Penalty Types
- Source hash: `9e6968d0b1dedd52d980c226a3076c2fe601bd55c682be4d06a7e2cb96153703`

**Thai source**

VALORANT: In-Game Penalty Types

**English draft**

VALORANT: In-Game Penalty Types

## 313. curated_booking_no_edit / text

- Selector: `curated_booking_no_edit:text`
- Category: `reservation`
- Title: แก้ไขข้อมูลหลังจอง
- Source hash: `84b329b55d590399d829ec60765e2c68be0a68be25c17d9d5a0c734524766b45`

**Thai source**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

**English draft**

Once booking has been confirmed, no changes can be made. If modifications are needed, the booking must be canceled via email at least one hour before usage, and then re-booked with the original transfer slip attached.

## 314. curated_booking_no_edit / title

- Selector: `curated_booking_no_edit:title`
- Category: `reservation`
- Title: แก้ไขข้อมูลหลังจอง
- Source hash: `2ba0a74b846cb38e246a907c2c6f11da6684f836c929427c576c9c3eb13bfd14`

**Thai source**

แก้ไขข้อมูลหลังจอง

**English draft**

Edit information after booking

## 315. curated_booking_non_transferable / text

- Selector: `curated_booking_non_transferable:text`
- Category: `reservation`
- Title: โอนสิทธิ์การจอง
- Source hash: `bdaf74cccd2b48afdda31a94a8185a6a14de02e8ef6a66fdf0840ad4ce0a381d`

**Thai source**

ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

**English draft**

Cannot transfer reservation rights to others

## 316. curated_booking_non_transferable / title

- Selector: `curated_booking_non_transferable:title`
- Category: `reservation`
- Title: โอนสิทธิ์การจอง
- Source hash: `485fe2525e9de0d947c632a829fb6c67aab5a302702d9ac3812b88e1cf887115`

**Thai source**

โอนสิทธิ์การจอง

**English draft**

Transfer reservation rights

## 317. curated_booking_steps / text

- Selector: `curated_booking_steps:text`
- Category: `reservation`
- Title: ขั้นตอนการจอง
- Source hash: `f157a7bea0f1f1332556122f5308f01ed5d413c8352a3b0490e0ad16ffb629e9`

**Thai source**

ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน

**English draft**

The reservation steps are: select the desired service, choose the date and time, enter user information, verify the details, pay by transferring funds to a bank account, and attach the transfer slip.

## 318. curated_booking_steps / title

- Selector: `curated_booking_steps:title`
- Category: `reservation`
- Title: ขั้นตอนการจอง
- Source hash: `0419f5421b62dbc7d60806d81a4adef6ee2c1c6df5eae0876229d8736925cbfe`

**Thai source**

ขั้นตอนการจอง

**English draft**

Steps to Reserve

## 319. curated_cancel_1_hour / text

- Selector: `curated_cancel_1_hour:text`
- Category: `reservation`
- Title: ยกเลิกการจอง
- Source hash: `6cd7295be273597ea908ad951176b8c8eadf8ed946f211f2e9452dd9599545d5`

**Thai source**

การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง

**English draft**

Cancellation must be made at least 1 hour in advance.

## 320. curated_cancel_1_hour / title

- Selector: `curated_cancel_1_hour:title`
- Category: `reservation`
- Title: ยกเลิกการจอง
- Source hash: `3b717bf0f563d46017ca65f1cec1b76f4263cd445f00b4ba49aefcce30792410`

**Thai source**

ยกเลิกการจอง

**English draft**

Cancel reservation

## 321. curated_checkin_30_minutes / text

- Selector: `curated_checkin_30_minutes:text`
- Category: `reservation`
- Title: เช็คอินล่วงหน้า
- Source hash: `20eae4a3896fd3a78aa672ed3a1a603cab8f5e5d186368a85d70e4356e602a3b`

**Thai source**

ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ

**English draft**

Users must check in before the start time of their scheduled round. Check-in can be done up to 30 minutes prior to the scheduled round start time, and users must check in before the round begins.

## 322. curated_checkin_30_minutes / title

- Selector: `curated_checkin_30_minutes:title`
- Category: `reservation`
- Title: เช็คอินล่วงหน้า
- Source hash: `d77ad30b3441a7e9e4b969af54154a63bf15c1a5b311f30df031bd8ae912c9cc`

**Thai source**

เช็คอินล่วงหน้า

**English draft**

Pre-check-in

## 323. curated_checkin_id_required / text

- Selector: `curated_checkin_id_required:text`
- Category: `reservation`
- Title: เอกสารตอนเช็คอิน
- Source hash: `9e5a38dd8cfd66cbd52f0c7256c538cb641aa2154c1939cdb12c71b7f68562d9`

**Thai source**

เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

**English draft**

Upon check-in to use the service, you must present your student ID card, staff ID card, or national identification card.

## 324. curated_checkin_id_required / title

- Selector: `curated_checkin_id_required:title`
- Category: `reservation`
- Title: เอกสารตอนเช็คอิน
- Source hash: `7d240261f6248b133a5f6453177a9e76beed76f0cac26bd62c1a7a9735ffa9eb`

**Thai source**

เอกสารตอนเช็คอิน

**English draft**

Check-in Document

## 325. curated_checkin_late_cancel / text

- Selector: `curated_checkin_late_cancel:text`
- Category: `reservation`
- Title: ไม่เช็คอินก่อนเวลา
- Source hash: `369a1fbf1e087893166d0639e81b512347f92385e481d63cfdeaac93c9daca14`

**Thai source**

หากไม่เช็คอินก่อนถึงเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงินใด ๆ ทั้งสิ้น

**English draft**

If you do not check in before the round's start time, your reservation will be immediately canceled with no refund.

## 326. curated_checkin_late_cancel / title

- Selector: `curated_checkin_late_cancel:title`
- Category: `reservation`
- Title: ไม่เช็คอินก่อนเวลา
- Source hash: `8934a78f6a45e05fea7e077758fa5285824703e511c14c55f7e8d4d76a1fdc19`

**Thai source**

ไม่เช็คอินก่อนเวลา

**English draft**

Not check-in before time

## 327. curated_contact_email / text

- Selector: `curated_contact_email:text`
- Category: `contact`
- Title: อีเมลติดต่อ
- Source hash: `ffb620405c437d6293a9574188542338ecfa8109fcf3e61bf0d59bb978f7f8e6`

**Thai source**

อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com

**English draft**

Email to contact the center is psuesportspkt@gmail.com

## 328. curated_contact_email / title

- Selector: `curated_contact_email:title`
- Category: `contact`
- Title: อีเมลติดต่อ
- Source hash: `1b3a0cb08588240e1c384a67803956ff8bac5ad96a723472e26e8f1ce3453e9f`

**Thai source**

อีเมลติดต่อ

**English draft**

Email Contact

## 329. curated_contact_facebook / text

- Selector: `curated_contact_facebook:text`
- Category: `contact`
- Title: Facebook ติดต่อ
- Source hash: `1688f391c7ed0c544ffa2a8b615ed4c3e6fe413b7a1faf0bbb52692f0856c370`

**Thai source**

Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket

**English draft**

The center's Facebook page is https://www.facebook.com/psuesportsphuket

## 330. curated_contact_facebook / title

- Selector: `curated_contact_facebook:title`
- Category: `contact`
- Title: Facebook ติดต่อ
- Source hash: `5ebf1bb352e4be732411ec84cb5641f6f3e80fe042f98d508195e016aad2e3f0`

**Thai source**

Facebook ติดต่อ

**English draft**

Contact Facebook

## 331. curated_contact_location / text

- Selector: `curated_contact_location:text`
- Category: `contact`
- Title: ที่ตั้งศูนย์
- Source hash: `e06574c3ba93c8daf846ef96d91c7d0ac9aab2fafbc8be42ff4d226f2b23244d`

**Thai source**

PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120

**English draft**

PSU Esports Studio - Phuket is located at the Prince of Songkla University, Phuket Campus, 80 Moo 1, Wichit Songkhram Road, Kata Noi Subdistrict, Phuket Province, 83120

## 332. curated_contact_location / title

- Selector: `curated_contact_location:title`
- Category: `contact`
- Title: ที่ตั้งศูนย์
- Source hash: `c463c9e3edd0df46cabbf4c54cdf8d3e5d0edcef0196c7c83abb7200339a2df9`

**Thai source**

ที่ตั้งศูนย์

**English draft**

Location of the Center

## 333. curated_contact_phone / text

- Selector: `curated_contact_phone:text`
- Category: `contact`
- Title: เบอร์ติดต่อจากระบบจอง
- Source hash: `8b68aeb59767128c7cd60fe84786222b2cdb42b6646fef7459527b08e1194ba2`

**Thai source**

เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045

**English draft**

The contact number listed in the booking system is +66 7627 6004 and +66 7627 6045

## 334. curated_contact_phone / title

- Selector: `curated_contact_phone:title`
- Category: `contact`
- Title: เบอร์ติดต่อจากระบบจอง
- Source hash: `fd4762bc2aee856a578f7ea1e1ca1300f8784ac79e9e416f87c638ba523f85cb`

**Thai source**

เบอร์ติดต่อจากระบบจอง

**English draft**

Contact number from booking system

## 335. curated_damage_minor / text

- Selector: `curated_damage_minor:text`
- Category: `penalty`
- Title: ค่าปรับความเสียหายเล็กน้อย
- Source hash: `bd0992c78b992acf8f00f07ff66fa4ce47561d2f733454fde0b830c31dce6c31`

**Thai source**

ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100 – 500 บาท

**English draft**

Minor damages such as stains, water marks, scratches, loose lids, or loose buttons incur a fine of 100–500 THB

## 336. curated_damage_minor / title

- Selector: `curated_damage_minor:title`
- Category: `penalty`
- Title: ค่าปรับความเสียหายเล็กน้อย
- Source hash: `75d11b5d95821057fde24b73bdfc709b113209ab4b8e51d582c16196043a9d5d`

**Thai source**

ค่าปรับความเสียหายเล็กน้อย

**English draft**

Minor damage fine

## 337. curated_damage_moderate / text

- Selector: `curated_damage_moderate:text`
- Category: `penalty`
- Title: ค่าปรับความเสียหายปานกลาง
- Source hash: `7bdefdf965fe3dbd62a3cfbae38a9c3afbb4674c52629ff723b6a4b60beb98d4`

**Thai source**

ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500 – 2,000 บาท

**English draft**

Moderate damage such as broken seats, deep scratches, damaged furniture frames, controllers with stuck buttons, or broken headphone cords must be repaired at actual cost, or between THB 500–2,000

## 338. curated_damage_moderate / title

- Selector: `curated_damage_moderate:title`
- Category: `penalty`
- Title: ค่าปรับความเสียหายปานกลาง
- Source hash: `106954844de358f359cdb0cd97b2c70fa564659060c10769c490967e3d0c66c9`

**Thai source**

ค่าปรับความเสียหายปานกลาง

**English draft**

Medium damage fine

## 339. curated_damage_severe / text

- Selector: `curated_damage_severe:text`
- Category: `penalty`
- Title: ความเสียหายร้ายแรง
- Source hash: `7f12bf75df1a7a6b1f42ca8e0b9ba654036f8940a2d8d99fe63016905aee1cbb`

**Thai source**

ความเสียหายร้ายแรง เช่น เฟอร์นิเจอร์เสียหายจนใช้ไม่ได้ จอแตก คอมพิวเตอร์พัง หรืออุปกรณ์ใช้งานไม่ได้ ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง

**English draft**

Severe damages, such as furniture rendered unusable, broken monitors, damaged computers, or equipment that cannot be used, must be compensated in full for the value of the assets at prevailing market rates.

## 340. curated_damage_severe / title

- Selector: `curated_damage_severe:title`
- Category: `penalty`
- Title: ความเสียหายร้ายแรง
- Source hash: `e5ef9fbd1053d65f1a4dd562aae9ed43319e125543977c3bc874b4a838a9cd55`

**Thai source**

ความเสียหายร้ายแรง

**English draft**

Severe Damage

## 341. curated_games_pc / text

- Selector: `curated_games_pc:text`
- Category: `games`
- Title: เกมบน PC
- Source hash: `a9770a0093bb193752ede741b9592e3ce1e9135e2e53a2abefdb816df1d6b536`

**Thai source**

เกมที่ปรากฏในรายการ PC ได้แก่ Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT และ Call of Duty: Warzone

**English draft**

The listed PC games include Tekken 8, Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT and Call of Duty: Warzone

## 342. curated_games_pc / title

- Selector: `curated_games_pc:title`
- Category: `games`
- Title: เกมบน PC
- Source hash: `3edc4d35baaf04c473e39d16ed5f0b920fc04bb3036da451dd8ee6272043b969`

**Thai source**

เกมบน PC

**English draft**

PC Games

## 343. curated_games_popular / text

- Selector: `curated_games_popular:text`
- Category: `games`
- Title: เกมยอดนิยมบนหน้า Home
- Source hash: `44ae2e5c2e502797918c8c3baad0867db1178855414db0de2d84973749560b80`

**Thai source**

เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber

**English draft**

Popular games featured on the Home page include Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 and Beat Saber

## 344. curated_games_popular / title

- Selector: `curated_games_popular:title`
- Category: `games`
- Title: เกมยอดนิยมบนหน้า Home
- Source hash: `820c55ca08ff7da1a2461545d6b202ed73928113d4eee85f5b296722819af2a1`

**Thai source**

เกมยอดนิยมบนหน้า Home

**English draft**

Popular Games on the Home Page

## 345. curated_games_ps5 / text

- Selector: `curated_games_ps5:text`
- Category: `games`
- Title: เกมบน PlayStation 5
- Source hash: `7a35254319f681e59c4f02a5d54c73e8951caa598a7158153839af9901fcfe08`

**Thai source**

เกมที่ปรากฏในรายการ PlayStation 5 ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered และ Uncharted: Legacy of Thieves Collection

**English draft**

Games available on PlayStation 5 include Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered and Uncharted: Legacy of Thieves Collection

## 346. curated_games_ps5 / title

- Selector: `curated_games_ps5:title`
- Category: `games`
- Title: เกมบน PlayStation 5
- Source hash: `dfc4183505585522aee542568e36a804394e0943012e0be67af91c016fa6192e`

**Thai source**

เกมบน PlayStation 5

**English draft**

Games on PlayStation 5

## 347. curated_games_switch / text

- Selector: `curated_games_switch:text`
- Category: `games`
- Title: เกมบน Nintendo Switch
- Source hash: `e25fd964dec6f27ef4bff4fdb56890d919da69747257d50d8106fb8526ef2d2b`

**Thai source**

เกมที่ปรากฏในรายการ Nintendo Switch ได้แก่ Pokémon Champions, Animal Crossing: New Horizon, It Takes Two, Little Nightmares II, Luigi’s Mansion 3, Mario Kart 8 Deluxe, Mario Party Superstars, Monster Hunter Rise, Moving Out 2, New Super Mario Bros. U Deluxe, Nintendo Switch Sports, Overcooked, Overcooked 2, Ring Fit Adventure, Super Mario Odyssey, Super Smash Bros Ultimate และ The Legend of Zelda: Breath of The Wild

**English draft**

Games featured in the Nintendo Switch lineup include Pokémon Champions, Animal Crossing: New Horizons, It Takes Two, Little Nightmares II, Luigi’s Mansion 3, Mario Kart 8 Deluxe, Mario Party Superstars, Monster Hunter Rise, Moving Out 2, New Super Mario Bros. U Deluxe, Nintendo Switch Sports, Overcooked, Overcooked 2, Ring Fit Adventure, Super Mario Odyssey, Super Smash Bros Ultimate and The Legend of Zelda: Breath of the Wild

## 348. curated_games_switch / title

- Selector: `curated_games_switch:title`
- Category: `games`
- Title: เกมบน Nintendo Switch
- Source hash: `e6d25da087ce1cfa365f40c06f01d3590cf63f3127483ce53b4be786f0c371b5`

**Thai source**

เกมบน Nintendo Switch

**English draft**

Games on Nintendo Switch

## 349. curated_games_vr / text

- Selector: `curated_games_vr:text`
- Category: `games`
- Title: เกมบน VR Station
- Source hash: `2d8005978b7dae73ba19321f4c31734834a8910b6f0f2c7b4519a1faa41c662c`

**Thai source**

เกมที่ปรากฏในรายการ VR Station ได้แก่ Beat Saber และ Horizon Call of the Mountain

**English draft**

The games featured in the VR Station list are Beat Saber and Horizon: Zero Dawn

## 350. curated_games_vr / title

- Selector: `curated_games_vr:title`
- Category: `games`
- Title: เกมบน VR Station
- Source hash: `dc021cb3c8639f16bb27244acf5bd9d63cae7cc6cbf8f28fdddb278b764cc0a3`

**Thai source**

เกมบน VR Station

**English draft**

VR Station Game

## 351. curated_overview_identity / text

- Selector: `curated_overview_identity:text`
- Category: `overview`
- Title: PSU Esports Studio - Phuket คืออะไร
- Source hash: `f1ad50dd71d417f235259938559383bd640ca245f276a8fde97b1662cf309778`

**Thai source**

PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์

**English draft**

PSU Esports Studio - Phuket is a center for esports education and excellence development to drive economic growth in the southern region, with Phuket as its branch. It is the university of songklanrantin school's gaming and esports learning center.

## 352. curated_overview_identity / title

- Selector: `curated_overview_identity:title`
- Category: `overview`
- Title: PSU Esports Studio - Phuket คืออะไร
- Source hash: `7d9a770eba4757ef59dc2aed02f17896d0af9eb1ea9c06a2a18140661f36256b`

**Thai source**

PSU Esports Studio - Phuket คืออะไร

**English draft**

What is PSU Esports Studio - Phuket

## 353. curated_overview_mission / text

- Selector: `curated_overview_mission:text`
- Category: `overview`
- Title: Mission ของ PSU Esports Studio - Phuket
- Source hash: `cc90fd36b9cd8e408786ffcf5eaea1e0c09a7f32bfe6e911736d6fffc618932e`

**Thai source**

Mission ของ PSU Esports Studio - Phuket คือการยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต ผ่านสิ่งอำนวยความสะดวกและอุปกรณ์ที่ช่วยเสริมสร้างการเรียนรู้ให้กับนักเล่นเกม นักศึกษา และผู้สนใจ โดยก่อตั้งโดยมหาวิทยาลัยสงขลานครินทร์และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์

**English draft**

The mission of PSU Esports Studio - Phuket is to elevate education and excellence in esports by providing facilities and equipment that enhance learning for gamers, students, and enthusiasts. Established by Chulalongkorn University and operated by the Faculty of Computer Science.

## 354. curated_overview_mission / title

- Selector: `curated_overview_mission:title`
- Category: `overview`
- Title: Mission ของ PSU Esports Studio - Phuket
- Source hash: `732d1fb83b08de623a2a04c24b3f18da3599ddce643ac65e1003089b422ba645`

**Thai source**

Mission ของ PSU Esports Studio - Phuket

**English draft**

PSU Esports Studio - Phuket Mission

## 355. curated_payment_10_minutes / text

- Selector: `curated_payment_10_minutes:text`
- Category: `reservation`
- Title: ชำระเงินหลังจอง
- Source hash: `521f89691c35d63e494bd122cc53e4df66f5d9764050bc007793f98f884a83a0`

**Thai source**

ผู้ใช้งานต้องชำระค่าบริการหลังจากจองเสร็จเรียบร้อยทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก

**English draft**

Users must pay the service fee immediately after booking is completed. If payment is not made within 10 minutes, the booking will be canceled.

## 356. curated_payment_10_minutes / title

- Selector: `curated_payment_10_minutes:title`
- Category: `reservation`
- Title: ชำระเงินหลังจอง
- Source hash: `324e491bf75544971369ad577f49fc526e9c251f76023bc2feb8b2780dea420e`

**Thai source**

ชำระเงินหลังจอง

**English draft**

Pay after booking

## 357. curated_payment_bank / text

- Selector: `curated_payment_bank:text`
- Category: `reservation`
- Title: บัญชีธนาคารสำหรับชำระเงิน
- Source hash: `c64bfc779202a364c2b3157d778d88c2c7118b9b743a71462519dabcd2fe3106`

**Thai source**

ชำระเงินโดยโอนเข้าบัญชี Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน

**English draft**

Pay by bank transfer to Siam Commercial Bank (Thai Commercial Bank) account named PSU Esports Studio - Phuket, account number 795-276244-1, and attach a copy of the bank transfer slip.

## 358. curated_payment_bank / title

- Selector: `curated_payment_bank:title`
- Category: `reservation`
- Title: บัญชีธนาคารสำหรับชำระเงิน
- Source hash: `29808003713ca60bc51180342273914050967ab27f74cd5cac44009e2a78d492`

**Thai source**

บัญชีธนาคารสำหรับชำระเงิน

**English draft**

Bank account for payment

## 359. curated_penalty_appeal / text

- Selector: `curated_penalty_appeal:text`
- Category: `penalty`
- Title: ยื่นคำร้องขอพิจารณาใหม่
- Source hash: `260ba18930371abb67aeeb06180437c12a214421f3be212de545549fc2d0ac01`

**Thai source**

หากผู้ใช้งานไม่พอใจการตัดสินใจเกี่ยวกับการลงโทษ สามารถยื่นคำร้องขอการพิจารณาใหม่ได้ภายใน 7 วันหลังจากการถูกลงโทษ

**English draft**

If a user is dissatisfied with the penalty decision, they may submit a request for reconsideration within 7 days after being penalized.

## 360. curated_penalty_appeal / title

- Selector: `curated_penalty_appeal:title`
- Category: `penalty`
- Title: ยื่นคำร้องขอพิจารณาใหม่
- Source hash: `4c11f74d9cc269780c7b5e59fc035c5394a675177fec8ad34595fb62417aeb39`

**Thai source**

ยื่นคำร้องขอพิจารณาใหม่

**English draft**

Submit request for reconsideration

## 361. curated_penalty_temp_suspension / text

- Selector: `curated_penalty_temp_suspension:text`
- Category: `penalty`
- Title: ระงับสิทธิ์ชั่วคราว
- Source hash: `193c9c999bb1f9a645114c81d43d6b588e2246ea4ca31ecddae00889923a979a`

**Thai source**

หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด

**English draft**

If a user repeatedly violates rules or engages in aggressive behavior, their account privileges may be suspended for a period of 1 to 7 days, depending on the nature of the violation.

## 362. curated_penalty_temp_suspension / title

- Selector: `curated_penalty_temp_suspension:title`
- Category: `penalty`
- Title: ระงับสิทธิ์ชั่วคราว
- Source hash: `4d10c38f411073ef7199ba4c447b5a9ec74c1e9f9c5ffcda21c918dd66c4ae12`

**Thai source**

ระงับสิทธิ์ชั่วคราว

**English draft**

Temporary Suspension

## 363. curated_penalty_warning_suspension / text

- Selector: `curated_penalty_warning_suspension:text`
- Category: `penalty`
- Title: การลงโทษเมื่อละเมิดกฎ
- Source hash: `93f711742b0e015385151846014cd500fcd9a415215bde66e3923c865ad7a132`

**Thai source**

หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง

**English draft**

If a violation is detected, users will receive a warning and may have their account privileges temporarily or permanently suspended, depending on the severity.

## 364. curated_penalty_warning_suspension / title

- Selector: `curated_penalty_warning_suspension:title`
- Category: `penalty`
- Title: การลงโทษเมื่อละเมิดกฎ
- Source hash: `a1176b09857239199f1f6c5310a397d034146e2743ad875c5149d910d01c3924`

**Thai source**

การลงโทษเมื่อละเมิดกฎ

**English draft**

Penalty for violating rules

## 365. curated_refund_policy / text

- Selector: `curated_refund_policy:text`
- Category: `reservation`
- Title: นโยบายคืนเงิน
- Source hash: `9a93ddb78a8c84b16ace4f9af638b64791ae9d9cde3655bad201192c6b77c58f`

**Thai source**

ไม่มีการคืนเงินในทุกกรณี ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ

**English draft**

No refunds in all cases, except when the center is at fault, such as malfunctioning equipment or unforeseen circumstances causing the center to close temporarily.

## 366. curated_refund_policy / title

- Selector: `curated_refund_policy:title`
- Category: `reservation`
- Title: นโยบายคืนเงิน
- Source hash: `3bbe00822945175d2f38bb77320e22fd746bda8993d4381cd923c998b538fd9e`

**Thai source**

นโยบายคืนเงิน

**English draft**

Refund Policy

## 367. curated_reservation_advance_time / text

- Selector: `curated_reservation_advance_time:text`
- Category: `reservation`
- Title: ต้องจองล่วงหน้า
- Source hash: `2414c09f03942f68ce59e3057fa943bf3f2c47ed83f23fd53a64f7c4bd170f07`

**Thai source**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

**English draft**

Users must book online at least 1 hour before the scheduled usage time.

## 368. curated_reservation_advance_time / title

- Selector: `curated_reservation_advance_time:title`
- Category: `reservation`
- Title: ต้องจองล่วงหน้า
- Source hash: `20f8968f23d26711d96987100079ee2e9a9bc35913e75be02b0019b6844f4704`

**Thai source**

ต้องจองล่วงหน้า

**English draft**

Must book in advance

## 369. curated_reservation_max_sessions / text

- Selector: `curated_reservation_max_sessions:text`
- Category: `reservation`
- Title: จำนวน session สูงสุดต่อการจอง
- Source hash: `3d66e017b8ada09c8fdee807910cc474aa671b7cd50db0e711cda5f2bc7d628a`

**Thai source**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

**English draft**

One booking can reserve up to 3 Sessions

## 370. curated_reservation_max_sessions / title

- Selector: `curated_reservation_max_sessions:title`
- Category: `reservation`
- Title: จำนวน session สูงสุดต่อการจอง
- Source hash: `99b54a0ae2595194f5c8d79c85f8cf9e8e2e0c532a49457bda343a43af97a4eb`

**Thai source**

จำนวน session สูงสุดต่อการจอง

**English draft**

Maximum number of sessions per reservation

## 371. curated_rule_belongings / text

- Selector: `curated_rule_belongings:text`
- Category: `rules`
- Title: ฝากสัมภาระ
- Source hash: `4c1d6b26a29fa3c5204bc86adf8a2ac3b401782820967cda1ec0db0498b3376d`

**Thai source**

กรุณาฝากสัมภาระก่อนเข้าใช้บริการ

**English draft**

Please check in luggage before using the service

## 372. curated_rule_belongings / title

- Selector: `curated_rule_belongings:title`
- Category: `rules`
- Title: ฝากสัมภาระ
- Source hash: `29c73e1ee2a483109ff4b6683ead516c5d005a8900c0f3faefcff072de8d247f`

**Thai source**

ฝากสัมภาระ

**English draft**

Leave luggage

## 373. curated_rule_food_drinks / text

- Selector: `curated_rule_food_drinks:text`
- Category: `rules`
- Title: อาหารและเครื่องดื่ม
- Source hash: `0a298a220fb70bb88ce20e52881a3ffceb64e49c50e7e47210868cd95e49f753`

**Thai source**

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น

**English draft**

Food and drinks are permitted only in designated areas.

## 374. curated_rule_food_drinks / title

- Selector: `curated_rule_food_drinks:title`
- Category: `rules`
- Title: อาหารและเครื่องดื่ม
- Source hash: `6bdfcbbbf9b765c43f94436c765efff2431f92297886d00ed0a9465f464f49c1`

**Thai source**

อาหารและเครื่องดื่ม

**English draft**

Food and Drinks

## 375. curated_rule_lost_items / text

- Selector: `curated_rule_lost_items:text`
- Category: `rules`
- Title: ทรัพย์สินสูญหาย
- Source hash: `58ee52f11b7054b0be10c140be9a486cb3bfb0a9ae83a9903d338468d3912961`

**Thai source**

กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี

**English draft**

Please check your assets every time you use our service. If any are lost, the Center reserves the right to not be liable in any case.

## 376. curated_rule_lost_items / title

- Selector: `curated_rule_lost_items:title`
- Category: `rules`
- Title: ทรัพย์สินสูญหาย
- Source hash: `f643b4b108548d9a213ae7674dde2b45c7a9fe1dfaa15296ce5d042da8f8c602`

**Thai source**

ทรัพย์สินสูญหาย

**English draft**

Lost Property

## 377. curated_rule_move_equipment / text

- Selector: `curated_rule_move_equipment:text`
- Category: `rules`
- Title: ห้ามเคลื่อนย้ายอุปกรณ์
- Source hash: `c40c06ac49f8510e655fd6f997a05fdd4482b218f689ae5280851561c03e4ce8`

**Thai source**

ห้ามเคลื่อนย้ายอุปกรณ์หรือสิ่งของใด ๆ โดยไม่ได้รับอนุญาต

**English draft**

No equipment or items may be moved without permission.

## 378. curated_rule_move_equipment / title

- Selector: `curated_rule_move_equipment:title`
- Category: `rules`
- Title: ห้ามเคลื่อนย้ายอุปกรณ์
- Source hash: `3ad4b2d77190fe78e312f2b03f3888808f3f97ea599bfd541a69eff4c8363ad4`

**Thai source**

ห้ามเคลื่อนย้ายอุปกรณ์

**English draft**

Prohibited to move equipment

## 379. curated_rule_noise_language / text

- Selector: `curated_rule_noise_language:text`
- Category: `rules`
- Title: เสียงดังและคำพูดไม่เหมาะสม
- Source hash: `01412ae999df1b7c98ad9948dbbdb31c06efa16ce691b144d377f756ac797c66`

**Thai source**

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น

**English draft**

Please refrain from making excessive noise and avoid any disrespectful or insulting remarks toward others.

## 380. curated_rule_noise_language / title

- Selector: `curated_rule_noise_language:title`
- Category: `rules`
- Title: เสียงดังและคำพูดไม่เหมาะสม
- Source hash: `4f0afdc10ab5fce666e373e8bcddfdf3b8676ef242fe4b9c364845c999ef7307`

**Thai source**

เสียงดังและคำพูดไม่เหมาะสม

**English draft**

Loud noises and inappropriate speech

## 381. curated_rule_power_outlet / text

- Selector: `curated_rule_power_outlet:text`
- Category: `rules`
- Title: ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
- Source hash: `a5748c6825d1970eed2134cb9fd04c6006a3ec9850b7e60970175e9eeb60be01`

**Thai source**

ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัวมาใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต

**English draft**

Prohibited to use personal electronic devices plugged into power sources without permission

## 382. curated_rule_power_outlet / title

- Selector: `curated_rule_power_outlet:title`
- Category: `rules`
- Title: ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
- Source hash: `3fa6d4ee86e850b49e9ccbd33eabb2f2c9b4b3bc9e38bb880dcad97ba60cd5e9`

**Thai source**

ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต

**English draft**

No unauthorized use of power plugs

## 383. curated_rule_return_equipment / text

- Selector: `curated_rule_return_equipment:text`
- Category: `rules`
- Title: คืนอุปกรณ์และแผ่นเกม
- Source hash: `d40513caf4eacaa2528abd56fb98cdbc7682874390bce3993ccf26d885eec610`

**Thai source**

กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ

**English draft**

Please return all equipment and game discs you have borrowed after use is complete.

## 384. curated_rule_return_equipment / title

- Selector: `curated_rule_return_equipment:title`
- Category: `rules`
- Title: คืนอุปกรณ์และแผ่นเกม
- Source hash: `d6189c77a1b05f9867ad2d5bf2b5f8274354b555d7c619af76a42478242fba74`

**Thai source**

คืนอุปกรณ์และแผ่นเกม

**English draft**

Return Equipment and Game Discs

## 385. curated_rule_smoking_alcohol_drugs / text

- Selector: `curated_rule_smoking_alcohol_drugs:text`
- Category: `rules`
- Title: บุหรี่ สารเสพติด และแอลกอฮอล์
- Source hash: `fa2d40b827a223e7ccd127f7f1030d75c73441e767bb12ed8be4c606afcb43f1`

**Thai source**

ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

**English draft**

Prohibited to smoke cigarettes, consume narcotics or drink alcohol within the facility.

## 386. curated_rule_smoking_alcohol_drugs / title

- Selector: `curated_rule_smoking_alcohol_drugs:title`
- Category: `rules`
- Title: บุหรี่ สารเสพติด และแอลกอฮอล์
- Source hash: `8e50b20cf7555f029ac9c2d55d5e2fbc90cb6c85d892f56640acadb8acd136e4`

**Thai source**

บุหรี่ สารเสพติด และแอลกอฮอล์

**English draft**

Tobacco, Drugs and Alcohol

## 387. curated_rule_weapons_gambling / text

- Selector: `curated_rule_weapons_gambling:text`
- Category: `rules`
- Title: อาวุธ ทะเลาะวิวาท การพนัน
- Source hash: `b3cb9993c541f73b09a30535159cecdd47b7a5065d297c2eb7e263fa4732c463`

**Thai source**

ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน

**English draft**

No weapons or sharp objects are allowed. No fighting or arguments are permitted, and gambling is strictly prohibited.

## 388. curated_rule_weapons_gambling / title

- Selector: `curated_rule_weapons_gambling:title`
- Category: `rules`
- Title: อาวุธ ทะเลาะวิวาท การพนัน
- Source hash: `892fa7468bd469cf81ddc23b0973dce483870b2cceeddce55c57761a0c28290e`

**Thai source**

อาวุธ ทะเลาะวิวาท การพนัน

**English draft**

Weapons Dispute Gambling

## 389. curated_schedule_afternoon / text

- Selector: `curated_schedule_afternoon:text`
- Category: `reservation`
- Title: ช่วงเวลาบ่าย
- Source hash: `13ade375f27368f3b6ef919f8b1df034cd03564db724f6a0b783cd2494e2fd58`

**Thai source**

ตารางบริการช่วง Afternoon คือ 13:00 – 16:00

**English draft**

Afternoon service schedule: 13:00 – 16:00

## 390. curated_schedule_afternoon / title

- Selector: `curated_schedule_afternoon:title`
- Category: `reservation`
- Title: ช่วงเวลาบ่าย
- Source hash: `97c0b8e202954fdec472e8b87739cc3b62e0586e450fd89e0d8ee26b81c29180`

**Thai source**

ช่วงเวลาบ่าย

**English draft**

Afternoon time

## 391. curated_schedule_morning / text

- Selector: `curated_schedule_morning:text`
- Category: `reservation`
- Title: ช่วงเวลาเช้า
- Source hash: `99acf8b020dcc46569411dbcd230bdf0afd44599452a56bf652c0b00e890c7c4`

**Thai source**

ตารางบริการช่วง Morning คือ 09:00 – 12:00

**English draft**

Morning service schedule is 09:00 – 12:00

## 392. curated_schedule_morning / title

- Selector: `curated_schedule_morning:title`
- Category: `reservation`
- Title: ช่วงเวลาเช้า
- Source hash: `305db82db0f26ce0305f59531ef653967b545f0cbbae2909e89be6ed6c7ed999`

**Thai source**

ช่วงเวลาเช้า

**English draft**

Morning time

## 393. curated_time_change_policy / text

- Selector: `curated_time_change_policy:text`
- Category: `reservation`
- Title: เปลี่ยนเวลาใช้งาน
- Source hash: `c1ff3fc60f3a67283d4cb77b585ec9a78ced895c3cdb8ab2783c6dd80fa0e6a9`

**Thai source**

สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

**English draft**

Reservation time can be changed, but must be notified at least 1 hour before the originally booked time. Failure to notify or notifying late will result in no refund and no compensation for time.

## 394. curated_time_change_policy / title

- Selector: `curated_time_change_policy:title`
- Category: `reservation`
- Title: เปลี่ยนเวลาใช้งาน
- Source hash: `5ae47e607a377170814d1dd0bec008faa8b71c4acfd72fb754945092f11f4a2c`

**Thai source**

เปลี่ยนเวลาใช้งาน

**English draft**

Change usage time

## 395. curated_user_info_required / text

- Selector: `curated_user_info_required:text`
- Category: `reservation`
- Title: ข้อมูลที่ต้องกรอกตอนจอง
- Source hash: `f08ac869b59ce6c9ab510669371da42e2fa0bd3f631bc0cb72e896c90339be75`

**Thai source**

ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี

**English draft**

The information required to book includes Student ID/Staff ID/National ID, full name, email, phone number, and comments if any

## 396. curated_user_info_required / title

- Selector: `curated_user_info_required:title`
- Category: `reservation`
- Title: ข้อมูลที่ต้องกรอกตอนจอง
- Source hash: `beddae5f410b8f176c7cb110b79677efa2ba87c97498f4b4e90564327fe5d155`

**Thai source**

ข้อมูลที่ต้องกรอกตอนจอง

**English draft**

Information to be filled when booking

## 397. equipment_driving_force_shifter / how_to_use_th

- Selector: `equipment_driving_force_shifter:how_to_use_th`
- Category: `equipment`
- Title: Driving Force Shifter
- Source hash: `ad65df0a06ad76052996766bcfd356295afe71e7d205c2ec418ce7eb27dcfd44`

**Thai source**

ใช้งานร่วมกับ Logitech G923 และ Cockpit ในเกมขับรถ หากไม่คุ้นเคยควรให้เจ้าหน้าที่แนะนำก่อนเริ่มเล่น

**English draft**

Use with Logitech G923 and Cockpit in racing games. If unfamiliar, allow staff to guide before playing.

## 398. equipment_driving_force_shifter / use_cases_th

- Selector: `equipment_driving_force_shifter:use_cases_th`
- Category: `equipment`
- Title: Driving Force Shifter
- Source hash: `56eb03ce0175e0d9a4c7319a39742101fda3e01a599f04b4cc599874411e50d6`

**Thai source**

['เพิ่มความสมจริงให้เกมขับรถ เช่น Gran Turismo 7']

**English draft**

Enhances realism in driving games such as Gran Turismo 7

## 399. equipment_driving_force_shifter / what_th

- Selector: `equipment_driving_force_shifter:what_th`
- Category: `equipment`
- Title: Driving Force Shifter
- Source hash: `1b99566fe9b2e3521c7d518eb9bea3b6318808ca9e5de7a3853dbab64eaa61c4`

**Thai source**

คันเกียร์เสริมสำหรับชุดพวงมาลัยขับรถ

**English draft**

Steering wheel upgrade kit for car steering column

## 400. equipment_gaming_chair / how_to_use_th

- Selector: `equipment_gaming_chair:how_to_use_th`
- Category: `equipment`
- Title: Gaming Chair
- Source hash: `91491a1ec15af5e0717388d22fc216147a67bfc9d080ff623fd2937efcfc5b6f`

**Thai source**

ใช้นั่งระหว่างเล่นเกมหรือฝึกซ้อม และไม่ควรย้ายหรือใช้งานผิดประเภท

**English draft**

Sit while playing games or practicing and do not move or use incorrectly

## 401. equipment_gaming_chair / use_cases_th

- Selector: `equipment_gaming_chair:use_cases_th`
- Category: `equipment`
- Title: Gaming Chair
- Source hash: `e4e4d5e102e3055f993720efc53cb436b1ff83ae8ef4a288fbb5336431905063`

**Thai source**

['รองรับการนั่งเล่น PC Zone เป็นรอบเวลา']

**English draft**

Supports playing PC Zone sessions

## 402. equipment_gaming_chair / what_th

- Selector: `equipment_gaming_chair:what_th`
- Category: `equipment`
- Title: Gaming Chair
- Source hash: `ac544ad5048d39bfb17d765a9c3a4a2cf0fe7155d1151953bb2a125fdf6fbcd3`

**Thai source**

เก้าอี้เกมมิ่งสำหรับนั่งใช้งาน PC Zone

**English draft**

Gaming chair for use with PC Zone

## 403. equipment_gaming_headset / how_to_use_th

- Selector: `equipment_gaming_headset:how_to_use_th`
- Category: `equipment`
- Title: Gaming Headset
- Source hash: `2df26336d7df682dca81f76f61808ae790b042c338b9bf7bb1b6e135c4078076`

**Thai source**

ใช้งานคู่กับ PC ที่จองไว้ ปรับระดับเสียงอย่างเหมาะสม และแจ้งเจ้าหน้าที่ถ้าเสียงหรือไมค์มีปัญหา

**English draft**

Use with your reserved PC, adjust volume levels appropriately, and inform staff if there are issues with sound or microphone.

## 404. equipment_gaming_headset / use_cases_th

- Selector: `equipment_gaming_headset:use_cases_th`
- Category: `equipment`
- Title: Gaming Headset
- Source hash: `031f67b65f2a348db42bc91f12faec2d2513ce9aa3395cd9eedacbdb181ef5de`

**Thai source**

['ฟังเสียงเกม', 'สื่อสารในเกมหรือกิจกรรมอีสปอร์ต']

**English draft**

Listen to game audio Communicate during gameplay or esports activities

## 405. equipment_gaming_headset / what_th

- Selector: `equipment_gaming_headset:what_th`
- Category: `equipment`
- Title: Gaming Headset
- Source hash: `36eae5b56b2b1dbd4e07894f19083ef761bf55f4f15ca901a070dd10c70ac60b`

**Thai source**

หูฟังเกมมิ่งสำหรับฟังเสียงเกมและสื่อสารระหว่างเล่น

**English draft**

Gaming headset for listening to game audio and communicating during gameplay

## 406. equipment_gaming_keyboard / how_to_use_th

- Selector: `equipment_gaming_keyboard:how_to_use_th`
- Category: `equipment`
- Title: Gaming Keyboard
- Source hash: `3496bf67a0fb517456a103c7c48a0a4fe1f3d6f603bdfef9f226924a9a0e03b8`

**Thai source**

ใช้งานกับเครื่อง PC ที่จองไว้ หลีกเลี่ยงการแกะ ย้าย หรือปรับอุปกรณ์เอง หากมีปุ่มเสียควรแจ้งเจ้าหน้าที่

**English draft**

Use with reserved PCs. Avoid disassembling, moving, or modifying equipment. If any buttons are faulty, notify staff.

## 407. equipment_gaming_keyboard / use_cases_th

- Selector: `equipment_gaming_keyboard:use_cases_th`
- Category: `equipment`
- Title: Gaming Keyboard
- Source hash: `0ac75db84692ebb6ae395e180734f3568ec2e5e6f66a618548fea9e57f0d50aa`

**Thai source**

['ควบคุมเกม PC', 'พิมพ์ข้อมูล']

**English draft**

PC gaming control Data input

## 408. equipment_gaming_keyboard / what_th

- Selector: `equipment_gaming_keyboard:what_th`
- Category: `equipment`
- Title: Gaming Keyboard
- Source hash: `c5c091dc34168d81fea53a54bb2512a7a813b0bc1608db2c25816299baeba960`

**Thai source**

คีย์บอร์ดสำหรับควบคุมเกมและพิมพ์บน Gaming PC

**English draft**

Keyboard for controlling games and typing on a Gaming PC

## 409. equipment_gaming_monitor / how_to_use_th

- Selector: `equipment_gaming_monitor:how_to_use_th`
- Category: `equipment`
- Title: Gaming Monitor
- Source hash: `d8e8d7dd72c35fd3261450fc4cc4bbe8a18dc15269a5e8cffbb40cc9f0ebcb94`

**Thai source**

ใช้งานพร้อมเครื่อง PC ที่จองไว้ โดยปกติผู้ใช้ไม่ต้องตั้งค่าฮาร์ดแวร์เอง หากจอหรือภาพมีปัญหาควรแจ้งเจ้าหน้าที่

**English draft**

Use with reserved PCs. Normally, users do not need to configure hardware settings. If there are issues with the monitor or display, please notify staff.

## 410. equipment_gaming_monitor / use_cases_th

- Selector: `equipment_gaming_monitor:use_cases_th`
- Category: `equipment`
- Title: Gaming Monitor
- Source hash: `dfb9da7cad9577925ee67d9384b87ca18a86b29ed548c99338f4098a531e71b7`

**Thai source**

['แสดงผลเกมและโปรแกรมบน PC Zone']

**English draft**

Display games and programs on PC Zone

## 411. equipment_gaming_monitor / what_th

- Selector: `equipment_gaming_monitor:what_th`
- Category: `equipment`
- Title: Gaming Monitor
- Source hash: `6a2ca199a5a97e3c95d115ce6933ef176635114ceef1896f955b9d5ff7c8bc91`

**Thai source**

จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone

**English draft**

Monitor for use with Gaming PC at PC Zone

## 412. equipment_gaming_mouse / how_to_use_th

- Selector: `equipment_gaming_mouse:how_to_use_th`
- Category: `equipment`
- Title: Gaming Mouse
- Source hash: `ba7be77a18922942b5e2de557b14d2b28a9e3c343b0abd9a17aafd5fcffd0999`

**Thai source**

ใช้งานกับ PC ที่จองไว้ และควรแจ้งเจ้าหน้าที่หากคลิกไม่ติด เซนเซอร์รวน หรือพบความเสียหาย

**English draft**

Use with the reserved PC and notify staff if clicking is unresponsive, sensor is loose, or damage is observed

## 413. equipment_gaming_mouse / use_cases_th

- Selector: `equipment_gaming_mouse:use_cases_th`
- Category: `equipment`
- Title: Gaming Mouse
- Source hash: `1a6f382416ebe30ec77e882af4288cdede48a4b87d5e535764f31dea56966605`

**Thai source**

['ควบคุมเกม PC โดยเฉพาะเกม FPS/MOBA']

**English draft**

Control PC games, especially FPS/MOBA titles

## 414. equipment_gaming_mouse / what_th

- Selector: `equipment_gaming_mouse:what_th`
- Category: `equipment`
- Title: Gaming Mouse
- Source hash: `0275b92eec07c0d149cb3a7fadf8cebffaff0498e85c3d2499811a3e0f69f940`

**Thai source**

เมาส์สำหรับเล่นเกมบน Gaming PC

**English draft**

Mouse for gaming on a Gaming PC

## 415. equipment_gaming_pc / how_to_use_th

- Selector: `equipment_gaming_pc:how_to_use_th`
- Category: `equipment`
- Title: Gaming PC รุ่น MSI MAG Infinite S3 14th
- Source hash: `a7a903107218b5303b6103b94a216b86cffc41c076cbded3afec3ca8e03f8700`

**Thai source**

เลือก PC Zone ในระบบจอง แล้วเข้าใช้งานตามรอบเวลาที่จองไว้ จากนั้นเปิดเกม/โปรแกรมที่ศูนย์จัดเตรียมไว้ให้

**English draft**

Select PC Zone in the booking system and access it according to your scheduled time. Then open the game/software provided by the center.

## 416. equipment_gaming_pc / note_th

- Selector: `equipment_gaming_pc:note_th`
- Category: `equipment`
- Title: Gaming PC รุ่น MSI MAG Infinite S3 14th
- Source hash: `ed1a1a6a0aca01c7f1f95ec4838f1dc0c957305a37d61b1869f5c4b54ae1a7bb`

**Thai source**

สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB

**English draft**

Specifications recorded in the project: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB

## 417. equipment_gaming_pc / use_cases_th

- Selector: `equipment_gaming_pc:use_cases_th`
- Category: `equipment`
- Title: Gaming PC รุ่น MSI MAG Infinite S3 14th
- Source hash: `b6a6e5a28c2d8e1e365a94ccdd8e42eacfdf5336ba8df6b539ced543a3180804`

**Thai source**

['เล่น VALORANT', 'เล่น Counter-Strike 2', 'เล่น PUBG: BATTLEGROUNDS', 'เล่น Call of Duty: Warzone', 'เล่น TEKKEN 8', 'เล่น League of Legends']

**English draft**

Play VALORANT Play Counter-Strike 2 Play PUBG: BATTLEGROUNDS Play Call of Duty: Warzone Play TEKKEN 8 Play League of Legends

## 418. equipment_gaming_pc / what_th

- Selector: `equipment_gaming_pc:what_th`
- Category: `equipment`
- Title: Gaming PC รุ่น MSI MAG Infinite S3 14th
- Source hash: `7e0189a1d86185c771e1ce0b43388b4ad2f36590f031b88bdb384d3ee417ce0e`

**Thai source**

เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต

**English draft**

PC gaming computer from PC Zone for playing games on a computer and training for esports

## 419. equipment_logitech_g923 / how_to_use_th

- Selector: `equipment_logitech_g923:how_to_use_th`
- Category: `equipment`
- Title: Logitech G923 TRUEFORCE Racing Wheel
- Source hash: `f23a518fb5577571f6ecb117f8d6751fd33681bfa73c6521cd661ba4855664c4`

**Thai source**

จอง Cockpit Zone แล้วใช้พวงมาลัย เหยียบคันเร่งและเบรก และควบคุมรถตามเกมที่ศูนย์จัดไว้

**English draft**

Book Cockpit Zone and use the steering wheel, accelerator, and brake pedals to control your vehicle according to the setup provided at the center.

## 420. equipment_logitech_g923 / use_cases_th

- Selector: `equipment_logitech_g923:use_cases_th`
- Category: `equipment`
- Title: Logitech G923 TRUEFORCE Racing Wheel
- Source hash: `0f8aabe9e44f09de3c1e7375b746b762e769794d62408d342feff836546928bb`

**Thai source**

['เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว']

**English draft**

Play Gran Turismo 7 with cockpit kit and 65-inch TV

## 421. equipment_logitech_g923 / what_th

- Selector: `equipment_logitech_g923:what_th`
- Category: `equipment`
- Title: Logitech G923 TRUEFORCE Racing Wheel
- Source hash: `e8ccb6505431f26ffd764484f7aa8584163ffa9ff8f2d48c49b86d471a7825ea`

**Thai source**

ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone

**English draft**

Racing steering wheel set for playing driving games in Cockpit Zone

## 422. equipment_nintendo_switch_oled / how_to_use_th

- Selector: `equipment_nintendo_switch_oled:how_to_use_th`
- Category: `equipment`
- Title: Nintendo Switch OLED
- Source hash: `6341be9a3830cde797f54c077a772ca0f6dcc7476bfa0ea874b6a41180fb507c`

**Thai source**

จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ

**English draft**

Book Nintendo Switch Zone and play through an 86-inch TV and provided controllers at the center during scheduled service rounds

## 423. equipment_nintendo_switch_oled / use_cases_th

- Selector: `equipment_nintendo_switch_oled:use_cases_th`
- Category: `equipment`
- Title: Nintendo Switch OLED
- Source hash: `a77461d1d2792cf061d2a48169d868f822d596e532b2c16ad56b0701ca0822c9`

**Thai source**

['เล่น Mario Kart 8 Deluxe', 'เล่น Overcooked 2', 'เล่น Super Smash Bros Ultimate', 'เล่น Nintendo Switch Sports']

**English draft**

Play Mario Kart 8 Deluxe Play Overcooked 2 Play Super Smash Bros Ultimate Play Nintendo Switch Sports

## 424. equipment_nintendo_switch_oled / what_th

- Selector: `equipment_nintendo_switch_oled:what_th`
- Category: `equipment`
- Title: Nintendo Switch OLED
- Source hash: `10d4e9272ea98a887b318051c57af01219276754cc5299b24f69238844313416`

**Thai source**

เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว

**English draft**

Nintendo Switch OLED console for multiplayer or family gaming

## 425. equipment_playstation_5_slim / how_to_use_th

- Selector: `equipment_playstation_5_slim:how_to_use_th`
- Category: `equipment`
- Title: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive
- Source hash: `ba7066584f57130e6d2afb2640a5a286ba16c775b862d964c754324ed3ef8b9d`

**Thai source**

จอง PlayStation 5 Zone หรือ VR Zone ตามบริการที่ต้องการ แล้วเล่นเกมที่ศูนย์จัดเตรียมไว้ตามรอบเวลา

**English draft**

Book a PlayStation 5 Zone or VR Zone according to your service needs, then play games at the center scheduled for specific times

## 426. equipment_playstation_5_slim / use_cases_th

- Selector: `equipment_playstation_5_slim:use_cases_th`
- Category: `equipment`
- Title: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive
- Source hash: `09d3786eac0bb4319c5dabf6e11529dadb2557c75e01ad1ea234e300a9d7549b`

**Thai source**

["เล่น Marvel's Spider-Man 2", 'เล่น TEKKEN 8', 'เล่น Fortnite', 'เล่น God of War Ragnarok', 'รองรับ VR Zone ที่ใช้ PlayStation VR2']

**English draft**

Play Marvel's Spider-Man 2 Play TEKKEN 8 Play Fortnite Play God of War Ragnarok Supports VR Zone using PlayStation VR2

## 427. equipment_playstation_5_slim / what_th

- Selector: `equipment_playstation_5_slim:what_th`
- Category: `equipment`
- Title: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive
- Source hash: `424a234eaa50996325268baae9e039accb37a43d3bcc283c08c61841ce648210`

**Thai source**

เครื่องเกม PlayStation 5 สำหรับเล่นเกมคอนโซล และใช้เป็นฐานสำหรับ VR Zone บางชุด

**English draft**

PlayStation 5 console for console gaming and used as a base for some VR Zone setups

## 428. equipment_pulse_elite_headset / how_to_use_th

- Selector: `equipment_pulse_elite_headset:how_to_use_th`
- Category: `equipment`
- Title: Pulse Elite Wireless Headset
- Source hash: `45cbe050367b3ff6398cadcbded39497d30443c642046b5252961a69c4c68f84`

**Thai source**

ใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่

**English draft**

Use the equipment provided by staff. If audio connection fails, inform staff.

## 429. equipment_pulse_elite_headset / use_cases_th

- Selector: `equipment_pulse_elite_headset:use_cases_th`
- Category: `equipment`
- Title: Pulse Elite Wireless Headset
- Source hash: `f99beac14004e89c33b95294027595780c23fcc096aa0f8842f996b81ee0221c`

**Thai source**

['ฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น']

**English draft**

Listen to racing game sounds and enhance realism during gameplay

## 430. equipment_pulse_elite_headset / what_th

- Selector: `equipment_pulse_elite_headset:what_th`
- Category: `equipment`
- Title: Pulse Elite Wireless Headset
- Source hash: `8517cfe6759d7130067a89aea4ceedde6612b082154f6367b82ccfe88ce2035e`

**Thai source**

หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone

**English draft**

Wireless headset for use with gaming gear in Cockpit Zone

## 431. equipment_racezone_cockpit_v3 / how_to_use_th

- Selector: `equipment_racezone_cockpit_v3:how_to_use_th`
- Category: `equipment`
- Title: Racezone Full Cockpit V3
- Source hash: `cc80c2666625f20b873c41b72551d69829feee8fc52a0db5de62c90262b57623`

**Thai source**

นั่งใน Cockpit แล้วใช้พวงมาลัย คันเร่ง และเบรกตามที่ตั้งค่าไว้ในเกม

**English draft**

Sit in the cockpit and use the steering wheel, throttle, and brakes as set in the game

## 432. equipment_racezone_cockpit_v3 / use_cases_th

- Selector: `equipment_racezone_cockpit_v3:use_cases_th`
- Category: `equipment`
- Title: Racezone Full Cockpit V3
- Source hash: `f590ec2ed4b24d685d0e3d8fa93486793adf1590bfd9a581fbc983ee592d68f5`

**Thai source**

['เล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น']

**English draft**

Play Gran Turismo 7 with more realistic driving simulation

## 433. equipment_racezone_cockpit_v3 / what_th

- Selector: `equipment_racezone_cockpit_v3:what_th`
- Category: `equipment`
- Title: Racezone Full Cockpit V3
- Source hash: `46373b5719445a99e388b040830e4091259417d58c48f15ee050353af7b26735`

**Thai source**

ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ

**English draft**

Seat cushion and car chassis simulation set for racing games

## 434. equipment_sofa_2_seats / how_to_use_th

- Selector: `equipment_sofa_2_seats:how_to_use_th`
- Category: `equipment`
- Title: Sofa 2 seats
- Source hash: `c7894ec5a69e0dc1545709a568b5aaa589fbbbceafd18edccca5be0c0ea2a4e0`

**Thai source**

ใช้นั่งระหว่างเล่น Nintendo Switch และไม่ควรเคลื่อนย้ายหรือใช้งานผิดประเภท

**English draft**

Sit while playing Nintendo Switch and do not move or use incorrectly

## 435. equipment_sofa_2_seats / use_cases_th

- Selector: `equipment_sofa_2_seats:use_cases_th`
- Category: `equipment`
- Title: Sofa 2 seats
- Source hash: `4aeed0e9141ed169248ab98c00472a4bc29d0c5bb6ea1e134821326682362fff`

**Thai source**

['รองรับการเล่นเกมเป็นกลุ่มใน Nintendo Switch Zone']

**English draft**

Supports multiplayer gaming in Nintendo Switch Zone

## 436. equipment_sofa_2_seats / what_th

- Selector: `equipment_sofa_2_seats:what_th`
- Category: `equipment`
- Title: Sofa 2 seats
- Source hash: `67b9801f6e5cd28b3b27b7a41cceceeaaf651875b81d70efd13599adb5ab8ba8`

**Thai source**

โซฟาสำหรับนั่งเล่นเกมใน Nintendo Switch Zone

**English draft**

Couch for playing games in Nintendo Switch Zone

## 437. equipment_sony_playstation_vr2 / how_to_use_th

- Selector: `equipment_sony_playstation_vr2:how_to_use_th`
- Category: `equipment`
- Title: Sony PlayStation VR2
- Source hash: `99ce5a080410974189b74ba564594a9250eadf88416204315e47a7403c9a3278`

**Thai source**

จอง VR Zone แล้วสวมแว่น PlayStation VR2 และใช้คอนโทรลเลอร์ตามคำแนะนำของเจ้าหน้าที่หรือเกม

**English draft**

Book VR Zone, then put on PlayStation VR2 headset and use the controllers as instructed by staff or according to game guidelines.

## 438. equipment_sony_playstation_vr2 / use_cases_th

- Selector: `equipment_sony_playstation_vr2:use_cases_th`
- Category: `equipment`
- Title: Sony PlayStation VR2
- Source hash: `0c46b95666e5d6545dc01832aef8e7c09183f8ec9feb4bce89e9f1d28f3a01a0`

**Thai source**

['เล่น Beat Saber', 'เล่น Horizon Call of the Mountain']

**English draft**

Play Beat Saber Play Horizon Call of the Mountain

## 439. equipment_sony_playstation_vr2 / what_th

- Selector: `equipment_sony_playstation_vr2:what_th`
- Category: `equipment`
- Title: Sony PlayStation VR2
- Source hash: `7606777548671b806e0a089928a2c01d68d005b1866e1aa15e42842138ae9cc4`

**Thai source**

ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone

**English draft**

VR headset set for playing virtual reality games in VR Zone

## 440. equipment_tv_65 / how_to_use_th

- Selector: `equipment_tv_65:how_to_use_th`
- Category: `equipment`
- Title: TV 65 นิ้ว
- Source hash: `5926bb7d3c6564408ca955bdc9cc4a97247049ddf80c0c3344c0503836bed895`

**Thai source**

ใช้งานพร้อมชุด Cockpit และพวงมาลัยที่ศูนย์จัดไว้ ผู้ใช้ไม่จำเป็นต้องปรับสายหรือเคลื่อนย้ายทีวีเอง

**English draft**

Use with the cockpit and steering wheel setup provided at the center. Users do not need to adjust the cable or move the TV themselves.

## 441. equipment_tv_65 / use_cases_th

- Selector: `equipment_tv_65:use_cases_th`
- Category: `equipment`
- Title: TV 65 นิ้ว
- Source hash: `a218c47048dc52f18f2101d04daffe8d40965af33f312bcd55c56f9fe6c23185`

**Thai source**

['แสดงผลเกม Gran Turismo 7 ใน Cockpit Zone']

**English draft**

Displays Gran Turismo 7 in Cockpit Zone

## 442. equipment_tv_65 / what_th

- Selector: `equipment_tv_65:what_th`
- Category: `equipment`
- Title: TV 65 นิ้ว
- Source hash: `53cf4c62513d8149e0cb7dddb113edf0cbe2d86b273497793f483721f14a4eb5`

**Thai source**

จอทีวีขนาด 65 นิ้วสำหรับแสดงภาพเกมขับรถใน Cockpit Zone

**English draft**

65-inch TV for displaying racing game visuals in Cockpit Zone

## 443. equipment_tv_86 / how_to_use_th

- Selector: `equipment_tv_86:how_to_use_th`
- Category: `equipment`
- Title: TV 86 นิ้ว
- Source hash: `b90c2a8fd6f5499a26e74fc0b8870606769cc85ae23edcd4b044f76932f08395`

**Thai source**

ใช้งานพร้อม Nintendo Switch OLED ใน Nintendo Switch Zone ตามรอบบริการ

**English draft**

Use with Nintendo Switch OLED in Nintendo Switch Zone during service rounds

## 444. equipment_tv_86 / use_cases_th

- Selector: `equipment_tv_86:use_cases_th`
- Category: `equipment`
- Title: TV 86 นิ้ว
- Source hash: `c1b2f51552bdb2ddedf6bbd480d558c26c32333c12127e395232107435c53f13`

**Thai source**

['แสดงผลเกม Nintendo Switch เช่น Mario Kart, Overcooked, Super Smash Bros และ Switch Sports']

**English draft**

Displays Nintendo Switch games such as Mario Kart, Overcooked, Super Smash Bros., and Switch Sports

## 445. equipment_tv_86 / what_th

- Selector: `equipment_tv_86:what_th`
- Category: `equipment`
- Title: TV 86 นิ้ว
- Source hash: `d08028807add97d8ddf88f844d353f54715932c8e513611f3d3f8d606ea5d70a`

**Thai source**

จอทีวีขนาด 86 นิ้วสำหรับเล่นเกม Nintendo Switch เป็นกลุ่ม

**English draft**

An 86-inch TV for playing Nintendo Switch is the group

## 446. game_detail_animal_crossing / genre

- Selector: `game_detail_animal_crossing:genre`
- Category: `games`
- Title: Animal Crossing: New Horizons
- Source hash: `377ddce31ad74a9f13851326e5fdb6550b9b899253ddf7c4d69d55fef3aaf534`

**Thai source**

เกม Life Simulation

**English draft**

Life Simulation

## 447. game_detail_animal_crossing / how_to_play_th

- Selector: `game_detail_animal_crossing:how_to_play_th`
- Category: `games`
- Title: Animal Crossing: New Horizons
- Source hash: `353f9dae08988e5f9aaf71b29e472aaec3fcce879bc8507e6a5023b444fe9321`

**Thai source**

เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน

**English draft**

Play casually by gathering resources, fishing, catching insects, decorating the island, and completing daily activities

## 448. game_detail_animal_crossing / summary_th

- Selector: `game_detail_animal_crossing:summary_th`
- Category: `games`
- Title: Animal Crossing: New Horizons
- Source hash: `a14ddfb819047343a962c4f56c0357346a95376214511f2fd3405ceda9aeb1e5`

**Thai source**

Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ

**English draft**

Animal Crossing: New Horizons is a life simulation game where players decorate homes, collect items, create spaces, and chat with island residents.

## 449. game_detail_beat_saber / genre

- Selector: `game_detail_beat_saber:genre`
- Category: `games`
- Title: Beat Saber
- Source hash: `5c025eb8f4c966520d9296d6dcafb9bfaec4af0898c1001ba0fa50085256c539`

**Thai source**

เกม VR Rhythm

**English draft**

VR Rhythm Game

## 450. game_detail_beat_saber / how_to_play_th

- Selector: `game_detail_beat_saber:how_to_play_th`
- Category: `games`
- Title: Beat Saber
- Source hash: `620a09253f59a034e02245d41500b3925e062c65757cb86b610e19bc25fbbf4d`

**Thai source**

สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง

**English draft**

Put on VR glasses, hold the controller, and smash blocks in the direction indicated. Dodge obstacles and try to score points according to the rhythm of the music.

## 451. game_detail_beat_saber / summary_th

- Selector: `game_detail_beat_saber:summary_th`
- Category: `games`
- Title: Beat Saber
- Source hash: `855154ac969b4d73f74e426030bbc61e77e7e328b9736d6ad19f675d8cdc0f33`

**Thai source**

Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง

**English draft**

Beat Saber is a rhythm-based VR game where players slash blocks in time with the music.

## 452. game_detail_call_of_duty_mw3 / genre

- Selector: `game_detail_call_of_duty_mw3:genre`
- Category: `games`
- Title: Call of Duty: Modern Warfare III
- Source hash: `b488334ef74ca9cd57a750bf3af48dd4ca4e8369212bd3ffadcda0977a02d674`

**Thai source**

เกมยิง FPS

**English draft**

FPS

## 453. game_detail_call_of_duty_mw3 / how_to_play_th

- Selector: `game_detail_call_of_duty_mw3:how_to_play_th`
- Category: `games`
- Title: Call of Duty: Modern Warfare III
- Source hash: `a653e029e66dd3c6d687d3895af09abb2941fbd250f8cc1ac66180cac3c0b02b`

**Thai source**

เล็ง ยิง เคลื่อนที่ ใช้อุปกรณ์ และทำ objective ของโหมดเกมหรือภารกิจให้สำเร็จ

**English draft**

Aim, shoot, move, use equipment, and complete the game mode or mission objectives

## 454. game_detail_call_of_duty_mw3 / summary_th

- Selector: `game_detail_call_of_duty_mw3:summary_th`
- Category: `games`
- Title: Call of Duty: Modern Warfare III
- Source hash: `e97f1628ef73343607e7021aac8edfb89ef4ee4a247585a6449b7f19874bfbac`

**Thai source**

Call of Duty: Modern Warfare III คือเกมยิงมุมมองบุคคลที่หนึ่งที่เน้นภารกิจและการยิงต่อสู้แบบรวดเร็ว

**English draft**

Call of Duty: Modern Warfare III is a first-person shooter game emphasizing fast-paced missions and combat.

## 455. game_detail_cs2 / genre

- Selector: `game_detail_cs2:genre`
- Category: `games`
- Title: Counter-Strike 2
- Source hash: `7aa434ecb07965447924bcf66d300cd7738b8d3dd61feacdfd63a662424386b1`

**Thai source**

เกมยิง Tactical FPS

**English draft**

Tactical FPS

## 456. game_detail_cs2 / how_to_play_th

- Selector: `game_detail_cs2:how_to_play_th`
- Category: `games`
- Title: Counter-Strike 2
- Source hash: `7f6cce1e0a1b2369d986205f97bb938da65bb646f36b96631ede4ad6db283546`

**Thai source**

เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ

**English draft**

Play in rounds, must buy weapons, plan with your team, control territory, and use aiming along with communication to win the round

## 457. game_detail_cs2 / summary_th

- Selector: `game_detail_cs2:summary_th`
- Category: `games`
- Title: Counter-Strike 2
- Source hash: `f28ed0a9c6b791ab27335484ed3f68cb5a501d9fddcca61806c739fb1e7db7e2`

**Thai source**

Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม

**English draft**

Counter-Strike 2 is a team-based competitive shooting game where players are divided into offensive and defensive teams, with the main objective being to place or defuse explosives or manage the opposing team.

## 458. game_detail_ea_sports_fc_24 / genre

- Selector: `game_detail_ea_sports_fc_24:genre`
- Category: `games`
- Title: EA Sports FC 24
- Source hash: `6f72579a4e205518f79d9b5e68fc1c028c7504aa62d495e7ecb1de203ed0bc2b`

**Thai source**

เกมฟุตบอล

**English draft**

football

## 459. game_detail_ea_sports_fc_24 / how_to_play_th

- Selector: `game_detail_ea_sports_fc_24:how_to_play_th`
- Category: `games`
- Title: EA Sports FC 24
- Source hash: `321169ee9fa3c466edfb936fa9f7e0e5cd2a2b849c7cefa4e8482f54343076c9`

**Thai source**

เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง

**English draft**

Select a team, form up, control ball passing, dribble, shoot, and defend to score more goals than the opponent

## 460. game_detail_ea_sports_fc_24 / summary_th

- Selector: `game_detail_ea_sports_fc_24:summary_th`
- Category: `games`
- Title: EA Sports FC 24
- Source hash: `dd6851e81e8dfd89344f6dbfa6e2dfff39a3d754cd9274f3b82c8633db2cb60d`

**Thai source**

EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล

**English draft**

EA Sports FC 24 is a football game where players control teams, compete, score goals, and plan matches just like real football games.

## 461. game_detail_final_fantasy_xvi / genre

- Selector: `game_detail_final_fantasy_xvi:genre`
- Category: `games`
- Title: FINAL FANTASY XVI
- Source hash: `6a0ef0211109e7ba55db517d3fed601820868b013c5d412e94f35344402c7fc6`

**Thai source**

เกม Action RPG

**English draft**

Action RPG

## 462. game_detail_final_fantasy_xvi / how_to_play_th

- Selector: `game_detail_final_fantasy_xvi:how_to_play_th`
- Category: `games`
- Title: FINAL FANTASY XVI
- Source hash: `56111ee5e0a0b56e534ec8aea790cfe585225fa9d139246163cc1c1fd74ca1d3`

**Thai source**

เล่นตามเนื้อเรื่อง ต่อสู้ด้วยสกิล/คอมโบ ทำภารกิจ และพัฒนาความสามารถของตัวละคร

**English draft**

Follow the storyline, fight using skills/combo, complete missions and develop your character's abilities

## 463. game_detail_final_fantasy_xvi / summary_th

- Selector: `game_detail_final_fantasy_xvi:summary_th`
- Category: `games`
- Title: FINAL FANTASY XVI
- Source hash: `87376394cb7c576c5ad866bd6832fec7a42d20e16181c97db00ab08fd3b31b45`

**Thai source**

FINAL FANTASY XVI คือเกมแอ็กชัน RPG แฟนตาซีที่เน้นเนื้อเรื่อง การต่อสู้ และการพัฒนาตัวละคร

**English draft**

FINAL FANTASY XVI is a fantasy action RPG that emphasizes story, combat, and character development.

## 464. game_detail_fortnite / genre

- Selector: `game_detail_fortnite:genre`
- Category: `games`
- Title: Fortnite
- Source hash: `dfc187b6b72b5e86880ca1e7d1778005881e512346c380a59463ca7155dc5277`

**Thai source**

เกม Battle Royale / Action

**English draft**

Battle Royale / Action

## 465. game_detail_fortnite / how_to_play_th

- Selector: `game_detail_fortnite:how_to_play_th`
- Category: `games`
- Title: Fortnite
- Source hash: `fa140b19ecd1acfec404e89dcc26173734a2007122dedd1f91f2e1f9f91733be`

**Thai source**

เก็บอาวุธ เคลื่อนตามวง ต่อสู้กับผู้เล่นอื่น และใช้การสร้างหรือโหมดไม่สร้างตามรูปแบบที่เลือก

**English draft**

Collect weapons, move around the ring, fight other players, and use either creation or non-creation modes based on the selected format

## 466. game_detail_fortnite / summary_th

- Selector: `game_detail_fortnite:summary_th`
- Category: `games`
- Title: Fortnite
- Source hash: `557a92da5c7e62fc81d04b16f9670d155f587121d1969d09a2831cd72419fece`

**Thai source**

Fortnite คือเกมต่อสู้เอาชีวิตรอดที่ผู้เล่นแข่งกันในแผนที่ขนาดใหญ่และพยายามอยู่เป็นคนสุดท้าย

**English draft**

Fortnite is a battle royale game where players compete on large maps and try to be the last one standing

## 467. game_detail_god_of_war_ragnarok / genre

- Selector: `game_detail_god_of_war_ragnarok:genre`
- Category: `games`
- Title: God of War Ragnarok
- Source hash: `411ce98360c7a9a887dd0c7ffa061671cca58fb87424cb7371c667cdb9a11179`

**Thai source**

เกม Action-Adventure

**English draft**

Action-Adventure

## 468. game_detail_god_of_war_ragnarok / how_to_play_th

- Selector: `game_detail_god_of_war_ragnarok:how_to_play_th`
- Category: `games`
- Title: God of War Ragnarok
- Source hash: `e68e47fed17501615adb13ecb3fef23ccbb3304b54597d5f321361382ef0443f`

**Thai source**

ควบคุมตัวละครหลัก ต่อสู้กับศัตรู แก้ปริศนา สำรวจพื้นที่ และพัฒนาอาวุธ/สกิลตามเนื้อเรื่อง

**English draft**

Control the main character, fight enemies, solve puzzles, explore areas, and develop weapons/skills according to the story.

## 469. game_detail_god_of_war_ragnarok / summary_th

- Selector: `game_detail_god_of_war_ragnarok:summary_th`
- Category: `games`
- Title: God of War Ragnarok
- Source hash: `bce92022eb977d74c1014da89d9373a344f7381047c67c583b426881b6c5982b`

**Thai source**

God of War Ragnarok คือเกมแอ็กชันผจญภัยที่เน้นเนื้อเรื่อง การต่อสู้ และการสำรวจในโลกตำนานนอร์ส

**English draft**

God of War Ragnarök is an action-adventure game that emphasizes story, combat, and exploration in a legendary Norse world.

## 470. game_detail_gran_turismo_7 / genre

- Selector: `game_detail_gran_turismo_7:genre`
- Category: `games`
- Title: Gran Turismo 7
- Source hash: `d054f31c1d51600361cc0615a99ff405b5cc2ccbfe2e30f23b7fc501e2d13417`

**Thai source**

เกมแข่งรถ / Driving Simulator

**English draft**

Racing / Driving Simulator

## 471. game_detail_gran_turismo_7 / how_to_play_th

- Selector: `game_detail_gran_turismo_7:how_to_play_th`
- Category: `games`
- Title: Gran Turismo 7
- Source hash: `770978a78a12d3d6bee502fb301ad76ae6a6b8ceae661c7060199c2f13785ed6`

**Thai source**

ใน Cockpit Zone เล่นโดยใช้พวงมาลัย คันเร่ง เบรก และชุดเบาะจำลองการขับรถ เป้าหมายคือขับให้เร็วและควบคุมรถให้แม่นในแต่ละสนาม

**English draft**

In Cockpit Zone, play using the steering wheel, accelerator, brake, and simulated seat controls. The objective is to drive quickly and maintain precise vehicle control in each arena.

## 472. game_detail_gran_turismo_7 / summary_th

- Selector: `game_detail_gran_turismo_7:summary_th`
- Category: `games`
- Title: Gran Turismo 7
- Source hash: `a7b31d4dd6cf3d708245de217b9f47a8297a8297acce3c11d62f441c890e90bc`

**Thai source**

Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง

**English draft**

Gran Turismo 7 is a racing game that emphasizes realistic driving. Players choose tracks, cars, and control their cornering rhythm.

## 473. game_detail_hogwarts_legacy / genre

- Selector: `game_detail_hogwarts_legacy:genre`
- Category: `games`
- Title: Hogwarts Legacy
- Source hash: `7ebbce68f16745232c983f4dfcac953205e46983b26cae0b103d0bfc36c1e6f2`

**Thai source**

เกม Open-world Action RPG

**English draft**

Open-world Action RPG

## 474. game_detail_hogwarts_legacy / how_to_play_th

- Selector: `game_detail_hogwarts_legacy:how_to_play_th`
- Category: `games`
- Title: Hogwarts Legacy
- Source hash: `359539affe43a9466f30dbaec0390f25d1449f531b70bc738bc544ce32d30061`

**Thai source**

สำรวจพื้นที่ ใช้คาถา ต่อสู้ แก้ปริศนา และทำเควสต์เพื่อพัฒนาตัวละคร

**English draft**

Explore areas, use spells, fight enemies, solve puzzles, and complete quests to level up your character

## 475. game_detail_hogwarts_legacy / summary_th

- Selector: `game_detail_hogwarts_legacy:summary_th`
- Category: `games`
- Title: Hogwarts Legacy
- Source hash: `4a2608545bb81e311d1a8a12168de0437f54ce8cf346eebed840339ad2eaff4c`

**Thai source**

Hogwarts Legacy คือเกมผจญภัยในโลกเวทมนตร์ ผู้เล่นเรียนคาถา สำรวจ และทำภารกิจในฮอกวอตส์และพื้นที่รอบ ๆ

**English draft**

Hogwarts Legacy is a fantasy adventure game where players learn spells, explore, and complete quests in Hogwarts and the surrounding areas.

## 476. game_detail_horizon_call_of_the_mountain / genre

- Selector: `game_detail_horizon_call_of_the_mountain:genre`
- Category: `games`
- Title: Horizon Call of the Mountain
- Source hash: `992c9e73e95b024d228631feee11abbb4b2aa91e90b4974a51c4ed13bbb8f23f`

**Thai source**

เกม VR Action-Adventure

**English draft**

VR Action-Adventure

## 477. game_detail_horizon_call_of_the_mountain / how_to_play_th

- Selector: `game_detail_horizon_call_of_the_mountain:how_to_play_th`
- Category: `games`
- Title: Horizon Call of the Mountain
- Source hash: `d81dc251c073d7b9e38918e71f2ee2bb9fbe873da2533dc7d87272f427f6a04a`

**Thai source**

สวมแว่น VR ใช้คอนโทรลเลอร์ปีน เคลื่อนที่ เล็งธนู และทำภารกิจตามฉาก

**English draft**

Put on VR glasses, use the controller to climb, move around, aim your bow, and complete scene-specific quests

## 478. game_detail_horizon_call_of_the_mountain / summary_th

- Selector: `game_detail_horizon_call_of_the_mountain:summary_th`
- Category: `games`
- Title: Horizon Call of the Mountain
- Source hash: `b31f60c5e1befaae1f90ee6f271ddc108b48af68d04e665f533894d66ce2b925`

**Thai source**

Horizon Call of the Mountain คือเกม VR ผจญภัยในโลก Horizon ที่เน้นการปีนป่าย สำรวจ และต่อสู้กับจักรกล

**English draft**

Horizon Call of the Mountain is a VR adventure game set in the Horizon world, emphasizing climbing, exploration, and combat with machinery.

## 479. game_detail_it_takes_two / genre

- Selector: `game_detail_it_takes_two:genre`
- Category: `games`
- Title: It Takes Two
- Source hash: `c5018c7a0c9f9fa3f15b7bb0ba90fe4127f001be44bb89648cf5e38e3db319e9`

**Thai source**

เกม Co-op Adventure

**English draft**

Co-op Adventure

## 480. game_detail_it_takes_two / how_to_play_th

- Selector: `game_detail_it_takes_two:how_to_play_th`
- Category: `games`
- Title: It Takes Two
- Source hash: `ae738c75244766aa60315e0283ce93a41a25f6ed9069350ec452865b20898971`

**Thai source**

ผู้เล่นสองคนต้องสื่อสาร แบ่งหน้าที่ ใช้ความสามารถของตัวละคร และช่วยกันผ่านอุปสรรค

**English draft**

Two players must communicate, divide responsibilities, use character abilities, and work together to overcome obstacles

## 481. game_detail_it_takes_two / summary_th

- Selector: `game_detail_it_takes_two:summary_th`
- Category: `games`
- Title: It Takes Two
- Source hash: `5de3ca8f8a920f640fc43dd94f8380e67be8b6f401e7443261de70379126aabb`

**Thai source**

It Takes Two คือเกมผจญภัยสำหรับเล่นร่วมกันสองคน ที่ต้องช่วยกันแก้ปริศนาและผ่านด่าน

**English draft**

It Takes Two is a cooperative adventure game where two players must work together to solve puzzles and progress through levels.

## 482. game_detail_league_of_legends / genre

- Selector: `game_detail_league_of_legends:genre`
- Category: `games`
- Title: League of Legends
- Source hash: `8025ea66bf896fade9a41ddd6699914ef951ad4346fb9734b778452b50b84684`

**Thai source**

เกม MOBA แบบทีม 5v5

**English draft**

MOBA game

## 483. game_detail_league_of_legends / how_to_play_th

- Selector: `game_detail_league_of_legends:how_to_play_th`
- Category: `games`
- Title: League of Legends
- Source hash: `7413ee725f2c4d95ee94e005be574d23628d4eb428a53ecac7f79b2dd9f4c3b7`

**Thai source**

แบ่งเลน ฟาร์มเงินและเลเวล คุม objective ช่วยทีมไฟต์ และดันเข้าไปทำลาย Nexus ของศัตรู

**English draft**

Split lanes, farm gold and levels, control objectives, assist the team in fights, and push into enemy Nexus to destroy it

## 484. game_detail_league_of_legends / summary_th

- Selector: `game_detail_league_of_legends:summary_th`
- Category: `games`
- Title: League of Legends
- Source hash: `f4a683a64f8376592730fc0fcbc82bffde9737a8f5a6778a01292452d050ab35`

**Thai source**

League of Legends คือเกมวางแผนต่อสู้แบบทีม ผู้เล่นเลือก Champion และร่วมกันทำลายฐานหลักของฝ่ายตรงข้าม

**English draft**

League of Legends is a team-based tactical combat game where players choose Champions and work together to destroy the opposing team's base.

## 485. game_detail_little_nightmares_2 / genre

- Selector: `game_detail_little_nightmares_2:genre`
- Category: `games`
- Title: Little Nightmares II
- Source hash: `674fe54961093cd363eb0da14e8f6d3b146353a998a50ba3d00166a445fe9506`

**Thai source**

เกม Puzzle Platform / Horror

**English draft**

Puzzle Platform / Horror

## 486. game_detail_little_nightmares_2 / how_to_play_th

- Selector: `game_detail_little_nightmares_2:how_to_play_th`
- Category: `games`
- Title: Little Nightmares II
- Source hash: `d7e48d7b8d91000d9a502c0734bedfab92512b680b83197d97c82699da9ae288`

**Thai source**

เดิน สำรวจ หลบศัตรู ใช้สิ่งของในฉากแก้ปริศนา และหาจังหวะผ่านอุปสรรค

**English draft**

Walk, explore, avoid enemies, use in-scene items to solve puzzles, and find opportunities to overcome obstacles

## 487. game_detail_little_nightmares_2 / summary_th

- Selector: `game_detail_little_nightmares_2:summary_th`
- Category: `games`
- Title: Little Nightmares II
- Source hash: `b1da6c80c638a52f92ac799e9fc66eabe2f50ce53363b464667fc90ed8b465ff`

**Thai source**

Little Nightmares II คือเกมผจญภัยบรรยากาศสยองที่เน้นการหลบหนี แก้ปริศนา และผ่านฉากอันตราย

**English draft**

Little Nightmares II is a horror-themed adventure game focusing on evasion, puzzle-solving, and navigating dangerous scenes.

## 488. game_detail_luigis_mansion_3 / genre

- Selector: `game_detail_luigis_mansion_3:genre`
- Category: `games`
- Title: Luigi's Mansion 3
- Source hash: `f26ee1c8f2e27c67efb57d6b18202290c84a07cb4adcfc35a8a94294a30a5533`

**Thai source**

เกม Action Puzzle

**English draft**

Action Puzzle

## 489. game_detail_luigis_mansion_3 / how_to_play_th

- Selector: `game_detail_luigis_mansion_3:how_to_play_th`
- Category: `games`
- Title: Luigi's Mansion 3
- Source hash: `69205d7d561516a0501f0e1ffd79e12679ebd2c44414e8144fbe187d850ed445`

**Thai source**

ใช้เครื่องดูดผี สำรวจห้อง แก้ปริศนา และจับผีเพื่อผ่านด่าน

**English draft**

Use the spirit vacuum to explore rooms, solve puzzles, and catch ghosts to progress through stages

## 490. game_detail_luigis_mansion_3 / summary_th

- Selector: `game_detail_luigis_mansion_3:summary_th`
- Category: `games`
- Title: Luigi's Mansion 3
- Source hash: `93eb5a37efc16c89654dd5c58ce20c3e4e8f45661da2a1f810e2c69f2fe5a69b`

**Thai source**

Luigi's Mansion 3 คือเกมผจญภัยจับผีที่ผู้เล่นสำรวจโรงแรมและแก้ปริศนา

**English draft**

Luigi's Mansion 3 is a horror-themed exploration game where players explore a haunted hotel and solve puzzles.

## 491. game_detail_mario_kart_8 / genre

- Selector: `game_detail_mario_kart_8:genre`
- Category: `games`
- Title: Mario Kart 8 Deluxe
- Source hash: `2a583c56ab775c75591e1e8171c06c7cb2f4fefbbca3e8f8809e49c5ea72ab95`

**Thai source**

เกมแข่งรถ Party Racing

**English draft**

Racing Party Racing

## 492. game_detail_mario_kart_8 / how_to_play_th

- Selector: `game_detail_mario_kart_8:how_to_play_th`
- Category: `games`
- Title: Mario Kart 8 Deluxe
- Source hash: `045e23feb100b8b8a7f6cfdc1796a982d9a855312f04161041b244a2a12bff16`

**Thai source**

เลือกตัวละครและรถ ขับเข้าเส้นชัย ใช้ไอเทมช่วยโจมตี/ป้องกัน และเล่นสนุกได้หลายคน

**English draft**

Choose a character and vehicle, drive to the finish line, use items to attack or defend, and enjoy multiplayer gameplay

## 493. game_detail_mario_kart_8 / summary_th

- Selector: `game_detail_mario_kart_8:summary_th`
- Category: `games`
- Title: Mario Kart 8 Deluxe
- Source hash: `1e45cc5bb04ee53bfebac0ee3d9048209112277085280b04089e1815d4a5fddd`

**Thai source**

Mario Kart 8 Deluxe คือเกมแข่งรถสไตล์ปาร์ตี้ที่ใช้ตัวละคร Nintendo ขับรถแข่งกันในสนามหลากหลายแบบ

**English draft**

Mario Kart 8 Deluxe is a party-style racing game featuring Nintendo characters racing on diverse tracks.

## 494. game_detail_mario_party / genre

- Selector: `game_detail_mario_party:genre`
- Category: `games`
- Title: Mario Party Superstars
- Source hash: `65f1d26b8739b38d6a6c05f92ab6ac46543daedc78b81d6a450feda8126bf04f`

**Thai source**

เกม Party / Mini-games

**English draft**

Party / Mini-games

## 495. game_detail_mario_party / how_to_play_th

- Selector: `game_detail_mario_party:how_to_play_th`
- Category: `games`
- Title: Mario Party Superstars
- Source hash: `162bff6e225576e250f1860c1662e7ed32c5b39fa9ec94a9873abf10f6b21d53`

**Thai source**

ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน

**English draft**

Roll the dice to move across the board, collect stars, and play mini-games to earn points

## 496. game_detail_mario_party / summary_th

- Selector: `game_detail_mario_party:summary_th`
- Category: `games`
- Title: Mario Party Superstars
- Source hash: `45326fc9a7c9de265b86948e12830f98743d9619a3bc2a46c54bc47321438d5d`

**Thai source**

Mario Party Superstars คือเกมปาร์ตี้ที่เล่นบนกระดานและแข่งมินิเกมกับเพื่อน

**English draft**

Mario Party Superstars is a party game played on a board and competes in mini-games with friends

## 497. game_detail_monster_hunter_rise / genre

- Selector: `game_detail_monster_hunter_rise:genre`
- Category: `games`
- Title: Monster Hunter Rise
- Source hash: `f9345651ed3bec149558fd3601c72dab5e59793bc24d5b747c6ca14689cecde2`

**Thai source**

เกม Action RPG ล่ามอนสเตอร์

**English draft**

Action RPG monster hunting game

## 498. game_detail_monster_hunter_rise / how_to_play_th

- Selector: `game_detail_monster_hunter_rise:how_to_play_th`
- Category: `games`
- Title: Monster Hunter Rise
- Source hash: `58ccb6a1c1d3d285f23188965b1b1304ad53804e275bf62032974cbc2a068d27`

**Thai source**

เลือกอาวุธ รับเควสต์ ตามหามอนสเตอร์ หลบ/โจมตีให้ถูกจังหวะ และคราฟต์อุปกรณ์จากวัตถุดิบ

**English draft**

Choose a weapon, accept quests, hunt monsters, dodge and attack at the right moment, and craft equipment from raw materials

## 499. game_detail_monster_hunter_rise / summary_th

- Selector: `game_detail_monster_hunter_rise:summary_th`
- Category: `games`
- Title: Monster Hunter Rise
- Source hash: `230b42b00b1ebb41eb04674b5a36e4d9009a7710a78f25f80c758de05d62fbda`

**Thai source**

Monster Hunter Rise คือเกมล่ามอนสเตอร์ที่ผู้เล่นเลือกอาวุธ ทำภารกิจ และเก็บวัตถุดิบมาสร้างอุปกรณ์

**English draft**

Monster Hunter Rise is a monster hunting game where players choose weapons, complete missions, and gather materials to craft equipment.

## 500. game_detail_moving_out_2 / genre

- Selector: `game_detail_moving_out_2:genre`
- Category: `games`
- Title: Moving Out 2
- Source hash: `425c17508d5b40733ce127d1cb1d717fd2bf3aa0ec2d4d8cb0192a4c9cdb0606`

**Thai source**

เกม Co-op Puzzle / Party

**English draft**

Co-op Puzzle / Party

## 501. game_detail_moving_out_2 / how_to_play_th

- Selector: `game_detail_moving_out_2:how_to_play_th`
- Category: `games`
- Title: Moving Out 2
- Source hash: `d5c25435be8735ecee21c69c42628c8f8e0bfa604bb35fc7a059c9bdf7754d1c`

**Thai source**

ช่วยกันยก โยน วางแผนเส้นทาง และขนของให้เสร็จภายในเวลา

**English draft**

Work together to lift, toss, plan routes, and deliver items within the time limit

## 502. game_detail_moving_out_2 / summary_th

- Selector: `game_detail_moving_out_2:summary_th`
- Category: `games`
- Title: Moving Out 2
- Source hash: `8b9f13e4556561614ba19eda1aafe6c8cca1cfc05c2f25f9c5e4ef47c921b640`

**Thai source**

Moving Out 2 คือเกมย้ายของแบบร่วมมือกันที่ต้องช่วยกันขนของผ่านฉากวุ่น ๆ

**English draft**

Moving Out 2 is a cooperative moving game where players must help carry items through a chaotic environment.

## 503. game_detail_naruto_x_boruto / genre

- Selector: `game_detail_naruto_x_boruto:genre`
- Category: `games`
- Title: NARUTO X BORUTO Ultimate Ninja Storm Connections
- Source hash: `32c9a05be5724e82c33c68c21ebdc7278dea23d6f70e7cb3d151421c0223ab7e`

**Thai source**

เกมต่อสู้จากอนิเมะ

**English draft**

Fighting game from anime

## 504. game_detail_naruto_x_boruto / how_to_play_th

- Selector: `game_detail_naruto_x_boruto:how_to_play_th`
- Category: `games`
- Title: NARUTO X BORUTO Ultimate Ninja Storm Connections
- Source hash: `7340a305dd12ce89e7de6a923abe43e208669da1bc6c1b54eddf692f762cdb6e`

**Thai source**

เลือกตัวละคร ใช้คอมโบ สกิลนินจา และจังหวะหลบ/สวนกลับเพื่อเอาชนะคู่ต่อสู้

**English draft**

Select a character, use combos, ninja skills, and timing for dodging and countering to defeat your opponent

## 505. game_detail_naruto_x_boruto / summary_th

- Selector: `game_detail_naruto_x_boruto:summary_th`
- Category: `games`
- Title: NARUTO X BORUTO Ultimate Ninja Storm Connections
- Source hash: `4bb3572f4279c257b58d74cf3384e1ce1c622cd24c72d2f015a56be1776151b3`

**Thai source**

NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมต่อสู้ที่ใช้ตัวละครจากจักรวาล Naruto/Boruto

**English draft**

NARUTO X BORUTO Ultimate Ninja Storm Connections is a fighting game featuring characters from the Naruto/Boruto universe.

## 506. game_detail_new_super_mario_bros / genre

- Selector: `game_detail_new_super_mario_bros:genre`
- Category: `games`
- Title: New Super Mario Bros. U Deluxe
- Source hash: `ddf4138c35c5e8e3daf6ed87d2b0c544ac2db3846487c37d57495fa3f0bd3851`

**Thai source**

เกม Platformer 2D

**English draft**

Genre: Platformer 2D

## 507. game_detail_new_super_mario_bros / how_to_play_th

- Selector: `game_detail_new_super_mario_bros:how_to_play_th`
- Category: `games`
- Title: New Super Mario Bros. U Deluxe
- Source hash: `5ebdcc8e537f0d202ee6a5c427e70591cae7ae3ded8b8a80ef6c4dcb12b619c8`

**Thai source**

วิ่ง กระโดด ใช้ power-up ผ่านด่าน และร่วมมือกับเพื่อนได้หลายคน

**English draft**

Run, jump, use power-ups to progress through levels and play with multiple teammates

## 508. game_detail_new_super_mario_bros / summary_th

- Selector: `game_detail_new_super_mario_bros:summary_th`
- Category: `games`
- Title: New Super Mario Bros. U Deluxe
- Source hash: `ce5d01a1e346387e97a9d3880783e86e4ea82889c56d04f6b759b70e46dfdcb1`

**Thai source**

New Super Mario Bros. U Deluxe คือเกมมาริโอแบบเดินลุยด่าน กระโดด หลบศัตรู และเก็บเหรียญ

**English draft**

New Super Mario Bros. U Deluxe is a Mario-style platformer game featuring jumping, enemy evasion, and coin collection.

## 509. game_detail_overcooked_2 / genre

- Selector: `game_detail_overcooked_2:genre`
- Category: `games`
- Title: Overcooked 2
- Source hash: `c78df092aac5422d032567f9fb1d1d5caccc5377f8a7b9df3b1f023183cb3462`

**Thai source**

เกม Co-op ทำอาหาร

**English draft**

Co-op cooking game

## 510. game_detail_overcooked_2 / how_to_play_th

- Selector: `game_detail_overcooked_2:how_to_play_th`
- Category: `games`
- Title: Overcooked 2
- Source hash: `bbdf988b66f01c7505e5569a76dd8ceb7d523fb489d40b667083426b9f42962e`

**Thai source**

ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา

**English draft**

Work together to chop ingredients, cook, serve, clean up, and communicate with the team on time

## 511. game_detail_overcooked_2 / summary_th

- Selector: `game_detail_overcooked_2:summary_th`
- Category: `games`
- Title: Overcooked 2
- Source hash: `b79e2fe9ec538ac4265dced54bbe4ef19cb2846b166807bca1bf1251959d353f`

**Thai source**

Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย

**English draft**

Overcooked 2 is a cooperative cooking game where players must divide tasks, prepare food, serve dishes, and manage a chaotic kitchen.

## 512. game_detail_pubg / genre

- Selector: `game_detail_pubg:genre`
- Category: `games`
- Title: PUBG: BATTLEGROUNDS
- Source hash: `6621be569dc65d545b5abe7ad6a77f230159d6463936294d8e83c62252e51eeb`

**Thai source**

เกม Battle Royale

**English draft**

Battle Royale game

## 513. game_detail_pubg / how_to_play_th

- Selector: `game_detail_pubg:how_to_play_th`
- Category: `games`
- Title: PUBG: BATTLEGROUNDS
- Source hash: `4e2030b99523ecd40465c010e353dfb05841c5b5b1b128c443b49c439a719964`

**Thai source**

เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม

**English draft**

Choose spawn point, find weapons, enter safe zone, position yourself, and fight against the other team until one team wins at the end of the game

## 514. game_detail_pubg / summary_th

- Selector: `game_detail_pubg:summary_th`
- Category: `games`
- Title: PUBG: BATTLEGROUNDS
- Source hash: `cc8f1e55dce34db42dc63feb72c11a9f4534c6a5a413876500c10078c89bdca6`

**Thai source**

PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย

**English draft**

PUBG: BATTLEGROUNDS is an escape survival game where players enter the battlefield, search for weapons and gear, and try to survive as the last person or team standing

## 515. game_detail_resident_evil_4 / genre

- Selector: `game_detail_resident_evil_4:genre`
- Category: `games`
- Title: Resident Evil 4
- Source hash: `1add304f37ce05509a7facbbbc381bfc38414aa3006f87b9b1c3c037415a997a`

**Thai source**

เกม Survival Horror / Action

**English draft**

Survival Horror / Action

## 516. game_detail_resident_evil_4 / how_to_play_th

- Selector: `game_detail_resident_evil_4:how_to_play_th`
- Category: `games`
- Title: Resident Evil 4
- Source hash: `b9dd856615c56d1a443611675f34eea7a0d7a622e2340969c2f5e1c8ba69156f`

**Thai source**

สำรวจพื้นที่ เก็บทรัพยากร ต่อสู้กับศัตรู แก้ปริศนา และเอาตัวรอดตามเนื้อเรื่อง

**English draft**

Explore the area, gather resources, fight enemies, solve puzzles, and survive according to the story.

## 517. game_detail_resident_evil_4 / summary_th

- Selector: `game_detail_resident_evil_4:summary_th`
- Category: `games`
- Title: Resident Evil 4
- Source hash: `7a81b9b53862bf46de33b4c42e239a22add65d4e4af305ed0bb1757b92fab5ca`

**Thai source**

Resident Evil 4 คือเกมเอาตัวรอดสยองขวัญที่เน้นการต่อสู้ การสำรวจ และการบริหารกระสุน/ไอเทม

**English draft**

Resident Evil 4 is a survival horror game that emphasizes combat, exploration, and ammunition/item management.

## 518. game_detail_resident_evil_village / genre

- Selector: `game_detail_resident_evil_village:genre`
- Category: `games`
- Title: Resident Evil Village
- Source hash: `8c70e5ca33df9ff8cc4f812580f7378d9bdf49e4bff98c00f1d318094de01479`

**Thai source**

เกม Survival Horror

**English draft**

Survival Horror

## 519. game_detail_resident_evil_village / how_to_play_th

- Selector: `game_detail_resident_evil_village:how_to_play_th`
- Category: `games`
- Title: Resident Evil Village
- Source hash: `8ba7555b474537e7cece027db70bb0353fb8a922e117c2f22ff4a016b4643caf`

**Thai source**

สำรวจฉาก เก็บไอเทม จัดการทรัพยากร ต่อสู้ และแก้ปริศนาเพื่อดำเนินเรื่อง

**English draft**

Explore scenes, collect items, manage resources, fight and solve puzzles to progress the story

## 520. game_detail_resident_evil_village / summary_th

- Selector: `game_detail_resident_evil_village:summary_th`
- Category: `games`
- Title: Resident Evil Village
- Source hash: `91e7322511434b221848ad321ebea44e0b6bfdea4c3ecb8145e5ac118a83a442`

**Thai source**

Resident Evil Village คือเกมสยองขวัญเอาตัวรอดที่เน้นบรรยากาศ การสำรวจ และการต่อสู้กับศัตรูหลากหลายรูปแบบ

**English draft**

Resident Evil Village is a survival horror game emphasizing atmosphere, exploration, and combat against diverse enemies.

## 521. game_detail_ring_fit_adventure / genre

- Selector: `game_detail_ring_fit_adventure:genre`
- Category: `games`
- Title: Ring Fit Adventure
- Source hash: `b1d8ca65f8963a479ce9bdb7bf53db31db4d9e5b330d1f78675e898882390d99`

**Thai source**

เกมออกกำลังกาย Adventure

**English draft**

Fitness Adventure

## 522. game_detail_ring_fit_adventure / how_to_play_th

- Selector: `game_detail_ring_fit_adventure:how_to_play_th`
- Category: `games`
- Title: Ring Fit Adventure
- Source hash: `5731a4ed2110150b3a4432a38646ed3b874a245a3ea01b6e8934c172199ca0a7`

**Thai source**

ใส่ Joy-Con กับ Ring-Con แล้วทำท่าออกกำลังกาย เช่น วิ่ง บีบ ดัน หรือยืด เพื่อโจมตีและผ่านด่าน

**English draft**

Attach Joy-Con and Ring-Con, then perform exercise motions such as running, squeezing, pushing, or stretching to attack and progress through stages.

## 523. game_detail_ring_fit_adventure / summary_th

- Selector: `game_detail_ring_fit_adventure:summary_th`
- Category: `games`
- Title: Ring Fit Adventure
- Source hash: `e78f17f6fdc977bcc22451d915aa5d01e7d0fbd569cf1ee1573bfbeb255cdc06`

**Thai source**

Ring Fit Adventure คือเกมออกกำลังกายที่ใช้ Ring-Con และท่าทางร่างกายเพื่อผจญภัยในเกม

**English draft**

Ring Fit Adventure is a fitness game that uses Ring-Con and physical movements to explore the game world.

## 524. game_detail_spider_man_2 / genre

- Selector: `game_detail_spider_man_2:genre`
- Category: `games`
- Title: Marvel's Spider-Man 2
- Source hash: `411ce98360c7a9a887dd0c7ffa061671cca58fb87424cb7371c667cdb9a11179`

**Thai source**

เกม Action-Adventure

**English draft**

Action-Adventure

## 525. game_detail_spider_man_2 / how_to_play_th

- Selector: `game_detail_spider_man_2:how_to_play_th`
- Category: `games`
- Title: Marvel's Spider-Man 2
- Source hash: `e52bdc6a8710d59cf7dde00d8ed22c626c94897ed0ab80760a7e400bd473c8c9`

**Thai source**

โหนใยเดินทาง ทำภารกิจ ใช้การต่อสู้แบบคอมโบ หลบหลีก และอัปเกรดสกิลระหว่างเนื้อเรื่อง

**English draft**

Travel, complete missions, use combo combat, dodge, and upgrade skills during gameplay

## 526. game_detail_spider_man_2 / summary_th

- Selector: `game_detail_spider_man_2:summary_th`
- Category: `games`
- Title: Marvel's Spider-Man 2
- Source hash: `7d8f588b647fa68fb9025cf9cc09ad3ce018e8895a7f646c7646e3cc44057afe`

**Thai source**

Marvel's Spider-Man 2 คือเกมแอ็กชันผจญภัยที่ผู้เล่นรับบท Spider-Man ต่อสู้กับศัตรูและสำรวจเมือง

**English draft**

Marvel's Spider-Man 2 is an action-adventure game where players take on the role of Spider-Man, fighting enemies and exploring the city.

## 527. game_detail_super_mario_odyssey / genre

- Selector: `game_detail_super_mario_odyssey:genre`
- Category: `games`
- Title: Super Mario Odyssey
- Source hash: `3d9f2c92c563b76f9f1cdfbe153944a99e922faae94bfb80f4bacdbb91a708cf`

**Thai source**

เกม Platformer 3D

**English draft**

Genre: Platformer 3D

## 528. game_detail_super_mario_odyssey / how_to_play_th

- Selector: `game_detail_super_mario_odyssey:how_to_play_th`
- Category: `games`
- Title: Super Mario Odyssey
- Source hash: `8006a00e341cb1d60feb7026953e4f882052229cbe2b46782b3e297365dac64a`

**Thai source**

วิ่ง กระโดด ใช้หมวก Cappy จับ/ควบคุมบางสิ่ง และสำรวจฉากเพื่อเก็บเป้าหมาย

**English draft**

Run, jump, use the Cappy helmet to grab or control objects and explore the environment to collect objectives

## 529. game_detail_super_mario_odyssey / summary_th

- Selector: `game_detail_super_mario_odyssey:summary_th`
- Category: `games`
- Title: Super Mario Odyssey
- Source hash: `0920028fd4496518eb6b66b9acfd1ee63011d74ef57144edb3d8735529944338`

**Thai source**

Super Mario Odyssey คือเกมผจญภัย 3D ที่ Mario สำรวจโลกต่าง ๆ และเก็บ Power Moon

**English draft**

Super Mario Odyssey is a 3D adventure game where Mario explores different worlds and collects Power Moons.

## 530. game_detail_super_smash_bros / genre

- Selector: `game_detail_super_smash_bros:genre`
- Category: `games`
- Title: Super Smash Bros Ultimate
- Source hash: `2a6dc4fcc938a22347b16f187bf3d49fdb2985133d4007556af676814c7933a5`

**Thai source**

เกมต่อสู้แบบ Platform Fighter

**English draft**

Platform fighter

## 531. game_detail_super_smash_bros / how_to_play_th

- Selector: `game_detail_super_smash_bros:how_to_play_th`
- Category: `games`
- Title: Super Smash Bros Ultimate
- Source hash: `864bb7fedd339306bf55163937160d5b262dd9109a48c08408a05d906c0f5cbd`

**Thai source**

เลือกตัวละคร ใช้ท่าโจมตี หลบ กระโดด และพยายามทำให้คู่แข่งกระเด็นออกนอกสนาม

**English draft**

Select a character, use attacks, dodge, jump, and try to knock your opponent out of the arena

## 532. game_detail_super_smash_bros / summary_th

- Selector: `game_detail_super_smash_bros:summary_th`
- Category: `games`
- Title: Super Smash Bros Ultimate
- Source hash: `31281ce8207e8a117b58bf9c5bb30c8175867f9780329ff510a00746ae3c3ea4`

**Thai source**

Super Smash Bros Ultimate คือเกมต่อสู้ที่ใช้ตัวละครจากหลายเกม ผลักคู่ต่อสู้ออกจากฉากเพื่อทำคะแนน

**English draft**

Super Smash Bros Ultimate is a fighting game featuring characters from multiple games, scoring by knocking opponents off the stage.

## 533. game_detail_switch_sports / genre

- Selector: `game_detail_switch_sports:genre`
- Category: `games`
- Title: Nintendo Switch Sports
- Source hash: `987ef1a892ce6b1a1dee57c424f0d82e38e207060c1cc9f6dd3c996548fe3543`

**Thai source**

เกมกีฬา Motion Control

**English draft**

Sports game

## 534. game_detail_switch_sports / how_to_play_th

- Selector: `game_detail_switch_sports:how_to_play_th`
- Category: `games`
- Title: Nintendo Switch Sports
- Source hash: `30377064a20c1a6a46bb5b8b5c1a6524de78c893be1f874ed69951047d1f3e6a`

**Thai source**

ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม

**English draft**

Hold the Joy-Con and move it according to the selected sport, such as swing, throw, or gesture motions in the game.

## 535. game_detail_switch_sports / summary_th

- Selector: `game_detail_switch_sports:summary_th`
- Category: `games`
- Title: Nintendo Switch Sports
- Source hash: `415e98ddb4f75abad9467a42d5870ae4bf61f762c8efe3d47fc854dac68e04d2`

**Thai source**

Nintendo Switch Sports คือเกมกีฬาที่ใช้การขยับ Joy-Con จำลองการเล่นกีฬาหลายประเภท

**English draft**

Nintendo Switch Sports is a sports game that uses Joy-Con motion controls to simulate playing various sports.

## 536. game_detail_tekken_8 / genre

- Selector: `game_detail_tekken_8:genre`
- Category: `games`
- Title: TEKKEN 8
- Source hash: `e2751baf8a82a861190ebbd45343f362b9d7a532ca72285a02dfad82c0b552c6`

**Thai source**

เกมต่อสู้ 1v1

**English draft**

Fighting game 1v1

## 537. game_detail_tekken_8 / how_to_play_th

- Selector: `game_detail_tekken_8:how_to_play_th`
- Category: `games`
- Title: TEKKEN 8
- Source hash: `57fe7f479501471316f3869a33e284761622a2b36f634d9d5faebda1683b4f55`

**Thai source**

เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน

**English draft**

Play in rounds. Choose a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero before them.

## 538. game_detail_tekken_8 / summary_th

- Selector: `game_detail_tekken_8:summary_th`
- Category: `games`
- Title: TEKKEN 8
- Source hash: `be447495c14fdd73d442b33b466bdb92943e4828f2377037edcf468484c8e4b5`

**Thai source**

TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง

**English draft**

TEKKEN 8 is a one-on-one fighting game where players select characters and win by using combos, blocking, and counterattacks against their opponent.

## 539. game_detail_the_last_of_us / genre

- Selector: `game_detail_the_last_of_us:genre`
- Category: `games`
- Title: The Last of Us Part I / Part II
- Source hash: `32245230b489b1154c26c037e8cc8df0506be4beed8d0f9a2abb289635170105`

**Thai source**

เกม Action-Adventure / Survival

**English draft**

Action-Adventure / Survival

## 540. game_detail_the_last_of_us / how_to_play_th

- Selector: `game_detail_the_last_of_us:how_to_play_th`
- Category: `games`
- Title: The Last of Us Part I / Part II
- Source hash: `0e5004f8480934b658edbf30d1317e672e0513c27ef45b435f7be2bf7d902dd5`

**Thai source**

สำรวจ ฉวยโอกาสลอบเร้น ต่อสู้ เก็บทรัพยากร และดำเนินเรื่องผ่านภารกิจต่าง ๆ

**English draft**

Explore, seize opportunities stealthily, fight, gather resources, and progress through various missions

## 541. game_detail_the_last_of_us / summary_th

- Selector: `game_detail_the_last_of_us:summary_th`
- Category: `games`
- Title: The Last of Us Part I / Part II
- Source hash: `8cb803e24334672e56bcb5ec6dfec70dcaec8f3e9ed1e5b0b442b51a1267e46d`

**Thai source**

The Last of Us คือเกมผจญภัยเอาตัวรอดที่เน้นเนื้อเรื่อง การลอบเร้น และการจัดการทรัพยากร

**English draft**

The Last of Us is an adventure survival game that emphasizes storytelling, stealth, and resource management.

## 542. game_detail_uncharted / genre

- Selector: `game_detail_uncharted:genre`
- Category: `games`
- Title: Uncharted: Legacy of Thieves Collection
- Source hash: `411ce98360c7a9a887dd0c7ffa061671cca58fb87424cb7371c667cdb9a11179`

**Thai source**

เกม Action-Adventure

**English draft**

Action-Adventure

## 543. game_detail_uncharted / how_to_play_th

- Selector: `game_detail_uncharted:how_to_play_th`
- Category: `games`
- Title: Uncharted: Legacy of Thieves Collection
- Source hash: `5784b14e0b6ecdc197a09b101f9b7f14b3e975f6a86143a810505c0a3a5dbbe1`

**Thai source**

สำรวจฉาก ปีนป่าย แก้ปริศนา ยิงต่อสู้ และดำเนินเรื่องผ่านภารกิจ

**English draft**

Explore scenes, climb, solve puzzles, fight, and progress through missions

## 544. game_detail_uncharted / summary_th

- Selector: `game_detail_uncharted:summary_th`
- Category: `games`
- Title: Uncharted: Legacy of Thieves Collection
- Source hash: `f9fcc7beee28d16e3b5b8b24d445ee5dbf5340db3687c17cec7074db5f8f503b`

**Thai source**

Uncharted คือเกมผจญภัยแนวล่าสมบัติที่เน้นปีนป่าย สำรวจ แก้ปริศนา และฉากแอ็กชัน

**English draft**

Uncharted is an adventure game focused on climbing, exploring, puzzle-solving, and action scenes.

## 545. game_detail_valorant / genre

- Selector: `game_detail_valorant:genre`
- Category: `games`
- Title: VALORANT
- Source hash: `8ed1b97d46685265d76bce4b9bafa500fc1fda1bf6b8a3df0bf86a1a6961489b`

**Thai source**

เกมยิง Tactical FPS แบบทีม 5v5

**English draft**

Tactical 5v5 team-based FPS

## 546. game_detail_valorant / how_to_play_th

- Selector: `game_detail_valorant:how_to_play_th`
- Category: `games`
- Title: VALORANT
- Source hash: `81cd6fd64da2b857d0d3bf7d6428d0c331436e1fd2375432c129c0620dabb228`

**Thai source**

ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม

**English draft**

The offensive team must place a spike, while the defensive team must defend their area or recover a spike. Gameplay emphasizes aiming, communication, skill usage, and teamwork.

## 547. game_detail_valorant / summary_th

- Selector: `game_detail_valorant:summary_th`
- Category: `games`
- Title: VALORANT
- Source hash: `3896b3af649ec60a37923e84c4a515edc651d5fee924317a0b30eded765c02f7`

**Thai source**

VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ

**English draft**

VALORANT is a tactical shooter game where players select agents with unique skills and play as either attackers or defenders in each round.

## 548. game_detail_warzone / genre

- Selector: `game_detail_warzone:genre`
- Category: `games`
- Title: Call of Duty: Warzone
- Source hash: `b3a65788846f2e97e771ff8cfa351806a981d53596dd5045405ea11aa709941a`

**Thai source**

เกมยิง Battle Royale

**English draft**

Battle Royale shooter

## 549. game_detail_warzone / how_to_play_th

- Selector: `game_detail_warzone:how_to_play_th`
- Category: `games`
- Title: Call of Duty: Warzone
- Source hash: `91bf81366c4eaed2d181cdd6c6764fc85b828f8cc6c0db97fdb409c7a06f1021`

**Thai source**

ลงพื้นที่ หาอาวุธ ใช้ loadout/อุปกรณ์ช่วยทีม เคลื่อนตามวง และพยายามอยู่รอดจนจบเกม

**English draft**

Go to the area, find weapons, use loadout/team gear, move around the ring, and try to survive until the end of the game

## 550. game_detail_warzone / summary_th

- Selector: `game_detail_warzone:summary_th`
- Category: `games`
- Title: Call of Duty: Warzone
- Source hash: `4b42e284665b0a1539fdd08e9039bdb12ff0f827a2c46efe2f8b6809294f2902`

**Thai source**

Call of Duty: Warzone คือเกมยิงแนว Battle Royale ที่เน้นการยิงรวดเร็ว การเก็บอุปกรณ์ และการเอาตัวรอดในแผนที่ขนาดใหญ่

**English draft**

Call of Duty: Warzone is a fast-paced Battle Royale shooter game that emphasizes quick shooting, equipment gathering, and surviving on a large map.

## 551. game_detail_zelda_breath_of_the_wild / genre

- Selector: `game_detail_zelda_breath_of_the_wild:genre`
- Category: `games`
- Title: The Legend of Zelda: Breath of the Wild
- Source hash: `5e9dd06659e9b2f53370f50ff386e2aaa4b25a6f86e2d856e2b9d0c00f8dffca`

**Thai source**

เกม Open-world Adventure

**English draft**

Open-world Adventure

## 552. game_detail_zelda_breath_of_the_wild / how_to_play_th

- Selector: `game_detail_zelda_breath_of_the_wild:how_to_play_th`
- Category: `games`
- Title: The Legend of Zelda: Breath of the Wild
- Source hash: `fd0ff40f0cd587869c6be6692fc8ab51c3725123b1bb47390925fad7100d6ca7`

**Thai source**

สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก

**English draft**

Explore the map, collect weapons/food, clear shrines, fight enemies, and choose your own adventure path

## 553. game_detail_zelda_breath_of_the_wild / summary_th

- Selector: `game_detail_zelda_breath_of_the_wild:summary_th`
- Category: `games`
- Title: The Legend of Zelda: Breath of the Wild
- Source hash: `58df8ab1a8405a8b7c7f4bd733c42a97d45d26886d80f0413c17fa9a52f5431a`

**Thai source**

The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ

**English draft**

The Legend of Zelda: Breath of the Wild is an open-world adventure game that lets players explore, fight, solve puzzles, and experiment with different ways to navigate through various situations.

## 554. member_0629f0033d3d9b24 / name

- Selector: `member_0629f0033d3d9b24:name`
- Category: `members`
- Title: นายธนชาติ เอ่งฉ้วน
- Source hash: `b71f660698440a5ff01d4dd3e29221785e13b22716ee19612fa9190c8c71e6c6`

**Thai source**

นายธนชาติ เอ่งฉ้วน

**English draft**

Thanatip Engchuan

## 555. member_0629f0033d3d9b24 / role

- Selector: `member_0629f0033d3d9b24:role`
- Category: `members`
- Title: นายธนชาติ เอ่งฉ้วน
- Source hash: `7f30d78300670ba3841f3d6cbf4b30329f2ac1e486a604de3d5fa87f28bf94fd`

**Thai source**

ประชาสัมพันธ์

**English draft**

PR

## 556. member_17d23bd43ffdcfb0 / affiliation

- Selector: `member_17d23bd43ffdcfb0:affiliation`
- Category: `members`
- Title: นายชนะชัย สิริพันธ์วราภรณ์
- Source hash: `f54026b2c438d5603559b05b389e75dd9be67d90adbb2d6cc6995c7523c63949`

**Thai source**

PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

PSU Esports Studio - Phuket Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 557. member_17d23bd43ffdcfb0 / name

- Selector: `member_17d23bd43ffdcfb0:name`
- Category: `members`
- Title: นายชนะชัย สิริพันธ์วราภรณ์
- Source hash: `e19f31cef0eea45843e45665997b508fa66cb68de2fefe2d2cbb4d819ab7260c`

**Thai source**

นายชนะชัย สิริพันธ์วราภรณ์

**English draft**

Mr. Kanat Chai Siripanthisaraworn

## 558. member_17d23bd43ffdcfb0 / role

- Selector: `member_17d23bd43ffdcfb0:role`
- Category: `members`
- Title: นายชนะชัย สิริพันธ์วราภรณ์
- Source hash: `8bdc0e266e7457dd13ededc4becdc05a655d72fb06bf5564372bc2db600a5a75`

**Thai source**

ผู้จัดการ

**English draft**

Manager

## 559. member_18a751d710b9b30c / name

- Selector: `member_18a751d710b9b30c:name`
- Category: `members`
- Title: นางสาวกมลวรรณ นวลสาย
- Source hash: `f3b8d0c9b26ea698573ff3c3fab7c8250eba0b5e3716298474d9e92512f43691`

**Thai source**

นางสาวกมลวรรณ นวลสาย

**English draft**

Miss Kamolwan Nuansai

## 560. member_18a751d710b9b30c / role

- Selector: `member_18a751d710b9b30c:role`
- Category: `members`
- Title: นางสาวกมลวรรณ นวลสาย
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 561. member_1d37816f5d904797 / name

- Selector: `member_1d37816f5d904797:name`
- Category: `members`
- Title: นางสาวชญาภา จันทร์เอิบ
- Source hash: `07a76fa98e207557c9350cb02e732b3ea0af6306dfd740d2bb214e6a06e2104e`

**Thai source**

นางสาวชญาภา จันทร์เอิบ

**English draft**

Ms. Chayapa Janneeb

## 562. member_1d37816f5d904797 / role

- Selector: `member_1d37816f5d904797:role`
- Category: `members`
- Title: นางสาวชญาภา จันทร์เอิบ
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 563. member_1d884f11f3890dea / name

- Selector: `member_1d884f11f3890dea:name`
- Category: `members`
- Title: นายษุภากรณ์ จิราจินดากุล
- Source hash: `382b109f4c6ce4588eedf07b765fa1323d57202432ae227707533782ffcdc1be`

**Thai source**

นายษุภากรณ์ จิราจินดากุล

**English draft**

Suthapakorn Jirajindakul

## 564. member_1d884f11f3890dea / role

- Selector: `member_1d884f11f3890dea:role`
- Category: `members`
- Title: นายษุภากรณ์ จิราจินดากุล
- Source hash: `1bf469285fc6074558e419a3c19158b64e9cd713eb7b4dc88332c61e336e2fda`

**Thai source**

ประธาน

**English draft**

President

## 565. member_2035485e1198bd6d / affiliation

- Selector: `member_2035485e1198bd6d:affiliation`
- Category: `members`
- Title: นายณัฐวัฒน์ นิธิคุณานนต์
- Source hash: `36601e699a96609973b4d02ae25aa755ba489ee081d3b2e9a3f041315dc31512`

**Thai source**

วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 566. member_2035485e1198bd6d / name

- Selector: `member_2035485e1198bd6d:name`
- Category: `members`
- Title: นายณัฐวัฒน์ นิธิคุณานนต์
- Source hash: `efb9a3ecd11372e8ca01270b7db5a867829311339ccdffb2213a7bf31b8a661f`

**Thai source**

นายณัฐวัฒน์ นิธิคุณานนต์

**English draft**

Nattawat Nitikunn

## 567. member_2035485e1198bd6d / role

- Selector: `member_2035485e1198bd6d:role`
- Category: `members`
- Title: นายณัฐวัฒน์ นิธิคุณานนต์
- Source hash: `4d2255b60a39490b730a4ed595fbc5a5f05e6dba8147367a6fd30a9d60cae431`

**Thai source**

นักวิชาการคอมพิวเตอร์

**English draft**

Computer scientist

## 568. member_453ecaf47e840388 / affiliation

- Selector: `member_453ecaf47e840388:affiliation`
- Category: `members`
- Title: รศ.ดร.อซีส นันทอมรพงศ์
- Source hash: `36601e699a96609973b4d02ae25aa755ba489ee081d3b2e9a3f041315dc31512`

**Thai source**

วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 569. member_453ecaf47e840388 / name

- Selector: `member_453ecaf47e840388:name`
- Category: `members`
- Title: รศ.ดร.อซีส นันทอมรพงศ์
- Source hash: `e4fc8fd8eeb21fe8a502b6197e215515b42945015e0f827461e3d7e2d2369431`

**Thai source**

รศ.ดร.อซีส นันทอมรพงศ์

**English draft**

Dr. Aces Nanthamrong

## 570. member_453ecaf47e840388 / role

- Selector: `member_453ecaf47e840388:role`
- Category: `members`
- Title: รศ.ดร.อซีส นันทอมรพงศ์
- Source hash: `6082e04b385ecac51f2ad6981230cba3b10bfd1830bdeb7e32ed65b0809c4b2d`

**Thai source**

คณบดี

**English draft**

Dean

## 571. member_4e005eeca4b538a1 / affiliation

- Selector: `member_4e005eeca4b538a1:affiliation`
- Category: `members`
- Title: รศ.ดร.พันธ์ ทองชุมนุม
- Source hash: `88f443e0b82b4d3c0d12d094ac50ea51a503129f59ca366f8cb81bbebfbc9e0c`

**Thai source**

มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Chulalongkorn University Phuket Campus

## 572. member_4e005eeca4b538a1 / name

- Selector: `member_4e005eeca4b538a1:name`
- Category: `members`
- Title: รศ.ดร.พันธ์ ทองชุมนุม
- Source hash: `2e0c8e36d4fb5da25ad0e27a4bcc4f7e8471d4b315bad4a51f8e13c358b02ba6`

**Thai source**

รศ.ดร.พันธ์ ทองชุมนุม

**English draft**

Dr. Pong Tongchumnuam

## 573. member_4e005eeca4b538a1 / role

- Selector: `member_4e005eeca4b538a1:role`
- Category: `members`
- Title: รศ.ดร.พันธ์ ทองชุมนุม
- Source hash: `568c97c1db3dc0c84c06bf3a384a786ba77349aa50aa39a487924c18b1f280ad`

**Thai source**

รองอธิการบดี

**English draft**

Deputy Vice-Chancellor

## 574. member_68e4915433f294b7 / affiliation

- Selector: `member_68e4915433f294b7:affiliation`
- Category: `members`
- Title: นายภาสวุฒิ ชูติประชากิจ
- Source hash: `15f839a009f2157fa646750f66097c7889408ac95b3c8184053a7657b780eb7c`

**Thai source**

วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง

**English draft**

Department of Information and Communication Systems Engineering, King Chulalongkorn Memorial Institute of Technology

## 575. member_68e4915433f294b7 / name

- Selector: `member_68e4915433f294b7:name`
- Category: `members`
- Title: นายภาสวุฒิ ชูติประชากิจ
- Source hash: `49595b0af070ba75ad679213fb9829a62c7b22f6f05c5a04d98eeda7457f5529`

**Thai source**

นายภาสวุฒิ ชูติประชากิจ

**English draft**

Mr. Phaswut Chootiprakashik

## 576. member_68e4915433f294b7 / role

- Selector: `member_68e4915433f294b7:role`
- Category: `members`
- Title: นายภาสวุฒิ ชูติประชากิจ
- Source hash: `615e4733a4a949bf2c92391d0386e764e35148ac5e7483c153e2edeb4a8ce8fa`

**Thai source**

นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer

**English draft**

Student intern for the Super AI SS6 project, position: AI Chat Bot Developer

## 577. member_704fe601a50d54d0 / name

- Selector: `member_704fe601a50d54d0:name`
- Category: `members`
- Title: นางสาวอาทิตยา แดงประดับ
- Source hash: `0487d014f7f0aaad796a96d2cde34bb43c73ae367a867cbc1cee64c1d4d34454`

**Thai source**

นางสาวอาทิตยา แดงประดับ

**English draft**

Miss Atiya Danapradab

## 578. member_704fe601a50d54d0 / role

- Selector: `member_704fe601a50d54d0:role`
- Category: `members`
- Title: นางสาวอาทิตยา แดงประดับ
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 579. member_832e24bbcd11737e / affiliation

- Selector: `member_832e24bbcd11737e:affiliation`
- Category: `members`
- Title: ผศ.ดร.ณัฐพงศ์ ทองเทพ
- Source hash: `88f443e0b82b4d3c0d12d094ac50ea51a503129f59ca366f8cb81bbebfbc9e0c`

**Thai source**

มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Chulalongkorn University Phuket Campus

## 580. member_832e24bbcd11737e / name

- Selector: `member_832e24bbcd11737e:name`
- Category: `members`
- Title: ผศ.ดร.ณัฐพงศ์ ทองเทพ
- Source hash: `d692f271b85f21a6c9d74107a44d69681b5642dadc79f1168df4f6c901885ebb`

**Thai source**

ผศ.ดร.ณัฐพงศ์ ทองเทพ

**English draft**

Dr. Nattapong Tongthep

## 581. member_832e24bbcd11737e / role

- Selector: `member_832e24bbcd11737e:role`
- Category: `members`
- Title: ผศ.ดร.ณัฐพงศ์ ทองเทพ
- Source hash: `e97b5809d355c28d6387f52238f2c00495e51763af6dd15a0c5202b0b60c49ec`

**Thai source**

ผู้ช่วยอธิการบดีฝ่ายวิชาการ

**English draft**

Deputy Vice-Chancellor (Academic)

## 582. member_930bf12e4f38f6ff / affiliation

- Selector: `member_930bf12e4f38f6ff:affiliation`
- Category: `members`
- Title: นายพฤทธิ์ เกษตรสมบูรณ์
- Source hash: `36601e699a96609973b4d02ae25aa755ba489ee081d3b2e9a3f041315dc31512`

**Thai source**

วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 583. member_930bf12e4f38f6ff / name

- Selector: `member_930bf12e4f38f6ff:name`
- Category: `members`
- Title: นายพฤทธิ์ เกษตรสมบูรณ์
- Source hash: `31abf1546f2cb929ec01a13f51f5189fa816b24239927f5761adfa3b18fc2926`

**Thai source**

นายพฤทธิ์ เกษตรสมบูรณ์

**English draft**

Mr. Phurit Kesatsampan

## 584. member_930bf12e4f38f6ff / role

- Selector: `member_930bf12e4f38f6ff:role`
- Category: `members`
- Title: นายพฤทธิ์ เกษตรสมบูรณ์
- Source hash: `4d2255b60a39490b730a4ed595fbc5a5f05e6dba8147367a6fd30a9d60cae431`

**Thai source**

นักวิชาการคอมพิวเตอร์

**English draft**

Computer scientist

## 585. member_9e9cb3b178e5d76c / name

- Selector: `member_9e9cb3b178e5d76c:name`
- Category: `members`
- Title: นางสาวณัฐธิดา คำทะเนตร์
- Source hash: `a1d5adc1fca1d553fc6b9fed28e5d587bc9026e988e9422725d2443a08e2ad41`

**Thai source**

นางสาวณัฐธิดา คำทะเนตร์

**English draft**

Ms. Nattida Kamthaneer

## 586. member_9e9cb3b178e5d76c / role

- Selector: `member_9e9cb3b178e5d76c:role`
- Category: `members`
- Title: นางสาวณัฐธิดา คำทะเนตร์
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 587. member_a19d2197ce8e1a38 / name

- Selector: `member_a19d2197ce8e1a38:name`
- Category: `members`
- Title: นายณัฐพนธ์ อินทรสังขนาวิน
- Source hash: `125d59475155e07f69a30633dfa132a4c8b02df27b481579286a2e854dd1cd58`

**Thai source**

นายณัฐพนธ์ อินทรสังขนาวิน

**English draft**

Mr. Nattaphon Inturasangkawin

## 588. member_a19d2197ce8e1a38 / role

- Selector: `member_a19d2197ce8e1a38:role`
- Category: `members`
- Title: นายณัฐพนธ์ อินทรสังขนาวิน
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 589. member_a2e050f57fcf6d7a / affiliation

- Selector: `member_a2e050f57fcf6d7a:affiliation`
- Category: `members`
- Title: Mr. Amine Abidellaoui
- Source hash: `c9bc740718d6f81316cc8e5978416d4a3c9637e4524f60800a9e5875054e9c9a`

**Thai source**

High School Bristol Cannes, France

**English draft**

High School Bristol Cannes, France

## 590. member_a2e050f57fcf6d7a / name

- Selector: `member_a2e050f57fcf6d7a:name`
- Category: `members`
- Title: Mr. Amine Abidellaoui
- Source hash: `8f26e977e822f55680bd7b9c6b7162512d352513d6d4bd9fcedba6360ce535d7`

**Thai source**

Mr. Amine Abidellaoui

**English draft**

Mr. Amine Abidellaoui

## 591. member_a2e050f57fcf6d7a / role

- Selector: `member_a2e050f57fcf6d7a:role`
- Category: `members`
- Title: Mr. Amine Abidellaoui
- Source hash: `43ca7b31266899eb755500766ad5015eda9254a4ea79ba5dcc82aacfd54f2df0`

**Thai source**

Internship Student

**English draft**

Internship Student

## 592. member_a69fd942fc2537c2 / name

- Selector: `member_a69fd942fc2537c2:name`
- Category: `members`
- Title: นางสาวสุภาสินี ธนภพ
- Source hash: `80593536c56b0d0d60f1ab9cc5b58ac61f0934a418efaa59897fca100ee21cb7`

**Thai source**

นางสาวสุภาสินี ธนภพ

**English draft**

Ms. Supasinee Thanapap

## 593. member_a69fd942fc2537c2 / role

- Selector: `member_a69fd942fc2537c2:role`
- Category: `members`
- Title: นางสาวสุภาสินี ธนภพ
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 594. member_acb83e6fddde5334 / name

- Selector: `member_acb83e6fddde5334:name`
- Category: `members`
- Title: นายอรรถนนท์ สุขแก้ว
- Source hash: `a2f75f04f9b7fe3baea3fcf25262ab57fdf1133ce8b68d826c63275f61f3822b`

**Thai source**

นายอรรถนนท์ สุขแก้ว

**English draft**

Mr. Arthorn Sukkawat

## 595. member_acb83e6fddde5334 / role

- Selector: `member_acb83e6fddde5334:role`
- Category: `members`
- Title: นายอรรถนนท์ สุขแก้ว
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 596. member_b71d33c7b6468ebc / affiliation

- Selector: `member_b71d33c7b6468ebc:affiliation`
- Category: `members`
- Title: นายสุพศิน อะนะฝรั่ง
- Source hash: `36601e699a96609973b4d02ae25aa755ba489ee081d3b2e9a3f041315dc31512`

**Thai source**

วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 597. member_b71d33c7b6468ebc / name

- Selector: `member_b71d33c7b6468ebc:name`
- Category: `members`
- Title: นายสุพศิน อะนะฝรั่ง
- Source hash: `7bb01e7d31891e60374bca1c467f1514c17bb2b5407f626bde932802f17d1db1`

**Thai source**

นายสุพศิน อะนะฝรั่ง

**English draft**

Mr. Supasit Anavaran

## 598. member_b71d33c7b6468ebc / role

- Selector: `member_b71d33c7b6468ebc:role`
- Category: `members`
- Title: นายสุพศิน อะนะฝรั่ง
- Source hash: `9e4573e8916c876b9affa07f2019c5de7eb62f8aa7733f516447571d373b4759`

**Thai source**

นักศึกษาสหกิจ Web & AI Developer

**English draft**

Intern Student Web & AI Developer

## 599. member_b898853273feb841 / name

- Selector: `member_b898853273feb841:name`
- Category: `members`
- Title: นายอภิวิชญ์ เลิศกมลรักษ์
- Source hash: `f2af5b5d681eb50564cdda9d893fc1a72480845934ef385cb94fd34c86a764f6`

**Thai source**

นายอภิวิชญ์ เลิศกมลรักษ์

**English draft**

Mr. Apivichai Leekamolrak

## 600. member_b898853273feb841 / role

- Selector: `member_b898853273feb841:role`
- Category: `members`
- Title: นายอภิวิชญ์ เลิศกมลรักษ์
- Source hash: `f6e974c952dccea13ae5ecb7fe5d04c3c8de7ee793a0eb10bcc4bb17d6dda6de`

**Thai source**

กรรมการ

**English draft**

Chairman

## 601. member_bf43feb569776b8b / name

- Selector: `member_bf43feb569776b8b:name`
- Category: `members`
- Title: นายนพัทธ์ ฝอยทอง
- Source hash: `b32f0714cb791d111bc474462d40e6dff62a1f94558b444a2399ce6ff3537625`

**Thai source**

นายนพัทธ์ ฝอยทอง

**English draft**

Mr. Napath Poyton

## 602. member_bf43feb569776b8b / role

- Selector: `member_bf43feb569776b8b:role`
- Category: `members`
- Title: นายนพัทธ์ ฝอยทอง
- Source hash: `52fe29b1e8c31077484c716ddd03180347d08114d8de45372611a394c9c3f480`

**Thai source**

รองประธาน

**English draft**

Deputy Chair

## 603. member_c0944fdade08a06c / affiliation

- Selector: `member_c0944fdade08a06c:affiliation`
- Category: `members`
- Title: นายณภัทร เชื้อเหล่าวานิช
- Source hash: `36601e699a96609973b4d02ae25aa755ba489ee081d3b2e9a3f041315dc31512`

**Thai source**

วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต

**English draft**

Faculty of Computer, King Chulalongkorn Memorial University, Phuket Campus

## 604. member_c0944fdade08a06c / name

- Selector: `member_c0944fdade08a06c:name`
- Category: `members`
- Title: นายณภัทร เชื้อเหล่าวานิช
- Source hash: `18eef74a4c95578901f06b220bab5686929b1dc0b6fe39f1b92d754a1581114a`

**Thai source**

นายณภัทร เชื้อเหล่าวานิช

**English draft**

Mr. Naphat Chuea Lekwanich

## 605. member_c0944fdade08a06c / role

- Selector: `member_c0944fdade08a06c:role`
- Category: `members`
- Title: นายณภัทร เชื้อเหล่าวานิช
- Source hash: `c2e7af9f9faf38f9b3f0c4e577aa52f7a899d26b20c7e8abb9798b78d3fc1138`

**Thai source**

นักศึกษาสหกิจ Game and 3D Developer

**English draft**

Intern Student Game and 3D Developer

## 606. member_ce4590ddc09c0f4e / affiliation

- Selector: `member_ce4590ddc09c0f4e:affiliation`
- Category: `members`
- Title: ผศ.ดร.นิวัติ แก้วประดับ
- Source hash: `fc78991ac6a1254b836090d4af791054e0357703d3d568f82f6c933f876a6208`

**Thai source**

มหาวิทยาลัยสงขลานครินทร์

**English draft**

Chulalongkorn University

## 607. member_ce4590ddc09c0f4e / name

- Selector: `member_ce4590ddc09c0f4e:name`
- Category: `members`
- Title: ผศ.ดร.นิวัติ แก้วประดับ
- Source hash: `8081d09f9b08cc545c3e1f01cfca954862211ed84376ab146b8e9264c108b5b9`

**Thai source**

ผศ.ดร.นิวัติ แก้วประดับ

**English draft**

Prof. Dr. Nuwat Kaewprapub

## 608. member_ce4590ddc09c0f4e / role

- Selector: `member_ce4590ddc09c0f4e:role`
- Category: `members`
- Title: ผศ.ดร.นิวัติ แก้วประดับ
- Source hash: `96b556c6f5fdd2760379090cc6e182de530e10bd9afbe56e4ee63e84d9c46c1d`

**Thai source**

อธิการบดี

**English draft**

President

## 609. member_d7fc7da21ef72803 / affiliation

- Selector: `member_d7fc7da21ef72803:affiliation`
- Category: `members`
- Title: Mr. Yanis Igoudjil
- Source hash: `3480bc45be4c275aac8e15d23fc204b27743eb82ebf0390afec8e82e436402ec`

**Thai source**

Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France

**English draft**

Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France

## 610. member_d7fc7da21ef72803 / name

- Selector: `member_d7fc7da21ef72803:name`
- Category: `members`
- Title: Mr. Yanis Igoudjil
- Source hash: `5f267fb7556e83328af9caa5e5d66b8ddd87264a3f81fc6a33b6f5dc11e31964`

**Thai source**

Mr. Yanis Igoudjil

**English draft**

Mr. Yanis Igoudjil

## 611. member_d7fc7da21ef72803 / role

- Selector: `member_d7fc7da21ef72803:role`
- Category: `members`
- Title: Mr. Yanis Igoudjil
- Source hash: `43ca7b31266899eb755500766ad5015eda9254a4ea79ba5dcc82aacfd54f2df0`

**Thai source**

Internship Student

**English draft**

Internship Student

## 612. member_df4264b9c7e37a23 / name

- Selector: `member_df4264b9c7e37a23:name`
- Category: `members`
- Title: นายภูจิตร จิรวิริยาภรณ์
- Source hash: `c12dba87c1fc42c803cdbd9938ca0b6d188d1f4b910dbecb1babfc48169bb5b8`

**Thai source**

นายภูจิตร จิรวิริยาภรณ์

**English draft**

Mr. Phujitr Jiraviriyanont

## 613. member_df4264b9c7e37a23 / role

- Selector: `member_df4264b9c7e37a23:role`
- Category: `members`
- Title: นายภูจิตร จิรวิริยาภรณ์
- Source hash: `f1effd6d98e0580dfc76e03ea45eaf1f9583cf4abd7e389dbb3c47a893820a58`

**Thai source**

เหรัญญิก

**English draft**

Priest

## 614. member_f90051b3c68e16b4 / name

- Selector: `member_f90051b3c68e16b4:name`
- Category: `members`
- Title: นายปัณณวิชญ์ หนูเรือง
- Source hash: `668da71892dd20bf4e714245553ddc36c377db7daba2254b6abbc9d3f117648b`

**Thai source**

นายปัณณวิชญ์ หนูเรือง

**English draft**

Mr. Panawan Joonreung

## 615. member_f90051b3c68e16b4 / role

- Selector: `member_f90051b3c68e16b4:role`
- Category: `members`
- Title: นายปัณณวิชญ์ หนูเรือง
- Source hash: `8be3aad36b1b3ffc9cca5d2f8613497dd8d1aa9762a1c03ea209ad34b50004de`

**Thai source**

เลขานุการ

**English draft**

Assistant
