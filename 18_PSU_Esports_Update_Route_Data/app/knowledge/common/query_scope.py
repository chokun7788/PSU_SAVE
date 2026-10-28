"""Operation and relation scopes for arbitrary published common records.

Contains language/schema semantics, never studio prices, game lists or policies.
"""
import re
from .registry import value
from .query_contract import normalize, resolve_fields, matches, broad_request,button_action_question

def operation(question):
    q=normalize(question)
    if re.search(r'เสียหาย|ทำ.{0,8}พัง|\bdamag\w*\b',q) and re.search(r'ค่าปรับ|ชดเชย|รับผิดชอบ|\b(?:fines?|penalt\w*|compensation)\b',q) and not re.search(r'แข่ง|กฎ|กติกา|\b(?:tournament|competition|rules|rulebook)\b',q):return 'policy'
    if re.search(r'\bhow much\s+(?:is|are|does|do|will|would|for|to|it)\b',q) and not re.search(r'แข่ง|กฎ|กติกา|\b(?:tournament|competition|rules|rulebook)\b',q):return 'price'
    if re.search(r'ใครบ้าง|คนไหนบ้าง',q):return 'people'
    rental_q=q.replace('เหมาะ',' ')
    if re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rent|rental|half.day|full.day)\b',rental_q):return 'rental'
    # Competition money/time/maps are game rules, not service fees/hours/maps.
    if re.search(r'แข่ง|กติก|กฎ|กฏ|\b(?:tournament|competition|rules|rulebook)\b',q):return 'rules'
    if re.search(r'ราคา|ค่าบริการ|ค่าเล่น|กี่บาท|เล่นฟรี|\b(?:price|cost|fees?|rates?|budget|free of charge)\b',q):return 'price'
    if re.search(r'ปลั๊กไฟ|เสียบปลั๊ก|ชาร์จ.{0,20}(?:ตัวเอง|ส่วนตัว)|\b(?:plug\s+in|power\s+outlets?|charg\w*.{0,25}(?:own|personal|laptop))\b',q) and re.search(r'ได้ไหม|อนุญาต|ห้าม|\b(?:can|may|allowed|permission|permitted)\b',q):return 'policy'
    if re.search(r'ติดตั้ง|ลงเกม|โหลดเกม|โปรแกรม|ม็อด|ยืม|เอา.{0,25}(?:มา|กลับ)|\b(?:install|download|mods?|borrow|bring|take home)\b',q) and re.search(r'ได้ไหม|อนุญาต|ห้าม|\b(?:can|may|allowed|permission|permitted)\b',q):return 'policy'
    if button_action_question(q) or re.search(r'ปุ่ม|กด|ควบคุม|\b(?:buttons?|controls?|accelerat|jump|bindings|[lr][123])\b',q):return 'controls'
    if re.search(r'นโยบาย|\bpolicy\b',q):return 'policy'
    if re.search(r'อายุ|ผู้ปกครอง|\b(?:minimum age|age limit|years? old|guardian|parental)\b',q):return 'policy'
    if re.search(r'เวลาเปิด|เปิดกี่โมง|เปิดปิด|เปิดไหม|ปิดไหม|ช่วงจอง|maintenance|\b(?:opening hours|open hours|bookable|closed|open on)\b',q):return 'calendar'
    if re.search(r'จอง|จะเล่นต้องทำ(?:ไง|ยังไง|อย่างไร)|เข้า(?:ใช้บริการ|เล่น).*ต้องทำ|\b(?:book|booking|reserve|reservation|start using the studio)\b',q):return 'booking'
    if re.search(r'เช็คอิน|เช็กอิน|ตอนมา|ตอนมาถึง|\b(?:check.in|upon arrival|when i arrive)\b',q) and re.search(r'หลักฐาน|เอกสาร|บัตร|\b(?:proof|documents?|evidence|identification|id)\b',q):return 'checkin'
    if re.search(r'^เกม[?!.]*$|มีเกม|เกมอะไร|เกมไหน|\b(?:games|game list|list of games)\b',q):return 'games'
    if re.search(r'บุคลากร|ทีมงาน|สมาชิก|\b(?:members|staff|personnel)\b',q):return 'people'
    if re.search(r'สเปก|อุปกรณ์|\b(?:equipment|specs|hardware)\b',q):return 'equipment'
    if re.search(r'เวลาเปิด|เปิดกี่โมง|เปิดปิด|เปิดไหม|ปิดไหม|ช่วงจอง|maintenance|\b(?:opening hours|open hours|bookable|closed|open on)\b',q):return 'calendar'
    return None

