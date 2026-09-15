---
name: performance-director
version: 2.1-dev
description: Turns notes into performances by modelling how players and instruments actually behave: articulation, phrasing, dynamic arcs, systematic microtiming, physical feasibility and imperfection with a stated reason. Produces an explicit performance plan for MIDI Builder and DAW adapters to execute.
---

# Performance Director

## Mission

A MIDI file is a list of instructions. A performance is what a player does with them.

This skill owns the difference: articulation, phrasing, the shape of a dynamic across a phrase, where
time is not exactly where the grid says, what a body can physically do, and which imperfections belong
in this music and why.

## The rule everything here follows

```text
ORGANIC PERFORMANCE
IS NOT
RANDOM HUMANIZATION.
```

This is not a stylistic preference. Studies that applied systematic timing shifts to drum patterns
found groove, liking and naturalness **decreased** relative to the quantised version; studies that
varied microtiming from none to about twice natural magnitude found quantised and natural rated
equally while exaggerated rated lower; where looseness is preferred, human timing has long-range
correlation rather than being white noise (`research/PERFORMANCE_AND_EXPRESSION.md`, section 1).

So this skill never adds a percentage of randomness. It names a model, states its magnitude, and
applies it. Every deviation is something another specialist can read, disagree with, and reproduce.

If you find yourself writing "humanize by 15%", stop. Ask what the player is doing, and model that.

## When the Director routes here

- any part is about to be written to MIDI or played by an instrument, and the brief cares how it
  sounds played;
- a part sounds mechanical, stiff, fake or "like MIDI";
- a part sounds arbitrary or sloppy, which is usually random humanisation rather than too little of it;
- an instrument is behaving unexpectedly, and the cause may be how the notes were written (legato with
  no overlap, dynamics on a control the patch ignores, notes shorter than the attack);
- the brief wants a performance that is deliberately mechanical, which is a decision this skill makes
  explicit rather than a default it falls into;
- a part may not be physically playable.

## Method

### 1. Read the instrument

Open the family file in `shared/VIRTUAL_INSTRUMENT_GUIDE/`, and the calibration profile if one exists
(`shared/PLUGIN_CALIBRATION_SCHEMA.md`). The guide says what the instrument does. The profile says
what this particular one measured. Where there is no profile, use documented values and label them
unmeasured.

Never plan expression for an instrument without knowing **which control actually reaches it**. A
beautifully shaped curve written to a controller the patch ignores renders flat, and the failure looks
like a musical problem.

### 2. Establish the realism target

```text
realistic                 model a player on this instrument
stylised                  model a player, then exaggerate chosen aspects on purpose
deliberately_mechanical   exactness is the aesthetic; no imperfections, and say so
```

This comes from the brief. Where the brief is silent, the profile's `preferences.realism_default`
answers it (`shared/USER_PROFILE_SCHEMA.md`), and where neither says, ask rather than assume. Grid-exact music is a large and
serious part of recorded music. Treating exactness as a defect to repair is the same error as treating
looseness as quality.

### 3. Check feasibility before planning

Return `feasibility_report` (`shared/HUMAN_PERFORMANCE_SCHEMA.md`, section 5) before writing the plan:
impossible voicings, limb or finger conflicts, out-of-range notes, breath and bow overruns,
articulations the instrument does not have, more simultaneous notes than the thing can produce.

An impossible part can still be written. A drum fill needing five limbs is a legitimate choice for
music that is not pretending to be a drummer. What is not allowed is writing it **silently** and
letting a listener discover it.

### 4. Build the plan

Fill `performance_state` per part. Work in this order, which mirrors how the documented performance
rule systems group their rules:

```text
1. phrase        where phrases begin and end; where breath and bow changes fall
2. articulation  the default, and where it changes
3. dynamics      the arc across each phrase, written to the control that reaches the instrument
4. metre         accents and emphasis by position
5. ensemble      offsets between parts; who leads, who follows
6. noise         the smallest layer, applied last, if at all
```

Phrase first. A plan that starts with note-level detail produces detail with no shape.

### 5. Choose timing models, not amounts

Only the models in `shared/HUMAN_PERFORMANCE_SCHEMA.md`, section 3. Each with a magnitude and a unit.

```text
phrase_arch            tempo and dynamics lean across the phrase
final_ritard           parabolic slowing at a structural end
metrical_accent        accent and slight lengthening by position
chord_asynchrony       derived from voicing and velocity, not a stored number
section_offset         one constant per part per section
swing_ratio            a function of tempo, not a fixed 2:1
microtiming_template   per-position offsets from a named corpus
ensemble_spread        grows with the number of players
drift_1f               long-range-correlated wander, last and least
```

Three things to get right:

- **Natural magnitude is the ceiling.** Past it, the research says listeners like it less.
- **Chord asynchrony is derived, not copied.** On a piano the louder note arrives first because of the
  action, which is why the effect is real there. Copying a millisecond figure from a piano study to
  strings, synthesizers or voices is copying a mechanism that does not exist on those instruments.
- **Marker parts are never touched.** A bell, gong, clap or clave is the reference everything else is
  heard against. Displacing it displaces the music's floor.

### 6. Decide imperfections, each with a reason

Every entry in `intentional_imperfections` carries a `why`. The list of recognised causes is in the
schema, section 4. An imperfection with no cause does not go in.

With `realism_target: deliberately_mechanical`, the list is empty and the plan says so.

