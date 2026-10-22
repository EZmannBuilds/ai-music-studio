# Patch Design and Review Standard

Use this as the one-page brief and acceptance checklist for an original synth patch. A rich patch is a playable instrument with deliberate behavior, not a high count of oscillators, effects, or modulation slots.

## 1. Patch brief

```yaml
patch:
  name:
  version:
  synth: Vital
  synth_version:
  author:
  status: concept | built | rendered | auditioned | approved
  musical_role: lead | bass | pad | pluck | keys | texture | transition | other
  song_context:
  intended_register:
  note_behavior: short | sustained | legato | percussive | evolving | other
  audible_target:
    attack:
    body:
    motion:
    release:
    stereo:
  constraints:
  knowledge_status: sourced | measured | inference | to-verify
  reconstruction_note: # explain whether this is an original recipe and what has/has not been auditioned
  architecture:
    oscillator_sources: []
    wavetable_or_warping:
    sample_or_noise:
    filter_routing:
    amplitude_envelope:
    modulation_routes: []
    effects_order: []
    performance_controls: []
  render_tests: []
  known_issues: []
  next_revision:
```

## 2. Build order

1. **Role and register:** decide what the patch does in the arrangement and where it sits.
2. **Source:** choose a basic waveform, wavetable, sample/noise component, or intentional combination.
3. **Amplitude envelope:** make note-on and note-off behavior fit the part before adding effects.
4. **Spectral shape:** use wavetable position, a warp mode, oscillator blend, or filter to form the tone.
5. **Movement:** add one modulation route at a time; define its audible purpose and safe range.
6. **Performance:** add velocity, note tracking, aftertouch/MPE, glide, or macro controls only where useful.
7. **Layering:** make each layer supply a distinct function (sub/body, transient, air/noise, width, motion, dirt).
8. **Effects:** add color and space after the dry patch has an identity. Check that effects do not obscure the source.
9. **Musical test:** play the actual role in a phrase and revise in context.

## 3. Modulation route card

For every important route, document:

| Field | Question |
|---|---|
| Source | Which envelope, LFO, random, note, velocity, pressure, or macro drives it? |
| Destination | Which sound parameter changes? |
| Direction | Positive, negative, bipolar, or remapped? |
| Range | What is the minimum-to-maximum audible change? |
| Time scale | Per note, per beat/bar, slow drift, or performance gesture? |
| Musical purpose | What does a listener hear that they would not hear without it? |
| Failure cue | What would make this route too much, too fast, or distracting? |

Vital supports drag-and-drop modulation and an explicit matrix, including modulation amount/polarity and remapping. Treat the matrix as a design and debugging view, not a reason to fill every available slot.

## 4. Complexity rubric

Score each 0–2. A patch need not score highly in every dimension; its role decides what matters.

- **Source identity:** source choice and spectral structure fit the target.
- **Time behavior:** attack, sustain, and release have a clear shape.
- **Internal motion:** modulation creates meaningful change over at least one useful time scale.
- **Interaction:** velocity, note, macro, pressure, or automation changes the sound usefully.
- **Layer function:** any extra source contributes something distinct and audible.
- **Playability:** patch behaves across a musical phrase, range, and intended polyphony.
- **Mix fit:** low end, stereo, and effects are controlled in the song context.
- **Explainability:** another person can reproduce the design decisions and understand why they exist.

A minimum viable patch should pass the role, time behavior, playability, and explainability checks. An advanced patch should score 10/16 or higher, with no zero in its primary role dimensions. A score never replaces listening.

## 5. Test protocol

Save versions, preserve the original, and compare at matched perceived loudness where possible.

1. **Source audition:** oscillator(s) alone, effects off.
2. **Envelope audition:** short notes, long notes, note-off tail.
3. **Range:** play the intended low, middle, and high notes; note what changes and whether it remains useful.
4. **Velocity:** soft, medium, hard. Check both loudness and timbral change.
5. **Polyphony:** single notes, intervals, and the densest expected chord. Listen for cancellation, masking, or excessive build-up.
6. **Movement:** hold a note and play a short phrase. Confirm modulation is audible, musical, and not merely visual.
7. **Macro/performance:** test each control from minimum to maximum; verify the sweep remains useful throughout.
8. **Context:** place it in the intended song role. Check masking, low-end overlap, stereo stability, and transition behavior.
9. **Render check:** compare DAW playback and render; check silence, clipping, clicks, excessive tail, and preset recall.

## 6. Revision note

Record: what was heard; the likely cause; one change; what was held constant; the result; keep/revert decision; next question. If a change improves one note but harms the phrase, revise or revert it.