def primary_ids(question,ids,records):
    """Choose roles before treating shared aliases as equally primary targets."""
    from app.pipeline.competition_taxonomy import detect_competition_facet
    from .schema_language import recover_schema_language
    question,_=recover_schema_language(question,{'competition','rate','control_set','service'})
    op=operation(question);ids=list(dict.fromkeys(ids));by={}
    if op not in {'rules','price','rental'} and re.search(r'เสียหาย|ค่าปรับ|ทำ.{0,8}พัง|\b(?:damag\w*|broken|compensation|fines?)\b',normalize(question)):op='policy'
    if op in {None,'people'} and re.search(r'ใคร|\bwho\b',normalize(question)):
        role_matches=[]
        for rid,r in records.items():
            if r['kind']!='person':continue
            role=value(r,'role')
            for label in role.values() if isinstance(role,dict) else [role]:
                if isinstance(label,str) and label and matches(normalize(question),label):role_matches.append((len(normalize(label)),rid))
        if role_matches:
            longest=max(size for size,_ in role_matches)
            return list(dict.fromkeys(rid for size,rid in role_matches if size==longest)),'people'
    for rid in ids:
        if rid in records:by.setdefault(records[rid]['kind'],[]).append(rid)
    presence=op not in {'rules','price','rental','controls','booking'} and any(by.get(k) for k in ('resource','service','zone')) and bool(re.search(r'มี.{0,90}ไหม|เล่น.{0,90}(?:ได้ไหม|ได้หรือเปล่า)|\b(?:installed|available|have|has|play)\b',normalize(question)))
    if presence and not by.get('game'):
        from .answer import named
        for rid in by.get('control_set',[])+by.get('game_service',[]):
            gid=value(records[rid],'game_id');game=records.get(gid)
            if not game:continue
            title=value(game,'title') or {};aliases=list(game.get('aliases',{}).get('th',[]))+list(game.get('aliases',{}).get('en',[]))+list(title.values() if isinstance(title,dict) else [title])
            aliases=[a for a in aliases if isinstance(a,str) and a]
            matched,_=named(question,{gid:aliases})
            if matched and gid not in by.get('game',[]):by.setdefault('game',[]).append(gid)
    if op not in {'rules','price','rental','controls','booking'} and by.get('game') and any(by.get(k) for k in ('resource','service','zone')) and re.search(r'มี.{0,90}ไหม|เล่น.{0,90}(?:ได้ไหม|ได้หรือเปล่า)|\b(?:installed|available|have|has|play)\b',normalize(question)):
        return by['game']+[rid for kind in ('resource','service','zone') for rid in by.get(kind,[])],'game_presence'
    if not broad_request(question) and (by.get('control_set') or by.get('game_service')) and (op in {'rules','price','controls','booking','games'} or resolve_fields(question,{'game'})[0]):
        linked_games=[value(records[rid],'game_id') for rid in ids if records[rid]['kind'] in {'control_set','game_service'}]
        for gid in linked_games:
            if gid in records and gid not in by.get('game',[]):by.setdefault('game',[]).append(gid)
    if by.get('game') and re.search(r'คือเกมอะไร|เป็นเกมอะไร|\bwhat\s+(?:kind|type)\s+of\s+game|\bwhat\s+game\s+is\b',normalize(question)):
        return by['game'],'game_overview'
    if re.search(r'บัญชี|\baccounts?\b',normalize(question)) and not re.search(r'แข่ง|แมตช์|\b(?:match|tournament|competition)\b',normalize(question)):
        return by.get('game') or [rid for rid in ids if records[rid]['kind']!='competition'],'policy'
    competition_context=bool(re.search(r'แข่ง|กติก|แมตช์|รอบชิง|\b(?:match|tournament|competition|rulebook|rules|finals?|protests?|disputes?)\b',normalize(question)))
    facet=detect_competition_facet(question)
    specific_rule_facets={'rulebook_identity','protest_dispute','dispute','roster_composition','map_pool','match_configuration','match_settings','penalty_matrix'}
    if (op=='rules' or competition_context or facet in specific_rule_facets or facet and by.get('competition')) and (by.get('competition') or by.get('game')):
        games=set(by.get('game',[]))
        events=by.get('competition',[]) or [rid for rid,r in records.items() if r['kind']=='competition' and value(r,'game_id') in games]
        if events:return events,'rules'
    if op=='price' and not competition_context and re.search(r'เสียหาย|ทำ.{0,8}พัง|\bdamag\w*\b',normalize(question)) and any(by.get(k) for k in ('resource','service','equipment_model')):op='policy'
    if op=='policy' and any(by.get(k) for k in ('resource','service','zone','equipment_model','game')):
        return [rid for k in ('resource','service','zone','equipment_model','game') for rid in by.get(k,[])],op
    if op in {'price','rental','controls','games','equipment','booking'}:
        priority={'price':['service','resource','zone','game','rate','rental_package','audience'],
                  'rental':['rental_package','zone','service','resource'],
                  'controls':['game','control_set'], 'games':['service','resource','zone','game'],
                  'equipment':['resource','service','zone','equipment_model'],
                  'booking':['service','resource','zone','game','procedure','faq']}[op]
        explicit_services=[rid for rid in by.get('service',[]) if any(matches(normalize(question),p) for p in platforms_for(records[rid],records))]
        if by.get('game') and not explicit_services and op in {'price','controls','booking'}:chosen=by['game']
        else:chosen=next((by[k] for k in priority if by.get(k)),ids)
        if op in {'price','rental'}:chosen=list(dict.fromkeys(chosen+by.get('audience',[])))
        return chosen,op
    if by.get('person') and re.search(r'ใคร|who|แต่ละหมวด|แต่ละกลุ่ม',normalize(question)):return by['person'],'people'
    if by.get('game') and not competition_context:return by['game'],op
    return ids,op

