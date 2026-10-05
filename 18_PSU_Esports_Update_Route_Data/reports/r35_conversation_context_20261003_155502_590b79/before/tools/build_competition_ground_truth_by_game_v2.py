from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "ground_truth" / "competition_by_game_v2"
REPORT_PATH = ROOT / "docs" / "21_competition_ground_truth_by_game_v2.md"


GAME_META = {
    "cs2": {
        "game": "Counter-Strike 2",
        "source": "competition_rules_cs2_psu_phuket_2026",
        "prefix": "cs2",
        "filename": "ground_truth_competition_cs2_v2_diverse.jsonl",
    },
    "rov": {
        "game": "Arena of Valor (RoV)",
        "source": "competition_rules_rov_blueket_2025_men",
        "prefix": "rov",
        "filename": "ground_truth_competition_rov_v2_diverse.jsonl",
    },
    "valorant": {
        "game": "VALORANT",
        "source": "competition_rules_valorant_psu_phuket_2026",
        "prefix": "valorant",
        "filename": "ground_truth_competition_valorant_v2_diverse.jsonl",
    },
    "tekken8": {
        "game": "Tekken 8",
        "source": "competition_rules_tekken8_psu_esports",
        "prefix": "tekken8",
        "filename": "ground_truth_competition_tekken8_v2_diverse.jsonl",
    },
}


def case(
    question: str,
    intent: str,
    expected_keywords: list[str],
    source_fact_key: str,
    answer_type: str = "fact",
    difficulty: str = "medium",
    variant_type: str | None = None,
    expected_mode_prefix: str = "pipeline:",
) -> dict[str, Any]:
    return {
        "category": "competition_rules",
        "intent": intent,
        "question": question,
        "expected_keywords": expected_keywords,
        "answer_type": answer_type,
        "difficulty": difficulty,
        "variant_type": variant_type or intent,
        "source_fact_key": source_fact_key,
        "expected_mode_prefix": expected_mode_prefix,
    }


