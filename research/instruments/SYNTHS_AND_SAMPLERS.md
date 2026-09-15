# Synths and Samplers: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Two behaviour cards (a general synthesizer, covering both subtractive/analog and digital/virtual-
analog instruments together, and a sampler), plus brief, uncarded treatment of drum machines and
arpeggiators in prose, per the brief's "briefly" instruction. Six sources were read at section depth:
the official MIDI Polyphonic Expression specification, one pedagogy article on glide/portamento and
mono/legato/retrigger modes, one manufacturer manual page on filter key tracking, one technical
explainer on round-robin sampling, one pedagogy article on drum-machine sequencer programming, and one
pedagogy article on analog oscillator drift. A manufacturer support article stating that analog
oscillator drift is expected, normal behaviour was targeted at two different manufacturers' help
centres and both returned HTTP 403 responses to this session's fetch tool; it is recorded `not-read`.

Performance-behaviour claims here (glide, mono/legato/retrigger, envelope/note-length, velocity and
aftertouch/MPE) are read against `shared/HUMAN_PERFORMANCE_SCHEMA.md`, which this file does not
re-derive; where a claim is really that schema's own content restated for the synthesizer context, it
is tagged `inference` and cross-referenced rather than given a fresh source.

## Records

### SYN-01 MPE assigns each sounding note its own MIDI channel to carry independent pitch, pressure and timbre
- claim: MIDI Polyphonic Expression assigns each active note its own MIDI channel for the note's
  lifetime, so Pitch Bend and Control Change messages (which are ordinarily channel-wide) can apply to
  one note at a time inside a chord. The specification defines three per-note control dimensions:
  pitch (via Pitch Bend, default range plus-or-minus 48 semitones per note, changeable via RPN 0),
  pressure (via Channel Pressure, i.e. monophonic/channel aftertouch per note-channel), and a third
  dimension, timbre (via CC74). Channels are organised into Zones with a dedicated Master Channel per
  Zone carrying information common to the whole zone.
- source: MPE-SPEC-2018 (section)
- source_type: specification
- confidence: high
- scope: any MPE-compliant controller, synthesizer or DAW implementing the MMA/AMEI RP-053
  recommended practice.
- limitations: this is the specification's own stated design, not an independent evaluation of how
  well real hardware implements it; implementation quality and per-note channel availability (limited
  by how many channels a Zone reserves) vary by product and are calibration-profile facts, not guide
  facts.
- inference: none for the specification's content; the guide's framing of MPE as "the largest single
  upgrade available to a synthesizer part" is this pack's editorial emphasis, consistent with the 2.0
  page's existing claim.

### SYN-02 Mono, legato and retrigger modes differ in whether the envelope re-attacks on an overlapping note
- claim: in mono/retrigger mode, the amplitude and filter envelopes re-attack on every new note,
  including a note played while a previous one is still held, producing an audible re-attack on each
  note. In legato mode, the envelopes do not re-trigger when a new note overlaps a currently sounding
  one, producing a smooth transition with only the first note of a phrase carrying a full attack; this
  typically requires high sustain levels in the amplitude and filter envelopes to avoid an audible
  level or brightness jump at the transition. Portamento/glide (a smooth pitch slide between the
  previous and new note, at a rate set by a glide-time or glide-rate control) is a related but
  independent parameter: legato controls whether the envelope re-attacks, glide controls how the pitch
  moves between notes, and an instrument can combine them in any of the four combinations.
- source: LEGATO-GLIDE-PEDAGOGY-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: general monophonic and mono-with-legato synthesizer voice architecture, as commonly
  implemented across hardware and software synthesizers.
- limitations: a single pedagogy article; does not state whether glide time is implemented as a fixed
  duration or as a constant rate (time per octave/semitone) on any given instrument, which the guide
  therefore leaves as a product/calibration fact rather than asserting either way.
- inference: none for the mode distinctions themselves.

