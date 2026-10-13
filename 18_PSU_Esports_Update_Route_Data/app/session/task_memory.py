"""Session-bound requested tasks, not cached facts or implicit personal memory."""
import copy
import re
import unicodedata
from app.core.normalization import THAI_DIGIT_TRANS
from app.session.conversation_plan import resolve_request_plan, service_mentions, valid_price_task

MAX_TASKS = 8
ALL_REPLY = re.compile(r'^(?:ทั้งหมด|ทั้งหมดเลย|ขอทั้งหมด|เอาทั้งหมด|ทุกอัน|ทุกโซน|all\s+zones|all(?:\s+of\s+them)?|everything|both(?:\s+of\s+them)?)(?:\s*(?:ครับ|ค่ะ|please))?[.!?\s]*$',re.I)
RETURN = re.compile(r'^(?:please\s+)?(?:กลับ(?:ไป|มา)(?:ที่|เรื่อง|ดู)?|ย้อนกลับ(?:ไป)?|\b(?:back\s+to|return\s+to|go\s+back\s+to)\b)\s*(.+)$',re.I)
ORDINAL = re.compile(r'^(?:อัน|ข้อ|ตัวเลือก)(?:ที่)?\s*(แรก|หนึ่ง|สอง|สาม|สี่|สุดท้าย)|^(?:(?:the|choose|select)\s+)?(first|second|third|fourth|last)(?:\s+one)?[.!?\s]*$',re.I)

def task_from_response(question, response, plan=None):
    """Targets come from user/resolved queries; never from answer examples."""
    category=response.get('route_category','');intent=response.get('route_intent','');mode=response.get('mode','')
    query=response.get('resolved_question') or question
    if not isinstance(query,str) or not query.strip() or len(query)>2000:
        return None
    domain,operation=None,None
    from app.session.context_resolver import detect_games
    named_games=list(detect_games(query))
    # Family prompts have several historically used mode/category names.
    # Only actual game choices grounded in the query can form this menu;
    # generic assistant examples cannot supply the user's missing target.
    family_offer=[]
    if category=='clarification' and re.search(r'ปุ่ม|ควบคุม|\bcontrols?\b',query,re.I):
        from app.pipeline.entity_resolver import resolve_game_entity
        resolution=resolve_game_entity(query,operation='controls')
        text=response.get('answer','')
        family_offer=[c.title for c in resolution.candidates if c.title.casefold() in text.casefold()] if resolution.is_ambiguous else []
        family_offer.sort(key=lambda g:text.casefold().find(g.casefold()))
        if len(family_offer)>1:domain,operation='game_controls','control_lookup'
    if category=='service_fee':
        domain,operation=('zone_rental','zone_rental_fee') if intent=='zone_rental_fee' else ('service_fee','price_lookup')
    elif category=='competition_rules':domain,operation='competition_rules','rule_lookup'
    elif category=='games':
        if 'control' in mode or 'control' in intent:domain,operation='game_controls','control_lookup'
        elif 'catalog' in mode or 'availability' in mode or intent in ('games_lookup','list','game_list'):domain,operation='games','list'
        elif 'game_detail' in mode:domain,operation='games','game_detail'
        elif 'family' in mode:domain,operation='games','game_detail'
    elif category=='equipment':domain,operation='equipment','equipment_lookup'
    elif category=='reservation':
        domain='reservation'
        operation='availability_lookup' if 'live_booking' in mode or intent=='live_booking_status' else 'booking_navigation' if 'booking_navigation' in mode else 'booking_policy'
    elif category=='schedule':
        domain,operation=('reservation','availability_lookup') if 'live_booking' in mode or intent=='live_booking_status' else ('schedule','schedule_lookup')
    elif category in ('members','overview') and ('member' in mode or 'member' in intent or intent=='group_count'):domain,operation='members','members_lookup'
    elif category=='contact':domain,operation='contact','contact_lookup'
    if domain is None:return None
    targets=list(detect_games(query)) if domain in ('game_controls','competition_rules') or operation=='game_detail' else service_mentions(query)
    price_task=None
    rental_plan=None
    if domain=='zone_rental':
        from app.pipeline.zone_rental import valid_zone_rental_plan
        if valid_zone_rental_plan(plan):
            rental_plan=copy.deepcopy(plan);targets=list(plan['targets'])
    if domain=='service_fee':
        p=plan or resolve_request_plan(query,[],locale='en' if query.isascii() else 'th')
        if p and p.get('tasks') and valid_price_task(p['tasks'][0]):
            price_task=copy.deepcopy(p['tasks'][0]);targets=price_task['targets']
    offered=family_offer
    if 'family' in mode:
        text=response.get('answer','')
        offered=[g for g in detect_games(text) if g.casefold() in text.casefold()]
        offered.sort(key=lambda g:text.casefold().find(g.casefold()))
    if len(offered)>1 and domain=='game_controls':targets=[]
    return dict(schema_version=1,key=domain+'/'+operation,domain=domain,operation=operation,targets=targets,offered_options=offered,
                query=query,price_task=price_task,rental_plan=rental_plan,seed_question=question,mode=mode,route_category=category,route_intent=intent,
                response_id=response.get('request_id'),status=response.get('task_status') or (response.get('task_contract') or {}).get('status','recorded'),
                provenance='server_completed_user_request')

