# Synths and Samplers

Electronic sound generators (analog and digital, subtractive, virtual-analog and otherwise) and
samplers, plus the general question of what "organic" means when there is no acoustic original to
imitate. Drum machines and arpeggiators are covered briefly, in prose, since their behaviour is largely
the general synthesizer/sampler behaviour below applied through a sequencer.

> Evidence: six sources read at section depth: the official MIDI Polyphonic Expression specification,
> pedagogy on glide/portamento and mono/legato/retrigger modes, one manufacturer manual page on filter
> key tracking, a technical explainer on round-robin sampling, and pedagogy on drum-machine sequencer
> programming and on analog oscillator drift. A manufacturer statement that oscillator drift is
> expected, designed-around behaviour was targeted at two manufacturers and blocked both times; that
> specific claim stays at `inference`. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`;
> the claims and their limits are recorded in `research/instruments/SYNTHS_AND_SAMPLERS.md`. Read with
> `shared/TUNING_AND_MPE.md` for per-note expression and microtuning, and with
> `shared/HUMAN_PERFORMANCE_SCHEMA.md` for the imperfection-cause vocabulary referenced throughout.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## The rule this file exists for

```text
ORGANIC DOES NOT MEAN ACOUSTIC IMITATION.
It means response and change.
```

A synthesizer that sounds alive is not one that sounds like a violin. It is one that **responds** to
what the player does and **changes** while the note is sounding. Those are two different axes and both
are needed [inference]. A synthesizer part judged by an acoustic-realism standard will be rewritten
into a bad imitation of a string section; the correct standard is the one this file states.

---

## Behaviour cards

### Synthesizer (Subtractive, Virtual-Analog and Digital)

Rows marked "not applicable" describe a real behaviour a physical acoustic instrument has that a
synthesizer, having no fixed body or excitation, simply does not; the evidence label on those rows is
`inference` because the absence itself is a design fact about electronic instruments generally, not a
claim read from a specific source, except where a row states a real electronic-domain behaviour that
replaces the acoustic one (analog drift, filter key tracking), which carries its own source.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Not applicable: no fixed body, string, air column or excitation; sound originates from an electronic oscillator (analog or digital) or, on a virtual-analog/digital instrument, a modelled or computed equivalent. On an analog instrument specifically, oscillator frequency is sensitive to the temperature of the discrete circuitry producing it, which is a real physical-domain behaviour this family does have | sourced: OSC-DRIFT-PEDAGOGY-1 + inference |
| attack_behavior | Fully designed: attack time, shape and velocity sensitivity are all envelope and modulation-routing decisions with no physical constraint forcing any particular shape, unlike a struck, plucked, bowed or blown instrument | inference |
| sustain_behavior | Fully designed: a sustained note can be perfectly static, continuously evolving, or anything between, entirely as a function of the patch's modulation routing; nothing about the instrument forces change the way a bowed or blown instrument's continued excitation does | inference |
| release_behavior | Fully designed: release time and shape are envelope decisions with no physical decay to approximate, unlike an acoustic instrument's resonator | inference |
| dynamic_timbre_change | Not automatic: velocity and aftertouch must be explicitly routed to more than output level (filter cutoff, envelope times, waveshape, layer balance) for playing harder to change timbre, since nothing in the circuit couples loudness and colour the way a physical excitation mechanism does | inference |
| register_character | Not applicable in the acoustic sense (no register is physically weak); the closest analogue is filter key tracking, a designed control that scales cutoff frequency by keyboard position so that higher notes open the filter (brighter) and lower notes close it (darker), imitating the register-dependent brightness change of an acoustic instrument as a deliberate, programmed choice | sourced: KEYTRACKING-MANUAL-1 |
| practical_range | Unbounded by the instrument; bounded in practice only by what the ear resolves and what the arrangement has room for. Register discipline is an arrangement decision, not a physical one, and has to be made rather than inherited | inference |
| tessitura | Not applicable in the acoustic sense; any register is equally available | inference |
| articulation_logic | Fully designed via envelope, modulation and (on many instruments) mono/legato/retrigger mode; there is no physical articulation vocabulary to discover, only one to build | inference |
| phrase_limits | Not applicable: no breath, bow or hand-position constraint bounds a phrase; phrase shaping is entirely a modulation and automation decision | inference |
| transitions | Governed by mono/legato/retrigger mode and by glide/portamento: in legato mode a new note overlapping a held one does not re-trigger the envelopes, producing a smooth transition (typically requiring high envelope sustain levels to avoid a level or brightness jump); in mono/retrigger mode every new note re-attacks the envelopes even when overlapping a held one. Glide/portamento is an independent parameter controlling how fast pitch slides from the previous note to the new one, and can be combined with either mode | sourced: LEGATO-GLIDE-PEDAGOGY-1 |
| repeated_note_behavior | Not automatic: a repeated pitch at a fixed velocity is, by default, perfectly identical on a static patch, which is the electronic equivalent of a machine-gunned sample; making repeated notes differ requires a designed cause (per-note envelope-time variation on an analog voice from the same temperature sensitivity that causes drift, deliberate detuning, or a HUMAN_PERFORMANCE_SCHEMA-named cause such as `metrical_accent` or `velocity_asymmetry`), not an arbitrary "vary a little" instruction | sourced: OSC-DRIFT-PEDAGOGY-1 |
| vibrato | Not physically inherent; commonly implemented via an LFO routed to pitch, controllable in depth and onset (immediate, delayed or growing) exactly like a designed parameter, since there is no finger, breath or hand producing it | inference |
| pitch_instability | On an analog instrument specifically: oscillator frequency drifts slowly with circuit temperature, including drift between multiple oscillators in one patch, which is a real, named physical cause (not an arbitrary randomisation) and is the acoustic-domain source of what is usually called "analog warmth" or detuning between voices. Digitally controlled and fully digital oscillators are drift-stable by design and this row does not apply to them | sourced: OSC-DRIFT-PEDAGOGY-1 |
| resonance | Not applicable in the acoustic sympathetic-resonance sense; a filter's resonance (emphasis at the cutoff frequency) is a designed timbral parameter, not a coupled physical resonance with other strings or a body | inference |
| physical_noise | Not applicable as an incidental mechanism noise; where present (key click on a physical controller, circuit noise floor on an analog instrument), it is either a controller-hardware fact outside this file's scope or a deliberately added/left-in synthesis element, not an unavoidable acoustic byproduct | inference |
| feasibility | Mostly not applicable: no physical body, hand span or breath limits what can be played, so `impossible_voicings` and `limb_or_finger_conflicts` are meaningful only when the brief specifies a performed (physically playable) instrument rather than a pure sound source | inference |
| ensemble_behavior | Not physically constrained; a synthesizer's role in an ensemble (foundation, colour, lead) is entirely an arrangement decision, including how much register space a pad or lead is allowed to occupy | inference |
| recording_behavior | Not applicable as an acoustic capture; a synthesizer's "recording behaviour" is signal-path behaviour instead (analog saturation/nonlinearity in the signal path, stereo width from detuned/spread voices, any modelled amplifier or speaker stage), which is a designed or chosen characteristic, not an incidental one | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Fully designed via the envelope's release stage; a held note and a short note can sound identical or completely different depending entirely on envelope and modulation settings, not on the instrument's own acoustic decay | inference |
| overlap | Governed by mono/legato/retrigger mode (see transitions above): overlap suppresses envelope re-triggering in legato mode and, combined with glide, produces a sliding transition; overlap has no effect in retrigger mode, where every note re-attacks regardless | sourced: LEGATO-GLIDE-PEDAGOGY-1 |
| velocity | Should be routed to more than output level: filter cutoff, envelope times, waveshape and layer balance are all legitimate velocity destinations, and a patch mapping velocity to level only is the electronic equivalent of a sampled instrument with a single dynamic layer | inference |
| continuous_dynamics | Aftertouch (channel or, under MPE, per-note polyphonic pressure) is the primary continuous within-note control; MPE specifically defines per-note Channel Pressure as one of its three per-note dimensions, alongside per-note pitch bend and a third dimension, commonly used for timbre | sourced: MPE-SPEC-2018 |
| expression | The mod wheel is conventionally a macro control, not a fixed vibrato-depth control by default; a continuous expression line should be drawn per phrase on whatever control the patch actually maps, exactly as `dynamic_arc.control` requires elsewhere in this pack | inference |
| articulation_switching | Where an instrument implements distinct articulations (mono/legato/retrigger mode, glide on/off, layer selection), switching is typically a host parameter or a non-sounding control change rather than a keyswitch note, though keyswitch-style implementations exist on some sample-based synth/sampler hybrids | inference |
| round_robins | Not inherent to a pure synthesis voice (a static patch produces bit-identical repeats by default, which is the point of the "repeated_note_behavior" row above); relevant primarily on the sampler side, or on a synth layering recorded transient/noise elements | sourced: ROUNDROBIN-EXPLAINER-1 |
| release_samples | Not applicable in the acoustic sense; the release stage of the amplitude envelope is a fully designed parameter, not a recorded artifact to preserve | inference |
| pedal_or_breath_behavior | Whatever continuous physical input the performer actually has (breath controller, ribbon, expression pedal, mod wheel) should be routed to a musically meaningful destination per phrase, rather than left at a default mapping | inference |
| transition_samples | Not applicable to a pure synthesis voice; a recorded portamento/legato transition sample exists only on a sampler or hybrid instrument, covered under Samplers below | inference |
| mic_or_room_behavior | Not applicable as an acoustic capture; the closest analogues are a modelled amplifier/speaker stage or spatial (stereo-spread, detune-based width) processing, which are designed signal-path choices | inference |
| likely_fake_sounding_errors | Velocity mapped to level only; every voice of a chord identical in tuning and envelope on an analog-modelled patch (which should drift); a held note identical at its end and its beginning; a crescendo made with a linear volume fader instead of a nonlinear stage that changes colour with level; LFOs all synchronised to the grid so every movement lands on a subdivision, when the target is not `deliberately_mechanical`; a pad occupying many octaves because nothing stops it; aftertouch and MPE available and unused; randomisation applied everywhere as a substitute for a decision | inference |
| organic_programming_methods | Map velocity to at least two destinations, one of them timbral. Use aftertouch or MPE where the target can carry it, and say so in the plan if it cannot — named basis: `MPE-SPEC-2018`'s per-note pressure and third-dimension control. On an analog-modelled voice, let multiple oscillators drift and detune slightly and independently — named cause: component-temperature sensitivity, the same mechanism that causes single-oscillator drift. Put a nonlinear stage somewhere in the signal path so dynamics change colour, not only level. Give a held note something that moves, on a period unrelated to the bar length, unless the target is `deliberately_mechanical`, in which case grid-synchronised, unmoving modulation is the correct choice, not a defect — see `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4 on that target producing a legitimately empty imperfection list. Build a macro for the gesture the part needs and automate the macro, not five separate parameters | sourced: MPE-SPEC-2018; OSC-DRIFT-PEDAGOGY-1 + inference |

