# Equal divisions of the octave

## Cultural context

A tuning theory file. An **EDO** divides the octave into some number of equal steps. Twelve is one
choice among many, and the others are used in three distinguishable ways:

- As **living practice**: 12-EDO in most Western and Western-influenced music worldwide.
- As a **theoretical frame** for a practice that does not actually measure that way: 24-EDO in
  Arabic notation, 53-EDO behind Turkish Arel-Ezgi-Uzdilek theory. See `MAQAM.md` and
  `ADDITIVE_METERS_BALKAN_TURKISH.md`.
- As **composer's material** in the xenharmonic tradition: 19, 22, 31, 53 and many others, chosen
  for what they can do. See `CONTEMPORARY_MICROTONALITY.md`.

Much of the current documentation of EDOs lives on the Xenharmonic Wiki, which is a community
wiki. It is excellent for definitions and numbers. Cite it as a community wiki, and prefer primary
theorists for claims about history or perception.

## Pitch organisation

**Understand an EDO by which just intervals it approximates and which commas it tempers out.**
Step count alone tells you almost nothing.

A comma tempered out is a comma set to zero: two pitches that differ by that comma become the same
pitch, which collapses part of the just lattice into a usable keyboard. Which comma you choose to
vanish determines the whole character of the system, including how notation works and which chord
progressions close.

```text
step size = 1200 / n cents

12-EDO   100 cents        19-EDO  63.158       22-EDO  54.545
24-EDO    50 cents        31-EDO  38.710       53-EDO  22.642
```

| EDO | Family and character | What it is good for |
|---|---|---|
| 19 | meantone family; fifth flatter than usual for meantone | meantone repertoire with fewer pitches than 31; practical keyboard size |
| 22 | not meantone; the fifth is sharp; tunes the septimal supermajor third 9/7 almost exactly just | seventh-limit harmony with a distinctly different chord vocabulary |
| 31 | the meantone temperament, extended quarter-comma meantone with good seventh-limit | the most accurate common meantone EDO; strong for just-leaning harmony |
| 53 | near-pure fifths, approximately a schisma temperament; one step is the Holdrian comma | Pythagorean and near-just work; the frame for Turkish AEU theory |
| 24 | 12-EDO plus a note halfway between each pair | the notation frame for Arabic music, and quarter-tone concert repertoire |

**19 versus 31 is an open trade, not a settled question.** 31 approximates the just intervals more
accurately; 19 requires fewer pitches and is easier to build and play. Both are reasonable and the
choice is compositional.

**24-EDO is a notation frame, not a tuning of Arabic music.** The equal quarter tone was contested
at the 1932 Cairo Congress and measurement shows practice varies by maqam. Similarly, **53-EDO is
not "the Turkish tuning"**: AEU theory is framed in 53 commas, and measured performance deviates
from the theoretical positions systematically. Both points are load-bearing and are repeated here
because they are the most common misuse of this file.

## Rhythm and cycle

Not applicable.

## Phrase structure and form

Not applicable directly. One practical consequence is worth stating: in an EDO whose thirds or
sevenths are much closer to just than 12-EDO's, chords sustain and blend differently, and a piece
can hold a harmony longer before it tires.

## Ornamentation

Not applicable, except that in an EDO with small steps (53, and larger divisions) a step can
function as an inflection rather than as a melodic move, which is an ornamental resource.

## The role of improvisation

Not applicable as a system property. Practically, improvising in an unfamiliar EDO is limited by
the controller: a standard keyboard has to be remapped, and the player's muscle memory does not
transfer.

## Ensemble behaviour

Omitted. The practical constraint is the same as in `JUST_INTONATION.md`: every instrument has to
be in the same division, from the same reference, or the approximations the division was chosen
for do not appear.

## Notation and instrument support

Practical notes, because these determine whether a piece can be played at all:

- **Notation.** There is no single accepted notation for non-12 EDOs. Systems exist per EDO and
  per community (ups and downs notation, sagittal accidentals, and others), and they are not
  interchangeable. State which system a score uses.
- **Controllers.** A standard keyboard gives twelve keys per octave. An EDO with more pitches
  needs a mapping decision: which pitches are reachable and where. That decision is part of the
  composition.
- **Instruments.** Support varies by product and by mechanism. The audit questions are in
  `shared/TUNING_AND_MPE.md`, which is where implementation belongs.
- **Step count versus period.** Some scale files repeat at something other than the octave. An EDO
  by definition repeats at the octave; see `CONTEMPORARY_MICROTONALITY.md` for the alternative.

## What generalises

- Asking "which just intervals does this approximate, and which commas does it temper out" is the
  right question to ask of any tuning, including 12-EDO.
- A tuning can be chosen for a specific harmonic goal (a near-just septimal third, near-pure
  fifths) rather than for exoticism, and that choice should be stated as a goal.
- Fewer, more practical pitches versus more, more accurate pitches is a real design trade that
  recurs everywhere.

## What must not be casually universalised

- **Do not present 24-EDO as the Arabic tuning or 53-EDO as the Turkish tuning.** Both are
  notational or theoretical frames, and measured practice differs.
- Do not describe an EDO by its step count alone, as though 22 were simply "more notes than 19".
- Do not assume a chord progression transfers between EDOs. Different commas vanish, so different
  progressions close.
- Do not treat the Xenharmonic Wiki as a primary source for historical or perceptual claims.
- Do not assume a listener hears a small-step EDO as microtonal rather than as mistuned.
  Familiarity governs that, and it is a real constraint on the music.

## Working with this in the studio

**Composer** sets: the EDO, the reason for choosing it stated as an interval goal, the reference
pitch in Hz, the subset of pitches actually used, the notation system, and the keyboard or
controller mapping.

**Performance Director** needs: the mapping, the notation system, and which intervals in this
division are the good ones, since those are what the writing should lean on.

**MIDI Builder and Plugin Auditor** must check that the instrument supports more (or fewer) than
twelve pitches per octave, which many do not even when they advertise microtuning. Verify the
mechanism, the reference pitch, and whether held notes retune. Where a per-note bend fallback is
used, verify the bend range is declared and that resolution is sufficient for the step size. See
`shared/TUNING_AND_MPE.md`. Silent re-quantisation to 12-tone equal temperament is not acceptable.

**Listener Model** should not treat unfamiliar intervals as errors, and should not assume the
surprise value of a chord transfers from 12-EDO experience.

## Sources and confidence

- Xenharmonic Wiki pages for 19edo, 22edo, 31edo and 53edo, and its "Tour of regular
  temperaments". Open these first for definitions and numbers, and cite them as a community wiki.
- On the Holdrian comma as one step of 53 and on AEU theory in 53 commas: the Turkish theory
  literature, with Akkoc and related measurement work for the deviation of practice from theory.
- On 24-EDO and the 1932 Cairo Congress: see `MAQAM.md` and its sources.

Confidence: the step sizes above are arithmetic and exact to three decimal places. The family
characterisations (19 and 31 meantone, 22 superpyth with a near-just 9/7, 53 near-Pythagorean)
come from the Xenharmonic Wiki and are consistent with the wider literature, but the pages were
not read in full. **To verify:** the precise error figures for each approximation, and the details
of which commas each division tempers out, before printing them as fact.
