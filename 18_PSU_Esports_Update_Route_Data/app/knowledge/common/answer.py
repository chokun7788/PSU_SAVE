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
from .query_scope import complete_control_notes
from .dialogue import resolve_state,changed_domain
from .query_scope import primary_ids,operation,offered_games,platforms_for,control_text,rule_selection,derived_names,operation_faqs,control_projection,calendar_ids,rental_ids,scoped_live_request,same_platform
from functools import lru_cache
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
 'game':['เกม','game'], 'rate':['ราคา','ค่าบริการ','ค่าเล่น','price','fee','rate'],
 'policy':['กฎ','กฏ','นโยบาย','policy','rules'], 'procedure':['ขั้นตอน','procedure'], 'zone':['โซน','zone'],
 'resource':['อุปกรณ์','เครื่อง','equipment','resources'], 'schedule':['ตารางเวลา','เวลาเปิด','opening hours','schedule'],
 'news':['ข่าว','กิจกรรม','news','events'], 'person':['บุคลากร','ทีมงาน','staff'], 'contact':['ติดต่อ','contact'],
 'center':['ศูนย์อยู่','ที่ตั้ง','center location','studio location'], 'facility':['สิ่งอำนวยความสะดวก','facilities']}
@lru_cache(maxsize=32768)
def normal(s):return normalize(s)
def all_query(q):return broad_request(q)
def live_query(q):return live_request(q)
def text(v,lang):
    if isinstance(v,dict) and set(v)=={'th','en'}:
        chosen=v.get(lang)
        if chosen:return chosen
        fallback=v.get('th' if lang=='en' else 'en') or ''
        if lang=='en' and not re.search(r'[\u0e00-\u0e7f]',fallback):return fallback
        return ('[Translation pending; Thai source] ' if lang=='en' else '[ต้นฉบับอังกฤษ] ')+fallback
    if type(v) is bool:return ('Yes' if v else 'No') if lang=='en' else ('มี/ใช่' if v else 'ไม่มี/ไม่ใช่')
    if isinstance(v,list):return '\n'.join('• '+text(x,lang) for x in v) if v else ('None (confirmed)' if lang=='en' else 'ไม่มี (ยืนยันแล้ว)')
    if isinstance(v,dict):return '; '.join(k+': '+text(x,lang) for k,x in v.items())
    return str(v)
