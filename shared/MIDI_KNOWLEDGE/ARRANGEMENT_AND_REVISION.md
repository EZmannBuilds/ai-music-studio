# Arrangement, interplay and revision

Labels: **Measured**, **Practice**, **Inference**.

## 1. Sections must differ in measurable ways

**Measured:**
- In longer scores (24+ bars), note density varies with a coefficient of variation of 0.39 (0.22–0.68) in PDMX
  classical, and 0.5–0.7 in the Mutopia orchestral and concerto selections.
- Between consecutive 8-bar blocks, density or the number of active parts changes in 0.67–0.88 of block
  boundaries.
- Loops that never change score near 0 on both.

**Rule:** before writing notes, write the section map with what changes at each boundary. At least two of
these change at every boundary:
- number of parts playing (layers in or out)
- note density (half-time, double-time, held notes against 16ths)
- register (lead up an octave, bass drops an octave, pads open wider)
- drum pattern (a different hat rate, a kick pattern, the snare moved to half-time)
- harmony (new chord, a pedal against moving chords, a key change)
- a marker gesture in the bar before: a fill, a drop, a riser, a stop

`midi_check` counts the 8-bar blocks that change. A song of 48+ bars should change at 3+ boundaries.

## 2. Space between parts

**Measured:**
- In fugues 60% of attack points have one voice moving, 39% in PDMX classical. Parts take turns.
- Melodies avoid landing exactly where accompaniment chords attack about half the time (Maple Leaf Rag 0.52).
- Electronic productions keep chords about an octave above the bass (practice).

**Rules:**
- **Call and response:** when the lead rests, something else answers (a fill, a guitar lick, an arp turn).
  When the lead is busy, the others hold or simplify.
- **Register lanes:**
  - sub/808 (24–40)
  - bass (36–52)
  - chords (52–72), kept under a vocal or lead
  - lead or vocal (60–84)
  - sparkle (84+)
  Two parts in one lane need different rhythms.
- **Rhythmic lanes:** a 16th hat, a syncopated bass and a sustained pad can coexist. Three syncopated parts
  can't.
- **For a vocal:** chords held or sparse (no more than 4 attacks a bar), voiced under about MIDI 72, and no
  busy melodic part in the vocal's range.

## 3. Multiple directions before committing

**Practice** (the studio's own protocol: `../SKETCH_ROUND_PROTOCOL.md` and the Music Director's
divergent search):
- For a composition task, sketch 2–3 short versions that differ by mechanism, not by surface: a different
  groove, a different bass relationship, a different harmonic rhythm.
- Measure each with `midi_check`, say what each one does better, pick one or combine them, and only then
  build the full piece.
- When the brief says "just make it", run the round internally and report which direction won and why.

## 4. Revision loop: don't stop at "a file exists"

1. **Write** the part or song.
2. **Measure:** run Faderhand's `midi_check <file> --genre <genre>` (when installed). Fix every REVISE that isn't a deliberate
   choice, and write the deliberate ones in the notes.
3. **Read back:** dump the notes of bars 1, 4, 8 and a section boundary. Check the protected material
   (hooks, chords the user gave you) is unchanged.
4. **Listen** when a renderer or DAW is available: render through Faderhand (`record_track_audio`) or the
   DAW, and analyse with WavRead if installed (the separate WavRead skill). Measurements decide whether something is
   there; only listening decides whether it works.
5. **Revise the cause.** A weak chorus is usually a weak contrast with the verse, not a weak chorus. Change
   the boundary, not just the section.
6. **Stop** when the checks pass and a listen (or, without audio, a bar-by-bar read) finds nothing that
   serves the brief better. Report what wasn't heard.

## 5. Revising someone's material

**Practice:**
- Protect what the user made. Before editing, list what is protected (their chords, their hook, their
  tempo). After editing, diff the protected notes and prove they're unchanged.
- To make a part sound performed:
  - Change velocities first (by role and position).
  - Then timing (placement, then jitter).
  - Then durations (legato or detached by role).
  - Then variation (fills, pickups, drops every 4 or 8 bars).
- Don't re-write pitches unless asked.
- Check the low end against the kick after any timing change: a humanised bass that drifts off its kicks flams
  the low end. Re-lock bass onsets that belong with a kick, then humanise them together.
