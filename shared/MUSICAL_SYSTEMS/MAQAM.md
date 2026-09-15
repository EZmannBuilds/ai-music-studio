# Arabic maqam

## Cultural context

Maqam is the melodic system of Arabic art and popular music across Egypt, the Levant (Aleppo,
Damascus, Beirut), Iraq and the Maghreb, carried largely by oral transmission and by a performance
culture of know-how rather than by a codified textbook. Farraj and Abu Shumays, both
practitioners, describe it that way in *Inside Arabic Music* (2019).

The internal distinctions matter more than the umbrella:

- **Egyptian and Levantine practice** differ in intonation of the same named note, and in
  repertoire.
- **Turkish makam** shares much vocabulary and history but is a separate system with its own
  theory (Arel-Ezgi-Uzdilek, 53 commas) and its own repertoire. **Persian dastgah** is a third
  system again.
- Within Arabic practice, the tradition of the *muwashshah*, the *qasida*, the Iraqi maqam and
  modern Egyptian song each use the system differently.

Treating these as one interchangeable pool is the first error.

## Pitch organisation

The operative unit is the **jins** (plural **ajnas**): a cell of three to five notes with a tonic,
an internal character, and a **ghammaz**, a pivot note from which the next jins hangs. Abu Shumays
(2013) argues explicitly against the inherited Greek-tetrachord, octave-scale account, on the
evidence of eighteen analysed pieces.

A **maqam** is a default pathway through a set of ajnas, plus expectations about where to dwell,
when you may ascend, where you may leave for another maqam, and how you come home. That pathway is
the **sayr**. The same collection of pitches under two different sayrs is two different maqamat.

Intonation belongs to the jins in context, not to a scale degree in the abstract. Marcus (1993) is
cited in the later literature as showing that the so-called quarter tones differ in intonation
from scale to scale, and that the apparently normal notes do too.

The **quarter tone is a notation, not a tuning.** The equal 24-division was the subject of fierce
disagreement at the Congress of Cairo in 1932: Egyptian delegates favoured it, Turkish (Yekta Bey)
and Syro-Lebanese (Sabra, al-Sabbagh) delegates rejected it. The half-flat sign is a placeholder
for a regionally variable pitch. Do not print 24-EDO cents as "Arabic tuning".

Working shape for a jins, filled in per jins rather than inherited from a scale:

```yaml
jins:
  name:
  tonic:
  notes:                  # 3 to 5, written pitches
  ghammaz:                # pivot to the next jins
  typical_register:
  intonation_note:        # which note is regionally variable, and how
  characteristic_motion:  # how the cell is habitually traversed
```

## Rhythm and cycle

Rhythmic cycles are **iqa'at** (singular **iqa'**), notated as skeletons of **dum** (low,
resonant), **tak** (high, dry) and rests. The percussionist ornaments the skeleton; the skeleton
is what holds.

The research could not reach MaqamWorld's iqa'at pages. Named cycles such as maqsum and samai
thaqil are standard, but **the exact stroke patterns are to verify against a primary source before
any file or output prints them.** Write the iqa' by name and structure, and fetch the pattern when
you need it.

## Phrase structure and form

Composed forms (samai, bashraf, muwashshah, dawr, and modern song forms) alternate fixed material
with sections that open toward improvisation. Across forms the constant is the **qafla**, a
cadential formula that closes a phrase or a section and confirms which jins you are standing in.

Phrases are built jins by jins: establish the cell, reach its ghammaz, hand over to the next cell,
and eventually retrace the path down to the tonic.

## Ornamentation

Ornament is part of the identity of the jins, not surface decoration. Slides, turns, repeated-note
attacks and the shaping of the variable note carry the regional accent of a performance. A line
stripped of ornament and quantised to fixed pitch is not the same line played plainly; it is a
different melodic object.

## The role of improvisation

**Taqsim** is instrumental improvisation that follows the maqam's sayr closely, including its
intonation, phrasing and modulation. It opens in the lower ajnas to establish the maqam, may
modulate to other maqamat provided it returns to the original, and closes sections with qaflat.

