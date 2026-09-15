#!/usr/bin/env python3
"""Release check: the behavioural evaluation harness catches what it claims to catch.

usage: python3 tools/eval_selftest.py [--root .]

No model is called. For every case in evals/cases/ this check:
  - validates the case against evals/schemas/CASE_SCHEMA.md (required fields, a known category, a
    human question, known assertion types, fixtures and routes that exist);
  - requires a hand-written passing response and a hand-written failing response in
    evals/expected/<ID>/pass/ and fail/;
  - grades them with the same graders a real run uses, and fails (exit 1) if a passing response
    fails any assertion, or a failing response does not fail every assertion its
    "<!-- must_fail: ... -->" line names.

So a grader that stops detecting random humanisation, a rewritten lyric, a collapsed batch or a
missing trace is caught in CI, before anyone relies on it against a real agent. PyYAML is required,
as it is for the harness itself. Nothing is changed.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
MUST_FAIL = re.compile(r'<!--\s*must_fail:\s*(.*?)\s*-->')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    runners = os.path.join(root, 'evals', 'runners')
    try:
        import yaml  # noqa: F401
    except ImportError:
        print('PyYAML is not installed; the evaluation self-test needs it (pip install pyyaml)')
        sys.exit(1)
    sys.path.insert(0, runners)
    import cases as caselib
    import run_evals
    from graders import grade

    vocab = run_evals.load_vocab()
    fixtures = os.path.join(root, 'evals', 'fixtures')
    specialists = {d for d in os.listdir(root)
                   if os.path.exists(os.path.join(root, d, 'SKILL.md')) and d != 'music-director'}
    expected = os.path.join(root, 'evals', 'expected')
    problems, n = [], 0
    ctx = {'vocab': vocab}

    all_cases = caselib.load_all(os.path.join(root, 'evals', 'cases'))
    ids = [c.get('id') for c in all_cases]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f'case id {dup} is used twice')

    for c in all_cases:
        n += 1
        problems += caselib.validate(c, fixtures, vocab, specialists)
        for kind in ('pass', 'fail'):
            folder = os.path.join(expected, c['id'], kind)
            if not os.path.isdir(folder):
                problems.append(f'evals/expected/{c["id"]}/{kind}/: missing; every case needs a '
                                f'passing and a failing response')
                continue
            if c.get('batch'):
                sets = [os.path.join(folder, d) for d in sorted(os.listdir(folder))
                        if os.path.isdir(os.path.join(folder, d))]
                replies = [[open(os.path.join(s, f), encoding='utf-8').read()
                            for f in sorted(os.listdir(s)) if f.endswith('.md')] for s in sets]
                results = run_evals.grade_batch(c, replies, ctx, fixtures)
                texts = [r[0] if r else '' for r in replies]
            else:
                files = sorted(f for f in os.listdir(folder) if f.endswith('.md'))
                texts = [open(os.path.join(folder, f), encoding='utf-8').read() for f in files]
                results = [grade(t, caselib.all_assertions(c), ctx, fixtures) for t in texts]
            if not results:
                problems.append(f'evals/expected/{c["id"]}/{kind}/: no responses')
            for text, res in zip(texts, results):
                failed = {r['id'] for r in res if not r['passed']}
                if kind == 'pass' and failed:
                    detail = '; '.join(f'{r["id"]}: {r["detail"][:160]}' for r in res if not r['passed'])
                    problems.append(f'{c["id"]}: the expected passing response fails: {detail}')
                if kind == 'fail':
                    m = MUST_FAIL.search(text)
                    named = {x.strip() for x in m.group(1).split(',')} if m else set()
                    if not named:
                        problems.append(f'{c["id"]}: the expected failing response names no '
                                        f'must_fail assertion')
                    unknown = named - {r['id'] for r in res}
                    if unknown:
                        problems.append(f'{c["id"]}: must_fail names unknown assertion(s) {sorted(unknown)}')
                    missed = (named & {r['id'] for r in res}) - failed
                    if missed:
                        problems.append(f'{c["id"]}: the expected failing response passes '
                                        f'{sorted(missed)}, which it must fail')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s) across {n} case(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