### Sampler

A sampler's behaviour was decided by whoever recorded and programmed it, and is not discoverable from
the notes alone; the rows below name what must be established before writing for one, and the general
mechanisms (round robins, note-length-driven sample choice) that apply regardless of the specific
library.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Not applicable directly: the source is a stored digital recording of some prior physical or synthetic event; what that event was (an acoustic instrument, a synth patch, a field recording) determines everything downstream, and the sampler's own electronics add no excitation of their own | inference |
| attack_behavior | Fixed by the recording's sample-start point, unless a patch offers a sample-start-offset or transient-detection control; if the sample was not cut exactly at the true onset, every note using it sounds early or late by a fixed amount, which is corrected with playback timing (track delay), not by moving the written notes | sourced: ROUNDROBIN-EXPLAINER-1 |
| sustain_behavior | Fixed by whether the source recording was looped or was a fixed-length one-shot; a looped sustain can be static (an obvious sampler tell if the source was meant to sound continuously alive) or crossfaded between dynamic layers, depending on the patch's design | inference |
| release_behavior | Fixed by whether a separate release sample was recorded and is triggered on note-off; without one, note-off simply stops or fades the currently playing sample, losing whatever release character (mechanism noise, room tail) the source instrument actually has | inference |
| dynamic_timbre_change | Depends entirely on the patch's control model: dynamics may come from discrete velocity-selected recorded layers, from a continuous controller crossfading recorded dynamic layers, or, on a poorly built patch, from a simple level scale with no timbral change at all. This must be established before writing, not assumed | inference |
| register_character | Fixed by what was actually recorded; a sampler cannot produce a register the source was never recorded in, and if a register was recorded thinly (fewer velocity layers, sparser round robins), it will sound less convincing than a well-sampled one even though the pitch is present via stretching | inference |
| practical_range | Bounded by the recorded (or pitch-stretched) note range of the specific patch, which is a calibration-profile fact, not a guide fact | inference |
| tessitura | Follows the source recording's own tessitura if the source was an acoustic instrument; a purely synthetic or sound-design source has no inherited tessitura and the concept does not apply | inference |
| articulation_logic | Fixed by which articulations were actually recorded and how they are selected (separate patches, keyswitches, velocity, or a host parameter); an unavailable articulation should be reported, not silently substituted | inference |
| phrase_limits | Not physically bounded by the sampler itself; if the source was a breath- or bow-limited acoustic instrument, its own phrase limits (covered in that instrument's own family file) still apply musically even though the sampler could technically play forever | inference |
| transitions | Legato/portamento patches are monophonic and require overlapping notes to trigger a recorded transition sample; without overlap, the patch plays two separate attacks instead of the transition the writer intended | inference |
| repeated_note_behavior | Governed by round robins: cycling through several recordings of the same note avoids the audibly identical "machine-gun" repeat that a single fixed recording produces on every repeated trigger; sequential round-robin cycling (A, B, C, back to A) differs from random selection, which can occasionally repeat a sample on consecutive triggers | sourced: ROUNDROBIN-EXPLAINER-1 |
| vibrato | Fixed by what was recorded (a straight-tone or vibrato-tone sample, or separate samples for each) unless the patch implements a synthesized pitch-LFO vibrato layered on top, which is a designed addition, not a captured behaviour | inference |
| pitch_instability | Not present beyond what the source recording itself contains, plus whatever tuning/pitch-stretching artifacts the sampler's own pitch-shifting algorithm introduces at extreme transposition | inference |
| resonance | Captured as part of the recording if the source instrument or room had it; cannot be added after the fact except by a separate convolution/reverb process, which is then a room effect, not the instrument's own resonance | inference |
| physical_noise | Captured as part of the recording (breath, fret, key, mechanism noise) if the source had it and the sampling was close enough to capture it; a patch with this noise removed for "cleanliness" has removed part of what makes the source recognisable | inference |
| feasibility | Inherits the source instrument's physical feasibility limits if the source was a real, playable instrument; a sampler will happily play an "impossible" voicing the source instrument could never produce, which is exactly the trap `COMMON_ERRORS.md` error 6 describes | inference |
| ensemble_behavior | Inherits the source's real ensemble behaviour, including its practical section voice count; stacking more simultaneous notes on a section patch than the recorded section had players multiplies the recording rather than thickening the section, per `COMMON_ERRORS.md` error 14 | inference |
| recording_behavior | The room captured in the original recording is baked in and is not a mix decision available to change later, only to blend with; a sampler's own recorded room and the arrangement's other elements can conflict if they imply different spaces | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Establish, before writing, what a written note's length actually does on this patch: some samplers loop and sustain for the held duration, others simply play a fixed one-shot regardless of note length | inference |
| overlap | Legato/portamento patches are monophonic and need overlap to trigger a recorded transition; this is identical in kind to the requirement already established for bowed and wind instruments elsewhere in this pack | sourced: ROUNDROBIN-EXPLAINER-1 |
| velocity | The first of three control-model questions to answer before writing: does velocity here mean level, timbre, articulation selection, legato-transition-type selection, or nothing at all? | inference |
| continuous_dynamics | The second control-model question: what carries dynamics on a long or looped note — a continuous controller crossfading recorded dynamic layers, a simple volume trim, or velocity alone (with no further change once the note is held)? | inference |
| expression | Where present, typically a volume trim layered on top of whatever carries the primary dynamic, not the same control | inference |
| articulation_switching | Keyswitches, separate patches, a host parameter, or velocity zones, depending on the specific library; must be established, not assumed | inference |
| round_robins | The third control-model question: do round robins exist, how many, and does the host reset the rotation at the start of every bar or transport start (which recreates the machine-gun problem on the beats the listener attends to most, and should not be done)? | sourced: ROUNDROBIN-EXPLAINER-1 |
| release_samples | Where recorded, losing them by gluing notes end to end removes the release, decay and room-tail character on note-off, exactly as `COMMON_ERRORS.md` error 12 describes | inference |
| pedal_or_breath_behavior | Present only if the source instrument had one and it was captured or modelled (e.g. a piano sample's sustain-pedal resonance layer); otherwise not applicable | inference |
| transition_samples | Recorded legato, portamento and slide transitions, where present, are triggered by overlap and by the arriving note's velocity in some libraries, making those velocities articulation choices rather than loudness choices | inference |
| mic_or_room_behavior | Recorded mic positions and room, where offered, are genuine spatial and tonal choices baked into the patch, not a post-hoc mix effect | inference |
| likely_fake_sounding_errors | Assuming a control-model answer instead of checking it (writing dynamics to a control the patch does not read); samples cut from the true onset played without a negative track-delay correction, so notes read late; round robins reset every bar; release samples glued away | sourced: ROUNDROBIN-EXPLAINER-1 |
| organic_programming_methods | Identify the library's actual control model (the three questions above) before writing a single note — named basis: this is a calibration-profile fact, not something inferable from the notes. Use negative track delay to correct a late-cut sample rather than dragging notes earlier. Keep round robins running continuously rather than resetting them per bar. Where the sampler is used for sound design rather than imitation, the synthesizer guidance above (layer, detune, saturate, modulate, let the note change) still applies in full | sourced: ROUNDROBIN-EXPLAINER-1 |

---

## What the instrument is

A synthesizer has no fixed body, no fixed excitation and no physical constraints except the ones its
designer chose [inference]. That is its advantage and its problem: nothing in the instrument forces
variation, so any variation has to be put there deliberately. A sampler is a different problem
entirely: its behaviour was decided by whoever recorded and programmed it, and three questions (what
velocity means, what carries dynamics on long notes, whether round robins exist) have to be answered
from the specific patch before a note is written, not assumed from general synthesizer knowledge
[inference].

## Range and register

Unbounded in principle for a synthesizer, bounded in practice by what the ear resolves and what the
arrangement has room for; register discipline is an arrangement decision, not a physical one
[inference]. Filter key tracking is the one designed control that reintroduces a register-dependent
brightness change, mapping keyboard position to cutoff frequency so higher notes open the filter and
lower notes close it, in imitation of how acoustic instruments naturally brighten with register
[sourced: KEYTRACKING-MANUAL-1]. A sampler's range is whatever was recorded or can be convincingly
pitch-stretched from it, a calibration-profile fact rather than a guide fact [inference].

## Articulation and note transitions

Mono, legato and retrigger modes govern whether a new, overlapping note re-triggers the envelopes: in
retrigger mode every note re-attacks; in legato mode an overlapping note does not, producing a smooth
transition that typically needs high envelope sustain levels to avoid an audible jump [sourced: LEGATO-GLIDE-PEDAGOGY-1]. Glide/portamento is an independent parameter controlling how the pitch moves
between notes, combinable with either mode [sourced: LEGATO-GLIDE-PEDAGOGY-1]. On a sampler, a
legato/portamento patch is monophonic and needs overlapping notes to trigger a recorded transition
sample, exactly as on a sampled bowed or wind instrument elsewhere in this pack [sourced: ROUNDROBIN-EXPLAINER-1].

## Physical constraints

```text
synthesizer: none inherent; impossible_voicings and limb_or_finger_conflicts are meaningful
  only when the brief specifies a performed, physically playable instrument
sampler: inherits the source instrument's real physical constraints when the source was a
  real, playable instrument; otherwise none inherent
```

[inference]

## Phrase behaviour

A synthesizer's phrases are bounded by nothing physical; phrase shaping (a swell, a filter opening
across a held chord, an LFO-driven evolution) is entirely a modulation and automation decision
[inference]. A sampler inherits its source's real phrase limits musically (a sampled wind instrument
still implies breath, even though the sampler itself could sustain forever), which is covered in that
source instrument's own family file rather than repeated here [inference].

