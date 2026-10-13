"""Schema-driven read/joins. No game names or owner facts live in this module."""
from __future__ import annotations
import os,re,json,time,sqlite3,unicodedata
from pathlib import Path
from datetime import datetime,timezone
from difflib import SequenceMatcher
from app.pipeline.schemas import PipelineAnswer,PipelineRoute,PipelineTrace,EntityBundle,ValidationResult
from .store import CommonStore
from .registry import CATALOG,value,aware
from .semantics import project,label
from .read_contract import build_needs
from .authority import classify as authority_decision,scoped_names,field_ownership
from .relations import linked_policies,related_rates,related_attributes
from .discovery import discover_games
from .budget import budget_request
from .rendering import enum_text,conditions_text
from .dialogue import resolve_state,changed_domain
from .query_contract import normalize,broad_request,live_request,strip_names,resolve_fields,unresolved_clauses,overview_request,bare_selector,focus_request,resolution_uncertain,scope_kinds

ROOT=Path(__file__).resolve().parents[3]
# Kept for older diagnostic scripts only. Routing uses query_contract instead.
TERMS={
 'how_to_play':['วิธีเล่น','เล่นยังไง','เล่นอย่างไร','how to play','how do i play','instructions'],
 'genre':['แนว','ประเภทเกม','genre','what kind of game'],
 'summary':['เกี่ยวกับ','คืออะไร','what is','about','description'],
 'supported_platforms':['แพลตฟอร์ม','platform','เครื่องไหน','อุปกรณ์ไหน','เล่นที่ไหน','where can','available on'],
 'bindings':['ปุ่ม','ควบคุม','กดอะไร','กดตรงไหน','controls','buttons','jump','กระโดด','input'],
 'players_min':['กี่คน','เพื่อน','players','multiplayer','together'],
 'amount_minor':['ราคา','ค่าบริการ','กี่บาท','เท่าไหร่','price','cost','rate','fee','how much'],
 'details':['กฎ','กฏ','ข้อกำหนด','นโยบาย','อนุญาต','policy','allowed','rules','permission'],
 'steps':['ขั้นตอน','ทำยังไง','วิธี','how do','procedure','steps'],
 'open_periods':['เวลาเปิด','เปิดกี่โมง','opening hours','open hours'],
 'bookable_periods':['ช่วงจอง','เวลาจอง','booking hours','bookable'],
 'address':['ที่อยู่','อยู่ไหน','ที่ไหน','address','located','location'],
 'value':['ติดต่อ','contact','เบอร์','phone'],
}
KIND_TERMS={'competition':['การแข่งขัน','แข่ง','competition','tournament'], 'rental_package':['เหมา','rental','package'],
 'game':['เกม','game'], 'rate':['ราคา','ค่าบริการ','price','fee','rate'],
 'policy':['กฎ','กฏ','นโยบาย','policy','rules'], 'procedure':['ขั้นตอน','procedure'], 'zone':['โซน','zone'],
 'resource':['อุปกรณ์','เครื่อง','equipment','resources'], 'schedule':['ตารางเวลา','เวลาเปิด','opening hours','schedule'],
 'news':['ข่าว','กิจกรรม','news','events'], 'person':['บุคลากร','ทีมงาน','staff'], 'contact':['ติดต่อ','contact'],
 'center':['ศูนย์อยู่','ที่ตั้ง','center location','studio location'], 'facility':['สิ่งอำนวยความสะดวก','facilities']}
def normal(s):return normalize(s)
def all_query(q):return broad_request(q)
def live_query(q):return live_request(q)
def text(v,lang):
    if isinstance(v,dict) and set(v)=={'th','en'}:
        return v.get(lang) or ((('[Thai source] ' if lang=='en' else '[ต้นฉบับอังกฤษ] ')+(v.get('th' if lang=='en' else 'en') or '')))
    if type(v) is bool:return ('Yes' if v else 'No') if lang=='en' else ('มี/ใช่' if v else 'ไม่มี/ไม่ใช่')
    if isinstance(v,list):return '\n'.join('• '+text(x,lang) for x in v) if v else ('None (confirmed)' if lang=='en' else 'ไม่มี (ยืนยันแล้ว)')
    if isinstance(v,dict):return '; '.join(k+': '+text(x,lang) for k,x in v.items())
    return str(v)
def title(r,lang):
    for k in ('title','name','display_name','event_name','subject','question','heading','mode_name','topic','value'):
        if value(r,k) is not None:return text(value(r,k),lang)
    if r.get('aliases',{}).get(lang):return r['aliases'][lang][0]
    captions={'rate':('ค่าบริการ','Service rate'),'control_set':('ปุ่มควบคุมเกม','Game controls'),'game_service':('เกมกับบริการ','Game on this service'),'schedule':('ตารางเวลาบริการ','Service schedule'),'closure':('วันปิดหรือเวลาเปลี่ยนพิเศษ','Special closing or hours'),'live_binding':('ข้อมูลเชื่อมสถานะจอง','Booking data mapping')}
    if r['kind'] in captions:return captions[r['kind']][lang=='en']
    return CATALOG[r['kind']]['owner_form'] if lang=='th' else r['kind'].replace('_',' ')
