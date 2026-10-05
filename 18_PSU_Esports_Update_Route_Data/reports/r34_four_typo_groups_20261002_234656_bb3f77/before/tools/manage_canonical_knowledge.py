from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.local_models import embed_documents, warm_knowledge_models
from app.knowledge.store import KnowledgeStore


def main() -> int:
    parser = argparse.ArgumentParser(description="Trusted local operator workflow. No public admin endpoint.")
    parser.add_argument("--db", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    init = sub.add_parser("init")
    init.add_argument("--demo", action="store_true")
    sub.add_parser("status")
    sub.add_parser("warmup")
    save = sub.add_parser("save")
    save.add_argument("file", type=Path)
    save.add_argument("--expected-version", type=int, required=True)
    save.add_argument("--actor", required=True)
    approve = sub.add_parser("approve")
    approve.add_argument("record_id")
    approve.add_argument("--version", type=int, required=True)
    approve.add_argument("--hash", required=True)
    approve.add_argument("--actor", required=True)
    publish = sub.add_parser("publish")
    publish.add_argument("--request-key", required=True)
    publish.add_argument("--expected-active", required=True)
    publish.add_argument("--actor", required=True)
    withdraw = sub.add_parser("withdraw")
    withdraw.add_argument("record_id")
    withdraw.add_argument("--actor", required=True)
    rollback = sub.add_parser("rollback")
    rollback.add_argument("release_id")
    rollback.add_argument("--expected-active", required=True)
    rollback.add_argument("--actor", required=True)
    args = parser.parse_args()
    store = KnowledgeStore(args.db)
    if args.action == "warmup":
        result = warm_knowledge_models()
    elif args.action == "init":
        store.initialize(allow_demo=args.demo)
        result = {"initialized": True, "db": str(store.path)}
    elif args.action == "save":
        record = json.loads(args.file.read_text(encoding="utf-8-sig"))
        result = store.save(record, actor=args.actor, expected_version=args.expected_version)
    elif args.action == "approve":
        store.approve(args.record_id, args.version, args.hash, actor=args.actor)
        result = {"approved": True}
    elif args.action == "publish":
        result = {"release_id": store.publish(actor=args.actor, request_key=args.request_key,
                                             expected_active=args.expected_active, embed=embed_documents)}
    elif args.action == "withdraw":
        store.withdraw(args.record_id, actor=args.actor)
        result = {"withdrawn": True}
    elif args.action == "rollback":
        store.rollback(args.release_id, actor=args.actor, expected_active=args.expected_active)
        result = {"active": args.release_id}
    else:
        snapshot = store.snapshot()
        result = {"active": snapshot["active"], "epoch": snapshot["epoch"], "demo": snapshot["allow_demo"],
                  "record_count": len(snapshot["release"]["records"]) if snapshot["release"] else 0}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
