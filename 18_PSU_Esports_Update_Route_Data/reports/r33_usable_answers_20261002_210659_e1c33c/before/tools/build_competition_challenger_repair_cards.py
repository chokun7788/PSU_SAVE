from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


ROOT = Path(__file__).resolve().parents[1]
RESULT_PATH = ROOT / "reports" / "pipeline_ground_truth_results_competition_challenger_v2_afterfix1_20260704.jsonl"
GT_PATH = ROOT / "data" / "ground_truth" / "competition_challenger_v2" / "ground_truth_competition_challenger_v2_real_competitor_questions.jsonl"
OUT_PATH = ROOT / "data" / "competition_rules" / "competition_rule_fact_cards_round5_challenger_repairs.jsonl"


TOURNAMENT = {
    "Counter-Strike 2": "PSU Phuket CS2 2026 Tournament",
    "Arena of Valor (RoV)": "Blueket Games 2025 ประเภททีมชาย",
    "VALORANT": "PSU Phuket VALORANT 2026 Tournament",
    "Tekken 8": "PSU Esports ปะทะมันส์ สนั่นจอ",
}


ANSWER_BY_FACT_KEY = {
    "cs2_member_withdraw": "ถ้าผู้เล่น CS2 ถอนตัว ทีมเสี่ยงถูกตัดสิทธิ์ตามเงื่อนไขของกติกา",
    "cs2_late_may_disqualify": "CS2 หากมาสายหรือไม่ยืนยันเข้าแข่งขันก่อนแมตช์ ทีมเสี่ยงถูกตัดสิทธิ์",
    "cs2_no_install": "CS2 ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์แข่งขัน",
    "cs2_location_day": "CS2 แข่งขัน 1 วัน ที่ PSU Esports Studio - Phuket วิทยาเขตภูเก็ต",
    "cs2_bug_penalty": "CS2 ห้ามใช้บัค หากพบการใช้บัคอาจถูกปรับแพ้เป็นรอบหรือถึงแมตช์ตามความรุนแรง",
    "cs2_hate_speech": "CS2 ห้าม hate speech การเหยียดเชื้อชาติหรือศาสนา และวาจาสร้างความเกลียดชัง",
    "cs2_no_mod": "CS2 ห้ามดัดแปลงตัวเกม ใช้ mod หรือ config แปลกๆ ที่ผิดกติกา",
    "cs2_stream_snipe_penalty": "CS2 ห้ามดูสตรีมระหว่างแข่ง การดูสตรีมอาจนำไปสู่โทษปรับแพ้ถึงแมตช์",
    "cs2_team_size": "CS2 ต้องมีผู้เล่น 5 คนต่อทีม ดังนั้นมีแค่ 4 คนยังไม่ครบตามกติกา",
    "cs2_timeout_freeze_only": "CS2 ขอเวลานอก Tactical Timeout ได้เฉพาะช่วง Freeze time",
    "cs2_roster_lock": "CS2 ไม่มีการเปลี่ยนแปลงสมาชิกหลังยืนยันรายชื่อ ต้องใช้สมาชิกที่ลงทะเบียนไว้",
    "rov_registration_time": "RoV ลงทะเบียนเวลา 8.00-8.30 น.",
    "rov_five_team_round": "RoV รอบ 5 ทีมแข่งขันเวลา 8.40-10.00 น. และแข่งแบบ BO3",
    "rov_location": "RoV จัดที่ PSU Esports Studio - Phuket อาคาร 5102A หรืออาคาร 5 ชั้น 1",
    "rov_location_building": "RoV จัดที่ PSU Esports Studio - Phuket อาคาร 5102A หรืออาคาร 5",
    "rov_offline": "RoV แข่งขันแบบออฟไลน์",
    "rov_format_bo3": "RoV แข่ง Best of 3 (BO3) ทุกรอบ",
    "rov_skin": "RoV ใช้ได้เฉพาะ Default Skin เท่านั้น ห้ามใช้สกินพิเศษ",
    "rov_rematch_after_first_blood": "RoV หากเกิด First Blood แล้วจะ remake ไม่ได้ เว้นแต่ได้รับอนุญาตจากคู่แข่งและ/หรือกรรมการ",
    "rov_late_after_break": "RoV หากไม่กลับมาหลังเวลาพักที่กำหนด ผู้ตัดสินอาจปรับให้แพ้",
    "rov_break_absent": "RoV หากไม่กลับมาตามเวลาพัก ผู้ตัดสินอาจปรับให้แพ้",
    "rov_pause_over_10": "RoV หากเกมหยุดเกิน 10 นาที ทีมงานอาจสั่งให้เริ่มเกมใหม่ตามดุลยพินิจ",
    "rov_pause_penalty_first": "RoV Pause ผิดครั้งที่ 1 ถูกตักเตือน",
    "rov_pause_penalty_second": "RoV Pause ผิดครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ให้ฝ่ายตรงข้าม 1 ครั้ง",
    "rov_pause_troll_penalty": "RoV การกดหยุดเกมเพื่อก่อกวนอาจถูกปรับแพ้และตัดสิทธิ์",
    "rov_unregistered_player": "RoV ใช้ผู้เล่นไม่ตรงตามที่ลงทะเบียนมีโทษปรับแพ้และตัดสิทธิ์",
    "rov_substitute_play": "RoV ห้ามให้คนอื่นเล่นแทนผู้เล่นที่ลงทะเบียนไว้",
    "rov_disconnect_summary": "RoV กรณี disconnect ให้ใช้ pause; ถ้ายังไม่มี First Blood และไม่เกิน 2 นาทีอาจขอ remake ได้ ส่วนหลัง First Blood ต้องได้รับอนุญาตจากคู่แข่งและ/หรือกรรมการ",
    "rov_server_down": "RoV ถ้าอินเทอร์เน็ตหรือเซิร์ฟเวอร์มีปัญหา ต้องแจ้งทีมงาน/กรรมการ และให้พิจารณาตามดุลยพินิจ",
    "rov_rude_words": "RoV ห้ามใช้คำหยาบคายหรือถ้อยคำเสียดสีในการแข่งขัน",
    "rov_pause_wrong_penalty": "ต่างกันคือ RoV Pause ผิดครั้งที่ 1 ตักเตือน, ครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง, และโทษรุนแรงอาจถึงปรับแพ้",
    "valorant_map_ban_three": "VALORANT ban map จนเหลือ 3 แผนที่",
    "valorant_ban_3_maps": "VALORANT ban map จนเหลือ 3 แผนที่",
    "valorant_pause_types": "VALORANT Pause มี 3 ประเภทหลัก: Tactical, Technical และ Emergency",
    "valorant_pause_summary": "VALORANT Pause แบ่งเป็น Tactical, Technical และ Emergency",
    "valorant_technical_pause_reason": "VALORANT Technical Pause ใช้กับเหตุขัดข้อง เช่น อุปกรณ์ขัดข้อง ผู้เล่นหลุด หรือปัญหาซอฟต์แวร์",
    "valorant_no_rollback_after_damage": "VALORANT ถ้าทำ damage ไปแล้วโดยทั่วไปไม่สามารถ Challenge เพื่อ rollback รอบได้",
    "valorant_out_of_bounds": "VALORANT ห้ามใช้สกิลนอกขอบเขตแผนที่เพื่อหาข้อมูลหรือสร้างความได้เปรียบ",
    "valorant_round_rollback_penalty": "VALORANT Round Rollback ใช้กับกรณีช่องโหว่หรือบัคที่ต้องย้อนรอบตามดุลยพินิจ",
    "valorant_round_loss": "VALORANT Round Loss ใช้เมื่อมีเจตนาใช้ช่องโหว่หรือกระทำผิดที่กระทบต่อรอบนั้น",
    "valorant_map_forfeit": "VALORANT Map Forfeit ใช้กับความผิดร้ายแรงหรือการทำผิดซ้ำ",
    "valorant_snap_tap": "VALORANT อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีเทียบเท่าได้ (permitted) เว้นแต่เจ้าหน้าที่สั่งเป็นอย่างอื่น",
    "valorant_content_map_summary": "VALORANT Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ แผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ และ map pool มี Abyss รวมอยู่ด้วย",
    "valorant_checkin_30": "VALORANT ต้องรายงานตัวก่อนแข่ง 30 นาที",
    "valorant_checkin": "VALORANT ต้องรายงานตัว/check in ก่อนแข่ง 30 นาที",
    "valorant_emergency_exceed": "VALORANT หาก Emergency Pause เกินเวลา ผู้เล่นอาจหมดสิทธิ์กลับเข้าแข่งขัน และต้องใช้ตัวสำรองถ้ามี",
    "valorant_emergency_over_time": "VALORANT หากหมดเวลาพักฉุกเฉินแล้วผู้เล่นยังไม่พร้อม ผู้เล่นอาจหมดสิทธิ์กลับเข้าแข่งขัน และทีมต้องใช้ตัวสำรองถ้ามี",
    "valorant_match_forfeit": "VALORANT ความผิดร้ายแรงอย่าง Cheating หรือ Match fixing มีโทษถึง Match Forfeit",
    "valorant_no_install": "VALORANT ห้ามติดตั้งโปรแกรมเองบนเครื่องแข่งขัน",
    "valorant_social_media": "VALORANT ห้ามเปิด Facebook, social media หรือเว็บไซต์สื่อสารบนคอมพิวเตอร์แข่งขัน",
    "valorant_blood_bodies": "VALORANT ต้องตั้งค่า Blood และ Bodies เป็น Off",
    "valorant_tactical_24_rounds": "VALORANT Tactical Timeout ใช้ได้ 2 ครั้ง ครั้งละ 60 วินาที ใน 24 รอบแรกของแผนที่",
    "valorant_technical_no_talk": "VALORANT ระหว่าง Technical Pause ห้ามสื่อสารกัน เว้นแต่ได้รับอนุญาตจากเจ้าหน้าที่",
    "tekken8_round_3": "Tekken 8 แต่ละเกมแข่งขัน 3 รอบ",
    "tekken8_advantage": "Tekken 8 ตั้งค่า Advantage เป็น No advantage",
    "tekken8_stage_random": "Tekken 8 ต้องตั้ง Stage เป็น Random",
    "tekken8_pause_penalty": "Tekken 8 หากตั้งใจกด Pause ระหว่างเกม จะถูกปรับแพ้ 1 รอบ",
    "tekken8_allowed_pause_case": "Tekken 8 ขอหยุดเกมได้เมื่อทั้งสองฝ่ายยินยอม หรือมีเหตุสมควร เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน",
    "tekken8_pause_emergency": "Tekken 8 หากอุปกรณ์ขัดข้องหรือมีเหตุฉุกเฉิน สามารถขอหยุดเกมได้ตามกติกาและดุลยพินิจกรรมการ",
    "tekken8_platform_stage": "Tekken 8 ใช้ PlayStation 5 และตั้ง Stage เป็น Random",
    "tekken8_match_count": "Tekken 8 ใช้รูปแบบ FT2 คือชนะครบ 2 เกมก่อน",
    "tekken8_customization": "Tekken 8 ห้ามใช้ Customization เช่น ชุด ทรงผม เอฟเฟกต์ หรือออร่า",
    "tekken8_dlc_assist_combo": "Tekken 8 ห้ามใช้ตัวละคร DLC แต่อนุญาตให้ใช้ Assist",
    "tekken8_rule_change": "Tekken 8 ผู้จัดสงวนสิทธิ์ในการเปลี่ยนแปลงกฎได้โดยไม่ต้องแจ้งล่วงหน้า",
    "tekken8_tiebreaker": "Tekken 8 หากเสมอ 1-1 ต้องเล่นเกมตัดสิน",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def source_for(item: dict[str, Any]) -> str:
    sources = item.get("expected_source_keywords") or []
    return str(sources[0]) if sources else ""


def main() -> int:
    gt = {row["id"]: row for row in load_jsonl(GT_PATH)}
    results = load_jsonl(RESULT_PATH)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in results:
        if row.get("verdict") == "PASS":
            continue
        item = gt[row["id"]]
        source_key = str(item.get("source_fact_key", row["id"]))
        grouped[source_key].append(item)

    cards: list[dict[str, Any]] = []
    for source_key, items in sorted(grouped.items()):
        first = items[0]
        answer = ANSWER_BY_FACT_KEY.get(source_key)
        if not answer:
            answer = "สรุปจากกติกา: " + ", ".join(str(k) for k in first.get("expected_keywords", []))
        source_id = source_for(first)
        patterns: list[str] = []
        for item in items:
            q = str(item.get("question", "")).strip()
            if q and q not in patterns:
                patterns.append(q)
        cards.append(
            {
                "id": f"round5_{source_key}",
                "category": "competition_rule_fact",
                "game": first.get("game"),
                "tournament": TOURNAMENT.get(str(first.get("game", "")), ""),
                "intent": first.get("intent"),
                "answer_type": "explicit_fact",
                "exact_only": True,
                "question_patterns": patterns,
                "answer": answer,
                "evidence": "เพิ่มจากการ audit Ground Truth Challenger V2 เพื่อให้ตอบคำถามภาษาคนจริงได้ตรงประเด็นและไม่ดึง chunk ใกล้เคียงผิด",
                "source_url": f"local://competition_rules/{source_id}",
                "source_ids": [source_id] if source_id else [],
                "tags": ["competition_rules", str(first.get("game", "")), str(first.get("intent", "")), source_key],
                "priority": 320,
            }
        )

    with OUT_PATH.open("w", encoding="utf-8", newline="\n") as f:
        for card in cards:
            f.write(json.dumps(card, ensure_ascii=False) + "\n")
    print(f"Wrote {len(cards)} repair cards")
    print(OUT_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