def title(r,lang):
    for k in ('title','name','display_name','event_name','subject','question','heading','mode_name','topic','value'):
        if value(r,k) is not None:
            v=value(r,k);shown=text(v,lang)
            if r.get('kind')=='faq' and k=='question':shown=shown.replace('.*',' — ')
            if r.get('kind')=='game' and lang=='th' and isinstance(v,dict) and v.get('en') and v.get('en')!=v.get('th'):shown+=' ('+v['en']+')'
            return shown
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
        # Optional context (including a superseded edition) does not determine
        # the lifetime of an independent current fact. Normative dependencies do.
        if spec['reference_kind'] and (spec['publish_core'] or spec['key']=='depends_on_ids') and value(r,spec['key']) is not None:
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
            exact.extend((rid,m.start(),m.end()) for m in re.finditer(pattern,q))
    if exact:
        # Suppress only an actually observed nested mention. An unobserved
        # shared alias (e.g. the same platform) cannot erase a second target.
        keep=[rid for rid,start,end in exact if not any(other!=rid and a<=start and end<=b and b-a>end-start for other,a,b in exact)]
        return list(dict.fromkeys(keep)), 'exact'
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
            matcher=SequenceMatcher(None,'',a)
            from collections import Counter
            aq=Counter(a);qq=Counter(q)
            if 2*sum(min(n,qq[c]) for c,n in aq.items())/(2*len(a)-1)<.88:continue
            for size in (len(a)-1,len(a),len(a)+1):
                for i in range(max(0,len(q)-size+1)):
                    span=q[i:i+size]
                    if re.search('[a-z]',a):
                        if i and q[i-1].isascii() and q[i-1].isalnum():continue
                        if i+size<len(q) and q[i+size].isascii() and q[i+size].isalnum():continue
                    if (i>0 and q[i-1].isdigit() and span[:1].isdigit()) or (i+size<len(q) and q[i+size].isdigit() and span[-1:].isdigit()):continue
                    if re.findall(r'\d+',span)!=re.findall(r'\d+',a):continue
                    matcher.set_seq1(span)
                    if matcher.real_quick_ratio()<.88 or matcher.quick_ratio()<.88:continue
                    s=matcher.ratio()
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
        if state:return state.get('query',question),state['record_ids'],state['method']
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
    def answer(self,question,*,locale='th',history=None,at=None,planner=None,_composing=False):
        started=time.perf_counter();snap=self.store.snapshot();rel=snap['release']
        if not rel:return None
        from app.calendar.service_calendar import now_bangkok
        lang='en' if locale=='en' else 'th';at=at or now_bangkok()
        if at.tzinfo is None:raise ValueError('Query time needs timezone')
        records={k:r for k,r in rel['records'].items() if k not in snap['withdrawn']}
        names=derived_names(scoped_names(snap),records)
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
        if not _composing:
            from .composition import parts,compose
            entity_ids=[rid for rid in ids if records[rid]['kind'] not in {'faq','policy','procedure'}]
            clauses=parts(strip_names(question,entity_ids,names))
            if clauses and ids:return compose(self,snap,started,clauses,ids,lang=lang,history=history,at=at,planner=planner)
        matched_ids=list(ids)
        ids,query_operation=primary_ids(question,ids,records)
        if method=='state_comparison_selection':query_operation='price'
        roles={'price':{'service','resource','zone','game','audience','rate'},'rental':{'rental_package','zone','service','resource','audience'},'controls':{'game','control_set'},'games':{'game','service','resource','zone'},'equipment':{'equipment_model','resource','service','zone'},'booking':{'service','resource','zone','game'},'people':{'person'}}
        if query_operation in roles and method!='state_comparison_selection':
            role_ids,_=named(question,{rid:aliases for rid,aliases in names.items() if rid in records and records[rid]['kind'] in roles[query_operation]},allow_fuzzy=False)
            if role_ids:ids,query_operation=primary_ids(question,role_ids,records)
        comparison_audit=None
        if query_operation=='price':
            from .price_comparison import requested as comparison_requested,groups_for_roots,ROOT_KINDS
            if comparison_requested(q):
                from .audience_scope import resolve as resolve_comparison_audience
                roots=[rid for rid in ids if records[rid]['kind'] in ROOT_KINDS];audiences,_=resolve_comparison_audience(question,records)
                audiences=list(dict.fromkeys((audiences or [])+[rid for rid in ids if records[rid]['kind']=='audience']))
                if roots and re.search(r'ทุกกลุ่ม|แต่ละกลุ่ม|\ball (?:groups|audiences)\b',normal(question)):audiences=groups_for_roots(records,roots)
                from .query_contract import matches
                anchors={max((normal(alias) for alias in names[rid] if matches(normal(question),alias)),key=len,default='') for rid in roots};anchors.discard('')
                from .dialogue import previous_state
                prior_comparison=(previous_state(history,records) or {}).get('price_comparison')
                axis=prior_comparison.get('axis','audience') if method=='state_comparison_selection' and isinstance(prior_comparison,dict) else ('service' if len(anchors)>=2 else 'audience')
                missing=(['at_least_two_services'] if axis=='service' and len(roots)<2 else ['service'] if not roots else [])+(['audience'] if axis=='service' and not audiences else ['at_least_two_explicit_audiences'] if axis=='audience' and len(audiences)<2 else [])
                comparison_audit={'scope_ids':roots,'audience_ids':audiences,'axis':axis,'missing':missing,'guest_group_assumed':False}
                if missing:
                    labels={'service':('บริการ','the service'),'at_least_two_services':('บริการทั้งสองฝั่ง','both services'),'audience':('กลุ่มผู้ใช้','the audience group'),'at_least_two_explicit_audiences':('กลุ่มผู้ใช้ทั้งสองฝั่ง','both audience groups')}
                    needs=[labels[x][lang=='en'] for x in missing]
                    msg=('กรุณาระบุ'+' และ'.join(needs)+'ที่ต้องการเปรียบเทียบราคาครับ') if lang=='th' else ('Please specify '+' and '.join(needs)+' to compare prices.')
                    return self.finish(snap,started,msg,[],{'record_ids':list(dict.fromkeys(roots+audiences)),'requested_fields':['amount_minor'],'operation':'price','method':'price_comparison_missing_scope','price_comparison':comparison_audit},[],response='clarification')
                ids=list(dict.fromkeys(roots+audiences));method='common_price_comparison';q='price'
        scope_ids=list(ids)
        audience_audit=None
        if comparison_audit is None and (query_operation in {'price','rental'} or re.search(r'งบ|มีเงิน|\b(?:budget|afford|spend)\b',normal(question))):
            from .audience_scope import resolve as resolve_audience
            audiences,audience_audit=resolve_audience(question,records)
            if audiences is not None:
                ids=[rid for rid in ids if records[rid]['kind']!='audience']+audiences;scope_ids=list(ids)
                if not audiences and audience_audit['concepts']:
                    msg='ยังไม่พบกลุ่มผู้ใช้ที่ตรงคำถามในข้อมูลราคา กรุณาระบุกลุ่มที่ใช้บริการ' if lang=='th' else 'No matching audience group is recorded for this price question. Please specify the applicable group.'
                    return self.finish(snap,started,msg,[],{'record_ids':ids,'audience_selection':audience_audit,'method':'unresolved_audience_scope'},[],response='clarification')
        if live_query(question):return None
        if query_operation=='game_presence':
            from .game_presence import answer as game_presence_answer
            return game_presence_answer(self,snap,started,ids,question,lang,at)
        if live_query(question) or scoped_live_request(question,ids,records):return None
        if query_operation=='calendar':
            calendar_scope,target_date=calendar_ids(question,records,at)
            if calendar_scope:
                ids=calendar_scope;scope_ids=list(ids);method='common_calendar_date_scope'
                # Closure validity is evaluated at the requested local date.
                if any(records[rid]['kind']=='closure' for rid in ids):
                    from zoneinfo import ZoneInfo
                    at=datetime.combine(target_date,datetime.min.time(),tzinfo=ZoneInfo('Asia/Bangkok'))
        if query_operation=='people':
            if not ids:ids=[rid for rid,r in records.items() if r['kind']=='person']
            if ids and all(records[rid]['kind']=='person' for rid in ids):method='common_people_directory'
        if query_operation=='rental':
            packages=rental_ids(question,ids,records)
            if packages:ids=packages;method='common_rental_scope'
        from .dialogue import previous_state
        prior_context=previous_state(history,records)
        procedure_query=question
        if query_operation is None and prior_context and prior_context.get('operation')=='booking' and re.search(r'สรุป|ทำ(?:ไง|ยังไง|อย่างไร)|\b(?:summary|summarize|so how|then how|steps)\b',normal(question)):
            query_operation='booking';procedure_query='booking steps'
            scope_ids=list(prior_context.get('scope_ids') or ids)
        if query_operation in {'booking','price'} and prior_context and not any(records[rid]['kind']=='game' for rid in ids):
            prior_games=[rid for rid in prior_context['record_ids'] if records[rid]['kind']=='game']
            linked={value(r,'game_id') for r in records.values() if r['kind']=='game_service' and value(r,'service_id') in ids and value(r,'offered') is True}
            scope_ids=list(dict.fromkeys(scope_ids+[rid for rid in prior_games if rid in linked]))
        secondary_audit=None;secondary_ids=None
        if ids and query_operation in {None,'policy'} and not all_query(question) and all(records[rid]['kind'] in {'game','resource','service','zone','equipment_model'} for rid in ids):
            owned=field_requests(strip_names(question,ids,names),scope_kinds({records[rid]['kind'] for rid in ids}))
            if not owned and all(effective(records[rid],at,records) for rid in ids):
                from .scoped_topics import lookup
                secondary_ids,secondary_audit=lookup(question,{rid:r for rid,r in records.items() if effective(r,at,records)},names,ids,allow_llm=planner is not None)
                if secondary_ids:ids=secondary_ids;method='declared_scoped_topic'
        procedure_ids=operation_faqs(procedure_query,records,query_operation) if not secondary_ids else []
        if procedure_ids:
            # Prefer the requested language when duplicate migrated textual rows exist.
            localized=[rid for rid in procedure_ids if (value(records[rid],'answer') or {}).get(lang)]
            from .provenance import owner_basis
            from .entity_search import grams
            candidates=localized or procedure_ids
            candidates.sort(key=lambda rid:(owner_basis(records[rid],self.store,rel),len(grams(question)&grams(text(value(records[rid],'question') or {},lang)))),reverse=True)
            ids=candidates[:1];method='common_faq_topic' if query_operation=='policy' else 'common_procedure_topic'
            if query_operation not in {'checkin','policy'}:query_operation='booking'
        missing_policy_topic=None
        if re.search(r'อายุ|ผู้ปกครอง|\b(?:minimum age|age limit|years? old|guardian|parental)\b',normal(question)):missing_policy_topic=('อายุขั้นต่ำ/ผู้ปกครอง','minimum age / guardian requirements')
        elif re.search(r'กลับบ้าน|\btake home\b',normal(question)):missing_policy_topic=('การยืมอุปกรณ์กลับบ้าน','borrowing equipment to take home')
        if query_operation=='policy' and missing_policy_topic and ids and all(records[rid]['kind'] in {'game','resource','service','zone','equipment_model'} for rid in ids) and not field_requests(strip_names(question,ids,names),scope_kinds({records[rid]['kind'] for rid in ids})):
            caption=' / '.join(title(records[rid],lang) for rid in ids)
            msg=('ยังไม่มีข้อมูลยืนยันนโยบาย'+missing_policy_topic[0]+' สำหรับ '+caption+' กรุณาติดต่อเจ้าหน้าที่เพื่อยืนยันครับ') if lang=='th' else ('Policy is not confirmed for '+missing_policy_topic[1]+' on '+caption+'. Please contact staff to confirm.')
            return self.finish(snap,started,msg,[],{'record_ids':ids,'scope_ids':scope_ids,'operation':'policy','method':'common_policy_unconfirmed','missing_policy_topic':missing_policy_topic[lang=='en'],'semantic_correctness_verified':False},[],response='partial_answer')
        if query_operation=='games':
            roots=[rid for rid in ids if records[rid]['kind'] in {'service','resource','zone'}]
            catalog_ids=offered_games(roots,records)
            if catalog_ids and (roots or not ids):
                obs=[];hits=[];lines=[]
                for rid in catalog_ids:
                    game=records[rid]
                    if not active(game,at):continue
                    f=game['fields']['title'];lines.append('• '+title(game,lang))
                    obs.append({'record_id':rid,'field':'title','status':f['status'],'evidence_refs':f['evidence_refs']})
                    for e in f['evidence_refs']:
                        src=rel['sources'][e['source_id']];hits.append({'id':rid+':title','record_id':rid,'field':'title','title':title(game,lang),'text':text(f['value'],lang),'source_id':e['source_id'],'snapshot_sha256':src['sha256'],'locator':e['locator'],'source_url':src['public_url'] or ''})
                caption=' / '.join(title(records[rid],lang) for rid in roots)
                msg=('เกมที่มีให้เล่น' if lang=='th' else 'Offered games')+(' — '+caption if caption else '')+': '+str(len(lines))+'\n'+'\n'.join(lines)
                return self.finish(snap,started,msg,hits,{'record_ids':roots or catalog_ids,'requested_fields':[],'all_fields':False,'method':'offered_game_service_catalog','catalog_game_ids':catalog_ids,'scope_ids':roots},obs,response='list')
        budget=budget_request(q,{rid:r for rid,r in records.items() if effective(r,at,records)},[rid for rid in ids if effective(records[rid],at,records)])
        if budget is not None:
            ids=[row['rate_id'] for row in budget['rows']];method=budget['method']
            if not ids:
                msg='ยังไม่มีราคาที่ได้รับการยืนยันว่าตรงงบนี้ ไม่ได้แปลว่าไม่มีอุปกรณ์ว่าง / No confirmed rate matches this budget; this is not live availability.'
                return self.finish(snap,started,msg,[],{'budget':budget},[],response='list')
        entity_audit=None
        if not ids and query_operation not in {'rules','price','rental'} and re.search(r'ศูนย์|สตูดิโอ|\b(?:studio|cent(?:er|re))\b',normal(q)) and 'address' in field_requests(q) and not re.search(r'ติดต่อ|หา.{0,12}ไม่เจอ|\b(?:contact|cannot find|can.t find)\b',normal(q)):
            ids=[rid for rid,r in records.items() if r['kind']=='center' and effective(r,at,records)]
            if ids:scope_ids=list(ids);method='common_typed_attribute_scope'
        if not ids and planner and budget is None and not live_query(q) and not all_query(q) and not re.search(r'อะไรบ้าง|มีเกมอะไร|\blist\b|what games|which games|(?:what|which)\b.*\b(?:prices|fees|rates)\b',q,re.I):
            from .entity_search import select
            choice,entity_audit=select(q,{rid:r for rid,r in records.items() if effective(r,at,records)},names)
            if choice is None and (entity_audit.get('reason')=='model_busy' or entity_audit.get('error')):
                return self.finish(snap,started,'ระบบยังเลือกข้อมูลให้คำถามนี้ไม่ทัน กรุณาลองอีกครั้ง / The model could not select the relevant data in time; please retry.',[],{'entity_selection':entity_audit},[],response='retry')
            if isinstance(choice,list):ids=choice;method='published_semantic_candidates'
            elif isinstance(choice,dict) and choice.get('ambiguous'):
                options=choice['ambiguous']
                return self.finish(snap,started,('หมายถึงรายการไหน: ' if lang=='th' else 'Which record do you mean: ')+ ' / '.join(title(records[x['record_id']],lang) for x in options),[],{'pending_selection':{'record_ids':[x['record_id'] for x in options],'requested_fields':field_requests(question)},'entity_selection':entity_audit},[],response='clarification')
        q=strip_names(q,list(dict.fromkeys(ids+matched_ids)),names) if ids else normal(q)
        # For unique repetition recovery strip the actually observed noisy span.
        if method=='unique_repeat_edit':
            for rid in ids:
                for alias in names[rid]:
                    a=normal(alias)
                    for i in range(len(a)):
                        if not a[i].isdigit():q=q.replace(a[:i]+a[i]+a[i:],' ')
            q=normal(q)
        current_kinds={records[k]['kind'] for k in ids}
        if current_kinds:
            from .schema_language import recover_schema_language
            q,schema_recoveries=recover_schema_language(q,scope_kinds(current_kinds))
        else:schema_recoveries=[]
        q,focus=focus_request(q,current_kinds or None)
        broad=all_query(q);requested=field_requests(q);kind=None
        if method in {'state_audience_selection','state_service_selection','typed_common_state'} and (not requested or broad):
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
            listing=query_operation!='policy' and bool(re.search(r'อะไรบ้าง|มีอะไร|what .*games|which games|(?:what|which)\b.*\b(?:prices|fees|rates)\b|\blist\b',q,re.I))
            for k,terms in KIND_TERMS.items():
                if any(t in normal(q) for t in terms) and (broad or listing or k in {'center','contact','schedule'} and requested):kind=k;break
            if not kind:
                kind=next((k for field,k in [('address','center'),('value','contact'),('open_periods','schedule'),('bookable_periods','schedule')] if field in requested),None)
            if not kind:return None
            ids=[k for k,r in records.items() if r['kind']==kind and (kind=='rate' or effective(r,at,records))]
            if not ids:return None
            if listing:broad=not requested or broad_request(q)
        # Operational live availability remains with the existing live adapter.
        if live_query(q):return None
        field_kinds=scope_kinds({records[k]['kind'] for k in ids})
        requested=((['amount_minor','period_label','duration_minutes','equipment_included'] if budget.get('kind_scope')=='rental_package' else ['amount_minor','unit','calculation_rule','duration_minutes']) if budget is not None else discovery_requested or field_requests(q,field_kinds))
        if method=='common_calendar_date_scope':
            requested=(['state','reason','open_periods','bookable_periods'] if any(records[rid]['kind']=='closure' for rid in ids) else field_requests(q,{'schedule'}) or ['bookable_periods','maintenance_periods']);broad=False
        if method=='common_people_directory':requested=['display_name','team','role'];broad=False
        if query_operation=='equipment' and not requested and not broad:requested=['specifications','usage']
        if query_operation=='controls' and not requested and not broad:requested=['bindings']
        if query_operation=='price' and not requested and not broad:requested=['amount_minor']
        if method=='common_rental_scope' and not requested and not broad:requested=['amount_minor','equipment_included','terms'];broad=False
        if query_operation=='game_overview' or (any(records[rid]['kind']=='game' for rid in ids) and re.fullmatch(r'(?:เกม|game)\s*[?!.,]*',q)):
            requested=[key for key in ('summary','genre','how_to_play') if any(value(records[rid],key) is not None for rid in ids)] or ['title'];broad=False
        if method in {'common_procedure_topic','common_faq_topic'}:requested=['answer'];broad=False
        if method=='declared_scoped_topic':
            defaults={'faq':['answer'],'policy':['decision','details','conditions_all','exceptions','consequence'],'procedure':['steps','preconditions','required_documents']}
            requested=list(dict.fromkeys(f for rid in ids for f in defaults[records[rid]['kind']] if f in records[rid]['fields'] and (f in {'answer','decision','details','conditions_all','steps','preconditions'} or records[rid]['fields'][f]['status']=='known')));broad=False
        if method=='exact' and not broad and requested in ([],['answer']) and all(records[rid]['kind']=='faq' for rid in ids) and re.fullmatch(r'(?:\s|[?!.,]|ทำ|ต้อง|การ|ยังไง|ยังงัย|อย่างไร|ติดต่อ|คือ|อะไร|ครับ|ค่ะ|คะ|อ่า+|หน่อย|please|what|is|it|how|do|i|the|tell|me)*',normal(q)):
            requested=['answer'];method='common_named_faq_content'
        if not requested and not broad and method=='exact' and all(records[rid]['kind']=='faq' for rid in ids):requested=['answer']
        if method=='published_semantic_candidates' and all(records[rid]['kind']=='faq' for rid in ids):requested=['answer']+(['scope_note'] if 'scope_note' in field_requests(q,{'faq'}) else [])
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
        plan={'record_ids':ids,'requested_fields':requested,'all_fields':broad,'method':method,'scope':'common_published','platform':None,'query_without_entity':q,'operation':query_operation,'scope_ids':scope_ids,'field_selection':resolve_fields(q,field_kinds)[1],'confidence_calibrated':False,'request_focus':focus,'schema_language_recoveries':schema_recoveries}
        billing_query=raw_query
        if 'amount_minor' in requested and method.startswith(('state_audience_selection','state_service_selection','typed_price_duration_selection','typed_common_state','state_comparison_selection','common_price_comparison')):
            from .dialogue import previous_state
            from app.calculator.service_fee import _detect_minutes
            previous=previous_state(history,records) or {};constraints=previous.get('constraints');duration=constraints.get('duration_minutes') if isinstance(constraints,dict) else None
            if _detect_minutes(raw_query) is None and type(duration) is int and 0<duration<=1440:
                billing_query=raw_query+' '+str(duration)+' minutes';plan['inherited_constraints']={'duration_minutes':duration};plan['duration_constraint_supplied']=True
        if broad and not kind:requested=[];plan['requested_fields']=[]
        if any(records[rid]['kind']=='competition' for rid in ids):
            from app.pipeline.competition_taxonomy import detect_competition_facet
            if (detect_competition_facet(raw_query) or query_operation=='rules') and not (broad and not re.search(r'กฎ|กฏ|กติกา|\b(?:rules|rulebook)\b',q)):
                requested=['text'];plan['requested_fields']=requested;plan['all_fields']=False;broad=False
                plan['rule_content_all']=broad_request(q) or overview_request(q) or bool(re.search(r'มีอะไร(?:บ้าง|มั่ง)|ทั้งหมด|(?:what|which)\s+(?:are\s+)?(?:the\s+)?rules\s*(?:of|for|in|do)?\s*$',q)) or bool(re.fullmatch(r'(?:กฎ|กฏ|กติกา|rules|rulebook|ตอน|แข่ง|\s|[?!.,])+',q))
        if 'amount_minor' in requested and re.search(r'\d+\s*(?:นาที|minutes?|mins?|ชั่วโมง|hours?)',raw_query,re.I):
            plan['duration_constraint_supplied']=True
            requested=[f for f in requested if f!='duration_minutes'];plan['requested_fields']=requested
        plan['authority']=authority_decision(raw_query,snap,ids)
        if plan['authority']['decision']=='defer':return None
        if plan['authority']['decision']=='blocked':
            return self.finish(snap,started,'ข้อมูลราคาที่เกี่ยวข้องถูกถอนแล้ว / The related price has been withdrawn.',[],plan,[],response='withdrawn')
        if entity_audit:plan['entity_selection']=entity_audit
        if secondary_audit:plan['scoped_topic_selection']=secondary_audit
        if audience_audit:plan['audience_selection']=audience_audit
        if comparison_audit:plan['price_comparison']=comparison_audit
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
        if query_operation=='rules' and plan.get('rule_content_all') is not None:
            review=False;gaps=[]
        if method in {'common_calendar_date_scope','common_people_directory','common_procedure_topic','common_faq_topic','declared_scoped_topic','common_named_faq_content','common_typed_attribute_scope','typed_price_duration_selection','state_audience_selection','common_price_comparison'}:review=False;gaps=[]
        plan['unresolved_clauses']=gaps if review and not broad and not overview else []
        if method in {'common_calendar_date_scope','common_people_directory'}:review=False;gaps=[]
        if method in {'common_procedure_topic','published_semantic_candidates'} and all(records[rid]['kind']=='faq' for rid in ids):plan['unresolved_clauses']=[];review=False
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
        # Preserve an explicit platform after operation parsing has removed
        # service aliases. Mask game titles only, so titles cannot imply devices.
        platform_query=strip_names(raw_query,[rid for rid in matched_ids if records[rid]['kind']=='game'],names)
        for p in platforms:
            if re.search(r'(?<![a-z0-9])'+re.escape(p)+r'(?![a-z0-9])',platform_query,re.I):plan['platform']=p;break
        # A named device outside published platforms must not inherit PC controls.
        device=re.search(r'(?<![a-z0-9])(?:playstation\s*|ps\s*)(\d+)(?![a-z0-9])',platform_query,re.I)
        if device:plan['platform']='PS'+device.group(1)
        if not plan['platform']:
            scoped_platforms=set().union(*(platforms_for(records[rid],records) for rid in scope_ids)) if scope_ids else set()
            if len(scoped_platforms)==1:plan['platform']=next(iter(scoped_platforms))
        if plan['platform'] and 'supported_platforms' in requested:plan['requested_platform']=plan['platform']
        if kind and broad and requested:
            # "All games and their platforms" asks for all records, not every
            # field in each record. A plain list still returns all titles.
            broad=False;plan['all_fields']=False;plan['list_scope']=True
        plan['read_contract']=build_needs(raw_query,field_kinds,requested,model=plan['semantic_plan_accepted'],unresolved=plan['unresolved_clauses'])
        plan['response_projection']=[]
        if method=='common_procedure_topic' and re.search(r'ต่อวัน|\b(?:daily|per day)\b',normal(raw_query)):
            plan['scope_limits']=[{'requested':'per_day','available_source_scope':'per_booking','daily_limit_verified':False}]
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
        if plan.get('scope_limits'):blocks.append('ข้อมูลที่ยืนยันได้เป็นจำนวนรอบต่อการจองหนึ่งครั้ง ยังไม่มีข้อมูลยืนยันเพดานต่อวัน' if lang=='th' else 'The confirmed limit applies per booking. A daily limit has not been confirmed.')
        if query_operation in {'price','booking'} and scope_ids and any(records[rid]['kind']=='game' for rid in scope_ids) and not any(records[rid]['kind']=='game' for rid in selected):
            blocks.append(('เกมที่เกี่ยวข้อง: ' if lang=='th' else 'Related game: ')+ ' / '.join(title(records[rid],lang) for rid in scope_ids if records[rid]['kind']=='game'))
        if method in {'common_procedure_topic','common_faq_topic','declared_scoped_topic'} and scope_ids:
            blocks.append(('บริการที่ถาม: ' if lang=='th' else 'Selected service/game: ')+ ' / '.join(title(records[rid],lang) for rid in scope_ids))
        for r in selected.values():
            if r['kind']=='game':blocks.append(('ข้อมูลเกม: ' if lang=='th' else 'Game: ')+title(r,lang))
            if r['kind']=='competition':
                game=records.get(value(r,'game_id'));name=title(game,lang) if game else title(r,lang)
                blocks.append(('กติกา ' if lang=='th' else 'Competition rules: ')+name+' — '+title(r,lang))
        def add(r,keys):
            rows=[]
            if not effective(r,at,records):
                caption=title(r,lang)
                if r['kind']=='rate':
                    srv=records.get(value(r,'service_id'));aud=records.get(value(r,'audience_id'))
                    caption+=' — '+(title(srv,lang) if srv else '')+' / '+(title(aud,lang) if aud else '')
                interval=r['validity'];until=interval.get('effective_until');since=interval.get('effective_from')
                when=(' (recorded validity: '+str(since or '?')+' until (exclusive) '+str(until or '?')+')' if lang=='en' else ' (ช่วงมีผลที่บันทึก: '+str(since or '?')+' ถึงก่อน '+str(until or '?')+')') if since or until else ''
                blocks.append('**'+caption+'**\n'+('This revision or a referenced record is not effective at the query time; no current fact is asserted.' if lang=='en' else 'ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้')+when)
                obligations.append({'record_id':r['record_id'],'field':'validity','status':'not_current'});return
            for key in keys:
                if (r['record_id'],key) in rendered_fields:continue
                f=r['fields'].get(key)
                if f is None:continue
                rendered_fields.add((r['record_id'],key))
                display_label=label(r['kind'],key,lang)
                status=f['status'];v=f['value']
                spec=next((s for s in CATALOG[r['kind']]['fields'] if s['key']==key),{})
                if status=='known' and spec.get('reference_kind'):
                    refs=v if isinstance(v,list) else [v]
                    if any(ref not in records or not effective(records[ref],at,records) for ref in refs):
                        rows.append('• '+display_label+': '+('Referenced information is not current; no current detail is asserted.' if lang=='en' else 'ข้อมูลที่เชื่อมยังไม่มีผลหรือหมดอายุ จึงยังยืนยันรายละเอียดปัจจุบันไม่ได้'))
                        obligations.append({'record_id':r['record_id'],'field':key,'status':'not_current'});continue
                partial=control_text(r,key)
                if partial is not None:
                    f=partial;status='known';v=f['value']
                    plan.setdefault('representation_adapters',[]).append({'record_id':r['record_id'],'requested':'bindings','read':'limitations','gesture':'unknown','reason':'lossless_R63_partial_controls'})
                if status=='known':
                    if key=='amount_minor':out=f'{v//100:,}.{v%100:02d} '+str(value(r,'currency') or 'THB')
                    elif key=='bindings' and partial is not None:
                        display,pending=complete_control_notes(v,lang)
                        out=control_projection(display,raw_query,lang) or text(display,lang)
                        shown_pending=out.count('[Translation pending; Thai source]') if pending else 0
                        if shown_pending:
                            plan.setdefault('localization_gaps',[]).append({'record_id':r['record_id'],'field':'limitations','displayed_pending_note_rows':shown_pending,'source_language':'th','target_language':'en'})
                            plan.setdefault('scope_limits',[]).append('control_note_translation_pending')
                    elif key=='bindings':
                        out='\n'.join('• '+text(b['action'],lang)+' → '+', '.join(b['buttons'])+' ('+b['gesture']+'; '+text(b['context'],lang)+')' for b in v)
                    elif key=='steps':out='\n'.join(str(s['order'])+'. '+text(s['instruction'],lang)+((' — '+title(records[s['contact_id']],lang)) if s['contact_id'] in records else '') for s in sorted(v,key=lambda x:x['order']))
                    elif key.endswith('_id') or key.endswith('_ids'):
                        targets=v if isinstance(v,list) else [v];out=', '.join(title(records[x],lang) if x in records else x for x in targets)
                        if key=='zone_ids' and r['kind'] in {'schedule','closure'} and v==[]:out='All zones' if lang=='en' else 'ทุกโซน'
                        elif v==[]:out='No linked records in this field (confirmed)' if lang=='en' else 'ไม่มีรายการที่เชื่อมในช่องนี้ (ยืนยันแล้ว)'
                    elif key in {'open_periods','bookable_periods','maintenance_periods'} and v:out=' / '.join(period['start']+'–'+period['end'] for period in v)
                    elif key=='conditions_all':out=conditions_text(v,lang,text)
                    elif isinstance(v,list) and not v:out='No entries in this field (confirmed)' if lang=='en' else 'ไม่มีรายการในช่องนี้ (ยืนยันแล้ว)'
                    else:out=enum_text(key,v,lang) or text(v,lang)
                    refs=f['evidence_refs'];labels=[]
                    for ref in refs:
                        src=rel['sources'][ref['source_id']];citation='S'+str(len(hits)+1)
                        hits.append({'id':r['record_id']+':'+key+':'+citation,'record_id':r['record_id'],'field':key,'title':'ข้อมูลศูนย์ที่ผ่านการอนุมัติ' if lang=='th' else 'Approved center information','source_url':src['public_url'] or '', 'text':text(v,lang),'source_id':src['source_id'],'snapshot_sha256':src['sha256'],'citation_label':citation,'locator':ref['locator']});labels.append(citation)
                    rows.append('• '+display_label+': '+out+' '+''.join('['+s+']' for s in labels))
                    if key=='amount_minor' and r['kind']=='rate':
                        from .billing import calculate,render
                        calculation=calculate(r,billing_query)
                        if calculation:
                            rows.append('• '+render(calculation,lang));plan.setdefault('price_calculations',[]).append(calculation)
                        if r['validity']['state']=='unknown':
                            rows.append('• ช่วงมีผลของอัตราที่บันทึกนี้: ต้นฉบับยังไม่ระบุ จึงยังไม่ยืนยันว่าเป็นราคาปัจจุบัน' if lang=='th' else '• Effective period of this recorded rate: not specified in the source; current applicability is not confirmed.')
                            obligations.append({'record_id':r['record_id'],'field':'validity','status':'unknown','reason':'source_has_no_confirmed_effective_date'})
                else:rows.append('• '+display_label+': '+({'unknown':'Not yet confirmed','not_applicable':'Not applicable','conflicted':'Conflicting sources; needs a decision'}[status] if lang=='en' else {'unknown':'ยังไม่มีข้อมูลยืนยัน','not_applicable':'ไม่เกี่ยวข้องกับรายการนี้','conflicted':'หลักฐานขัดกัน ต้องตัดสินใจก่อน'}[status]))
                obligations.append({'record_id':r['record_id'],'field':key,'status':status,'evidence_refs':f['evidence_refs']})
            if rows:blocks.append('**'+title(r,lang)+'**\n'+'\n'.join(rows))
        for rid,r in selected.items():
            if not effective(r,at,records):add(r,[]);continue
            keys=list(r['fields']) if broad else [k for k in requested if k in r['fields']]
            if not keys and not requested:keys=[s['key'] for s in CATALOG[r['kind']]['fields'] if s['publish_core'] or s['key'] in {'summary','how_to_play'}]
            keys,basis=project(r,keys,full=broad)
            if r['kind']=='game' and 'genre' in keys and value(r,'genre') is None and value(r,'summary') is not None:
                keys=list(dict.fromkeys(keys+['summary']));basis['summary']='source_description_when_structured_genre_unknown'
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
                    children=[rr for rr in records.values() if rr['kind']==childkind and value(rr,'game_id')==rid and (not plan['platform'] or same_platform(value(rr,'platform'),plan['platform']) or rr['kind']=='game_service' and same_platform(value(records.get(value(rr,'service_id'),{'fields':{}}),'platform'),plan['platform']))]
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
                if r['kind']=='audience' and any(rr['kind']!='audience' for rr in selected.values()):continue
                related=related_rates(records,r,audiences=audiences,platform=plan['platform'])
                if r['kind']=='zone' and re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|rent|package|half.day|full.day)\b',raw_query,re.I):
                    related=[rr for rr in records.values() if rr['kind']=='rental_package' and rid in (value(rr,'zone_ids') or []) and (not audiences or value(rr,'audience_id') in audiences)]
                for rr in related:
                    pricekeys,pricebasis=project(rr,requested,full=broad);add(rr,pricekeys)
                    plan['response_projection'].append({'record_id':rr['record_id'],'fields':pricebasis})
                if not related:
                    blocks.append(('No confirmed price for ' if lang=='en' else 'ยังไม่มีราคายืนยันสำหรับ ')+title(r,lang))
                    obligations.append({'record_id':rid,'field':'amount_minor','status':'unknown','evidence_refs':[],'reason':'missing_declared_rate_in_scope'})
            if r['kind']=='competition' and (broad or set(requested)&{'text','details','depends_on_ids','completeness'}):
                children=[rr for rr in records.values() if rr['kind']=='competition_rule' and value(rr,'competition_id')==rid]
                children,rule_audit=rule_selection(q,children,full=plan.get('rule_content_all',False) or broad)
                plan.setdefault('rule_selection',[]).append({'competition_id':rid,**rule_audit,'selected_ids':[c['record_id'] for c in children]})
                if not children:
                    blocks.append('ยังไม่พบข้อกฎที่ยืนยันหัวข้อนี้ในเอกสารที่เลือก' if lang=='th' else 'No verified clause for this topic was found in the selected rulebook.')
                    obligations.append({'record_id':rid,'field':'text','status':'unknown','evidence_refs':[]})
                for child in children:
                    add(child,['heading','text'])
                    for dep in value(child,'depends_on_ids') or []:
                        if dep in records and value(records[dep],'competition_id')==rid:add(records[dep],['heading','text'])
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
                if key=='amount_minor' and any(o['field']=='validity' and o['status']=='not_current' for o in obligations):
                    obligations.append({'record_id':ids[0] if ids else None,'field':key,'status':'not_current','evidence_refs':[],'reason':'declared_rate_outside_validity'})
                    blocks.append('ราคาปัจจุบันยังยืนยันไม่ได้จากอัตราที่หมดอายุแล้ว' if lang=='th' else 'The current price cannot be confirmed from expired rates.')
                    continue
                # Do not call an unsupported schema request an unknown owner fact.
                obligations.append({'record_id':None,'field':key,'status':'unsupported_scope'})
                shown=next((label(k,key,lang) for k in sorted(field_kinds) if any(f['key']==key for f in CATALOG[k]['fields'])),key.replace('_',' '))
                blocks.append((shown+': No confirmed answer for this detail in the selected scope.' if lang=='en' else shown+': ยังไม่มีคำตอบที่ยืนยันได้สำหรับรายละเอียดนี้ในขอบเขตที่เลือก'))
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
        if comparison_audit:
            from .price_comparison import summaries
            comparisons=summaries(records,comparison_audit['scope_ids'],comparison_audit['audience_ids'],at,comparison_audit['axis']);plan['price_comparison']['results']=comparisons
            for row in comparisons:
                target=row.get('service_id') or row.get('audience_id');caption=title(records[target],lang) if target in records else ('บริการที่เลือก' if lang=='th' else 'Selected service')
                if row['status']=='not_confirmed':
                    blocks.append(caption+(': ยังยืนยันผลเปรียบเทียบไม่ได้ เพราะอัตราปัจจุบันหรือฐานคิดราคายังไม่ครบตรงกัน' if lang=='th' else ': the comparison is not confirmed because current rates or a shared billing basis are not established.'));plan.setdefault('scope_limits',[]).append({'requested':'price_comparison','reason':row['reason']})
                else:blocks.append(caption+(': อัตราฐานที่มีผล '+('เท่ากัน' if row['status']=='equal' else 'ต่างกัน') if lang=='th' else ': current base rates are '+('equal' if row['status']=='equal' else 'different')+' on the same billing basis.'))
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
        if response=='answer':
            substantive=[o for o in obligations if o['field'] in plan.get('requested_fields',[]) and o['status']=='known']
            unavailable=[o for o in obligations if o['field'] in plan.get('requested_fields',[]) and o['status'] in {'unknown','conflicted','unsupported_scope','needs_clarification'}]
            if unavailable:response='partial_answer' if substantive else 'clarification'
            if response=='answer' and any(o['field']=='validity' and o['status']=='unknown' and o.get('reason')=='source_has_no_confirmed_effective_date' for o in obligations):response='partial_answer'
            if response=='answer' and plan.get('scope_limits'):response='partial_answer'
            if not substantive and any(o['status']=='not_current' for o in obligations):response='not_current'
        if errors:response='partial_answer'
        view='evaluation_draft' if snap.get('evaluation_draft_only') else 'synthetic_demo' if snap.get('allow_demo') else 'published'
        from .evidence import enrich_hit
        hits=[enrich_hit(hit,snap,self.store) for hit in hits]
        for hit in hits:
            if view!='published':hit['title']='ร่างข้อมูลทดสอบ / Evaluation draft information' if view=='evaluation_draft' else 'Synthetic fixture information'
            hit['metadata']={**hit.get('metadata',{}),'common_approved':view=='published','content_view':view,'title':hit['title'],'release_id':snap['active']}
        confidence=.8 if response in {'answer','list'} else 0.0
        artifact={'response_type':response,'release_id':snap['active'],'query_plan':plan,'obligations':obligations,'catalog_scope':'common_published','coverage_errors':errors,'confidence_calibrated':False,'validation_scope':'selected fields and evidence, not human intent correctness','content_view':view,'production_publication_verified':view=='published'}
        trace=PipelineTrace('common_content',response,confidence,'typed fields and source-backed joins; uncalibrated confidence',artifact)
        reason={'published':'published common content','evaluation_draft':'unpublished evaluation draft','synthetic_demo':'synthetic demo common content'}[view]
        return PipelineAnswer(answer=answer,hits=hits,elapsed=time.perf_counter()-started,mode='pipeline:common_'+response,confidence=confidence,route=PipelineRoute('knowledge','common_read',confidence,response,'medium',reason),entities=EntityBundle(),validation=ValidationResult(not errors,tuple(errors)),trace=[trace],decision_artifact=artifact)

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
