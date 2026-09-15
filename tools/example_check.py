#!/usr/bin/env python3
"""Release check: the examples and the profile template obey the schemas they illustrate.

usage: python3 tools/example_check.py [--root .]

Every file in examples/ and profiles/user-profile.example.yaml names its schema in a header comment
("# Schema: shared/...md"). This check parses each example and fails (exit 1) when:
  - a YAML or JSON example does not parse;
  - a value is not one of the choices its own schema lists for that key (a line such as
    "status: clear | ask" in the schema);
  - a value is outside a vocabulary in tools/vocab.json that governs its key (key_vocabularies),
    allowing the documented aliases;
  - a path the example points into the pack does not exist;
  - a Track DNA row uses a dimension the ledger does not define, or the example's
    diversity_comparison disagrees with its own rows (shared, distinct, classified, unclassified);
  - a lyric-alignment syllable uses a field the lyric schema does not define.

Examples teach by being copied, so an example that contradicts its schema teaches the
contradiction. PyYAML is needed for the YAML examples; without it they are skipped and said to be.
Nothing is changed.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from schema_check import blocks  # noqa: E402

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

ROOT = os.path.join(HERE, '..')
SCHEMA_REF = re.compile(r'Schema[^:\n]*:\s*(shared/[\w/.-]+\.md)')
CHOICE_LINE = re.compile(r'^\s*-?\s*([A-Za-z_][\w]*):\s*([^#\n]*?)\s*(?:#\s*(.*))?$')
TRACK_DNA_META = {'song', 'project', 'written', 'melody_variety_report', 'lyric_uniqueness_report'}


def choice_lists(schema_path):
    """(parent key, key) -> set of allowed values, from `key: a | b | c` lines and
    `key:  # a | b | c` comments in the schema's yaml blocks. The parent is the enclosing mapping
    key, found by indentation, because the same key name can be free text in one record and a
    closed list in another. A comment list counts only when it looks like a closed list: every item
    is short and none is an ellipsis or an example."""
    out = {}
    for lang, _, text in blocks(schema_path):
        if lang != 'yaml':
            continue
        stack = []  # (indent, key)
        for line in text.split('\n'):
            m = CHOICE_LINE.match(line)
            if not m:
                continue
            indent = len(line) - len(line.lstrip(' -'))
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1] if stack else ''
            key, val, comment = m.group(1), m.group(2), m.group(3) or ''
            stack.append((indent, key))
            src = val if '|' in val else (comment if '|' in comment and not val else '')
            if not src or src.startswith(('[', '{')):
                continue
            items = [x.strip().strip('"\'') for x in src.split('|')]
            if any(x in ('', '...') or '...' in x or x.startswith(('e.g', 'or ')) or len(x.split()) > 3
                   for x in items):
                continue
            out.setdefault((parent, key), set()).update(items)
    return out


def walk(node, path=()):
    """Yield (path, key, value) for every mapping entry, depth first."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield path, k, v
            yield from walk(v, path + (str(k),))
    elif isinstance(node, list):
        for item in node:
            yield from walk(item, path + ('[]',))


