# Instrument Behaviour Schema
## Version 1.1

The structure behind every file in `shared/VIRTUAL_INSTRUMENT_GUIDE/`.

Two records. The first describes a real instrument. The second describes what a sampled or modelled
version of it needs from the notes.

```text
instrument_behavior                what the instrument is        general, portable, in the guide
virtual_instrument_programming     how to write for a virtual one  general, portable, in the guide
plugin_audit.instruments[]         what is installed here          per machine, per edition
calibration_profile                what it measured                per patch, per version
```

The line matters. "A horn player breathes" belongs in the guide. "This library's dynamics arrive on
a particular controller and its legato lags a particular number of milliseconds" belongs in a
calibration profile, because the next user has a different library. **Human limits belong in the
guide, not in calibration.** How long an oboist can hold a phrase, how fast a marimbist rolls or how
far a pianist's hand spans is a fact about players; a calibration render measures a patch and cannot
measure a player.

---

# 1. `instrument_behavior`

```yaml
instrument_behavior:
  family:                      # strings, brass, woodwinds, keys, plucked, percussion, voice, ...
  instrument:
  traditions: []               # for a tradition-specific instrument; see section 5, rule 5

  physical_sound_source:       # what vibrates, what excites it, what shapes it
  attack_behavior:             # how a note starts, and what changes the start
  sustain_behavior:            # whether it sustains at all, and what sustains it
  release_behavior:            # how a note ends, and whether the ending is audible
  dynamic_timbre_change:       # what else changes when it gets louder or softer
  register_character:          # where it is strong, thin, covered, unstable or hard to control
  practical_range:             # written and sounding, for a transposing instrument
  tessitura:                   # where it lives comfortably for long stretches
  articulation_logic:          # the real articulations, named as players name them, and why they differ
  phrase_limits:               # what bounds a phrase: breath, bow length, endurance, hand position
  transitions:                 # slurred, tongued, bowed, picked, hammered: what a real legato is here
  repeated_note_behavior:      # what happens when the same note comes twice quickly
  vibrato:                     # kind, who controls it, whether it is constant, and by style
  pitch_instability:           # where pitch is not fixed, and why
  resonance:                   # sympathetic, body, room, pedal
  physical_noise:              # breath, fret, bow, pick, key, mechanism, air
  feasibility:                 # limbs, fingers, reach, one note per string, pedals: what cannot be played
  ensemble_behavior:           # solo versus section; blend; divisi; who doubles whom
  recording_behavior:          # how it is normally captured, and what that does to the sound
```

---

# 2. `virtual_instrument_programming`

```yaml
virtual_instrument_programming:
  instrument_family:

  note_length:                 # how written length relates to the sound, and what cuts a note short
  overlap:                     # when notes must overlap (monophonic legato) and when they must not
  velocity:                    # what velocity selects: level, timbre, articulation, or transition
  continuous_dynamics:         # whether a continuous control carries dynamics, and what it crossfades
  expression:                  # the trim control, and why it is not the same as dynamics
  articulation_switching:      # how articulations are selected; switching notes are non-sounding
  round_robins:                # whether they exist, and the rule against resetting them per bar
  release_samples:             # what is lost when notes are glued end to end
  pedal_or_breath_behavior:    # sustain pedal, breath noise, bow change, fret and pick noise
  transition_samples:          # recorded legato, portamento, slides, and what triggers them
  mic_or_room_behavior:        # what the recorded positions and room change, including width
  likely_fake_sounding_errors: []
  organic_programming_methods: []   # each one names its cause, per shared/HUMAN_PERFORMANCE_SCHEMA.md
```

**Field names changed in 1.1**, and the old ones are still read:

| 1.0 field | 1.1 field |
|---|---|
| `acoustic_identity`, `spectral_character` | `physical_sound_source`, `dynamic_timbre_change` |
| `attack`, `sustain`, `release` | `attack_behavior`, `sustain_behavior`, `release_behavior` |
| `natural_dynamic_behavior` | `dynamic_timbre_change` |
| `strongest_registers`, `weak_registers` | `register_character` |
| `articulations` | `articulation_logic` |
| `transitions_between_notes`, `legato_behavior` | `transitions` |
| `noise_components` | `physical_noise` |
| `physical_constraints`, `nonidiomatic_but_possible` | `feasibility` |
| `phrase_behavior` | `phrase_limits` |
| `velocity_behavior`, `dynamic_layers` | `velocity` |
| `cc_dynamics` | `continuous_dynamics` |
| `keyswitches` | `articulation_switching` |
| `legato_patch_behavior` | `overlap`, `transition_samples` |
| `pedal`, `breath_noise`, `fret_noise`, `bow_change`, `pick_noise` | `pedal_or_breath_behavior` |
| `mic_positions`, `room`, `stereo_width` | `mic_or_room_behavior` |
| `common_fake_sounding_errors` | `likely_fake_sounding_errors` |
| `organic_programming_strategies`, `humanization` | `organic_programming_methods` |

`idiomatic_patterns` and `sympathetic_resonance` are carried in the guide's prose, and in
`resonance` and `feasibility`.

---

# 3. How the records appear on a guide page

Each instrument, or each sub-instrument that behaves differently, gets a **behaviour card**: two
Markdown tables under a `### <instrument>` heading inside `## Behaviour cards`. The first table's
header is `| instrument_behavior | behaviour | evidence |`; the second's is
`| virtual_programming | behaviour | evidence |`. Every field in sections 1 and 2 (apart from
`family`, `instrument`, `traditions` and `instrument_family`) is a row, and **no row is ever
deleted**. A field nobody could fill says `unresolved: <what is unknown>` in the behaviour column and
`to-verify: <what would settle it>` in the evidence column. An empty scaffold is an unanswered
question, not permission to invent.

The evidence column holds one label, then `: ` and source IDs separated by `; `. The prose sections
that follow explain the cards and carry the same labels as tags. `tools/evidence_check.py` checks
that every card has every row, that every label is one of the labels below, and that every source ID
is in the register at a read depth the label allows.

---

# 4. Evidence labels

The labels, their meaning and their mapping to MEASURED / RESEARCH-SUPPORTED / CREATIVE INFERENCE
are defined once, in `shared/RESEARCH_RULES.md`: `sourced`, `academic`, `manual-derived`,
`standard-reference`, `measured`, `inference`, `to-verify`. The evidence behind each claim, and
its limits, is recorded in `research/instruments/<FAMILY>.md`, and every source, with how much of
it was read, in `research/sources/INSTRUMENT_SOURCES.md`.

Only `measured` may be reported as MEASURED, and `measured` never appears in the guide: a number in
the guide is a typical range from a source, not a fact about the user's instrument. The calibration
profile is where facts about the user's instrument live.

The 2.0 labels are still read: `musicianship` as `inference`, `orchestration-text` and
`excerpt-derived` as `standard-reference`.

---

# 5. Who reads this

| Specialist | Uses it for |
|---|---|
| Performance Director | articulation, phrase limits, feasibility, what organic means here |
| Producer | character, register, ensemble behaviour, recording behaviour |
| Composer | practical range, idiom, what falls under the hand |
| Vocal Director | the voice and choir files |
| MIDI Builder | overlap, velocity meaning, articulation switching, release handling |
| Plugin Auditor | what to look for in a patch, and what a calibration pass can and cannot measure |
| Music Critics | whether a part is playable, and whether "fake" is a real finding |

---

# 6. Rules for writing a guide file

1. **Behaviour before programming.** A file that opens with controller numbers has skipped the point.
2. **No vendor lists and no product names.** Products belong in `shared/FREE_INSTRUMENTS.md`, the
   plugin audit and the research pages. No controller numbers, velocity zones or product latencies
   in the guide: those are calibration facts.
3. **Ranges, not constants**, with a label saying where the range came from. A transposing
   instrument's range says whether it is written or sounding.
4. **Name what you do not know.** A `to-verify` line is more useful than a confident invention.
5. **A tradition-specific instrument gets a page only when it passes the source gate** in
   `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md`: at least two independent
   specialist sources read at section depth, one of them from practitioners, teachers, an
   institution of the tradition or fieldwork. Such a page names its tradition precisely, links its
   `shared/MUSICAL_SYSTEMS/` file for context instead of repeating it, and says what must not be
   generalised outside the tradition. Without the sources it gets the protocol, not a page.
6. **Every file links to `COMMON_ERRORS.md`**, which holds the cross-family failure list once.