def harvest_tasks(question,response,plan=None):
    contract=response.get('task_contract') or {}
    if not contract:
        contract=next((t.get('metadata',{}) for t in response.get('trace',[]) if isinstance(t,dict) and t.get('stage')=='task_answer_contract'),{})
    children=contract.get('tasks',[]) if contract.get('kind')=='compound' else []
    tasks=[]
    if children:
        for child in children:
            b=dict(route_category=child['category'],route_intent=child['intent'],mode=child['mode'],
                   resolved_question=child['question'],request_id=response.get('request_id'),task_status=child['status'])
            task=task_from_response(child['question'],b)
            if task:tasks.append(task)
    else:
        task=task_from_response(question,response,plan)
        if task:tasks.append(task)
    grouped={}
    for task in tasks:
        old=grouped.get(task['key'])
        if old and task['domain']!='service_fee':
            old['queries']=old.get('queries',[old['query']])+[task['query']]
            old['request_targets']=old.get('request_targets',[old['targets'][0] if len(old['targets'])==1 else old['query']])+[task['targets'][0] if len(task['targets'])==1 else task['query']]
            old['query']='; '.join(old['queries'])
            old['targets']=list(dict.fromkeys(old['targets']+task['targets']))
            old['offered_options']=[]  # Separate child displays are not one ordinal menu.
        elif old:
            # Conflicting requests with one operation cannot be resumed by a
            # single topic marker without silently dropping a child.
            old['resume_ambiguous']=True
        else:grouped[task['key']]=task
    return list(grouped.values())

def _resolved(question, query, task, reason, *, error=None):
    from app.session.context_resolver import ResolvedQuestion
    if error:
        return ResolvedQuestion(question,question,True,context_domain=task.get('domain'),context_operation=task.get('operation'),
                                reason=reason).to_dict(), {'schema_type':'dialogue_state_clarification_v1','schema_version':1,
                                'resolved_query':question,'context_used':True,'reason':reason,'message_key':error}
    targets=task.get('targets',[])
    return ResolvedQuestion(question,query,True,context_game=targets[0] if len(targets)==1 and task['domain'] in ('game_controls','competition_rules') else None,
             context_domain=task['domain'],context_operation=task['operation'],context_topic=', '.join(targets),reason=reason).to_dict(),None

def _resume_many(question,task,resolved):
    queries=task['queries']
    if not 1<=len(queries)<=4 or any(not isinstance(q,str) or not 0<len(q)<=2000 for q in queries):
        return _resolved(question,question,task,'archived_requests_exceed_bound',error='scope')
    return resolved,dict(schema_type='dialogue_resume_v1',schema_version=1,domain=task['domain'],operation=task['operation'],
        targets=task['request_targets'],requests=list(queries),resolved_query=resolved['resolved_question'],context_used=True,
        provenance='acknowledged_server_requested_tasks')

