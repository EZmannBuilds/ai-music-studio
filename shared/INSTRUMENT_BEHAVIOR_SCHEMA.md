# Instrument Behaviour Schema
## Version 1.0

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
CC1 and its legato lags 120 ms" belongs in a calibration profile, because the next user has a
different library.

---

# 1. `instrument_behavior`

```yaml
instrument_behavior:
  family:                      # strings, brass, woodwinds, keys, plucked, percussion, voice, ...
  instrument:
  evidence: {}                 # per section: see section 3

  acoustic_identity:           # what makes it recognisable in one or two sentences
  spectral_character:          # where its energy sits, and how that changes with dynamic
  attack:                      # how a note starts, and what changes the start
  sustain:                     # whether it sustains at all, and what sustains it
  release:                     # how a note ends, and whether the ending is audible
  natural_dynamic_behavior:    # what gets louder, and what else changes when it does

  practical_range: {low:, high:}
  strongest_registers: []
  weak_registers: []           # where it is thin, covered, unstable or hard to control

  articulations: []            # the real ones, named as players name them
  transitions_between_notes:   # slurred, tongued, bowed, picked, hammered, breathed
  legato_behavior:             # what a real legato actually is on this instrument
  repeated_note_behavior:      # what happens when the same note comes twice quickly
  vibrato:                     # kind, who controls it, whether it is constant
  pitch_instability:           # where pitch is not fixed, and why
  resonance:                   # sympathetic, body, room, pedal
  noise_components: []         # breath, fret, bow, pick, key, mechanism, air

  physical_constraints:        # limbs, fingers, breath, reach, one-note-per-string, pedals
  phrase_behavior:             # what bounds a phrase
  idiomatic_patterns: []       # what falls under the hand
  nonidiomatic_but_possible: []# hard but real, and what it costs the player
  ensemble_behavior:           # solo versus section; blend; divisi; who doubles whom
  recording_behavior:          # how it is normally captured, and what that does to the sound
```

---

# 2. `virtual_instrument_programming`

```yaml
virtual_instrument_programming:
  instrument_family:
  evidence: {}

  velocity_behavior:           # what velocity selects: level, timbre, articulation, or transition
  round_robins:                # whether they exist, and the rule against resetting them per bar
  dynamic_layers:              # how many, and whether they crossfade or switch
  cc_dynamics:                 # which continuous control carries dynamics, when one does
  expression:                  # the trim control, and why it is not the same as dynamics
  keyswitches:                 # how articulations are selected; keyswitch notes are non-sounding
  legato_patch_behavior:       # monophonic? overlap required? transition latency?
  release_samples:             # what is lost when notes are glued end to end
  pedal:
  breath_noise:
  fret_noise:
  bow_change:
  pick_noise:
  sympathetic_resonance:
  mic_positions:               # what they change, and what they cost in load and width
  room:
  stereo_width:                # including whether the patch is wide by design
  humanization:                # what belongs here, per shared/HUMAN_PERFORMANCE_SCHEMA.md
  common_fake_sounding_errors: []
  organic_programming_strategies: []
```

---

# 3. Evidence labels

Every section of every guide file carries one, because the guide was written with several primary
sources unreachable (`research/INSTRUMENT_BEHAVIOR.md`).

| Label | Means |
|---|---|
| `manual-derived` | stated in a manufacturer manual that was read |
| `excerpt-derived` | from an excerpt of a named source, not the full text |
| `orchestration-text` | attributed to a standard reference that was not opened |
| `musicianship` | general practice, stated as inference |
| `measured` | from a calibration render on the user's own system |
| `to-verify` | named explicitly, with what should be opened to confirm it |

Only `measured` may be reported as MEASURED under `shared/RESEARCH_RULES.md`. A number in the guide
is a **typical range**, not a fact about the user's instrument. The calibration profile is where facts
about the user's instrument live.

---

# 4. Who reads this

| Specialist | Uses it for |
|---|---|
| Performance Director | articulation, phrase limits, feasibility, what organic means here |
| Producer | character, register, ensemble behaviour, recording behaviour |
| Composer | practical range, idiom, what falls under the hand |
| Vocal Director | the voice and choir files |
| MIDI Builder | overlap, velocity meaning, keyswitches, release handling |
| Plugin Auditor | what to look for in a patch, and what to ask a calibration pass to measure |
| Music Critics | whether a part is playable, and whether "fake" is a real finding |

---

# 5. Rules for writing a guide file

1. **Behaviour before programming.** A file that opens with controller numbers has skipped the point.
2. **No vendor lists.** Products belong in `shared/FREE_INSTRUMENTS.md` and the plugin audit.
3. **Ranges, not constants**, and a label saying where the range came from.
4. **Name what you do not know.** A `to-verify` line is more useful than a confident invention.
5. **Culturally specific instruments get a research protocol, not a summary.** See
   `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md`, and
   `shared/MUSICAL_SYSTEMS/INDEX.md` for why.
6. **Every file links to `COMMON_ERRORS.md`**, which holds the cross-family failure list once rather
   than repeating it thirteen times.
