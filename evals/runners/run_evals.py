#!/usr/bin/env python3
"""Run the studio's behavioural evaluation cases and grade what it did.

usage:
  python3 evals/runners/run_evals.py --list
  python3 evals/runners/run_evals.py --adapter manual --responses DIR [--only D16,D18] [--out DIR]
  python3 evals/runners/run_evals.py --adapter command --cmd "AGENT-CLI ..." [--trials 3]
                                     [--only ...] [--pack-path .] [--timeout 900] [--out DIR]

Each case in evals/cases/ is run for k trials (the case's `trials`, or --trials). Agents are
nondeterministic, so every assertion is reported as passed in k of k trials, and a case that passes
in some trials and not others is marked flaky rather than averaged into a number.

Outputs, in --out (default evals/reports/runs/<timestamp>/, which git ignores):
  results.json          every assertion in every trial, with the reason
  REPORT.md             the same, readable
  HUMAN_EVALUATION.md   the questions only a person can answer, one section per case, blank
  responses/            what the agent said, when the command adapter ran it

No score for musical quality is computed anywhere. The harness checks structure and behaviour; the
human evaluation sheet is where musical judgement goes, and it stays with the person who listened.
"""
import argparse, datetime, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
EVALS = os.path.normpath(os.path.join(HERE, '..'))
PACK = os.path.normpath(os.path.join(EVALS, '..'))

import cases as caselib  # noqa: E402
from graders import grade  # noqa: E402
from diversity import batch_diversity, rows_from, exploration_frequency  # noqa: E402
from adapters import manual, command  # noqa: E402


def load_vocab():
    return json.load(open(os.path.join(PACK, 'tools', 'vocab.json'), encoding='utf-8'))


def specialists():
    return {d for d in os.listdir(PACK)
            if os.path.exists(os.path.join(PACK, d, 'SKILL.md')) and d != 'music-director'}


def grade_batch(case, sets, ctx, fixtures):
    """One result per trial set: each reply graded alone, then the set graded as a batch."""
    b = case['batch']
    out = []
    for replies in sets:
        per_reply = [grade(t, caselib.all_assertions(case), ctx, fixtures) for t in replies]
        if b.get('kind') == 'exploration':
            stats = exploration_frequency(replies, threshold=b.get('threshold', 0.9))
            failed = b['fail_if'] == 'any_always_changed' and bool(stats['always_changed'])
        else:
            stats = batch_diversity(rows_from(replies), ctx['vocab']['track_dna_dimensions'],
                                    threshold=b.get('threshold', 0.9), watch=b.get('watch'),
                                    brief_implied=b.get('brief_implied'))
            watched = stats['collapsed_watched_dimensions']
            if b['fail_if'] == 'all_watched_collapsed':
                failed = bool(b.get('watch')) and len(watched) == len(b['watch'])
            else:
                failed = bool(watched)
        enough = len(replies) == len(b['briefs'])
        results = [{'id': 'batch_complete', 'passed': enough,
                    'detail': f'{len(replies)} replies for {len(b["briefs"])} briefs'},
                   {'id': 'batch_diversity', 'passed': not failed,
                    'detail': json.dumps(stats, sort_keys=True)}]
        for i, pr in enumerate(per_reply, 1):
            for a in pr:
                results.append({'id': f'brief{i:02d}.{a["id"]}', 'passed': a['passed'],
                                'detail': a['detail']})
        out.append(results)
    return out


def summarise(case, trials):
    ids = []
    for t in trials:
        for a in t:
            if a['id'] not in ids:
                ids.append(a['id'])
    rows = []
    for aid in ids:
        passes = sum(1 for t in trials for a in t if a['id'] == aid and a['passed'])
        rows.append({'id': aid, 'passed_in': passes, 'trials': len(trials)})
    all_pass = [all(a['passed'] for a in t) for t in trials]
    status = 'no responses' if not trials else (
        'pass' if all(all_pass) else 'fail' if not any(all_pass) else 'flaky')
    return {'status': status, 'trials_passing': sum(all_pass), 'trials': len(trials),
            'assertions': rows}


