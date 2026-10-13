# รายละเอียดฟอร์มทุกหมวด — 24 kinds / 155 fields

ทุก field มี status/value/evidence_refs/note ใช้ schema 2020-12 ค่าที่กรอกผิดชนิดหรือ key นอก schema ถูกปฏิเสธ

ค่ากลาง: schema_version, record_id, kind, branch_id=psu_phuket, revision, lifecycle, validity, localization, aliases, review ตัวระบบบันทึก revision/hash/audit ส่วนเจ้าของยืนยันเนื้อหา

## ข้อมูลศูนย์ (`center`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อศูนย์อย่างเป็นทางการ | ★ | object {th, en} |
| operator | หน่วยงานเจ้าของ/ผู้ดำเนินการ | ★ | object {th, en} |
| description | ศูนย์ทำอะไร/ขอบเขตบริการ | optional | object {th, en} |
| address | ที่อยู่เต็ม | optional | object {th, en} |
| building | อาคาร | optional | string |
| floor | ชั้น | optional | string |
| map_url | ลิงก์แผนที่ | optional | string |
| timezone | เขตเวลา | ★ | string enum=Asia/Bangkok |

ต้นแบบ JSON: `app/knowledge/common/templates/center.draft.json`
schema: `app/knowledge/common/schemas/center.schema.json`

## ติดต่อ (`contact`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| channel | ประเภทช่องทาง | ★ | string enum=facebook, email, phone, website, onsite |
| value | URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย | ★ | string |
| purpose | ติดต่อเรื่องอะไรได้บ้าง | ★ | object {th, en} |
| office_hours | เวลาตอบของช่องทางนี้ | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/contact.draft.json`
schema: `app/knowledge/common/schemas/contact.schema.json`

## สิ่งอำนวยความสะดวก (`facility`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | เช่น ที่จอดรถ/ที่นั่งพัก | ★ | object {th, en} |
| location | อยู่บริเวณไหน | ★ | object {th, en} |
| usage_conditions | เงื่อนไขใช้บริการ | optional | object {th, en} |
| accessibility | การเข้าถึง/รถเข็น หากยังไม่มีข้อมูลให้ unknown | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/facility.draft.json`
schema: `app/knowledge/common/schemas/facility.schema.json`

## โซนบริการ (`zone`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ | ★ | object {th, en} |
| description | โซนนี้ใช้ทำอะไร | optional | object {th, en} |
| location | ตำแหน่งในศูนย์ | optional | object {th, en} |
| room_seats | จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน | optional | integer |

ต้นแบบ JSON: `app/knowledge/common/templates/zone.draft.json`
schema: `app/knowledge/common/schemas/zone.schema.json`

