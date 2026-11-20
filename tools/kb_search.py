"""Search the knowledge library and return only the relevant sections, not whole files.

Usage (from the studio folder): python3 tools/kb_search.py "trap 808 slide kick" [-n 5] [--full]
Indexes every "## " section of the markdown in shared/MIDI_KNOWLEDGE/ (and its local/ when present),
scores sections by TF-IDF over words and genre/role synonyms, and prints the best ones with their file and
heading, so the agent loads a few hundred words instead of the whole library.
"""
import argparse, math, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "shared", "MIDI_KNOWLEDGE")
SYN = {
    "808": ["808", "sub", "low", "bass"], "hats": ["hat", "hats", "hihat", "roll", "rolls"], "hihat": ["hat", "hats"],
    "groove": ["swing", "pocket", "placement", "jitter", "timing", "feel"], "humanize": ["placement", "jitter", "velocity", "played", "feel"],
    "human": ["played", "placement", "jitter", "velocity"], "drill": ["drill", "triplet", "808", "slide"], "trap": ["trap", "808", "roll", "half-time"],
    "boombap": ["boom-bap", "hip-hop", "swing", "ghost"], "neosoul": ["neo-soul", "r&b", "soul", "swing", "chords"],
    "rnb": ["r&b", "neo-soul", "soul"], "funk": ["funk", "ghost", "swing", "pocket"], "melody": ["melody", "hook", "steps", "leaps", "phrase"],
    "hook": ["hook", "cell", "motif", "repeat"], "arp": ["arp", "arpeggio", "broken-chord"], "counterpoint": ["contrary", "voices", "parallel", "independence"],
    "arrangement": ["section", "boundary", "layers", "density", "form"], "revise": ["revision", "revise", "measure", "check"],
    "bass": ["bass", "low", "kick", "walk"], "kick": ["kick", "808", "low"], "chords": ["chords", "voicing", "register", "harmony"],
    "house": ["house", "four-on-the-floor", "offbeat"], "techno": ["techno", "offbeat", "rolling"], "fill": ["fill", "fills", "boundary", "drop"],
}


def sections():
    out = []
    for base, _, files in os.walk(ROOT):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            path = os.path.join(base, f)
            text = open(path, encoding="utf-8").read()
            parts = re.split(r"(?m)^## ", text)
            title = parts[0].splitlines()[0].lstrip("# ").strip() if parts[0].strip() else f
            for p in parts[1:]:
                head, _, body = p.partition("\n")
                out.append((os.path.relpath(path, ROOT), f"{title} > {head.strip()}", body.strip()))
    return out


def toks(s):
    return re.findall(r"[a-z0-9&'-]+", s.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--full", action="store_true", help="print whole sections (default: first 1,200 characters)")
    a = ap.parse_args()
    secs = sections()
    docs = [Counter(toks(h + " " + h + " " + b)) for _, h, b in secs]
    df = Counter(w for d in docs for w in d)
    N = len(docs)
    q = []
    for w in toks(a.query):
        q.append(w)
        q += SYN.get(w.replace("-", ""), [])
    scores = []
    for i, d in enumerate(docs):
        L = sum(d.values()) or 1
        s = sum((d[w] / L) * math.log(1 + N / (1 + df[w])) for w in q if w in d)
        scores.append((s, i))
    for s, i in sorted(scores, reverse=True)[: a.n]:
        if s <= 0:
            break
        f, h, b = secs[i]
        print(f"=== {f} :: {h}  (score {s:.3f})")
        print(b if a.full else (b[:1200] + (" …" if len(b) > 1200 else "")))
        print()


if __name__ == "__main__":
    main()