def write_reports(out, results, cases_by_id, meta):
    os.makedirs(out, exist_ok=True)
    json.dump({'meta': meta, 'results': results}, open(os.path.join(out, 'results.json'), 'w'),
              indent=2)
    lines = [f'# Evaluation run {meta["started"]}', '',
             f'Adapter: `{meta["adapter"]}`. Cases: {len(results)}. Pack version: {meta["version"]}.',
             '', '**This report checks structure and behaviour. It does not score music.** '
             'Musical judgement goes in `HUMAN_EVALUATION.md`.', '',
             '| case | title | status | trials passing |', '|---|---|---|---|']
    for cid, r in results.items():
        s = r['summary']
        lines.append(f'| {cid} | {cases_by_id[cid]["title"]} | {s["status"]} | '
                     f'{s["trials_passing"]} of {s["trials"]} |')
    for cid, r in results.items():
        lines += ['', f'## {cid}: {cases_by_id[cid]["title"]}', '']
        for a in r['summary']['assertions']:
            lines.append(f'- `{a["id"]}` passed in {a["passed_in"]} of {a["trials"]}')
        for i, t in enumerate(r['trials'], 1):
            bad = [a for a in t if not a['passed']]
            if bad:
                lines.append(f'- trial {i} failures:')
                lines += [f'  - `{a["id"]}`: {a["detail"][:300]}' for a in bad]
    open(os.path.join(out, 'REPORT.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

    tpl = os.path.join(EVALS, 'reports', 'HUMAN_EVALUATION_TEMPLATE.md')
    head = open(tpl, encoding='utf-8').read().split('<!-- cases -->')[0] if os.path.exists(tpl) else ''
    h = [head.rstrip(), '', f'Run: {meta["started"]}, adapter `{meta["adapter"]}`.', '']
    for cid in results:
        c = cases_by_id[cid]
        h += [f'## {cid}: {c["title"]}', '', f'Brief: {c["brief"].strip()}', '',
              'Responses: `responses/' + cid + '/`' if meta['adapter'] == 'command' else
              'Responses: see the folder given to --responses.', '']
        for q in c['human_questions']:
            h += [f'- {q}', '  - answer:', '']
        h += ['- Anything the checks missed?', '  - answer:', '']
    open(os.path.join(out, 'HUMAN_EVALUATION.md'), 'w', encoding='utf-8').write('\n'.join(h) + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--adapter', choices=['manual', 'command'])
    ap.add_argument('--responses', help='manual adapter: folder of responses')
    ap.add_argument('--cmd', help='command adapter: the agent command line')
    ap.add_argument('--only', help='comma-separated case ids')
    ap.add_argument('--trials', type=int, default=0)
    ap.add_argument('--timeout', type=int, default=900)
    ap.add_argument('--pack-path', default=PACK)
    ap.add_argument('--out')
    a = ap.parse_args()

    only = set(a.only.split(',')) if a.only else None
    all_cases = caselib.load_all(only=only)
    if a.list:
        for c in all_cases:
            print(f'{c["id"]:6} {c["category"]:26} {c["title"]}')
        return
    if not a.adapter:
        ap.error('--adapter is required unless --list is given')

    vocab = load_vocab()
    fixtures = os.path.join(EVALS, 'fixtures')
    problems = [p for c in all_cases for p in caselib.validate(c, fixtures, vocab, specialists())]
    if problems:
        print('\n'.join(problems))
        sys.exit(2)

    started = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
    out = a.out or os.path.join(EVALS, 'reports', 'runs', started.replace(' ', '_'))
    ctx = {'vocab': vocab}
    manifest = json.load(open(os.path.join(PACK, 'manifest.json'), encoding='utf-8'))
    results = {}
    for c in all_cases:
        if a.adapter == 'manual':
            if not a.responses:
                ap.error('--responses is required with the manual adapter')
            got = manual.responses_for(c, a.responses)
        else:
            if not a.cmd:
                ap.error('--cmd is required with the command adapter')
            got = command.responses_for(c, {'cmd': a.cmd, 'trials': a.trials, 'timeout': a.timeout,
                                            'fixtures_dir': fixtures, 'pack_path': a.pack_path},
                                        os.path.join(out, 'responses'))
        if c.get('batch'):
            trials = grade_batch(c, got, ctx, fixtures)
        else:
            trials = [grade(t, caselib.all_assertions(c), ctx, fixtures) for t in got]
        results[c['id']] = {'trials': trials, 'summary': summarise(c, trials)}
        s = results[c['id']]['summary']
        print(f'{c["id"]:6} {s["status"]:12} {s["trials_passing"]} of {s["trials"]} trials  {c["title"]}')

    meta = {'started': started, 'adapter': a.adapter, 'version': manifest.get('version'),
            'cmd': a.cmd if a.adapter == 'command' else None}
    write_reports(out, results, {c['id']: c for c in all_cases}, meta)
    print(f'\nreports written to {out}')
    failed = [cid for cid, r in results.items() if r['summary']['status'] in ('fail', 'flaky')]
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
