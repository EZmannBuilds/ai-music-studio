# Piano and Keyboards

Acoustic piano first, then electric piano and clavinet as keyboard-family cousins with different
mechanisms.

> Evidence: `excerpt-derived` for the sampled and modelled piano capabilities, from excerpts of a
> modelled-piano manual and its forum. `to-verify` for the hammer-felt acoustics. `musicianship` for
> hand span, voicing and pedalling practice. No measured figures.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. Felt hammers thrown at strings by a mechanical action, with dampers that stop the
strings and pedals that lift or soften them. The player has no contact with the string after the
hammer leaves the action, so everything about a single note is decided at the moment of the strike,
and everything after it is pedalling and release.

`to-verify`, against Fletcher and Rossing, *The Physics of Musical Instruments*, not opened for this
work: hammer felt behaves as a nonlinear spring, so a harder strike both drives the string harder and
contacts it for a shorter, stiffer moment. The consequence is the one that matters for programming:
**velocity changes timbre as well as level.** A loud note is brighter, not only bigger.

## Range and register

`musicianship`. A full instrument covers A0 to C8, seven and a bit octaves. The extremes are
character registers rather than working ones: the bottom octave is inharmonic and thick, and muddies
quickly under pedal; the top octave has almost no sustain and functions as attack and sparkle.

The singing register sits roughly from two octaves below middle C to two above it. Below that, close
voicings turn to mud, and the usual remedy is to open the spacing as the register descends.
**To verify against Adler**, *The Study of Orchestration*, not opened.

## Articulation and note transitions

`musicianship`. The piano has no true legato: one note decays while the next begins, and the illusion
of connection is made by overlapping fingers and by the pedal. Articulation is therefore a matter of
note length, attack strength and pedal, not of separate techniques.

`excerpt-derived`. Repeated notes are limited by the action, which must reset before the same key
speaks again. A repetition faster than the action allows produces a weak or missing note, and this is
one of the few places where a written part can be physically impossible on a keyboard.

## Physical constraints

`musicianship`.

```text
two hands, ten fingers, and usually two or three pedals
a hand spans a ninth comfortably; a tenth is a stretch; wider is rolled
one finger per key, and the thumb cannot be in two places
a leap takes time, and the hand cannot hold and leap at once
```

A chord wider than a hand is not impossible, it is **rolled**, which is a different sound and should
be written as one.

## Phrase behaviour

`musicianship`. Phrases are bounded by the hand and by the pedal, not by breath. The characteristic
shape is a decay: every note begins dying immediately, so a long line is written with re-strikes,
with rhythmic figuration, or with the pedal holding harmony while the hand moves.

**Melody is voiced above inner parts.** A pianist plays the top of a chord harder than its middle,
deliberately and constantly. A chord with uniform velocity has no melody in it.

## Ensemble behaviour

`musicianship`. The piano covers its own bass, harmony and melody, so in an ensemble it is usually
either the whole accompaniment or a deliberately restricted layer. Doubling a bass part in the left
hand at the same octave as a bass instrument thickens the low end quickly.

## Recording behaviour

`excerpt-derived` and `musicianship`. Recorded close, the instrument is percussive and detailed, with
audible hammer and damper noise. Recorded further back it becomes rounder and the room takes over.
Lid position, microphone distance and whether the perspective is the player's or the audience's are
part of the instrument's sound, not effects added later.

## Programming it: the control model

`excerpt-derived`, from excerpts of one documented modelled and sampled product. Exact layer counts
and controller assignments are product facts and belong in the calibration profile.

```yaml
velocity:
  selects: level and timbre together, via recorded or modelled dynamic layers
  documented_extreme: up to roughly one hundred velocity layers per key in one product
sustain_pedal:
  binary_in_simple_patches: true
  documented_capability:
    half_pedalling: partial damper contact, a continuous value rather than on or off
    re_pedalling: lifting and reapplying so that some resonance is kept and some released
sympathetic_resonance:
  documented: modelled with and without the pedal down
soft_pedal:
  changes: colour, not only level
release_and_damper_noise: present, and part of the instrument
```

## Programming it: what makes it sound real

`musicianship`, on top of the model above.

- Voice every chord. Melody note highest in velocity, bass next, inner parts lowest.
- Roll anything wider than a hand, and roll upward by default.
- Spread chord attacks slightly rather than placing all notes on one tick.
- **Pedal follows harmony, not bar lines.** Lift where the harmony changes, and where the register is
  low enough to muddy. A pedal lane quantised to the bar is a tell.
- Use half-pedalling and re-pedalling where the patch supports them, especially under a descending
  line in the low register.
- Give notes real note-offs so the damper and release are heard.
- Vary velocity between repeated notes, and keep repetition rates within what the action allows.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Piano-specific tells:

- uniform velocity chords, which is error 3, and the reason a sampled piano sounds like an organ;
- a sustain lane that changes exactly on bar lines;
- chords wider than a hand played as blocks;
- repeated notes faster than the action, at identical velocity;
- dynamics made with a volume fader instead of velocity, so loud passages are loud but not bright;
- release and pedal noise muted for tidiness.

## Electric piano and clavinet

`musicianship`. Same keyboard, different mechanism, so the behaviour transfers only in part.

**Tine and reed electric pianos** strike a metal tine or reed and sense it with a pickup. Velocity
change is dramatic: soft is a bell, hard is a bark with an audible overdrive edge. The instrument
distorts musically as it is pushed, so the dynamic range is a timbral range. Notes sustain longer and
more purely than a piano's, and the noise floor and mechanical clunk are part of the sound.

**Clavinet** plucks a string with a rubber pad, so it is closer to a plucked instrument than to a
piano: short, sharp, and almost entirely about rhythm and note length. It has no pedal; release is
immediate and percussive, and the muted release is half the groove. Written as sustained chords it
does not work.

Both have no sympathetic resonance to speak of, and neither should inherit a piano's pedalling model.

## What the Performance Director needs from this file

- `impossible_voicings`: any simultaneous span wider than a ninth in one hand, or more than five
  notes in one hand. Wider spans are rolled, which is a performance decision, not an error.
- `limb_or_finger_conflicts`: two hands, and a hand cannot sustain and leap simultaneously.
- `velocity_asymmetry` is the correct imperfection cause for chord voicing here, and it is expected
  on every chord, not occasional.
- `melody_lead` applies: the louder note arrives fractionally first.
- Repeated-note rate is a real feasibility check on this instrument, unlike most keyboards.

## Sources and what to verify

- **To verify**: hammer felt as a nonlinear spring, and the velocity-to-spectrum relationship, in
  Fletcher and Rossing, *The Physics of Musical Instruments*. Not opened for this work.
- **To verify**: register descriptions and practical writing ranges in Adler, *The Study of
  Orchestration*. Not opened.
- `excerpt-derived` material comes from excerpts of one modelled-piano manual and its forum, not
  named here by folder rule 6 in `INDEX.md`.
- Not available: any measured figure for maximum repetition rate, or for typical chord roll spread.
  Both are practitioner values until calibrated.
