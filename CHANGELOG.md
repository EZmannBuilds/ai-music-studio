# Changelog

**Release status.** 1.0 is the only published release. 2.0 was a development milestone that was
never released. 2.1 is being built and tested on `main`. A version with a suffix (`-dev`, `-beta.N`,
`-rc.N`) is not a release.

## 2.1-dev — unreleased, in development and testing

2.1 adds no specialists. It makes what 2.0 already claims better sourced, more specific and
testable, and it was built and tested on `main` without a release.

### Versioning

- The pack is versioned `2.1-dev` in `manifest.json` and in every skill's front matter, and `music-research`,
  left at 1.1 by 2.0, now agrees with the rest.
- `manifest.json` gains `status` and `stable_release`.
- `tools/manifest_check.py` accepts pre-release versions, requires a pre-release to carry an
  "unreleased" CHANGELOG heading, and now does what its docstring said: it compares the README's
  version, and every skill's front-matter version, with the manifest.
- README opens with the testing status and says where the stable release is. Its routing table now
  matches the Director: Lyric Generator, Listener Model and MIDI Builder were missing, and render
  verification, which is a Director procedure and not a specialist, was listed as one.
- `tools/check_all.py` prints each check's heading before its output when the output is piped.

### Examples and schemas agree, and old files keep reading

- **The Track DNA example contradicted its schema.** It used `chorus_lift_mechanism` where the
  ledger defines `lift_mechanism` (and `vocal_lift_mechanism` inside the vocal record), compared two
  rows where "shared" means three or more agree, left thirteen shared dimensions out of its own
  comparison, and classified a dimension it had not listed. It now compares three rows and its
  comparison is what its rows say. "Chorus lift" is renamed "lift mechanism" in the Director, the
  Arranger, the critics and the benchmark, since most music has no chorus.
- **The profile template's `default_mode: vocal` was never a deliverable mode.** It now reads
  `full_with_vocal`, and a 1.0 or 1.1 profile that says `vocal` is read as `full_with_vocal`, with no
  edit needed. `profile_version` is quoted, because YAML reads an unquoted `1.10` as 1.1.
- The Composer's `midi_spec` no longer carries `humanization_notes`, which 2.0 said it had removed.
- Small corrections: the handoff path in `INTERACTION_MODES`, a wrong section reference in the
  Director, the Creative Lab's description of B1, a miscounted list and a spliced sentence in
  `HUMAN_PERFORMANCE_SCHEMA`, and a note on how the lyric-alignment example relates to its schema.
- **New `tools/example_check.py`**: every example and the profile template are parsed and held to
  the choice lists of the schema they name, to the shared vocabularies, and, for Track DNA, to their
  own rows. No tool read the examples before, which is how the drift above went unnoticed.
- **New `tools/compat_check.py`** with real old files in `evals/fixtures/compatibility/`: the 1.0 and
  1.1 profile templates as released, a 1.0 track state using `wavread_findings`, a 2.0 calibration
  profile, and every path that existed at 2.0. It fails if a key disappears without a documented
  alias, a value stops being accepted, or a file a user's plan may point to is deleted without a
  pointer page.
- **`tools/privacy_check.py` missed real paths.** Its Windows pattern needed doubled backslashes, so
  an ordinary `C:\Users\<name>` path passed; it now also catches forward-slash Windows paths,
  mounted volumes, the home-directory variables on every OS, and names inside MIDI track-name and lyric events. Private terms are matched as
  whole words: with a surname as a private term, 2.0's research citations of Hartmann, Kilchenmann
  and Schumann were false findings, so the check with a real profile could not report zero.
  The tool and the profile template are now scanned for private terms too; they had skipped
  themselves entirely, and the tool's own docstring was carrying a real name as its example.
- `tools/routing_check.py` now holds the README's routing table to the Director too.
- `tools/check_all.py` runs eight checks (ten, with the two below).

### One evidence model for the pack's knowledge

- `shared/RESEARCH_RULES.md` defines one set of evidence labels (`sourced`, `academic`,
  `manual-derived`, `standard-reference`, `measured`, `inference`, `to-verify`), maps each to
  MEASURED, RESEARCH-SUPPORTED or CREATIVE INFERENCE, and defines the `research_record`. **MEASURED
  now means the user's own material only**; a published third-party measurement is a cited finding.
  2.0's six instrument labels were defined four slightly different ways, and nothing checked them.