def calendar_ids(question,records,at):
    from app.calendar.service_calendar import resolve_date_from_text
    from zoneinfo import ZoneInfo
    from datetime import timedelta
    q=normalize(question);base=at.astimezone(ZoneInfo('Asia/Bangkok')).date()
    if 'tomorrow' in q:target=base+timedelta(days=1)
    else:
        resolved=resolve_date_from_text(q,today=base);target=resolved.target_date if resolved else None
    days=[('จันทร์','monday'),('อังคาร','tuesday'),('พุธ','wednesday'),('พฤหัส','thursday'),('ศุกร์','friday'),('เสาร์','saturday'),('อาทิตย์','sunday')]
    wd=next((i for i,terms in enumerate(days) if any(t in q for t in terms)),None)
    if target is None and wd is not None:target=base+timedelta(days=(wd-base.weekday())%7)
    if target is None:return [],None
    closures=[rid for rid,r in records.items() if r['kind']=='closure' and value(r,'local_date')==target.isoformat()]
    if closures:return closures,target
    return [rid for rid,r in records.items() if r['kind']=='schedule' and value(r,'weekday')==target.weekday()],target

def derived_names(names,records):
    """Names already present in schema values; no per-query spelling aliases."""
    out={rid:list(aliases) for rid,aliases in names.items()}
    for rid,r in records.items():
        if rid not in out:continue  # Never reintroduce a withdrawn target.
        for key in ('title','name','event_name','display_name','question'):
            v=value(r,key)
            if isinstance(v,dict):out[rid].extend(s for s in v.values() if isinstance(s,str) and s)
            if r['kind']=='faq' and key=='question' and isinstance(v,dict):out[rid].extend(s.rstrip(' ?!.,') for s in v.values() if isinstance(s,str) and s.rstrip(' ?!.,'))
        if r['kind']=='service':
            p=value(r,'platform')
            if p:
                out[rid].append(p)
                # Conventional device notation, derived from the numbered platform.
                m=re.fullmatch(r'PlayStation\s+(\d+)',p,re.I)
                if m:out[rid].append('PS'+m[1])
        if r['kind']=='zone':
            v=value(r,'name') or {}
            for s in v.values() if isinstance(v,dict) else [v]:
                if isinstance(s,str) and s.endswith(' Zone'):out[rid].append(s[:-5])
        if r['kind']=='game':
            v=value(r,'title') or {}
            for s in v.values() if isinstance(v,dict) else [v]:
                if s:out[rid].extend(re.findall(r'\(([A-Za-z][A-Za-z0-9]{1,9})\)',s))
        if r['kind']=='equipment_model':
            v=value(r,'name') or {}
            for text in v.values() if isinstance(v,dict) else [v]:
                if isinstance(text,str):
                    family=re.split(r'\s+รุ่น\s*|\s+model\b\s*',text,maxsplit=1,flags=re.I)[0].strip()
                    if family and family!=text:out[rid].append(family)
        if r['kind']=='person':
            group=value(r,'team')
            if isinstance(group,dict):out[rid].extend(s for s in group.values() if isinstance(s,str) and s)
        out[rid]=list(dict.fromkeys(out[rid]))
    return out