### SYN-03 Filter key tracking maps keyboard position to filter cutoff, imitating a register-dependent brightness change
- claim: filter key tracking is a control that scales a filter's cutoff frequency by keyboard
  position, typically referenced to a middle point (such as middle C); with positive tracking, notes
  above the reference open the filter and sound brighter, notes below it close the filter and sound
  darker, in proportion to a settable tracking amount; the control can also be inverted or applied to
  other parameters, not only cutoff.
- source: KEYTRACKING-MANUAL-1 (section)
- source_type: manual
- confidence: medium
- scope: this specific synthesizer's documented implementation of key tracking on its filter page;
  the general concept (mapping keyboard position to a synthesis parameter) is common across
  subtractive synthesizers, but exact curve shapes and default reference points are product-specific
  and are excluded from the guide page as calibration-profile facts.
- limitations: manufacturer-manual documentation for one product; read only for the filter-tracking
  page, not for the product's full parameter set.
- inference: the guide's framing of key tracking as "the electronic equivalent of an acoustic
  instrument's register-dependent brightness" is this pack's musical-purpose framing, not a claim the
  manual itself makes explicitly.

### SYN-04 Round-robin sample rotation exists to prevent the "machine-gun" effect of identical repeated samples
- claim: playing the same sampled note repeatedly from one fixed recording produces an audibly
  identical attack, decay and timbre every time, which the ear detects quickly because no acoustic
  source repeats a strike or pluck identically; round-robin sample sets rotate sequentially through
  several recordings of the same note (A, then B, then C, then back to A) to avoid this, and are
  distinct from random selection, which can occasionally repeat the same sample on two consecutive
  triggers.
- source: ROUNDROBIN-EXPLAINER-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: general sample-library and drum-machine round-robin implementation; consistent with, and not
  contradicting, the manual-derived round-robin claim already established for `STRINGS.md` via
  `COMMON_ERRORS.md`.
- limitations: a single technical-explainer source, not a manufacturer manual for a specific product,
  so labelled `sourced`/`inference` on the page rather than `manual-derived`; does not state whether
  round-robin position resets on transport start or loop, which the guide (per `COMMON_ERRORS.md`
  error 11) treats as a general rule regardless.
- inference: none for the core mechanism.

### SYN-05 Vintage-style drum-machine programming deliberately limits velocity variety rather than maximising it
- claim: classic hardware drum machines (commonly cited examples used two or three velocity/accent
  levels per drum rather than continuous velocity, using separate accent lanes instead) produced their
  characteristic feel partly through that constraint; a producer aiming for that vintage character is
  advised to use no more than two or three distinct velocity values per drum voice rather than a wide,
  continuously varied velocity range, and to use swing (which delays off-beat steps by a settable
  amount) or nudged/groove-template timing rather than only velocity to add feel.
- source: DRUM-SEQUENCER-PEDAGOGY-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: step-sequenced drum-machine programming generally, with an explicit vintage-hardware-emulation
  framing; does not claim this constraint applies to every drum-programming context.
- limitations: a single production-pedagogy article; presented as a stylistic recommendation for one
  target sound, not a universal rule, and the guide states it that way rather than as a general drum
  machine limitation.
- inference: the guide's connection of this to `shared/HUMAN_PERFORMANCE_SCHEMA.md`'s
  `realism_target: deliberately_mechanical` (a limited, constrained velocity/timing palette as a
  legitimate aesthetic choice, not a defect) is this pack's synthesis, not a statement the source
  itself makes in those terms.

