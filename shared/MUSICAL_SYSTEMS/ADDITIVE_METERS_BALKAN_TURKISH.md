# Additive meters: aksak and usul

## Cultural context

Two related but separate practices are covered here.

**Balkan dance music**, across Bulgaria, Macedonia, Greece, Serbia and neighbouring regions, is
built around dances in unequal metres. Each dance has a name, a step pattern, a region and a
repertoire.

**Turkish art music** organises metre through **usul**, a cycle that is part of the compositional
system rather than a dance step, and that binds metre to melodic phrase length.

Brailoiu ("Le rythme aksak", 1951) took the Turkish word *aksak*, "limping", into analytical use
for metres built from unequal groups, where the ratio between short and long units is not 2 to 1
but roughly 3 to 2. Arom (2004) extends the typology. Aksak metres occur widely in Turkish music
and across Bulgaria and the Balkans.

The dances are village and regional practice with living communities of dancers. The usul
repertoire is a court and conservatory tradition. Do not merge the vocabularies.

## Pitch organisation

Balkan folk pitch practice varies by region and instrument and is not covered here; where a
melodic system is needed, `MODAL_FOLK_SYSTEMS.md` is closer.

Turkish makam pitch theory is **Arel-Ezgi-Uzdilek**, a 24-note set constructed from Pythagorean
commas, nine commas to a whole tone, closely approximated by 53-tone equal temperament (the
Holdrian comma is one step of 53). Empirical measurement of master recordings (Bozkurt, Yarman,
Karaosmanoglu, Akkoc) shows performance deviating systematically from the theoretical AEU
positions. As with the Arabic quarter tone, **the theory is a notation, not a measurement of
practice.** Do not present 53-EDO as "the Turkish tuning". See `EDO_SYSTEMS.md`.

## Rhythm and cycle

**Unequal beats are the primary metrical level.** A short beat is two pulses and a long beat is
three. They are beats, not subdivisions of a larger regular beat, and they are felt as beats by
dancers.

**Always write the grouping, never a bare signature.** "9/8" alone is not information.

```text
9 = 2+2+2+3      one dance
9 = 3+2+2+2      a different dance
```

The same total divided differently is a different piece with a different step. This is the single
most important practical rule in the file.

Specific dance groupings are **widely taught and to verify** before printing:

| Dance | Grouping as commonly taught | Status |
|---|---|---|
| karsilama | 9 as 2+2+2+3 | to verify |
| ruchenitsa | 7 as 2+2+3 | to verify |
| lesnoto | 7 as 3+2+2 | to verify |
| daichovo | 9 as 2+2+2+3 | to verify |
| kopanitsa | 11 as 2+2+3+2+2 | reported in reference sources; confirm before use |

**Performance stretches the ratio.** The long beat is not reliably exactly 1.5 short beats. Treat
3:2 as a nominal value and expect the performed ratio to differ, consistently, within a style.

Turkish usuls are categorised by beat count (for example Aksak at 9 beats, Devr-i Hindi at 7,
Curcuna at 10) and are written as pronounceable vocables built from **dum** and **tek**, where dum
is a strong low beat. **Velvele** forms elaborate an usul by increasing the number of strokes
within each main beat without changing the metre, which is exactly the relationship between a drum
pattern and its fills.

## Phrase structure and form

In Turkish art music a composition in a given usul has phrase lengths that fit its cycle: the
metre determines the melodic form rather than merely underlying it. When writing in an usul,
phrase length is a constraint, not a free choice.

In Balkan dance music, form follows the dance: repeated melodic strains over a constant metre,
with tempo often increasing across a set.

## Ornamentation

Instrument-specific and regional in both practices, and not something this file can generalise
safely. Treat it as a matter for the named repertoire and the named instrument rather than a
system-wide rule.

## The role of improvisation

In Turkish art music, **taksim** is unmetred improvisation in a makam, and it sits outside the
usul; the usul governs the composed and metred sections. In Balkan dance music the melody is
largely fixed by the tune, with variation in ornament and in instrumental idiom rather than free
improvisation.

## Ensemble behaviour

Balkan dance ensembles vary widely by region and instrument family (gaida, kaval, gadulka,
tambura, accordion, brass bands). Turkish art music ensembles pair melodic instruments in
heterophony with percussion holding the usul. In both, the percussion states the cycle and the
melody is written to it.

## What generalises

- Metres built from twos and threes, named by their grouping, are a compositional resource in any
  genre, provided the grouping is stated and held.
- Binding phrase length to cycle length, as usul does, is a strong formal discipline and prevents
  the common failure where an odd metre is used as a novelty over four-bar pop phrasing.
- The dum and tek skeleton, elaborated by velvele-style fills, is a clean model for writing a drum
  part: skeleton first, fills second, skeleton never obscured.
- A nominal ratio that is deliberately performed away from its nominal value is a general
  microtiming idea, applicable to swing, to shuffle, and to non-isochronous feel generally.

## What must not be casually universalised

- **7/8 in a Bulgarian dance is not 7/8 in progressive rock.** The dance step defines the grouping
  and the feel. Borrowing the count without the grouping produces a different thing, and calling
  it the dance is wrong.
- **Usul names are repertoire-bound** and are not interchangeable with Balkan dance names, even
  where the beat count matches.
- Do not assume the long-to-short ratio is exactly 3:2.
- Do not treat aksak as "odd time". The conception differs: unequal beats versus an irregular
  number of equal beats.
- Do not present AEU or 53-EDO as the measured tuning of Turkish practice.

## Working with this in the studio

**Composer** sets: the total pulse count **and** the grouping, written out; which beat is long and
where it sits; the dance or usul by name if one is intended; the dum and tek skeleton; and phrase
lengths locked to the cycle where usul practice applies.

**Performance Director** needs: the intended long-to-short ratio as performed rather than nominal,
the placement of the long beat, and whether the tempo rises across the piece.

**MIDI Builder and Plugin Auditor** must check that the DAW can express the grouping rather than
only the signature: some hosts will accept 9/8 but beam and quantise it as 3+3+3, which silently
destroys 2+2+2+3. Verify the bar subdivision and the metronome accent pattern after import. If the
performed ratio is non-nominal, verify the offsets survive export rather than being re-quantised.

**Listener Model** should not model an unequal beat as a syncopation of an underlying equal beat,
and should not treat a listener familiar with the dance as experiencing the metre as complex.

## Sources and confidence

- Brailoiu, "Le rythme aksak", *Revue de Musicologie* 33 (1951), 71 to 108. Open first for the
  concept.
- Arom, "L'aksak: Principes et typologie", 2004, for the typology.
- Turkish Music Portal, for usul categories and the dum and tek vocables.
- Akkoc, "Experiments on the relationship between perde and seyir in Turkish makam music", on
  measured deviation from AEU positions; related measurement work by Bozkurt, Yarman and
  Karaosmanoglu.

Confidence: the aksak concept, the unequal-beat principle, the usul vocable notation and the
measured deviation from AEU are all supported. **Explicitly unverified:** the specific dance
groupings in the table above, which are widely taught but were not confirmed against a primary
source in this research pass, and any precise performed ratio. None of the sources were read in
full.
