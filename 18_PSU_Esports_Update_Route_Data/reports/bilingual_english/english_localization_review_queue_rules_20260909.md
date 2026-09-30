# English Localization Review Queue

> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.

- Draft input: `data\locales\en\localization_review_drafts_machine_20260909_verified.jsonl`
- Filter: `rules`
- Review items: **18**

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

## 1. curated_rule_belongings / text

- Selector: `curated_rule_belongings:text`
- Category: `rules`
- Title: ฝากสัมภาระ
- Source hash: `4c1d6b26a29fa3c5204bc86adf8a2ac3b401782820967cda1ec0db0498b3376d`

**Thai source**

กรุณาฝากสัมภาระก่อนเข้าใช้บริการ

**English draft**

Please check in luggage before using the service

## 2. curated_rule_belongings / title

- Selector: `curated_rule_belongings:title`
- Category: `rules`
- Title: ฝากสัมภาระ
- Source hash: `29c73e1ee2a483109ff4b6683ead516c5d005a8900c0f3faefcff072de8d247f`

**Thai source**

ฝากสัมภาระ

**English draft**

Leave luggage

## 3. curated_rule_food_drinks / text

- Selector: `curated_rule_food_drinks:text`
- Category: `rules`
- Title: อาหารและเครื่องดื่ม
- Source hash: `0a298a220fb70bb88ce20e52881a3ffceb64e49c50e7e47210868cd95e49f753`

**Thai source**

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น

**English draft**

Food and drinks are permitted only in designated areas.

## 4. curated_rule_food_drinks / title

- Selector: `curated_rule_food_drinks:title`
- Category: `rules`
- Title: อาหารและเครื่องดื่ม
- Source hash: `6bdfcbbbf9b765c43f94436c765efff2431f92297886d00ed0a9465f464f49c1`

**Thai source**

อาหารและเครื่องดื่ม

**English draft**

Food and Drinks

## 5. curated_rule_lost_items / text

- Selector: `curated_rule_lost_items:text`
- Category: `rules`
- Title: ทรัพย์สินสูญหาย
- Source hash: `58ee52f11b7054b0be10c140be9a486cb3bfb0a9ae83a9903d338468d3912961`

**Thai source**

กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี

**English draft**

Please check your assets every time you use our service. If any are lost, the Center reserves the right to not be liable in any case.

## 6. curated_rule_lost_items / title

- Selector: `curated_rule_lost_items:title`
- Category: `rules`
- Title: ทรัพย์สินสูญหาย
- Source hash: `f643b4b108548d9a213ae7674dde2b45c7a9fe1dfaa15296ce5d042da8f8c602`

**Thai source**

ทรัพย์สินสูญหาย

**English draft**

Lost Property

## 7. curated_rule_move_equipment / text

- Selector: `curated_rule_move_equipment:text`
- Category: `rules`
- Title: ห้ามเคลื่อนย้ายอุปกรณ์
- Source hash: `c40c06ac49f8510e655fd6f997a05fdd4482b218f689ae5280851561c03e4ce8`

**Thai source**

ห้ามเคลื่อนย้ายอุปกรณ์หรือสิ่งของใด ๆ โดยไม่ได้รับอนุญาต

**English draft**

No equipment or items may be moved without permission.

## 8. curated_rule_move_equipment / title

- Selector: `curated_rule_move_equipment:title`
- Category: `rules`
- Title: ห้ามเคลื่อนย้ายอุปกรณ์
- Source hash: `3ad4b2d77190fe78e312f2b03f3888808f3f97ea599bfd541a69eff4c8363ad4`

**Thai source**

ห้ามเคลื่อนย้ายอุปกรณ์

**English draft**

Prohibited to move equipment

## 9. curated_rule_noise_language / text

- Selector: `curated_rule_noise_language:text`
- Category: `rules`
- Title: เสียงดังและคำพูดไม่เหมาะสม
- Source hash: `01412ae999df1b7c98ad9948dbbdb31c06efa16ce691b144d377f756ac797c66`

**Thai source**

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น

**English draft**

Please refrain from making excessive noise and avoid any disrespectful or insulting remarks toward others.

## 10. curated_rule_noise_language / title