CASES: dict[str, list[dict[str, Any]]] = {
    "cs2": [
        case("PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน", "eligibility", ["นักศึกษา", "มหาวิทยาลัยสงขลานครินทร์", "ภูเก็ต"], "cs2_eligibility", "fact", "medium"),
        case("คนนอก PSU Phuket ลงแข่ง CS2 รายการนี้ได้ไหม", "eligibility", ["เฉพาะ", "นักศึกษา", "ภูเก็ต"], "cs2_eligibility", "policy", "hard"),
        case("CS2 แข่งทีมละกี่คน", "team_size", ["CS2", "ผู้เล่น 5 คน"], "cs2_team_size", "fact", "easy"),
        case("Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน", "team_size", ["5 คน"], "cs2_team_size", "fact", "medium"),
        case("CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม", "game_version", ["Steam", "ห้าม", "ดัดแปลง"], "cs2_game_version", "fact", "hard"),
        case("รายการ CS2 ใช้เวอร์ชันเกมแบบไหน", "game_version", ["ล่าสุด", "CS2", "Steam"], "cs2_game_version", "fact", "medium"),
        case("ภาษาทางการของการแข่งขัน CS2 คือภาษาอะไร", "language", ["ภาษาไทย"], "cs2_official_language", "fact", "easy"),
        case("ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร", "language", ["ภาษาไทย"], "cs2_official_language", "fact", "hard"),
        case("CS2 แข่งกี่วันและแข่งที่ไหน", "schedule_location", ["1 วัน", "PSU Esports Studio", "Phuket"], "cs2_location_duration", "fact", "medium"),
        case("สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน", "schedule_location", ["PSU Esports Studio", "Phuket"], "cs2_location_duration", "fact", "medium"),
        case("CS2 ใช้ช่องทางสื่อสารหลักอะไร", "communication", ["Discord"], "cs2_discord", "fact", "easy"),
        case("ผู้เข้าแข่ง CS2 ต้องใช้เซิร์ฟเวอร์ไหนในการสื่อสาร", "communication", ["Discord", "ศูนย์"], "cs2_discord", "fact", "medium"),
        case("CS2 เปลี่ยนสมาชิกทีมระหว่างทัวร์นาเมนต์ได้ไหม", "roster_change", ["ไม่มีการเปลี่ยนแปลง", "สมาชิก"], "cs2_roster_lock", "policy", "medium"),
        case("หลังปิดรับสมัคร CS2 ลงทะเบียนผู้เล่นเพิ่มได้ไหม", "registration", ["ไม่อนุญาต", "ปิดรับสมัคร"], "cs2_no_late_registration", "policy", "medium"),
        case("ถ้าผู้เล่น CS2 ถอนตัวทีมจะเป็นยังไง", "eligibility", ["ถอนตัว", "ตัดสิทธิ์"], "cs2_member_withdraw", "policy", "hard"),
        case("ผู้เล่น CS2 เล่นให้สองทีมได้ไหม", "eligibility", ["ทีมเดียว"], "cs2_one_team_only", "policy", "medium"),
        case("สายการแข่งขัน CS2 จะประกาศก่อนแข่งนานแค่ไหน", "schedule", ["ล่วงหน้า", "1 วัน"], "cs2_bracket_notice", "fact", "medium"),
        case("CS2 มาสายหรือไม่ยืนยันเข้าแข่งก่อนแมตช์เสี่ยงอะไร", "late_start", ["มาสาย", "ตัดสิทธิ์"], "cs2_late_may_disqualify", "policy", "hard"),
        case("รูปแบบทัวร์นาเมนต์ CS2 เป็นแบบไหน", "format", ["Single Elimination"], "cs2_format", "fact", "medium"),
        case("CS2 รอบรองกับรอบชิงแข่ง BO อะไร", "format", ["รอบรอง", "รอบชิง", "BO3"], "cs2_format", "fact", "medium"),
        case("โหมดในเกม CS2 ใช้โหมดอะไร", "game_setting", ["Competitive", "5v5"], "cs2_competitive_5v5", "fact", "medium"),
        case("CS2 เวลาต่อรอบกับ Freeze time เท่าไหร่", "game_setting", ["1:55", "15 วินาที"], "cs2_round_time_freeze", "fact", "hard"),
        case("CS2 เงินเริ่มต้นกับเวลาระเบิดตั้งไว้เท่าไหร่", "game_setting", ["$800", "40 วินาที"], "cs2_start_money_bomb_timer", "fact", "hard"),
        case("CS2 ชนะกี่รอบก่อนถึงชนะในแผนที่", "game_setting", ["13 รอบ"], "cs2_win_13_rounds", "fact", "medium"),
        case("CS2 เล่นสูงสุดกี่รอบก่อน overtime", "game_setting", ["24 รอบ", "12 รอบ"], "cs2_max_rounds", "fact", "hard"),
        case("CS2 overtime เล่นยังไง", "game_setting", ["ฝั่งละ 3 รอบ", "4 ใน 6", "$10,000"], "cs2_overtime", "fact", "hard"),
        case("CS2 ต่อเวลาได้จำกัดกี่ครั้ง", "game_setting", ["ไม่จำกัด"], "cs2_overtime_unlimited", "fact", "hard"),
        case("CS2 map pool มีอะไรบ้าง", "map_pool", ["Ancient", "Anubis", "Dust 2", "Train"], "cs2_map_pool", "fact", "medium"),
        case("CS2 มี Mirage กับ Nuke ในแผนที่แข่งไหม", "map_pool", ["Mirage", "Nuke"], "cs2_map_pool", "fact", "medium"),
        case("CS2 เลือกแผนที่ผ่านอะไร", "map_pool", ["MAPBAN.GG"], "cs2_mapban", "fact", "medium"),
        case("CS2 เลือกฝั่งด้วยวิธีไหน", "side_selection", ["ดวลมีด", "เลือกฝั่ง"], "cs2_knife_round", "fact", "medium"),
        case("CS2 technical pause ขอได้กี่ครั้งและนานเท่าไหร่", "pause", ["2 ครั้ง", "10 นาที"], "cs2_pause", "fact", "medium"),
        case("CS2 เครื่องมีปัญหาต้องแจ้งใครตอน technical pause", "pause", ["กรรมการ", "ทันที"], "cs2_pause", "fact", "hard"),
        case("CS2 tactical timeout ได้กี่ครั้ง ครั้งละกี่วินาที", "pause", ["4 ครั้ง", "30 วินาที"], "cs2_timeout", "fact", "medium"),
        case("CS2 ขอเวลานอกใช้ได้ช่วงไหน", "pause", ["Freeze time"], "cs2_timeout_freeze", "fact", "hard"),
        case("CS2 ใช้บัคแผนที่หรือ Engine ได้ไหม", "penalty", ["ห้าม", "บัค", "ปรับแพ้"], "cs2_bug_penalty", "policy", "medium"),
        case("CS2 ดูสตรีมสดระหว่างแข่งได้ไหม", "penalty", ["ห้าม", "สตรีม"], "cs2_stream_sniping", "policy", "medium"),
        case("CS2 พฤติกรรมเหยียดหรือวาจาสร้างความเกลียดชังผิดกติกาไหม", "penalty", ["ห้าม", "เกลียดชัง"], "cs2_player_conduct", "policy", "medium"),
        case("CS2 นำคีย์บอร์ดเมาส์ส่วนตัวไปเองได้ไหม", "equipment", ["คีย์บอร์ด", "เมาส์", "มาเองได้"], "cs2_allowed_personal_equipment", "fact", "medium"),
        case("CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้บ้าง", "equipment", ["PC", "จอภาพ", "โต๊ะ", "เก้าอี้"], "cs2_organizer_equipment", "fact", "medium"),
        case("CS2 ปรับ crosshair หรือ resolution ได้ไหม", "game_setting", ["Crosshair", "Resolution", "Brightness"], "cs2_allowed_settings", "fact", "medium"),
        case("CS2 ใช้ macro หรือ script ได้หรือเปล่า", "equipment", ["ห้าม", "สคริปต์", "มาโคร"], "cs2_macro_ban", "policy", "medium"),
        case("CS2 ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม", "equipment", ["ห้าม", "ติดตั้งโปรแกรม"], "cs2_no_install", "policy", "medium"),
        case("CS2 เข้าโซเชียลบนคอมแข่งได้ไหม", "equipment", ["ห้าม", "โซเชียลมีเดีย"], "cs2_no_social", "policy", "medium"),
        case("CS2 ช่วงเตรียมตัวมีคนในพื้นที่ได้ไม่เกินกี่คน", "area_rules", ["ไม่เกิน 6 คน"], "cs2_match_prep_people", "fact", "medium"),
        case("CS2 เอามือถือหรือ smart watch เข้าพื้นที่แข่งได้ไหม", "area_rules", ["ห้าม", "โทรศัพท์มือถือ", "สมาร์ทวอทช์"], "cs2_no_electronics", "policy", "medium"),
        case("CS2 หัวหน้าทีมนำเอกสารเข้าไปได้ไหม", "area_rules", ["หัวหน้าทีม", "เอกสาร", "กรรมการ"], "cs2_notes_captain", "policy", "hard"),
        case("CS2 อนุญาตอาหารหรือเครื่องดื่มอะไรในพื้นที่แข่ง", "area_rules", ["น้ำดื่ม", "ปิดสนิท", "หมากฝรั่ง"], "cs2_food_drink", "fact", "hard"),
    ],
    "rov": [
        case("Blueket Games RoV แข่งวันไหน", "schedule", ["11 กันยายน 2568"], "rov_schedule_date", "fact", "medium"),
        case("RoV ลงทะเบียนช่วงกี่โมง", "schedule", ["8.00", "8.30"], "rov_registration_time", "fact", "medium"),
        case("RoV แบ่งสายการแข่งขันกี่โมง", "schedule", ["8.30", "8.40"], "rov_bracket_time", "fact", "medium"),
        case("RoV รอบ 5 ทีมแข่งช่วงเวลาไหน", "schedule", ["8.40", "10.00", "BO3"], "rov_five_team_round", "fact", "hard"),
        case("RoV รอบรองคู่ที่ 1 เริ่มประมาณกี่โมง", "schedule", ["10.00", "11.30"], "rov_semifinal_1", "fact", "hard"),
        case("RoV รอบรองคู่ที่ 2 อยู่ช่วงเวลาไหน", "schedule", ["12.30", "14.00"], "rov_semifinal_2", "fact", "hard"),
        case("RoV รอบชิงอันดับ 3 แข่งกี่โมงถึงกี่โมง", "schedule", ["14.00", "15.30"], "rov_third_place", "fact", "hard"),
        case("RoV รอบชิงชนะเลิศแข่งช่วงไหน", "schedule", ["15.30", "17.00"], "rov_final_time", "fact", "hard"),
        case("RoV แข่งที่อาคารไหนของ PSU Esports Studio Phuket", "schedule_location", ["อาคาร 5", "ชั้น 1"], "rov_location", "fact", "medium"),
        case("RoV แข่งออนไลน์หรือออฟไลน์", "format", ["ออฟไลน์"], "rov_offline", "fact", "easy"),
        case("แข่ง ROV ต้องเล่นกี่เกม", "format", ["BO3", "ทุกรอบ"], "rov_format_bo3", "fact", "medium"),
        case("RoV รายการนี้เป็น Best of 3 ทุกด่านไหม", "format", ["Best of 3", "ทุกรอบ"], "rov_format_bo3", "fact", "medium"),
        case("RoV เกมแรกใครได้ฝั่งสีน้ำเงิน", "side_selection", ["ด้านบน", "สายการแข่งขัน", "สีน้ำเงิน"], "rov_blue_side_first_game", "fact", "hard"),
        case("RoV เกมถัดไปใครเลือกฝั่ง", "side_selection", ["ผู้ที่แพ้", "เลือกฝั่ง"], "rov_loser_side_choice", "fact", "hard"),
        case("กรรมการ RoV แจ้งอะไรให้ทีมเข้าห้องแข่ง", "match_process", ["หมายเลขห้อง"], "rov_room_number", "fact", "medium"),
        case("RoV มาสายเกิน 15 นาทีเป็นอะไร", "late_start", ["15 นาที", "ปรับแพ้"], "rov_late_start", "policy", "medium"),
        case("กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง", "late_start", ["ล่าช้า", "ปรับแพ้"], "rov_late_start", "policy", "hard"),
        case("RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว", "hero_rule", ["18 ตัว"], "rov_hero_minimum", "fact", "medium"),
        case("RoV ใช้ระบบแบนเลือกฮีโร่แบบไหน", "hero_rule", ["Global Ban/Pick"], "rov_global_ban_pick", "fact", "hard"),
        case("RoV ใส่รูนและพลังเสริมได้ไหม", "hero_rule", ["รูน", "พลังเสริม", "ตามความต้องการ"], "rov_rune_talent", "policy", "medium"),
        case("RoV เลือกฮีโร่ซ้ำได้ไหม", "hero_rule", ["ห้าม", "ฮีโร่ซ้ำ"], "rov_duplicate_hero", "policy", "medium"),
        case("RoV ใช้สกินพิเศษได้หรือเปล่า", "skin", ["Default Skin"], "rov_skin", "policy", "medium"),
        case("RoV แต่ละทีม pause ได้กี่ครั้ง ครั้งละเท่าไหร่", "pause", ["5 ครั้ง", "1 นาที"], "rov_pause", "fact", "medium"),
        case("RoV ถ้า pause เกิน 1 นาทีอีกทีมทำอะไรได้", "pause", ["Resume"], "rov_resume_after_pause", "fact", "hard"),
        case("RoV หลุดเพราะเน็ตล่มหรือเซิร์ฟเวอร์พังต้องทำยังไง", "rematch", ["แจ้งทีมงาน", "ดุลยพินิจ", "กรรมการ"], "rov_force_majeure_disconnect", "policy", "hard"),
        case("RoV ขอเริ่มเกมใหม่ได้ตอนไหนก่อน First Blood", "rematch", ["First Blood", "2 นาที", "เริ่มเกมใหม่"], "rov_rematch_first_blood", "fact", "medium"),
        case("RoV ถ้าเกิด First Blood แล้วขอ remake ได้ไหม", "rematch", ["First Blood", "อนุญาต", "คู่แข่ง", "กรรมการ"], "rov_rematch_after_first_blood", "policy", "hard"),
        case("RoV เจตนากด pause ก่อกวนโดนอะไร", "penalty", ["ปรับแพ้", "ตัดสิทธิ์"], "rov_intentional_pause_penalty", "policy", "medium"),
        case("RoV พักหลังจบทุกสองเกมกี่นาที", "break_time", ["5 นาที"], "rov_break_after_two_games", "fact", "medium"),
        case("RoV ไม่กลับมาหลังเวลาพักที่กำหนดเสี่ยงอะไร", "break_time", ["ปรับ", "แพ้"], "rov_late_after_break", "policy", "hard"),
        case("RoV เกมหยุดเกิน 10 นาทีทีมงานทำอะไรได้", "pause", ["10 นาที", "เริ่มเกมใหม่"], "rov_pause_over_10", "policy", "hard"),
        case("RoV เครื่องร้อนพักได้กี่นาที", "pause", ["เครื่องร้อน", "5 นาที"], "rov_device_overheat_pause", "fact", "hard"),
        case("RoV ระหว่าง pause ผู้เล่นคุยกันได้ไหม", "pause", ["ห้าม", "สื่อสาร"], "rov_no_comm_pause", "policy", "medium"),
        case("RoV บทลงโทษการ pause ผิดครั้งแรกคืออะไร", "penalty", ["ครั้งที่ 1", "ตักเตือน"], "rov_pause_penalty_first", "fact", "medium"),
        case("RoV pause ผิดครั้งที่ 2 โดนอะไร", "penalty", ["ครั้งที่ 2", "เพิ่มสิทธิการแบนฮีโร่", "1 ครั้ง"], "rov_pause_penalty_second", "fact", "hard"),
        case("RoV pause ผิดครั้งที่ 3 โดนอะไร", "penalty", ["ครั้งที่ 3", "เพิ่มสิทธิการแบนฮีโร่", "2 ครั้ง"], "rov_pause_penalty_third", "fact", "hard"),
        case("RoV ใช้อุปกรณ์อะไรแข่ง", "equipment", ["โทรศัพท์มือถือ"], "rov_mobile_only", "fact", "easy"),
        case("RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม", "equipment", ["ไม่อนุญาต", "Tablet", "iPad"], "rov_no_tablet_ipad", "policy", "medium"),
        case("RoV เอาปลั๊กพ่วงกับอุปกรณ์ชาร์จส่วนตัวได้ไหม", "equipment", ["ปลั๊กพ่วง", "อุปกรณ์ชาร์จ"], "rov_charger", "fact", "medium"),
        case("RoV ใช้คำพูดไม่สุภาพหรือเสียดสีโดนอะไร", "penalty", ["ปรับแพ้", "เกมที่พบ"], "rov_rude_penalty", "policy", "medium"),
        case("RoV ส่งผลการแข่งขันเท็จโดนลงโทษยังไง", "penalty", ["ปรับแพ้", "ตัดสิทธิ์"], "rov_false_result", "policy", "hard"),
        case("RoV ให้คนอื่นที่ไม่ได้ลงทะเบียนมาแข่งแทนได้ไหม", "penalty", ["ไม่ตรงตามที่ลงทะเบียน", "ปรับแพ้", "ตัดสิทธิ์"], "rov_unregistered_player", "policy", "hard"),
        case("RoV ห้ามให้คนอื่นเล่นแทนตัวเองไหม", "penalty", ["เล่นแทน", "ห้าม"], "rov_substitute_play", "policy", "medium"),
        case("RoV ถามสรุปรูปแบบแข่งกับสถานที่แบบสั้นๆ", "summary", ["ออฟไลน์", "BO3", "PSU Esports Studio"], "rov_format_location_summary", "summary", "hard"),
        case("RoV ถ้าถามเรื่องเวลาแข่งทั้งวันควรตอบหัวข้ออะไรบ้าง", "schedule", ["ลงทะเบียน", "รอบรอง", "รอบชิง"], "rov_full_day_schedule", "summary", "hard"),
        case("RoV ขอกฎ disconnect แบบเข้าใจง่าย", "rematch", ["pause", "First Blood", "2 นาที"], "rov_disconnect_summary", "summary", "hard"),
        case("RoV มีข้อมูลตัวสำรองชัดเจนไหมในไฟล์นี้", "team_size", ["5v5"], "rov_team_size", "fact", "hard"),
        case("สมาชิกในทีม ROV ต้องเล่นพร้อมกันฝั่งละกี่คน", "team_size", ["5v5", "ฝ่ายละ 5 คน"], "rov_team_size", "fact", "medium"),
    ],
    "valorant": [
        case("VALORANT ทีมละกี่คน", "team_size", ["5 คน"], "valorant_team_size", "fact", "easy"),
        case("วาโลต้องส่งผู้เล่นตัวจริงกี่คน", "team_size", ["ตัวจริง 5 คน"], "valorant_team_size", "fact", "medium"),
        case("VALORANT Match Prep มีคนได้ไม่เกินกี่คน", "area_rules", ["ไม่เกิน 6"], "valorant_match_prep_people", "fact", "medium"),
        case("VALORANT เอามือถือเข้าพื้นที่แข่งได้ไหม", "area_rules", ["ห้าม", "โทรศัพท์มือถือ"], "valorant_no_mobile", "policy", "medium"),
        case("VALORANT หัวหน้าทีมนำโน้ตเข้าได้ไหม", "area_rules", ["หัวหน้าทีม", "กรรมการ"], "valorant_notes_captain", "policy", "hard"),
        case("VALORANT อาหารเครื่องดื่มที่อนุญาตมีอะไร", "area_rules", ["น้ำดื่ม", "ปิดสนิท", "หมากฝรั่ง"], "valorant_food_drink", "fact", "hard"),
        case("VALORANT ต้องมารายงานตัวก่อนแข่งกี่นาที", "checkin", ["30 นาที"], "valorant_checkin_30", "fact", "medium"),
        case("วาโล agent ใหม่ใช้ได้ทันทีไหม", "character", ["Agent", "2 สัปดาห์"], "valorant_new_agent_restriction", "policy", "medium"),
        case("VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนใช้แข่ง", "map_pool", ["4 สัปดาห์"], "valorant_new_map_restriction", "policy", "medium"),
        case("VALORANT ต้องปิด setting อะไรก่อนแข่ง", "game_setting", ["เลือด", "ศพ", "OFF"], "valorant_blood_bodies_off", "fact", "hard"),
        case("VALORANT เปิดกราฟ FPS หรือ latency ระหว่างแข่งได้ไหม", "game_setting", ["ห้าม", "FPS", "Latency"], "valorant_no_fps_latency_graph", "policy", "hard"),
        case("VALORANT map pool มีทั้งหมดกี่ map และชื่ออะไรบ้าง", "map_pool", ["7", "Abyss", "Sunset"], "valorant_map_pool", "fact", "medium"),
        case("วาโลมี Haven Lotus Sunset ใน map pool ไหม", "map_pool", ["Haven", "Lotus", "Sunset"], "valorant_map_pool", "fact", "medium"),
        case("VALORANT ban map จนเหลือกี่แผนที่", "map_pool", ["3 แผนที่"], "valorant_map_ban_three", "fact", "hard"),
        case("VALORANT เลือกฝั่งด้วยวิธีอะไร", "side_selection", ["โยนเหรียญ"], "valorant_coin_toss", "fact", "medium"),
        case("หลังจบแมตช์ VALORANT ใครยืนยันและบันทึกผล", "post_match", ["เจ้าหน้าที่", "บันทึกผล"], "valorant_result_recording", "fact", "medium"),
        case("VALORANT ถ้า forfeit แผนที่นั้นบันทึกผลเป็นเท่าไหร่", "penalty", ["13-0"], "valorant_forfeit_score", "fact", "medium"),
        case("VALORANT pause มีกี่ประเภทหลัก", "pause", ["3", "Tactical", "Technical", "Emergency"], "valorant_pause_types", "fact", "medium"),
        case("VALORANT tactical timeout ได้กี่ครั้งต่อแผนที่", "pause", ["2", "ต่อแผนที่"], "valorant_tactical_timeout", "fact", "medium"),
        case("วาโล tactical timeout ครั้งละกี่วินาที", "pause", ["60 วินาที"], "valorant_tactical_timeout", "fact", "medium"),
        case("VALORANT overtime ได้ timeout เพิ่มไหม", "pause", ["Overtime", "เพิ่ม", "1 ครั้ง"], "valorant_overtime_timeout", "fact", "hard"),
        case("VALORANT Technical Pause ใช้กรณีไหน", "pause", ["อุปกรณ์ขัดข้อง", "หลุด", "ซอฟต์แวร์"], "valorant_technical_pause_reason", "fact", "medium"),
        case("ตอน Technical Pause วาโลคุยกันได้ไหม", "pause", ["ห้าม", "สื่อสาร", "เว้นแต่"], "valorant_no_comm_technical_pause", "policy", "hard"),
        case("VALORANT Emergency Pause ขอได้กี่ครั้ง", "pause", ["1 ครั้ง", "ต่อแผนที่"], "valorant_emergency_pause", "fact", "medium"),
        case("VALORANT Emergency Pause รวมเวลาได้ไม่เกินกี่นาที", "pause", ["10 นาที"], "valorant_emergency_pause", "fact", "medium"),
        case("VALORANT ถ้า emergency pause เกินเวลาผู้เล่นอาจเป็นอะไร", "pause", ["หมดสิทธิ์", "ตัวสำรอง"], "valorant_emergency_over_time", "policy", "hard"),
        case("VALORANT Play Through Bug คืออะไร", "bug_rule", ["ไม่ส่งผลกระทบ", "เล่นต่อ"], "valorant_play_through_bug", "fact", "hard"),
        case("VALORANT Major Bug ขอ Challenge ได้ไหม", "bug_rule", ["Major Bug", "Challenge"], "valorant_major_bug", "fact", "hard"),
        case("VALORANT Game Breaking Bug จัดการยังไง", "bug_rule", ["Game-Breaking", "ย้อนรอบ"], "valorant_game_breaking_bug", "policy", "hard"),
        case("VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้", "bug_rule", ["ก่อน", "ดาเมจ", "ย้อนรอบ"], "valorant_rollback_before_damage", "fact", "hard"),
        case("VALORANT ถ้าทำ damage ไปแล้ว rollback ได้ไหม", "bug_rule", ["damage", "ไม่", "Challenge"], "valorant_no_rollback_after_damage", "policy", "hard"),
        case("VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม", "penalty", ["ผิด", "ได้เปรียบ"], "valorant_exploit_offense", "policy", "medium"),
        case("VALORANT วางกล้อง Cypher จุดมองไม่เห็นได้ไหม", "character", ["ห้าม", "Cypher"], "valorant_cypher_camera", "policy", "medium"),
        case("VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม", "character", ["ห้าม", "นอกขอบเขต"], "valorant_out_of_bounds", "policy", "hard"),
        case("VALORANT ข้อยกเว้น KAY/O ZERO/POINT คืออะไร", "character", ["KAY/O", "ZERO/POINT", "Texture"], "valorant_kayo_exception", "fact", "hard"),
        case("VALORANT ใช้เพื่อนกระโดดต่อตัวขึ้นจุดสูงได้ไหม", "character", ["ห้าม", "กระโดด"], "valorant_boosting_ban", "policy", "hard"),
        case("VALORANT ความผิดครั้งแรกผลกระทบต่ำโดนอะไร", "penalty", ["Warning", "ตักเตือน"], "valorant_warning", "fact", "medium"),
        case("VALORANT Round Rollback ใช้เมื่อไหร่", "penalty", ["Round Rollback", "ช่องโหว่"], "valorant_round_rollback_penalty", "fact", "hard"),
        case("VALORANT Round Loss เกิดจากอะไร", "penalty", ["Round Loss", "เจตนา", "ช่องโหว่"], "valorant_round_loss", "fact", "hard"),
        case("VALORANT Map Forfeit ใช้กรณีไหน", "penalty", ["Map Forfeit", "ร้ายแรง", "ซ้ำ"], "valorant_map_forfeit", "fact", "hard"),
        case("VALORANT Match Forfeit ใช้กับความผิดแบบไหน", "penalty", ["Match Forfeit", "Cheating", "Match fixing"], "valorant_match_forfeit", "fact", "hard"),
        case("VALORANT ใช้ keyboard Snap Tap หรือ SOCD ได้ไหม", "equipment", ["Snap Tap", "SOCD", "permitted"], "valorant_snap_tap", "policy", "hard"),
        case("VALORANT ใช้ macro ได้ไหม", "equipment", ["ห้าม", "Macros"], "valorant_macro_ban", "policy", "medium"),
        case("VALORANT ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม", "equipment", ["ห้าม", "ติดตั้งโปรแกรม"], "valorant_no_install", "policy", "medium"),
        case("VALORANT เข้าเว็บสื่อสารหรือโซเชียลบนคอมแข่งได้ไหม", "equipment", ["ห้าม", "social media"], "valorant_no_social", "policy", "medium"),
        case("VALORANT สรุป pause แต่ละประเภทแบบสั้นๆ", "pause", ["Tactical", "Technical", "Emergency"], "valorant_pause_summary", "summary", "hard"),
        case("VALORANT สรุปกฎเนื้อหาใหม่กับ map pool", "summary", ["Agent", "2 สัปดาห์", "แผนที่ใหม่", "4 สัปดาห์", "Abyss"], "valorant_content_map_summary", "summary", "hard"),
        case("VALORANT สรุปบทลงโทษในเกมว่ามีอะไรบ้าง", "penalty", ["Warning", "Round Rollback", "Round Loss", "Map Forfeit", "Match Forfeit"], "valorant_penalty_summary", "summary", "hard"),
    ],
    "tekken8": [
        case("Tekken 8 แข่งออนไลน์หรือออฟไลน์", "format", ["ออฟไลน์"], "tekken8_offline", "fact", "easy"),
        case("Tekken 8 ใช้เครื่องอะไรแข่ง", "equipment", ["PlayStation 5"], "tekken8_platform", "fact", "easy"),
        case("Tekken 8 แข่งแบบกี่ต่อกี่", "format", ["1v1"], "tekken8_1v1", "fact", "easy"),
        case("Tekken 8 FT2 คือชนะกี่เกมก่อน", "format", ["ชนะครบ 2 เกม"], "tekken8_ft2", "fact", "medium"),
        case("Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร", "format", ["เกมตัดสิน"], "tekken8_decider", "fact", "medium"),
        case("Tekken 8 ในแต่ละเกมแข่งกี่รอบ", "game_setting", ["3 รอบ"], "tekken8_round_3", "fact", "medium"),
        case("Tekken 8 จำกัดเวลาต่อรอบกี่วินาที", "game_setting", ["60 วินาที"], "tekken8_timer_60", "fact", "medium"),
        case("Tekken 8 ตั้งค่า Advantage เป็นอะไร", "game_setting", ["No advantage"], "tekken8_advantage", "fact", "hard"),
        case("Tekken 8 เลือก Stage อย่างไร", "game_setting", ["Random"], "tekken8_stage_random", "fact", "medium"),
        case("Tekken 8 เลือกตัวละคร DLC ได้ไหม", "character", ["ยกเว้น", "DLC"], "tekken8_dlc_ban", "policy", "medium"),
        case("Tekken 8 ใช้ตัวละครตัวไหนก็ได้ไหม", "character", ["ทุกตัว", "ยกเว้น", "DLC"], "tekken8_character_rule", "policy", "hard"),
        case("Tekken 8 ปรับแต่งชุดหรือทรงผมตัวละครได้ไหม", "character", ["ห้าม", "ปรับแต่ง"], "tekken8_customization_ban", "policy", "medium"),
        case("Tekken 8 ต้องใช้สกินแบบไหน", "skin", ["สกินมาตรฐาน"], "tekken8_standard_skin", "fact", "medium"),
        case("Tekken 8 ใช้ปุ่ม Assist ได้ไหม", "game_setting", ["อนุญาต", "Assist"], "tekken8_assist_allowed", "policy", "hard"),
        case("Tekken 8 ใช้ bug หรือ glitch ได้ไหม", "penalty", ["ห้าม", "Bug", "Glitch"], "tekken8_bug_glitch_ban", "policy", "medium"),
        case("Tekken 8 เมื่อเริ่มเกมแล้ว pause ได้ไหม", "pause", ["ห้าม", "หยุดเกม"], "tekken8_pause_ban_after_start", "policy", "medium"),
        case("Tekken 8 ตั้งใจกด pause โดนอะไร", "pause", ["ปรับแพ้ 1 รอบ"], "tekken8_pause_penalty", "policy", "medium"),
        case("Tekken 8 กดหยุดเกมได้ในกรณีไหน", "pause", ["ยินยอม", "อุปกรณ์ขัดข้อง", "เหตุฉุกเฉิน"], "tekken8_allowed_pause_case", "policy", "hard"),
        case("Tekken 8 ถ้าออกจากเกมก่อนจบโดยไม่ได้รับอนุญาตโดนอะไร", "penalty", ["ปรับแพ้ทันที"], "tekken8_leave_game_penalty", "policy", "medium"),
        case("Tekken 8 หยุดเกมโดยไม่จำเป็นลงโทษเหมือนอะไร", "pause", ["ออกจากเกมก่อนจบ"], "tekken8_unnecessary_pause", "policy", "hard"),
        case("Tekken 8 เยาะเย้ยหรือไม่สุภาพต่อคู่แข่งโดนอะไร", "penalty", ["ปรับแพ้ทันที"], "tekken8_bad_manner_penalty", "policy", "medium"),
        case("Tekken 8 ดูถูกผู้ตัดสินหรือผู้เข้าแข่งคนอื่นได้ไหม", "penalty", ["ห้าม", "ปรับแพ้ทันที"], "tekken8_respect_rule", "policy", "medium"),
        case("Tekken 8 ผู้เข้าแข่งขันต้องยอมรับอะไรเกี่ยวกับคำตัดสิน", "policy", ["คำตัดสิน", "กรรมการ"], "tekken8_accept_decision", "policy", "medium"),
        case("ผู้จัด Tekken 8 เปลี่ยนกฎได้ไหม", "policy", ["ปรับเปลี่ยนกฎ", "ไม่ต้องแจ้ง"], "tekken8_rule_change", "policy", "hard"),
        case("Tekken 8 คำตัดสินของกรรมการถือว่าอย่างไร", "policy", ["ถือเป็นที่สิ้นสุด"], "tekken8_final_decision", "policy", "medium"),
        case("Tekken 8 ถ้าเกิดข้อโต้แย้งต้องฟังคำตัดสินใคร", "dispute", ["ผู้ดูแล", "กรรมการ"], "tekken8_dispute_decision", "policy", "medium"),
        case("Tekken 8 หากเกิดปัญหาใดๆ ต้องแจ้งใคร", "dispute", ["ผู้จัดการแข่งขัน", "ทันที"], "tekken8_report_problem", "policy", "medium"),
        case("Tekken 8 สรุปรูปแบบการแข่งขันแบบสั้นๆ", "summary", ["ออฟไลน์", "PlayStation 5", "1v1", "FT2"], "tekken8_format_summary", "summary", "hard"),
        case("Tekken 8 สรุปกฎตัวละครและสกิน", "summary", ["DLC", "ปรับแต่ง", "สกินมาตรฐาน"], "tekken8_character_summary", "summary", "hard"),
        case("Tekken 8 สรุปกฎ pause แบบเข้าใจง่าย", "summary", ["Pause", "ยินยอม", "ปรับแพ้"], "tekken8_pause_summary", "summary", "hard"),
        case("Tekken 8 รอบละ 60 วิและ R3 หมายถึงอะไร", "game_setting", ["3 รอบ", "60 วินาที"], "tekken8_r3_timer", "fact", "hard"),
        case("Tekken 8 ใช้ PS5 กับ Stage Random ใช่ไหม", "game_setting", ["PlayStation 5", "Random"], "tekken8_platform_stage", "fact", "medium"),
        case("Tekken 8 ถามว่าแข่งกี่เกมควรตอบว่าอะไร", "format", ["FT2", "ชนะครบ 2 เกม"], "tekken8_match_count", "fact", "hard"),
        case("Tekken 8 ใช้ customization เอฟเฟกต์หรือออร่าได้ไหม", "character", ["ห้าม", "เอฟเฟกต์", "ออร่า"], "tekken8_effect_aura_ban", "policy", "hard"),
        case("Tekken 8 เหตุผลด้านอุปกรณ์ขัดข้องสามารถ pause ได้ไหม", "pause", ["อุปกรณ์ขัดข้อง", "ยินยอม"], "tekken8_hardware_pause", "policy", "medium"),
        case("Tekken 8 เหตุฉุกเฉินใช้เป็นเหตุผล pause ได้ไหม", "pause", ["เหตุฉุกเฉิน"], "tekken8_emergency_pause", "policy", "medium"),
        case("Tekken 8 กติกาบอกว่าผู้จัดขอสงวนสิทธิ์อะไร", "policy", ["เปลี่ยนแปลง", "กฎระเบียบ"], "tekken8_reserved_right", "policy", "hard"),
        case("Tekken 8 ถ้าฝ่าฝืนมารยาทมีข้อยกเว้นไหม", "penalty", ["ไม่มีข้อยกเว้น", "ปรับแพ้"], "tekken8_no_exception_manners", "policy", "hard"),
        case("Tekken 8 เลือกตัวละคร DLC ไม่ได้แต่ใช้ Assist ได้ใช่ไหม", "character", ["DLC", "Assist"], "tekken8_dlc_assist_combo", "fact", "hard"),
        case("Tekken 8 ต้องเล่นบนแพลตฟอร์มอะไรและเป็นเดี่ยวไหม", "format", ["PlayStation 5", "เดี่ยว", "1v1"], "tekken8_platform_1v1", "fact", "medium"),
    ],
}


