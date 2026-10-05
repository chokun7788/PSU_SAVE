"""Build an assistant-source-reviewed candidate from preserved drafts.

The root assistant read Thai/English pairs by category, corrected the entries
below and reviewed headings independently. AI audit verdicts alone do not admit
content. No invented person transliterations or repairs to Thai owner policy.
"""
from __future__ import annotations
import json
import re
import sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.review_english_r21_20261001 import MANUAL, read
from tools.manage_english_localizations import source_fields, validate_candidate
from app.knowledge.localization import source_text_sha256

CS='competition_rules_cs2_psu_phuket_2026_'
VAL='competition_rules_valorant_psu_phuket_2026_'
ROV='competition_rules_rov_blueket_2025_men_'
TK='competition_rules_tekken8_psu_esports_'
FIX={
 (CS+'s15_c01','text'): 'Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified.',
 (CS+'s24_c01','text'): 'Round time: 1:55 minutes | Freeze time: 15 seconds',
 (CS+'s26_c01','text'): 'Maximum of 24 rounds (12 rounds per side). The winner is the first team to win 13 rounds.',
 (CS+'s28_c01','text'): 'Competition maps',
 (CS+'s32_c01','text'): 'Side selection: a knife round is used to choose sides.',
 (CS+'s34_c01','text'): 'Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.',
 (CS+'s36_c01','text'): 'Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.',
 (CS+'s37_c01','text'): 'Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification.',
 (CS+'s42_c01','text'): 'Players are responsible for the quality and readiness of their own equipment.',
 (CS+'s58_c01','text'): 'Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.',
 (VAL+'s03_c01','text'): 'Pre-game procedure through agent selection\n* Check-in: arrive at least 30 minutes before the scheduled match time.\n* New agents may not be used for approximately 2 weeks after release in Competitive mode.\n* New maps may not be used for approximately 4 weeks after release in Competitive mode.\n* Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited.\n* Map pool: Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset (7 maps).\n* Side selection uses a coin toss.\n* Ban maps until 3 remain.',
 (VAL+'s04_c01','text'): 'Post-match procedure\n* Officials confirm and record the result immediately.\n* If a forfeit is imposed, the result for that map is recorded as 13-0.\nGame pauses',
 (VAL+'s06_c01','text'): '1. Tactical Timeout\n* 2 requests per map during regulation (first 24 rounds), 60 seconds each.\n* In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.',
 (VAL+'s09_c01','text'): "Using player-caused bugs to gain an unintended advantage is an offense.\n* Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.\n* Abilities must not be used outside map boundaries to obtain information or an advantage.\n* Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid.\n* Using teammates to jump higher than the normal jump range is prohibited.\nPenalties\nOfficials assess penalties according to Intent and Impact.",
 (TK+'s04_c01','text'): 'Game settings\n* Rounds per game (Round): 3\n* Time per round (Timer): 60 seconds\n* Advantage: No advantage\n* Stage: Random',
 (TK+'s05_c01','text'): 'Competition etiquette\n* Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.\n* Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.',
 (TK+'s06_c01','text'): "Agreements and conduct\n* Competitors must accept and follow the rules, regulations, and referees' decisions unconditionally.\n* Organizers may change competition rules at any time without prior notice.\n* Referees' decisions are final.\n* Referees may reconsider decisions as appropriate to ensure fairness.",
 (ROV+'s03_c01','text'): '1. Competition schedule\n1.1. Offline competition on 11 September 2025 (B.E. 2568).\n* 08:00-08:30: registration\n* 08:30-08:40: bracket allocation\n* 08:40-10:00: round of 5 teams, Single Elimination BO3\n* 10:00-11:30: semifinal match 1, Single Elimination BO3\n* 12:30-14:00: semifinal match 2, Single Elimination BO3\n* 14:00-15:30: third-place match, Single Elimination BO3\n* 15:30-17:00: final, Single Elimination BO3',
 (ROV+'s07_c01','text'): '5. Competition attire and equipment\n5.1. Personal mobile phones and personal internet and/or university internet.\n5.2. Personal power strips and battery-charging equipment.\n5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.',
 ('curated_games_ps5','text'): 'Games listed for PlayStation 5 include Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts Legacy, Marvel’s Spider-Man 2, Naruto X Boruto Ultimate Ninja Storm Connections, Resident Evil 4, Resident Evil Village, TEKKEN 8, THE FINALS, The Last of Us Part I, The Last of Us Part II Remastered and Uncharted: Legacy of Thieves Collection.',
 ('curated_games_vr','text'): 'The VR Station list includes Beat Saber and Horizon Call of the Mountain.',
 ('equipment_driving_force_shifter','what_th'): 'A gear shifter accessory for a driving wheel setup.',
 ('equipment_gaming_mouse','how_to_use_th'): 'Use with the reserved PC. Notify staff if clicks do not register, the sensor malfunctions, or any damage is found.',
 ('equipment_racezone_cockpit_v3','what_th'): 'A racing simulator seat and frame for racing games.',
 ('equipment_tv_86','what_th'): 'An 86-inch TV for playing Nintendo Switch games as a group.',
 ('equipment_playstation_5_slim','how_to_use_th'): 'Book PlayStation 5 Zone or VR Zone for the desired service, then play the games provided by the center during the booked time slot.',
 ('game_detail_beat_saber','summary_th'): 'Beat Saber is a VR rhythm game in which players use light swords to slash blocks in time with the music.',
 ('game_detail_cs2','summary_th'): 'Counter-Strike 2 is a competitive team shooter with attackers and defenders. The main objectives involve planting/defusing a bomb or eliminating opponents.',
 ('game_detail_fortnite','how_to_play_th'): 'Collect weapons, move with the circle, fight other players, and use building or no-build play according to the selected mode.',
 ('game_detail_fortnite','summary_th'): 'Fortnite is a survival combat game in which players compete on a large map and try to be the last person standing.',
 ('game_detail_gran_turismo_7','how_to_play_th'): 'In Cockpit Zone, use the steering wheel, accelerator, brake and driving simulator seat. Aim to drive quickly and control the car accurately on each track.',
 ('game_detail_league_of_legends','genre'): 'Team-based 5v5 MOBA game',
 ('game_detail_luigis_mansion_3','summary_th'): "Luigi's Mansion 3 is a ghost-catching adventure game in which players explore a hotel and solve puzzles.",
 ('game_detail_pubg','summary_th'): 'PUBG: BATTLEGROUNDS is a survival game in which players enter the battlefield, find weapons and equipment, and try to be the last person or team standing.',
 ('game_detail_ring_fit_adventure','how_to_play_th'): 'Attach the Joy-Con to the Ring-Con, then perform exercises such as running, squeezing, pushing or stretching to attack and complete stages.',
 ('game_detail_spider_man_2','how_to_play_th'): 'Swing on webs to travel, complete missions, use combat combos, dodge and upgrade skills as the story progresses.',
 ('game_detail_super_mario_odyssey','how_to_play_th'): 'Run, jump, use the Cappy hat to capture/control some things, and explore locations to collect objectives.',
 ('game_detail_switch_sports','genre'): 'Motion control sports game',
 ('game_detail_uncharted','summary_th'): 'Uncharted is a treasure-hunting adventure game focused on climbing, exploration, puzzle solving and action scenes.',
 ('game_detail_uncharted','how_to_play_th'): 'Explore locations, climb, solve puzzles, fight with firearms and progress through missions.',
 ('game_detail_valorant','how_to_play_th'): 'Attackers must plant the Spike; defenders must defend the area or defuse the Spike. Play emphasizes aiming, communication, ability use and teamwork.',
 ('game_detail_warzone','how_to_play_th'): 'Land in the area, find weapons, use loadouts/equipment to help the team, move with the circle and try to survive until the game ends.',
 ('curated_contact_location','text'): 'PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1, Wichit Songkhram Road, Kathu District, Phuket 83120.',
 ('curated_overview_identity','text'): 'PSU Esports Studio - Phuket is a center for developing esports learning and excellence and driving the economy in southern Thailand, Phuket branch. It is a gaming and esports learning center of Prince of Songkla University.',
 ('curated_overview_mission','text'): 'The mission of PSU Esports Studio - Phuket is to improve education and excellence in esports through facilities and equipment that support learning for gamers, students and interested people. It was founded by Prince of Songkla University and is operated by the College of Computing.',
 ('curated_payment_bank','text'): 'Pay by bank transfer to Siam Commercial Bank, account name PSU Esports Studio - Phuket, account number 795-276244-1, and attach the transfer slip.',
 ('curated_rule_noise_language','text'): 'Please avoid excessive noise. Insulting or mocking others is prohibited.',
 ('curated_rule_belongings','text'): 'Please leave your belongings before entering to use the service.',
 ('curated_rule_weapons_gambling','text'): 'Carrying weapons or sharp objects is prohibited. Quarrelling or fighting and gambling are prohibited.',
 ('curated_time_change_policy','text'): 'The usage time may be changed by notifying the center at least 1 hour before the booked time. If notice is late or absent, the center reserves the right to provide neither a refund nor compensation for time.',
}
HEADINGS={
 'ภาพรวมเอกสาร':'Document overview', '8. ตารางบทลงโทษ (Penalties)':'8. Penalty table',
 '1. กำหนดการแข่งขัน':'1. Competition schedule','2. สถานที่แข่งขัน':'2. Competition venue',
 '4. ระเบียบและกติกาการแข่งขัน':'4. Competition regulations and rules',
 '5. ชุดแข่งขันและอุปกรณ์การแข่งขัน':'5. Competition attire and equipment',
 '6. การกระทำความผิดและบทลงโทษ':'6. Offenses and penalties',
 'กติกาการแข่งขัน':'Competition rules','ตัวละครและการตั้งค่า':'Characters and settings',
 'การตั้งค่าเกม':'Game settings','มารยาทในการแข่งขัน':'Competition etiquette',
 'ข้อตกลงและข้อปฏิบัติ':'Agreements and conduct','การหยุดเกม':'Game pauses',
 'การแก้ปัญหาข้อพิพาท':'Dispute resolution','พื้นที่การแข่งขันและกฎระเบียบ':'Competition area and regulations',
 'ขั้นตอนตั้งแต่ก่อนเริ่มเกมจนถึงการเลือกตัวละคร':'Pre-game procedure through agent selection',
 'กระบวนการหลังจบแมตช์':'Post-match procedure',
 '1. เวลานอกทางยุทธวิธี (Tactical Timeout)':'1. Tactical Timeout',
 '2. การหยุดเกมทางเทคนิค (Technical Pause)':'2. Technical Pause',
 '3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)':'3. Player Emergency Pause',
 'การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด':'Using player-caused bugs to gain an unintended advantage is an offense.',
 'ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า':'The organizer reserves the right to amend the regulations without prior notice.',
}

