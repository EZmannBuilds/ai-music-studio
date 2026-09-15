# Research Use Rules

The research integrated into this skill is evidence, not a universal aesthetic.

## Do not turn empirical averages into laws

Examples:

- Moderate syncopation produced the strongest groove ratings in specific experimental
  paradigms. This does not mean every groove should use "medium syncopation."
- Intermediate predictive complexity is often pleasurable, but artistic goals may require
  extreme simplicity, repetition, or instability.
- Vocal signals are highly salient in many popular-music mixtures, but not every record
  should center vocals.
- Major/minor emotional associations vary with cultural exposure and context.

## Separate three levels of claim

```text
MEASURED
Directly observed in a user's audio, MIDI, WavRead report, or analyzer.

RESEARCH-SUPPORTED
A tendency supported by cited studies.

CREATIVE INFERENCE
A recommendation made for this specific track.
```

Never present a creative inference as a measurement.

**MEASURED means this user's material and nothing else**: their audio, their MIDI, their analyzer
report, their calibration render. A figure someone else measured and published, however careful,
is RESEARCH-SUPPORTED and is cited as the source's finding, with whose instruments or recordings it
measured.

## Evidence labels for the pack's own knowledge

The three levels describe claims made about a track. The knowledge pages, starting with
`shared/VIRTUAL_INSTRUMENT_GUIDE/`, label each claim more finely, by how it is known:

| Label | Means | Level |
|---|---|---|
| `sourced` | read directly in pedagogy, performer, orchestration or tradition-institution text | RESEARCH-SUPPORTED |
| `academic` | read in a scholarly acoustics, perception or ethnomusicology work, at least the relevant section | RESEARCH-SUPPORTED |
| `manual-derived` | read in a manufacturer's manual; scoped to that kind of product | RESEARCH-SUPPORTED, product-scoped |
| `standard-reference` | attributed to a published source that was not read at section depth here: known from an abstract, an excerpt, or its standard attribution | RESEARCH-SUPPORTED, weak |
| `measured` | this user's material or calibration; never used in a knowledge page | MEASURED |
| `inference` | musicianship reasoning that no read source states | CREATIVE INFERENCE |
| `to-verify` | named with what would settle it | not usable as fact |

A label is written as a tag at the end of the sentence, bullet or paragraph it covers:
`[academic: WOLFE-CLARINET]`, `[standard-reference: FLETCHER-ROSSING-1998]`, `[inference]`,
`[to-verify: what would settle it]`. A claim whose parts rest on different support says so with
` + `: `[academic: WOLFE-CLARINET + inference]`. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`,
which records once, for every source, **how much of it was actually read**: `full`, `section`,
`excerpt`, `abstract` or `not-read`. `sourced`, `academic` and `manual-derived` need a source read
at `section` depth or more. Anything read less is `standard-reference` at best. `tools/evidence_check.py`
enforces this, so a label cannot be upgraded by assertion.

**Do not quietly upgrade a claim.** A claim moves from `inference` or `to-verify` to a stronger label
only when a source is read that states it, and that source is added to the register with its read
depth. Output carries the label forward: a `to-verify` claim is said to be unverified when it is
used.

The 2.0 labels are read as follows: `musicianship` → `inference`; `orchestration-text` and
`excerpt-derived` → `standard-reference`.

## Research records

The knowledge pages carry conclusions. The evidence behind them, and its limits, sits in research
pages (`research/instruments/` for instruments) as one record per claim or closely related group of
claims:

```yaml
research_record:
  claim:            # as the knowledge page states it
  source: []        # register IDs, each with its read depth
  source_type:      # pedagogy | orchestration | academic acoustics | perception | ethnomusicology |
                    # performer | manual | specification | tradition institution | standard reference
  confidence:       # high | medium | low
  scope:            # which instruments, styles, eras, players or corpus the claim covers
  limitations:      # what the source does not show, and where it may not generalise
  inference:        # what the page infers beyond the source, or "none"
  tradition_scope:  # for tradition-specific claims: which tradition, school or corpus
```

A research page is written as a Markdown list of these fields under a heading per record, so it
reads as prose and parses as data. Skills and knowledge pages link to the research page; they do
not repeat its citations.

## Audience calibration

Expectation is listener-dependent.

Consider:
- genre familiarity;
- musical training;
- cultural exposure;
- age/context;
- listening environment;
- target community.

A surprising jazz voicing may be ordinary to a jazz listener and highly surprising to a
mainstream-pop listener.

## Human preference remains authoritative

Automatic metrics can diagnose:
- repetition;
- spectral balance;
- tempo;
- pitch/rhythm regularity;
- structural similarity.

They do not determine:
- beauty;
- emotional truth;
- originality;
- artistic importance;
- whether a hook actually works for the target audience.
