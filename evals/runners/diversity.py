"""Batch diversity: B1 and B2 in research/BENCHMARK_DIVERSITY.md, computed.

Given the Track DNA rows from a batch of runs, report for each ledger dimension how many distinct
values appeared, and which dimensions collapsed: a dimension collapses when at least `threshold` of
the rows share one value and the briefs did not imply that value (shared/TRACK_DIVERSITY_LEDGER.md
section 6). The threshold is CREATIVE INFERENCE, as the benchmark says, and is set per case.

Values are compared after light normalisation (case, surrounding spaces, list order is kept), because
"4/4" and "4/4 " are one value. Two different spellings of one idea ("verse/chorus" and
"verse-chorus") are two values: the harness does not guess at meaning, and a human reading the report
can merge them.
"""
import json
from collections import Counter

from graders import Response


def norm(v):
    if isinstance(v, (list, dict)):
        return json.dumps(v, sort_keys=True).lower()
    return str(v).strip().lower()


def rows_from(texts):
    rows = []
    for t in texts:
        r = Response(t)
        dna = r.doc.get('track_dna')
        if isinstance(dna, dict):
            rows.append(dna)
    return rows


def batch_diversity(rows, dimensions, threshold=0.9, watch=None, brief_implied=None):
    brief_implied = {k: {str(x).lower() for x in v} for k, v in (brief_implied or {}).items()}
    per_dim, collapsed = {}, []
    n = len(rows)
    for d in dimensions:
        vals = [norm(r.get(d)) for r in rows if r.get(d) not in (None, '', [], {})]
        if not vals:
            continue
        counts = Counter(vals)
        top, top_n = counts.most_common(1)[0]
        per_dim[d] = {'distinct': len(counts), 'decided_in': len(vals), 'most_common': top,
                      'most_common_count': top_n}
        if n and top_n / n >= threshold and top not in brief_implied.get(d, set()):
            collapsed.append(d)
    watched = [d for d in collapsed if not watch or d in watch]
    return {
        'briefs_compared': n,
        'per_dimension': per_dim,
        'collapsed_dimensions': collapsed,
        'collapsed_watched_dimensions': watched,
        'architecture_collapse': bool(watched),
    }


def candidates_in(text):
    """Every exploration_candidate in a reply, wherever it appears: one block per candidate, a list
    under `candidates`, or a list under `exploration_candidates`."""
    import yaml
    from graders import FENCE
    found = []
    for block in FENCE.findall(text):
        try:
            data = yaml.safe_load(block)
        except Exception:
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if isinstance(node.get('exploration_candidate'), dict):
                    found.append(node['exploration_candidate'])
                    stack.extend(v for k, v in node.items()
                                 if k != 'exploration_candidate' and isinstance(v, (dict, list)))
                    continue
                if 'dimensions_changed' in node:
                    found.append(node)
                stack.extend(v for v in node.values() if isinstance(v, (dict, list)))
            elif isinstance(node, list):
                stack.extend(node)
    return found


def exploration_frequency(texts, threshold=0.9):
    """B3: across candidate sets from unrelated tasks, which dimensions does the Creative Lab always
    change, and which does it never touch? A dimension changed in at least `threshold` of the sets is
    a habit, which is the failure B3 looks for."""
    sets = [candidates_in(t) for t in texts]
    per_set = [set(d for c in cs for d in (c.get('dimensions_changed') or [])) for cs in sets]
    n = len(per_set)
    counts = Counter(d for s in per_set for d in s)
    always = sorted(d for d, k in counts.items() if n and k / n >= threshold)
    return {'sets_compared': n, 'candidates_per_set': [len(cs) for cs in sets],
            'dimension_counts': dict(sorted(counts.items())), 'always_changed': always}
