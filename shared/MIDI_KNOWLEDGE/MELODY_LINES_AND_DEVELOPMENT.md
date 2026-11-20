# Melody, arps, counterpoint and development

Labels: **Measured** (corpus), **Practice**, **Inference**. Numbers: `stats/classical_lines_counterpoint.json`
(Mutopia selection, n=136 files; PDMX approved sample, n=3,805; medians with 10th–90th percentiles).
Electronic melody and arp numbers are in `local/ZYNTHION_FINDINGS.md` when present.

## 1. Melodic motion

**Measured (top line of each score):**

| Group | Stepwise (≤2 st) | Leaps (≥5 st) | Leap recovered by step the other way | Range (st) |
|---|---|---|---|---|
| PDMX classical (n≈2,700) | 0.39 (0.17–0.61) | 0.32 | 0.40 | 36 (whole piece) |
| PDMX folk (n≈370) | 0.42 (0.16–0.64) | 0.17 | 0.36 | 20 |
| PDMX sacred (n≈70) | 0.41 | 0.19 | 0.41 | 21 |
| Mutopia counterpoint (inventions) | 0.52 | 0.29 | 0.46 | 43 |
| Mutopia concert-band marches | 0.43 | 0.22 | 0.43 | 26 |

**Inference:** tunes move mostly by step, but not only. Roughly 1 move in 5 to 1 in 3 is a leap of a 4th or
more, and after a leap about 40% of lines turn back by step. A melody that is all steps sounds like a scale;
one that is all leaps sounds like an arpeggio.

**Rule:** aim for 40–60% steps, 15–30% leaps, and recover most big leaps by stepping back the other way. Put
the leaps on the words or beats that matter (the hook's peak) rather than spreading them evenly.

## 2. Hooks and phrase length

**Practice:** a hook is short, repeated and changed once. Write a 2–4 note cell; repeat it with one change of
rhythm, interval or ending; make the 4th statement answer the first three.
**Practice:** electronic and trap hooks usually stay inside about an octave, and trap phrases are short and
detached (measured numbers in `local/` when present). **Measured (Mutopia marches):** phrases of about 6 notes between
rests. That's shorter than most generated melodies, which tend to run on without breathing.

**Rule:** give the lead a breath (a rest of a beat or more) at least every 1–2 bars, unless the genre is a
continuous line (arps, Baroque solo lines). Repeat the cell; don't write 8 bars of new notes.

## 3. Melody against harmony

**Measured (PDMX classical, scores with a separate chord or accompaniment part):** 62% of melody notes are chord
tones (33–85%). Folk 64%.
**Rule:** land chord tones on strong beats and long notes. Use non-chord tones (passing notes, neighbours,
suspensions, anticipations) on weak positions and short values: about a third of the notes.

## 4. Arpeggios and broken-chord figures

**Practice (with measured electronic numbers when present):** an arp is a texture, not a tune.
- Choose one rate (8ths, 16ths or triplets) and a span of about an octave plus a step.
- Use a gate slightly under 1, and a cycle that repeats until the chord changes.
- Accent the first note of each group, or every 3rd note against a 4-feel for a polyrhythmic lilt.
- **Mutopia selections** (guitar etudes, Chopin's Op. 28 No. 1, Debussy's arabesques) show the classical form:
  the arpeggio carries a hidden melody on its top or bottom note. Voice the arp so its highest notes move by
  step.

**Rule:** if an arp and a lead share a register, one of them moves. Arps in the 70s–80s MIDI range sit above a
lead in the 60s–70s, or the reverse.

## 5. Two lines at once: counterpoint and part independence

**Measured (outer voices wherever two or more pitches sound):**

| Group | Contrary motion | Oblique | Parallel 5ths per 100 moves | Attack points with only one part moving |
|---|---|---|---|---|
| Mutopia counterpoint (inventions) | 0.45 | 0.06 | 0.0 | 0.47 |
| Mutopia fugues | 0.37 | 0.04 | 0.0 | 0.60 |
| PDMX classical | 0.36 (0.19–0.50) | 0.20 | 0.0 (0–1.4) | 0.39 |
| PDMX folk | 0.33 | 0.24 | 0.0 | 0.38 |

**Inference:**
- Independent lines move against each other about 40% of the time. Parallel fifths are essentially absent
  from art music, and present but rare in user-original scores (median 0.4).
- In fugues, 60% of attack points have just one voice moving: **voices take turns being active**. That rhythmic
  complementarity, more than pitch, is what makes parts sound independent.

**Rule for any multi-part writing (bass vs lead, strings, keys left vs right hand):**
- When the top goes up, move the bass down or hold it at least a third of the time.
- Let one part move while the other holds.
- Avoid parallel fifths and octaves between the outer voices, except as a deliberate doubling, which is an
  orchestration choice, not counterpoint.

## 6. Development: repetition with change

**Measured:**
- Melody bar-pattern uniqueness (share of bars whose pitch-and-rhythm pattern differs from every other bar):
  PDMX classical median 0.68, folk 0.48, Mutopia marches 0.51.
- Pieces chosen for development show more: Beethoven's 5th, 1st movement, built from one 4-note motif, and
  the inventions, which reach near 1.0.

**Inference:**
- Folk and dance music repeat (half the bars recur). Developed art music varies almost every bar while
  keeping a motif recognisable.
- Popular genres sit between: a hook that recurs exactly, and verses that vary.

**Rule:** develop a motif by one change at a time: transpose it (sequence), invert it, change its rhythm,
fragment it (keep the first 2 notes), extend it, or reharmonise it. Keep the hook exact where it must be
recognised, and develop everything around it.

## 7. Ground bass and ostinato builds

**Practice, from the Mutopia selections** (Pachelbel's canon over a 2-bar bass, Bach's Passacaglia BWV 582 and
Chaconne, the Allegretto of Beethoven's 7th):
- A fixed bass loop can carry a long piece if the upper parts enter one at a time, imitate each other and
  increase in rhythmic density.
- Beethoven's Allegretto builds by adding instruments and registers over an unchanged rhythm.
- **This is the loop-based producer's arrangement problem, solved centuries ago.** A 2- or 4-bar loop stays
  interesting when each 8 bars adds a layer, raises a register, doubles a rhythm or takes something away.

## 8. Accompaniment as drama

**Practice, from the Mutopia songs** (Schubert's *Erlkönig*, *Auf dem Wasser zu singen*): the accompaniment
figure *is* the image, as galloping repeated octaves or rippling water. **Rule:** give the accompaniment one
characteristic figure that means something, and change the figure when the meaning changes. That's more
effective than block chords under a busy melody.