## Ensemble behaviour

A synthesizer's ensemble role (foundation, colour, lead, and how much register space it is allowed to
occupy) is entirely an arrangement decision with no physical constraint behind it [inference]. A
sampled section patch inherits the source recording's real, fixed voice count, and stacking more
simultaneous notes than that count multiplies the recording rather than thickening the section, per
`COMMON_ERRORS.md` error 14 [inference].

## Recording behaviour

A synthesizer's "recording behaviour" is really signal-path behaviour: analog or modelled saturation
and nonlinearity, stereo width built from detuned or spread voices, and any modelled amplifier or
speaker stage are designed, chosen characteristics rather than incidental acoustic ones [inference]. A
sampler's recorded room and mic position, where offered, are baked into the patch and are a genuine
spatial choice, not a later mix decision [inference].

## Programming it: the control model

Product-specific controller assignments, exact drift or detune amounts, and any single library's
particular velocity-to-articulation mapping are calibration-profile facts and belong there, not here
[inference].

```text
synthesizer:
  response:
    velocity: should reach more than level -- filter cutoff, envelope times, waveshape, layer balance
    aftertouch: channel or polyphonic; a second continuous dimension inside a held note
    mpe: per-note pitch, pressure and a third (commonly timbre) dimension, so one voice in a
      chord can move independently of the others
    mod_wheel: a macro by default, not a fixed vibrato-depth control
    expression: a continuous line, drawn per phrase, on whatever control the patch actually maps
  change:
    per_voice_drift: independent, slow detuning between oscillators, most legitimately on an
      analog-modelled voice, caused by component-temperature sensitivity
    envelope_variation: per-note variation in attack/decay times, with a named cause rather than a
      flat percentage
    nonlinear_stage: somewhere in the signal path, so a crescendo changes colour, not only level
    evolving_timbre: a held note should change across its length unless the target is
      deliberately_mechanical
    macro_gestures: one control moving several parameters at once, the synthesizer's equivalent of a
      single physical gesture changing several things about an acoustic instrument at once
sampler:
  control_model_questions:
    - what does velocity mean here: level, timbre, articulation selection, transition-type
      selection, or nothing at all?
    - what carries dynamics on long or looped notes: a continuous crossfade, a volume trim, or
      velocity alone?
    - do round robins exist, how many, and does the host reset them?
  legato_patches: monophonic; need overlap to trigger a recorded transition
  sample_start: a late-cut sample is corrected with negative track delay, not by dragging notes
    earlier
```

