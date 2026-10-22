# Vital Sound Design: Learn by Building

This is a guided course, not a reference encyclopedia. Each lesson produces a patch and a listening skill. Use Vital's initialized patch and save a new version before experiments. If the interface differs from the lesson, identify the control in the installed version rather than guessing from a screenshot or old tutorial.

## How to take the course

Work in 15–30 minute sessions. Use headphones or speakers at a comfortable level. Keep a simple MIDI test clip containing a short note, a held note, a two-note interval, a chord, and a short phrase. Disable reverb and delay until a lesson calls for them. Keep a notebook of what you heard, not just knob positions.

The agent should present one lesson at a time, ask you to predict what will change, let you try it, then explain the listening result. When working alone, write your prediction before turning the control.

## Lesson 1 — Build a note, shape a note

**You learn:** oscillator source and amplitude envelope are different jobs. The oscillator supplies the repeating tone; the amp envelope shapes how the note starts, holds, and ends.

**Build:** initialize Vital. Use Oscillator 1 at a simple saw or square-like source. Turn other oscillators and effects off. Shape the amp envelope into a short pluck; then save a second copy and turn it into a slow pad by changing attack, sustain, and release.

**Listen:** compare the same pitch as a short note and a held note. Notice that the pluck's decay happens while the key is down; release controls the tail after key-up.

**Checkpoint:** explain which control changes the onset, which changes the held level, and which changes the sound after note-off. If the sound never decays while held, inspect sustain/decay rather than adding reverb.

**Stretch:** make a third version with a delayed swell or very long attack. Keep the oscillator unchanged so the envelope remains the only main difference.

## Lesson 2 — Hear the harmonics

**You learn:** the fundamental and its harmonics give a sound its spectral character; waveform and oscillator blend change that structure, while a filter removes or emphasizes parts of it.

**Build:** compare sine/triangle/saw/pulse-like sources one at a time at the same pitch and level. Then blend two sources at different octaves. Route the result through a low-pass filter and sweep the cutoff slowly; try a small resonance increase after you can hear the cutoff movement.

**Listen:** use a middle-register note first. A low note can make high harmonics hard to judge; a very high note can make the fundamental hard to hear. Keep the source level matched between comparisons.

**Checkpoint:** describe whether a change added harmonic content, removed it, or emphasized a narrow region. Do not use "warmer" as the only answer; say what moved in the audible spectrum.

**Stretch:** make one patch bright at the attack and darker while held by modulating filter cutoff with an envelope. Keep the modulation range restrained enough that the note remains recognizable.

## Lesson 3 — Wavetables and spectral movement

**You learn:** a wavetable can move among related waveforms. Vital's oscillator warping can reshape harmonics; this is different from simply changing volume or playing a sample back.

**Build:** choose a wavetable with visibly different frames. Hold a note while moving its position manually. Find a small position range where the change sounds musical. Then assign a slow LFO to position and constrain its amount to that range. Compare a smooth shape with a stepped or custom shape.

**Listen:** distinguish the timbre changing within one held note from a repeated rhythmic gate. If the LFO changes level but not tone, check that it is assigned to wavetable position or a warp amount, rather than amplitude.

**Checkpoint:** draw or describe the movement over time. Name the start, peak, and return point, and say whether the motion restarts per note or continues.

**Stretch:** use a second, slower modulation source for subtle drift, or try one spectral warp and one waveform warp in separate saved versions. A warped signal can become thin, harsh, or hollow at extremes; compare useful ranges instead of maximizing the control.

## Lesson 4 — Modulation as a musical arrangement

**You learn:** a modulation source is an event or gesture; a destination is what changes. The amount and shape define how much of the event reaches the sound.

**Build:** create three versions of one sustained patch: (A) an envelope opens the filter once per note; (B) a tempo-synced LFO cycles the filter; (C) a random source makes small differences between notes. Inspect every route in the Matrix. Change one amount at a time. If available, use a remap curve to make a response stay subtle for most of its travel and open near the end.

**Listen:** A should have a one-shot contour; B should repeat; C should vary across notes. Confirm by playing a repeated-note pattern, not only by watching the animation.

**Checkpoint:** identify which source is note-triggered, synchronized to the host, or randomized. Explain how you would make each motion slower or less intense.

**Stretch:** build a patch with two time scales: a short envelope attack and a slow evolving wavetable/filter drift. Keep one motion obvious and the other subtle.