def rental_ids(question,ids,records):
    zones={rid for rid in ids if records[rid]['kind']=='zone'}
    audiences={rid for rid in ids if records[rid]['kind']=='audience'}
    for rid in ids:
        r=records[rid]
        if r['kind']=='resource':zones.add(value(r,'zone_id'))
        if r['kind']=='service':zones.update(value(records.get(resource,{'fields':{}}),'zone_id') for resource in value(r,'resource_ids') or [])
    q=normalize(question)
    periods=set()
    if re.search(r'ครึ่งวัน|half.day',q):periods.add('half_day')
    if re.search(r'เต็มวัน|full.day',q):periods.add('full_day')
    return [rid for rid,r in records.items() if r['kind']=='rental_package' and (not zones or zones.intersection(value(r,'zone_ids') or [])) and (not audiences or value(r,'audience_id') in audiences) and (not periods or value(r,'period_label') in periods)]

def scoped_live_request(question,ids,records):
    q=normalize(question)
    if re.search(r'free\s+(?:to\s+play|of\s+charge|admission)|\b(?:cost|fee|price|charge)\b|เล่นฟรี|ไม่เสียเงิน',q):return False
    kinds={records[rid]['kind'] for rid in ids if rid in records}
    return bool(kinds.intersection({'resource','service','zone'}) and not kinds.intersection({'game','control_set','game_service'}) and re.search(r'\b(?:free|available|busy|occupied|booked)\b',q))

def platforms_for(record,records):
    if record['kind']=='service':return {value(record,'platform')} - {None}
    if record['kind']=='resource':
        return {value(r,'platform') for r in records.values() if r['kind']=='service' and record['record_id'] in (value(r,'resource_ids') or [])} - {None}
    if record['kind']=='zone':
        resources={r['record_id'] for r in records.values() if r['kind']=='resource' and value(r,'zone_id')==record['record_id']}
        return {value(r,'platform') for r in records.values() if r['kind']=='service' and resources.intersection(value(r,'resource_ids') or [])} - {None}
    return set()

def offered_games(ids,records):
    services=set();platforms=set()
    for rid in ids:
        r=records[rid];platforms.update(platforms_for(r,records))
        if r['kind']=='service':services.add(rid)
        if r['kind']=='resource':services.update(rr['record_id'] for rr in records.values() if rr['kind']=='service' and rid in (value(rr,'resource_ids') or []))
        if r['kind']=='zone':
            rs={rr['record_id'] for rr in records.values() if rr['kind']=='resource' and value(rr,'zone_id')==rid}
            services.update(rr['record_id'] for rr in records.values() if rr['kind']=='service' and rs.intersection(value(rr,'resource_ids') or []))
    return list(dict.fromkeys(value(r,'game_id') for r in records.values() if r['kind']=='game_service' and value(r,'offered') is True and
        (not ids or value(r,'service_id') in services or value(records.get(value(r,'service_id'),{'fields':{}}),'platform') in platforms)
        and value(r,'game_id') in records))

def control_text(record,key):
    """Only R63's explicitly lossless partial control representation.

    A genuine owner-unknown/withdrawn bindings field must not be replaced.
    """
    if record['kind']!='control_set' or key!='bindings':return None
    f=record['fields'].get(key,{})
    if f.get('status')!='unknown' or 'gesture/context' not in str(f.get('note','')):return None
    source=record['fields'].get('limitations',{})
    v=source.get('value')
    if source.get('status')=='known' and isinstance(v,dict) and any(' | ' in str(v.get(lang) or '') for lang in ('th','en')):
        return source
    return None

