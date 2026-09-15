# Brass

Horn, trumpet, trombone, tuba, and the family around them.

> Evidence: `musicianship` for breath, endurance and attack behaviour. `excerpt-derived` for the horn
> material, from a public orchestration academy's horn articles read as excerpts. `orchestration-text`
> for ranges and mute behaviour, attributed to Adler, *The Study of Orchestration*, and Berlioz and
> Strauss, *Treatise on Instrumentation*, neither opened. `to-verify` for the spectral physics.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. A column of air in a tube, excited by the player's vibrating lips, with valves or a
slide changing the tube length. The player's embouchure selects which harmonic of the tube sounds,
so pitch is a joint decision between the lips and the valves, and it is never entirely mechanical.

Two consequences run through the whole file. **Breath bounds the phrase**, and **embouchure fatigue
accumulates**: a high loud passage costs the player something that is not repaid until they rest.

## Range and register

`orchestration-text`, attributed to Adler and to Berlioz and Strauss, not opened. Typical practical
ranges, to verify.

| Instrument | Typical practical range | Character |
|---|---|---|
| Horn | roughly F2 to F5 | wide; the upper middle is the singing register and the most tiring |
| Trumpet | roughly F3 to C6 | brilliant above the staff, thick and less agile at the bottom |
| Trombone | roughly E2 to B4 | full and vocal in the middle; the pedal register is a special effect |
| Tuba | roughly D1 to F4 | the bottom is slow to speak and needs time and air |

The horn plays in a high, closely spaced part of its harmonic series, which is why it is the least
secure of the family and why its notes are traditionally considered the most easily cracked.
`excerpt-derived`.

Register and endurance interact: a passage that is comfortable once is not comfortable for sixteen
bars. Write rests, and mean them.

## Articulation and note transitions

`musicianship`. Notes are started by the tongue or by the breath alone.

```text
tongued          a clean consonant start; single, double or triple tonguing by speed
slurred          the air keeps moving and the lips or valves change the pitch; no new attack
accented         a harder tongue and more air, which is also a brighter sound
fall, rip, doit  approach and departure gestures through the harmonic series, not pitch bends
flutter          rolled tongue against the airstream
```

**Attack character changes with dynamic and with register.** A quiet low entry speaks slowly and
softly; a loud high one has a hard, bright front edge. A library that plays one recorded attack at
all dynamics is the thing the dynamic-layer crossfade exists to fix.

## Physical constraints

`musicianship` and `excerpt-derived`.

- A phrase is a breath. Long tied passages are impossible for one player, and are covered in a
  section by staggered breathing, which is invisible but real.
- Endurance is finite and cumulative. `performer_fatigue` is a recognised imperfection cause.
- **Mutes are physical objects.** Fitting or removing one takes time, and a mute change needs rest
  bars in the part. It is not a filter switch.
- Trombone glissando is limited by **slide reach**: a true glissando is only available between notes
  on the same harmonic within the seven slide positions. Anything else is a valve-style leap or a
  lip movement, not a slide.
- Horn lip trills are easiest where the harmonics are close together, which is the upper middle
  register, and easiest as **whole tones**. Lower down the harmonics are too far apart to trill with
  the lip at all. `excerpt-derived`, to verify against a horn pedagogy source.

## Phrase behaviour

`musicianship`. A brass phrase has a breath at each end and an air-driven shape in the middle. Held
notes move: the air pressure is never perfectly constant, and players lean into and out of long
notes as a matter of course. A perfectly flat brass sustain does not occur.

**A swell is a timbre change, not a volume fade.** Brass spectra brighten with dynamic, so a
crescendo is the tone opening up, and a loud recorded note turned down with a fader is a loud tone
played quietly, which is audibly wrong. `to-verify` against Fletcher and Rossing, *The Physics of
Musical Instruments*, not opened for this work. This is error 10 in `COMMON_ERRORS.md` and it matters
more on brass than anywhere else.

## Ensemble behaviour

`musicianship` and `orchestration-text`. Brass blends with itself more readily than with anything
else, and a brass section is heard as one instrument when the players match attack and vibrato.
Horns sit between the woodwinds and the heavy brass and are used to join them. A brass section at
full dynamic covers everything else in the arrangement, which is a compositional fact rather than a
mix problem.

**Stopped horn is not a muted horn.** The hand is pushed into the bell, which darkens and constricts
the tone and **raises the pitch by about a semitone**, so the player transposes to compensate. It is
a different colour from a straight mute and the two are not interchangeable. `excerpt-derived`.

## Recording behaviour

`musicianship`. Brass is directional and loud, so distance and angle change the sound enormously.
Close microphones capture the bell and the buzz; distant ones capture the room being driven by the
instrument, which is where most of the impression of power comes from. Orchestral libraries are
usually recorded at the section's hall position, already wide and already reverberant.

## Programming it: the control model

`musicianship`, consistent with the documented model in `STRINGS.md`. Product specifics belong in the
calibration profile.

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
  because: the timbre must change with the level, or the swell is a fade
short_notes:
  dynamics_from: velocity, which may also select the attack type
mutes:
  are: separate sample sets, loaded and keyswitched
  are_not: a filter or an EQ curve applied to an open patch
  require: rest bars in the part for the change
stopped_horn:
  is: a distinct sample set, not a mute preset
legato_patches: monophonic, need overlap, and the transition is a slur with no new attack
release_samples: present; brass note ends are audible
breath_noise: part of the instrument; do not mute it
```

## Programming it: what makes it sound real

- Draw a dynamic curve on every long note, and let the loudest point be the brightest.
- Write breaths. Put real gaps where a player would take one, and vary their length.
- Model fatigue: after a long loud high passage, let the next entry be a little less confident.
- Keep mute changes plausible and leave bars for them.
- Use the attack that fits the register and the dynamic, not one attack everywhere.
- Alternate round robins on repeated notes, and vary velocity, which is error 1.
- In a section, do not align the attacks exactly. `ensemble_spread` is the cause.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Brass-specific tells:

- swells made with a volume fader, which is error 10;
- phrases longer than a breath, with no gaps anywhere in a part;
- mute changes with no time to make them, and mutes implemented as filters;
- stopped horn and straight mute used interchangeably;
- a trombone glissando across an interval the slide cannot reach;
- horn lip trills written wide, or written low where the harmonics are too far apart;
- flat sustains, which is error 2;
- a section attacking on one tick with one velocity, which is error 3.

## What the Performance Director needs from this file

- `breath_or_bow_overruns`: any phrase longer than a plausible breath, per instrument and register.
- `out_of_range`: against the typical ranges above, noting that they are `orchestration-text`.
- `articulation_unavailable`: mutes and stopped horn are separate sample sets; substitution is
  reportable.
- `impossible_voicings`: one note per player. A brass dyad is two players.
- `performer_fatigue` is a recognised cause and should be applied to long high loud passages.
- Mute changes should be reported as `limb_or_finger_conflicts` when there is no time to make them.

## Sources and what to verify

- **To verify**: practical ranges, mute descriptions and section writing in Adler, *The Study of
  Orchestration*, and Berlioz and Strauss, *Treatise on Instrumentation*. Neither was opened.
- **To verify**: spectral brightening with dynamic, in Fletcher and Rossing, *The Physics of Musical
  Instruments*. Not opened. This claim carries a lot of weight in this file and deserves the check.
- `excerpt-derived` horn material came from a public orchestration academy's horn articles, read as
  search excerpts only.
- **Not available**: measured attack times by register and dynamic. Calibrate if a part depends on it.
