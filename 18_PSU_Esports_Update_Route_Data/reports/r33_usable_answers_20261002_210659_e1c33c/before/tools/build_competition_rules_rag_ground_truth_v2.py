#!/usr/bin/env python3
"""Build a paraphrase-heavy, source-preserving competition RAG Gold corpus.

The v2 cases deliberately keep the evidence contract from v1.  Only the
surface wording changes, so a failing v2 case identifies a language or
retrieval weakness instead of a disagreement about the ground truth.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "eval" / "competition_rules_rag_ground_truth_v1.jsonl"
OUTPUT = ROOT / "data" / "eval" / "competition_rules_rag_ground_truth_v2_expanded.jsonl"
MANIFEST = ROOT / "data" / "eval" / "competition_rules_rag_ground_truth_v2_expanded_manifest.json"


GAME_LABELS = {
    "th": {"cs2": "CS2", "rov": "RoV", "tekken8": "Tekken 8", "valorant": "VALORANT"},
    "en": {"cs2": "Counter-Strike 2", "rov": "Arena of Valor", "tekken8": "Tekken 8", "valorant": "VALORANT"},
}

# These are intent-preserving paraphrases, not aliases.  They exercise how a
# participant naturally describes a scenario while their expected source IDs
# still originate in the reviewed v1 Gold record for the same game and facet.
FACET_PROMPTS = {
    "th": {
        "competition_format": ("{game} แข่งใช้รูปแบบไหนบ้าง", "ถ้าลง {game} ต้องแข่งกี่เกมต่อแมตช์", "ระบบแข่งของ {game} เป็นแพ้คัดออกหรือมีรอบอื่นด้วย"),
        "conduct": ("ผู้เล่น {game} มีข้อควรระวังเรื่องการวางตัวอะไร", "ระหว่างแข่ง {game} พูดหรือทำแบบไหนถึงผิดมารยาท", "กฎความประพฤติของผู้แข่ง {game} ระบุไว้อย่างไร"),
        "fair_play_conduct": ("การแข่งขัน {game} มีหลัก fair play อะไรที่ต้องทำตาม", "{game} ห้ามมีพฤติกรรมที่ไม่เป็นนักกีฬาแบบไหน", "อยากเช็กเรื่องน้ำใจนักกีฬาของ {game} ต้องดูข้อไหน"),
        "dispute": ("ถ้าโต้แย้งผลแข่ง {game} ต้องทำอย่างไร", "เกิดข้อพิพาทใน {game} ใครเป็นคนตัดสิน", "กติกา {game} รับมือความเห็นไม่ตรงกันหลังแข่งอย่างไร"),
        "protest_dispute": ("อยากยื่นประท้วงในรายการ {game} ต้องทำตอนไหน", "ถ้าจะคัดค้านผล {game} มีขั้นตอนอะไร", "การประท้วงผลแข่ง {game} ส่งให้ใครและมีเงื่อนไขไหม"),
        "eligibility_registration": ("ใครบ้างที่มีสิทธิ์สมัครแข่ง {game}", "คนที่จะลง {game} ต้องมีคุณสมบัติอะไร", "{game} รับผู้เข้าแข่งขันแบบไหน"),
        "registration": ("สมัครเข้าร่วม {game} ต้องเตรียมอะไร", "ถ้าจะลงทะเบียน {game} ทำได้ถึงเมื่อไร", "ขั้นตอนส่งชื่อเข้ารายการ {game} เป็นอย่างไร"),
        "team_size": ("ทีม {game} ต้องส่งผู้เล่นกี่คน", "{game} ให้ลงรายชื่อทีมได้กี่คนรวมสำรอง", "จำนวนตัวจริงและตัวสำรองของ {game} กำหนดไว้อย่างไร"),
        "equipment": ("แข่ง {game} ใช้อุปกรณ์ของตัวเองได้ไหม", "{game} อนุญาตอุปกรณ์หรือการตั้งค่าแบบไหน", "เรื่องเครื่องแข่งและอุปกรณ์ของ {game} มีกฎอะไร"),
        "pause_timeout": ("ระหว่างแข่ง {game} ขอหยุดเกมได้ในกรณีไหน", "{game} มี timeout หรือ technical pause อย่างไร", "ถ้าเกม {game} มีปัญหากลางคัน ต้อง pause ตามกฎแบบไหน"),
        "disconnect": ("ถ้าผู้เล่นหลุดระหว่าง {game} ต้องทำอย่างไร", "เน็ตหลุดตอนแข่ง {game} ยังเล่นต่อหรือแข่งใหม่ได้ไหม", "กติกา {game} ว่าด้วยการเชื่อมต่อขาดหายเป็นอย่างไร"),
        "map_pool": ("รายการ {game} ใช้แผนที่อะไรบ้าง", "ก่อนแข่ง {game} เลือกหรือแบนแผนที่อย่างไร", "map pool ของ {game} ในรายการนี้มีอะไร"),
        "match_configuration": ("ตั้งค่าแมตช์ {game} ตามกติกาแบบไหน", "ห้องแข่ง {game} ต้องใช้การกำหนดค่าอะไร", "รายละเอียดการตั้งค่าเกมสำหรับ {game} คืออะไร"),
        "match_settings": ("{game} มี setting ที่ผู้เล่นต้องใช้เหมือนกันไหม", "อยากเช็กค่าตั้งต้นของแมตช์ {game}", "ก่อนแข่ง {game} ต้องตั้งค่าเกมอะไรบ้าง"),
        "penalty": ("ถ้าฝ่าฝืนกติกา {game} จะมีผลอย่างไร", "การทำผิดใน {game} มีโทษระดับไหน", "กรณีผิดกฎ {game} ผู้จัดจัดการอย่างไร"),
        "penalty_matrix": ("ขอตารางบทลงโทษของ {game}", "ความผิดแต่ละแบบใน {game} โดนโทษต่างกันอย่างไร", "มีรายการบทลงโทษการแข่งขัน {game} ให้ดูไหม"),
        "pre_match_on_site": ("วันแข่ง {game} ต้องไปรายงานตัวอย่างไร", "ก่อนเริ่ม {game} ผู้เล่นต้องทำอะไรที่หน้างาน", "{game} กำหนดเวลา check-in หรือพื้นที่แข่งไว้ไหม"),
        "in_match_operations": ("ระหว่างแมตช์ {game} ต้องประสานกับกรรมการอย่างไร", "ขั้นตอนทำงานระหว่างการแข่งขัน {game} เป็นแบบไหน", "ถ้าเกิดเรื่องระหว่างแข่ง {game} ต้องแจ้งใคร"),
        "schedule": ("ตารางหรือกำหนดการของ {game} ดูได้จากไหน", "{game} แข่งวันไหนและมีประกาศเวลาอย่างไร", "ช่วยดูเรื่องกำหนดการแข่งขัน {game} ให้หน่อย"),
        "rulebook_identity": ("เอกสารกติกา {game} ฉบับนี้ครอบคลุมเรื่องอะไร", "ขอภาพรวมข้อกำหนดของรายการ {game}", "กติกา {game} ใช้กับการแข่งขันไหน"),
    },
    "en": {
        "competition_format": ("What competition format does {game} use?", "How many games are played in a {game} match?", "Is the {game} event single elimination or does it use another format?"),
        "conduct": ("What conduct is expected from {game} players?", "What behaviour is not allowed during a {game} match?", "What do the {game} rules say about player sportsmanship?"),
        "fair_play_conduct": ("What fair-play rules apply to {game}?", "Which unsporting behaviours are prohibited in {game}?", "Where can I check the sportsmanship rules for {game}?"),
        "dispute": ("What happens if there is a dispute about a {game} result?", "Who decides a disagreement in a {game} match?", "How do the {game} rules resolve a conflict after a match?"),
        "protest_dispute": ("How can a team protest a {game} result?", "When may we raise an objection in the {game} event?", "What is the process for challenging a {game} decision?"),
        "eligibility_registration": ("Who is eligible to enter the {game} tournament?", "What eligibility requirements apply to {game} participants?", "Which players may register for {game}?"),
        "registration": ("How do I register for {game}?", "What is needed to submit a {game} entry?", "Until when can a team register for {game}?"),
        "team_size": ("How many players must a {game} team have?", "How many starters and substitutes can a {game} roster include?", "What is the permitted roster size for {game}?"),
        "equipment": ("May players use their own equipment in {game}?", "Which devices or settings are allowed for {game}?", "What equipment rules apply to the {game} event?"),
        "pause_timeout": ("When may a {game} match be paused?", "How do timeout and technical pause rules work in {game}?", "What should we do if a {game} match needs to stop mid-game?"),
        "disconnect": ("What happens if someone disconnects in {game}?", "Can a {game} match restart after a connection loss?", "How do {game} rules handle an internet disconnection?"),
        "map_pool": ("Which maps are used in the {game} event?", "How are maps picked or banned for {game}?", "What is the {game} map pool for this tournament?"),
        "match_configuration": ("How should a {game} match be configured?", "Which match configuration is required for {game}?", "What room setup does the {game} event require?"),
        "match_settings": ("Are there required in-game settings for {game}?", "What default match settings should {game} players use?", "Which settings must be configured before a {game} match?"),
        "penalty": ("What happens when a {game} rule is broken?", "What penalties can apply to a {game} violation?", "How do organisers handle misconduct in {game}?"),
        "penalty_matrix": ("Is there a penalty table for {game}?", "How do penalties differ by violation in {game}?", "Where are the {game} tournament penalties listed?"),
        "pre_match_on_site": ("How do players check in for {game}?", "What must players do on site before a {game} match?", "Does the {game} event have a check-in time or venue requirement?"),
        "in_match_operations": ("How should players contact officials during a {game} match?", "What is the in-match procedure for {game}?", "Who should we notify if an issue occurs during {game}?"),
        "schedule": ("Where can I find the {game} event schedule?", "When is {game} played and how is the time announced?", "Please check the competition schedule for {game}."),
        "rulebook_identity": ("What does this {game} rulebook cover?", "Can you give an overview of the {game} event rules?", "Which tournament does this {game} rulebook apply to?"),
    },
}


def load_rows(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def special_question(row: dict[str, Any], number: int) -> str:
    """Keep intentional clarification/no-answer and multi-target cases valid."""
    locale = str(row["locale"])
    game_id = str(row.get("expected_game_id") or "")
    if game_id == "multi":
        options = (
            ("ช่วยเทียบกติกา pause ของ CS2 กับ VALORANT ให้หน่อย", "Could you compare the pause rules for CS2 and VALORANT?"),
            ("CS2 กับ VALORANT ถ้าเกมมีปัญหากลางคัน ใช้กฎหยุดเกมต่างกันไหม", "Do CS2 and VALORANT handle an in-match pause differently?"),
            ("อยากดูความต่างเรื่อง timeout ระหว่าง CS2 และ VALORANT", "I want to compare timeout rules between CS2 and VALORANT."),
        )
        return options[number % len(options)][0 if locale == "th" else 1]
    if game_id in {"dota2", "freefire"}:
        game = "Dota 2" if game_id == "dota2" else "Free Fire"
        options = (
            (f"มีเอกสารกติกาการแข่งขัน {game} ของศูนย์ไหม", f"Do you have an official {game} tournament rulebook?"),
            (f"ช่วยหากฎแข่ง {game} ในฐานข้อมูลนี้ให้หน่อย", f"Please check whether this knowledge base has {game} competition rules."),
            (f"{game} ใช้กติกาการแข่งฉบับไหน", f"Which competition rules apply to {game} here?"),
        )
        return options[number % len(options)][0 if locale == "th" else 1]
    # A bare rule question must still produce a clarification rather than
    # silently choosing a game from the catalogue.
    options = (
        ("ถ้าอยากรู้กติกา pause ต้องระบุเกมก่อนใช่ไหม", "Do I need to specify the game before asking about pause rules?"),
        ("ช่วยบอกกฎ timeout ให้หน่อย", "Please tell me the timeout rules."),
        ("กติกาเรื่องการประท้วงดูได้ไหม", "Can you show me the protest rules?"),
    )
    return options[number % len(options)][0 if locale == "th" else 1]


def build_cases(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["locale"]), str(row.get("expected_game_id") or "safe"), str(row.get("expected_facet") or "safe"))].append(row)

    output: list[dict[str, Any]] = []
    for (locale, game_id, facet), members in sorted(groups.items()):
        representative = members[0]
        prompts = FACET_PROMPTS.get(locale, {}).get(facet)
        if game_id not in GAME_LABELS.get(locale, {}) or not prompts:
            prompts = tuple(special_question(representative, index) for index in range(3))
        for index, prompt in enumerate(prompts, start=1):
            question = prompt.format(game=GAME_LABELS[locale][game_id]) if "{game}" in prompt else prompt
            case = dict(representative)
            case.update({
                "id": f"COMP-RAG-V2-{locale.upper()}-{len(output) + 1:03d}",
                "question": question,
                "question_style": "participant_natural_paraphrase",
                "suite": "competition_rules_rag_ground_truth_v2_expanded",
                "parent_gold_id": representative["id"],
                "review_status": "source_preserving_paraphrase_candidate",
                "generation": {"strategy": "facet_prompt_v2", "variant": index},
            })
            output.append(case)
    return output


def validate(cases: list[dict[str, Any]]) -> None:
    ids = [str(case["id"]) for case in cases]
    questions = [(str(case["locale"]), " ".join(str(case["question"]).casefold().split())) for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case ID")
    if len(questions) != len(set(questions)):
        raise ValueError("duplicate normalized question within a locale")
    for case in cases:
        if case["expected_answer_status"] == "answer_available" and case.get("rag_required"):
            if not case.get("expected_rulebook_ids"):
                raise ValueError(f"{case['id']} is answerable RAG without a rulebook target")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source_rows = load_rows(SOURCE)
    cases = build_cases(source_rows)
    validate(cases)
    OUTPUT.write_text("\n".join(json.dumps(case, ensure_ascii=False, sort_keys=True) for case in cases) + "\n", encoding="utf-8")
    locale_counts = {locale: sum(case["locale"] == locale for case in cases) for locale in ("th", "en")}
    MANIFEST.write_text(json.dumps({
        "suite": "competition_rules_rag_ground_truth_v2_expanded",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total": len(cases),
        "locale_counts": locale_counts,
        "source": str(SOURCE),
        "source_sha256": digest(SOURCE),
        "sha256": digest(OUTPUT),
        "generation_policy": "Each v2 case inherits evidence contract from one reviewed v1 Gold row; only wording changes.",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(cases)} cases to {OUTPUT}")
    print(f"Manifest: {MANIFEST}")


if __name__ == "__main__":
    main()