[sourced: MPE-SPEC-2018; OSC-DRIFT-PEDAGOGY-1; KEYTRACKING-MANUAL-1; LEGATO-GLIDE-PEDAGOGY-1; ROUNDROBIN-EXPLAINER-1]

## Programming it: what makes it sound real

- Map velocity to at least two destinations, one of them timbral, never to level alone [inference].
- Use aftertouch or MPE where the target can carry it, and state in the plan when it cannot [sourced: MPE-SPEC-2018].
- On an analog-modelled voice, let oscillators drift and detune slightly and independently, naming
  component-temperature sensitivity as the cause rather than an arbitrary amount [sourced: OSC-DRIFT-PEDAGOGY-1].
- Put a nonlinear stage somewhere in the path so dynamics change colour, not only level [inference].
- Give a sustained note something that moves, on a period unrelated to the bar length, unless the
  target is `deliberately_mechanical`, in which case unmoving, grid-synchronised modulation is the
  correct choice, not a defect [inference].
- Build a macro for the gesture the part needs and automate the macro, not five separate parameters
  [inference].
- On a sampler, answer the three control-model questions before writing a note, and correct a
  late-cut sample with negative track delay rather than by moving the written notes [sourced: ROUNDROBIN-EXPLAINER-1].
- Keep round robins running continuously; do not reset them at the start of every bar [sourced: ROUNDROBIN-EXPLAINER-1].

