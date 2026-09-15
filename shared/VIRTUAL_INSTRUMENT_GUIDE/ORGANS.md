# Organs

Two unrelated instruments that share a keyboard and a name: the pipe organ, and the electromechanical
drawbar (tonewheel) organ.

> Evidence: eight sources read at section depth, covering tracker-action touch, pedal technique, the
> swell box, stop registration, rotary-speaker acoustics, tonewheel generation and electronics, drawbar
> additive synthesis, and single-trigger percussion. Audsley's *Art of Organ-Building* was targeted per
> the research brief but could not be opened in this session (see the research file); claims that would
> rest on it stay `to-verify`. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; the
> claims and their limits are recorded in `research/instruments/ORGANS.md`.

Cross-family failures are in `COMMON_ERRORS.md`. One of them, error 3, applies here in a qualified
way: uniform velocity is broadly correct on both of these instruments, because neither has a
loudness-sensitive keyboard, but a tracker-action pipe organ's touch does still shape attack
character (see the pipe organ's `attack_behavior` row below), so "no velocity at all" is too strong.

---

## Behaviour cards

### Pipe Organ

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Ranks of pipes fed by a wind supply, selected by stops and played from two or more manuals plus a pedalboard; each stop is a complete rank across the keyboard, and the set of engaged stops is the registration | inference |
| attack_behavior | The key is a binary on/off for loudness, but on a mechanically linked (tracker) action, the player's touch directly controls pallet-opening speed: a fast attack opens the pallet abruptly and produces a more pronounced "chiff," a gentler attack smooths it. This is a real, graded attack-character control, not a loudness control, and it does not exist on electric or pneumatic actions, which decouple the finger from the pallet | sourced: TRACKERACTION-PEDAGOGY-1 |
| sustain_behavior | Sustains at a fixed level for as long as the key is held and wind is supplied; unlike a struck or plucked instrument, there is no decay to manage during the note | inference |
| release_behavior | The pipe stops speaking promptly when the key is released, but the room the organ lives in keeps the sound going as reverberant tail; the release is audible and is part of the instrument's normal sound, not a defect | inference |
| dynamic_timbre_change | There is no per-note dynamic control; loudness and colour both change only through registration (adding or removing stops) and, on enclosed divisions, through the swell box, and in both cases loudness and timbre change together, not independently | sourced: SWELLBOX-TUTORIAL-1 |
| register_character | Different stop families characteristically differ in colour and role: flute-family stops are dark and fundamental-heavy, typically supplying foundational weight rather than brightness; principal and reed stops supply more upper harmonic content. No single "bright register / weak register" map applies the way it does on a wind instrument, since colour is a registration choice, not a fixed property of a keyboard position | sourced: FLUTE-STOPS-REGISTRATION-1 |
| practical_range | Manuals typically span about five octaves; the pedalboard covers roughly two and a half octaves from the bottom. Sounding range is far wider than the keyboard because of footages: a stop labelled by pipe length sounds at a fixed transposing relationship to the key (16' an octave below, 8' at the key's pitch, 4' an octave above, 2' two octaves above, and mixtures adding several ranks at once, heard as brightness rather than as distinct pitches) | inference |
| tessitura | No register is avoided for tone-quality reasons the way a wind instrument's extremes are; registration is chosen for the musical role of a passage, not because a particular keyboard position is weak | inference |
| articulation_logic | Articulation is entirely note length and note placement, since there is no touch-sensitive loudness and (on non-tracker actions) no touch-sensitive attack either. This is not a limitation to work around; it is the technique | inference |
| phrase_limits | Bounded by hand position across manuals, by the two feet on the pedalboard, and by how often registration can realistically change (registration changes need a free hand or a foot on a preset and happen between phrases, not within one), not by breath | inference |
| transitions | No sampled-legato-style transition exists; connection between notes is made by exact note-length and overlap decisions, since there is no attack strength to blend | inference |
| repeated_note_behavior | A repeated note has no attack-strength variation to distinguish it (except the touch-driven chiff variation on a tracker action); detaching repeated notes clearly is the main way to keep them distinct, since there is no other attack cue | inference |
| vibrato | Not a native mechanism; some instruments and most drawbar-organ-style built-in effects add an electronic or mechanical tremulant (see the tremulant note under Ensemble/Recording), which is a wind- or circuit-level effect applied to a whole division, not a per-note player gesture | inference |
| pitch_instability | The wind supply on many instruments is not perfectly steady, and heavy chords can pull the wind slightly, producing a small, real pitch and level movement; this instability is part of the sound rather than a flaw | to-verify: a direct acoustic measurement of wind-supply pitch pull under load, in Fletcher and Rossing, not opened for this work |
| resonance | The room is not separable from the instrument: pipe organs are built for and voiced in large reverberant spaces, and a recording or patch that omits the room misrepresents the instrument | inference |
| physical_noise | Mechanism noise (tracker/action clatter, wind noise, stop-action clicks when registration changes) is audible at close range and is part of a real recorded organ's character | inference |
| feasibility | Two hands, which may be on different manuals, and two feet on the pedalboard; registration changes need a free hand or a foot on a preset mechanism, so a change mid-phrase competes with playing | inference |
| ensemble_behavior | A pipe organ is normally a solo/self-sufficient instrument (covering its own bass, harmony and melody, like a piano) rather than a typical ensemble blend partner; where it does accompany, registration is chosen to sit under or answer the other forces rather than to blend homogeneously the way orchestral strings blend with each other | inference |
| recording_behavior | The room is the dominant recording variable: the same instrument recorded closer foregrounds mechanism and wind noise, recorded further back is dominated by the building's reverberation; there is no "close mic'd, dry" version of a real pipe organ the way there is of a piano | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | The primary and near-only expressive parameter available; note length and placement carry articulation entirely | inference |
| overlap | Not applicable in the sampled-legato-transition sense; there is no recorded transition to trigger, since the instrument has no attack-strength-driven articulation vocabulary to select between | inference |
| velocity | Should be ignored for dynamics; on a tracker-modelled instrument it may legitimately drive a small attack-character (chiff) variation, which is a documented, player-controllable effect, not a red herring | sourced: TRACKERACTION-PEDAGOGY-1 |
| continuous_dynamics | Not carried by a crossfaded dynamic layer the way a bowed or blown instrument's is; the only continuous, graded dynamic control is the swell pedal on enclosed divisions | sourced: SWELLBOX-TUTORIAL-1 |
| expression | The swell pedal functions as the expression control on enclosed divisions, changing loudness and brightness together, not as a separate trim | sourced: SWELLBOX-TUTORIAL-1 |
| articulation_switching | Registration (stop selection) functions as the switch that changes colour and loudness together; it is normally changed between phrases or sections, via separate patches, keyswitches or registration presets, not continuously | inference |
| round_robins | Not meaningfully applicable: there is no per-strike sample variation to rotate through, since a sustained pipe tone is not a discrete transient the way a struck or plucked note is | inference |
| release_samples | The release is audible (pipe stop plus room tail) and should be preserved with a real note-off; gluing notes together removes it | inference |
| pedal_or_breath_behavior | Not applicable to breath; the swell pedal (a continuous foot control) is the closest analogue and should be automated as a continuous line, not a stepped switch | sourced: SWELLBOX-TUTORIAL-1 |
| transition_samples | Not applicable; no recorded legato transition exists to trigger | inference |
| mic_or_room_behavior | Room is not separable from the instrument's identity; treat a recorded patch's room as part of the sound, not a mix decision layered on afterward | inference |
| likely_fake_sounding_errors | A velocity curve written into a part for an instrument with no loudness-sensitive keyboard, which does nothing on a real instrument and something wrong on some sampled patches; uniform note lengths, which removes the entire articulation vocabulary; registration changing note by note instead of between phrases; the swell pedal used as a stepped switch instead of a continuous line; notes glued end to end, losing the audible release | inference |
| organic_programming_methods | Vary note length constantly, since that is the primary phrasing device — named cause: `note_length_variation`. Detach repeated notes clearly, since there is no attack-strength cue to distinguish them otherwise. Use the swell pedal as a continuous line, not a step. Change registration at structural points, with time allowed, and treat it as a placed event in the plan, not a continuous curve. Let the room ring: do not truncate the recorded or modelled tail | inference |

### Drawbar Organ

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Rotating tonewheels driven by a constant-speed motor through fixed mechanical gear ratios generate the raw tones; drawbars mix a fixed set of these tones, and the result is normally amplified and heard through a rotating speaker | sourced: TONEWHEEL-TECHNICAL-1 |
| attack_behavior | The key is a binary on/off for loudness, with no touch-driven attack-character control at all (unlike a tracker pipe organ); an optional built-in percussion circuit adds a short decaying extra harmonic to the attack, but only on a single-trigger basis (see repeated_note_behavior) | sourced: PERCUSSION-RETRIGGER-1 |
| sustain_behavior | Sustains at a fixed level for as long as the key is held, since the tonewheel generator runs continuously and the key simply connects its output to the mix | inference |
| release_behavior | The tone stops promptly on key release; key contacts produce an audible "key click" transient on both note-on and note-off, which is a defining part of the instrument's sound, not a fault to remove | sourced: TONEWHEEL-TECHNICAL-1 |
| dynamic_timbre_change | No per-note dynamic control; loudness and colour come from drawbar registration, from driving the amplifier harder (which adds audible overdrive as part of the normal dynamic range), and from the expression pedal | inference |
| register_character | Even, additive-synthesis-built colour across the range; the instrument does not have acoustically weak or strong registers the way a wind or bowed instrument does, since every note is generated the same electromechanical way | inference |
| practical_range | Drawbars are labelled by footage in the same transposing system as the pipe organ; the "16-foot" drawbar is a sub-octave (one octave below the fundamental 8-foot drawbar), not a harmonic of it, and each drawbar corresponds to a specific harmonic-number relationship to the fundamental rather than an arbitrary per-drawbar assignment | sourced: TONEWHEEL-TECHNICAL-1 |
| tessitura | Usable evenly across the range for the same additive-mixing reason given under register_character | inference |
| articulation_logic | As with the pipe organ, articulation is entirely note length and placement; the instrument adds phrasing-dependent percussion behaviour on top of that (see repeated_note_behavior) | sourced: PERCUSSION-RETRIGGER-1 |
| phrase_limits | Bounded by hand position, by how the built-in percussion behaves across a phrase (it fires once per phrase, not per note, unless the player deliberately releases all keys), and by rotary-speaker speed changes, which are placed at musical points rather than switched arbitrarily | sourced: PERCUSSION-RETRIGGER-1 |
| transitions | No sampled-legato transition exists; glissandi and pitch smears between notes are idiomatic on this instrument in a way they are not on most keyboards, achievable by physically sliding across the keys | inference |
| repeated_note_behavior | Single-trigger percussion re-triggers only after every key has been released; in a legato/overlapping passage it sounds once, on the first note of the phrase, and not again until the player releases all keys, while the same passage played fully detached gets the percussion attack on every note. Which behaviour is wanted is a musical decision that has to be made deliberately, since a sequencer will produce one or the other by accident depending only on note overlap | sourced: PERCUSSION-RETRIGGER-1 |
| vibrato | The instrument's built-in vibrato/chorus is a scanner-type circuit effect applied to the whole output, set for a passage, not a per-note player gesture the way a string or wind player's vibrato is | inference |
| pitch_instability | Tonewheel-generated pitches are a tempered approximation of 12-tone equal temperament, not exact: fixed integer gear ratios cannot reproduce equal temperament exactly, so specific note classes are measurably (if very slightly, well under a semitone) off from a theoretically perfect equal-tempered reference. This is a fixed, tiny, per-note-class deviation, not a wandering instability | sourced: TONEWHEEL-TECHNICAL-1 |
| resonance | Not applicable in the acoustic-instrument sense; there is no string, air column or resonant body, only electrical mixing of generator outputs, so any "resonance" character comes from the amplifier, cabinet and rotary speaker downstream, not from the tone generation itself | inference |
| physical_noise | Key-contact click on note-on and note-off is audible and is a defining, deliberately preserved part of the instrument's identity | sourced: TONEWHEEL-TECHNICAL-1 |
| feasibility | Two hands, potentially across two manuals; registration (drawbar) changes are physically made with the same hands that are playing, so a mid-phrase drawbar change competes with playing exactly as a pipe organ's registration change does | inference |
| ensemble_behavior | Typically a self-sufficient solo/comping voice (melody, harmony and bass together), similarly to piano; its identity in an ensemble is defined largely by the chosen drawbar registration and by the rotary speaker's state, both of which are held or changed deliberately rather than varied constantly | inference |
| recording_behavior | Normally captured through (or as a direct model of) the rotary speaker system, whose moving horn and drum/rotor make stereo width, movement and speed state part of the recorded identity, not an effect added afterward; a static, one-speed capture misrepresents an instrument whose recorded character is built on that movement | sourced: ROTARY-SPEAKER-TECH-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | The primary phrasing parameter, and it also determines percussion behaviour (see repeated_note_behavior above): note overlap versus detachment changes whether percussion fires on every note or once per phrase | sourced: PERCUSSION-RETRIGGER-1 |
| overlap | Overlap is not needed to trigger a legato transition (there isn't one), but it directly controls whether single-trigger percussion re-fires; overlapping notes suppress repeated percussion, detached notes restore it on every attack | sourced: PERCUSSION-RETRIGGER-1 |
| velocity | Should be ignored entirely; the instrument has no touch-sensitive loudness or attack-character control at all, unlike the tracker pipe organ | inference |
| continuous_dynamics | Not carried by a crossfaded dynamic layer; dynamics come from drawbar positions, amplifier drive, and the expression pedal, none of which is a per-note velocity value | inference |
| expression | The expression pedal is a genuine continuous control here, analogous to the pipe organ's swell pedal, and should be automated as a continuous line | inference |
| articulation_switching | Drawbar registration functions as the main timbre switch and, unlike the pipe organ, is often changed by the player while playing rather than only between phrases, since there is no wind-supply or stop-mechanism delay to work around | sourced: TONEWHEEL-SYNTHESIS-1 |
| round_robins | Not meaningfully applicable to the sustained tone generation itself; may matter for a sampled/modelled key-click layer, which is a short transient with the same repeated-identical-sample risk as any other percussive click source | inference |
| release_samples | Key-click on note-off is real and audible and should not be removed for tidiness | sourced: TONEWHEEL-TECHNICAL-1 |
| pedal_or_breath_behavior | The expression pedal (loudness/amplifier drive) is the closest analogue to a breath or swell control and should be a continuous automation target | inference |
| transition_samples | Not applicable for pitch (no recorded legato transition), but glissando/smear playing is idiomatic and, where modelled, should be supported as a genuine gliding gesture, not approximated by fast individual notes | inference |
| mic_or_room_behavior | The rotary speaker's movement is itself a "room behaviour" in the sense that it is a moving acoustic environment, not a static mic position; a modelled or recorded patch that omits the horn/drum speed and acceleration misses a large part of the instrument's identity | sourced: ROTARY-SPEAKER-TECH-1 |
| likely_fake_sounding_errors | A velocity curve written into a part for an instrument with no velocity at all; uniform note lengths, removing the only articulation vocabulary; a registration held static for an entire track with no player-driven changes; percussion firing on every note of a legato passage or not firing at all, regardless of phrasing; key click gated away for tidiness; a rotary speaker fixed at one speed for a whole track with no transition; notes glued end to end, losing the key-click release | inference |
| organic_programming_methods | Decide the drawbar registration deliberately and hold it, or change it as a placed event while playing, since that is how the instrument is actually played — named cause: this is a direct performer-controlled parameter, not incidental variation. Write overlapping and detached passages on purpose, because percussion behaviour depends on note overlap, not on a setting. Place rotary-speed changes at phrase boundaries and let them ramp with the asymmetric horn/drum acceleration, rather than switching instantly. Use the expression pedal as a continuous line. Play glissandi and smears where idiomatic | sourced: PERCUSSION-RETRIGGER-1; ROTARY-SPEAKER-TECH-1 |

---

## What the instrument is

Two instruments share a keyboard and a naming tradition and little else. A pipe organ sounds ranks of
pipes fed by a wind supply and selected by stops [inference]. A drawbar organ generates tone
electromechanically from rotating tonewheels and mixes it additively through drawbars, normally heard
through a rotating speaker [sourced: TONEWHEEL-TECHNICAL-1]. **Neither has a touch-sensitive loudness
control**: a key is on or off, and everything a pianist does with velocity, an organist does instead
with which stops or drawbars are engaged, how long a note is held, and when it starts and stops
[inference]. That is not a limitation to program around; it is the technique both instruments are
built on. The one qualification worth keeping precise: a mechanically linked (tracker) pipe-organ
action does give the player real, graded control over attack character through pallet-opening speed,
even though it still gives no control over loudness [sourced: TRACKERACTION-PEDAGOGY-1].

## Range and register

A pipe organ's manuals typically span about five octaves and its pedalboard roughly two and a half
from the bottom, with sounding range far wider than the keyboard because of footages, the organ's
transposition system: a stop labelled by pipe length sounds at a fixed relationship to the key played
[inference]. A drawbar organ's footages work the same way but are generated electromechanically: the
16-foot drawbar is a sub-octave, not a harmonic, of the 8-foot fundamental, and the tempered gearing
that produces every drawbar's pitch is a close but inexact approximation of equal temperament
[sourced: TONEWHEEL-TECHNICAL-1]. Neither instrument has acoustically weak registers the way a wind
instrument does; colour is a registration choice, and flute-family and low-pitched stops darken a
pipe-organ registration rather than brightening it [sourced: FLUTE-STOPS-REGISTRATION-1].

## Articulation and note transitions

On both instruments, articulation is almost entirely note length and note placement, since neither has
a touch-sensitive attack the piano-family instruments have [inference]. On the drawbar organ this
interacts directly with the single-trigger percussion effect: overlapping notes suppress repeated
percussion attacks, detached notes restore them on every note, so a phrase's overlap decision is also
a timbre decision [sourced: PERCUSSION-RETRIGGER-1]. Neither instrument has a sampled-legato-style
transition to trigger; the drawbar organ's idiomatic glissando/smear playing is a genuine physical
slide across the keys, not a recorded transition sample [inference].

## Physical constraints

```text
pipe organ: two hands (possibly on different manuals), two feet on the pedalboard;
  registration changes need a free hand or a foot on a preset
drawbar organ: two hands, potentially across two manuals; drawbar changes are made
  with the playing hands themselves, competing directly with playing
```

[inference]

## Phrase behaviour

Pipe-organ phrases are bounded by hand position across manuals, by the two feet on the pedalboard, and
by how often registration can realistically change, since a change needs a free hand or a foot on a
preset and happens between phrases rather than within one [inference]. Pedal lines are not uniformly
slow: heel-and-toe technique lets a pedalist play genuinely fast alternating pedal lines, which the
2.0 page understated [sourced: PEDAL-TECHNIQUE-1]. Drawbar-organ phrasing adds the percussion-retrigger
constraint (see Articulation above) and, where a rotary speaker is used, treats a speed change as a
placed event with real acceleration time, not an instant switch [sourced: PERCUSSION-RETRIGGER-1; ROTARY-SPEAKER-TECH-1].

## Ensemble behaviour

Both instruments are normally self-sufficient solo or comping voices, covering their own bass, harmony
and melody much as a piano does, rather than blending homogeneously into a section the way orchestral
strings blend with each other [inference]. Where a pipe organ accompanies other forces, registration
is chosen to sit under or answer them rather than to match their colour [inference]. A drawbar organ's
ensemble identity is defined largely by its held (or deliberately changed) drawbar registration and by
the rotary speaker's state, both chosen decisions rather than incidental variation [inference].

## Recording behaviour

A pipe organ's room is not separable from its identity: the building's reverberation is part of the
instrument, and mic distance trades mechanism/wind noise for room dominance rather than offering a
"dry" version of the instrument the way close-miking a piano does [inference]. A drawbar organ is
normally captured through, or modelled from, its rotary speaker, whose moving horn and drum/rotor make
stereo width, motion and speed state part of the recorded sound; a static, one-speed capture
misrepresents an instrument whose identity is built on that movement [sourced: ROTARY-SPEAKER-TECH-1].

## Programming it: the control model

Controller numbers, exact drawbar-to-harmonic mapping tables for a specific product, and rotary-speed
ramp-time figures are product facts and belong in the calibration profile, not here [inference].

```yaml
pipe_organ:
  velocity: ignored for dynamics; may legitimately drive a small attack-character (chiff) variation
    on a tracker-modelled instrument only
  dynamics: stop selection, plus a continuous swell-pedal control on enclosed divisions
  articulation: note length and placement only
  registration_changes: between phrases, with time allowed; often separate patches or keyswitches
  release: audible; give notes real note-offs
  room: part of the instrument, already present in a well-recorded or well-modelled patch
drawbar_organ:
  velocity: ignored entirely
  dynamics: drawbar positions, amplifier drive, expression pedal
  percussion: single-trigger; depends on note overlap, so it depends on phrasing
  key_click: present on note-on and note-off; do not remove it
  rotary_speed: a performance automation event with modelled acceleration, not a static setting
  overdrive: part of the normal dynamic range; louder is dirtier
```

[sourced: TRACKERACTION-PEDAGOGY-1; SWELLBOX-TUTORIAL-1; PERCUSSION-RETRIGGER-1; TONEWHEEL-TECHNICAL-1; ROTARY-SPEAKER-TECH-1]

## Programming it: what makes it sound real

- Pipe organ: vary note length constantly, since that is the phrasing device; detach repeated notes
  clearly; use the swell pedal as a continuous line; change registration at structural points; let the
  room ring [sourced: SWELLBOX-TUTORIAL-1].
- Pipe organ: where the target is modelled as a tracker action, let attack speed (touch) drive a small
  chiff variation, rather than mapping velocity to loudness [sourced: TRACKERACTION-PEDAGOGY-1].
- Pipe organ: write pedal lines with real speed where the music calls for it; heel-and-toe technique
  makes fast alternating pedal lines idiomatic, not exceptional [sourced: PEDAL-TECHNIQUE-1].
- Drawbar organ: decide the registration and keep it, or move it deliberately while playing, since
  that is how the instrument is actually played [sourced: TONEWHEEL-SYNTHESIS-1].
- Drawbar organ: write overlapping and detached passages on purpose, because percussion behaviour
  depends on note overlap, not on a setting [sourced: PERCUSSION-RETRIGGER-1].
- Drawbar organ: place rotary-speed changes at phrase boundaries and let them ramp, with the horn
  reaching its new speed well before the heavier drum does [sourced: ROTARY-SPEAKER-TECH-1].
- Drawbar organ: play glissandi and smears, which are idiomatic here and impossible on most keyboards;
  use the expression pedal as a continuous line [inference].

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Organ-specific tells:

- a velocity curve written into a part for an instrument with no velocity, which does nothing on a
  real patch and something wrong on some sampled ones [inference];
- uniform note lengths, which removes the entire articulation vocabulary on both instruments
  [inference];
- registration changing note by note instead of at structural points [inference];
- a swell pedal used as a stepped switch rather than a continuous line [sourced: SWELLBOX-TUTORIAL-1];
- assuming adding stops always brightens the sound, when 16-foot and flute stops characteristically
  darken it [sourced: FLUTE-STOPS-REGISTRATION-1];
- a drawbar-organ patch with percussion on every note regardless of overlap, or off entirely [sourced: PERCUSSION-RETRIGGER-1];
- key click gated away for tidiness, which is error 7 in `COMMON_ERRORS.md` [sourced: TONEWHEEL-TECHNICAL-1];
- a rotary speaker held at one fixed speed for a whole track, with no transition [sourced: ROTARY-SPEAKER-TECH-1];
- notes glued end to end, so the audible release disappears, which is error 12 in `COMMON_ERRORS.md`
  [inference].

## What the Performance Director needs from this file

- **Velocity is not a dynamic control on either instrument.** `dynamic_arc.control` must be the swell
  or expression pedal, or registration, and never velocity; the one narrow exception is a
  tracker-modelled pipe organ's attack-character (chiff) response to touch, which is not a dynamic
  control either.
- `note_length_variation` is the primary expressive parameter on both instruments, not a secondary one.
- `limb_or_finger_conflicts`: two hands (possibly across manuals) plus two feet on a pedalboard for the
  pipe organ; two hands, sometimes across manuals, for the drawbar organ, with registration changes
  competing directly with playing hands on both.
- Registration changes and rotary-speed changes are **events in the plan**, with time allowed for both.
- Percussion single-trigger behaviour on the drawbar organ is a phrasing constraint the Director should
  state explicitly, because the MIDI Builder's note-overlap decision changes the timbre, not just the
  rhythm.
- Pedal-line tempo is a real feasibility consideration on the pipe organ, and heel-and-toe technique
  should be assumed rather than a uniformly slow default.

## Sources and what to verify

- **To verify**: Audsley, *The Art of Organ-Building*, was targeted per the research brief; the
  archive.org text view returned only viewer scaffolding and the direct-download endpoint required
  authentication this session lacks. Registration conventions and footage nomenclature beyond what is
  sourced above should be checked against it directly.
- **To verify**: pipe-speech transients and wind-supply pitch/level instability under load, in
  Fletcher and Rossing, *The Physics of Musical Instruments*. Not opened for this work.
- **To verify**: registration and writing-convention detail in Adler, *The Study of Orchestration*.
  Not opened.
- **Not available**: a measured rotary-speaker horn/drum acceleration time in milliseconds; treat any
  figure as a practitioner value, or calibrate.
- **Not available**: a quantified chiff-amplitude-versus-pallet-opening-speed curve for tracker
  actions; `TRACKERACTION-PEDAGOGY-1` states the relationship qualitatively only.
