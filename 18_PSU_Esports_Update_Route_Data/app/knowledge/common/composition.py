"""Bounded common-only operation composition with explicit clause coverage."""
import re
from .query_contract import semantic_clauses,live_request
from .query_scope import operation

def parts(question):
    if live_request(question):return []
    clauses=semantic_clauses(question)
    if not 2<=len(clauses)<=4:return []
    ops=[operation(q) for q in clauses]
    # Noun coordinations (minimum and maximum, keyboard and mouse) are not tasks.
    concrete={op for op in ops if op}
    if len(concrete)<2 or concrete&{'rules'}:return []
    return clauses

def compose(reader,snap,started,clauses,ids,*,lang,history,at,planner):
    records=snap['release']['records']
    roots=[rid for rid in ids if records[rid]['kind'] not in {'faq','policy','procedure'}] or list(ids)
    context={'role':'assistant','common_read_state':{'schema_version':1,'record_ids':roots,'requested_fields':[],'all_fields':False,'release_id':snap['active']}}
    blocks=[];hits=[];obligations=[];children=[];incomplete=[]
    for i,clause in enumerate(clauses,1):
        result=reader.answer(clause,locale=lang,history=[*(history or []),context],at=at,planner=planner,_composing=True)
        if result is None:
            blocks.append(str(i)+'. '+clause+'\n'+('ยังไม่มีคำตอบที่ยืนยันได้สำหรับส่วนนี้' if lang=='th' else 'No verified answer is available for this part.'));incomplete.append(i);continue
        art=result.decision_artifact or {};children.append({'clause':clause,'response_type':art.get('response_type'),'query_plan':art.get('query_plan'),'coverage_errors':art.get('coverage_errors',[])})
        if art.get('response_type') not in {'answer','list'} or not result.validation.ok:incomplete.append(i)
        rename={}
        for hit in result.hits:
            old=hit.get('citation_label');new='S'+str(len(hits)+1)
            if old:rename[old]=new
            hits.append({**hit,'citation_label':new})
        text=re.sub(r'\[(S\d+)\]',lambda m:'['+rename.get(m[1],m[1])+']',result.answer)
        blocks.append(str(i)+'. '+clause+'\n'+text);obligations.extend(art.get('obligations',[]))
    plan={'record_ids':roots,'scope_ids':roots,'requested_fields':[],'all_fields':False,'method':'common_compound_operations','operation':'compound','clauses':children,'incomplete_clause_numbers':incomplete}
    return reader.finish(snap,started,'\n\n'.join(blocks),hits,plan,obligations,response='partial_answer' if incomplete else 'answer')