## What sounds fake here

The general list is in `COMMON_ERRORS.md`, and most of it applies, but the family-specific failure is
single and specific:

> A static preset with one envelope and no modulation is the electronic equivalent of a machine-gunned
> sample.

Around it:

- velocity mapped to level only [inference];
- every voice of a chord identical in tuning and envelope on a patch that should be drifting
  [sourced: OSC-DRIFT-PEDAGOGY-1];
- a held note the same at its end as at its beginning [inference];
- a crescendo made with a linear volume fader through a signal path with no nonlinearity [inference];
- LFOs all synchronised to the grid so every movement lands on a subdivision, when the target is not
  `deliberately_mechanical` [inference];
- a pad occupying many octaves because nothing stops it [inference];
- aftertouch and MPE available and unused [sourced: MPE-SPEC-2018];
- randomisation applied everywhere as a substitute for a decision, which is not organic, it is noise
  [inference];
- on a sampler, a control-model assumption instead of a check, and round robins reset every bar
  [sourced: ROUNDROBIN-EXPLAINER-1].

Note the second-to-last item. **Organic is not random.** Random modulation with no cause is a bug,
exactly as in `shared/HUMAN_PERFORMANCE_SCHEMA.md`, and `realism_target: deliberately_mechanical` is a
legitimate choice that should produce a genuinely static, even grid-locked part, not a slightly wobbly
one [inference].

