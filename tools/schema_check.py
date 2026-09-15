#!/usr/bin/env python3
"""Release check: the YAML blocks parse, and the shared vocabularies agree.

usage: python3 tools/schema_check.py [--root .]

Fails (exit 1) when:
  - a ```yaml block in a shared schema or a SKILL.md does not parse;
  - a fenced block is left unclosed;
  - a pipe-separated choice list has drifted from a vocabulary in tools/vocab.json, which is
    checked by its values rather than by its key, because the same choices appear under several
    key names;
  - the ledger's track_dna block or the exploration dimension list has drifted from vocab.json.

PyYAML is used when it is installed. Without it the parse check is skipped and the rest still runs,
so the tool is useful on a bare Python 3. Nothing is changed.
"""
import argparse, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKIP_DIRS = {'.git', 'local', '__pycache__'}

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

FENCE = re.compile(r'^```(\w*)\s*$')


def blocks(path):
    """Yield (language, start_line, text) for every fenced block, and flag an unclosed fence."""
    lang, start, buf, unclosed = None, 0, [], None
    for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        m = FENCE.match(line.rstrip('\n'))
        if m and lang is None:
            lang, start, buf = m.group(1) or 'text', i, []
        elif line.rstrip('\n').startswith('```') and lang is not None:
            yield lang, start, ''.join(buf)
            lang = None
        elif lang is not None:
            buf.append(line)
    if lang is not None:
        unclosed = start
    if unclosed:
        yield '__unclosed__', unclosed, ''


def placeholder_free(text):
    """Blocks in this pack are schemas with empty values and pipe-separated choices.
    Turn them into something a YAML parser can accept, so the check finds real breakage
    (bad indentation, a stray tab, an unclosed quote) rather than the house style."""
    out = []
    for line in text.split('\n'):
        if '#' in line:
            q = line.split('#')[0]
            if q.count('"') % 2 == 0 and q.count("'") % 2 == 0:
                line = q.rstrip()
        if not line.strip():
            continue
        m = re.match(r'^(\s*-?\s*[\w.\'"\[\]<> -]+:)\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if '|' in val and not val.startswith(('[', '{', '"', "'")):
                val = ''
            if val.endswith(':'):
                val = ''
            line = f'{key} {val}'.rstrip()
        out.append(line)
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems, n_blocks = [], 0

    vocab_path = os.path.join(root, 'tools', 'vocab.json')
    vocab = json.load(open(vocab_path, encoding='utf-8')) if os.path.exists(vocab_path) else {}
    vocabs = vocab.get('vocabularies', {})

    md = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in sorted(fn):
            if f.endswith('.md'):
                md.append(os.path.join(dp, f))

    for path in md:
        rel = os.path.relpath(path, root).replace(os.sep, '/')
        for lang, line_no, text in blocks(path):
            if lang == '__unclosed__':
                problems.append(f'{rel}:{line_no}: fenced block is never closed')
                continue
            if lang != 'yaml':
                continue
            n_blocks += 1
            if '\t' in text:
                problems.append(f'{rel}:{line_no}: tab character in a yaml block')
            if HAVE_YAML:
                try:
                    yaml.safe_load(placeholder_free(text))
                except Exception as e:
                    first = str(e).split('\n')[0]
                    problems.append(f'{rel}:{line_no}: yaml block does not parse: {first}')

        # Vocabulary agreement, checked by value rather than by key. The same choices appear
        # under several key names (mode, deliverable_mode, tier_used), so matching on the key
        # misses real drift. A choice list that mostly matches a vocabulary and has one member
        # outside it is the drift worth catching.
        txt = open(path, encoding='utf-8', errors='replace').read()
        for i, line in enumerate(txt.split('\n'), 1):
            m = re.match(r'^\s*[\w.]+:\s*([^#\n]*\|[^#\n]*)$', line)
            if not m:
                continue
            parts = [v.strip() for v in m.group(1).split('|') if v.strip()]
            if len(parts) < 2 or any(p.startswith(('<', '[', '{')) for p in parts):
                continue
            # A list that is wholly inside some declared vocabulary is correct, whatever else
            # it partially resembles. Two vocabularies can legitimately share members.
            if any(all(p in allowed for p in parts) for allowed in vocabs.values()):
                continue
            near = []
            for key, allowed in vocabs.items():
                hits = [p for p in parts if p in allowed]
                misses = [p for p in parts if p not in allowed]
                if len(hits) >= 2 and misses and len(hits) >= len(misses):
                    near.append((len(hits), key, misses))
            if near:
                _, key, misses = max(near)
                problems.append(
                    f'{rel}:{i}: choice list looks like the {key} vocabulary but adds '
                    f'{misses}; either add it to tools/vocab.json or use the vocabulary')

    # the ledger and the exploration schema define lists that other files rely on
    def check_list(rel_path, marker, expected, label):
        p = os.path.join(root, rel_path)
        if not os.path.exists(p):
            problems.append(f'{rel_path}: missing, so {label} cannot be checked')
            return
        txt = open(p, encoding='utf-8').read()
        missing = [d for d in expected if d not in txt]
        if missing:
            problems.append(f'{rel_path}: {label} missing from the page: {missing}')

    check_list('shared/TRACK_DIVERSITY_LEDGER.md', 'track_dna',
               vocab.get('track_dna_dimensions', []), 'track_dna dimensions')
    check_list('shared/CREATIVE_EXPLORATION_SCHEMA.md', 'dimensions',
               vocab.get('exploration_dimensions', []), 'exploration dimensions')
    check_list('shared/HUMAN_PERFORMANCE_SCHEMA.md', 'models',
               vocab.get('timing_models', []), 'timing models')

    for p in problems:
        print(p)
    note = '' if HAVE_YAML else ' (PyYAML not installed: parse check skipped)'
    print(f'{len(problems)} finding(s) in {n_blocks} yaml block(s){note}')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
