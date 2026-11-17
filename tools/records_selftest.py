#!/usr/bin/env python3
"""Self-test for tools/validate_records.py: the shipped examples pass, and each broken variant of the
sketch_round example fails for the reason it should (shared/SKETCH_ROUND_PROTOCOL.md). Stdlib only."""
import copy, json, pathlib, sys
BASE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / 'tools'))
from validate_records import validate  # noqa: E402

CASES = [  # (name, mutation, text the error must contain; None = must pass)
    ('valid example', lambda r: None, None),
    ('two KEEPs', lambda r: r['candidates'][1].update(decision='KEEP'), 'more than one KEEP'),
    ('one dimension', lambda r: r['candidates'][0].update(differs_on=['groove']), 'at least two dimensions'),
    ('unknown dimension', lambda r: r['candidates'][0].update(differs_on=['groove', 'vibes']), 'unknown dimension'),
    ('user without listening', lambda r: r['candidates'][0].update(basis='measured'), 'must rest on listening'),
    ('measured KEEP', lambda r: r['candidates'][0].update(basis='measured', decided_by='pending'), 'only be provisional'),
    ('REVISE without plan', lambda r: r['candidates'][1].update(decision='REVISE'), 'revision_plan'),
    ('RECOMBINE without sources', lambda r: r['candidates'][2].update(decision='RECOMBINE'), 'recombine_sources'),
    ('judged without render', lambda r: r['candidates'][0].pop('render'), 'without a render'),
    ('decision without reason', lambda r: r['candidates'][1].pop('reason'), 'needs a reason'),
    ('outcome mismatch', lambda r: r.update(outcome='B'), 'outcome must name the KEEP'),
    ('one candidate', lambda r: r.update(candidates=r['candidates'][:1]), 'at least two'),
    ('open round', lambda r: ([c.update(decision='PENDING', basis='pending', decided_by='pending') for c in r['candidates']], r.update(outcome='open')), None),
    ('provisional KEEP from measurement', lambda r: r['candidates'][0].update(basis='measured', decided_by='director_provisional'), None),
]


def main():
    bad = 0
    for kind in ('analysis_finding', 'decision_event', 'sketch_round'):
        errs = validate(kind, json.loads((BASE / 'examples' / f'{kind}.example.json').read_text()))
        if errs:
            print(f'FAIL example {kind}: {errs}'); bad += 1
    base = json.loads((BASE / 'examples' / 'sketch_round.example.json').read_text())
    for name, mut, want in CASES:
        r = copy.deepcopy(base); mut(r); errs = validate('sketch_round', r)
        ok = (not errs) if want is None else any(want in e for e in errs)
        if not ok:
            print(f'FAIL {name}: got {errs}'); bad += 1
    print(f'{bad} finding(s) across {len(CASES) + 3} record case(s)')
    return int(bool(bad))


if __name__ == '__main__':
    sys.exit(main())
