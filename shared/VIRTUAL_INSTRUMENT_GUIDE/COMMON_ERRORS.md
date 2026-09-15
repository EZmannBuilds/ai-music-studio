# Common Errors

The failures that make a competently written part sound fake. Held here once so every instrument
page links to this list instead of repeating it.

> Evidence: tags per item, in the labels of `shared/RESEARCH_RULES.md`. The round-robin, overlap,
> continuous-dynamics and release items rest on one symphonic strings library's manual, re-read for
> 2.1 (`STRINGS-LIBRARY-MANUAL-1` in `research/sources/INSTRUMENT_SOURCES.md`); the rest is inference
> unless tagged otherwise. Nothing here was measured on the reader's system.

---

## 1. Machine-gun repeated samples

The same pitch repeated at the same velocity, so the sampler plays one identical recording several
times. No player produces two identical notes, and the ear hears the loop point faster than it hears
anything else on this list [inference]. The documented library states that round robins exist to
prevent repeated identical samples [manual-derived: STRINGS-LIBRARY-MANUAL-1].

Fix: use round robins, and let each repetition differ **for the reason a player's would**, never by
a random amount: the metrical accent of its position, the alternation that produced it (sticking,
bow direction, single against double tonguing, plucking fingers), and the direction of the phrase's
dynamic. Those are causes in `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4, and each gives the
repetitions a pattern the ear accepts as playing [inference].

## 2. No continuous dynamics on long notes

A held note given a velocity and nothing else, sitting at one loudness and one colour. On a bowed,
blown or sung instrument there is no held note at constant intensity. Fix: draw a dynamic shape per
phrase on the control that crossfades recorded dynamic layers. The documented library makes using it
on every long note one of its two basic rules [manual-derived: STRINGS-LIBRARY-MANUAL-1]. Which controller it is belongs in the calibration profile, not
here.

## 3. Quantised chord attacks with uniform velocity

Every chord tone on the same tick at the same velocity. A hand does not strike evenly, a section does
not attack at one instant, and a chord with no internal balance has no melody in it. Fix: spread the
attack in a direction the instrument produces, and bias velocity by role, melody above inner parts
above pads. This is `chord_asynchrony` in `shared/HUMAN_PERFORMANCE_SCHEMA.md`, derived from the
voicing rather than stored as a fixed number, and never copied from a keyboard part to another part.

## 4. Ignoring range and register strength

Notes where the instrument does not go, or where it goes but is thin, covered, unstable or hard to
control. Out of range it does not exist. In a weak register the sample plays happily at any dynamic
the writer asks for, which the real instrument cannot, so the part convinces in the sequencer and
fails for anyone who knows the instrument. Fix: check the family file's range and register sections
first, then move the line, re-orchestrate the register, or accept the weakness deliberately.

## 5. Legato written without note overlap

A melodic line with clean note-off before note-on, handed to a legato patch. A legato patch is
monophonic and plays a recorded transition only when the new note arrives while the old one is still
sounding. Without overlap it plays separate attacks, the articulation the writer was avoiding. Fix:
overlap the notes. The amount is a product fact, carried as `note_overlap.legato_overlap_ms`. In the
documented library the arriving note's velocity selects the transition, so those velocities are
articulation choices, not loudness [manual-derived: STRINGS-LIBRARY-MANUAL-1].

## 6. Voicings the instrument cannot physically play

Six-note guitar chords with a nine-fret stretch, two notes on one string, piano chords wider than a
hand, harp chords using nine fingers, a dyad on a wind instrument. It does not sound wrong, it sounds
impossible, which is worse, because the listener cannot name the problem and stops believing the
part. Fix: solve the physical instrument first. The Performance Director returns
`impossible_voicings` and `simultaneity_exceeded`. An impossible part may still be written when the
brief wants it. What is not allowed is writing it silently.

## 7. No releases, no breaths, no mechanism noise

A part with no gaps, no audible note endings, and the incidental noise stripped out. Real instruments
are noisy machines operated by people who breathe, and fret squeak, bow change, key noise, pick
attack and damper thump are how the ear places an instrument in a body and a room. Fix: leave gaps
where a player breathes or changes bow, and leave the noise layers on. The causes are named in
`shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4.

