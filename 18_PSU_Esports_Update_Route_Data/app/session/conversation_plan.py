"""Typed dialogue requests. User selections, not assistant examples, supply slots."""
from __future__ import annotations

import copy
import re
from typing import Any

from app.core.normalization import SERVICE_ALIASES, contains_alias, normalize_text
from app.calculator.service_fee import _detect_group, _detect_minutes, _detect_people

SERVICE_LABELS = {'pc': 'PC', 'ps5': 'PlayStation 5', 'nintendo_switch': 'Nintendo Switch', 'cockpit': 'Cockpit', 'vr': 'VR'}
SERVICES = tuple(SERVICE_LABELS)
GROUPS = ('psu_student_staff', 'general_student', 'general_adult')
ALL = re.compile(r'ทั้งหมด|ทุก(?:เครื่อง|บริการ|โซน|อย่าง|อัน|แพ็กเกจ)|แต่ละ(?:เครื่อง|บริการ|โซน)|ตาราง.*ราคา|เอาหมด|ทั้งห้า|\b(?:all|each|every|both)\s+(?:(?:of\s+)?(?:the\s+)?)?(?:them|services?|devices?|zones?|stations?|prices?|fees?)\b|^\s*(?:all|each|every|everything|both)(?:\s+(?:of\s+)?them)?\s*[.!?]*\s*$', re.I)
OTHER_TASK = re.compile(r'ว่าง|ถูกจอง|กฎ|กฏ|กติกา|แข่ง|เกม|ปุ่ม|เปิด|ปิด|คืออะไร|หมายถึงอะไร|สมาชิก|\b(?:available|booked|rules?|rulebooks?|tournaments?|competitions?|games?|controls?|open|closed|what\s+is|who)\b', re.I)
BOOKING = re.compile(r'วิธีจอง|จอง(?:เครื่อง|อุปกรณ์)?(?:ยังไง|อย่างไร)|ขั้นตอนจอง|\b(?:how\s+(?:to\s+)?(?:book|reserve)|booking\s+(?:steps|instructions))\b', re.I)
SCHEDULE_TASK = re.compile(r'\b(?:opening|closing|schedule|timetable|maintenance)\b|\b(?:service|studio|business|operating)\s+(?:hours?|times?)\b', re.I)
CANCEL = re.compile(r'ไม่(?:เอา|ต้องการ|อยาก(?:รู้|ดู))ราคา|ไม่ต้อง(?:ดู|บอก)?ราคา|\b(?:forget|stop|no\s+more|not\s+the)\s+(?:the\s+)?(?:prices?|fees?)\b', re.I)
REJECT_FEE = re.compile(r'ค่าปรับ|ค่าซ่อม|เสียหาย|รายปี|สมาชิก|ส่วนลด|โปรโม|\b(?:fine|damage|repair|discount|promotion|membership)\b', re.I)


def excluded_services(text: str) -> list[str]:
    # Only the directly negated noun span is excluded, not the rest of the turn.
    excluded = []
    for match in re.finditer(r'(?:ไม่เอา|ไม่ใช่|ยกเว้น|เว้น|\b(?:except|exclude|excluding|not)\b)\s*([^,;.\n]+)', normalize_text(text), re.I):
        # Only an immediately named device is negated. 'Not a student'
        # must never remove a device mentioned later in the sentence.
        span = match.group(1).strip()
        for key, aliases in SERVICE_ALIASES.items():
            if any(re.match(re.escape(normalize_text(a)) + (r'(?![a-z0-9])' if a.isascii() else ''), span, re.I) for a in aliases):
                excluded.append(key)
    return list(dict.fromkeys(excluded))


def service_mentions(text: str, *, fuzzy: bool = False) -> list[str]:
    q = normalize_text(text)
    found = []
    for key, aliases in SERVICE_ALIASES.items():
        for alias in aliases:
            a = normalize_text(alias)
            if (re.search(r'(?<![a-z0-9])' + re.escape(a) + r'(?![a-z])', q) if a.isascii() else a in q):
                found.append(key)
                break
    if found or not fuzzy or len(q) > 50 or re.search(r'\d', q):
        return list(dict.fromkeys(found))
    scores = []
    for key, aliases in SERVICE_ALIASES.items():
        ok, _, score = contains_alias(q, [a for a in aliases if len(a) >= 4], threshold=.84)
        if ok:
            scores.append((score, key))
    scores.sort(reverse=True)
    if scores and (len(scores) == 1 or scores[0][0] - scores[1][0] >= .07):
        return [scores[0][1]]
    return []