def same_platform(actual,requested):
    if not actual or not requested:return False
    if normalize(actual)==normalize(requested):return True
    def ps_number(text):
        q=normalize(text)
        if re.search(r'\bpc\b|nintendo|switch',q):return None
        numbers=set(re.findall(r'(?:playstation\s*|\bps\s*)(\d+)\b',q))
        return next(iter(numbers)) if len(numbers)==1 else None
    a,b=ps_number(str(actual)),ps_number(str(requested))
    return a is not None and a==b

def complete_control_notes(v,lang):
    """Preserve omitted source columns, without pretending to translate them.

    Only the migrated parallel pipe table is eligible; row order alone is not
    sufficient to bind a note to a button. Never mutate the stored source.
    """
    if lang!='en' or not isinstance(v,dict):return v,0
    th=(v.get('th') or '').splitlines();en=(v.get('en') or '').splitlines()
    if not th or len(th)!=len(en):return v,0
    paired=[]
    for a,b in zip(th,en):
        ta=[x.strip() for x in a.split('|')];eb=[x.strip() for x in b.split('|')]
        if len(ta)<3 or len(eb)<3 or ta[0]!=eb[0]:return v,0
        paired.append((ta,eb))
    pending=0;lines=[]
    for ta,eb in paired:
        if ta[2] and not eb[2]:
            eb[2]='[Translation pending; Thai source] '+ta[2];pending+=1
        lines.append(' | '.join(eb))
    return {**v,'en':'\n'.join(lines)},pending


def control_projection(v,question,lang):
    """Narrow only when a literal action/description is present in the question."""
    q=normalize(question);raw=v.get(lang) or ''
    if not raw:return None
    lines=raw.splitlines();selected=[]
    for line in lines:
        pieces=[x.strip() for x in line.split(' | ')]
        if len(pieces)<2:continue
        actions=[normalize(a) for a in re.split(r'\s*/\s*',pieces[1]) if len(a.strip())>=3]
        buttons=[normalize(a) for a in re.split(r'\s*/\s*|,',pieces[0]) if a.strip()]
        if any(matches(q,a) for a in actions+buttons):selected.append(line)
    return '\n'.join(selected) if selected else None

def operation_faqs(question,records,op):
    """Interpret procedure/FAQ topics from their own schema text, not fixed IDs."""
    from .faq_topics import select
    topical=select(question,records,op)
    if topical:return topical
    normalized=normalize(question)
    quota=op not in {'calendar','price','rental','rules'} and bool(re.search(r'(?:กี่|สูงสุด).{0,35}ต่อวัน|(?:สูงสุด|maximum|max).{0,30}(?:session|รอบ)|(?:session|รอบ).{0,30}(?:สูงสุด|maximum)|\b(?:how many|how long|maximum|max)\b.{0,60}\b(?:daily|per day)\b',normalized))
    if quota:
        result=[]
        for rid,r in records.items():
            if r['kind']!='faq':continue
            heading=value(r,'question') or {};heading=' '.join(str(x or '') for x in heading.values()) if isinstance(heading,dict) else str(heading)
            if re.search(r'สูงสุด.{0,20}session|maximum.{0,25}sessions',normalize(heading)):result.append(rid)
        if result:return result
    if op not in {'booking','checkin'}:return []
    q=normalize(question)
    if op=='checkin':
        selected=[]
        for rid,r in records.items():
            if r['kind']!='faq':continue
            v=value(r,'question') or {};title=' '.join(str(x or '') for x in v.values()) if isinstance(v,dict) else str(v)
            if re.search(r'หลักฐาน|เอกสาร|บัตร|\b(?:proof|documents?|evidence|identification|id)\b',normalize(title)) and re.search(r'ตอนมา|มาถึง|แสดง|เช็คอิน|เช็กอิน|\b(?:arriv|show|check.in)',normalize(title)):selected.append(rid)
        return selected
    if re.search(r'ยกเลิก|แก้ไข|เปลี่ยน|เช็คอิน|เช็กอิน|ชำระ|จ่าย|\b(?:cancel|change|edit|check.in|pay|payment|refund)\b',q):return []
    if not re.search(r'จอง|จะเล่นต้องทำ(?:ไง|ยังไง|อย่างไร)|เข้า(?:ใช้บริการ|เล่น).*ต้องทำ|\b(?:book|booking|reserve|reservation)\b',q):return []
    selected=[]
    for rid,r in records.items():
        if r['kind'] not in {'faq','procedure'}:continue
        f=value(r,'question') or value(r,'title') or {}
        words=' '.join(str(x or '') for x in f.values()) if isinstance(f,dict) else str(f)
        words=normalize(words).replace('_',' ')
        if re.search(r'(?:วิธี|ขั้นตอน).{0,10}จอง|(?:booking|reservation).{0,12}(?:steps|procedure)|(?:steps|procedure).{0,12}(?:booking|reservation)',words):selected.append(rid)
    return selected