## รุ่นและสเปกอุปกรณ์ (`equipment_model`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อรุ่นอุปกรณ์ | ★ | object {th, en} |
| device_type | ประเภทอุปกรณ์ | ★ | string enum=pc, console, vr, wheel, display, peripheral, furniture |
| specifications | สเปกทีละค่า พร้อมหน่วย/รุ่น | optional | array rows{key, value, unit} |
| usage | วิธีใช้อุปกรณ์/ข้อควรทราบจากแหล่งข้อมูล | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/equipment_model.draft.json`
schema: `app/knowledge/common/schemas/equipment_model.schema.json`

## เครื่องหรือทรัพยากรจริง (`resource`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อเครื่อง เช่น PC #01 | ★ | object {th, en} |
| zone_id | โซนที่เครื่องตั้งอยู่ | ★ | string → zone |
| equipment_model_ids | รุ่นอุปกรณ์ที่ประกอบในเครื่องนี้ | optional | array → equipment_model |
| capacity_persons | จำนวนคนเล่นพร้อมกันของเครื่อง ไม่ใช่ห้อง | optional | integer |
| physical_pool_key | รหัสทรัพยากรร่วม เช่น VR 30/60 นาทีใช้เครื่องเดียวกัน | ★ | string |
| operational_status | พร้อมให้บริการทางกายภาพ ไม่ใช่สถานะจอง | ★ | string enum=in_service, out_of_service, retired |

ต้นแบบ JSON: `app/knowledge/common/templates/resource.draft.json`
schema: `app/knowledge/common/schemas/resource.schema.json`

## รายการที่เลือกในระบบจอง (`service`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อบริการตามหน้า WordPress | ★ | object {th, en} |
| resource_ids | เครื่องจริงที่บริการใช้ | ★ | array → resource |
| platform | แพลตฟอร์มของบริการ | ★ | string |
| session_minutes | ระยะเวลาเล่นของบริการ | ★ | integer |
| occupancy_minutes | เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60 | ★ | integer |
| capacity_min | ผู้เล่นขั้นต่ำ | optional | integer |
| capacity_max | ผู้เล่นสูงสุดตามบริการ | optional | integer |
| booking_product_key | รหัสผลิตภัณฑ์/API จาก WordPress ไม่ใช่เดาจากชื่อ | optional | string |

ต้นแบบ JSON: `app/knowledge/common/templates/service.draft.json`
schema: `app/knowledge/common/schemas/service.schema.json`

## ข้อมูลเกม (`game`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| title | ชื่อเกมอย่างเป็นทางการ | ★ | object {th, en} |
| edition | ภาค/edition ให้ตรง หากต้นทางไม่มีให้ unknown | optional | string |
| genre | แนวเกม | optional | object {th, en} |
| summary | เกมเกี่ยวกับอะไร | optional | object {th, en} |
| how_to_play | เป้าหมาย/วงจรการเล่นโดยสรุป | optional | object {th, en} |
| publisher_url | แหล่งจากผู้พัฒนาเกม | optional | string |
| supported_platforms | แพลตฟอร์มที่ตัวเกมรองรับ ไม่แปลว่าศูนย์มีให้เล่น | optional | array |
| age_rating | เรตเกมจากต้นทาง ไม่ใช่นโยบายรับเด็กของศูนย์ | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/game.draft.json`
schema: `app/knowledge/common/schemas/game.schema.json`

## เกมที่ศูนย์มีให้เล่นจริง (`game_service`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| game_id | เลือกเกมจากทะเบียนเกม | ★ | string → game |
| service_id | เลือกบริการจากทะเบียนการจอง | ★ | string → service |
| offered | ศูนย์ยืนยันมี/ไม่มีเกมนี้ในบริการนี้ | ★ | boolean |
| installed_resource_ids | ถ้ายืนยันเฉพาะเครื่อง ให้ระบุเครื่อง ห้ามอนุมานทั้งโซน | optional | array → resource |
| game_version | เวอร์ชันเกมที่ติดตั้ง ถ้าไม่ทราบให้ unknown | optional | string |
| account_policy_id | นโยบายบัญชีของศูนย์ | optional | string → policy |

ต้นแบบ JSON: `app/knowledge/common/templates/game_service.draft.json`
schema: `app/knowledge/common/schemas/game_service.schema.json`

## รูปแบบเล่นและเล่นกับเพื่อน (`game_mode`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| game_id | เกมที่อ้างถึง | ★ | string → game |
| mode_name | เช่น local co-op/online multiplayer | ★ | object {th, en} |
| platform | แพลตฟอร์มของโหมดนี้ | ★ | string |
| players_min | จำนวนผู้เล่นขั้นต่ำของโหมด | optional | integer |
| players_max | สูงสุดของโหมดเกม ไม่ใช่ความจุบริการ | optional | integer |
| network_requirement | ออนไลน์/อินเทอร์เน็ต/บัญชีที่ต้องใช้ | optional | object {th, en} |
| studio_supported | ศูนย์รองรับโหมดนี้จริงหรือยังไม่ยืนยัน | optional | boolean |

ต้นแบบ JSON: `app/knowledge/common/templates/game_mode.draft.json`
schema: `app/knowledge/common/schemas/game_mode.schema.json`