def active(r,at):
    v=r['validity']
    return v['state']=='unknown' or ((not v['effective_from'] or aware(v['effective_from'])<=at) and (not v['effective_until'] or at<aware(v['effective_until'])))
def effective(r,at,records,seen=None):
    seen=set(seen or ())
    if r['record_id'] in seen:return True
    if not active(r,at):return False
    seen.add(r['record_id'])
    for spec in CATALOG[r['kind']]['fields']:
        if spec['reference_kind'] and value(r,spec['key']) is not None:
            refs=value(r,spec['key']);refs=refs if isinstance(refs,list) else [refs]
            if any(k not in records or not effective(records[k],at,records,seen) for k in refs):return False
    return True
def named(q,names,*,allow_fuzzy=True):
    q=normal(q);exact=[]
    for rid,aliases in names.items():
        for alias in aliases:
            a=normal(alias)
            if len(a)<2:continue
            if a not in q:continue
            pattern=re.escape(a)
            if re.search('[a-z0-9]',a):pattern=r'(?<![a-z0-9])'+pattern+r'(?![a-z0-9])'
            if re.search(pattern,q):exact.append((rid,len(a)));break
    if exact:
        # Nested shorter aliases cannot hijack a longer title.
        longest=max(x[1] for x in exact)
        return [rid for rid,length in exact if length>=longest or not any(normal(a) in normal(b) for a in names[rid] for other,ln in exact if ln>length for b in names[other])], 'exact'
    # A repeated character is a concrete error channel. Accept only a unique
    # exact candidate after deleting ONE adjacent duplicate in a name span.
    # Ordinary exact names were already handled above; numbers stay protected.
    repeated=[]
    variants={q[:i]+q[i+1:] for i in range(len(q)-1) if q[i]==q[i+1] and not q[i].isdigit() and not q[i].isspace()}
    for variant in variants:
        for rid,aliases in names.items():
            for alias in aliases:
                a=normal(alias)
                if len(a)<5:continue
                if a not in variant:continue
                p=(r'(?<![a-z0-9])' if re.match('[a-z0-9]',a) else '')+re.escape(a)+(r'(?![a-z0-9])' if re.search('[a-z0-9]$',a) else '')
                if re.search(p,variant):repeated.append((rid,len(a)));break
    if repeated:
        longest=max(length for _,length in repeated)
        unique={rid for rid,length in repeated if length>=longest or not any(normal(a) in normal(b) for a in names[rid] for other,ln in repeated if ln>length for b in names[other])}
        if len(unique)==1:return list(unique),'unique_repeat_edit'
    if not allow_fuzzy:return [],'none'
    candidates=[]
    for rid,aliases in names.items():
        score=0
        for alias in aliases:
            a=normal(alias)
            if len(a)<5:continue
            # Numeric editions are protected. Only compare bounded question spans.
            for size in (len(a)-1,len(a),len(a)+1):
                for i in range(max(0,len(q)-size+1)):
                    span=q[i:i+size]
                    if (i>0 and q[i-1].isdigit() and span[:1].isdigit()) or (i+size<len(q) and q[i+size].isdigit() and span[-1:].isdigit()):continue
                    if re.findall(r'\d+',span)!=re.findall(r'\d+',a):continue
                    s=SequenceMatcher(None,span,a).ratio()
                    if s>=.88:score=max(score,s)
        if score:candidates.append((score,rid))
    candidates.sort(reverse=True)
    if candidates and (len(candidates)==1 or candidates[0][0]-candidates[1][0]>=.06):return [candidates[0][1]],'bounded_fuzzy'
    return [],'none'
def field_requests(q,kinds=None):
    return resolve_fields(q,kinds)[0]
def context_query(question,history,names,records=None):
    ids,method=named(question,names,allow_fuzzy=False)
    if records:
        state=resolve_state(question,history,records,names,ids)
        if state:return question,state['record_ids'],state['method']
    if ids:return question,ids,method
    if not history:
        ids,method=named(question,names)
        return question,ids,method
    for turn in reversed(history[-6:]):
        if not isinstance(turn,dict):continue
        role=turn.get('role');prior=turn.get('question') or (turn.get('text') or turn.get('content') if role=='user' else None)
        if not prior:continue
        previous,pm=named(str(prior),names)
        if records and previous and changed_domain(question,{records[rid]['kind'] for rid in previous if rid in records}):return question,[],'new_domain'
        if previous and (len(question)<240 and (field_requests(question) or all_query(question) or re.search(r'อันนี้|แบบนี้|เกมนี้|มัน|แล้ว|\b(?:and|also|so|then|it|this|that)\b',question,re.I))):return question,previous,'history_'+pm
    ids,method=named(question,names)
    return question,ids,method

