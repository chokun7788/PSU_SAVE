# English Localization Review Queue

> Status: draft only. Nothing in this file is visible to chatbot users until an authorized reviewer explicitly approves and publishes it.

- Draft input: `data\locales\en\localization_review_drafts_machine_20260909_verified.jsonl`
- Filter: `reservation`
- Review items: **32**

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

## 1. curated_booking_no_edit / text

- Selector: `curated_booking_no_edit:text`
- Category: `reservation`
- Title: แก้ไขข้อมูลหลังจอง
- Source hash: `84b329b55d590399d829ec60765e2c68be0a68be25c17d9d5a0c734524766b45`

**Thai source**

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่อีกครั้ง พร้อมแนบสลิปการโอนเงินเดิม

**English draft**

Once booking has been confirmed, no changes can be made. If modifications are needed, the booking must be canceled via email at least one hour before usage, and then re-booked with the original transfer slip attached.

## 2. curated_booking_no_edit / title

- Selector: `curated_booking_no_edit:title`
- Category: `reservation`
- Title: แก้ไขข้อมูลหลังจอง
- Source hash: `2ba0a74b846cb38e246a907c2c6f11da6684f836c929427c576c9c3eb13bfd14`

**Thai source**

แก้ไขข้อมูลหลังจอง

**English draft**

Edit information after booking

## 3. curated_booking_non_transferable / text

- Selector: `curated_booking_non_transferable:text`
- Category: `reservation`
- Title: โอนสิทธิ์การจอง
- Source hash: `bdaf74cccd2b48afdda31a94a8185a6a14de02e8ef6a66fdf0840ad4ce0a381d`

**Thai source**

ไม่สามารถโอนสิทธิ์การจองให้กับผู้อื่นได้

**English draft**

Cannot transfer reservation rights to others

## 4. curated_booking_non_transferable / title

- Selector: `curated_booking_non_transferable:title`
- Category: `reservation`
- Title: โอนสิทธิ์การจอง
- Source hash: `485fe2525e9de0d947c632a829fb6c67aab5a302702d9ac3812b88e1cf887115`

**Thai source**

โอนสิทธิ์การจอง

**English draft**

Transfer reservation rights

## 5. curated_booking_steps / text

- Selector: `curated_booking_steps:text`
- Category: `reservation`
- Title: ขั้นตอนการจอง
- Source hash: `f157a7bea0f1f1332556122f5308f01ed5d413c8352a3b0490e0ad16ffb629e9`

**Thai source**

ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน

**English draft**

The reservation steps are: select the desired service, choose the date and time, enter user information, verify the details, pay by transferring funds to a bank account, and attach the transfer slip.

## 6. curated_booking_steps / title

- Selector: `curated_booking_steps:title`
- Category: `reservation`
- Title: ขั้นตอนการจอง
- Source hash: `0419f5421b62dbc7d60806d81a4adef6ee2c1c6df5eae0876229d8736925cbfe`

**Thai source**

ขั้นตอนการจอง

**English draft**

Steps to Reserve

## 7. curated_cancel_1_hour / text

- Selector: `curated_cancel_1_hour:text`
- Category: `reservation`
- Title: ยกเลิกการจอง
- Source hash: `6cd7295be273597ea908ad951176b8c8eadf8ed946f211f2e9452dd9599545d5`

**Thai source**

การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมง

**English draft**

Cancellation must be made at least 1 hour in advance.

## 8. curated_cancel_1_hour / title

- Selector: `curated_cancel_1_hour:title`
- Category: `reservation`
- Title: ยกเลิกการจอง
- Source hash: `3b717bf0f563d46017ca65f1cec1b76f4263cd445f00b4ba49aefcce30792410`

**Thai source**

ยกเลิกการจอง

**English draft**

Cancel reservation

## 9. curated_checkin_30_minutes / text

- Selector: `curated_checkin_30_minutes:text`
- Category: `reservation`
- Title: เช็คอินล่วงหน้า
- Source hash: `20eae4a3896fd3a78aa672ed3a1a603cab8f5e5d186368a85d70e4356e602a3b`

**Thai source**

ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ

**English draft**

Users must check in before the start time of their scheduled round. Check-in can be done up to 30 minutes prior to the scheduled round start time, and users must check in before the round begins.

## 10. curated_checkin_30_minutes / title

- Selector: `curated_checkin_30_minutes:title`
- Category: `reservation`
- Title: เช็คอินล่วงหน้า
- Source hash: `d77ad30b3441a7e9e4b969af54154a63bf15c1a5b311f30df031bd8ae912c9cc`

**Thai source**

เช็คอินล่วงหน้า

**English draft**

Pre-check-in

## 11. curated_checkin_id_required / text

- Selector: `curated_checkin_id_required:text`
- Category: `reservation`
- Title: เอกสารตอนเช็คอิน
- Source hash: `9e5a38dd8cfd66cbd52f0c7256c538cb641aa2154c1939cdb12c71b7f68562d9`

