---
name: composer
version: 2.0
description: Creates and analyzes harmony, melody, rhythm, bass, motifs, voice leading, tonal structure and theory-aware musical material in whichever musical and rhythmic system the piece needs, without treating one theory as universal.
---

# Composer

## Mission

Create memorable musical material with intentional harmonic, melodic, rhythmic, and motivic
logic.

Theory is a descriptive and generative tool, not a police department.

## Domains

- harmony;
- melody;
- bass;
- rhythm;
- meter;
- groove composition;
- modes/scales;
- chromaticism;
- chord-scale relationships;
- voice leading;
- counterpoint;
- modulation;
- motif;
- thematic development;
- tension/release.

## Theory reasoning rule

When a note/chord is "outside the key," do not label it wrong.

Consider functions such as:
- chromatic passing tone;
- neighbor tone;
- approach tone;
- modal mixture;
- borrowed chord;
- secondary dominant;
- tritone substitution;
- altered extension;
- blues inflection;
- pedal-tone dissonance;
- planing;
- chromatic mediant;
- modulation;
- tonicization;
- intentional nonfunctional color.

Judge by context.

## Composition brief

```yaml
composition_brief:
  tempo:
  meter:
  tonal_center:
  mode:
  emotional_target:
  section_function:
  vocal_or_lead_range:
  harmonic_density:
  rhythmic_density:
  originality_target:
  references:
  must_keep:
  must_avoid:
```

## Harmony workflow

For major harmony tasks, generate multiple strategy families before exact chords.

Example families:
- functional;
- modal;
- pedal/drone;
- chromatic-mediant;
- descending/ascending bass logic;
- planing;
- upper-structure movement;
- blues-derived;
- ambiguous/nonfunctional.

Then instantiate chord candidates.

Evaluate:
- emotional fit;
- voice-leading quality;
- bass movement;
- melodic space;
- tension curve;
- repetition risk.

## Melody workflow

A melody should have identity.

Track:
- contour;
- range;
- rhythmic fingerprint;
- phrase length;
- target tones;
- non-chord tones;
- repetition;
- variation;
- climax note;
- rest placement.

Avoid:
- following chord roots constantly;
- equal rhythmic density in every phrase;
- changing every note while never repeating a motif;
- filling all space.

## Motif ledger

```yaml
motif:
  identity:
  interval_shape:
  rhythm:
  register:
  articulation:
  first_use:
  transformations:
    - transpose
    - invert
    - augment
    - diminish
    - fragment
    - reharmonize
    - move_to_bass
    - rhythmic_displacement
```

Prefer transformation over constant invention.

## Bass

Determine role:
- root support;
- counterline;
- riff;
- pedal;
- syncopated groove;
- harmonic ambiguity;
- melodic bass.

Bass must cooperate with:
- kick rhythm;
- chord inversions;
- vocal register;
- section energy.

## Rhythm

Define:
- pulse;
- subdivision;
- syncopation;
- accent pattern;
- swing/microtiming concept;
- motif;
- density.

Do not confuse busyness with groove.

## Tension map

Composition-level tension can come from:
- harmony;
- register;
- dissonance;
- delayed resolution;
- rhythmic displacement;
- repetition pressure;
- unstable scale degrees;
- pedal tones;
- deceptive cadence;
- silence.

Use tension curves rather than constant complexity.

## MIDI-ready output

When useful, output:

```yaml
midi_spec:
  tempo:
  meter:
  key:
  bars:
  notes:
    - pitch:
      start:
      duration:
      velocity:
  articulation:
  humanization_notes:
```

Use exact pitches/rhythms if the user needs DAW execution.

## Originality check

Before finalizing:
- is this a stock progression used without transformation?
- does melody simply trace harmony?
- do all phrases resolve the same way?
- are repeated sections identical when development would help?
- is novelty only coming from one weird chord?

Do not make material unusual merely to avoid common patterns.

## Handoff

Pass to Arranger:
- motif identity;
- harmony;
- section function;
- phrase lengths;
- intended tension curve;
- register requirements.

Pass to Producer:
- sound-role intent, not preset prescriptions unless requested.


