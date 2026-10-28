"""Read installed/offered relations without turning omission into a false fact."""
import re
from .registry import value

def answer(reader,snap,started,ids,question,lang,at):
    from .answer import title,text,effective
    records=snap['release']['records'];games=[rid for rid in ids if records[rid]['kind']=='game'];scopes=[rid for rid in ids if records[rid]['kind'] in {'resource','service','zone'}]
    if not games or not scopes:return None
    wanted_resources={rid for rid in scopes if records[rid]['kind']=='resource'}
    unit_match=re.search(r'\b(?:pc|ps|vr|cockpit)\s*#?\s*\d+',question,re.I);explicit_unit=bool(unit_match)
    wanted_services={rid for rid in scopes if records[rid]['kind']=='service'}
    wanted_zones={rid for rid in scopes if records[rid]['kind']=='zone'}
    hits=[];obs=[];blocks=[];complete=True
    def cite(record,keys):
        labels=[]
        for key in keys:
            f=record['fields'].get(key,{})
            if f.get('status')!='known':continue
            obs.append({'record_id':record['record_id'],'field':key,'status':'known','evidence_refs':f['evidence_refs']})
            for ref in f['evidence_refs']:
                source=snap['release']['sources'][ref['source_id']];label='S'+str(len(hits)+1);labels.append(label)
                hits.append({'id':record['record_id']+':'+key+':'+label,'record_id':record['record_id'],'field':key,'title':title(record,lang),'text':text(f['value'],lang),'source_id':ref['source_id'],'snapshot_sha256':source['sha256'],'locator':ref['locator'],'citation_label':label,'source_url':source.get('public_url') or ''})
        return ''.join('['+s+']' for s in labels)
    for gid in games:
        links=[r for r in records.values() if r['kind']=='game_service' and value(r,'game_id')==gid and effective(r,at,records)]
        yes=[];no=[];available=[]
        for link in links:
            service=records.get(value(link,'service_id'));installed=set(value(link,'installed_resource_ids') or [])
            if value(link,'offered') is True:available.append(link)
            scope_match=value(link,'service_id') in wanted_services
            if wanted_resources and service:scope_match=scope_match or bool(wanted_resources&set(value(service,'resource_ids') or []))
            if not wanted_resources and not explicit_unit:
                resource_zones={value(records[rid],'zone_id') for rid in value(service,'resource_ids') or [] if rid in records} if service else set()
                scope_match=scope_match or bool(resource_zones&wanted_zones)
            if wanted_resources:
                if installed&wanted_resources and value(link,'offered') is True:yes.append(link)
                elif scope_match and value(link,'offered') is False:no.append(link)
            elif not explicit_unit:
                if scope_match and value(link,'offered') is True:yes.append(link)
                elif scope_match and value(link,'offered') is False:no.append(link)
        caption=title(records[gid],lang);target=unit_match[0] if explicit_unit and not wanted_resources else ' / '.join(title(records[rid],lang) for rid in scopes)
        coverage=set().union(*(set(value(link,'installed_resource_ids') or []) for link in yes)) if yes else set()
        if yes and no:
            complete=False;blocks.append(('ข้อมูลขัดกันเกี่ยวกับเกม ' if lang=='th' else 'Conflicting offered/install records for ')+caption+' — '+target)
        elif yes:
            blocks.append(('ยืนยันว่ามีข้อมูลเกม ' if lang=='th' else 'Confirmed game records: ')+caption)
            missing=wanted_resources-coverage
            if missing:
                complete=False;blocks.append(('ยังไม่ยืนยันการติดตั้งบน ' if lang=='th' else 'Installation is still unconfirmed on ')+', '.join(title(records[rid],lang) for rid in missing))
        elif no:blocks.append(('ข้อมูลระบุว่าไม่มีเกมนี้ให้บริการในชุดที่ถาม: ' if lang=='th' else 'The source marks this game as not offered in the selected service: ')+caption+' — '+target)
        else:
            complete=False;blocks.append(('ยังไม่พบ '+target+' ในข้อมูลติดตั้งที่ยืนยันของ '+caption if lang=='th' else 'No confirmed installation for '+caption+' on '+target+' was found.'))
        selected_links=yes+no if yes and no else yes or no or available
        for link in selected_links:
            marker=cite(link,['game_id','service_id','offered','installed_resource_ids']);service=records.get(value(link,'service_id'))
            installed=value(link,'installed_resource_ids')
            detail=title(service,lang) if service else ''
            if installed:detail+=' — '+', '.join(title(records[rid],lang) for rid in installed if rid in records)
            blocks.append(('• ข้อมูลที่ยืนยัน: ' if lang=='th' else '• Confirmed source scope: ')+detail+' '+marker)
    if re.search(r'ตอนนี้|วันนี้|\b(?:now|today|free|available)\b',question,re.I):complete=False
    blocks.append('ข้อมูลนี้ยืนยันรายการเกม/การติดตั้ง ไม่ใช่สถานะช่องจองว่างแบบสด' if lang=='th' else 'This confirms game offerings/installations, not live booking availability.')
    plan={'record_ids':ids,'scope_ids':scopes,'operation':'game_presence','requested_fields':[],'all_fields':False,'method':'declared_game_installation_scope','negative_from_absence':False,'live_availability_asserted':False}
    return reader.finish(snap,started,'\n\n'.join(blocks),hits,plan,obs,response='answer' if complete else 'partial_answer')