def customer_filter(text: str, previous: dict | None = None) -> tuple[str, list[str]]:
    q = normalize_text(text)
    if re.search(r'ไม่ใช่\s*(?:นักศึกษา|บุคลากร)\s*(?:psu|มอ)|\bnot\s+(?:a\s+)?psu\s+(?:student|staff)\b', q):
        return 'external_unspecified', ['general_student', 'general_adult']
    if re.search(r'\b(?:general\s+adults?|adults?(?:\s+from\s+the\s+public)?)\b|บุคคลทั่วไป|คนทั่วไป|ผู้ใหญ่',q) and not re.search(r'ไม่(?:ใช่|เป็น).{0,6}(?:บุคคลทั่วไป|คนทั่วไป)|\bnot\s+(?:a\s+)?(?:general\s+)?adult\b',q):
        return 'general_adult', ['general_adult']
    # Negation must win before the legacy group's positive substring aliases.
    if re.search(r'ไม่ใช่\s*(?:นักศึกษา|นักเรียน)|ไม่ได้เป็นนักศึกษา|\b(?:not\s+(?:a\s+)?student|non[- ]student)\b', q):
        if previous and previous.get('customer_scope') in {'external_unspecified', 'general_adult', 'general_student'}:
            return 'general_adult', ['general_adult']
        if re.search(r'บุคคลทั่วไป|คนทั่วไป|คนนอก|ภายนอก|\b(?:adult|public|external)\b', q):
            return 'general_adult', ['general_adult']
        return 'non_student_unspecified', []
    if re.search(r'บุคคลภายนอก|ผู้ใช้ภายนอก|คนนอก|ไม่ใช่\s*(?:psu|มอ)|ไม่ได้เรียน\s*มอ|\b(?:external\s+users?|outsiders?|non[- ]psu|not\s+(?:a\s+)?psu)\b', q):
        if not re.search(r'นักศึกษา|นักเรียน|\bstudent\b', q):
            return 'external_unspecified', ['general_student', 'general_adult']
    if re.search(r'นักศึกษา|นักเรียน|\bstudents?\b', q) and not re.search(r'psu|มอ|ต่าง|ศิษย์เก่า|external|other\s+institutions?|alumni|kmitl|chula', q):
        return 'student_unspecified', ['psu_student_staff', 'general_student']
    group, ambiguous, _ = _detect_group(q)
    if group and not ambiguous:
        return group, [group]
    if re.search(r'บุคคลภายนอก|ภายนอก|\bexternal\b', q):
        return 'external_unspecified', ['general_student', 'general_adult']
    return '', []


def is_fee_request(text: str) -> bool:
    q = normalize_text(text)
    if CANCEL.search(q) or REJECT_FEE.search(q):
        return False
    explicit = bool(re.search(r'ราคา|ค่าบริการ|ค่าใช้บริการ|ค่าเล่น|\b(?:prices?|fees?|costs?|rates?)\b', q))
    amount = bool(re.search(r'กี่บาท|เท่าไหร่|เท่าไร|\bhow\s+much\b', q))
    usage = bool(re.search(r'ใช้บริการ|เล่น|อุปกรณ์|เครื่อง|ภายนอก|\b(?:service|play|equipment|external)\b', q))
    # Keep range pricing/comparisons with their established calculator adapters.
    if re.search(r'\d\s*(?:โมง|:|am|pm)|ตั้งแต่|ถึง|เปรียบเทียบ|ต่างกัน|ถูกกว่า|แพงกว่า|\b(?:compare|cheaper|difference|from.+to)\b', q, re.I):
        return False
    return (explicit and (usage or customer_filter(q)[0] or service_mentions(q, fuzzy=True) or ALL.search(q))) or (amount and bool(service_mentions(q, fuzzy=True)))


