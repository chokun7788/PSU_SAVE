"""Local maintenance CLI. Backups use SQLite's consistent backup API."""
import argparse,json,sqlite3,getpass
from pathlib import Path
from .store import CommonStore
from .answer import database_path
from .registry import validate

def main():
    p=argparse.ArgumentParser();p.add_argument('--db',type=Path,default=database_path())
    commands=p.add_subparsers(dest='command',required=True)
    commands.add_parser('status');commands.add_parser('check')
    backup=commands.add_parser('backup');backup.add_argument('destination',type=Path)
    rollback=commands.add_parser('rollback');rollback.add_argument('release_id');rollback.add_argument('--expected-active',required=True)
    a=p.parse_args();store=CommonStore(a.db)
    if not store.path.is_file():raise SystemExit('Database does not exist; start the owner editor first.')
    if a.command=='backup':
        dest=a.destination.resolve()
        if dest.exists():raise SystemExit('Backup destination already exists; choose a new filename.')
        dest.parent.mkdir(parents=True,exist_ok=True)
        with sqlite3.connect(store.path.as_uri()+'?mode=ro',uri=True) as source,sqlite3.connect(dest) as target:source.backup(target)
        print(json.dumps({'backup':str(dest),'integrity':sqlite3.connect(dest).execute('PRAGMA integrity_check').fetchone()[0]}));return
    snap=store.snapshot()
    if a.command=='status':print(json.dumps({'active':snap['active'],'demo':snap['allow_demo'],'records':store.list_heads()},ensure_ascii=False,indent=2))
    elif a.command=='rollback':store.rollback(a.release_id,actor=getpass.getuser(),expected_active=a.expected_active);print('Rollback completed; revisions and audit history preserved.')
    else:
        with store.connect() as c:
            records=store.heads(c);sources=store.sources(c)
            report={k:validate(r,records,sources,publish=True,demo=snap['allow_demo']) for k,r in records.items()}
        print(json.dumps({'publication_errors':{k:v for k,v in report.items() if v},'checked':len(report),'active':snap['active']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