class CommonAnswerer:
    def __init__(self,store):self.store=store
    def answer(self,question,*,locale='th',history=None,at=None,planner=None):
        started=time.perf_counter();snap=self.store.snapshot();rel=snap['release']
        if not rel:return None
        lang='en' if locale=='en' else 'th';at=at or datetime.now(timezone.utc)
        if at.tzinfo is None:raise ValueError('Query time needs timezone')
        records={k:r for k,r in rel['records'].items() if k not in snap['withdrawn']}
        names=scoped_names(snap)
        q,ids,method=context_query(question,history,names,records)
        if not ids and not live_query(question):
            from .name_candidates import recover
            recovery=recover(question,names)
            if recovery and recovery.get('record_ids'):q,ids,method=recovery['corrected'],recovery['record_ids'],recovery['method']
            elif recovery and recovery.get('ambiguous'):
                options=recovery['ambiguous'];msg=('คุณหมายถึงรายการใด: ' if lang=='th' else 'Which record do you mean: ')+ ' / '.join(x['alias'] for x in options)
                return self.finish(snap,started,msg,[],{'pending_selection':{'record_ids':[x['record_id'] for x in options],'requested_fields':field_requests(question)},'name_candidates':options},[],response='clarification')
        if any(k not in records for k in ids):
            return self.finish(snap,started,'รายการนี้ถูกถอนแล้ว / This record has been withdrawn.',[],{'record_ids':ids,'method':method},[],response='withdrawn')
        raw_query=question
        budget=budget_request(q,{rid:r for rid,r in records.items() if effective(r,at,records)},[rid for rid in ids if effective(records[rid],at,records)])
        if budget is not None:
            ids=[row['rate_id'] for row in budget['rows']];method=budget['method']
            if not ids:
                msg='ยังไม่มีราคาที่ได้รับการยืนยันว่าตรงงบนี้ ไม่ได้แปลว่าไม่มีอุปกรณ์ว่าง / No confirmed rate matches this budget; this is not live availability.'
                return self.finish(snap,started,msg,[],{'budget':budget},[],response='list')
        entity_audit=None
        if not ids and planner and budget is None and not live_query(q) and not all_query(q) and not re.search(r'อะไรบ้าง|มีเกมอะไร|\blist\b|what games|which games|(?:what|which)\b.*\b(?:prices|fees|rates)\b',q,re.I):
            from .entity_search import select
            choice,entity_audit=select(q,{rid:r for rid,r in records.items() if effective(r,at,records)},names)
            if choice is None and (entity_audit.get('reason')=='model_busy' or entity_audit.get('error')):
                return self.finish(snap,started,'ระบบยังเลือกข้อมูลให้คำถามนี้ไม่ทัน กรุณาลองอีกครั้ง / The model could not select the relevant data in time; please retry.',[],{'entity_selection':entity_audit},[],response='retry')
            if isinstance(choice,list):ids=choice;method='published_semantic_candidates'
            elif isinstance(choice,dict) and choice.get('ambiguous'):
                options=choice['ambiguous']
                return self.finish(snap,started,('หมายถึงรายการไหน: ' if lang=='th' else 'Which record do you mean: ')+ ' / '.join(title(records[x['record_id']],lang) for x in options),[],{'pending_selection':{'record_ids':[x['record_id'] for x in options],'requested_fields':field_requests(question)},'entity_selection':entity_audit},[],response='clarification')
        q=strip_names(q,ids,names) if ids else normal(q)
        # For unique repetition recovery strip the actually observed noisy span.
        if method=='unique_repeat_edit':
            for rid in ids:
                for alias in names[rid]:
                    a=normal(alias)
                    for i in range(len(a)):
                        if not a[i].isdigit():q=q.replace(a[:i]+a[i]+a[i:],' ')
            q=normal(q)
        current_kinds={records[k]['kind'] for k in ids}
        q,focus=focus_request(q,current_kinds or None)
        broad=all_query(q);requested=field_requests(q);kind=None
        if method in {'state_audience_selection','typed_common_state'} and (not requested or broad):
            from .dialogue import previous_state
            prior_state=previous_state(history,records)
            if prior_state and prior_state['requested_fields']:
                requested=prior_state['requested_fields'];broad=False;method+=':pending_fields'
        if budget is not None:broad=False
        discovery=None;discovery_requested=[]
        if not ids:
            discovery=discover_games(q,{k:r for k,r in records.items() if effective(r,at,records)})
            if discovery:
                ids=discovery['record_ids'];method=discovery['method'];broad=False
                discovery_requested=['game_id','mode_name','platform','players_min','players_max','studio_supported']
                if not ids:
                    return self.finish(snap,started,'ยังไม่พบโหมดเกมที่ศูนย์ยืนยันว่ารองรับจำนวนผู้เล่นนี้ / No confirmed venue-supported game mode matches this player count.',[],{'discovery':discovery},[],response='list')
        if ids and broad and method.startswith('history_'):
            for turn in reversed((history or [])[-6:]):
                if not isinstance(turn,dict) or turn.get('role')!='user':continue
                prior=str(turn.get('content') or turn.get('text') or turn.get('question') or '')
                previous,_=named(prior,names,allow_fuzzy=False)
                previous_fields=field_requests(strip_names(prior,previous,names))
                if previous_fields and not all_query(prior):
                    broad=False;method+=':pending_fields:all_choices';break
        if ids and not requested and not broad and bare_selector(q):
            for turn in reversed((history or [])[-6:]):
                if not isinstance(turn,dict):continue
                prior=turn.get('question') or (turn.get('text') or turn.get('content') if turn.get('role')=='user' else '')
                prior_ids,_=named(str(prior or ''),names,allow_fuzzy=False)
                inherited=field_requests(strip_names(str(prior or ''),prior_ids,names))
                if inherited:requested=inherited;method+=':pending_fields';break
        if not ids:
            listing=bool(re.search(r'อะไรบ้าง|มีอะไร|what .*games|which games|(?:what|which)\b.*\b(?:prices|fees|rates)\b|\blist\b',q,re.I))
            for k,terms in KIND_TERMS.items():
                if any(t in normal(q) for t in terms) and (broad or listing or k in {'center','contact','schedule'} and requested):kind=k;break
            if not kind:
                kind=next((k for field,k in [('address','center'),('value','contact'),('open_periods','schedule'),('bookable_periods','schedule')] if field in requested),None)
            if not kind:return None
            ids=[k for k,r in records.items() if r['kind']==kind and effective(r,at,records)]
            if not ids:return None
            if listing:broad=not requested or broad_request(q)
        # Operational live availability remains with the existing live adapter.
        if live_query(q):return None
        field_kinds=scope_kinds({records[k]['kind'] for k in ids})
        requested=((['amount_minor','period_label','duration_minutes','equipment_included'] if budget.get('kind_scope')=='rental_package' else ['amount_minor','unit','calculation_rule','duration_minutes']) if budget is not None else discovery_requested or field_requests(q,field_kinds))
        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):requested=['answer','scope_note']
        if not requested and ':pending_fields' in method:
            from .dialogue import previous_state
            prior_state=previous_state(history,records)
            if prior_state:requested=list(prior_state['requested_fields'])
            for turn in ([] if requested else reversed((history or [])[-6:])):
                if not isinstance(turn,dict):continue
                prior=turn.get('question') or (turn.get('text') or turn.get('content') if turn.get('role')=='user' else '')
                prior_ids,_=named(str(prior or ''),names,allow_fuzzy=False)
                requested=field_requests(strip_names(str(prior or ''),prior_ids,names),field_kinds)
                if requested:break
        rule_request=bool(re.search(r'กฎ|กฏ|กติกา|\brules\b',q,re.I)) and not re.search(r'เรต|\bage\b',q,re.I)
        if any(records[k]['kind']=='game' for k in ids) and (rule_request or re.search(r'แข่ง|การแข่งขัน|\b(?:competition|tournament)\b',q,re.I)) and not re.search(r'บัญชี|\baccounts?\b|ไม่.*แข่ง|\bnot\b.*\b(?:competition|tournament)\b',q,re.I):
            competitions=[k for k,r in records.items() if r['kind']=='competition' and value(r,'game_id') in ids]
            if competitions:
                ids=competitions;field_kinds={'competition','competition_rule'};requested=field_requests(q,field_kinds)
            else:return None # Legacy rulebooks remain authoritative until migrated.
        plan={'record_ids':ids,'requested_fields':requested,'all_fields':broad,'method':method,'scope':'common_published','platform':None,'query_without_entity':q,'field_selection':resolve_fields(q,field_kinds)[1],'confidence_calibrated':False,'request_focus':focus}
        plan['authority']=authority_decision(raw_query,snap,ids)
        if plan['authority']['decision']=='defer':return None
        if plan['authority']['decision']=='blocked':
            return self.finish(snap,started,'ข้อมูลราคาที่เกี่ยวข้องถูกถอนแล้ว / The related price has been withdrawn.',[],plan,[],response='withdrawn')
        if entity_audit:plan['entity_selection']=entity_audit
        plan['field_authority']=field_ownership(snap,ids,requested)
        if discovery:plan['discovery']=discovery
        if budget is not None:plan['budget']=budget
        supported={records[k]['kind'] for k in ids}
        if 'game' in supported:supported.update(('game_service','game_mode','control_set'))
        if 'competition' in supported:supported.add('competition_rule')
        schema_keys={f['key'] for k in supported for f in CATALOG[k]['fields']}
        overview=overview_request(q)
        gaps=unresolved_clauses(q,field_kinds)
        review=resolution_uncertain(q,field_kinds)
        plan['unresolved_clauses']=gaps if review and not broad and not overview else []
        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):plan['unresolved_clauses']=[]
        plan['semantic_review_needed']=review
        plan['semantic_plan_accepted']=False
        if planner and budget is None and not discovery and not broad and not overview and review and not (method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids)):
            proposed=planner(q,records,ids)
            if proposed:
                from .planner import checked_plan
                clean=checked_plan({k:v for k,v in proposed.items() if k!='method'},ids,records)
                if clean:
                    semantic=getattr(proposed,'semantic_audit',{})
                    plan.update(clean);requested=plan['requested_fields'];plan['unresolved_clauses']=semantic.get('unclear_clauses',[])
                    plan['semantic_plan_accepted']=True;plan['planner_semantic_audit']=semantic
            broad=plan['all_fields']
        if not broad and not requested:
            remainder=normal(q)
            for rid in ids:
                for alias in sorted(names[rid],key=len,reverse=True):remainder=remainder.replace(normal(alias),'')
            remainder=re.sub(r'รายละเอียด|ข้อมูล|คืออะไร|เกี่ยวกับ|ขอ|หน่อย|ครับ|ค่ะ|นะ|\b(?:details|information|about|please|tell me)\b','',remainder).strip(' ?!.,')
            if remainder:
                options=[]
                for k in sorted({records[rid]['kind'] for rid in ids}):
                    options.extend(label(k,f['key'],lang) for f in CATALOG[k]['fields'] if f['publish_core'] and not f['reference_kind'])
                choices=' / '.join(list(dict.fromkeys(options))[:4])
                msg=('ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ '+title(records[ids[0]],lang)+' เช่น '+choices+'?' if lang=='th' else 'The requested topic is unclear. Which part of '+title(records[ids[0]],lang)+' do you need: '+choices+'?')
                return self.finish(snap,started,msg,[],plan,[],response='clarification')
        platforms=sorted({str(value(r,'platform')) for r in records.values() if value(r,'platform')},key=len,reverse=True)
        for p in platforms:
            if re.search(r'(?<![a-z0-9])'+re.escape(p)+r'(?![a-z0-9])',q,re.I):plan['platform']=p;break
        # A named device outside published platforms must not inherit PC controls.
        device=re.search(r'(?<![a-z0-9])(?:playstation\s*|ps\s*)(\d+)(?![a-z0-9])',q,re.I)
        if device:plan['platform']='PS'+device.group(1)
        if plan['platform'] and 'supported_platforms' in requested:plan['requested_platform']=plan['platform']
        if kind and broad and requested:
            # "All games and their platforms" asks for all records, not every
            # field in each record. A plain list still returns all titles.
            broad=False;plan['all_fields']=False;plan['list_scope']=True
        plan['read_contract']=build_needs(raw_query,field_kinds,requested,model=plan['semantic_plan_accepted'],unresolved=plan['unresolved_clauses'])
        plan['response_projection']=[]
        if kind and broad and kind not in {'rate','rental_package','policy','schedule','competition'}:
            from .legacy_bridge import legacy_game_titles
            legacy_titles=legacy_game_titles(snap,locale=lang) if kind=='game' else []
            answer=('Published records in the common catalog' if lang=='en' else 'รายการที่เผยแพร่ในฐานข้อมูลกลาง')+f': {len(ids)}\n'
            answer+='\n'.join('• '+title(records[k],lang) for k in sorted(ids))
            if legacy_titles:
                answer+='\n\n'+('Existing published game information' if lang=='en' else 'เกมจากข้อมูลเดิมที่ใช้งานอยู่')+f': {len(legacy_titles)}\n'+'\n'.join('• '+name for name in legacy_titles)
            elif kind!='game':answer+='\n\n'+('Legacy records awaiting migration are not included in this list.' if lang=='en' else 'รายการเดิมที่ยังไม่ได้ย้ายและอนุมัติในฐานข้อมูลกลางไม่รวมในรายการนี้')
            plan['legacy_title_count']=len(legacy_titles)
            return self.finish(snap,started,answer,[],plan,[],response='list')
        selected={k:records[k] for k in ids};obligations=[];blocks=[];hits=[];rendered_fields=set()
        def add(r,keys):
            rows=[]
            if not effective(r,at,records):
                blocks.append('**'+title(r,lang)+'**\n'+('This revision or a referenced record is not effective at the query time; no current fact is asserted.' if lang=='en' else 'ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้'))
                obligations.append({'record_id':r['record_id'],'field':'validity','status':'not_current'});return
            for key in keys:
                if (r['record_id'],key) in rendered_fields:continue
                f=r['fields'].get(key)
                if f is None:continue
                rendered_fields.add((r['record_id'],key))
                display_label=label(r['kind'],key,lang)
                status=f['status'];v=f['value']
                if status=='known':
                    if key=='amount_minor':out=f'{v//100:,}.{v%100:02d} '+str(value(r,'currency') or 'THB')
                    elif key=='bindings':
                        out='\n'.join('• '+text(b['action'],lang)+' → '+', '.join(b['buttons'])+' ('+b['gesture']+'; '+text(b['context'],lang)+')' for b in v)
                    elif key=='steps':out='\n'.join(str(s['order'])+'. '+text(s['instruction'],lang)+((' — '+title(records[s['contact_id']],lang)) if s['contact_id'] in records else '') for s in sorted(v,key=lambda x:x['order']))
                    elif key.endswith('_id') or key.endswith('_ids'):
                        targets=v if isinstance(v,list) else [v];out=', '.join(title(records[x],lang) if x in records else x for x in targets)
                        if key=='zone_ids' and r['kind'] in {'schedule','closure'} and v==[]:out='All zones' if lang=='en' else 'ทุกโซน'
                        elif v==[]:out='No linked records in this field (confirmed)' if lang=='en' else 'ไม่มีรายการที่เชื่อมในช่องนี้ (ยืนยันแล้ว)'
                    elif key=='conditions_all':out=conditions_text(v,lang,text)
                    elif isinstance(v,list) and not v:out='No entries in this field (confirmed)' if lang=='en' else 'ไม่มีรายการในช่องนี้ (ยืนยันแล้ว)'
                    else:out=enum_text(key,v,lang) or text(v,lang)
                    refs=f['evidence_refs'];labels=[]
                    for ref in refs:
                        src=rel['sources'][ref['source_id']];citation='S'+str(len(hits)+1)
                        hits.append({'id':r['record_id']+':'+key+':'+citation,'title':'ข้อมูลศูนย์ที่ผ่านการอนุมัติ' if lang=='th' else 'Approved center information','source_url':src['public_url'] or '', 'text':text(v,lang),'source_id':src['source_id'],'snapshot_sha256':src['sha256'],'citation_label':citation,'locator':ref['locator']});labels.append(citation)
                    rows.append('• '+display_label+': '+out+' '+''.join('['+s+']' for s in labels))
                else:rows.append('• '+display_label+': '+({'unknown':'Not yet confirmed','not_applicable':'Not applicable','conflicted':'Conflicting sources; needs a decision'}[status] if lang=='en' else {'unknown':'ยังไม่มีข้อมูลยืนยัน','not_applicable':'ไม่เกี่ยวข้องกับรายการนี้','conflicted':'หลักฐานขัดกัน ต้องตัดสินใจก่อน'}[status]))
                obligations.append({'record_id':r['record_id'],'field':key,'status':status,'evidence_refs':f['evidence_refs']})
            if rows:blocks.append('**'+title(r,lang)+'**\n'+'\n'.join(rows))
        for rid,r in selected.items():
            if not effective(r,at,records):add(r,[]);continue
            keys=list(r['fields']) if broad else [k for k in requested if k in r['fields']]
            if not keys and not requested:keys=[s['key'] for s in CATALOG[r['kind']]['fields'] if s['publish_core'] or s['key'] in {'summary','how_to_play'}]
            keys,basis=project(r,keys,full=broad)
            plan['response_projection'].append({'record_id':rid,'fields':basis})
            add(r,keys)
            missing_fields=[key for key in requested if key not in r['fields']]
            for child,childkeys,edge in related_attributes(records,r,missing_fields,full=broad and r['kind'] in {'resource','service','policy'}):
                plan.setdefault('relation_edges',[]).append(edge);add(child,project(child,childkeys)[0])
            if r['kind']=='game':
                wanted=[]
                if broad or 'supported_platforms' in requested:wanted+=['game_service']
                if broad or 'bindings' in requested:wanted+=['control_set']
                if broad or set(requested)&{'players_min','players_max','mode_name','network_requirement','studio_supported'}:wanted+=['game_mode']
                # The exposed child schema must also be readable. Project unique
                # child fields through the verified game_id relationship.
                shared={'game_id','platform','game_version'}
                for childkind in ('game_service','control_set','game_mode'):
                    unique={f['key'] for f in CATALOG[childkind]['fields']}-shared
                    if set(requested)&unique:wanted.append(childkind)
                if 'game_version' in requested:
                    control_fields={f['key'] for f in CATALOG['control_set']['fields']}-shared
                    wanted.append('control_set' if set(requested)&control_fields else 'game_service')
                if 'platform' in requested and not wanted:wanted.append('game_service')
                if set(requested)&{'decision','conditions_all','exceptions','details','consequence','procedure_id'} and re.search(r'บัญชี|\baccounts?\b',q,re.I):wanted.append('game_service')
                for childkind in dict.fromkeys(wanted):
                    children=[rr for rr in records.values() if rr['kind']==childkind and value(rr,'game_id')==rid and (not plan['platform'] or value(rr,'platform')==plan['platform'] or rr['kind']=='game_service' and value(records.get(value(rr,'service_id'),{'fields':{}}),'platform')==plan['platform'])]
                    if childkind=='control_set' and len(children)>1 and not plan['platform']:
                        blocks.append(('Choose a platform/control preset: ' if lang=='en' else 'กรุณาระบุแพลตฟอร์มหรือชุดปุ่ม: ')+', '.join(str(value(x,'platform'))+' / '+str(value(x,'preset')) for x in children))
                        fields=set(requested)&{f['key'] for f in CATALOG['control_set']['fields']} or {'bindings'}
                        obligations.extend({'record_id':rid,'field':key,'status':'needs_clarification'} for key in fields);continue
                    if not children:
                        blocks.append(('No confirmed '+childkind+' data for this scope.' if lang=='en' else 'ยังไม่มีข้อมูลยืนยันในส่วน '+CATALOG[childkind]['owner_form']+' สำหรับขอบเขตนี้'))
                        obligations.append({'record_id':rid,'field':childkind,'status':'unknown'})
                    for child in children:
                        childkeys,childbasis=project(child,requested,full=broad)
                        if childkind=='game_service' and 'supported_platforms' in requested:childkeys=list(dict.fromkeys(childkeys+['offered','service_id']))
                        plan['response_projection'].append({'record_id':child['record_id'],'fields':childbasis})
                        add(child,childkeys)
                        if not effective(child,at,records):continue
                        for policy,policykeys,edge in related_attributes(records,child,[key for key in requested if key not in child['fields']],full=broad and childkind=='game_service'):
                            plan.setdefault('relation_edges',[]).append(edge);add(policy,project(policy,policykeys)[0])
                        if childkind=='game_service':
                            srv=records.get(value(child,'service_id'))
                            if srv and (broad or 'supported_platforms' in requested):add(srv,['name','platform'])
            # Prices are scoped by service and audience. Never choose an arbitrary group.
            if 'amount_minor' in requested and r['kind'] not in {'rate','rental_package'}:
                audiences=[k for k,rr in selected.items() if rr['kind']=='audience']
                related=related_rates(records,r,audiences=audiences,platform=plan['platform'])
                if r['kind']=='zone' and re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|rent|package|half.day|full.day)\b',raw_query,re.I):
                    related=[rr for rr in records.values() if rr['kind']=='rental_package' and rid in (value(rr,'zone_ids') or []) and (not audiences or value(rr,'audience_id') in audiences)]
                for rr in related:
                    pricekeys,pricebasis=project(rr,requested,full=broad);add(rr,pricekeys)
                    plan['response_projection'].append({'record_id':rr['record_id'],'fields':pricebasis})
                if not related:blocks.append('No confirmed price in this scope.' if lang=='en' else 'ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้')
            if r['kind']=='competition' and (broad or set(requested)&{'text','details','depends_on_ids','completeness'}):
                children=[rr for rr in records.values() if rr['kind']=='competition_rule' and value(rr,'competition_id')==rid]
                for child in sorted(children,key=lambda x:str(value(x,'section_number'))):add(child,project(child,requested,full=broad)[0])
            if r['kind']=='competition_rule':
                seen={rid}
                def deps(rr):
                    for dep in value(rr,'depends_on_ids') or []:
                        if dep not in seen and dep in records:seen.add(dep);add(records[dep],list(records[dep]['fields']));deps(records[dep])
                deps(r)
            for policy,policykeys,edge in linked_policies(records,r,requested,full=broad):
                plan.setdefault('relation_edges',[]).append(edge);add(policy,project(policy,policykeys)[0])
        for key in requested:
            if not any(o['field']==key for o in obligations):
                # Do not call an unsupported schema request an unknown owner fact.
                obligations.append({'record_id':None,'field':key,'status':'unsupported_scope'})
                blocks.append((key.replace('_',' ')+': This attribute is outside the selected record scope; please specify the related service or record.' if lang=='en' else key+': หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง'))
        if any(records[rid]['localization']['en_status']=='agent_translated' for rid in ids) and lang=='en':blocks.append('English translation is machine generated and has not been reviewed by the owner.')
        if plan.get('unresolved_clauses') and requested:
            blocks.append(('Some parts of your question are still unclear; please specify: ' if lang=='en' else 'ยังตีความคำถามบางส่วนไม่ชัด กรุณาระบุเพิ่ม: ')+ ' / '.join(plan['unresolved_clauses']))
        if budget is not None:
            plan['unresolved_clauses']=budget.get('unresolved_qualifiers',[])
            if plan['unresolved_clauses']:
                blocks.append('Group pricing or additional requirements still need confirmation; the listed prices alone do not confirm them.' if lang=='en' else 'ราคาเหล่านี้ยังไม่ยืนยันว่าครอบคลุมจำนวนคนหรือความต้องการเพิ่มเติมที่ถาม ต้องตรวจเงื่อนไขนั้นเพิ่ม')
            for row in budget['rows']:
                if row['max_minutes'] is not None:
                    blocks.append((title(records[row['rate_id']],lang)+': '+('Maximum under this confirmed linear rate: ' if lang=='en' else 'สูงสุดตามกฎคิดราคานี้: ')+str(row['max_minutes'])+(' minutes' if lang=='en' else ' นาที')))
            blocks.append('Price options only; availability must be checked live. Groups and services are shown separately.' if lang=='en' else 'เป็นตัวเลือกตามราคา ต้องตรวจสถานะว่างแบบสดอีกครั้ง ราคาแต่ละกลุ่มและบริการแสดงแยกกัน')
            if budget['unknown_rate_ids']:blocks.append('Some rates remain unconfirmed.' if lang=='en' else 'บางรายการยังไม่มีราคายืนยัน')
        return self.finish(snap,started,'\n\n'.join(blocks),hits,plan,obligations)
    def finish(self,snap,started,answer,hits,plan,obligations,response='answer'):
        if not self.store.still_current(snap):answer='ข้อมูลเปลี่ยนระหว่างตอบ กรุณาถามใหม่ / Data changed; please retry.';hits=[];response='retry'
        errors=[]
        if response=='answer':
            if plan.get('unresolved_clauses') and plan.get('requested_fields'):errors.append('unresolved_query_clause')
            for key in plan.get('requested_fields',[]):
                obs=[o for o in obligations if o['field']==key and o.get('record_id') is not None]
                if not obs and not any(o['field']=='validity' and o['status']=='not_current' for o in obligations):errors.append('missing_requested_field:'+key)
            for o in obligations:
                if o['status']=='known' and not o.get('evidence_refs'):errors.append('missing_source_pointer:'+str(o['record_id'])+':'+o['field'])
        if errors:response='partial_answer'
        for hit in hits:hit['metadata']={'common_approved':True,'title':hit['title'],'release_id':snap['active']}
        confidence=.8 if response in {'answer','list'} else 0.0
        artifact={'response_type':response,'release_id':snap['active'],'query_plan':plan,'obligations':obligations,'catalog_scope':'common_published','coverage_errors':errors,'confidence_calibrated':False,'validation_scope':'selected fields and evidence, not human intent correctness'}
        trace=PipelineTrace('common_content',response,confidence,'typed fields and source-backed joins; uncalibrated confidence',artifact)
        return PipelineAnswer(answer=answer,hits=hits,elapsed=time.perf_counter()-started,mode='pipeline:common_'+response,confidence=confidence,route=PipelineRoute('knowledge','common_read',confidence,response,'medium','approved common content'),entities=EntityBundle(),validation=ValidationResult(not errors,tuple(errors)),trace=[trace],decision_artifact=artifact)