**Thai source**

เมื่อเช็คอินเข้าใช้บริการ ต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง

**English draft**

Upon check-in to use the service, you must present your student ID card, staff ID card, or national identification card.

## 12. curated_checkin_id_required / title

- Selector: `curated_checkin_id_required:title`
- Category: `reservation`
- Title: เอกสารตอนเช็คอิน
- Source hash: `7d240261f6248b133a5f6453177a9e76beed76f0cac26bd62c1a7a9735ffa9eb`

**Thai source**

เอกสารตอนเช็คอิน

**English draft**

Check-in Document

## 13. curated_checkin_late_cancel / text

- Selector: `curated_checkin_late_cancel:text`
- Category: `reservation`
- Title: ไม่เช็คอินก่อนเวลา
- Source hash: `369a1fbf1e087893166d0639e81b512347f92385e481d63cfdeaac93c9daca14`

**Thai source**

หากไม่เช็คอินก่อนถึงเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงินใด ๆ ทั้งสิ้น

**English draft**

If you do not check in before the round's start time, your reservation will be immediately canceled with no refund.

## 14. curated_checkin_late_cancel / title

- Selector: `curated_checkin_late_cancel:title`
- Category: `reservation`
- Title: ไม่เช็คอินก่อนเวลา
- Source hash: `8934a78f6a45e05fea7e077758fa5285824703e511c14c55f7e8d4d76a1fdc19`

**Thai source**

ไม่เช็คอินก่อนเวลา

**English draft**

Not check-in before time

## 15. curated_payment_10_minutes / text

- Selector: `curated_payment_10_minutes:text`
- Category: `reservation`
- Title: ชำระเงินหลังจอง
- Source hash: `521f89691c35d63e494bd122cc53e4df66f5d9764050bc007793f98f884a83a0`

**Thai source**

ผู้ใช้งานต้องชำระค่าบริการหลังจากจองเสร็จเรียบร้อยทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิก

**English draft**

Users must pay the service fee immediately after booking is completed. If payment is not made within 10 minutes, the booking will be canceled.

## 16. curated_payment_10_minutes / title

- Selector: `curated_payment_10_minutes:title`
- Category: `reservation`
- Title: ชำระเงินหลังจอง
- Source hash: `324e491bf75544971369ad577f49fc526e9c251f76023bc2feb8b2780dea420e`

**Thai source**

ชำระเงินหลังจอง

**English draft**

Pay after booking

## 17. curated_payment_bank / text

- Selector: `curated_payment_bank:text`
- Category: `reservation`
- Title: บัญชีธนาคารสำหรับชำระเงิน
- Source hash: `c64bfc779202a364c2b3157d778d88c2c7118b9b743a71462519dabcd2fe3106`

**Thai source**

ชำระเงินโดยโอนเข้าบัญชี Siam Commercial Bank (ธนาคารไทยพาณิชย์) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน

**English draft**

Pay by bank transfer to Siam Commercial Bank (Thai Commercial Bank) account named PSU Esports Studio - Phuket, account number 795-276244-1, and attach a copy of the bank transfer slip.

## 18. curated_payment_bank / title

- Selector: `curated_payment_bank:title`
- Category: `reservation`
- Title: บัญชีธนาคารสำหรับชำระเงิน
- Source hash: `29808003713ca60bc51180342273914050967ab27f74cd5cac44009e2a78d492`

**Thai source**

บัญชีธนาคารสำหรับชำระเงิน

**English draft**

Bank account for payment

## 19. curated_refund_policy / text

- Selector: `curated_refund_policy:text`
- Category: `reservation`
- Title: นโยบายคืนเงิน
- Source hash: `9a93ddb78a8c84b16ace4f9af638b64791ae9d9cde3655bad201192c6b77c58f`

**Thai source**

ไม่มีการคืนเงินในทุกกรณี ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ

**English draft**

No refunds in all cases, except when the center is at fault, such as malfunctioning equipment or unforeseen circumstances causing the center to close temporarily.

## 20. curated_refund_policy / title

- Selector: `curated_refund_policy:title`
- Category: `reservation`
- Title: นโยบายคืนเงิน
- Source hash: `3bbe00822945175d2f38bb77320e22fd746bda8993d4381cd923c998b538fd9e`

**Thai source**

นโยบายคืนเงิน

**English draft**

Refund Policy

## 21. curated_reservation_advance_time / text

- Selector: `curated_reservation_advance_time:text`
- Category: `reservation`
- Title: ต้องจองล่วงหน้า
- Source hash: `2414c09f03942f68ce59e3057fa943bf3f2c47ed83f23fd53a64f7c4bd170f07`

**Thai source**

ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง

**English draft**

Users must book online at least 1 hour before the scheduled usage time.

## 22. curated_reservation_advance_time / title