def rule_selection(question,children,*,full=False):
    """Use literal source section support; dependencies remain explicit FKs."""
    from app.pipeline.competition_taxonomy import detect_competition_facet
    from app.pipeline.competition_source_facets import competition_source_facets,source_facet_equivalents
    from .query_contract import semantic_clauses
    facets=set(filter(None,(detect_competition_facet(clause) for clause in semantic_clauses(question))))
    facet=detect_competition_facet(question)
    if facet:facets.add(facet)
    def body(r,key):
        v=value(r,key)
        return (' '.join(str(x or '') for x in v.values()) if isinstance(v,dict) else str(v or '')).strip()
    def sortkey(r):
        # R63 IDs preserve occurrence order when source numbering repeats.
        occurrence=re.search(r'_section_(\d+)$',r['record_id'])
        if occurrence:return ((0,int(occurrence[1])),)
        return tuple((0,int(s)) if s.isdigit() else (1,s) for s in re.split(r'(\d+)',str(value(r,'section_number') or r['record_id'])))
    ordered=sorted(children,key=sortkey)
    if full:return ordered,{'facet':facet,'method':'explicit_all_source_order'}
    query=normalize(question)
    if len(semantic_clauses(question))==1 and re.search(r'how many teams|กี่ทีม',query) and re.search(r'player|represent|ผู้เล่น|ลงแข่ง|สังกัด',query):
        participation=r'player.{0,60}(?:compete|represent|registered|participate).{0,60}(?:only|at most|up to)\s*(?:\d+|one|two|three|four|five|six|a single)\s*teams?|(?:ผู้เล่น|ผู้เข้าแข่งขัน).{0,35}(?:ลงแข่ง|สังกัด|ในนาม).{0,45}(?:ทีมเดียว|(?:\d+|หนึ่ง|สอง|สาม)\s*ทีม)'
        selected=[r for r in ordered if re.search(participation,normalize(body(r,'text')))]
        if selected:return selected,{'facet':'eligibility_registration','method':'literal_player_team_limit','source_value_inferred':False}
    if re.search(r'forfeit|ปรับแพ้',query) and re.search(r'score|result|บันทึกผล|ผล.*เท่าไหร่|กี่คะแนน',query):
        selected=[r for r in ordered if re.search(r'forfeit|ปรับแพ้',normalize(body(r,'text'))) and re.search(r'\b\d+\s*[-:]\s*\d+\b',body(r,'text'))]
        if selected:return selected,{'facet':'penalty','method':'literal_recorded_forfeit_score','source_value_inferred':False}
    specific=not bool(re.fullmatch(r'\s*(?:กฎ|กฏ|กติกา|rules|rulebook|under|tournament|competition|ของ|ตอน|แข่ง|มีอะไรบ้าง|what|are|the|please|tell|me|ทั้งหมด|all|[\s?!.,:])+',normalize(question)))
    if facet:
        accepted={f for x in facets for f in source_facet_equivalents(x)};selected=[]
        for r in ordered:
            supported=competition_source_facets({'section_title':body(r,'heading'),'text':body(r,'text')})
            declared=value(r,'facet')
            if declared:supported=set(supported)|{declared}
            if accepted.intersection(supported):selected.append(r)
        if facet=='map_pool':
            # A literal map-list row following a confirmed map heading is part
            # of that source section. No map names are hard-coded here.
            for i,r in enumerate(ordered[1:],1):
                if ordered[i-1] in selected and re.search(r'^\d+\.\s*[A-Z][A-Z0-9 -]*(?:,\s*[A-Z][A-Z0-9 -]*){2,}',body(r,'text')) and r not in selected:selected.append(r)
            selected=sorted(selected,key=sortkey)
        # A recognized facet in one clause does not cover another coordinated
        # topic. Recover only literal source matches for those remaining clauses.
        for clause in semantic_clauses(question):
            if not detect_competition_facet(clause):
                for r in lexical_rule_topics(clause,ordered,body):
                    if r not in selected:selected.append(r)
        if not selected:selected=lexical_rule_topics(question,ordered,body)
        return sorted(selected,key=sortkey),{'facet':facet,'facets':sorted(facets),'method':'literal_source_facets','candidate_count':len(ordered)}
    # Explicit generic rules/overview means content, not internal metadata.
    if specific:
        chosen={r['record_id'] for clause in semantic_clauses(question) for r in lexical_rule_topics(clause,ordered,body)}
        selected=[r for r in ordered if r['record_id'] in chosen]
        if selected:return selected,{'facet':None,'method':'source_text_topic_retrieval','selected_ids':[r['record_id'] for r in selected],'semantic_verified':False}
    if re.search(r'กฎ|กฏ|กติกา|\b(?:rules|rulebook)\b',normalize(question)) and not specific:
        return ordered,{'facet':None,'method':'rules_overview_source_order'}
    return [],{'facet':None,'method':'unresolved_rule_topic'}