def database_path():return Path(os.getenv('PSU_KNOWLEDGE_DB') or ROOT/'data/knowledge/approved.sqlite')
def try_common_answer(question,*,locale='th',recent_history=None,allow_llm=False):
    path=database_path()
    if not path.is_file():return None
    store=CommonStore(path)
    try:
        # Missing V3 tables mean the legacy database has not been migrated yet.
        with store.connect() as c:
            if c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='cc_meta'").fetchone()[0]==0:return None
        snap=store.snapshot()
        if snap['allow_demo'] and os.getenv('PSU_COMMON_ALLOW_DEMO')!='1':return None
        from .planner import plan_fields
        audits=[]
        def traced_planner(q,records,ids):return plan_fields(q,records,ids,diagnostic=audits.append)
        result=CommonAnswerer(store).answer(question,locale=locale,history=recent_history,planner=traced_planner if allow_llm else None)
        if result is None and snap['release']:
            names=scoped_names(snap)
            _,ids,_=context_query(question,recent_history,names,snap['release']['records'])
            authority=authority_decision(question,snap,ids)
            if authority['decision'] in {'common','blocked'}:
                result=CommonAnswerer(store).finish(snap,time.perf_counter(),'ข้อมูลส่วนนี้ของรายการยังยืนยันไม่ได้ กรุณาระบุหัวข้อเพิ่มเติม / This part of the managed record is not confirmed; please specify the requested detail.',[],{'record_ids':ids,'authority':authority},[],response='clarification')
        if result is not None and audits:
            from dataclasses import replace
            artifact={**(result.decision_artifact or {}),'planner_audits':audits}
            result=replace(result,decision_artifact=artifact,trace=[*result.trace,PipelineTrace('common_query_planner','audited',0.0,'transport/schema/semantic outcome are separate',{'attempts':audits})])
        return result
    except (OSError,sqlite3.Error,ValueError,KeyError,TypeError):
        # Do not invent common facts or silently use a stale indexed release.
        return PipelineAnswer(answer='ฐานข้อมูลกลางยังยืนยันไม่ได้ กรุณาลองใหม่ / Common content is unavailable; please retry.',hits=[],elapsed=0,mode='pipeline:common_unavailable',confidence=0,route=PipelineRoute('knowledge','common_read',0,'no_answer','medium','store unavailable'),entities=EntityBundle(),validation=ValidationResult(True))