def main():
    out=ROOT/'reports/r21_integrated_improvement_20261001/english_final'
    out.mkdir(parents=True,exist_ok=False)
    rows=read(ROOT/'data/locales/en/localization_review_drafts_competition_20260921_repaired.jsonl')
    fields=source_fields(); reviewed={}; held=[]
    # The source clause is truncated and the event name has no verified
    # English form. Do not fill either by guessing.
    held_text={ROV+'s08_c01': 'source_clause_truncated', TK+'s01_c01':'event_name_translation_unverified'}
    for row in rows:
        if row['category']!='competition_rules' or row['field']!='text': continue
        if row['content_id'] in held_text: continue
        source=str(row['source_text'])
        text=FIX.get((row['content_id'],'text'),row['text'])
        if row['content_id']==VAL+'s01_c01':
            text='Competition rules and format for VALORANT\nPSU Phuket VALORANT 2026 Tournament\nUpdate: 17/02/2026\nEnglish below\n'+text.replace('Installing any unauthorized programs','Installing any programs yourself')
        if row['content_id']==VAL+'s16_c01':
            text=HEADINGS[source.split('\n')[0]]+'\n'+source.split('English\n',1)[1]
        if row['content_id']==ROV+'s06_c01':
            text=text.replace('Runes and item bonuses','Runes and enhancement systems')
        if not re.search(r'[\u0e00-\u0e7f]',source):
            text=source  # Preserve authoritative English text and formatting.
        reviewed[source]=text
    reviewed.update(HEADINGS)
    now=datetime.now().astimezone().isoformat(timespec='seconds')
    candidate=[]; review=[]
    for row in rows:
        source=fields[(row['content_id'],row['field'])].get(row['field'])
        source_s=json.dumps(source,ensure_ascii=False) if isinstance(source,list) else str(source)
        text=FIX.get((row['content_id'],row['field']),MANUAL.get(source_s,row['text']))
        reason='assistant_read_source_and_translation'
        if row['field']=='name' and re.search(r'[\u0e00-\u0e7f]',source_s):
            held.append({**row,'reason':'no_verified_romanization'}); continue
        if row['category']=='competition_rules':
            if row['field']=='text' and row['content_id'] in held_text:
                held.append({**row,'reason':held_text[row['content_id']]}); continue
            if source_s in reviewed: text=reviewed[source_s]
            elif not re.search(r'[\u0e00-\u0e7f]',source_s): text=source_s
            elif row['field']=='title' and ': ' in source_s and source_s.split(': ',1)[1] in reviewed:
                label,tail=source_s.split(': ',1); text=label+': '+reviewed[tail]
            else:
                held.append({**row,'reason':'heading_requires_separate_review'}); continue
            reason='assistant_clause_and_condition_review'
        if source_text_sha256(source)!=row['source_text_sha256'] or re.search(r'[\u0e00-\u0e7f]',text):
            raise RuntimeError('Invalid source hash or Thai prose: '+row['content_id'])
        item={**row,'text':text,'status':'approved','version':int(row.get('version',1))+1,
              'approved_by':'codex-assistant-user-authorized-20261001','approved_at':now,
              'review_kind':reason,'human_reviewed':False,'owner_policy_approval':False}
        candidate.append(item)
        review.append({**item,'previous_text':row['text'],'changed':text!=row['text']})
    for filename,items in [('reviewed_candidate.jsonl',candidate),('source_review.jsonl',review),('held.jsonl',held)]:
        with (out/filename).open('x',encoding='utf-8') as stream:
            for item in items: stream.write(json.dumps(item,ensure_ascii=False)+'\n')
    valid,errors=validate_candidate(out/'reviewed_candidate.jsonl',require_approved=True)
    summary={'total':len(rows),'approved_fields':len(valid),'held_fields':len(held),
             'changed_wording':sum(r['changed'] for r in review),'errors':errors,
             'human_reviewed':False,'owner_policy_approval':False}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))
    if errors: raise SystemExit(1)

if __name__=='__main__': main()