### SYN-06 Analog oscillator pitch drift is caused chiefly by component temperature sensitivity, and is treated as characterful rather than a defect
- claim: discrete analog oscillator circuitry is sensitive to temperature, and internal component
  temperature (itself affected by the circuit's own operation as well as ambient conditions) causes
  oscillator frequency to drift slowly over time, including drift between multiple oscillators in the
  same instrument or patch; this is treated by synthesizer users and some manufacturers as an inherent,
  often desirable characteristic of analog instruments (contributing to the "warm," slightly detuned
  quality of multi-oscillator analog sounds) rather than purely as a fault, though re-calibration after
  warm-up is still routinely needed for pitch-critical use.
- source: OSC-DRIFT-PEDAGOGY-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: discrete analog oscillator circuits generally; does not extend to digitally controlled
  oscillators (DCOs) or fully digital oscillators, which are drift-stable by design.
- limitations: a single pedagogy/production-technique article, not a circuit-engineering source; a
  targeted attempt to read a manufacturer's own support-article statement that this is expected,
  designed-for behaviour (`ANALOG-DRIFT-MANUAL-1`) failed at two different manufacturers due to access
  restrictions in this session, so the "manufacturers treat this as expected" clause is carried at
  `inference`, not `manual-derived`.
- inference: the "manufacturers treat this as expected" framing and the specific replacement of the
  2.0 page's unnamed "varying a few percent per note" claim with "temperature-driven component drift"
  as the named cause are this pack's synthesis; the underlying physical mechanism (temperature
  sensitivity of analog circuitry) is the source's own claim.

## Corrections to the 2.0 page

1. **The prior page's bare, uncited inference label was removed throughout**, replaced with `inference` per this pass's labelling
   rule; several previously unsourced claims (MPE architecture, key tracking, round-robin purpose) are
   now `sourced` or `specification`-backed instead.
2. **"Envelope and decay times varying a few percent per note" (old page, unnamed magnitude) replaced**
   with a named cause: on an analog instrument, per-note envelope-timing variation is a real
   consequence of the same component-temperature sensitivity that causes pitch drift, not an arbitrary
   percentage to dial in; where no analog cause applies (a purely digital voice), the guide now states
   that "vary a few percent" has no physical justification and should instead be replaced by a
   HUMAN_PERFORMANCE_SCHEMA-named cause (e.g. `metrical_accent`, `velocity_asymmetry`) or omitted.
3. **Grid-synced modulation, previously listed only as a fake-sounding error, is now qualified**: it is
   a legitimate, even correct, choice specifically when `realism_target: deliberately_mechanical` is
   the brief's stated target, per `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4's own statement that
   this target legitimately produces an empty (or here, grid-locked) intentional-imperfections list.
   Ungridded, freely wandering modulation is still the default recommendation outside that target.
4. **Mono/legato/retrigger modes and glide/portamento**, absent from the 2.0 page's performance-
   behaviour coverage, are added and sourced.
5. **Velocity/aftertouch/MPE as expression**, previously covered only as uncited general practice, now cites the
   MIDI Association's own specification directly for MPE's architecture and per-note dimensions.
6. **Sample start and round robins**, previously covered only under Samplers as `manual-derived` from
   one strings-library manual (reused via `COMMON_ERRORS.md`), now also cites a dedicated,
   non-product-specific technical explainer of the round-robin mechanism.
7. **Drum machines and arpeggiators**, absent from the 2.0 page, are added briefly per the brief's
   instruction, sourced for drum-machine velocity/swing programming and left at `inference` for
   arpeggiators, since no dedicated arpeggiator-pedagogy source was read at section depth in this pass.

## Still to verify

- Whether glide/portamento time is conventionally implemented as a fixed duration or a constant rate
  (time per octave) — `LEGATO-GLIDE-PEDAGOGY-1` does not state this either way.
- A manufacturer's own statement (rather than a pedagogy article's) that analog oscillator drift is
  expected, designed-around behaviour: attempted at two manufacturers' support sites, both returned
  HTTP 403 in this session.
- Any measured figure for typical analog drift rate (cents per minute, or similar) or for a
  characteristic envelope-timing variation percentage; no source read here measures either.
- Arpeggiator behaviour and conventions beyond the drum-machine-sequencer source's brief mention; not
  covered at section depth by any source read in this pass.
- Fletcher and Rossing on any acoustics relevant to sampler transient capture or analog circuit
  behaviour; not opened for this work.
