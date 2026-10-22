# Original Vital Patch Architecture Exercises

These are teaching blueprints, not verified Vital preset files and not claims about any artist's settings. Build from Init, audition each stage, and adapt values by ear. A percentage or range below is a starting region, not a calibrated Vital parameter value.

## 1. Moving Glass / Metallic Pad

**Role:** sustained chord layer with a bright edge that slowly changes without turning into an obvious filter sweep.

**Architecture**

- **Foundation:** Oscillator 1 uses a harmonically rich wavetable. Start with a moderate frame range rather than scanning the full table.
- **Edge:** Oscillator 2 uses a brighter, higher-register source at a much lower level. Keep it subtle enough that muting it removes sheen rather than the whole chord.
- **Envelope:** slow-to-medium attack; moderate sustain; release long enough to connect chord changes but short enough not to smear the progression.
- **Motion A:** slow LFO to wavetable position, small range, free-running or restart behavior chosen to suit whether each chord should feel related or newly articulated.
- **Motion B:** envelope to filter cutoff for a small initial opening. Avoid making both motions peak at the same moment unless that swell is wanted.
- **Performance:** macro `OPEN` moves cutoff and a small amount of wavetable position in coordinated directions; macro `DARK` reduces edge and reverb for a verse version.
- **Effects:** subtle chorus or stereo movement on upper content; short-to-medium reverb. Check mono compatibility and chord clarity.

**Teach the mechanism:** first make a static pad, then add Motion A only, then Motion B. Explain which movement is periodic/continuous and which is note-triggered. Compare both over the same four-chord phrase.

**Troubleshooting:** if it sounds like a generic sweep, reduce the LFO range or use a shaped LFO. If chords smear, shorten release/reverb or reduce low-frequency stereo. If the edge disappears in the mix, raise its level only after checking masking.

## 2. Articulated Bass / Growl With a Stable Core

**Role:** mono or near-mono bass whose center stays readable while its upper harmonics snarl and move.

**Architecture**

- **Core:** a simple low oscillator or sub source carries the fundamental. Keep this layer relatively clean and centered.
- **Character:** a second oscillator uses a harmonically rich table. Explore phase/frequency modulation or a warp mode to generate upper harmonics; begin with a low modulation amount and listen before increasing it.
- **Filter:** try a low-pass or band-focused shape on the character layer. If the synth's routing permits, keep the clean core out of the most destructive processing.
- **Envelope:** fast attack, controlled decay, modest sustain; release short enough to prevent note overlap unless the part is legato.
- **Motion:** a note-triggered envelope drives a brief filter/warp accent. A slower LFO or random source may add small phrase-level movement, but should not destabilize the core pitch.
- **Performance:** velocity increases bite or filter opening. Macro `BITE` increases character-layer drive/warp and filter emphasis while leaving sub level almost unchanged.
- **Effects:** distortion/saturation on the upper layer, not indiscriminately on the sub. Confirm the result at low playback level and in mono.

**Teach the mechanism:** mute the core and character layer in turn; compare the patch on single notes and a repeated bass pattern. Explain why an upper-harmonic growl can be audible on small speakers while the core supplies pitch weight.

**Troubleshooting:** if pitch becomes unclear, lower the character layer or modulation amount; if it vanishes on small speakers, restore upper harmonics rather than boosting sub; if notes blur, check release, glide, and overlapping MIDI.

## 3. Cinematic Formant / Vocal-Like Lead

**Role:** expressive lead with a vowel-like changing color; it should remain an instrument, not be presented as a human voice.

**Architecture**

- **Source:** two related oscillators or a wavetable with distinct spectral zones; set a stable core and a quieter color source.
- **Color movement:** use a filter/formant-like spectral shape, or move between useful wavetable regions. Map a macro to the timbral transition and restrict it to a range that remains musically legible.
- **Expression:** velocity shapes attack brightness; pressure or a DAW automation lane can move the macro during held notes. Use pitch bend/glide only if the part calls for it.
- **Envelope:** quick enough to articulate a line; sustain high enough for phrase continuity; release matched to the tempo.
- **Secondary motion:** subtle random variation or a slow LFO can prevent repeated notes from feeling identical. Keep pitch modulation independent unless intentional vibrato is part of the brief.
- **Effects:** short delay for rhythmic tail; reverb or chorus only if the arrangement needs it. Keep the direct signal present.

**Teach the mechanism:** play a repeated four-note phrase while moving the macro on different notes. Record one take with static timbre and one with the macro gesture. Compare whether the motion supports phrasing or distracts from it.

**Troubleshooting:** if it resembles a caricatured vowel filter, narrow the sweep and reduce resonance; if modulation sounds like vibrato but is meant to alter tone, verify the destination; if the phrase loses definition, reduce effect tails.

## Design challenge: same role, three mechanisms

Choose one role (for example, chorus lead) and design three variants that differ by mechanism:

- **Variant A:** timbre changes through wavetable position.
- **Variant B:** timbre changes through filter envelope and saturation.
- **Variant C:** timbre changes through velocity/performance control and a second layer.

Keep the MIDI, register, and loudness approximately constant. Ask a listener which version best serves the song and why. Do not choose solely from a soloed sound.
