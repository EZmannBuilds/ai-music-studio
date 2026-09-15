# Synths and Samplers

Electronic instruments, and the general question of what "organic" means when there is no acoustic
original to imitate.

> Evidence: `musicianship` throughout, in the sense of general practice stated as inference.
> `manual-derived` only where this file repeats the sample-library control model from `STRINGS.md`.
> No measured figures. Read with `shared/TUNING_AND_MPE.md` for per-note expression and microtuning.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## The rule this file exists for

```text
ORGANIC DOES NOT MEAN ACOUSTIC IMITATION.
It means response and change.
```

`musicianship`. A synthesizer that sounds alive is not one that sounds like a violin. It is one that
**responds** to what the player does and **changes** while the note is sounding. Those are two
different axes and both are needed.

A synthesizer part judged by an acoustic-realism standard will be rewritten into a bad imitation of a
string section. The correct standard is the one below.

---

## What the instrument is

`musicianship`. A sound generator with no fixed body, no fixed excitation and no physical constraints
except the ones the designer chose. That is its advantage and its problem: nothing in the instrument
forces variation, so any variation has to be put there.

There is no range limit, no breath, no hand span, and no reason a note must end. Every one of those
freedoms removes a source of natural variation that acoustic instruments get for nothing.

## Range and register

`musicianship`. Unbounded in principle, bounded in practice by two things: what the ear resolves, and
what the arrangement has room for. A synthesizer pad spread across six octaves occupies the space
every other instrument needs. Register discipline on electronic instruments is an arrangement
decision rather than a physical one, and it has to be made rather than inherited.

Low bass below the fundamental of the playback system is a real constraint. See `BASS.md`.

## Response: what the player's input should reach

`musicianship`. The first axis of organic.

```text
velocity        should reach more than level: filter cutoff, envelope times, waveshape, layer balance
aftertouch      channel or polyphonic; a second continuous dimension inside a held note
MPE             per-note pitch, pressure and a third dimension, so one voice in a chord can move alone
mod wheel       a macro, not a vibrato depth control by default
expression      a continuous line, drawn per phrase
breath / ribbon / foot   any continuous input the performer actually has
```

**Velocity mapped only to level is the electronic equivalent of a sampled instrument with one dynamic
layer.** It is error 9 in `COMMON_ERRORS.md` seen from the other side: the control exists, and nothing
listens to it.

MPE is the largest single upgrade available to a synthesizer part, because it lets a chord behave like
several players instead of one gesture. `shared/TUNING_AND_MPE.md` covers how it reaches the target
and what to do when the target cannot carry it.

## Change: what should move without being played

`musicianship`. The second axis.

- **Per-voice drift and detune.** Every voice slightly different in pitch, and drifting slowly and
  independently. This is what "analogue" usually means when people say it, and it is the difference
  between a chord and a stack.
- **Envelope variation per note.** Attack and decay times varying a few percent per note, so repeated
  notes are not identical. This is the electronic answer to round robins.
- **Nonlinear saturation.** A stage where louder is also **different**, not just bigger: harmonics
  appear as the signal is driven. Without one, a crescendo is a fader move, which is error 10.
- **Evolving timbre across a held note.** A slow filter movement, a slow modulation of a waveform, an
  LFO that is not synchronised to anything. A held note that does not change is a held sample.
- **Macro gestures.** One control moving several parameters at once, in the way a player's single
  physical gesture changes several things about an acoustic instrument simultaneously. A macro is the
  synthesizer's version of bow pressure.
- **Instability as a parameter.** A small amount of drift, noise or unpredictability in the right
  place, chosen and dialled rather than sprinkled. It has a cause, like every imperfection in
  `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4.

## What sounds fake here

`musicianship`. The general list is in `COMMON_ERRORS.md`, and most of it applies, but the
family-specific failure is single and specific:

> **A static preset with one envelope and no modulation is the electronic equivalent of a
> machine-gunned sample.**

Around it:

- velocity mapped to level only;
- every voice of a chord identical, in tuning and in envelope;
- a held note that is the same at its end as at its beginning;
- crescendos made with a volume fader through a linear signal path;
- LFOs all synchronised to the grid, so every movement lands on a subdivision;
- a pad occupying six octaves because it can;
- aftertouch and MPE available and unused;
- randomisation applied everywhere as a substitute for a decision, which is not organic, it is noise.

Note the last one. Organic is not random. Random modulation with no cause is a bug, exactly as in
`shared/HUMAN_PERFORMANCE_SCHEMA.md`, and `realism_target: deliberately_mechanical` is a legitimate
choice that should produce a genuinely static part rather than a slightly wobbly one.

---

## Samplers

`manual-derived` and `musicianship`. A sampler is a different problem: the instrument's behaviour was
decided by whoever recorded it, and it is not discoverable from the notes.

**Identify the library's control model before writing any notes.** Three questions, in this order:

```text
1. What does velocity mean here?
   level? timbre? articulation selection? legato transition type? nothing at all?

2. What carries dynamics on long notes?
   a continuous controller crossfading recorded layers? a volume trim? velocity only?

3. Do round robins exist, and how many?
   and does the host reset them?
```

`manual-derived`: in the one library read in full for this work, the answers were velocity for short
notes and transition selection in legato patches, a continuous controller crossfading recorded dynamic
layers on long notes, a separate expression control acting as a volume trim, and round robins present.
**That is one library's answer, not the answer.** The next one differs, which is why these facts live
in the calibration profile and not here.

Two more, which catch people out:

- **Legato patches are monophonic and need overlap**, as in `STRINGS.md`.
- **Samples cut from the true onset make notes sound late.** The fix is negative track delay, not
  dragging the notes earlier.

Where a sampler is being used for a sound rather than an imitation, all of the synthesizer guidance
above still applies: layer, detune, saturate, modulate and let the note change.

## Programming it: what makes it sound real

- Map velocity to at least two things, one of them timbral.
- Use aftertouch or MPE if the target can carry it, and say so in the plan if it cannot.
- Detune and drift the voices, slightly and independently.
- Put a nonlinear stage somewhere in the path so dynamics change colour.
- Give every sustained note something that moves, with a period unrelated to the bar length.
- Vary envelope times per note rather than repeating one exactly.
- Build a macro for the gesture the part needs, and automate the macro rather than five parameters.
- Decide the register the part occupies and hold it.

## What the Performance Director needs from this file

- **The realism standard is response and change, not acoustic plausibility.** A synthesizer part
  should not be flagged for being unplayable by a human unless the brief asked for a played instrument.
- Physical feasibility mostly does not apply. `impossible_voicings` and `limb_or_finger_conflicts` are
  meaningful only when the brief specifies a performed instrument.
- `dynamic_arc.control` should be a control the patch actually maps, and the plan should name it.
- Per-note expression requirements go to `shared/TUNING_AND_MPE.md`, and the DAW adapter reports in
  `daw_capabilities` whether it can carry MPE and tuning at all.
- For a sampler part, the plan should carry the three control-model answers above, from calibration.
- `drift_1f`, `pitch_drift` and `note_length_variation` are the recognised imperfection causes that
  transfer here. Anything else needs a stated cause.

## Sources and what to verify

- `manual-derived` material repeats the control model documented in `STRINGS.md`, from the one
  symphonic strings manual read in full for this work.
- **Not available**: any measured figure for per-voice detune amounts, drift rates or envelope
  variation that sounds natural. These are taste decisions, and a calibration render is the only way
  to turn them into numbers for a given instrument.
- Everything else in this file is `musicianship`: general practice stated as inference, not citation.