- `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md` 1.1: a behaviour card per instrument with every behaviour and
  programming field, 1.0 field names kept as aliases, and the rule that human limits (breath, reach,
  roll speed) belong in the guide, because a calibration render measures a patch, not a player.
- `research/sources/INSTRUMENT_SOURCES.md`: one register of every source, with **how much of it was
  actually read**. New `tools/evidence_check.py`: a claim labelled `sourced` or `academic` must cite a
  source read at section depth or more, every card has every row, and no heading uses a continent or
  "world" as a category. Pages not yet migrated are listed and must shrink to none.

### Behavioural evaluation

- **New `evals/`**: 41 cases, covering the whole of `research/BENCHMARK_DIVERSITY.md` (D1-D20,
  B1-B3, N1-N4) plus performance feasibility, routing, cultural-system and compatibility cases.
  Each has a brief written as a user would write it, supplied material, expected routes, required
  and forbidden behaviours, deterministic structural assertions and questions only a person can
  answer.
- `evals/runners/run_evals.py` grades any agent: a **manual** adapter for replies collected by hand,
  and a **command** adapter that runs any command-line agent. Nothing model-specific is in the core.
  Cases run for several trials and report k of k, marking inconsistent cases flaky. Batch cases
  compute architecture collapse across ten briefs (B1, B2) and the Creative Lab's habits across ten
  candidate sets (B3).
- **No quality score exists anywhere.** Every run writes a human evaluation sheet, and listening
  stays the authority.
- The Director writes an optional **session trace** when asked (`shared/SPECIALIST_HANDOFF_SCHEMA.md`),
  so routing and whether the user's material was changed can be checked rather than assumed.
- `tools/eval_selftest.py`, in CI: every case validates, and hand-written passing and failing
  responses prove each grader catches what it claims to, without calling a model.
- `research/EVALUATION.md` records the evidence for the harness's design and where it stops.

### The instrument guide, researched

- **All fourteen family pages were researched and rewritten** against sources that were actually
  read: public-domain orchestration texts (Rimsky-Korsakov, Forsyth), the UNSW music acoustics pages,
  peer-reviewed acoustics and performance papers, pedagogy from named teachers and professional
  societies, and one strings library manual, re-opened for 2.1. Each page opens with a behaviour card
  per instrument, every field present, and each claim's evidence and limits are in
  `research/instruments/`. 185 sources are in the register, across the families and the tradition pages, most read at section depth; the standard
  texts that could not be opened are listed as not read and cited only as `standard-reference`.
- **Factual errors in 2.0 corrected**, each with its source: the harpist's thumb takes the highest
  note of a hand's group, not the lowest; xylophone and glockenspiel ranges were sounding ranges
  labelled as written; the oboist's breath problem is stale air, not shortage; the clavinet is struck,
  not plucked; electric pianos are pedalled much like a piano; every snare roll alternates hands; the
  female primo passaggio sits low; sibilants, not plosives, need the longest consonant lead; no bowed
  chord sustains three strings; stopped-horn pitch differs between the F and B-flat sides; E- and
  A-shape barre chords are movable full voicings; a ghost note is usually a low velocity layer.
- **Coverage added**: saxophones and the woodwind and brass auxiliaries, with written and sounding
  ranges; harpsichord, celesta, accordion and harmonium; solo voice registers and ranges; string
  techniques; drum rudiments and brushes; tubular bells and crotales; a hand-percussion frame page.
- **The three layers are kept apart.** The 40-to-70 ghost-note velocity band and other product facts
  left the guide; human limits (breath, roll speed, reach) are no longer deferred to calibration,
  which measures a patch, not a player. The Plugin Auditor now starts from the instrument's page.
- **Random variation is gone from the advice.** Common error 1 told the reader to vary velocity a few
  points per repetition; it, the bass page and the synth page now name the cause of each difference.
- Sample-library behaviour that no opened manual states is labelled `inference`, not `manual-derived`;
  about seventy such labels were downgraded during integration.

### Instruments of named traditions

- **Fourteen pages for instruments of ten traditions**, on the same footing as the families, each
  through a source gate (two independent specialist sources read at section depth, one of them
  practice) and each with what virtual implementations get wrong, what must not be generalised
  outside the tradition, and the repertoire the studio declines: tanpura, sitar, tabla, mridangam
  (Hindustani and Carnatic, kept distinct); oud, qanun, nay (Arabic maqam); Ewe dance drums; jembe
  and dunun (Mande); Central Javanese and Balinese gamelan instruments, kept apart; Cuban hand
  percussion; Hardanger fiddle; Highland bagpipe.