## 8. One articulation for everything

A whole part on a single sustain or generic long-note patch. Players change how a note starts several
times a bar, and one articulation flattens the rhythm of attack that carries the phrasing. Fix:
choose articulations per note or per group. Where the required one is not installed, the Performance
Director reports `articulation_unavailable` rather than substituting silently.

## 9. Dynamics written to a control the instrument ignores

A carefully drawn curve on a controller the patch does not read, or on a volume trim when the
instrument wants the layer crossfade, or on velocity for a long-note patch that takes dynamics
elsewhere. The curve does nothing, or it changes level without changing colour, which is item 10.
Fix: find out what the patch listens to before writing. MIDI Builder writes to `dynamic_arc.control`,
not to whichever control is habitual.

## 10. A swell written as a volume fade

A crescendo made by raising the output level of a quiet sample. On most acoustic instruments, and on
brass most obviously, the spectrum brightens as the player pushes, so louder is a different sound and
not only a bigger one. For brass this is measured: the lips add harmonics as blowing pressure rises,
and at fortissimo a trombone's bore steepens the wave into a shock [academic: UNSW-BRASS;
HIRSCHBERG-1996]. That the same holds, less dramatically, across most blown and bowed instruments is
[standard-reference: FLETCHER-ROSSING-1998]. A loud sample turned down reads as a fader move. Fix:
use the control that crossfades recorded dynamic layers so timbre changes with level [inference].

## 11. Round robins reset every bar

A host setting that returns the round robin counter to position one at each bar line or transport
start. It recreates item 1 on the beats the listener attends to most. Fix: do not reset per bar.
Reset once at the start of a render if a bounce comparison needs determinism, and say so in the notes.

## 12. Notes glued end to end, killing release samples

Every note ending exactly where the next begins, on a patch that is not a legato patch. Release
samples need a real note-off with somewhere to sound; glued notes lose the release, the decay, the
damper noise and the room tail. Fix: shorten notes so note-off happens, except where legato requires
overlap. `note_length_variation` exists because releases are decisions.

## 13. Moving the reference the other parts are heard against

Applying expressive timing deviation to the part that states the time: a click, a sequenced pulse, an
arpeggiator, a timeline bell. Deviation reads as expression only against a stable reference; move
the reference and the arrangement reads as loose rather than expressive. Fix: name those parts in
`marker_parts_excluded` [inference].

Two limits on that rule. **A drum kit in live-feel music is usually not a marker part**: its
microtiming is the groove, as the pack's own hi-hat study shows [academic: RASANEN-2015]. And **in
some traditions the reference part carries the feel itself**: in one measured Khasonka dundunba
piece the bell plays a long-short subdivision averaging about 59:41 [academic: POLAK-LONDON-2014].
There the bell takes that piece's named microtiming template, applied as a model, not left on the
grid. What the rule forbids is deviation without a cause, not a
reference that has a feel.

## 14. A section patch playing more voices than the section has

Six-note chords on a patch recorded by four players, or divisi that leaves one player per part and
still expects a full sound. A sampled section is a fixed number of people, so stacking notes
multiplies the recording where the real thing would thin out and become exposed. Fix: know the
practical voice count before divisi, and write divisi as a deliberate thinning. Reported as
`simultaneity_exceeded`.

---

## Before you deliver

```text
[ ] every note inside the practical range, in a register that supports its dynamic
[ ] no repeated pitch at identical velocity; round robins on, not reset per bar
[ ] every long note carries a drawn dynamic shape, on the control the patch actually reads
[ ] every swell changes colour, not only level
[ ] legato lines overlap; non-legato lines do not glue end to end
[ ] chords spread and voiced, in a direction the instrument produces
[ ] articulations change where the music changes; unavailable ones reported, not substituted
[ ] voicings physically playable, or the exception recorded
[ ] breaths, bow changes and gaps exist; noise layers not muted
[ ] reference parts steady, unless their feel is a named model (a drum groove, a timeline's template)
[ ] every imperfection in the plan names its cause
```

The last line is the rule the rest serve. Organic performance is not random humanisation. See
`shared/HUMAN_PERFORMANCE_SCHEMA.md`.
