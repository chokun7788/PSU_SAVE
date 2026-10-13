"""Source-bound price tables with explicit scope, group and coverage contracts."""
from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import date, datetime
from pathlib import Path

from app.calculator.service_fee import SERVICE_FEES, GROUP_LABELS
from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID, make_source_hits
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, ValidationResult
from app.session.conversation_plan import GROUPS, SERVICE_LABELS, valid_price_task
from app.calendar.service_calendar import today_bangkok

GROUP_EN = {'psu_student_staff': 'PSU students and staff', 'general_student': 'PSU alumni / students from other institutions', 'general_adult': 'General adults'}


def price_release() -> str:
    return hashlib.sha256(json.dumps(SERVICE_FEES, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def recorded_expiry() -> date | None:
    p = Path(__file__).resolve().parents[2] / 'data/curated/curated_facts_service_fee_2026_aliases.jsonl'
    if not p.exists():
        return None
    for line in p.read_text(encoding='utf-8').splitlines():
        row = json.loads(line)
        if row.get('id') == 'curated_service_fee_2026_full_table':
            dates = re.findall(r'\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}', row.get('text',''))
            return datetime.strptime(dates[-1], '%d %B %Y').date() if dates else None
    return None


def expected_packages(task: dict) -> list[str]:
    keys = []
    for service in task['targets']:
        filters = {**task['filters'], **{k:v for k,v in task.get('per_target_filters',{}).get(service,{}).items() if v is not None}}
        minutes, people = filters.get('duration_minutes'), filters.get('people_count')
        for key in SERVICE_FEES:
            if not (key == service or key.startswith(service+'_')):
                continue
            if service == 'vr' and minutes is not None and key != ('vr_30' if minutes <= 30 else 'vr_60'):
                continue
            if service == 'nintendo_switch' and people is not None:
                if people not in range(1,5) or key != ('nintendo_switch_1_2' if people <= 2 else 'nintendo_switch_3_4'):
                    continue
            capacity_numbers = [int(n) for n in re.findall(r'\d+', SERVICE_FEES[key]['capacity'])]
            if people is not None and capacity_numbers and people > max(capacity_numbers):
                continue
            keys.append(key)
    return list(dict.fromkeys(keys))


def coverage_errors(expected: list[str], returned: list[str]) -> list[str]:
    errors = []
    missing = sorted(set(expected)-set(returned))
    extra = sorted(set(returned)-set(expected))
    if missing:
        errors.append('conversation_coverage_missing:'+','.join(missing))
    if extra:
        errors.append('conversation_scope_extra:'+','.join(extra))
    return errors


def build_price_plan_answer(plan: dict, locale: str = 'th') -> dict | None:
    tasks = plan.get('tasks', [])
    english = locale == 'en'
    task = tasks[0] if tasks else None
    if not task or not valid_price_task(task):
        if plan.get('missing') == 'scope':
            answer = 'All of which topic or service would you like to see?' if english else 'ต้องการดูทั้งหมดของเรื่องหรือบริการใดครับ?'
            return {'answer':answer,'hits':[],'mode':'pipeline:conversation_scope_clarification','route':PipelineRoute('clarification','conversation_scope_missing',.95,'clarification','low','no active scope'), 'entities':EntityBundle(), 'validation':ValidationResult(True), 'metadata':{'outcome':'clarification_required','request_plan':plan}, 'trace':[]}
        return None
    if plan.get('needs_review'):
        answer = ('I am still answering your price question. Which service do you mean: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can choose all services.' if english else 'กำลังคุยเรื่องราคาอยู่ครับ ข้อความล่าสุดหมายถึงบริการใด: PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR? เลือกทุกบริการได้ครับ')
        return {'answer':answer,'hits':[],'mode':'pipeline:conversation_choice_clarification','route':PipelineRoute('clarification','price_choice_unresolved',.95,'clarification','low','reply did not select a verified option'), 'entities':EntityBundle(price_intent=True), 'validation':ValidationResult(True, warnings=('dialogue_choice_unresolved',)), 'metadata':{'outcome':'clarification_required','request_plan':plan}, 'trace':[]}
    if task.get('pending_slots'):
        answer = ('Which service would you like the prices for: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can also choose all services.' if english else
                  'ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ')
        return {'answer':answer,'hits':[],'mode':'pipeline:protected_price_missing_service','route':PipelineRoute('clarification','price_missing_service',.98,'clarification','low','service selection is pending'), 'entities':EntityBundle(price_intent=True), 'validation':ValidationResult(True), 'metadata':{'outcome':'clarification_required','request_plan':plan}, 'trace':[]}
    groups = task['filters'].get('customer_group_ids') or list(GROUPS)
    if task['filters'].get('customer_scope') == 'non_student_unspecified':
        groups = ['psu_student_staff', 'general_adult']
    packages = expected_packages(task)
    missing_targets = [s for s in task['targets'] if not any(k == s or k.startswith(s+'_') for k in packages)]
    expected = [f'{key}:{group}' for key in packages for group in groups]
    labels = GROUP_EN if english else {**GROUP_LABELS,'psu_student_staff':GROUP_LABELS['psu_student_staff']+' (PSU Student and Staff)'}
    lines = ['Service prices (recorded package rates):' if english else 'ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:']
    if task['filters'].get('customer_scope') == 'external_unspecified':
        lines.append('External users have different rates depending on their eligibility; both relevant groups are shown below.' if english else 'ผู้ใช้ภายนอกมีอัตราต่างกันตามคุณสมบัติ จึงแสดงกลุ่มผู้เรียนต่างสถาบันและบุคคลทั่วไปให้เทียบครับ')
    rows=[]
    for key in packages:
        fee = SERVICE_FEES[key]
        service = next(s for s in task['targets'] if key == s or key.startswith(s+'_'))
        filters={**task['filters'],**{k:v for k,v in task.get('per_target_filters',{}).get(service,{}).items() if v is not None}}
        minutes=filters.get('duration_minutes')
        sessions=max(1,math.ceil(minutes/fee['minutes_per_session'])) if minutes else 1
        capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people').strip()) if english else fee['capacity']
        lines.append(f"\n{fee['label']} — {fee['minutes_per_session']} "+('minutes/package' if english else 'นาที/แพ็กเกจ')+f' ({capacity})')
        if minutes is not None:
            hours = f'{minutes/60:g}'
            lines.append(f'Requested duration: {minutes} minutes ({hours} hours); {sessions} session(s).' if english else
                         f'ระยะเวลาที่ถาม {minutes} นาที ({hours} ชั่วโมง) คิดเป็น {sessions} session (แพ็กเกจ)')
        for group in groups:
            unit=fee['prices'][group]
            suffix=(f' × {sessions} = {unit*sessions:,} '+('THB' if english else 'บาท')) if sessions>1 else ''
            lines.append(f"• {labels[group]}: {unit:,} "+('THB/package' if english else 'บาท/แพ็กเกจ')+suffix)
            rows.append({'id':f'{key}:{group}','package_id':key,'group_id':group,'unit_price':unit,'sessions':sessions,'total':unit*sessions})
    if missing_targets:
        lines.append('The requested player count does not match a recorded package. Please specify the number of devices or ask staff for a suitable package.' if english else 'จำนวนผู้เล่นที่ถามไม่ตรงกับแพ็กเกจที่บันทึกไว้ กรุณาระบุจำนวนเครื่องหรือสอบถามเจ้าหน้าที่เรื่องแพ็กเกจที่เหมาะสมครับ')
        lines.append(('Services needing clarification: ' if english else 'บริการที่ยังต้องระบุเพิ่ม: ')+', '.join(SERVICE_LABELS[s] for s in missing_targets))
    if 'psu_student_staff' in groups and task['filters'].get('customer_scope') == 'non_student_unspecified':
        lines.append('The PSU rate requires PSU staff eligibility; being a non-student alone does not establish eligibility.' if english else 'อัตรา PSU ต้องมีคุณสมบัติบุคลากร PSU การระบุว่าไม่ใช่นักศึกษาอย่างเดียวยังไม่ยืนยันสิทธิ์ครับ')
    sources=[PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if packages and all(k=='pc' for k in packages) else ([SERVICE_FEE_IMAGE_2026_ID]+([PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID] if 'pc' in packages else []))
    hits=make_source_hits(sources) if packages else []
    expiry=recorded_expiry() if any(k!='pc' for k in packages) else None
    temporal='recorded_rates'
    if expiry:
        temporal='source_not_current' if expiry < today_bangkok() else 'recorded_rates'
        lines.append((f'The original fee table states validity through {expiry.isoformat()}; continued validity for the requested date has not been confirmed.' if english else f'ตารางต้นฉบับระบุมีผลถึง {expiry.isoformat()} ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ'))
    if 'pc' in packages:
        lines.append('PC rates use the local update dated 2026-07-27.' if english else 'ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27')
    for source in hits:
        url=source.get('metadata',{}).get('source_url','')
        if url:
            lines.append(('Source: ' if english else 'แหล่งข้อมูล: ')+url)
    task_outcomes=[{'task_id':task['task_id'],'outcome':'answered_partial' if packages and missing_targets else 'answered_complete' if packages else 'clarification_required'}]
    for extra in tasks[1:]:
        if extra.get('domain')=='reservation' and extra.get('operation')=='how_to':
            from app.pipeline.structured_tools import _reservation_answer
            from app.pipeline.schemas import UniversalIntent
            if english:
                from app.pipeline.bilingual_english import _rule_answer
                from app.rules.matcher import RuleMatcher
                matcher = RuleMatcher.default()
                booking = _rule_answer('How do I make a booking?', matcher, category='reservation')
                deadline = _rule_answer('payment timeout', matcher, category='reservation')
            else:
                booking=_reservation_answer('วิธีจอง', UniversalIntent('reservation','how_to'))
            if booking:
                lines.append('\n'+('Booking steps:\n' if english else 'วิธีจอง:\n')+booking.answer)
                hits.extend(booking.hits)
                if english and deadline:
                    lines.append(deadline.answer)
                    hits.extend(deadline.hits)
                task_outcomes.append({'task_id':extra['task_id'],'outcome':'answered_complete'})
            else:
                lines.append('Verified booking instructions were not found.' if english else 'ส่วนวิธีจองยังไม่พบคำแนะนำที่ยืนยันได้ครับ')
                task_outcomes.append({'task_id':extra['task_id'],'outcome':'source_missing'})
    errors=coverage_errors(expected,[r['id'] for r in rows])
    metadata={'request_plan':plan,'source_release':price_release(),'expected_ids':expected,'returned_ids':[r['id'] for r in rows], 'missing_ids':sorted(set(expected)-{r['id'] for r in rows}), 'missing_targets':missing_targets, 'rows':rows, 'temporal_validity':temporal,'recorded_expiry':expiry.isoformat() if expiry else None, 'task_outcomes':task_outcomes,'outcome':'answered_complete' if packages and all(t['outcome']=='answered_complete' for t in task_outcomes) else 'answered_partial' if packages else 'clarification_required'}
    route=PipelineRoute('service_fee','conversation_price_lookup',.98,'list' if len(rows)>3 else 'fact','medium','typed service and customer filters with source-bound coverage')
    trace=[PipelineTrace('universal_intent','service_fee/price_lookup',.98,'typed dialogue request',{'filters':task['filters'],'target':','.join(task['targets']),'method':'conversation_plan'}),PipelineTrace('conversation_contract',metadata['outcome'],1.0,'coverage and source validity are separate',metadata)]
    return {'answer':'\n'.join(lines),'hits':hits,'mode':'pipeline:structured_service_fee_conversation','route':route,'entities':EntityBundle(service=task['targets'][0] if len(task['targets'])==1 else None,price_intent=True),'validation':ValidationResult(not errors,tuple(errors), ('source_current_validity_unconfirmed',) if temporal=='source_not_current' else ()), 'metadata':metadata,'trace':trace}