def resolve_memory(question,record,*,locale='th'):
    """Only explicit resume or bounded scope commands may access older tasks."""
    from app.session.service_fact_dialogue import resolve_service_fact_resume
    service=resolve_service_fact_resume(question,record)
    if service:
        plan=None
        if service.reason in {'ambiguous_service_resume','no_acknowledged_service_resume'}:
            plan={'schema_type':'dialogue_state_clarification_v1','schema_version':1,'resolved_query':question,'context_used':True,'reason':service.reason,'message_key':'scope' if service.reason=='ambiguous_service_resume' else 'no_previous_task'}
        return service.to_dict(),plan
    q=unicodedata.normalize('NFC',question).casefold().strip().translate(THAI_DIGIT_TRANS);archive=record.get('task_memory',{})
    def eligible(t):
        return bool(t.get('acknowledged'))
    resume=RETURN.fullmatch(q)
    if resume:
        tail=resume[1]
        # A return marker with a complete new target/filter is left to the
        # ordinary resolver rather than silently dropping those words.
        from app.session.context_resolver import detect_games
        if service_mentions(tail) or detect_games(tail) or re.search(r'\d|ไม่|\b(?:not|except|without)\b',tail):return None,None
        selector=None;remainder=tail
        for key,pattern in [('zone_rental/zone_rental_fee',r'(?:ราคา|ค่าบริการ)?(?:เช่า)?เหมา|ราคาเช่าโซน|\b(?:rental(?:\s+(?:prices?|fees?))?|zone rental)\b'),
                            ('service_fee/price_lookup',r'ราคา|ค่าบริการ|\b(?:prices?|fees?)\b'),
                            ('game_controls/control_lookup',r'ปุ่ม|ควบคุม|\bcontrols?\b'),
                            ('competition_rules/rule_lookup',r'กฎ|กฏ|กติกา|\b(?:rules?|rulebook)\b'),
                            ('games/list',r'รายชื่อเกม|รายการเกม|\b(?:game\s+list|games\s+list|catalog)\b'),
                            ('games/game_detail',r'รายละเอียดเกม|\bgame\s+details?\b'),
                            ('equipment/equipment_lookup',r'อุปกรณ์|\bequipment\b'),
                            ('schedule/schedule_lookup',r'เวลาเปิดปิด|เวลาบริการ|เวลาทำการ|ตารางบริการ|ตารางเวลา|\b(?:opening\s+hours|service\s+hours|schedule)\b'),
                            ('members/members_lookup',r'(?:รายชื่อ)?สมาชิก|รายชื่อผู้ดูแล|\b(?:member\s+list|members?|staff\s+list)\b'),
                            ('contact/contact_lookup',r'ช่องทางติดต่อ|ข้อมูลติดต่อ|\bcontact(?:\s+(?:details|information))?\b'),
                            ('reservation/availability_lookup',r'สถานะ(?:การ)?จอง|เครื่องว่าง|\bbooking\s+(?:status|availability)\b'),
                            ('reservation/booking_policy',r'วิธี(?:การ)?จอง|ขั้นตอน(?:การ)?จอง|\bbooking\s+(?:process|steps|policy)\b'),
                            ('reservation/*',r'การจอง|\bbooking\b')]:
            if re.search(pattern,remainder,re.I):
                if selector is not None:return _resolved(question,question,{},'ambiguous_return_domains',error='scope')
                selector=key;remainder=re.sub(pattern,'',remainder,flags=re.I)
        if selector:
            remainder=re.sub(r'\b(?:competition|the|previous|earlier|please)\b|เดิม|เมื่อกี้|การแข่งขัน|เรื่อง|ครับ|ค่ะ', '', remainder, flags=re.I).strip(' .!?')
            if remainder:return _resolved(question,question,{},'resume_contains_unresolved_new_conditions',error='scope')
        task=archive.get(selector) if selector else None
        if selector=='reservation/*':
            matches=[t for t in archive.values() if t['domain']=='reservation' and eligible(t)]
            if len(matches)>1:return _resolved(question,question,{},'booking_return_has_multiple_operations',error='booking_scope')
            task=matches[0] if matches else None
        if not task or not eligible(task):return _resolved(question,question,{},'no_acknowledged_archived_task',error='no_previous_task')
        if task.get('resume_ambiguous'):return _resolved(question,question,task,'archived_operation_has_multiple_requests',error='scope')
        query=task['query'];price_plan=None
        if task.get('price_task'):
            price_plan=resolve_request_plan('retry',[],active_task=task['price_task'],locale=locale)
            query=price_plan['resolved_query'];price_plan['original_query']=question;price_plan['context_used']=True;price_plan['act']='resume_task'
        if task.get('rental_plan'):
            from app.pipeline.zone_rental import valid_zone_rental_plan
            if valid_zone_rental_plan(task['rental_plan']):
                price_plan=copy.deepcopy(task['rental_plan'])
                price_plan.update(original_query=question,context_used=True,act='resume_rental_task')
                query=price_plan['resolved_query']
        resolved,unused=_resolved(question,query,task,'explicitly_resumed_archived_task')
        if task.get('queries'):return _resume_many(question,task,resolved)
        return resolved,price_plan
    current=[archive[k] for k in record.get('current_task_keys',[]) if k in archive and eligible(archive[k])]
    if ALL_REPLY.fullmatch(q):
        if len(current)>1:return _resolved(question,question,{},'all_has_multiple_operations',error='scope')
        if len(current)==1:
            task=copy.deepcopy(current[0])
            if task['domain']=='games' and task['operation']=='list':
                if q in ('all zones','ทุกโซน'):
                    return _resolved(question,'What games can I play?' if locale=='en' else 'มีเกมอะไรให้เล่นบ้าง',task,'explicit_all_catalog_zones')
                if task.get('targets'):
                    queries=[f'What games are on {t}?' if locale=='en' else f'{t} มีเกมอะไรบ้าง' for t in task['targets']]
                    return _resolved(question,'; '.join(queries),task,'all_games_preserves_selected_zone')
                return _resolved(question,question,task,'all_catalog_axis_ambiguous',error='scope')
            if task['domain']=='game_controls':
                if task.get('queries') and len(task['queries']) != len(task['targets']):
                    # Unresolved children still belong to the user's scope.
                    # Re-execute them rather than reporting only known games.
                    resolved,unused=_resolved(question,'; '.join(task['queries']),task,'all_preserves_unresolved_children')
                    return _resume_many(question,task,resolved)
                if not task['targets'] and task.get('offered_options'):
                    task['targets']=task['offered_options']
                if not task['targets']:return _resolved(question,question,task,'all_controls_without_game',error='game')
                if len(task['targets'])>4:return _resolved(question,question,task,'all_selection_exceeds_bound',error='scope')
                queries=[f'What are all the controls for {t}?' if locale=='en' else f'{t} มีปุ่มควบคุมทั้งหมดอะไรบ้าง' for t in task['targets']]
                resolved,unused=_resolved(question,'; '.join(queries),task,'all_controls_for_selected_targets')
                if len(queries)>1:
                    from app.session.context_resolver import ResolvedQuestion
                    resolved=ResolvedQuestion(**{**resolved,'selected_requests':tuple(queries)}).to_dict()
                    return resolved,ResolvedQuestion(**resolved).to_selection_plan()
                return resolved,None
    if ORDINAL.fullmatch(q) and len(current)==1:
        task=current[0];offered=task.get('offered_options',[])
        if offered:
            selector=next(g for g in ORDINAL.fullmatch(q).groups() if g)
            index={'แรก':0,'หนึ่ง':0,'first':0,'สอง':1,'second':1,'สาม':2,'third':2,'สี่':3,'fourth':3,'สุดท้าย':-1,'last':-1}[selector]
            if index>=len(offered):return _resolved(question,question,task,'ordinal_outside_offered_options',error='ordinal_axis')
            chosen=copy.deepcopy(task);chosen['targets']=[offered[index]]
            query=(f'What are the controls for {offered[index]}?' if locale=='en' else f'{offered[index]} มีปุ่มควบคุมอะไรบ้าง') if task['operation']=='control_lookup' else (f'What is {offered[index]}?' if locale=='en' else f'{offered[index]} คืออะไร')
            return _resolved(question,query,chosen,'explicit_ordinal_of_offered_family_options')
        # An ordinary catalog shows both zones and games, so its ordinal axis
        # is ambiguous. Do not pick the first source alias as a selection.
        if current[0]['operation']=='list':return _resolved(question,question,current[0],'ordinal_catalog_axis_ambiguous',error='ordinal_axis')
    return None,None