- Selector: `curated_rule_noise_language:title`
- Category: `rules`
- Title: เสียงดังและคำพูดไม่เหมาะสม
- Source hash: `4f0afdc10ab5fce666e373e8bcddfdf3b8676ef242fe4b9c364845c999ef7307`

**Thai source**

เสียงดังและคำพูดไม่เหมาะสม

**English draft**

Loud noises and inappropriate speech

## 11. curated_rule_power_outlet / text

- Selector: `curated_rule_power_outlet:text`
- Category: `rules`
- Title: ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
- Source hash: `a5748c6825d1970eed2134cb9fd04c6006a3ec9850b7e60970175e9eeb60be01`

**Thai source**

ห้ามนำอุปกรณ์อิเล็กทรอนิกส์ส่วนตัวมาใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต

**English draft**

Prohibited to use personal electronic devices plugged into power sources without permission

## 12. curated_rule_power_outlet / title

- Selector: `curated_rule_power_outlet:title`
- Category: `rules`
- Title: ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต
- Source hash: `3fa6d4ee86e850b49e9ccbd33eabb2f2c9b4b3bc9e38bb880dcad97ba60cd5e9`

**Thai source**

ห้ามใช้ปลั๊กไฟโดยไม่ได้รับอนุญาต

**English draft**

No unauthorized use of power plugs

## 13. curated_rule_return_equipment / text

- Selector: `curated_rule_return_equipment:text`
- Category: `rules`
- Title: คืนอุปกรณ์และแผ่นเกม
- Source hash: `d40513caf4eacaa2528abd56fb98cdbc7682874390bce3993ccf26d885eec610`

**Thai source**

กรุณานำอุปกรณ์และแผ่นเกมที่เบิกไปใช้งานมาคืนหลังจากใช้งานเสร็จ

**English draft**

Please return all equipment and game discs you have borrowed after use is complete.

## 14. curated_rule_return_equipment / title

- Selector: `curated_rule_return_equipment:title`
- Category: `rules`
- Title: คืนอุปกรณ์และแผ่นเกม
- Source hash: `d6189c77a1b05f9867ad2d5bf2b5f8274354b555d7c619af76a42478242fba74`

**Thai source**

คืนอุปกรณ์และแผ่นเกม

**English draft**

Return Equipment and Game Discs

## 15. curated_rule_smoking_alcohol_drugs / text

- Selector: `curated_rule_smoking_alcohol_drugs:text`
- Category: `rules`
- Title: บุหรี่ สารเสพติด และแอลกอฮอล์
- Source hash: `fa2d40b827a223e7ccd127f7f1030d75c73441e767bb12ed8be4c606afcb43f1`

**Thai source**

ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์

**English draft**

Prohibited to smoke cigarettes, consume narcotics or drink alcohol within the facility.

## 16. curated_rule_smoking_alcohol_drugs / title

- Selector: `curated_rule_smoking_alcohol_drugs:title`
- Category: `rules`
- Title: บุหรี่ สารเสพติด และแอลกอฮอล์
- Source hash: `8e50b20cf7555f029ac9c2d55d5e2fbc90cb6c85d892f56640acadb8acd136e4`

**Thai source**

บุหรี่ สารเสพติด และแอลกอฮอล์

**English draft**

Tobacco, Drugs and Alcohol

## 17. curated_rule_weapons_gambling / text

- Selector: `curated_rule_weapons_gambling:text`
- Category: `rules`
- Title: อาวุธ ทะเลาะวิวาท การพนัน
- Source hash: `b3cb9993c541f73b09a30535159cecdd47b7a5065d297c2eb7e263fa4732c463`

**Thai source**

ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน

**English draft**

No weapons or sharp objects are allowed. No fighting or arguments are permitted, and gambling is strictly prohibited.

## 18. curated_rule_weapons_gambling / title

- Selector: `curated_rule_weapons_gambling:title`
- Category: `rules`
- Title: อาวุธ ทะเลาะวิวาท การพนัน
- Source hash: `892fa7468bd469cf81ddc23b0973dce483870b2cceeddce55c57761a0c28290e`

**Thai source**

อาวุธ ทะเลาะวิวาท การพนัน

**English draft**

Weapons Dispute Gambling
