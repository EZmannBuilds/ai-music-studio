# The blues system

## Cultural context

The blues is a Black American music, formed under specific historical conditions in the American
South and carried north through migration. That context is part of the subject and stays explicit;
it is not a preface to be skipped on the way to the scale.

The name covers several distinct repertoires. Titon's corpus in *Early Downhome Blues* is recorded
downhome blues from 1926 to 1930. Classic blues, jump blues, Chicago electric blues, Texas blues
and later electric styles differ from that corpus and from each other in form, instrumentation and
harmonic language. When a brief says "blues", ask which.

Kubik (*Africa and the Blues*, 1999) traces blues tonality to the Western and Central Sudanic belt
and proposes an account of blue notes grounded in that ancestry rather than in flattened diatonic
degrees.

## Pitch organisation

**The third, fifth and seventh are pitch areas, not flattened degrees.** Titon identifies them as
"complexes", microtonal in character and clearly broader than a single note. Evans (1982) calls
them "tonal areas". This is the finding the file is built on.

Cutting (2018 and 2019) measured pitch in fifteen recorded classic blues performances and found a
broad cluster around the third holding almost a quarter of all tones, and that **a major third
occurred often enough that it should be considered an integral part of the system** rather than a
borrowing or an error. The fourth and fifth form distinct clusters. Hahnel and Pfleiderer
published commentaries disputing the method, so the measurements are evidence, not settled fact.

How the blues third should be modelled is therefore an **open question**: Titon's complex, Evans's
tonal area and Cutting's clustering are three accounts, and the method behind the third is
contested.

Van der Merwe (1989) proposes the **ladder of thirds**: a modal frame in which melodies are formed
by piling thirds below and above a tonic or central note. The important consequence is that **the
melodic frame is independent of the chords underneath.** A melody note that sits against the
harmony is not an error, because the melody was not derived from the harmony. The I, IV and V
chords are a later container for an older melodic system.

Practical statement of the system:

```yaml
blues_pitch:
  areas: [third, fifth, seventh]      # zones, resolved by context and by the performer
  resolution: continuous              # voice, slide, bend, not discrete semitones
  major_third: present_in_the_system  # Cutting; not an outside note
  melodic_frame: ladder_of_thirds     # independent of the chord underneath
  cents_ranges: measured_only         # cite the measurement; do not invent targets
```

Any cents range printed anywhere must be attributed to a measurement of specific performances, in
the sense of rule 7 in `INDEX.md`. There are no fixed targets.

## Rhythm and cycle

Shuffle and swung subdivisions, with the exact ratio a matter of style and performer rather than a
fixed value. Backbeat in the ensemble styles. Downhome solo performance often does not hold a
strict bar count at all, which is not an error of the performer but a property of the form.

## Phrase structure and form

**AAB** is the characteristic lyric and melodic shape: a line, the line again (usually varied),
then a responding line. Melody and lyrics frequently follow this together.

**Call and response** operates at two levels: within the text through AAB, and within the
performance between the voice and an answering instrument filling the gaps at the end of each
line.

**Twelve bars is one form among several.** Eight-bar and sixteen-bar forms are common, and
downhome performances routinely use irregular bar counts. The quick-change variant, the turnaround
and the stop-time chorus are variants within the twelve-bar family. Treating twelve bars as the
definition of the blues is a textbook reduction.

## Ornamentation

Bends, slides, vibrato, growls and falls are how the pitch areas are inhabited. They are the
mechanism of the pitch system, not decoration on top of it. A blues line played with fixed pitch
and vibrato added is a different melodic object.

## The role of improvisation

Substantial and bounded by the form, the lyric shape and the vocabulary of the style. A soloist
works within known phrases and their variations, in call and response with the vocal or with the
band, over a known cycle. Later electric styles extended this considerably.

## Ensemble behaviour

Varies by repertoire: solo voice and guitar in downhome blues; voice with a small jazz-derived
band in classic blues; guitar, harmonica, piano, bass and drums in Chicago electric blues.
Constant across them is the gap left for the answering instrument, and the rhythm section
supporting a melody it does not generate.

## What generalises

- Pitch as an **area** resolved by context, played on continuous-pitch instruments, is a usable
  idea in any genre with voice, strings, slide or bend.
- A melodic frame that is independent of the harmony beneath it removes the habit of deriving
  melody from chord tones. This is directly useful in `composer/SKILL.md`'s melody workflow.
- Call and response, at both text and phrase level, is a general structural device.
- Statement, varied restatement, response is a three-part phrase shape usable anywhere.
- Irregular bar counts driven by the words rather than by the grid are available to any
  songwriter.

## What must not be casually universalised

- **The six-note "blues scale" box is a pedagogical reduction, not the system.** Anything that
  emits a six-note set as "the blues" has failed rule 1 in `INDEX.md`.
- **Do not present blue notes as flattened 12-tone equal-tempered degrees.** They are areas, and
  the major third is inside the system.
- **Keep the Black American historical context explicit.** It is not optional background.
- **Blues is not raw material for other genres.** The framing in which the blues supplies colour
  to something else is the framing this folder rejects.
- Do not generalise Titon's findings to later electric styles; his corpus is early recorded blues.
- Do not treat twelve bars as the form.

## Working with this in the studio

**Composer** sets: the repertoire being worked in, the form (bar count and variant), the lyric
shape, the melodic frame as a ladder of thirds independent of the changes, and the pitch areas
with their intended inflection, marked as areas rather than as fixed pitches.

**Performance Director** needs: which notes are bent and from where, the bend speed and shape, the
shuffle ratio as a performed value, and the placement of the answering fills.

**MIDI Builder and Plugin Auditor** must check that the instrument supports continuous pitch,
because the pitch system cannot be expressed in discrete semitones. Per-note bend (MPE) or a
monophonic bend line is required for a lead; verify the declared bend range. See
`shared/TUNING_AND_MPE.md`. A fixed-pitch piano or organ patch can play the harmony but cannot
render the melodic system, and the audit should name that limitation rather than let it pass.

**Listener Model** should not score a note inside a pitch area as out of tune, and should not
treat the major third over a dominant chord as an error. Both are system-internal.

## Sources and confidence

- Titon, *Early Downhome Blues: A Musical and Cultural Analysis*, 1977, 2nd ed. 1994. Open first.
- Evans, *Big Road Blues*, 1982, for "tonal areas".
- Cutting, "Microtonal Analysis of Blue Notes and the Blues Scale", *Empirical Musicology Review*
  13/1-2 (2018 and 2019), with the commentaries by Hahnel and by Pfleiderer, which dispute the
  method.
- Van der Merwe, *Origins of the Popular Style*, Clarendon, 1989, for the ladder of thirds.
- Kubik, *Africa and the Blues*, University Press of Mississippi, 1999.

Confidence: that the third, fifth and seventh are areas is agreed across Titon, Evans, Kubik,
McClary and Cutting. **Open and reported as open:** how the blues third should be modelled, with
the method behind Cutting's measurements contested. **To verify:** any specific cents values,
which must be attributed to a named measurement of named performances. None of these sources were
read in full during research.