def enrich_cases(game_key: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    meta = GAME_META[game_key]
    enriched: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    for index, row in enumerate(rows, 1):
        question = row["question"].strip()
        if question in seen_questions:
            raise ValueError(f"Duplicate question in {game_key}: {question}")
        seen_questions.add(question)
        item = {
            "id": f"competition_{meta['prefix']}_v2_{index:03d}",
            "category": row["category"],
            "game": meta["game"],
            "intent": row["intent"],
            "question": question,
            "expected_keywords": row["expected_keywords"],
            "expected_source_keywords": [meta["source"]],
            "answer_type": row["answer_type"],
            "difficulty": row["difficulty"],
            "variant_type": row["variant_type"],
            "source_fact_key": row["source_fact_key"],
            "expected_mode_prefix": row["expected_mode_prefix"],
        }
        enriched.append(item)
    return enriched


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_report(outputs: dict[str, list[dict[str, Any]]], combined_path: Path) -> str:
    lines = [
        "# Competition Ground Truth By Game V2",
        "",
        "ชุดนี้สร้างเพื่อทดสอบคำถามกติกาการแข่งขันแบบแยกเกม โดยเน้นความหลากหลายของ intent มากกว่าการ paraphrase คำถามเดิมซ้ำหลายรอบ",
        "",
        "## Files",
        "",
    ]
    total = 0
    for game_key, rows in outputs.items():
        meta = GAME_META[game_key]
        total += len(rows)
        path = OUT_DIR / meta["filename"]
        lines.append(f"- `{meta['game']}`: `{path}` ({len(rows)} ข้อ)")
    lines.append(f"- รวมทุกเกม: `{combined_path}` ({total} ข้อ)")
    lines.extend(["", "## Intent Distribution", ""])
    for game_key, rows in outputs.items():
        meta = GAME_META[game_key]
        counter = Counter(row["intent"] for row in rows)
        lines.append(f"### {meta['game']}")
        for intent, count in counter.most_common():
            lines.append(f"- `{intent}`: {count}")
        lines.append("")
    lines.extend([
        "## Design Notes",
        "",
        "- คำถามที่มีความหมายใกล้กันมากถูกจำกัดไว้ประมาณ 2-3 ข้อต่อ fact สำคัญ",
        "- เพิ่มคำถามแบบสรุปหลายประเด็น เพื่อทดสอบว่าระบบตอบรวมหลาย fact ได้หรือไม่",
        "- เพิ่มคำถามเชิง policy เช่น `ได้ไหม`, `โดนอะไร`, `ควรตอบว่าอะไร` เพื่อทดสอบคำตอบที่ต้องไม่มั่ว",
        "- ใช้ `expected_keywords` แบบพอเหมาะ ไม่ล็อกยาวเกินไป แต่ยังบังคับให้คำตอบต้องมีแก่นข้อมูลจริง",
        "- ใช้ `expected_source_keywords` เป็น document id ของเกม เพื่อให้ตัวตรวจจับว่าดึงเอกสารเกมถูกหรือไม่",
        "",
        "## Next Check",
        "",
        "รันตรวจด้วย:",
        "",
        "```powershell",
        "py -3 tools\\run_ground_truth_pipeline_eval.py --ground-truth data\\ground_truth\\competition_by_game_v2\\ground_truth_competition_all_games_v2_diverse.jsonl --label competition_by_game_v2_all",
        "```",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    outputs: dict[str, list[dict[str, Any]]] = {}
    all_rows: list[dict[str, Any]] = []
    for game_key, rows in CASES.items():
        enriched = enrich_cases(game_key, rows)
        outputs[game_key] = enriched
        all_rows.extend(enriched)
        write_jsonl(OUT_DIR / GAME_META[game_key]["filename"], enriched)

    combined_path = OUT_DIR / "ground_truth_competition_all_games_v2_diverse.jsonl"
    write_jsonl(combined_path, all_rows)
    REPORT_PATH.write_text(build_report(outputs, combined_path), encoding="utf-8", newline="\n")

    print(f"Wrote {len(all_rows)} total cases")
    for game_key, rows in outputs.items():
        print(f"- {GAME_META[game_key]['game']}: {len(rows)}")
    print(REPORT_PATH)
    print(combined_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
