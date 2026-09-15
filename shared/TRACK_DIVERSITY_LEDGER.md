# Track Diversity Ledger
## Version 1.0

One row per song, describing its **shape** rather than its content, so that the studio can notice when
many songs share an architecture.

This generalises two checks that already exist: the Composer's melody-variety gate and the Lyric
Generator's cross-song uniqueness report. Those stay where they are and feed rows into this ledger.

```text
Composer, Arranger, Producer,        each fill the fields they decided
Vocal Director, Lyric Generator,
Performance Director
        ↓
Music Director                       assembles the row and writes it, once, at the end of the task
        ↓
track_dna row in the ledger
        ↓
Music Director, Creative Lab,        read it before the next song
Project Guide, Music Critics
```

**The Director assembles and writes the row.** Each specialist fills the fields for decisions it
actually made, and hands them over in its handoff. A row that six specialists were each supposed to
write is a row nobody writes, so the assembly is one job with one owner.

Fields nobody decided are left empty. An empty field means the decision was not made here, which is
information, and is different from a field set to a default.

---

# 1. The rule

**The ledger never forces diversity. It asks a question.**

Deliberate repetition is a real artistic strategy. A project identity, a genre convention and an album
callback all look like sameness in a table. The ledger's job is to make the pattern visible so the
user can say which it is.

```text
ACCIDENTAL REPETITION     nobody chose it; it is the generator's default showing through
PROJECT MOTIF             chosen, and part of what this project is
GENRE CONVENTION          the style requires it, and breaking it would be the error
DELIBERATE CALLBACK       a specific reference to a specific earlier track
```

Only the first is a problem. The Director asks; it does not rewrite.

---

# 2. Where it lives

The file is at the user's `paths.diversity_ledger`, or by default beside `paths.output_root`. With
`preferences.diversity_ledger: off` in the profile, nothing is written and the comparison is skipped,
which is a legitimate choice for someone who does not want their earlier work consulted.

With no earlier songs, the row is written and the comparison is skipped with a line saying so.

---

# 3. `track_dna`

One row per song. Populate what the task produced; an empty field is "not decided here", not zero.

```yaml
track_dna:
  song:
  project:                     # the project this belongs to, if any
  written:                     # date and time

  tempo_family:                # e.g. slow 60-80, mid 90-110, up 120-140, fast 140+, free
  meter:                       # including the grouping, e.g. "9/8 = 2+2+2+3"
  pitch_system:                # 12-TET major/minor, modal, maqam, raga, EDO-n, JI, atonal, none
  tonal_center_strategy:       # fixed, shifting, ambiguous, drone, none
  harmonic_mechanism:          # functional, modal vamp, chromatic mediant, pedal, planing,
                               # loop, nonfunctional, static, absent
  harmonic_rhythm:             # chords per bar or per section, or "none"
  bass_role:                   # root support, counterline, riff, pedal, groove engine, sub anchor,
                               # melodic, absent
  groove_family:               # straight, swung, shuffled, clave-oriented, polymetric, free, none
  subdivision:                 # 8ths, 16ths, triplets, mixed, non-isochronous
  form:                        # verse/chorus, strophic, through-composed, loop evolution, AABA,
                               # suite, cue, state machine, free
  section_lengths:             # e.g. "8/8/16", or "unequal"
  hook_type:                   # vocal, melodic, rhythmic, bass, harmonic, timbral, compound, none
  lead_source:                 # voice, instrument named by family, sample, texture, none
  lift_mechanism:              # how the piece's high point is reached, where it has one:
                               # register, density, width, harmony, rhythm, subtraction,
                               # vocal stack, accumulation, none.
                               # "no high point" is a real answer and a common one: a drone,
                               # a process piece and a six-hour installation may have none.
                               # Named for the mechanism, not for a chorus, because most
                               # music does not have a chorus.
  arrangement_curve:           # rising, arch, terraced, flat, descending, episodic
  production_density:          # sparse, moderate, dense, maximal
  texture_family:              # acoustic, electronic, hybrid, orchestral, band, processed, noise
  transition_grammar: []       # the devices actually used between sections
  vocal_architecture:          # from shared/VOCAL_ARCHITECTURE_SCHEMA.md section 3
  outro_behavior:              # hard stop, fade, vamp, collapse, return, new material, unresolved
  dynamic_shape:               # the loudness and energy contour in words
  performer_character:       # from performance_state.performer_character
  unusual_constraint:          # what this song was not allowed to do, if anything

  melody_variety_report: {}    # composer/SKILL.md
  lyric_uniqueness_report: {}  # lyric-generator/SKILL.md
```

---

# 4. The comparison, before a new track

Run against recent rows, by default the last five in the same project, or the last five overall when
there is no project.

```yaml
diversity_comparison:
  rows_compared: []
  shared_dimensions: []        # dimensions where 3 or more of the compared rows agree
  distinct_dimensions: []
  classification: {}           # per shared dimension: accidental | motif | convention | callback
  unclassified: []             # shared dimensions nobody has explained yet
  question_for_user:           # asked only when something is unclassified
  status: clear | ask
```

Default flag: **three or more of the last five rows agreeing on the same dimension**, where that
dimension is not already recorded as a project motif or a genre convention. This is CREATIVE INFERENCE
and the brief or the user may change it.

The question is asked once, in plain terms, naming what is shared:

> Five recent songs are all mid-tempo 4/4, verse/pre/chorus, sub-bass anchored, with the chorus lifted
> by width, a breakdown bridge and a doubled final chorus. Is that this project's identity, or is it
> the shape everything is coming out in?

Then the answer is recorded in `classification`, and the same question is not asked again for those
dimensions.

---

# 5. What happens with the answer

| Answer | What the studio does |
|---|---|
| project motif | records it; stops flagging it; protects it in later songs |
| genre convention | records it with the genre; stops flagging it |
| deliberate callback | records which track it refers to |
| accidental | routes to Creative Lab for candidates that break *those specific dimensions* |

Routing to the Creative Lab is the useful case: the Lab is told which dimensions are stale, so its
candidates differ where it matters rather than differing at random
(`shared/CREATIVE_EXPLORATION_SCHEMA.md`).

---

# 6. Batch diversity

For a run of songs planned together, or for testing the studio itself
(`research/BENCHMARK_DIVERSITY.md`), compare a whole set at once.

```yaml
batch_diversity:
  briefs_compared:
  per_dimension_distinct_values: {}   # dimension -> how many different values appeared
  collapsed_dimensions: []            # dimensions where nearly every brief produced one value
  architecture_collapse: true | false
  note:
```

**Architecture collapse** is when unrelated briefs produce one shape. It is a defect in the studio, not
in any one song, and it is what the batch tests exist to catch.

---

# 7. What the ledger does not do

- It does not score songs. There is no diversity number and no target.
- It does not compare quality, lyrics or melodies as content. The existing gates do that.
- It does not act. It reports, and the Director asks.
- It does not cross projects unless asked. Two projects are allowed to sound different from each other
  and consistent within themselves.
- It does not override the user. "I want every song on this record to share that shape" ends the
  matter, and is recorded as a project motif.
