"""Offline, user-authorized assistant translation review; no runtime publication.

Original drafts, names and Thai records stay untouched. Failed checks are held.
Local model judgments are AI review evidence, never human/owner approval.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.manage_english_localizations import source_fields
from tools.audit_competition_english_translation_semantics import mechanical_issues
from app.knowledge.localization import source_text_sha256

MANUAL = {
    "ประชาสัมพันธ์": "Public relations officer",
    "ผู้จัดการ": "Manager",
    "กรรมการ": "Committee member",
    "ประธาน": "Chairperson",
    "นักวิชาการคอมพิวเตอร์": "Computer technical officer",
    "คณบดี": "Dean",
    "รองอธิการบดี": "Vice President",
    "ผู้ช่วยอธิการบดีฝ่ายวิชาการ": "Assistant to the President for Academic Affairs",
    "รองประธาน": "Vice Chairperson",
    "อธิการบดี": "University President",
    "เหรัญญิก": "Treasurer",
    "เลขานุการ": "Secretary",
    "นักศึกษาสหกิจ Web & AI Developer": "Cooperative education student — Web & AI Developer",
    "นักศึกษาสหกิจ Game and 3D Developer": "Cooperative education student — Game and 3D Developer",
    "นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer": "Super AI SS6 project intern — AI Chat Bot Developer",
    "มหาวิทยาลัยสงขลานครินทร์": "Prince of Songkla University",
    "มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต": "Prince of Songkla University, Phuket Campus",
    "วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต": "College of Computing, Prince of Songkla University, Phuket Campus",
    "PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต": "PSU Esports Studio - Phuket, College of Computing, Prince of Songkla University, Phuket Campus",
    "วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง": "IoT System and Information Engineering, King Mongkut's Institute of Technology Ladkrabang",
}

def read(path):
    return [json.loads(l) for l in path.read_text(encoding="utf-8-sig").splitlines() if l.strip()]

def review_batch(batch):
    prompt = (
        "Audit each Thai source/English translation pair independently. JSON only: "
        '{"reviews":[{"id":0,"faithful":true,"issues":[]}]} . '
        "Never mark faithful if a condition, prohibition, exception, actor, number, time, "
        "institution, technical meaning or certainty is changed, omitted, or added. "
        "Check list entries too. Titles must retain material conditions present in source. "
        "Do not invent facts. No rewriting. Return exactly one review for every id.\n"
        + json.dumps(batch, ensure_ascii=False)
    )
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps({
        "model": "scb10x/typhoon2.5-qwen3-4b:latest", "prompt": prompt,
        "stream": False, "think": False, "format": "json", "keep_alive": "20m",
        "options": {"temperature": 0, "num_ctx": 8192, "num_predict": 900},
    }, ensure_ascii=False).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=55) as response:
        data = json.loads(response.read())
    payload = json.loads(data["response"])
    reviews = payload.get("reviews", [])
    if len(reviews) != len(batch) or {x.get("id") for x in reviews} != {x['id'] for x in batch}:
        raise ValueError("Incomplete or mismatched audit output")
    return {x['id']: x for x in reviews}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    evidence = out / "translation_audit.jsonl"
    if evidence.exists() and not args.resume:
        parser.error("Refusing to overwrite evidence")
    rows = read(ROOT / "data/locales/en/localization_review_drafts_competition_20260921_repaired.jsonl")
    fields = source_fields()
    prior = read(evidence) if evidence.exists() else []
    done = {(x['content_id'],x['field']) for x in prior}
    pending = []
    with evidence.open("a", encoding="utf-8") as stream:
        def emit(row):
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            prior.append(row)
        for row in rows:
            key = row['content_id'], row['field']
            if key in done:
                continue
            source = fields[key].get(row['field'])
            source_string = json.dumps(source, ensure_ascii=False) if isinstance(source,list) else str(source)
            text = MANUAL.get(source_string, str(row.get('text') or ''))
            base = {**row, "source_text": source, "text": text,
                    "source_hash_matches": source_text_sha256(source)==row['source_text_sha256'],
                    "human_reviewed": False, "owner_policy_approval": False}
            if row['field']=='name' and re.search(r"[\u0e00-\u0e7f]", source_string):
                emit({**base, "publishable": False, "review_kind": "official_identifier_preserved",
                      "issues": ["no_verified_romanization"]})
            elif source_string in MANUAL or source_string==text:
                emit({**base, "publishable": base['source_hash_matches'],
                      "review_kind": "assistant_source_review", "issues": []})
            else:
                pending.append((base, source_string))
        for offset in range(0,len(pending),6):
            group=pending[offset:offset+6]
            started=time.perf_counter()
            batch=[{"id":i,"source":s,"translation":r['text']} for i,(r,s) in enumerate(group)]
            try:
                reviews=review_batch(batch)
            except (OSError,ValueError,KeyError) as exc:
                reviews={i:{"faithful":False,"issues":[f"audit_error:{type(exc).__name__}"]} for i in range(len(group))}
            for i,(row,source) in enumerate(group):
                checks=mechanical_issues(source,row['text'])
                review=reviews[i]
                issues=checks+list(review.get('issues') or [])
                emit({**row, "publishable": bool(row['source_hash_matches'] and review.get('faithful') is True and not issues),
                      "review_kind":"assistant_with_local_model_semantic_audit", "issues":issues,
                      "model_review":review,"audit_batch_sec":round(time.perf_counter()-started,3)})
            print(f"audited {min(offset+6,len(pending))}/{len(pending)}, publishable={sum(x['publishable'] for x in prior)}",flush=True)
    candidate=out/'reviewed_candidate.jsonl'
    if candidate.exists():
        parser.error("Candidate exists; preserve it and choose a new output directory")
    now=datetime.now().astimezone().isoformat(timespec='seconds')
    with candidate.open('x',encoding='utf-8') as stream:
        for row in prior:
            if row['publishable']:
                approved={**row,'status':'approved','approved_by':'codex-assistant-user-authorized-20261001',
                          'approved_at':now,'version':int(row.get('version',1))+1}
                stream.write(json.dumps(approved,ensure_ascii=False)+'\n')
    summary={'total':len(prior),'publishable':sum(x['publishable'] for x in prior),
             'held':sum(not x['publishable'] for x in prior), 'human_reviewed':False,'candidate':str(candidate)}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
