"""Manual adapter: read responses that already exist on disk.

Use it to grade answers you collected by hand from any agent, to re-grade an earlier run, and in the
self-test, which grades the hand-written expected responses in evals/expected/.

Layout, under the directory passed as --responses:

    <CASE_ID>/<anything>.md          one file per trial, for an ordinary case
    <CASE_ID>/<set>/<NN>.md          one folder per trial, for a batch case; one file per brief,
                                     in brief order (01.md is the first brief)
"""
import os


def responses_for(case, root):
    base = os.path.join(root, case['id'])
    if not os.path.isdir(base):
        return []
    if case.get('batch'):
        sets = []
        for d in sorted(os.listdir(base)):
            full = os.path.join(base, d)
            if os.path.isdir(full):
                files = sorted(f for f in os.listdir(full) if f.endswith('.md'))
                sets.append([open(os.path.join(full, f), encoding='utf-8').read() for f in files])
        return sets
    return [open(os.path.join(base, f), encoding='utf-8').read()
            for f in sorted(os.listdir(base)) if f.endswith('.md')]