## วิธีเล่นและปุ่ม (`control_set`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| game_id | เกม/edition ที่ตรงกัน | ★ | string → game |
| platform | PC/PS5/Nintendo Switch/VR | ★ | string |
| input_device | ชนิดอุปกรณ์ควบคุม | ★ | string enum=keyboard_mouse, gamepad, racing_wheel, vr_motion |
| preset | default/custom profile ชื่อชุดปุ่ม | ★ | string |
| game_version | เวอร์ชันที่ตรวจชุดปุ่มนี้ | optional | string |
| bindings | ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record | ★ | array rows{buttons, gesture, action, context} |
| limitations | ข้อจำกัดหรือปุ่มที่ยังไม่ยืนยัน | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/control_set.draft.json`
schema: `app/knowledge/common/schemas/control_set.schema.json`

## กลุ่มผู้ใช้ (`audience`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อกลุ่ม เช่น บุคคลทั่วไป/หน่วยงานภายนอก | ★ | object {th, en} |
| eligibility | ใครอยู่ในกลุ่มนี้ ตามนโยบายจริง | ★ | object {th, en} |
| required_proofs | หลักฐานสิทธิ์ หากไม่มีข้อมูลให้ unknown | optional | array |

ต้นแบบ JSON: `app/knowledge/common/templates/audience.draft.json`
schema: `app/knowledge/common/schemas/audience.schema.json`

## ราคาต่อบริการ (`rate`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| service_id | บริการตามระบบจอง | ★ | string → service |
| audience_id | กลุ่มผู้ใช้ | ★ | string → audience |
| amount_minor | จำนวนสตางค์: 70 บาท = 7000; 0 คือฟรีเมื่อยืนยันจริง | ★ | integer |
| currency | สกุลเงิน | ★ | string enum=THB |
| unit | คิดต่ออะไร | ★ | string enum=per_session, per_hour, per_person, per_group |
| duration_minutes | ช่วงเวลาที่ราคานี้ครอบคลุม | ★ | integer |
| persons_min | ช่วงผู้ใช้ขั้นต่ำ | optional | integer |
| persons_max | ช่วงผู้ใช้สูงสุด | optional | integer |
| calculation_rule | อนุญาตคูณเวลาได้หรือคิดตายตัว ต้องมีหลักฐาน | ★ | string enum=fixed, linear, no_extrapolation |
| tax_note | ภาษี/เงื่อนไข ถ้ายังไม่ระบุห้ามคิดรวมเอง | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/rate.draft.json`
schema: `app/knowledge/common/schemas/rate.schema.json`

## ราคาเหมาโซน/ห้อง (`rental_package`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| name | ชื่อแพ็กเกจ | ★ | object {th, en} |
| zone_ids | โซนที่รวมในแพ็กเกจ | ★ | array → zone |
| audience_id | หน่วยงานภายใน/ภายนอก ไม่ใช่กลุ่มราคาบุคคล | ★ | string → audience |
| period_label | ครึ่งวัน/เต็มวันเป็นชื่อแพ็กเกจ | ★ | string enum=half_day, full_day, custom |
| duration_minutes | จำนวนจริงของนาที ต้องรอยืนยัน ไม่เดาว่า 4/8 ชั่วโมง | optional | integer |
| amount_minor | ราคาเป็นสตางค์ | ★ | integer |
| currency | สกุลเงิน | ★ | string enum=THB |
| equipment_included | จำนวนเครื่อง/อุปกรณ์ที่รวม | optional | object {th, en} |
| room_seats | จำนวนที่นั่งพื้นที่ตามชีต ไม่ใช่ผู้เล่นเครื่อง | optional | integer |
| terms | เช่น ค่าเจ้าหน้าที่นอกเวลา | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/rental_package.draft.json`
schema: `app/knowledge/common/schemas/rental_package.schema.json`

## ตารางบริการ (`schedule`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| timezone | เขตเวลา | ★ | string enum=Asia/Bangkok |
| zone_ids | ขอบเขตโซน; [] ที่ known หมายถึงทุกโซนตามประกาศ | ★ | array → zone |
| weekday | ISO weekday ในสเปกนี้ 0=จันทร์ ต้องแปลงจากต้นทางชัดเจน | ★ | integer |
| open_periods | ช่วงเปิดพื้นที่ | ★ | array rows{start, end} |
| bookable_periods | ช่วงที่จอง/เล่นได้ แยกจากเปิดพื้นที่ | ★ | array rows{start, end} |
| maintenance_periods | ช่วง maintenance | optional | array rows{start, end} |
| reason | เหตุผล/ประกาศของตาราง | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/schedule.draft.json`
schema: `app/knowledge/common/schemas/schedule.schema.json`