- **The bansuri did not pass the gate** and has no page: its practitioner sources could not be read.
  The guide's index keeps a coverage record of what was attempted, and
  `research/sources/WAVE2_SOURCE_SURVEY.md` records the sources for seventeen more instruments.
- **`WEST_AFRICAN_POLYRHYTHM` is split** into `EWE_DANCE_DRUMMING` and `MANDE_JEMBE_MUSIC`; the old
  file is a pointer, so existing links resolve. Ewe response drums do answer the lead drum, which 2.0
  denied.
- **`CULTURALLY_SPECIFIC_INSTRUMENTS.md` is rewritten** as the protocol for an instrument with no page
  and the gate for writing one. It no longer presumes such an instrument is monophonic with a drone,
  no longer says a cello is a cello wherever it is played, and declines sacred and restricted
  repertoire rather than handing it to the user as a question.
- `performance_state` gains an optional `performance_reference` (whose practice a plan follows), and
  `TUNING_AND_MPE` gains what the real instrument allows (fixed, fretted, movable-fret,
  mechanism-retuned, continuous) with an optional phrase-shaped `intonation` record.

### Musical and rhythm systems, corrected

- Werckmeister III had five narrowed fifths, which cannot close the circle; it has four.
- The Malian "60:40" was printed as fact in four files while its source was marked unreachable. The
  paper, read for 2.1, gives 58.6:41.4 for one Khasonka piece's bell and 41:31:28 for a Segu Bambara
  piece, and does not report ensembles dropping their fastest layer, which 2.0 attributed to it; that
  claim is now marked unverified.
- One corpus is no longer promoted to a law: Hindustani terms are no longer presented as tala in
  general, Balinese paired detuning no longer as gamelan in general, and "marker parts are never
  humanised" allows a timeline its own documented feel. Brazilian and Haitian timeline practices are
  named as unsourced. Maqam gains its sacred caution. The Euclidean correspondences are "reported",
  not "confirmed".
- Incomplete citations are completed, or marked to verify; the bagpipe's pitch is dated.
- `research/PERFORMANCE_AND_EXPRESSION.md` promised that each claim said what it rested on, and most
  did not; its entries are now read as `standard-reference` unless marked.

### What the first live run found

A smoke run of three cases against a command-line agent (`evals/reports/SMOKE_RUN_2026-09-15.md`)
passed D16 and N1-C and **failed D18**: asked only for help with an unfinished song, the studio chose
`DO IT` and rewrote the user's verse. The pack caused it, and is fixed: the user's own unfinished
work now defaults to review and options (`shared/INTERACTION_MODES.md`), and FINISH no longer means
writing the rest. D18 passed when rerun. Two over-narrow D18 assertions were corrected after reading
the replies, and the record says so.

## 2.0 — 2026-09-14 — development milestone, never released

Commit `8017f2b`. This entry is kept as it was written. 2.0 was merged and pushed but was never
tagged or published as a GitHub Release. The date is corrected from 2026-09-15, which was the UTC
date of the commits; they were made on the evening of 2026-09-14, US Central time.

A creative environment rather than a generator. 1.0 was good at preventing bad and generic decisions.
This release makes the studio able to explore, teach, perform, develop, diagnose, organise and finish
musical work with a user.

### Four new specialists

- **Creative Lab** produces directions that differ by *mechanism*. It names the rules the work is
  currently obeying, then breaks or replaces them, so that a choice between candidates is a real
  choice and not a choice between adjectives. It also runs seed translation, fusion and experimental
  exploration.
- **Performance Director** owns the difference between a list of notes and a performance:
  articulation, phrasing, dynamic arcs, systematic microtiming, physical feasibility, and imperfection
  with a stated reason. **Organic performance is not random humanization**, and the skill has no
  parameter for randomness, because the microtiming research contradicts it.
- **Vocal Director** owns what the voices do. That was previously scattered across four specialists,
  owned by none of them, and defaulting to one arrangement. It will not imitate a living artist's
  voice, and offers the mechanism instead.
- **Project Guide** owns the project over time: thesis, state, track functions, unresolved decisions,
  next actions, and the definition of done. Its most useful behaviour is declining to suggest another
  song when another song is not the answer.