def norm(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    return str(v)


def check_track_dna(doc, vocab, rel, problems):
    dims = set(vocab.get('track_dna_dimensions', []))
    vocal_fields = set(vocab.get('vocal_dna_fields', []))
    rows = [r.get('track_dna', {}) for r in doc.get('rows', []) if isinstance(r, dict)]
    for r in rows:
        for k in r:
            if k not in dims and k not in TRACK_DNA_META:
                problems.append(f'{rel}: track_dna row "{r.get("song")}" uses {k!r}, which '
                                f'shared/TRACK_DIVERSITY_LEDGER.md does not define')
        va = r.get('vocal_architecture') or {}
        if isinstance(va, dict) and vocal_fields:
            for k in va:
                if k not in vocal_fields:
                    problems.append(f'{rel}: vocal_architecture in "{r.get("song")}" uses {k!r}, '
                                    f'which shared/VOCAL_ARCHITECTURE_SCHEMA.md section 3 does not define')
    comp = doc.get('diversity_comparison')
    if not comp or not rows:
        return
    names = [r.get('song') for r in rows]
    if comp.get('rows_compared') != names:
        problems.append(f'{rel}: rows_compared {comp.get("rows_compared")} != the rows {names}')
    if len(rows) < 3:
        problems.append(f'{rel}: compares {len(rows)} rows, but "shared" means 3 or more agree '
                        f'(shared/TRACK_DIVERSITY_LEDGER.md section 4)')
    decided = [d for d in dims if all(r.get(d) is not None for r in rows)]
    shared = {d for d in decided if all(json.dumps(r.get(d), sort_keys=True) ==
                                        json.dumps(rows[0].get(d), sort_keys=True) for r in rows)}
    distinct = set(decided) - shared
    declared_shared = set(comp.get('shared_dimensions') or [])
    declared_distinct = set(comp.get('distinct_dimensions') or [])
    if declared_shared != shared:
        problems.append(f'{rel}: shared_dimensions should be {sorted(shared)}; missing '
                        f'{sorted(shared - declared_shared)}, extra {sorted(declared_shared - shared)}')
    if declared_distinct and declared_distinct != distinct:
        problems.append(f'{rel}: distinct_dimensions should be {sorted(distinct)}')
    classes = set(vocab.get('vocabularies', {}).get('diversity_classification', []))
    classified = comp.get('classification') or {}
    for k, v in classified.items():
        if k not in shared:
            problems.append(f'{rel}: classifies {k!r}, which is not a shared dimension')
        if classes and v not in classes:
            problems.append(f'{rel}: classification {k}: {v!r} is not one of {sorted(classes)}')
    unclassified = set(comp.get('unclassified') or [])
    if unclassified != shared - set(classified):
        problems.append(f'{rel}: unclassified should be {sorted(shared - set(classified))}')
    want = 'ask' if unclassified else 'clear'
    if comp.get('status') != want:
        problems.append(f'{rel}: status should be {want!r} when unclassified is '
                        f'{"non-empty" if unclassified else "empty"}')


def check_lyric_json(doc, root, rel, problems):
    schema = os.path.join(root, 'shared', 'LYRIC_ALIGNMENT_SCHEMA.md')
    allowed = set()
    for lang, _, text in blocks(schema):
        if lang == 'yaml' and 'syllables:' in text:
            tail = text.split('syllables:', 1)[1]
            allowed |= set(re.findall(r'^\s*-?\s*([a-z_]+):', tail, re.M))
    for i, syl in enumerate(doc.get('syllables', [])):
        for k in syl:
            if allowed and k not in allowed:
                problems.append(f'{rel}: syllable {i} uses {k!r}, which LYRIC_ALIGNMENT_SCHEMA '
                                f'does not define for a syllable')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems, checked, skipped = [], 0, []

    vocab = json.load(open(os.path.join(root, 'tools', 'vocab.json'), encoding='utf-8'))
    vocabs = vocab.get('vocabularies', {})
    aliases = vocab.get('aliases', {})
    key_vocabs = vocab.get('key_vocabularies', {})

    targets = []
    ex = os.path.join(root, 'examples')
    if os.path.isdir(ex):
        targets += [os.path.join(ex, f) for f in sorted(os.listdir(ex))
                    if f.endswith(('.yaml', '.yml', '.json'))]
    tpl = os.path.join(root, 'profiles', 'user-profile.example.yaml')
    if os.path.exists(tpl):
        targets.append(tpl)

    for path in targets:
        rel = os.path.relpath(path, root).replace(os.sep, '/')
        text = open(path, encoding='utf-8').read()
        if path.endswith('.json'):
            try:
                doc = json.loads(text)
            except Exception as e:
                problems.append(f'{rel}: does not parse: {e}')
                continue
        else:
            if not HAVE_YAML:
                skipped.append(rel)
                continue
            try:
                doc = yaml.safe_load(text)
            except Exception as e:
                problems.append(f'{rel}: does not parse: {str(e).splitlines()[0]}')
                continue
        checked += 1

        m = SCHEMA_REF.search(text[:600])
        choices = {}
        if m:
            spath = os.path.join(root, m.group(1))
            if not os.path.exists(spath):
                problems.append(f'{rel}: names schema {m.group(1)}, which does not exist')
            else:
                choices = choice_lists(spath)

        for path_, key, val in walk(doc):
            if isinstance(val, (dict, list)) or val is None or val == '':
                continue  # an empty value is "not set", which every schema allows
            v = norm(val)
            parent = next((x for x in reversed(path_) if x != '[]'), '')
            if key in key_vocabs:
                vname = key_vocabs[key]
                allowed = set(vocabs.get(vname, vocab.get(vname, [])))
                if allowed and v not in allowed and v not in aliases.get(vname, {}):
                    problems.append(f'{rel}: {".".join(path_ + (key,))}: {v!r} is not in '
                                    f'vocabulary {vname} {sorted(allowed)}')
                continue
            allowed = choices.get((parent, key))
            if allowed and v not in allowed:
                problems.append(f'{rel}: {".".join(path_ + (key,))}: {v!r} is not one of the '
                                f'choices its schema lists: {sorted(allowed)}')
            if key.endswith(('guide_file', 'schema_file')) and v.startswith(('shared/', 'research/')):
                if not os.path.exists(os.path.join(root, v)):
                    problems.append(f'{rel}: {key} points to {v}, which does not exist')

        if isinstance(doc, dict) and 'rows' in doc:
            check_track_dna(doc, vocab, rel, problems)
        if isinstance(doc, dict) and 'syllables' in doc and path.endswith('.json'):
            check_lyric_json(doc, root, rel, problems)

    for p in problems:
        print(p)
    note = f'; skipped without PyYAML: {", ".join(skipped)}' if skipped else ''
    print(f'{len(problems)} finding(s) in {checked} example(s){note}')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