## What the Performance Director needs from this file

- **The realism standard for a synthesizer is response and change, not acoustic plausibility.** A
  synthesizer part should not be flagged as unplayable by a human unless the brief specifically asked
  for a performed instrument.
- Physical feasibility mostly does not apply to a synthesizer voice. `impossible_voicings` and
  `limb_or_finger_conflicts` are meaningful only when the brief specifies a performed instrument. A
  sampler inherits its source's real feasibility limits when that source was a real, playable
  instrument.
- `dynamic_arc.control` should be a control the patch actually maps (velocity, aftertouch, MPE
  pressure, a mod-wheel macro), and the plan should name it explicitly.
- Per-note expression requirements go to `shared/TUNING_AND_MPE.md`; the DAW adapter reports in
  `daw_capabilities` whether it can carry MPE and tuning at all.
- For a sampler part, the plan should carry the three control-model answers (velocity meaning, long-
  note dynamics control, round-robin presence) as calibration facts, not guesses.
- `drift_1f`, `pitch_drift` and `note_length_variation` are the HUMAN_PERFORMANCE_SCHEMA-recognised
  imperfection causes that transfer most directly to this family; on an analog-modelled voice,
  component-temperature drift is the named physical cause behind both pitch and envelope-timing
  variation. `realism_target: deliberately_mechanical` legitimately produces grid-synced modulation and
  an empty imperfection list; this is a correct output for that target, not a missed check.

## Sources and what to verify

- **To verify**: a manufacturer's own statement that analog oscillator drift is expected, designed-
  around behaviour, rather than only a third-party pedagogy source's characterization of it; attempted
  at two manufacturers' support sites, both returned HTTP 403 in this session.
- **To verify**: whether glide/portamento time is conventionally a fixed duration or a constant rate
  (time per octave); not stated either way by the source read here.
- **To verify**: arpeggiator conventions and behaviour beyond a brief drum-sequencer mention; not
  covered at section depth by any source read in this pass.
- **Not available**: any measured figure for typical analog drift rate or for a characteristic per-note
  envelope-timing variation; both are taste decisions, and a calibration render is the only way to turn
  them into numbers for a given instrument.
- Fletcher and Rossing was not opened for this work and is not obviously the right source for this
  family in any case, since little here is acoustic in the traditional sense; a circuit-design or DSP
  reference would be the more useful target for a future pass on analog drift specifically.