- Selector: `curated_reservation_advance_time:title`
- Category: `reservation`
- Title: ต้องจองล่วงหน้า
- Source hash: `20f8968f23d26711d96987100079ee2e9a9bc35913e75be02b0019b6844f4704`

**Thai source**

ต้องจองล่วงหน้า

**English draft**

Must book in advance

## 23. curated_reservation_max_sessions / text

- Selector: `curated_reservation_max_sessions:text`
- Category: `reservation`
- Title: จำนวน session สูงสุดต่อการจอง
- Source hash: `3d66e017b8ada09c8fdee807910cc474aa671b7cd50db0e711cda5f2bc7d628a`

**Thai source**

การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions

**English draft**

One booking can reserve up to 3 Sessions

## 24. curated_reservation_max_sessions / title

- Selector: `curated_reservation_max_sessions:title`
- Category: `reservation`
- Title: จำนวน session สูงสุดต่อการจอง
- Source hash: `99b54a0ae2595194f5c8d79c85f8cf9e8e2e0c532a49457bda343a43af97a4eb`

**Thai source**

จำนวน session สูงสุดต่อการจอง

**English draft**

Maximum number of sessions per reservation

## 25. curated_schedule_afternoon / text

- Selector: `curated_schedule_afternoon:text`
- Category: `reservation`
- Title: ช่วงเวลาบ่าย
- Source hash: `13ade375f27368f3b6ef919f8b1df034cd03564db724f6a0b783cd2494e2fd58`

**Thai source**

ตารางบริการช่วง Afternoon คือ 13:00 – 16:00

**English draft**

Afternoon service schedule: 13:00 – 16:00

## 26. curated_schedule_afternoon / title

- Selector: `curated_schedule_afternoon:title`
- Category: `reservation`
- Title: ช่วงเวลาบ่าย
- Source hash: `97c0b8e202954fdec472e8b87739cc3b62e0586e450fd89e0d8ee26b81c29180`

**Thai source**

ช่วงเวลาบ่าย

**English draft**

Afternoon time

## 27. curated_schedule_morning / text

- Selector: `curated_schedule_morning:text`
- Category: `reservation`
- Title: ช่วงเวลาเช้า
- Source hash: `99acf8b020dcc46569411dbcd230bdf0afd44599452a56bf652c0b00e890c7c4`

**Thai source**

ตารางบริการช่วง Morning คือ 09:00 – 12:00

**English draft**

Morning service schedule is 09:00 – 12:00

## 28. curated_schedule_morning / title

- Selector: `curated_schedule_morning:title`
- Category: `reservation`
- Title: ช่วงเวลาเช้า
- Source hash: `305db82db0f26ce0305f59531ef653967b545f0cbbae2909e89be6ed6c7ed999`

**Thai source**

ช่วงเวลาเช้า

**English draft**

Morning time

## 29. curated_time_change_policy / text

- Selector: `curated_time_change_policy:text`
- Category: `reservation`
- Title: เปลี่ยนเวลาใช้งาน
- Source hash: `c1ff3fc60f3a67283d4cb77b585ec9a78ced895c3cdb8ab2783c6dd80fa0e6a9`

**Thai source**

สามารถเปลี่ยนแปลงเวลาใช้งานได้ โดยต้องแจ้งล่วงหน้าก่อนเวลาที่จองไว้อย่างน้อย 1 ชั่วโมง หากแจ้งล่าช้าหรือไม่แจ้ง ศูนย์สงวนสิทธิ์ไม่คืนเงินและไม่ชดเชยเวลา

**English draft**

Reservation time can be changed, but must be notified at least 1 hour before the originally booked time. Failure to notify or notifying late will result in no refund and no compensation for time.

## 30. curated_time_change_policy / title

- Selector: `curated_time_change_policy:title`
- Category: `reservation`
- Title: เปลี่ยนเวลาใช้งาน
- Source hash: `5ae47e607a377170814d1dd0bec008faa8b71c4acfd72fb754945092f11f4a2c`

**Thai source**

เปลี่ยนเวลาใช้งาน

**English draft**

Change usage time

## 31. curated_user_info_required / text

- Selector: `curated_user_info_required:text`
- Category: `reservation`
- Title: ข้อมูลที่ต้องกรอกตอนจอง
- Source hash: `f08ac869b59ce6c9ab510669371da42e2fa0bd3f631bc0cb72e896c90339be75`

**Thai source**

ข้อมูลที่ต้องกรอกตอนจองประกอบด้วย Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี

**English draft**

The information required to book includes Student ID/Staff ID/National ID, full name, email, phone number, and comments if any

## 32. curated_user_info_required / title

- Selector: `curated_user_info_required:title`
- Category: `reservation`
- Title: ข้อมูลที่ต้องกรอกตอนจอง
- Source hash: `beddae5f410b8f176c7cb110b79677efa2ba87c97498f4b4e90564327fe5d155`

**Thai source**

ข้อมูลที่ต้องกรอกตอนจอง

**English draft**

Information to be filled when booking
