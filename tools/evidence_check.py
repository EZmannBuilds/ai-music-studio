#!/usr/bin/env python3
"""Release check: every instrument claim says how it is known, and cannot claim more than that.

usage: python3 tools/evidence_check.py [--root .]

Checks the pages in shared/VIRTUAL_INSTRUMENT_GUIDE/, their research records in
research/instruments/, and the source register research/sources/INSTRUMENT_SOURCES.md, against the
evidence model in shared/RESEARCH_RULES.md and the card format in
shared/INSTRUMENT_BEHAVIOR_SCHEMA.md section 3. Fails (exit 1) when:

  register  - a row is malformed, an id repeats, or a type or read depth is not in tools/vocab.json;
  pages     - a behaviour card is missing a row, has an unknown or repeated row, or its evidence cell
              is not a known label; an "unresolved:" row is not labelled to-verify;
            - an evidence tag names an unknown label, a source missing from the register, or a
              source not read deeply enough for the label (tools/vocab.json evidence_label_needs_read);
            - a section of prose carries no evidence tag at all;
            - a 2.0 label (`musicianship`, `orchestration-text`, `excerpt-derived`) survives;
            - a controller number or a velocity zone appears (calibration facts, not guide facts);
            - a tradition-specific page lacks its context link or its three required sections;
            - a page has no research page;
  records   - a research record lacks a field, has an unknown confidence, cites an unknown source,
              or states a read depth the register contradicts;
  headings  - a heading in the guide or the musical-systems folder uses a continent, "world",
              "ethnic", "exotic", "oriental" or "tribal" as a category (shared/MUSICAL_SYSTEMS/INDEX.md
              rule 2).

Pages not yet moved to the 2.1 evidence model are listed in tools/vocab.json evidence_pending, and
system files whose bucket title is being decomposed in bucket_pending. They are reported but do not
fail, and the lists must shrink: a listed page that has been migrated is a finding, so the list
cannot go stale. Nothing is changed.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
GUIDE = 'shared/VIRTUAL_INSTRUMENT_GUIDE'
SYSTEMS = 'shared/MUSICAL_SYSTEMS'
REGISTER = 'research/sources/INSTRUMENT_SOURCES.md'
RESEARCH = 'research/instruments'
NOT_INSTRUMENT_PAGES = {'INDEX.md', 'COMMON_ERRORS.md', 'CULTURALLY_SPECIFIC_INSTRUMENTS.md'}
UNTAGGED_SECTIONS = {'behaviour cards', 'sources and what to verify',
                     'what the performance director needs from this file'}
TRADITION_SECTIONS = ['what virtual implementations commonly get wrong',
                      'what must not be generalised outside the tradition',
                      'restricted and ceremonial repertoire']
RECORD_FIELDS = ['claim', 'source', 'source_type', 'confidence', 'scope', 'limitations', 'inference']
LABELS_WITH_SOURCES = {'sourced', 'academic', 'manual-derived', 'standard-reference'}
OLD_LABELS = re.compile(r'`(musicianship|orchestration-text|excerpt-derived)`')
TAG = re.compile(r'\[(sourced|academic|manual-derived|standard-reference|measured|inference|'
                 r'to-verify|musicianship|orchestration-text|excerpt-derived)(?::\s*([^\]]*))?'
                 r'(?:\s\+\s[^\]]*)?\]')
SOURCE_ID = re.compile(r'^[A-Z0-9][A-Z0-9-]*[A-Z0-9]$')
CONTROLLER = re.compile(r'\b(?:CC|cc)\s?#?\d{1,3}\b')
VELOCITY_ZONE = re.compile(r'\bvelocit(?:y|ies)\s+(?:of\s+|from\s+)?\d{1,3}\s*(?:to|-|–)\s*\d{1,3}\b', re.I)
NEGATION = re.compile(r'\b(?:never|not|no|avoid|without)\b', re.I)  # a rule that forbids the bucket
BUCKET = re.compile(
    r'\b(?:world|ethnic|exotic|oriental|tribal)\b|'
    r'\b(?:african|asian|middle[- ]eastern|south[- ]asian|east[- ]asian|west[- ]african|'
    r'latin[- ]american|european)\s+(?:instruments?|music|rhythms?|polyrhythm|percussion|drums?)\b',
    re.I)


def strip_code(text):
    return re.sub(r'^```.*?^```', '', text, flags=re.S | re.M)


def table_rows(block):
    rows = []
    for line in block.split('\n'):
        s = line.strip()
        if s.startswith('|') and s.endswith('|'):
            cells = [c.strip() for c in s[1:-1].split('|')]
            if cells and not set(''.join(cells)) <= set('-: '):
                rows.append(cells)
    return rows


def parse_register(root, vocab, problems):
    path = os.path.join(root, REGISTER)
    if not os.path.exists(path):
        problems.append(f'{REGISTER}: missing')
        return {}
    types = set(vocab['vocabularies']['source_type'])
    depths = set(vocab['vocabularies']['source_read_depth'])
    reg = {}
    text = open(path, encoding='utf-8').read()
    sec = text.split('## Sources', 1)[1] if '## Sources' in text else ''
    for cells in table_rows(sec):
        if cells[0] == 'id':
            continue
        if len(cells) != 6:
            problems.append(f'{REGISTER}: row for {cells[0]!r} has {len(cells)} cells, not 6')
            continue
        sid, cite, typ, read, url, accessed = cells
        if not SOURCE_ID.match(sid):
            problems.append(f'{REGISTER}: id {sid!r} is not UPPERCASE-WITH-HYPHENS')
        if sid in reg:
            problems.append(f'{REGISTER}: id {sid} appears twice')
        if typ not in types:
            problems.append(f'{REGISTER}: {sid}: type {typ!r} is not one of {sorted(types)}')
        if read not in depths:
            problems.append(f'{REGISTER}: {sid}: read {read!r} is not one of {sorted(depths)}')
        if not url:
            problems.append(f'{REGISTER}: {sid}: url is empty; write "none" for print-only sources')
        reg[sid] = read
    return reg


def check_sources(where, label, ids_text, reg, needs, problems):
    if label not in LABELS_WITH_SOURCES:
        return
    ids = [x.strip() for x in re.split(r'[;,]', ids_text or '') if x.strip()]
    if not ids:
        problems.append(f'{where}: [{label}] names no source')
    for sid in ids:
        if sid not in reg:
            problems.append(f'{where}: source {sid} is not in {REGISTER}')
        elif reg[sid] not in needs.get(label, []):
            problems.append(f'{where}: {sid} was read at "{reg[sid]}" depth, which does not support '
                            f'[{label}]; use standard-reference or read it')


def segments(ev):
    """An evidence cell or tag may combine support for different parts of one claim, joined by
    ' + ': `academic: WOLFE-CLARINET + inference`. Returns [(label, ids_text)]."""
    out = []
    for part in ev.split(' + '):
        m = re.match(r'^\s*([a-z-]+)(?::\s*(.*))?$', part.strip())
        out.append((m.group(1), (m.group(2) or '').strip()) if m else (None, part.strip()))
    return out


def sections(text):
    """(heading, body) for every level-2 section, with code blocks removed."""
    parts = re.split(r'^## (.+)$', strip_code(text), flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def check_page(rel, text, reg, vocab, problems):
    labels = set(vocab['vocabularies']['guide_evidence']) - {'measured'}
    needs = vocab['evidence_label_needs_read']
    fields = vocab['instrument_card_fields']

    # behaviour cards
    cards_sec = dict((h.lower(), b) for h, b in sections(text)).get('behaviour cards', '')
    cards = re.split(r'^### (.+)$', cards_sec, flags=re.M)
    if len(cards) < 3:
        problems.append(f'{rel}: "## Behaviour cards" has no "### <instrument>" card')
    for i in range(1, len(cards) - 1, 2):
        name, body = cards[i].strip(), cards[i + 1]
        rows = table_rows(body)
        for table, want in fields.items():
            got = [r for r in rows if r[0] in want]
            present = [r[0] for r in got]
            missing = [f for f in want if f not in present]
            dup = sorted({f for f in present if present.count(f) > 1})
            if not any(r[0] == table for r in rows):
                problems.append(f'{rel}: card "{name}" has no {table} table')
                continue
            if missing:
                problems.append(f'{rel}: card "{name}" {table} is missing {", ".join(missing)}')
            if dup:
                problems.append(f'{rel}: card "{name}" repeats {", ".join(dup)}')
            for r in got:
                where = f'{rel}: card "{name}" {r[0]}'
                if len(r) != 3:
                    problems.append(f'{where}: has {len(r)} cells, not 3 (a "|" inside a cell?)')
                    continue
                ev = r[2]
                segs = segments(ev)
                if any(lab not in labels for lab, _ in segs):
                    problems.append(f'{where}: evidence {ev!r} is not a label from '
                                    f'shared/RESEARCH_RULES.md')
                    continue
                if r[1].lower().startswith('unresolved') and any(l != 'to-verify' for l, _ in segs):
                    problems.append(f'{where}: an unresolved row must be labelled to-verify')
                for lab, ids in segs:
                    if lab == 'to-verify' and not ids:
                        problems.append(f'{where}: to-verify must say what would settle it')
                    check_sources(where, lab, ids, reg, needs, problems)
        known = {f for w in fields.values() for f in w} | set(fields)
        for r in rows:
            if r[0] not in known and r[0] not in ('field',):
                problems.append(f'{rel}: card "{name}" has an unknown row {r[0]!r}')

    # tags in prose and in the other tables
    for m in TAG.finditer(strip_code(text)):
        where = f'{rel}: tag {m.group(0)[:50]}'
        # a tag may wrap across a line break in the source; read it as one line
        for label, ids in segments(re.sub(r'\s+', ' ', m.group(0)[1:-1])):
            if label not in labels:
                problems.append(f'{rel}: tag uses the 2.0 or reserved label "{label}"')
                continue
            if label == 'to-verify' and not ids:
                problems.append(f'{where}: to-verify must say what would settle it')
            check_sources(where, label, ids, reg, needs, problems)

    for heading, body in sections(text):
        if heading.lower() in UNTAGGED_SECTIONS:
            continue
        if not TAG.search(body):
            problems.append(f'{rel}: section "{heading}" carries no evidence tag')

    for m in OLD_LABELS.finditer(text):
        problems.append(f'{rel}: 2.0 label `{m.group(1)}` survives; relabel it')
    prose = strip_code(text)
    for pat, what in ((CONTROLLER, 'controller number'), (VELOCITY_ZONE, 'velocity zone')):
        for m in pat.finditer(prose):
            problems.append(f'{rel}: {what} "{m.group(0)}" belongs in a calibration profile')

    heads = [h.lower() for h, _ in sections(text)]
    if 'tradition and context' in heads or re.search(r'^Traditions:', text, re.M):
        if f'{SYSTEMS}/' not in text:
            problems.append(f'{rel}: a tradition-specific page must link its {SYSTEMS}/ file')
        for s in TRADITION_SECTIONS:
            if s not in heads:
                problems.append(f'{rel}: a tradition-specific page needs "## {s[0].upper() + s[1:]}"')


def check_records(root, stem, reg, vocab, problems):
    rel = f'{RESEARCH}/{stem}.md'
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        problems.append(f'{GUIDE}/{stem}.md: no research page at {rel}')
        return
    text = open(path, encoding='utf-8').read()
    conf = set(vocab['vocabularies']['record_confidence'])
    recs = text.split('## Records', 1)[1] if '## Records' in text else ''
    recs = re.split(r'^## ', recs, flags=re.M)[0]
    blocks = re.split(r'^### (.+)$', recs, flags=re.M)
    if len(blocks) < 3:
        problems.append(f'{rel}: no "### <record>" under "## Records"')
    for i in range(1, len(blocks) - 1, 2):
        name, body = blocks[i].strip(), blocks[i + 1]
        got = dict(re.findall(r'^- ([a-z_]+):\s*(.*)$', body, re.M))
        for f in RECORD_FIELDS:
            if f not in got:
                problems.append(f'{rel}: record "{name}" has no {f}')
        if 'confidence' in got and got['confidence'].strip().lower() not in conf:
            problems.append(f'{rel}: record "{name}" confidence {got["confidence"]!r} is not one of '
                            f'{sorted(conf)}')
        for sid, depth in re.findall(r'\b([A-Z0-9][A-Z0-9-]*[A-Z0-9])\b(?:\s*\(([a-z-]+)\))?',
                                     got.get('source', '')):
            if sid not in reg:
                problems.append(f'{rel}: record "{name}" cites {sid}, which is not in {REGISTER}')
            elif depth and depth != reg[sid]:
                problems.append(f'{rel}: record "{name}" says {sid} was read at "{depth}"; the '
                                f'register says "{reg[sid]}"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    vocab = json.load(open(os.path.join(root, 'tools', 'vocab.json'), encoding='utf-8'))
    pending = set(vocab.get('evidence_pending', []))
    bucket_pending = set(vocab.get('bucket_pending', []))
    problems, notes, n = [], [], 0

    reg = parse_register(root, vocab, problems)

    gdir = os.path.join(root, GUIDE)
    for f in sorted(os.listdir(gdir)):
        if not f.endswith('.md') or f in NOT_INSTRUMENT_PAGES:
            continue
        rel = f'{GUIDE}/{f}'
        text = open(os.path.join(gdir, f), encoding='utf-8').read()
        carded = re.search(r'^## Behaviour cards\s*$', text, re.M) is not None
        if f in pending:
            if carded:
                problems.append(f'{rel}: is migrated but still listed in tools/vocab.json '
                                f'evidence_pending; remove it from the list')
            else:
                notes.append(f)
            continue
        if not carded:
            problems.append(f'{rel}: has no "## Behaviour cards" and is not listed as pending')
            continue
        n += 1
        check_page(rel, text, reg, vocab, problems)
        check_records(root, f[:-3], reg, vocab, problems)

    for sub in (GUIDE, SYSTEMS):
        d = os.path.join(root, sub)
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            for i, line in enumerate(open(os.path.join(d, f), encoding='utf-8'), 1):
                rel_f = f'{sub}/{f}'
                if (line.startswith('#') and BUCKET.search(line) and not NEGATION.search(line)
                        and rel_f not in bucket_pending):
                    problems.append(f'{sub}/{f}:{i}: heading uses a bucket as a category: '
                                    f'{line.strip()}')

    for rel_f in sorted(bucket_pending):
        if not os.path.exists(os.path.join(root, rel_f)):
            problems.append(f'{rel_f}: listed in bucket_pending but does not exist')
        else:
            first = open(os.path.join(root, rel_f), encoding='utf-8').readline()
            if not BUCKET.search(first):
                problems.append(f'{rel_f}: no longer has a bucket title; remove it from bucket_pending')
            else:
                notes.append(rel_f.rsplit('/', 1)[1] + ' (bucket title)')

    for p in problems:
        print(p)
    tail = f'; {len(notes)} page(s) still on the 2.0 evidence model: {", ".join(notes)}' if notes else ''
    print(f'{len(problems)} finding(s) in {n} migrated page(s), {len(reg)} source(s){tail}')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