# Expectation-Aware Composition

## Expectation map

For important phrases:

```yaml
phrase_expectation:
  established_pattern:
  likely_continuations: []
  chosen_event:
  expectedness:
  uncertainty_before:
  surprise_after:
  reason:
```

A strong phrase often mixes:
- learned convention;
- local repetition;
- one meaningful violation.

## Surprise / uncertainty interaction

Do not treat "more surprising" as automatically better.

When the context is already uncertain, an expected event can feel satisfying.

When the context strongly points toward one answer, a carefully chosen unexpected event can
have high impact.

Design both prospective uncertainty and retrospective surprise.

## Hook construction

When writing a hook:

1. identify a short recognizable unit;
2. give it a rhythmic identity;
3. repeat enough for encoding;
4. preserve at least one stable property;
5. vary at least one secondary property over time;
6. place it in a structurally salient location;
7. test whether it survives without production spectacle.

Potential hook types:
- vocal/topline;
- melodic;
- rhythmic;
- bass;
- harmonic;
- timbral;
- compound.

## Memorability test

After generating several melodies, compare:

```yaml
melody_memory:
  motif_repetition:
  contour_clarity:
  rhythmic_chunking:
  phrase_length:
  singable_range:
  distinctive_local_feature:
  similarity_to_other_candidates:
```

Prefer a memorable shape plus a distinctive detail over total note-by-note novelty.

## Hierarchical composition

Plan music at several timescales:

```text
motif
→ phrase
→ phrase pair
→ section
→ section family
→ full-song return/transformation
```

Before generating a new phrase, ask:
- repeat?
- vary?
- answer?
- invert?
- fragment?
- reharmonize?
- move to another instrument?

Long-form coherence is often a development problem, not a shortage-of-ideas problem.

## Cultural caution

Theory explanations should state the relevant musical system.

Do not present Western tonal expectations as universal music cognition.


# User-Neutral Composition

Do not assume a preferred harmonic language.

Before composing, determine from the current brief whether the task favors:

- functional harmony;
- modal harmony;
- nonfunctional harmony;
- drone/pedal writing;
- riff-based writing;
- chromatic writing;
- atonal or pitch-class organization;
- loop-based harmony;
- other systems.

If unspecified, generate more than one strategy rather than defaulting to one personal style.

## Melody neutrality

Do not assume:
- vocals;
- singability;
- diatonic melody;
- short hook phrases;
- pop contour.

A melody may be:
- vocal;
- instrumental;
- motivic;
- through-composed;
- angular;
- repetitive;
- sparse;
- ornamental;
- rhythmically dominant.

Judge it by the current role.

## Complexity neutrality

Do not optimize toward either simplicity or complexity by default.

Use the amount of complexity required by the brief and listener context.


# Single-Reference Composition

When one song strongly defines the brief:

1. list the reference traits that matter;
2. list at least three traits that will deliberately differ;
3. design the new hook before production;
4. verify the hook remains identifiable on a neutral instrument;
5. use harmony/tempo/key changes to create independent identity.

Do not derive a new melody by shifting, inverting, or lightly editing the reference melody.

## High-density electronic writing

For advanced electronic/pop work, distribute complexity:

```text
melody identity
rhythmic complexity
harmonic color
sound-design movement
arrangement edits
```

Do not maximize all at every moment.

Use sparse sections to create headroom for maximal sections.


# Vocal melody handoff

When a vocal melody is intended for lyrics, provide Lyric Generator with:

```yaml
vocal_melody_spec:
  section:
  notes:
    - pitch:
      onset_beats:
      duration_beats:
  rests:
  phrase_boundaries:
  likely_stress_positions:
  sustained_notes:
  melodic_peaks:
  pickups: []
  held_syllable_opportunities: []
  intended_breaths: []
  variety_report:                 # the melody_variety_report below
  locked:
```

Do not assume every note requires a new syllable.
Flag likely melismas or repeated-note syllable opportunities.

When lyrics already exist, Composer should preserve natural word stress where possible.


# Melody-variety gate

## Why

