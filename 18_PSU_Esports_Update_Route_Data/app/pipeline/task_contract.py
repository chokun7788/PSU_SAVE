"""Execution coverage for requested tasks; this is not a factual accuracy score."""

def task_status(mode, route, validation, trace=()):
    if not validation.ok or 'answer_contract_no_answer' in mode:
        return 'rejected'
    if any(word in mode for word in ('timeout', 'unavailable', 'backend_error')):
        return 'unavailable'
    if route.answer_type == 'clarification' or any(word in mode for word in ('clarification', 'missing_game_context')):
        return 'clarification'
    if route.answer_type == 'no_answer' or any(word in mode for word in ('no_answer', 'unconfirmed', 'unverified', 'source_gap')):
        return 'missing'
    for item in trace:
        if item.stage == 'competition_full_coverage' and (item.metadata.get('remaining_ids') or item.metadata.get('missing_ids')):
            return 'partial'
    return 'answered'

def outcome(statuses):
    if statuses and all(s == 'answered' for s in statuses):
        return 'answered_complete'
    if any(s in ('answered', 'partial') for s in statuses):
        return 'answered_partial'
    if statuses and all(s == 'clarification' for s in statuses):
        return 'needs_clarification'
    if 'rejected' in statuses:
        return 'schema_rejected'
    if 'unavailable' in statuses:
        return 'unavailable'
    return 'no_answer'

def single_contract(mode, route, validation, hits, trace):
    status = task_status(mode, route, validation, trace)
    return dict(schema_version=1, kind='single', status=status, outcome=outcome([status]),
                category=route.category, intent=route.intent, source_count=len(hits),
                coverage_meaning='execution_status_not_factual_accuracy')

def compound_contract(questions, results):
    tasks = []
    for index, (question, result) in enumerate(zip(questions, results), 1):
        tasks.append(dict(task_id=f'task-{index}', question=question,
            category=result.route.category, intent=result.route.intent, mode=result.mode,
            status=task_status(result.mode, result.route, result.validation, result.trace),
            validation_ok=result.validation.ok, source_count=len(result.hits)))
    statuses = [t['status'] for t in tasks]
    return dict(schema_version=1, kind='compound', tasks=tasks,
        expected_task_ids=[f'task-{i}' for i in range(1, len(questions)+1)],
        executed_task_ids=[t['task_id'] for t in tasks],
        answered_task_ids=[t['task_id'] for t in tasks if t['status'] == 'answered'],
        pending_task_ids=[f'task-{i}' for i in range(len(results)+1, len(questions)+1)],
        missing_task_ids=[t['task_id'] for t in tasks if t['status'] == 'missing'],
        outcome=outcome(statuses) if len(results)==len(questions) else 'answered_partial' if any(s in ('answered','partial') for s in statuses) else 'unavailable',
        coverage_meaning='execution_status_not_factual_accuracy')
