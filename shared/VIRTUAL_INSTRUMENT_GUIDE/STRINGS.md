# Strings

Bowed strings: violin, viola, cello, double bass, solo and in sections.

> Evidence: this is the best-supported file in the folder. The programming half is `manual-derived`
> from the one symphonic strings user manual read in full for this work. The behaviour half is
> `musicianship` and `orchestration-text`, attributed to Adler, *The Study of Orchestration*, and
> Piston, *Orchestration*, neither of which was opened. Numbers are typical ranges.

Cross-family failures are in `COMMON_ERRORS.md`. This file covers what is specific to bowed strings.

---

## What the instrument is

`musicianship`. A string under tension, excited by a bow drawn across it, amplified by a wooden body.
The player controls pitch with one hand and everything else with the other: bow direction, speed,
pressure and contact point. Those four produce **dynamics and timbre at the same time**. Close to the
bridge with pressure is loud and edgy; over the fingerboard with a light fast bow is soft and
breathy. There is no setting that gives loudness without colour.

A bow has finite length, so a long note eventually requires a bow change, which is audible.

## Range and register

`orchestration-text`, attributed to Adler and Piston, not opened. Treat as typical ranges.

| Instrument | Typical practical range | Notes |
|---|---|---|
| Violin | G3 upward, roughly three and a half octaves in ordinary writing | top limited by player, not instrument |
| Viola | C3 upward | darker C string, the family's inner voice |
| Cello | C2 upward | tenor register around C3 to C4 is the singing one |
| Double bass | E1 upward, sounding an octave below written | low extension to C1 on some instruments |

Each instrument's lowest string has a distinct weight the strings above it do not have. High
positions on a low string are thicker and more effortful than the same pitch on a higher string, and
players choose between them for colour. **To verify against Adler for exact extremes.**

## Articulation and note transitions

`musicianship`. Articulations are distinguished mainly by **whether the bow leaves the string** and
how the note is started.

```text
on the string      sustained bowing, detached strokes, slurred groups, tremolo, accented attacks
off the string     bounced and thrown strokes, and everything derived from them
not bowed          plucked, and struck with the wood of the bow
```

Legato on a real instrument is a slur: several notes under one bow, with the left hand changing pitch
while the bow keeps moving. That is why a legato transition has a sound of its own, and why it is
recorded rather than synthesised in a sampled library. A change of bow direction under a slur mark is
a different thing again and is faintly audible.

Plucked playing needs time to prepare: the player puts the bow down or shifts grip. Allow a beat or
more when moving from bowed to plucked and back. `musicianship`.

## Physical constraints

`musicianship`. Four strings, one bow. Two adjacent strings can sound together. **Chords of three and
four notes are broken**, played as a fast roll, unless open strings let two pairs sustain. Wide
double stops are limited by hand span in low positions. A held note longer than a bow length needs a
bow change or, in a section, staggered bowing, which the section does invisibly.

## Phrase behaviour

`musicianship`. Phrases are bounded by bow length and by musical breath, and players shape them:
into the phrase, over its peak, away from its end. **Vibrato is shaped across the phrase**, often
absent at an onset and arriving as the note establishes, widening toward a climax. Constant vibrato
from the first millisecond of every note is a sampler behaviour, not a player behaviour.

## Ensemble behaviour

`manual-derived` and `musicianship`. A section is many slightly unsynchronised players. Its attacks
and its legato transitions **smear** where a soloist's are sharp, and that smear is the sound of a
section, not a defect. A solo patch and a section patch are therefore not interchangeable at any
size.

`manual-derived`: a sampled section has a practical voice count before the section must divide.
Writing more simultaneous notes than that does not add players, it re-plays the same recorded people.
Divisi thins each part, and the real ensemble gets more exposed as it divides.

## Recording behaviour

`manual-derived`. Orchestral string libraries are normally recorded in a hall, in the section's
seating position, with several microphone positions offered. Position affects distance, width and
how much hall is in the sound, and each active position costs load. A patch recorded in a hall is
already wide and already reverberant, and treating it as a dry source produces a section that sits
behind everything.

## Programming it: the control model

`manual-derived`, from the one manual read in full. Controller numbers, velocity zones and latency
figures are product facts and live in the calibration profile, never here.

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
  manual_says: the most important controller; always use it on long notes
expression:
  is: a volume trim
  is_not: the dynamics control
short_notes:
  dynamics_from: velocity
  velocity_may_also: select the articulation
legato_patches:
  polyphony: monophonic
  requires: overlapping notes to trigger a recorded transition
  in_one_library: the arriving note's velocity selects which transition is used
timing:
  samples_cut_from: the true onset, so notes sound late
  fix: play tight and apply a negative track delay
  not: dragging the notes earlier
round_robins: prevent repeated identical samples
release_triggers: matter most in slow music
sections: have a practical voice count before divisi
```

The manual's own summary rule is worth keeping as the file's closing standard: **there are no rules,
save that of plausibility.**

## Programming it: what makes it sound real

`manual-derived` and `musicianship`.

- Draw a dynamic curve on every long note, per phrase, not per bar. This is the single largest
  improvement available on a string part.
- Overlap legato notes by the amount the patch needs, and treat the arriving velocities as
  articulation choices.
- Compensate the onset offset with negative track delay so the notes stay where they were written.
- Vary bow direction implicitly by alternating short-note samples, and leave room for a bow change in
  a long line.
- Delay vibrato onset on exposed sustained notes where the patch allows it.
- Keep release triggers by giving notes real note-offs, especially in slow music.
- For a section, do not tighten the attacks. Smear is correct.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. The string-specific tells:

- flat sustains with no dynamic curve, which is error 2 and the loudest tell in this family;
- legato patches fed non-overlapping notes, which is error 5;
- three and four note chords sustained rather than broken;
- constant vibrato from every onset;
- section patches asked for more simultaneous voices than the section has, which is error 14;
- notes dragged earlier to fix sample onset delay, which loses the written timing;
- plucked and bowed alternating instantly with no preparation time.

## What the Performance Director needs from this file

- `legato_overlap_ms` is required and comes from calibration; this file says only that overlap is
  mandatory and the patch is monophonic.
- `impossible_voicings`: any sustained chord of three or more notes on one instrument, unless open
  strings support it.
- `simultaneity_exceeded`: chord density above the section's practical voice count.
- `breath_or_bow_overruns`: sustained notes longer than a bow, for solo parts. A section hides this.
- `articulation_unavailable`: on-string versus off-string strokes are genuinely different recordings;
  substituting one for the other is a reportable change, not a free choice.
- `ensemble_spread` is the correct imperfection cause for a section attack, and it should not be
  reduced toward a soloist's precision.

## Sources and what to verify

- Read in full: one symphonic strings user manual. Everything labelled `manual-derived` above comes
  from it. It is not named here by folder rule 6 in `INDEX.md`.
- **To verify**: practical ranges and register descriptions against Adler, *The Study of
  Orchestration*, and Piston, *Orchestration*. Neither was opened for this work.
- **To verify**: bow contact point and its spectral effect against Fletcher and Rossing, *The Physics
  of Musical Instruments*. Not opened.
- Not available: any measured figure for section attack spread. If one is needed, calibrate.