def _task(text: str) -> dict:
    scope, groups = customer_filter(text)
    excluded = excluded_services(text)
    services = [s for s in service_mentions(text, fuzzy=not bool(ALL.search(text))) if s not in excluded]
    all_services = bool(ALL.search(text)) and (not services or bool(excluded))
    filters = {'customer_scope': scope or 'unspecified', 'customer_group_ids': groups,
               'duration_minutes': _detect_minutes(text), 'people_count': _detect_people(text)}
    per_target = {}
    # A duration belongs to its service span, not to every service in a compound.
    positions = []
    for key in services:
        for alias in SERVICE_ALIASES[key]:
            m = re.search(re.escape(normalize_text(alias)), normalize_text(text))
            if m:
                positions.append((m.start(), key)); break
    positions.sort()
    if len(positions) > 1:
        for i, (start, key) in enumerate(positions):
            normalized = normalize_text(text)
            span = normalized[start:positions[i+1][0] if i+1 < len(positions) else len(normalized)]
            minutes = _detect_minutes(span)
            people = _detect_people(span)
            if minutes is not None or people is not None:
                per_target[key] = {'duration_minutes': minutes, 'people_count': people}
        if per_target:
            filters['duration_minutes'] = None
            filters['people_count'] = None
    return {'task_id': 'fee-1', 'domain': 'service_fee', 'operation': 'price_lookup',
            'targets': [s for s in SERVICES if s not in excluded] if all_services else services,
            'scope': {'entity_selection': 'all' if all_services else 'explicit' if services else 'unresolved', 'detail_level': 'package_rates'},
            'filters': filters, 'per_target_filters': per_target, 'excluded_targets': excluded,
            'pending_slots': [] if services or all_services else ['service'],
            'offered_option_ids': list(SERVICES),
            'provenance': {'operation': 'explicit_user', 'targets': 'explicit_user' if services or all_services else 'unresolved', 'filters': 'explicit_user'}}


def legacy_task(history: Any) -> dict | None:
    if not isinstance(history, list) or len(history) < 2:
        return None
    user, reply = history[-2:]
    if not isinstance(user, dict) or not isinstance(reply, dict) or user.get('role') != 'user' or reply.get('role') != 'assistant':
        return None
    if user.get('context_eligible') is False or reply.get('context_eligible') is False or user.get('contextEligible') is False or reply.get('contextEligible') is False:
        return None
    plan = reply.get('request_plan')
    if isinstance(plan, dict) and plan.get('schema_version') == 1:
        tasks = plan.get('tasks', [])
        if isinstance(tasks, list) and tasks and valid_price_task(tasks[0]):
            return copy.deepcopy(tasks[0])
    q = str(user.get('text') or user.get('content') or '')
    category = reply.get('route_category')
    pending = reply.get('route_intent') == 'price_missing_service'
    if is_fee_request(q) and (category == 'service_fee' or pending):
        return _task(q)
    return None


def _canonical(task: dict, locale: str) -> str:
    labels = ', '.join(SERVICE_LABELS[k] for k in task['targets'])
    all_services = task['scope']['entity_selection'] == 'all'
    filters = task['filters']
    customer = filters.get('customer_scope', '')
    group_text = {'general_adult': 'general adults' if locale == 'en' else 'บุคคลทั่วไป',
                  'general_student': 'external students' if locale == 'en' else 'นักศึกษาต่างสถาบัน',
                  'psu_student_staff': 'PSU students and staff' if locale == 'en' else 'นักศึกษาและบุคลากร PSU',
                  'external_unspecified': 'external users' if locale == 'en' else 'บุคคลภายนอก'}.get(customer, '')
    q = ('All service prices' if all_services else 'Service prices '+labels) if locale == 'en' else ('ตารางราคาทุกบริการ' if all_services else 'ค่าบริการ '+labels)
    if group_text:
        q += ' '+group_text
    if filters.get('duration_minutes'):
        q += f" {filters['duration_minutes']} "+('minutes' if locale == 'en' else 'นาที')
    if filters.get('people_count'):
        q += f" {filters['people_count']} "+('people' if locale == 'en' else 'คน')
    return q


