# Field Test: The Workshop Built in Vital

On 2026-10-22 an agent built this workshop's three recipes, the "same role, three mechanisms" challenge (three chorus leads) and the capstone (an evolving bass, a layered pad, a transition hit) as real Vital patches. It wrote each patch into a DAW set's plugin state, rendered the set, and ran `PATCH_STANDARD.md`'s test protocol by measurement. That route is not shipped with this skill (see `AUTOMATION_GUIDE.md`). This file records what the run measured. It does not record what anyone heard: listening results belong to the listener.

## How it was run

- Vital 1.0.7 (AU) in Ableton Live 12, 48 kHz, 120 BPM. Nine patches, each also rendered dry (effects off) and with every macro at half and full travel. Each recipe's counterpart from an earlier patch set played the same MIDI for a blind A/B, matched to within 0.1 dB of loudness.
- Four renders. Between renders, each measured symptom got one change (lesson 8), and a change that fixed nothing was reverted.

## Vital units it measured

Measured on one setup and one Vital version. Recheck them on another.

- **Oscillator level is quadratic:** amplitude is about level squared, and a modulation route acts before the square. A velocity route of 0.55 into a level of 0 reached only about -11 dB at velocity 120. A route of 0.8 gave about -24, -12 and -5 dB at velocities 40, 80 and 120.
- **A route's amount is a fraction of its destination's span.** A macro on another route's amount (span -1 to 1) moves that amount by twice the macro's value. A macro value of 0.1 took a filter-pump route from 0.18 to 0.38, and the pump's brightness range measured 13.0, 20.7 and 29.1 semitones at macro 0, 0.5 and 1.
- **Reverb decay spans 12 units of log2 seconds.** A macro amount of 0.2 on the decay multiplied it about five times (3.5 s to about 18 s). An amount of 0.05 multiplied it about 1.5 times.
- **Tempo-synced LFO:** tempo index 9 is an eighth note, measured at 4.0 Hz at 120 BPM.
- **Oscillator distortion type 7** is FM from another oscillator. Energy above 1 kHz rose from -16.6 to -11.5 dB as the amount rose.
- **Random style 1** is sample-and-hold. Three identical sixteenth notes measured 1150, 1201 and 1272 Hz spectral centroid.
- **Perlin random (style 0) restarts at every note in trigger mode** (`sync_type` 0, the default). A sine with random on its pitch (±4.8 st) put eight short notes within 0.1 st of each other, and moved a 4-second held note only 0.72 st. **In sync mode (`sync_type` 1) it runs on across notes**, but at 0.4 Hz it reaches only about 15–25% of its range in a few seconds (1.23 st and 0.32 st). So a drift needs about 5 times the route it seems to need. Sample-and-hold (style 1) picks a new value at each trigger and steps within a note (3.67 st on the held note).
- **A 7 kHz high cut before the reverb** did not change a bright reverb tail (energy above 14 kHz: -16.2 dB before, -16.4 dB after).

## What the protocol caught

- **A dead velocity layer:** a second layer meant to arrive on hard notes changed brightness by 0.15 semitones across the whole velocity range. The quadratic level was the cause. After the fix, the layer rose 19.5 dB from velocity 40 to 120.
- **A macro that did all its work in its first half:** +21.8 semitones, then -0.9. Step 7, "test each control from minimum to maximum", caught it.
- **A macro whose tail never ended** at full travel: about 18 s of reverb in a 32 s test slot.
- **A recipe's motion that was not there:** the bass recipe's slow random drift, and with it the macro meant to speed the drift up. Two fixes changed nothing, because the random was restarting at every note. With sync mode and a 5x route, the phrase moved 3.2 st from the original, and the macro gave 3.9 dB of held-note movement at full travel.
- **Macros that change loudness:** a drive macro added 4.1 dB over its travel and a wavetable-brightness macro lost 3.2 dB. The challenge asks for constant loudness, so both need compensating.
- **Hard chords that came out darker, not brighter**, on both pads (about -4 semitones). Unresolved; it may be the measurement (next section).

- **A challenge whose three versions sounded the same in the song:** the leads differed alone but only by 0.9–1.6 dB of spectral shape in the chorus, against 0.2–0.3 dB between the verses, which have no lead. Pushing each mechanism to its extreme, and giving the lead its solo level, brought every pair to 1.8–2.7 dB. Moving one lead's cutoff only slid it between the other two; resonance gave it an axis of its own.

## Traps in measuring the protocol

- **Slow attacks:** short-note, attack and chord-against-single-note readings land inside the swell. Measure after the attack, or say that the reading was taken inside it.
- **Delay and reverb inflate attack readings** because they keep raising the level after the envelope has peaked. Read the attack on the dry render.
- **Spectral centroid hides motion in an upper layer** that sits over a dominant core. Measure each band's spectral shape with the level removed.
- **An octave layer interferes with the core's own second harmonic,** so that band is unreliable at medium velocity. If the layer is the only stereo part, its side channel measures it cleanly.
- **"Largest jump against the median" flags bright sounds and decaying tails as clicks.** Compare each jump against the local 10 ms level instead.
- **A 14-second drift can't be heard or measured on a 4-second held note.** Hold one note for a full cycle.
- **Measure competing versions in context, against a baseline.** Compare their spectral shape in the part's own band, and their brightness over time, against a section where the part is absent. Match the versions alone on the material they play.
- **A loudness target and a peak ceiling can conflict for strikes.** A transition hit had to drop to -20.6 LUFS before its stacked strikes stopped clipping.

Measurement shows whether a route does anything. Only listening decides whether it serves the part, so rubric scores taken from measurements are provisional.