## Lesson 5 — Make a patch playable

**You learn:** a patch can respond to the musician, not only run its own modulation. Velocity may alter loudness and/or timbre. Note tracking may change a parameter with pitch. Aftertouch and MPE can provide continuing gestures when the controller and host support them.

**Build:** map velocity to amp level, then create a separate version where velocity also changes brightness. Test soft, medium, and hard notes at the same pitch. Map one macro to a useful performance transformation, such as moving from restrained to aggressive, and test its full travel. If you have a supported pressure/MPE controller, map pressure to one expressive parameter; otherwise mark it as unavailable and use a DAW automation lane for the exercise.

**Listen:** compare whether hard notes merely get louder or also become brighter/more biting. Check that the macro does not produce a useless middle range or an abrupt jump.

**Checkpoint:** explain the difference between a one-time note velocity and a continuous gesture such as pressure or a macro move.

**Stretch:** use note tracking to keep a filter or envelope behavior musically consistent across octaves. Check at least three registers; don't assume a mapping that works at C3 is right at C6.

## Lesson 6 — Layer with a purpose

**You learn:** layers work when each has a distinct job and remains audible in context. More oscillators can increase masking, phase interaction, stereo width, and CPU use without making the part more expressive.

**Build:** start with a lead or bass that has one oscillator. Duplicate the patch or add a second source with a named job: low foundation, transient, upper air, noise, width, or moving texture. Mute each source in turn. If muting a layer changes no useful feature, remove it. Keep a centered/mono-safe core for a bass or foreground lead and test stereo layers separately.

**Listen:** compare the patch in mono and stereo, then inside its song role. Check whether a second oscillator adds a stable harmonic identity or merely makes the sound louder and wider.

**Checkpoint:** name the function of every layer and identify what disappears when it is muted.

**Stretch:** make the layer change over time or velocity instead of sounding at full strength all the time.

## Lesson 7 — Effects, signal flow, and the mix

**You learn:** effects transform a source after it is generated; they cannot repair an unclear source architecture. Order matters: distortion before a filter often has a different result from distortion after it; delay and reverb create tails that can mask later notes.

**Build:** save a dry patch. Add one effect at a time, level-match the bypassed and active versions, and note what changed. Try a restrained saturation/distortion, then a short delay or reverb for a patch that needs space. Check dry/wet balance and effect tail against the MIDI phrase.

**Listen:** compare solo and in-context. Check whether the effect creates the desired identity or only makes the patch louder. For a bass, verify that the lowest octave stays defined and that stereo processing does not destabilize the center.

**Checkpoint:** state what each effect does, why it is placed there, and what would make you remove it.

**Stretch:** automate one send or macro across a section transition rather than leaving the patch permanently washed out.

## Lesson 8 — Diagnose and iterate

**You learn:** good revision is a controlled experiment. Change one cause, preserve the previous version, then decide from a musical test.

**Build:** choose one issue: too thin, too static, too harsh, too muddy, too wide, poor note-off, weak velocity response, or poor phrase fit. Write the audible symptom and a hypothesis. Change one control or route. Re-render the same test phrase and compare at similar loudness.

**Listen:** keep the change only if it fixes the target without breaking another required behavior. If several things changed, restore the previous version and isolate them.

**Checkpoint:** fill in a revision note: observation, hypothesis, single change, held-constant conditions, result, decision.

**Stretch:** design a contrasting version that solves the same role through a different mechanism—not just a different adjective or preset name.

## Capstone — Three instruments for one song

Create three original patches that have distinct jobs in a short arrangement:

1. **An evolving bass or lead:** controlled low end, one obvious motion, one usable performance control.
2. **A layered pad or chord instrument:** changing harmonic color over a held chord, with an intentional attack/release and stereo plan.
3. **A transient or transition instrument:** a clear attack and a defined tail, using modulation or effects to make its role audible.

For each patch, submit a `.vital` file if available, a patch card using `PATCH_STANDARD.md`, a short MIDI test phrase, a dry and processed render, and a short note explaining what changed from the first version. Test at least three velocities and the intended register.

### Capstone review

A reviewer should be able to answer yes to these questions:

- Can I hear the intended role without reading the patch name?
- Does the patch change over time or through performance in the intended way?
- Does every added layer or effect have an audible job?
- Does the patch survive the phrase, register, and mix context?
- Can I reproduce or revise it from the patch card?
- Are untested settings clearly marked as untested?