def lexical_rule_topics(question,ordered,body):
    """Rank current rule sections by source text; no answer generation or old facts."""
    from collections import Counter
    from math import log
    stop={'the','and','are','can','may','for','how','who','why','you','let','tell','all','what','which','when','where','would','could','should','please','help','under','rules','rule','tournament','competition','match','game','games','play','playing','policy','information','details','verified','studio','prepare','preparing','must','does','have','that','this','they','their','with','from','about','into','during','after','before','there','some','also','only','will'}
    def terms(s):
        s=normalize(s);out=set()
        for word in re.findall(r'[a-z]{3,}',s):
            if word in stop:continue
            if word.endswith('ies') and len(word)>5:word=word[:-3]+'y'
            elif word.endswith('s') and len(word)>5:word=word[:-1]
            out.add(word)
        out.update(re.findall(r'(?<!\d)\d+[-:]\d+(?!\d)',s))
        for word in re.findall(r'[\u0e00-\u0e7f]+',s):
            for i in range(max(0,len(word)-2)):out.add(word[i:i+3])
        return out
    # Location framing is not the proposition (e.g. food) requested inside it.
    query_text=re.sub(r'(?:ใน|ที่)(?:พื้นที่|บริเวณ)(?:การแข่งขัน|แข่ง)',' ',question)
    query=terms(query_text);docs=[terms(body(r,'heading')+' '+body(r,'text')) for r in ordered]
    freq=Counter(term for d in docs for term in d);scored=[]
    for r,d in zip(ordered,docs):
        overlap=query&d
        informative=[t for t in overlap if freq[t]<max(2,len(ordered)*.55)]
        if not informative:continue
        score=sum(log(1+len(ordered)/(1+freq[t])) for t in informative)/(1+.15*log(1+len(d)))
        scored.append((score,r))
    scored.sort(key=lambda row:-row[0])
    if not scored:return []
    # Keep tied relevant clauses, never top-k merely to fill an answer.
    chosen=[r for score,r in scored[:4] if score>=max(1.,scored[0][0]*.55)]
    if not re.search(r'scope|covers?|overview|general information|appl(?:y|ies) to|ขอบเขต|ภาพรวม',normalize(question)):
        from app.pipeline.competition_source_facets import competition_source_facets
        chosen=[r for r in chosen if competition_source_facets({'section_title':body(r,'heading'),'text':body(r,'text')})!=frozenset({'rulebook_identity'})]
    selected_ids={r['record_id'] for r in chosen}
    return [r for r in ordered if r['record_id'] in selected_ids]
