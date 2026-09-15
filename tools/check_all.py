#!/usr/bin/env python3
"""Run every release check.

usage: python3 tools/check_all.py [--profile path/to/profile.yaml] [--root .]

Runs, in order: manifest, links, skill lint, schemas, examples, compatibility,
evidence, evaluation self-test, routing, privacy. Reports each result and
exits non-zero if any of them found something. Nothing is changed.
"""
import argparse, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = [
    ('manifest', 'manifest_check.py', []),
    ('links', 'link_check.py', []),
    ('skills', 'skill_lint.py', []),
    ('schemas', 'schema_check.py', []),
    ('examples', 'example_check.py', []),
    ('compatibility', 'compat_check.py', []),
    ('evidence', 'evidence_check.py', []),
    ('evals', 'eval_selftest.py', []),
    ('routing', 'routing_check.py', []),
    ('privacy', 'privacy_check.py', []),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--profile')
    ap.add_argument('--root', default=os.path.join(HERE, '..'))
    a = ap.parse_args()

    failed = []
    for name, script, extra in CHECKS:
        args = [sys.executable, os.path.join(HERE, script), '--root', a.root] + extra
        if script == 'privacy_check.py' and a.profile:
            args += ['--profile', a.profile]
        print(f'\n=== {name} ===', flush=True)
        r = subprocess.run(args)
        if r.returncode != 0:
            failed.append(name)

    print('\n' + '=' * 40)
    if failed:
        print('FAILED: ' + ', '.join(failed))
        sys.exit(1)
    print('all checks passed')
    sys.exit(0)


if __name__ == '__main__':
    main()