## วันปิด/ข้อยกเว้น (`closure`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| local_date | วันที่ ISO ค.ศ. ตามเวลาไทย | ★ | string |
| zone_ids | โซนที่ได้รับผล; [] = ทุกโซนเมื่อยืนยัน | ★ | array → zone |
| state | ประเภทข้อยกเว้น | ★ | string enum=closed, modified_hours, open_override |
| open_periods | เวลาใหม่ กรณี modified/open override | optional | array rows{start, end} |
| bookable_periods | เวลาที่จองได้ในวันที่ยกเว้น | optional | array rows{start, end} |
| reason | เหตุผลปิด/เปิดพิเศษ | ★ | object {th, en} |
| resolution_policy_id | นโยบายจัดการรายการจองเดิม หากไม่มีให้ unknown | optional | string → policy |

ต้นแบบ JSON: `app/knowledge/common/templates/closure.draft.json`
schema: `app/knowledge/common/schemas/closure.schema.json`

## นโยบายและกฎศูนย์ (`policy`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| topic | หัวข้อเชิงความหมาย เช่น personal_peripherals | ★ | string |
| subject | สิ่งที่กฎใช้กับ เช่น คีย์บอร์ด/เมาส์ส่วนตัว | ★ | object {th, en} |
| decision | อนุญาต/ห้าม/จำเป็น/มีเงื่อนไข | ★ | string enum=allowed, prohibited, required, conditional |
| conditions_all | เงื่อนไขที่ต้องครบ เช่น booking_paid=true; ไม่มีเงื่อนไขต้องยืนยันจริง | ★ | array rows{field, operator, value} |
| exceptions | ข้อยกเว้น หากต้นทางไม่ได้ระบุให้ unknown | optional | object {th, en} |
| consequence | ผลเมื่อผิดกฎ/ค่าปรับ ห้ามเติมเอง | optional | object {th, en} |
| details | ข้อความกฎพร้อมเงื่อนไขจากต้นทาง | ★ | object {th, en} |
| procedure_id | ขั้นตอนปฏิบัติที่เกี่ยวข้อง | optional | string → procedure |

ต้นแบบ JSON: `app/knowledge/common/templates/policy.draft.json`
schema: `app/knowledge/common/schemas/policy.schema.json`

## ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา (`procedure`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| topic | เรื่องที่ขั้นตอนนี้ใช้กับ | ★ | string |
| preconditions | สถานการณ์ก่อนทำ เช่น จองผิดเครื่อง | ★ | array rows{field, operator, value} |
| steps | ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production | ★ | array rows{order, instruction, contact_id} |
| required_documents | หลักฐาน/รายการที่ต้องเตรียม | optional | array |
| deadline_minutes | กำหนดเวลา ถ้าไม่ทราบอย่าเติม | optional | integer |
| outcome | หลังทำแล้วได้อะไร ขอบเขตสิ่งที่ยืนยัน | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/procedure.draft.json`
schema: `app/knowledge/common/schemas/procedure.schema.json`

## รายการแข่งขันและฉบับกติกา (`competition`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| game_id | เกมที่แข่งขัน | ★ | string → game |
| event_name | ชื่อรายการ+ปี+ประเภทให้ตรง | ★ | object {th, en} |
| division | เช่น ทีมชาย/ทีมผสม ถ้าไม่ระบุให้ unknown | optional | object {th, en} |
| rulebook_release | ฉบับและเวอร์ชันกติกา | ★ | string |
| competition_dates | วันที่การแข่งขันจากต้นทาง | optional | array |
| coverage | ความครบของเอกสาร ตรวจจากสารบัญและต้นทาง ไม่ใช่มี JSON แล้วครบ | ★ | string enum=complete, partial, conflicted |
| supersedes_id | ฉบับก่อนหน้าถ้าทราบ | optional | string → competition |

ต้นแบบ JSON: `app/knowledge/common/templates/competition.draft.json`
schema: `app/knowledge/common/schemas/competition.schema.json`

## ข้อกติกาการแข่งขัน (`competition_rule`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| competition_id | ฉบับรายการที่กฎเป็นของมัน | ★ | string → competition |
| section_number | เลขข้อเดิม เช่น 6.1.5 | ★ | string |
| facet | หมวดกฎ | ★ | string enum=identity, eligibility_registration, roster_composition, competition_format, match_configuration, pre_match_on_site, in_match_operations, fair_play_conduct, penalty_matrix, protest_dispute, references_change_history, game_specific |
| heading | หัวข้อข้อกติกา | ★ | object {th, en} |
| text | ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ | ★ | object {th, en} |
| depends_on_ids | ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม | optional | array → competition_rule |
| completeness | สถานะความสมบูรณ์ของข้อนี้ | ★ | string enum=complete, truncated, conflicted |

ต้นแบบ JSON: `app/knowledge/common/templates/competition_rule.draft.json`
schema: `app/knowledge/common/schemas/competition_rule.schema.json`

## ข่าว/กิจกรรม/ประกาศ/โปรโมชัน (`news`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| title | หัวข้อประกาศ | ★ | object {th, en} |
| body | รายละเอียด | ★ | object {th, en} |
| event_start | เวลาเริ่มกิจกรรม | optional | string |
| event_end | เวลาจบกิจกรรม | optional | string |
| audience_ids | ผู้เข้าร่วม/กลุ่มสิทธิ์ | optional | array → audience |
| contact_id | ช่องทางเกี่ยวกับกิจกรรม | optional | string → contact |
| registration_url | ลิงก์สมัคร ถ้ามี | optional | string |

ต้นแบบ JSON: `app/knowledge/common/templates/news.draft.json`
schema: `app/knowledge/common/schemas/news.schema.json`

## บุคลากร/ทีมที่เปิดเผยได้ (`person`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| display_name | ชื่อที่อนุญาตให้เผยแพร่ | ★ | object {th, en} |
| role | ตำแหน่ง/หน้าที่ | ★ | object {th, en} |
| team | ทีม/หน่วยงาน | optional | object {th, en} |
| public_contact_id | ช่องทางงานที่อนุญาตเผยแพร่ | optional | string → contact |
| public_scope | รายละเอียดที่เผยแพร่ได้ ไม่ใส่ข้อมูลลูกค้าหรือสลิป | ★ | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/person.draft.json`
schema: `app/knowledge/common/schemas/person.schema.json`

## คำถามเสริมและเอกสารทั่วไปของศูนย์ (`faq`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| question | คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase | ★ | object {th, en} |
| answer | คำตอบพร้อมหลักฐานของศูนย์ | ★ | object {th, en} |
| related_ids | รายการที่เกี่ยวข้อง หากใช้ต้อง resolve ข้าม kind | optional | array → * |
| topic | หัวข้อเชิงความหมาย | ★ | string |
| scope_note | ขอบเขตและข้อจำกัด ไม่ใช้ FAQ override ราคาหรือสถานะสด | optional | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/faq.draft.json`
schema: `app/knowledge/common/schemas/faq.schema.json`

## การเชื่อมสถานะสด (`live_binding`)

| ช่อง | ความหมาย | ต้องทราบก่อนเผยแพร่ | ชนิด / อ้างอิง |
|---|---|---|---|
| service_id | บริการของศูนย์ | ★ | string → service |
| provider | ผู้ให้ข้อมูลสด | ★ | string enum=wordpress_booking |
| external_resource_key | รหัสที่ API ใช้จริง | ★ | string |
| physical_pool_key | ทรัพยากรร่วม ต้องตรง resource ที่ service ใช้ | ★ | string |
| status_mapping | ความหมายสถานะจาก API ต้องมี fixture ที่รู้ผล | ★ | array rows{raw, normalized} |
| timezone | เขตเวลาของการแปลงข้อมูล | ★ | string enum=Asia/Bangkok |
| freshness_policy | นโยบาย cache/TTL ที่อนุมัติ | ★ | object {th, en} |

ต้นแบบ JSON: `app/knowledge/common/templates/live_binding.draft.json`
schema: `app/knowledge/common/schemas/live_binding.schema.json`