### Session modes

The Music Director now runs a session as CREATE, CONTINUE, DIAGNOSE, LEARN, REVISE, ORGANIZE, FINISH
or RELEASE, and sets an interaction mode for every specialist. **A diagnosis request returns causes
and stops.** A project is loaded at session start and is the single exception to the reset rule,
scoped to itself.

### New shared systems

`PROJECT_STATE_SCHEMA`, `TRACK_DIVERSITY_LEDGER`, `CREATIVE_EXPLORATION_SCHEMA`,
`HUMAN_PERFORMANCE_SCHEMA`, `VOCAL_ARCHITECTURE_SCHEMA`, `INSTRUMENT_BEHAVIOR_SCHEMA`,
`INTERACTION_MODES`, `TUNING_AND_MPE`, `ADAPTIVE_MUSIC`, `SEED_TRANSLATION`, `FUSION_PROTOCOL`,
`EXPERIMENTAL_SYSTEMS`, and three knowledge folders:

- `MUSICAL_SYSTEMS/` — thirteen systems and an index whose first rule is that **a tradition is not a
  scale**;
- `RHYTHM_SYSTEMS/` — eight mechanism files covering metre, additive and non-isochronous metre,
  polymetre, Euclidean generation, metric modulation, cycles, microtiming and displacement;
- `VIRTUAL_INSTRUMENT_GUIDE/` — fourteen instrument families plus a common-errors page, organised
  around what real instruments do before what a sampled one needs.

### Diversity across a body of work

The melody-variety and lyric-uniqueness gates stay where they are and now feed a **track diversity
ledger** covering the whole musical identity. It never forces diversity. It asks whether a shared
dimension is accidental repetition, a project motif, a genre convention or a deliberate callback, and
records the answer.

### Tuning and expression

A pitch system that is not twelve-tone equal temperament now reaches the instrument, by the highest
tier it supports, or is reported as impossible. **Nothing is silently quantised.** The Plugin Auditor
reports tuning, MPE and expression capability; MIDI Builder writes the chosen tier and declares its
bend range.

### Testing and tooling

`research/BENCHMARK_DIVERSITY.md` adds twenty torture tests, three batch-diversity tests that detect
architecture collapse across unrelated briefs, and four neutrality and mode tests.

`tools/` gains `manifest_check`, `link_check`, `skill_lint`, `schema_check`, `routing_check` and
`check_all`, run by a GitHub Action on push. They use the Python standard library; PyYAML adds one
extra check when it is installed.

### Migration

- `track_state.evidence.wavread_findings` is now `evidence.analyzer_findings`. **Readers accept
  both.** WavRead remains the recommended analyzer, named in the user's profile rather than in a
  shared schema.
- User profiles go to 1.1, additively. A 1.0 profile stays valid. New optional keys cover project
  state, the diversity ledger, interaction mode, expertise, explanation depth and realism default.
- `composer`'s `midi_spec.humanization_notes` is replaced by a performance handoff.
- Existing track states, calibration profiles and artifacts keep working.

### Also

Duplicated sections removed from the quality gate, the generalization rules and the critics. System,
realism and project neutrality added. The listener model gains a **panel** that returns disagreements
rather than averaging them, and a groove model that no longer assumes a backbeat. Product-specific
claims moved out of tool-neutral skills into adapters and installation notes.

## 1.0 — 2026-09-14

First public release.

- **Music Director** and eleven specialists: Composer, Arranger, Producer, Lyric Generator, Mix
  Engineer, Reference Analyst, Music Critics, Listener Model, MIDI Builder, Plugin Auditor and
  Music Research.
- **Production with verification:** an instrument audit before production, an optional
  calibration pass that runs only with the user's consent, and a check of every track and every
  note after each export, with a release gate.
- **Melody-variety and cross-song lyric checks**, so songs do not share one rhythm, form or
  vocabulary.
- **Deliverable modes**, including instrumental exports.
- **User profiles** keep paths, tools, preferences and private terms out of the skills;
  `tools/privacy_check.py` checks a folder before it is published.
- **File naming system** for every artifact the studio writes.
- **Free instruments reference**, with how an agent can drive each one.
- **DAW adapters** for Ableton Live, FL Studio and Pro Tools, written to a shared contract.
- **Research** behind the skills, in `research/`, with a general-purpose benchmark.
- MIT license.