def resolve_request_plan(question: str, history=None, *, active_task: dict | None = None, locale='th') -> dict | None:
    from app.pipeline.zone_rental import resolve_zone_rental_plan
    rental = resolve_zone_rental_plan(question,history,locale=locale)
    if rental is not None:
        return rental
    from app.pipeline.request_focus import explicit_request_focus
    question = explicit_request_focus(question)[0]
    q = normalize_text(question)
    from app.pipeline.service_query_completion import split_service_operations
    if len(split_service_operations(question))>1:
        return None  # Preserve raw compound before the server rewrites it.
    active = copy.deepcopy(active_task) if valid_price_task(active_task) else legacy_task(history)
    price = is_fee_request(q)
    if price:
        from app.pipeline.control_request import is_booking_button_request
        parts = [part.strip(' ?？') for part in re.split(r'\s*(?:\band\b|และ|แล้ว|[;?？])\s*', q, flags=re.I) if part.strip(' ?？')]
        if (2 <= len(parts) <= 3 and any(is_fee_request(part) for part in parts)
            and any(is_booking_button_request(part) or (OTHER_TASK.search(part) and not is_fee_request(part)) for part in parts)):
            # The parent must preserve every requested operation for the
            # compound executor instead of rewriting the turn to prices only.
            return None
    if price and re.search(r'(?:และ|พร้อม|ด้วย|\band\b).*(?:กฎ|กฏ|กติกา|เกมอะไร|ว่างไหม|\brules?\b|\bgames?\b|\bavailable\b)',q,re.I):
        return None  # Delegate other compound domains to the existing planner.
    from app.pipeline.query_signals import looks_like_clear_general_request
    if looks_like_clear_general_request(q) and not price:
        return None
    # Scope words (all/every) belong to the explicit operation in this turn.
    # Bare hours remain a fee duration reply; opening/service hours name a new task.
    new_task = bool(CANCEL.search(q) or REJECT_FEE.search(q) or ((OTHER_TASK.search(q) or SCHEDULE_TASK.search(q)) and not price))
    if new_task or (BOOKING.search(q) and not price):
        return None
    excluded = excluded_services(q)
    all_selected = bool(ALL.search(q))
    known_customer_reply = bool(customer_filter(q, active['filters'] if active else None)[0])
    services = [s for s in service_mentions(q, fuzzy=bool(active) and not all_selected and not known_customer_reply) if s not in excluded]
    act = 'new_task'
    if price:
        task = _task(question)
    elif active and (services or excluded or all_selected or customer_filter(q, active['filters'])[0] or _detect_minutes(q) is not None or _detect_people(q) is not None):
        task = active
        act = 'fill_slot' if task.get('pending_slots') else 'replace_target' if services else 'expand_scope' if all_selected else 'update_filter'
        if services:
            task['targets'] = services
            task['scope']['entity_selection'] = 'explicit'
            task['per_target_filters'] = {}
            task['provenance']['targets'] = 'explicit_user'
        elif all_selected:
            expand_services = bool(task.get('pending_slots') or re.search(r'ทุก(?:บริการ|เครื่อง|โซน)|\ball\s+(?:services?|devices?|zones?|stations?)\b', q))
            if expand_services:
                task['targets'] = list(task['offered_option_ids']) if task.get('pending_slots') else list(SERVICES)
                task['scope']['entity_selection'] = 'all'
            else:
                task['scope']['package_selection'] = 'all_applicable'
            task['provenance']['targets'] = 'explicit_user_scope'
        if excluded:
            task['targets'] = [s for s in task['targets'] if s not in excluded]
            task['offered_option_ids'] = [s for s in task['offered_option_ids'] if s not in excluded]
            task['excluded_targets'] = excluded
        scope, groups = customer_filter(q, task['filters'])
        if scope:
            task['filters']['customer_scope'] = scope
            task['filters']['customer_group_ids'] = groups
        for field, value in [('duration_minutes', _detect_minutes(q)), ('people_count', _detect_people(q))]:
            if value is not None:
                task['filters'][field] = value
        task['pending_slots'] = [] if task['targets'] else ['service']
    elif active and re.fullmatch(r'(?:ลอง(?:อีกที|ใหม่)|อีกที|retry|try\s+again)[.!?\s]*', q):
        task = active
        act = 'retry'
    elif active and len(q) <= 80 and not OTHER_TASK.search(q):
        return {'schema_version': 1, 'original_query': question, 'resolved_query': question,
                'act': 'ambiguous', 'tasks': [active], 'context_used': False, 'needs_review': True}
    elif all_selected and BOOKING.search(q):
        return None  # All steps belongs to this explicit booking operation.
    elif all_selected:
        if isinstance(history,list) and history and isinstance(history[-1],dict) and history[-1].get('route_category') in {'competition_rules','games','equipment','reservation','schedule'}:
            return None  # The established domain resolver owns its own scope.
        return {'schema_version': 1, 'original_query': question, 'resolved_query': question,
                'act': 'ambiguous', 'tasks': [], 'context_used': False, 'missing': 'scope'}
    else:
        return None
    # Explicit new fee prompts can retain known filters in a genuine follow-up.
    if price and active and not re.search(r'เริ่มใหม่|คำถามใหม่|\b(?:reset|new\s+question|start\s+over)\b', q):
        # A rephrased fee request still belongs to the active price dialogue.
        # Omitted eligibility does not mean the user changed their group.
        keys = ['customer_scope', 'customer_group_ids']
        if re.search(r'แล้ว|ล่ะ|\b(?:and|what\s+about)\b', q):
            keys += ['duration_minutes', 'people_count']
        for k in keys:
            v = active['filters'].get(k)
            if task['filters'].get(k) in (None, [], 'unspecified'):
                task['filters'][k] = copy.deepcopy(v)
        if active.get('pending_slots') and active.get('additional_operations'):
            task['additional_operations'] = copy.deepcopy(active['additional_operations'])
        task['provenance']['filters'] = 'explicit_user_or_retained_context'
        act = 'replace_target'
    if BOOKING.search(q):
        task['additional_operations'] = ['booking_how_to']
    tasks = [task]
    if 'booking_how_to' in task.get('additional_operations', []):
        tasks.append({'task_id': 'booking-1', 'domain': 'reservation', 'operation': 'how_to', 'targets': task['targets']})
    return {'schema_version': 1, 'original_query': question, 'resolved_query': _canonical(task, locale),
            'act': act, 'tasks': tasks, 'context_used': bool(active and act != 'new_task'), 'needs_review': False}