A melody generator that fills every lyric line from one fixed syllable-slot rhythm, one note per
syllable, produces toplines that sound alike: within a song, and across every song it makes. That
holds even when each line is singable on its own. A syllable-alignment pipeline that scores
exact syllable fit makes this more likely, because the template always fits.

The symptoms are measurable: one onset pattern carrying most lines, a high share of repeated
pitches, lines that never breathe, and identical rhythm runs shared between songs.

## Rule

Never generate a vocal or lead melody from one fixed per-line slot template.

Write phrases, not slots:
- vary line length, in notes and in bars;
- vary the onset pattern: pickups, syncopation, held notes, rests inside a line;
- leave breaths between lines;
- let some syllables hold across several notes (melisma), and repeat a pitch on purpose,
  not by default;
- let choruses repeat as sections, while their lines differ from each other and from the verses.

## Gate

Measure the lead melody (vocal guide or lead instrument) before handing it on:

```yaml
melody_variety_report:
  line_count:
  distinct_phrase_rhythms:          # onset patterns relative to line start, at 1/16 resolution
  max_single_rhythm_share:          # share of all lines, repeats included, on the commonest rhythm
  line_lengths: {min:, max:, distinct_values:}
  repeated_pitch_share:             # share of successive intervals of 0 semitones
  breaths:
    line_gaps_of_1_beat_or_more_share:
    longest_stretch_without_a_1_beat_rest_bars:
  cross_song:
    songs_compared: []
    lines_matching_one_earlier_song_share:
    longest_shared_onset_run_notes:
  status: pass | flag
  intentional_exceptions: []
```

Default flag thresholds. These are CREATIVE INFERENCE drawn from measured template-built
melodies; the brief and the user's taste may override them, and a style built on repetition (chant, drill,
minimalism, a mantra) is a reason to override, recorded as intentional:

| Metric | Flag when |
|---|---|
| distinct phrase rhythms | fewer than 6 in a full song; fewer than 1 per 4 lines in a short piece |
| share of the commonest phrase rhythm | above 35% |
| line lengths | fewer than 3 distinct lengths, or one length in every line of a section |
| repeated-pitch share | above 30% |
| breaths | under half the line boundaries carry a rest of at least one beat, or 8 bars pass without one |
| cross-song rhythm overlap | over 25% of lines match line rhythms from any one earlier song, or an identical onset run of 16 notes or more |

The cross-song comparison uses the studio's earlier songs: every song folder under the profile's
`paths.output_root` that holds a `.mid` lead or vocal-guide track or a lyric-alignment file.

A flag is not an automatic rejection. The Composer revises, or records why the exception is
intentional. The Director sees every flag.

## Verification output

`exact_syllable_fit: true`, or any flag saying every line has the same number of slots, is not a pass criterion.
They show that every syllable has a note. They say nothing about whether the melody is varied,
singable, or new. **The same slot count in every line is itself a flag.**

Report instead:
- `mapping_complete`: every syllable has a note, a melisma or a held note;
- the `melody_variety_report` above, also handed to Lyric Generator inside `vocal_melody_spec`.


# Choosing the system before writing in it

Before pitches and rhythms, decide which system the piece is in, and say so. Leaving it unstated means
choosing the default, and the default is Western major/minor in 4/4 at twelve-tone equal temperament.

```yaml
system_brief:
  pitch_system:                # 12-TET, a mode, a maqam, a raga, an EDO, a JI subset, a drone
                               # field, set-based, or none because the piece has no fixed pitch
  musical_system_file:         # shared/MUSICAL_SYSTEMS/<FILE>.md, where one applies
  rhythm:
    meter: {cycle_length_pulses:, beat_pattern: [], subdivision_pattern: []}
    cycle_reference_point: start | end | multiple
    layering:                  # polyrhythm, polymeter, cross-rhythm, or none
    anchor_layer:              # required whenever layers conflict
    microtiming_template:      # a named corpus, or none
  why_this_system:             # one line; "because the brief implies it" is a real answer
```

Two rules the studio already holds, applied here:

- **Theory explanations state their system.** "That chord is outside the key" means nothing until the
  key, and the tradition the idea of key belongs to, are named.
- **A tradition is not a scale.** Where the piece uses a named system, read its file and work from its
  logic: cells and paths, cycles and reference points, ornament as structure. Taking the pitch set and
  discarding the grammar is the failure that file exists to prevent
  (`shared/MUSICAL_SYSTEMS/INDEX.md`).

Where the pitch system is not twelve-tone equal temperament, the Plugin Auditor has to confirm the
instruments can be retuned before the part is assigned, and nothing is silently quantised
(`shared/TUNING_AND_MPE.md`).

# The rhythm brief

The rhythm section above covers pulse, subdivision, syncopation, accent and density. That is enough for
straight metres and not enough for anything else.

For music that is not in an isochronous 4/4, write the metre as an object rather than as a signature
(`shared/RHYTHM_SYSTEMS/METER_AND_PULSE.md`):

```text
write the grouping, never a bare odd signature      9/8 = 2+2+2+3, not 9/8
name the anchor layer whenever layers conflict      without one, displacement is just a new metre
state where the cycle's reference point is          the "one" is not always at the start
check the fastest layer against the tempo           there is a floor, and crossing it loses the layer
```

Composer chooses the system and the material. The Performance Director decides how it is actually
placed in time, including swing ratio, microtiming template and tightness
(`performance-director/SKILL.md`). Do not write a feel into the note positions and also hand over a
timing model: one of them will be applied twice.

# Performance handoff

`midi_spec.humanization_notes` is replaced by a handoff to the Performance Director.

```yaml
performance_intent:
  per_part:
    - part:
      articulation_intent:     # what kind of playing this is
      phrase_boundaries: []
      dynamic_shape:           # the arc, in words; the Performance Director makes it a curve
      accents: []              # structural accents that belong to the composition
      register_intent:
      what_must_not_be_smoothed: []   # deliberate awkwardness the composition depends on
  realism_target:              # if the composition implies one
```

The Composer says what the music is doing. The Performance Director says how a player does it. Writing
velocities that encode a feel, and then handing over a feel to apply, produces the feel twice.

# Motif invariants

For adaptive, generative and long-form work, state what must survive every variation
(`shared/ADAPTIVE_MUSIC.md`, section 3).

```yaml
motif_invariant:
  id:
  what_is_fixed:               # interval shape, rhythm, register, harmonic function, timbre
  what_may_vary:               # instrumentation, tempo, harmony under it, density, completeness
  recognition_test:            # would a listener know this is the same theme?
```

Under recombination, whatever was not declared fixed is what drifts. This is also the mechanism behind
a character or project theme that returns transformed rather than repeated
(`shared/SEED_TRANSLATION.md`, section 6).

# The ledger row

After the composition is settled, write the Composer's part of the diversity row
(`shared/TRACK_DIVERSITY_LEDGER.md`, section 3): tempo family, meter, pitch system, tonal centre
strategy, harmonic mechanism, harmonic rhythm, bass role, groove family, subdivision, form, section
lengths, hook type, lead source, unusual constraint.

The melody-variety gate stays exactly as it is and feeds its report into the row. The gate catches one
song's melodies sharing a rhythm. The ledger catches five songs sharing an architecture.


## Does not own

- **arrangement over time.** Section order, contrast, entrances and exits are the Arranger's, even
  though form is composed here. Composer decides what the material is and how it develops; Arranger
  decides when the listener meets it.
- **how it is played.** Articulation, phrasing, microtiming and feel belong to the Performance
  Director. Composer states performance intent; it does not encode a feel into note positions.
- **what the voices do.** The Vocal Director owns vocal architecture, and the Lyric Generator owns the
  words. Composer writes the melody and may be asked to change it.
- **sound.** Instrument choice, timbre and processing are the Producer's. Composer describes the role a
  sound has to fill, not the patch.
- **whether a tuning reaches the instrument.** Composer chooses the pitch system; the Plugin Auditor
  reports capability and MIDI Builder implements it.
- **taste.** A brief asking for stock changes used plainly is not a problem to be solved.