The freedom is real and it is bounded: by the sayr, by the cadential formulas, and by the
obligation to return.

## Ensemble behaviour

The takht ensemble (oud, qanun, nay, violin, riqq, and voice) is largely **heterophonic**: parts
play the same melody, each in its own idiom, decorating differently. Percussion holds the iqa'.
There is no chord section, and no part is a harmonic accompaniment in the Western sense.

## What generalises

- Build melody from small cells with a tonic and a designated exit note, and join the cells,
  rather than filling in a scale.
- Give a mode a **path**: where you start, what you lean on, when you are allowed to climb, where
  you may leave, and how you return. This is a stronger compositional constraint than a pitch set.
- Treat intonation as a property of a cell in context, which is how many improvisers already think
  about targets.
- Close sections with a recognisable formula. A cadence can be a melodic object, not a chord pair.

## What must not be casually universalised

- **Do not harmonise a maqam with functional triads to "make it sound Arabic".** Adding ii-V-I
  under a maqam line replaces the system rather than supporting it. If harmony is wanted, treat it
  as a fusion decision and name it as one.
- **Do not treat Turkish makam or Persian dastgah as interchangeable with Arabic maqam.** Shared
  names do not mean shared intonation, repertoire or theory.
- **Do not present 24-EDO as the tuning of the tradition.** It was contested in 1932 and it
  remains a notational convenience.
- Do not assume Egyptian, Levantine and Turkish practice tune a written note the same way. Pick
  the practice you mean, and say which one.
- Do not generate "a maqam" by choosing a scale and adding an oud sample.
- **Maqam is also the melodic language of religious practice**: Qur'anic recitation, the call to
  prayer, Sufi ritual music, and Eastern Christian chant in the Arabic-speaking world. Those uses are
  not source material. Under `INDEX.md` rule 5 the studio does not imitate, sample or set new words to
  recitation or liturgy, and offers the secular repertoire (taqsim, the song and instrumental
  repertoire of the takht) instead.

## Working with this in the studio

**Composer** sets: the maqam, the ajnas in play with their tonics and ghammaz notes, the sayr as
an ordered list of stations, the qafla formulas, the iqa' by name, and the regional practice being
followed. Melody is written as cell traversals, not as scale runs.

**Performance Director** needs: which note is the variable one and roughly where it sits in this
practice, the ornament vocabulary for the instrument, and the heterophonic instruction that parts
decorate the same line rather than harmonising it.

**MIDI Builder and Plugin Auditor** must check whether the chosen instrument can be retuned at
all, and by which mechanism. A fixed 12-tone sampler cannot place the variable note. If it cannot
be retuned, per-note bend is the fallback and the export must declare it. See
`shared/TUNING_AND_MPE.md`. Silent re-quantisation to 12-tone equal temperament is not acceptable.

**Listener Model** should not assume that a note outside 12-tone equal temperament reads as "out
of tune" or as expressive deviation from a norm. For a listener inside this tradition it is the
norm, and the equal-tempered version is the deviation.

## Sources and confidence

- Farraj and Abu Shumays, *Inside Arabic Music*, Oxford University Press, 2019. Open this first.
- Abu Shumays, "Maqam Analysis: A Primer", *Music Theory Spectrum* 35/2 (2013), 235 to 255. The
  argument for ajnas over octave scales. Open second.
- Marcus, "The Interface between Theory and Practice: Intonation in Arab Music", *Asian Music*
  24/2 (1993). Also Marcus, *Arab Music Theory in the Modern Period*, PhD, UCLA, 1989.
- MaqamWorld (maqamworld.com) for sayr and taqsim descriptions and for the iqa'at reference.
- On the 1932 Cairo Congress: secondary summaries only were reachable during research.

Confidence: the ajnas-and-sayr account and the "quarter tone is notation" point are well supported
across the sources found. **To verify before printing as fact:** specific iqa' stroke patterns;
any cents values for the variable notes in a named practice; the full text of all of the above,
none of which could be read in full during the research pass.
