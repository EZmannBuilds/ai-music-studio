# Guitar

Six-string guitar, acoustic and electric.

> Evidence: `musicianship` throughout, from general practice. `excerpt-derived` for the fretboard and
> strum constraints repeated across programming guidance. **No source giving a measured strum spread
> in milliseconds could be opened**, so any default this file offers is a practitioner value and is
> labelled as one.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. Six strings over a fretted neck, plucked or struck by the other hand. The fretting
hand chooses which pitches are available; the picking hand decides when and how they sound. Both
hands are physical constraints, and most of what makes a guitar part idiomatic comes from the
fretting hand rather than from the harmony.

## Range and register

`musicianship`. Standard tuning sounds E2 to roughly E5 in ordinary playing, written an octave above
sounding pitch. The open strings from low to high are E2 A2 D3 G3 B3 E4. Above the twelfth fret the
instrument thins and shortens; below the fifth fret it is thick and the voicings must open up.
**To verify against Adler**, *The Study of Orchestration*, not opened for this work.

## Articulation and note transitions

`musicianship`. The vocabulary that carries guitar writing:

```text
palm mute          picking hand edge damping the strings near the bridge; short, thick, percussive
harmonics          natural at nodal frets, artificial anywhere; bell-like, quiet, thin
bends              a fretted note pushed sideways; a whole step is common, a step and a half hard
slides             one finger moving along a string; the intervening pitches are audible
hammer-on          a note sounded by the fretting hand alone, quieter than a picked note
pull-off           the descending equivalent, quieter again
vibrato            produced by the fretting hand, applied after the attack, not from it
dead note          a muted click at a rhythmic position, with no pitch
```

Hammer-ons and pull-offs are the instrument's real legato: the note is not re-attacked, so it is
**softer than the picked note before it**. A legato line with uniform velocity has been written as if
every note were picked.

## Physical constraints

`musicianship`, and the source of most feasibility failures in this family.

```text
one note per string, six strings, so six notes maximum and no unisons on one string
the fretting hand spans about four frets in low positions, more higher up where frets are closer
open strings extend what is reachable, which is why open-position chords are shaped as they are
a barre uses one finger across all six strings, leaving three fingers for the rest of the shape
movable shapes have no open strings, so the whole shape must fit the hand
```

**Four-note voicings are the practical default for movable chords.** Six-note voicings exist mainly
in open position, where open strings do the work. A dense jazz voicing on a movable shape is usually
three or four notes, and the omitted tones are chosen, not forgotten.

## Phrase behaviour

`musicianship`. Phrases are bounded by position on the neck. A shift is audible, either as a slide or
as a small gap, and a line that never shifts across two octaves has been written on a piano. A note
decays from the moment it is plucked, so sustained writing needs re-attack, tremolo picking,
distortion, or a different instrument.

**A strum is a spread, not a chord.** A downstroke runs low string to high, an upstroke high to low,
and alternating strokes give alternating directions. The order is not decorative: it is which note
the ear hears as the top of the attack.

The temporal spread of a strum is a **practitioner value**. No measured figure was available for this
work. A useful starting default is a few milliseconds per string for a fast strum and more for a slow
expressive one, widened at slow tempos, checked by ear, and recorded as a practitioner value rather
than a fact.

## Ensemble behaviour

`musicianship`. Two guitars playing the same voicing in the same register fight; the usual solution
is different positions on the neck, so the same chord has different string assignments and different
timbre. Rhythm guitar and bass share a low register and are separated by the guitar staying above the
bass, or by the guitar playing only the upper part of its voicing.

## Recording behaviour

`musicianship`. On an electric instrument the **pickup position and the amplifier and speaker are
part of the instrument**, not effects. A neck pickup is round and dark, a bridge pickup thin and
cutting, and the speaker rolls off most of the top end, which is why a raw direct signal sounds
brittle and unlike a guitar.

**Distortion is why power chords exist.** Non-linear gain generates intermodulation between
simultaneous notes, so a third inside a distorted chord produces harsh extra content, while a root
and fifth do not. A heavily distorted part written with rich four-note voicings is arranged for a
clean instrument. `to-verify` for the physics, against Fletcher and Rossing, *The Physics of Musical
Instruments*, not opened.

Acoustic instruments are captured by microphone position along the body, and a position near the
sound hole is boomy in a way that is a characteristic of the recording, not the instrument.

## Programming it: the control model

`musicianship` and `excerpt-derived`. Product specifics belong in the calibration profile.

```yaml
velocity: level and, in most libraries, pick strength and sample selection
articulation_switching: usually keyswitches; keyswitch notes are non-sounding and must not be audible
legato_patches: often monophonic per string or per patch, and need overlap
string_assignment: some libraries infer it; where they do, voicing decides the timbre
fret_noise: a separate layer or an articulation, and it is part of the instrument
strum_handling: either recorded strum patterns, or single notes spread manually by the writer
bends_and_slides: recorded articulations in some libraries, pitch bend in others; they are not the same
```

## Programming it: what makes it sound real

- Solve the fretboard before writing the MIDI. Decide which string each note is on, then check the
  fret span and remove anything that needs two notes on one string.
- Spread every strum with a direction, and alternate directions with the rhythm.
- Make hammer-ons and pull-offs quieter than picked notes.
- Use bends and slides for register changes that would require a shift.
- Keep fret noise audible on position changes.
- Let notes decay rather than holding them; a guitar chord does not sustain like a pad.
- Capo: a capo raises all open strings together, so a capoed part keeps open-string shapes in a
  higher key. Writing in the sounding key with movable shapes gives a different, thicker instrument.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Guitar-specific tells:

- six-note voicings with impossible spans, which is error 6, and the commonest failure in this family;
- chords with every note on the same tick, which is error 3 and removes the strum entirely;
- all strums in the same direction with the same spread;
- legato passages with picked-note velocity on every note;
- sustained block chords through a distorted tone;
- a part that never shifts position and never makes a noise doing it;
- pitch bend used as a smooth glide where the instrument would bend a whole step from a fretted note.

## What the Performance Director needs from this file

- `impossible_voicings`: more than six notes, two notes on one string, spans beyond roughly four
  frets in low positions, and unisons that need one string twice.
- `simultaneity_exceeded`: six voices maximum, and four is the practical default for movable shapes.
- `out_of_range`: below E2 in standard tuning, unless an alternate tuning or capo is declared.
- `articulation_unavailable`: bends and slides recorded as articulations cannot be substituted with
  pitch bend without a report.
- `fret_noise` and `pick_noise` are recognised imperfection causes and should be requested here.
- Strum spread is a practitioner value; the Director should state the number it used and label it.

## Sources and what to verify

- **Not available**: any measured strum spread in milliseconds. This was searched for and no source
  could be opened. Every figure in this file's phrase section is a practitioner value.
- **To verify**: sounding ranges and register descriptions in Adler, *The Study of Orchestration*.
  Not opened.
- **To verify**: intermodulation under non-linear gain, in Fletcher and Rossing, *The Physics of
  Musical Instruments*. Not opened.
