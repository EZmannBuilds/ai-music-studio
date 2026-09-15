# Woodwinds

Flute, oboe, clarinet, bassoon, and the saxophones as their close relatives.

> Evidence: `musicianship` for breath, tonguing and phrase behaviour. `excerpt-derived` for the
> clarinet register map, from instrument pedagogy pages read as excerpts. `orchestration-text` for
> ranges and register colour, attributed to Adler, *The Study of Orchestration*, and Piston,
> *Orchestration*, neither opened for this work. `to-verify` where marked.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. A tube with holes, excited by an air jet across an edge (flute) or by a vibrating
reed (everything else). Opening and closing holes changes the effective tube length; overblowing
jumps to a higher harmonic. The player controls pitch, dynamic and colour with breath pressure,
embouchure and the throat, all at once.

**These are solo instruments. One player, one note.** A woodwind pad is not an instrument, it is
several players, and it has to be written as several parts with slightly different entries. This is
the single most common misuse of a sampled woodwind.

## Range and register

`orchestration-text`, attributed to Adler and Piston, not opened. Typical practical ranges.

| Instrument | Typical practical range | Register notes |
|---|---|---|
| Flute | roughly C4 to C7 | low register weak and easily covered; top brilliant and loud |
| Oboe | roughly Bb3 to G6 | low register loud and reedy; very high is thin and effortful |
| Clarinet | roughly E3 to C7 | four distinct registers, below |
| Bassoon | roughly Bb1 to Eb5 | the tenor register is the lyrical one; low is dark and reedy |

**The clarinet's four registers** are unusually distinct and matter more than any other register map
in this family. `excerpt-derived`, to verify against a clarinet pedagogy source.

```text
chalumeau (low)      dark, rich, hollow; the instrument's most characteristic colour
throat (middle low)  weak, dull and least stable; avoid sustained exposed writing here
clarion (middle high) ringing, clear, the melodic register
altissimo (top)      piercing and effortful
```

The **break** between the throat register and the clarion is a change of harmonic and of fingering,
and slurring across it is genuinely harder than slurring anywhere else. A fast slurred line that
crosses it repeatedly is difficult in a way a piano roll does not show.

`musicianship`: on the flute the low register is easily covered by anything else in the arrangement,
and its **pitch is coupled to dynamic**, because pushing more air sharpens the note. A flute playing
loudly at the bottom of its range is fighting the instrument.

## Articulation and note transitions

`musicianship`.

```text
tongued        the tongue interrupts the air to start each note; single, double and triple by speed
slurred        one continuous airstream, fingers alone changing the pitch; the real legato
staccato       short and tongued, with the air still supporting
flutter        rolled tongue or throat against the airstream; an extended technique
multiphonics   special fingerings producing several pitches at once; an extended technique
```

Tonguing and slurring are audibly different, and the difference is the phrasing. A melodic line
written as slurred groups separated by tongued entries is a woodwind phrase; the same notes all
tongued, or all slurred, is not.

## Physical constraints

`musicianship`. A phrase is a breath, and it is shorter than a singer's on the reed instruments
because the reed consumes air under pressure. **Circular breathing exists and is rare**: it is a
specialist technique, and writing a part that requires it means writing for a specialist. Say so
rather than assuming it.

Fingerings that cross the break, or that need several fingers to move together, limit speed. Trills
and rapid figures are easy in some keys and awkward in others, which is why idiomatic woodwind
writing is key-sensitive in a way string writing is not. **To verify against Adler** for the trill
tables, not opened.

## Phrase behaviour

`musicianship`. A phrase runs from breath to breath and is shaped by air pressure across its length.
Sustained notes move, because air pressure is never constant, and the note's pitch moves slightly
with it. Vibrato on flute and oboe is a breath and throat vibrato applied across the note rather than
present from the onset; the clarinet traditionally uses much less in orchestral playing.

## Ensemble behaviour

`musicianship` and `orchestration-text`. The woodwind section blends by pairing and by register: two
of a kind blend, and unlike instruments in the same register colour each other. The oboe cuts through
almost anything and is the traditional tuning reference for that reason. The flute needs to be above
the texture or it disappears.

A sustained woodwind texture is written as **separate parts with separate breaths**, entering and
leaving at slightly different points, which is also how the texture stays alive.

## Recording behaviour

`musicianship`. Close microphones capture key noise, breath and the reed; distance captures the tone
and the room. Key mechanism noise is part of the instrument and should not be gated away. Orchestral
libraries are recorded at the section's hall position and are already reverberant.

## Programming it: the control model

`musicianship`, consistent with the documented model in `STRINGS.md`. Product specifics belong in the
calibration profile.

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
short_notes:
  dynamics_from: velocity, which may also select tongued versus slurred
legato_patches: monophonic, need overlap; the transition is a slur with no new attack
polyphony: one note. A chord on one patch is a misuse, not a voicing
keyswitches: articulation selection; keyswitch notes are non-sounding
breath_noise: part of the instrument
key_noise: part of the instrument
release_samples: present, and short
extended_techniques: flutter and multiphonics are separate recordings where they exist at all
```

## Programming it: what makes it sound real

- Write one line per instrument, and breathe. A pad is several parts, offset.
- Draw dynamic shapes per phrase on long notes, and remember the register limits: a quiet high oboe
  and a loud low flute are both fighting the instrument, whatever the sample will play.
- Alternate tongued and slurred groups the way the phrasing requires.
- Keep vibrato off the onset of exposed notes where the patch allows.
- Avoid sustained exposed writing in the clarinet's throat register.
- Vary velocity on repeated notes, which is error 1.
- Leave key noise and breath audible.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Woodwind-specific tells:

- chords played on a single solo woodwind patch, which is error 14 in its purest form;
- a sustained texture with no breaths anywhere, which is error 7;
- flat sustains, which is error 2;
- loud sustained writing in the flute's bottom octave;
- exposed lyrical writing in the clarinet's throat register;
- long fast slurred lines crossing the clarinet break repeatedly;
- constant vibrato from the first millisecond of every note;
- one articulation for a whole melody, which is error 8.

## What the Performance Director needs from this file

- `breath_or_bow_overruns`: phrases longer than a breath, and a note on whether circular breathing is
  being assumed. If it is, that is an `intentional_exception`, not a silent allowance.
- `simultaneity_exceeded`: any chord on a solo woodwind patch. One player, one note.
- `out_of_range`: against the typical ranges above, labelled `orchestration-text`.
- Register warnings rather than hard blocks for the flute's low register, the oboe's extreme top and
  the clarinet's throat register. These are weak, not impossible.
- `breath` and `key_noise` are recognised imperfection causes and should be requested here.

## Sources and what to verify

- **To verify**: practical ranges, trill tables and key-sensitivity of figuration in Adler, *The
  Study of Orchestration*, and Piston, *Orchestration*. Neither was opened for this work.
- **To verify**: the clarinet register boundaries and the exact break fingering, against a clarinet
  pedagogy source. The description here is `excerpt-derived`.
- **To verify**: pitch-dynamic coupling on the flute, in Fletcher and Rossing, *The Physics of
  Musical Instruments*. Not opened.
- **Not available**: measured typical breath lengths by instrument, register and dynamic. These are
  practitioner judgements until calibrated.
