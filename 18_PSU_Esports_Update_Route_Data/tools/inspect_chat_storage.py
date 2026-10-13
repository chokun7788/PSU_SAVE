"""Read-only storage diagnosis. Never deletes or changes chat history."""
import argparse,json,sqlite3,time
from pathlib import Path
def inspect(folder):
    folder=Path(folder).resolve();result={'path':str(folder),'mode':'read_only_no_retention_policy_assumed','files':[],'databases':[]}
    for p in sorted(folder.glob('*')):
        if p.is_file():result['files'].append({'name':p.name,'bytes':p.stat().st_size})
        if p.is_file() and p.suffix in ('.sqlite3','.sqlite','.db'):
            db=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True)
            try:
                tables={r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
                item={'name':p.name,'tables':{}}
                for name in ('chat_jobs','chat_turns','chat_history','conversation_sessions'):
                    if name in tables:item['tables'][name]={'count':db.execute(f'SELECT COUNT(*) FROM "{name}"').fetchone()[0]}
                if 'chat_jobs' in tables:
                    item['job_status_counts']=dict(db.execute('SELECT status,COUNT(*) FROM chat_jobs GROUP BY status'))
                    item['oldest_job_created_at']=db.execute('SELECT MIN(created) FROM chat_jobs').fetchone()[0]
                result['databases'].append(item)
            finally:db.close()
    result['total_top_level_bytes']=sum(r['bytes'] for r in result['files']);return result
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('folder');a=p.parse_args();print(json.dumps(inspect(a.folder),ensure_ascii=False,indent=2))