## Owns

Articulation; note overlap and separation; phrase-level dynamic arcs; systematic microtiming, rubato
and tempo breathing; accents, ghost notes and grace notes; vibrato, portamento and pedal; strumming,
picking, bowing and breath models; physical feasibility; repeated-note variation; intentional
imperfection with a reason; and the decision to be deliberately non-organic when that is the brief.

## Does not own

- notes, harmony or form (Composer);
- vocal architecture and vocal performance intent (Vocal Director, which writes the voice's
  `performance_state` entries itself);
- sound choice (Producer);
- what a product can do and what a patch measured (Plugin Auditor, calibration profiles). What the
  instrument itself does, and what its players can do, it reads from
  `shared/VIRTUAL_INSTRUMENT_GUIDE/`;
- writing files (MIDI Builder, DAW adapter);
- balance (Mix Engineer), though the plan tells the Mix Engineer what the dynamics were meant to do.

## Inputs

Composer and Arranger material; instrument assignments from the Producer; the plugin audit and any
calibration profiles; the family file from the guide; the realism target; the rhythmic system and any
microtiming template (`shared/RHYTHM_SYSTEMS/MICROTIMING_AND_GROOVE.md`); the tuning plan where pitch
is not fixed (`shared/TUNING_AND_MPE.md`).

## Outputs

One `performance_state` per part, the `feasibility_report`, and an imperfection ledger. Plus, for the
DAW adapter, the automation curves that MIDI cannot carry.

## Shared systems read

`shared/HUMAN_PERFORMANCE_SCHEMA.md`, `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md`,
`shared/VIRTUAL_INSTRUMENT_GUIDE/`, `shared/RHYTHM_SYSTEMS/`, `shared/PLUGIN_CALIBRATION_SCHEMA.md`,
`shared/TUNING_AND_MPE.md`, `shared/TRACK_DIVERSITY_LEDGER.md`, `shared/INTERACTION_MODES.md`,
`shared/USER_PROFILE_SCHEMA.md` for `preferences.realism_default`.

## Handoffs

| To | What it carries |
|---|---|
| MIDI Builder | the plan to execute: overlaps, controls, velocities, lengths, keyswitches |
| DAW adapter | automation lanes, articulation switches, per-note expression, tuning |
| Mix Engineer | the intended dynamic shape, so a fader does not fight it |
| Composer | requests, where a part cannot be played as written |
| Producer | where the sound choice, not the performance, is the problem |
| Music Critics | the plan, so the Performance Critic can check it against what was rendered |
| Diversity ledger | `performer_character`, so five songs do not share one player |

## Diagnosing "it sounds fake"

Work down this list. The first three are more often the cause than the last.

1. **Dynamics are flat** because there is no continuous controller movement on long notes, or it is
   going somewhere the instrument ignores.
2. **Every repetition is identical**, because round robins are absent or are being reset.
3. **Legato is not legato**, because the notes do not overlap and the patch is monophonic.
4. **Attacks are all the same**, because velocity is uniform, or because one articulation is doing
   every job.
5. **Nothing is physically true**: chords no hand could hold, fills no drummer could play, phrases no
   one could breathe through.
6. **There is no noise at all**: no breath, no fret, no bow change, no key. Real instruments are not
   silent between notes.
7. **The timing is random**, which reads as sloppy rather than human, and is the failure this skill
   exists to prevent.

## Diagnosing "it sounds sloppy"

Almost always random humanisation, or an exaggerated template. Remove the randomness, put back a
systematic model at natural magnitude, and listen again. Where a microtiming template is in use, check
it is the right corpus at the right tempo.

## Cultural care

Groove templates come from particular repertoires, measured at particular tempi. A swing ratio
measured on jazz ride cymbals is not a general fact about rhythm, and a samba sixteenth template is
not a general "latin feel". Every template names its corpus. The studio does not present one
tradition's microtiming as neutral or default, and it does not apply a tradition's feel to unrelated
music as a flavour (`shared/MUSICAL_SYSTEMS/INDEX.md`).

## Without optional tools

The plan is text and YAML. With no DAW it still tells a human player or another agent what to do. With
no calibration it uses documented values and labels them unmeasured. With no analyzer it cannot verify
what was rendered, and says so rather than claiming the performance landed.


## How this is tested

The checks that matter for this skill are mechanical, which is unusual and useful:

- **no parameter named random** anywhere in a plan. `tools/skill_lint.py` checks the pack's own pages
  for the phrasing; a plan that reintroduces it is a defect the Performance Critic reports.
- **every timing deviation names a model and a magnitude** from
  `shared/HUMAN_PERFORMANCE_SCHEMA.md`, section 3, and every imperfection names a cause from section
  4. An entry with neither does not go in.
- **magnitudes stay at or below natural**, because the research finds exaggeration is liked less than
  an exact grid.
- **feasibility is reported before the plan**, so an impossible part is a recorded decision rather
  than a surprise in the render.
- **a deliberately mechanical brief produces an empty imperfection list**, and says so.

In `research/BENCHMARK_DIVERSITY.md`: **D16** asks for a string quartet that sounds played and checks
for models rather than randomness; **D17** asks for the same music deliberately machine-exact and
checks that the studio does not add life to improve it; **D5** and **D9** check that a percussion-only
piece and an adaptive cue still get real performance plans rather than being treated as loops.
