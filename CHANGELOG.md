# Changelog

## 2.0 — 2026-09-15

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
