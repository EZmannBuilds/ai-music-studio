# Percussion

Orchestral percussion and hand percussion. The drum kit has its own file, `DRUM_KIT.md`. Tuned
mallet instruments have their own file, `MALLETS.md`.

> Evidence: `orchestration-text` for the orchestral percussion material, attributed to Adler, *The
> Study of Orchestration*, and Berlioz and Strauss, *Treatise on Instrumentation*, neither opened for
> this work. `musicianship` for the hand percussion material and the stroke vocabularies. No measured
> figures.

**Tabla, and any other drum belonging to a specific living tradition, route to
`CULTURALLY_SPECIFIC_INSTRUMENTS.md`.** This file does not summarise them, because a stroke
vocabulary lifted out of its tradition and printed as a table is exactly the failure that file exists
to prevent.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. A family united only by being struck, scraped or shaken. Each member is its own
instrument with its own physical rules, so this file is a set of behaviours rather than one model.
The two generalisations that hold: **the striking implement is half the sound**, and **what happens
after the strike is the other half**, because most of this family rings.

---

## Orchestral percussion

### Timpani

`orchestration-text`. Pitched drums, typically a set of four covering roughly D2 to A3 between them,
to verify against Adler. They are **tuned by pedal**, and a pedal change takes time and is audible as
a pitch bend if made while the head is ringing. A part that retunes a drum instantly between adjacent
bars is not playable, and a part that retunes silently during a rest needs the rest.

Mallet hardness governs the attack spectrum: soft mallets give a low thud with almost no articulation,
hard ones give a defined, bright attack. This is a sample set choice, not an EQ.

Rolls are single-stroke alternation at speed, and they sustain the note. The drum rings after the
stroke and must be damped by hand when the note should stop.

### Cymbals

`musicianship`. A suspended cymbal struck with a stick or rolled with mallets rings for a long time
and decays slowly. **The ring is the note.** A choke is a physical grab and is implemented as a
note-off or an aftertouch message depending on the product. Crash cymbals played as a pair have a
different, shorter, more air-driven sound than a struck suspended cymbal.

### Snare drum

`musicianship`. The orchestral snare's defining feature is the **wire buzz** underneath the head,
which rings after each stroke and, importantly, **buzzes sympathetically** when other loud
instruments play. A sampled snare with no sympathetic buzz sits outside the orchestra.

Rolls are pressed rather than alternated, giving a continuous sound rather than distinct strokes.
The wires can be disengaged, which turns the instrument into a small tom.

### Bass drum

`musicianship`. Large, low, and mostly air. Beater type and **muffling** decide almost everything:
an unmuffled drum booms and sustains, a muffled one thumps and stops. Muffling is a physical state
that persists, not a per-note choice.

---

## Hand percussion

`musicianship`. Struck with hands rather than sticks, which changes both the vocabulary and the speed.

**The core three strokes on most hand drums:**

```text
bass    the palm in the centre of the head; low, round, little attack
open    the fingers at the edge; the drum's pitched, ringing tone
slap    a sharp cupped strike at the edge; bright, cracking, cutting
```

Those three plus their muffled variants carry most hand drum writing. The accents are made of open
and slap strokes, and **heel-toe motion fills the space between the accents**: the hand rocks so that
the heel of the palm and the fingertips alternate, producing quiet subdivisions that are neither bass
nor open strokes. That filler is what makes a hand percussion part sound played. Without it the part
is a sequence of accents on a grid.

**Two hands alternating sets the speed limit.** A hand drum part faster than alternating hands can
manage is not playable, and a part that requires the same hand twice in immediate succession at speed
is not either.

**Cajón** is a box struck with the hands, with a bass tone in the centre of the face and a snare-like
slap at the top corners, often from wires or snares mounted inside. It behaves like a kick and a
snare played by two hands, with the same two-hand speed limit.

Shakers, tambourines and similar instruments are driven by a continuous arm motion, so they have a
natural pulse and a natural asymmetry between the forward and backward stroke. A shaker part with
identical hits at identical velocity has no arm in it.

---

## Phrase behaviour

`musicianship`. Percussion phrases are bounded by damping and by the hands. Ring is the default and
silence is the effort: a part that wants short notes has to say who is damping and when. In the
orchestra, damping timpani and cymbals is a written instruction and takes a hand.

## Ensemble behaviour

`musicianship`. Percussion is usually a marker layer in the arrangement, so timing deviation applied
to it moves the reference. Where a percussion part is the pulse, name it in `marker_parts_excluded`.

## Recording behaviour

`musicianship`. Orchestral percussion is recorded at the back of the hall, so it is distant and
reverberant by design, and close-miking it produces an instrument that is not in the same room as
the orchestra. Hand percussion is usually close, where hand noise, skin contact and the body of the
drum are audible, and those noises are the instrument.

## Programming it: the control model

`musicianship`. Product specifics belong in the calibration profile.

```yaml
velocity: selects the stroke sample first, the level second
round_robins: essential; percussion is the most exposed family for repeated identical samples
mallet_or_beater: a separate sample set, chosen before writing, not an EQ afterwards
timpani_tuning: a pedal state with a real transition time; check pedal changes as feasibility
damping: an explicit event; ring is the default
chokes: note-off or aftertouch, depending on the product
sympathetic_buzz: a feature of a good orchestral snare patch; do not gate it away
```

## Programming it: what makes it sound real

- Choose the implement first, then write the part.
- Write the quiet strokes: heel-toe filler on hand drums, taps and ghost strokes elsewhere.
- Alternate hands, and give the two hands slightly different velocities.
- Let things ring, and write the damping where it is wanted.
- Give timpani pedal changes the time they need.
- Vary velocity continuously on shakers and tambourines rather than repeating one value.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Percussion-specific tells:

- one sample repeated identically, which is error 1, most audible on shaker and tambourine;
- accents on a grid with nothing between them;
- cymbal and timpani notes truncated instead of damped, which is error 12;
- timpani retuning instantly;
- hard and soft mallets faked with a filter;
- an orchestral snare with no sympathetic buzz;
- hand percussion written at speeds two hands cannot alternate.

## What the Performance Director needs from this file

- `limb_or_finger_conflicts`: two hands, and damping takes one of them.
- `out_of_range`: timpani pitch per drum, and the pedal transition time between settings.
- `articulation_unavailable`: bass, open and slap are separate recordings, and so are mallet hardness
  sets.
- `simultaneity_exceeded`: two hands per player, and one player per instrument unless the part says
  otherwise.
- Marker part declaration where the percussion carries the pulse.

## Sources and what to verify

- **To verify**: timpani ranges, mallet conventions and damping notation in Adler, *The Study of
  Orchestration*, and Berlioz and Strauss, *Treatise on Instrumentation*. Neither was opened.
- **To verify**: cymbal and drumhead decay behaviour, in Fletcher and Rossing, *The Physics of
  Musical Instruments*. Not opened.
- **Not available**: measured stroke velocity bands for hand percussion. Do not borrow the drum kit's
  ghost note band, which is for sticks on a snare.
- Tradition-specific drums are deliberately absent. See `CULTURALLY_SPECIFIC_INSTRUMENTS.md`.
