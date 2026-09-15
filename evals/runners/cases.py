"""Load and validate evaluation cases (evals/schemas/CASE_SCHEMA.md).

Shared by run_evals.py and tools/eval_selftest.py, so a case that the self-test accepts is exactly a
case the runner can run.
"""
import os

import yaml

from graders import ASSERTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
EVALS = os.path.normpath(os.path.join(HERE, '..'))
REQUIRED = ['id', 'title', 'category', 'brief', 'required_behaviors', 'forbidden_behaviors',
            'structural_assertions', 'human_questions']
CATEGORIES = {'diversity', 'project_work', 'performance', 'routing', 'cultural_systems', 'tuning',
              'interaction_modes', 'rhythm_and_form', 'experimental_and_adaptive', 'compatibility'}
BATCH_FAIL_RULES = {'any_watched_collapsed', 'all_watched_collapsed', 'any_always_changed'}


def load_all(cases_dir=None, only=None):
    cases_dir = cases_dir or os.path.join(EVALS, 'cases')
    out = []
    for dp, dn, fn in os.walk(cases_dir):
        for f in sorted(fn):
            if not f.endswith(('.yaml', '.yml')):
                continue
            path = os.path.join(dp, f)
            doc = yaml.safe_load(open(path, encoding='utf-8'))
            case = (doc or {}).get('test', {})
            case['_path'] = os.path.relpath(path, EVALS)
            if only and case.get('id') not in only:
                continue
            out.append(case)
    return sorted(out, key=lambda c: (c.get('category', ''), str(c.get('id'))))


def all_assertions(case):
    """The case's structural assertions, plus the ones its expected_routes imply."""
    out = list(case.get('structural_assertions') or [])
    routes = case.get('expected_routes') or {}
    if routes.get('must_include'):
        out.append({'id': 'routes_include', 'routes_include': routes['must_include']})
    if routes.get('must_not_include'):
        out.append({'id': 'routes_exclude', 'routes_exclude': routes['must_not_include']})
    return out


def validate(case, fixtures_dir, vocab, specialists):
    problems = []
    where = case.get('_path', '?')
    for k in REQUIRED:
        if k not in case or case[k] in (None, ''):
            problems.append(f'{where}: missing {k}')
    if case.get('category') not in CATEGORIES:
        problems.append(f'{where}: category {case.get("category")!r} is not one of {sorted(CATEGORIES)}')
    expected_dir = os.path.basename(os.path.dirname(os.path.join(EVALS, where)))
    if case.get('category') and expected_dir != case['category']:
        problems.append(f'{where}: filed under {expected_dir}/ but its category is {case["category"]}')
    if not case.get('human_questions'):
        problems.append(f'{where}: at least one human question is required; the harness does not '
                        f'judge music')
    for rel in case.get('supplied_context') or []:
        if not os.path.exists(os.path.join(fixtures_dir, rel)):
            problems.append(f'{where}: supplied_context {rel} does not exist in evals/fixtures/')
    routes = case.get('expected_routes') or {}
    for r in (routes.get('must_include') or []) + (routes.get('must_not_include') or []):
        if r not in specialists:
            problems.append(f'{where}: expected route {r!r} is not a specialist folder')
    ids = []
    for a in all_assertions(case):
        kinds = [k for k in a if k in ASSERTIONS]
        if len(kinds) != 1:
            problems.append(f'{where}: assertion {a.get("id", a)!r} needs exactly one known type')
        if 'id' not in a:
            problems.append(f'{where}: every assertion needs an id')
        ids.append(a.get('id'))
        if 'field_in_vocab' in a:
            name = a['field_in_vocab'].get('vocab')
            if name not in vocab.get('vocabularies', {}) and name not in vocab:
                problems.append(f'{where}: vocabulary {name!r} is not in tools/vocab.json')
        if 'fixture_not_rewritten' in a:
            fx = a['fixture_not_rewritten'].get('fixture', '')
            if not os.path.exists(os.path.join(fixtures_dir, fx)):
                problems.append(f'{where}: fixture {fx} does not exist')
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        problems.append(f'{where}: repeated assertion id(s) {sorted(dup)}')
    b = case.get('batch')
    if b:
        if not b.get('briefs') or len(b['briefs']) < 2:
            problems.append(f'{where}: a batch needs at least two briefs')
        if b.get('fail_if') not in BATCH_FAIL_RULES:
            problems.append(f'{where}: batch.fail_if must be one of {sorted(BATCH_FAIL_RULES)}')
    return problems