def valid_price_task(task: dict) -> bool:
    basic = (isinstance(task, dict) and task.get('domain') == 'service_fee'
            and isinstance(task.get('targets'), list) and all(k in SERVICES for k in task['targets'])
            and isinstance(task.get('filters'), dict) and isinstance(task.get('scope'), dict)
            and isinstance(task.get('provenance'), dict)
            and isinstance(task.get('offered_option_ids'), list)
            and all(k in SERVICES for k in task['offered_option_ids'])
            and isinstance(task.get('pending_slots'), list)
            and all(k == 'service' for k in task['pending_slots'])
            and task['scope'].get('entity_selection') in ('all', 'explicit', 'unresolved')
            and task['filters'].get('customer_scope') in ('unspecified', 'external_unspecified', 'student_unspecified', 'non_student_unspecified', *GROUPS)
            and isinstance(task['filters'].get('customer_group_ids'), list)
            and all(k in GROUPS for k in task['filters']['customer_group_ids']))
    if not basic:
        return False
    for field in ('duration_minutes', 'people_count'):
        value = task['filters'].get(field)
        if value is not None and (type(value) is not int or not 0 < value <= 100000):
            return False
    per_target = task.get('per_target_filters', {})
    if not isinstance(per_target, dict):
        return False
    for key, filters in per_target.items():
        if key not in SERVICES or not isinstance(filters, dict):
            return False
        for field, value in filters.items():
            if field not in ('duration_minutes', 'people_count') or (value is not None and (type(value) is not int or not 0 < value <= 100000)):
                return False
    return isinstance(task.get('task_id'), str)
