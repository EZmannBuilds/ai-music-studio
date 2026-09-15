# Mallets

Tuned percussion struck with mallets: marimba, vibraphone, glockenspiel, and the xylophone beside
them.

> Evidence: `orchestration-text` for ranges and transposition, attributed to Adler, *The Study of
> Orchestration*, not opened for this work. `musicianship` for technique, rolls and dampening. No
> measured figures.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. A row of tuned bars struck with mallets, most with tuned resonator tubes underneath.
Wooden bars give a warm tone that decays quickly; metal bars ring for a long time. That one
difference decides how each instrument is written.

## Range and register

`orchestration-text`, attributed to Adler, not opened. Typical practical ranges.

| Instrument | Typical range | Sounding |
|---|---|---|
| Marimba | C2 to C7 on a large instrument; C3 upward on smaller ones | as written |
| Vibraphone | F3 to F6 | as written |
| Xylophone | F4 to C8 written | sounds an octave above written |
| Glockenspiel | G5 to C8 written | **sounds well above written**, typically two octaves |

The glockenspiel's transposition matters in practice: written in a comfortable staff register it
sounds at the very top of the audible orchestral range, where it functions as brilliance and
punctuation rather than melody.

**Marimba** has a rich fundamental and a **short sustain**, strongest in its low and middle register
and thinner at the top. **Vibraphone** rings long, and its low register is the warmest part of it.

## Articulation and note transitions

`musicianship`. There is no true legato: each note is a strike and a decay. Connection is produced
two ways.

```text
rolls          rapid alternation on one bar, or between the notes of a chord, to sustain a pitch
pedal          on the vibraphone only; a damper bar lifted so the bars ring freely
```

**Marimba rolls are how the instrument sustains.** A held marimba note written as a long note is a
strike followed by silence, because the bar decays in a second or two. A sustained marimba line is
written as a roll, and in a sampled instrument that means either a roll articulation or actual
repeated notes at a plausible roll rate.

Other articulations:

```text
mallet hardness   soft yarn, medium, hard rubber, brass; a separate sample set, not an EQ
dead stroke       the mallet held against the bar after striking; a dry, pitched thud, vibraphone especially
hand dampening    a finger pressed on a ringing bar to stop it, while the mallets continue elsewhere
```

## Physical constraints

`musicianship`.

- Two hands, and two or four mallets. **Two mallets means two notes; four mallets means up to four**,
  and four-mallet chords are limited by **arm reach**, because the two mallets in one hand are held
  at an angle that opens and closes but cannot exceed roughly an octave and a half comfortably.
- A leap across the instrument takes time, and so does a change of mallet interval.
- Hand dampening uses a hand, so it cannot happen while both hands are playing elsewhere.
- Mallet changes take time and are made between phrases.

## Phrase behaviour

`musicianship`. A phrase is bounded by decay and by reach. On marimba the natural gesture is
continuous motion, because stopping means silence. On vibraphone the natural gesture is the opposite:
notes accumulate under the pedal and have to be cleared, so **pedalling and dampening are the
phrasing**, exactly as on a piano but with a longer decay and an audible motor.

## The vibraphone motor

`musicianship`. Discs inside the resonator tubes rotate, opening and closing them, which produces a
**tremolo, an amplitude modulation, at a selectable speed**. It is not vibrato and it does not change
pitch. The motor can be off, and it usually is in modern playing; when it is on, the speed is a
character choice and is set for a passage rather than per note. A vibraphone patch with the motor
always on at one speed is a sound, not an instrument.

## Ensemble behaviour

`musicianship`. Mallet instruments cut through by attack rather than by level, so they double melodic
lines effectively at low dynamic. The glockenspiel doubles a melody two octaves up as brilliance.
Marimba doubling a bass line adds attack without adding weight.

## Recording behaviour

`musicianship`. These are large instruments recorded from a distance that lets the resonators speak.
Close-miking a marimba emphasises the mallet click and loses the tube resonance. Orchestral libraries
place them at the back of the hall, distant and reverberant.

## Programming it: the control model

`musicianship`. Product specifics belong in the calibration profile.

```yaml
velocity: level and mallet attack hardness within one sample set; often selects the sample
mallet_sets: separate patches or keyswitches; chosen before writing
round_robins: essential, because repeated single-bar notes are exposed
rolls: either a recorded roll articulation, or written repeated notes at a plausible rate
pedal: vibraphone only; a damper state, not a reverb
motor: a speed parameter, and off is a valid setting
dead_stroke: a separate recording
release_samples: the bar stopping is audible on a damped note
```

## Programming it: what makes it sound real

- Choose the mallet set first. It changes the instrument more than the velocity does.
- Sustain marimba with rolls, not with long notes.
- Pedal the vibraphone by harmony, and clear it. Dampen notes that should stop.
- Keep four-mallet chords inside arm reach, and voice them so the outer mallets carry the outer notes.
- Vary velocity between the two hands, and between roll strokes. A roll at one velocity is error 1.
- Let the glockenspiel be short and bright rather than sustained.
- Decide the motor speed per passage, or leave it off.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Mallet-specific tells:

- long held marimba notes, which the instrument cannot produce;
- rolls written as identical repeated samples at one velocity;
- four-mallet chords spanning more than the arms reach, which is error 6;
- vibraphone written with the pedal implicitly down forever and nothing dampened;
- motor always on, at one speed, as a substitute for expression;
- glockenspiel parts written as melodies in a register where they sound two octaves higher than
  intended, which is error 4;
- mallet hardness faked with a filter.

## What the Performance Director needs from this file

- `impossible_voicings`: more than four simultaneous notes, or a four-note chord outside arm reach.
- `simultaneity_exceeded`: two mallets means two notes; state which setup the part assumes.
- `limb_or_finger_conflicts`: hand dampening competes with playing.
- `articulation_unavailable`: roll, dead stroke and mallet hardness are separate recordings.
- Sustain feasibility on marimba: a long note is a flag, and the fix is a roll, not a longer sample.
- Vibraphone pedal state should be in the plan, as the piano's is.

## Sources and what to verify

- **To verify**: ranges, transpositions and standard mallet indications in Adler, *The Study of
  Orchestration*. Not opened for this work.
- **To verify**: bar decay times by material and register, and resonator tuning, in Fletcher and
  Rossing, *The Physics of Musical Instruments*. Not opened.
- **Not available**: typical roll rates in strokes per second by instrument and dynamic. These are
  practitioner judgements until calibrated.
