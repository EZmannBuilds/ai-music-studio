# Gamelan

## Cultural context

Gamelan is the tuned-percussion ensemble music of Indonesia. The two traditions most often meant
are **Javanese** and **Balinese**, and they are distinct: different repertoires, different
aesthetics, different instruments, different playing techniques. Balinese gong kebyar is
characterised by sudden flashes of sound, virtuosity and extreme dynamic contrast (Tenzer, 2000);
Javanese court gamelan works at different densities and tempos entirely. **Sundanese degung** is a
third tradition again.

An ensemble is a single object, tuned as a set, often named, and owned by a community, a court or
an institution rather than by the players.

**Ethics are not optional here.** Instruments are not stepped over. Players remove their shoes.
Some old sets are regarded as alive and receive offerings. Sacred ensembles, including iron
*selonding* gamelan, and temple repertoire, are ritual property. The studio declines to sample or
imitate consecrated ensembles and ceremonial repertoire, and says why when asked.

## Pitch organisation

**There is no canonical slendro or pelog in cents.** Slendro has five roughly equidistant tones
per octave; pelog has seven tones per octave with unequal intervals, from which five-note modes
(pathet) are selected. The actual interval profile, the **embat**, is a property of the individual
ensemble. Two respected sets can differ in absolute pitch and in interval size while both sound
entirely right.

Consequences that follow directly:

- Any `.scl` file for slendro or pelog is **one ensemble's** tuning. Label it with whose it is.
- Slendro is not five-tone equal temperament. Writing it as 5-EDO is the reduction this folder
  exists to prevent.
- The seven pelog tones are used as five-note pathet subsets, not played as a heptatonic scale.

**Ombak** is a tuning parameter, not an effect. Paired instruments are tuned slightly apart on
purpose: the lower is *pengumbang*, the higher *pengisep*. Sounded together they beat, producing
the shimmer characteristic of many Balinese ensembles. The beat rate is ensemble-specific and is
chosen by the tuner. This connects directly to the timbre-and-tuning argument in
`CONTEMPORARY_MICROTONALITY.md`: the ensemble's spectrum and its tuning are designed as one thing.

## Rhythm and cycle

Form is **colotomic**: nested cycles marked by punctuating instruments. The largest gong falls at
the **end** of the cycle, which is simultaneously the arrival and the point from which the next
cycle starts. Inside it, kenong, kempul and kethuk mark subdivisions at fixed positions.

```text
gongan (one full cycle)
  |----------------|----------------|----------------|--------------G|
      kenong            kenong           kenong          kenong  gong
   kethuk marks at fixed positions within each kenong span
```

Structure is heard as periodicity and as the arrival of punctuation, not as harmonic progression.
A programmer should treat the punctuation instruments as structural markers, not as accents.

## Phrase structure and form

A skeletal melody, the **balungan**, is elaborated by other instruments at **fixed density
ratios**. The Javanese **irama** levels set that ratio: roughly one to two, four, eight and
sixteen elaborating strokes per balungan beat across irama lancar or tanggung, dadi, wilet and
rangkep. Slowing the balungan therefore means moving to a denser elaboration, not merely lowering
the tempo.

At deeper irama levels, instruments change technique rather than simply playing faster. Drumming
cues the change of level.

**Tempo level equals density level.** That single idea is the most portable thing in this file.

## Ornamentation

Elaboration is the substance, not the decoration. **Kotekan** is two-part interlock: in Balinese
practice the *polos* part is generally on-beat and the *sangsih* part generally off-beat, and each
fills the gaps of the other. Neither part is the melody. The composite is.

## The role of improvisation

Limited compared with the other traditions in this folder. Elaborating parts are realised from the
balungan according to idiom and level rather than freely invented, and the drummer directs tempo
and irama. Treat this as a realisation practice rather than an improvisation practice, and do not
describe gamelan as improvised music.

## Ensemble behaviour

Layered by function: punctuating gongs mark the cycle; balungan instruments carry the skeleton;
elaborating instruments (bonang, gender, gambang, and in Bali the reyong and gangsa) fill at the
current density; drums direct; and in Javanese practice voices and softer instruments occupy their
own register and dynamic layer. Paired instruments are detuned against each other by design.

## What generalises

- Nested punctuating cycles are a way to build form without harmonic movement, and they work in
  any loop-based music.
- Putting the largest arrival at the **end** of a cycle rather than the beginning changes how
  phrases are shaped, in the same way sam does in `RAGA_AND_TALA.md`.
- Tying density to tempo level, so that slowing down means elaborating more, is a compositional
  rule worth borrowing directly.
- Interlock, where two parts that are individually simple produce a fast composite neither could
  play, is a general orchestration technique.
- Deliberate paired detuning as a tuning decision, rather than a chorus effect, is available to
  any producer who can tune two instances separately.

## What must not be casually universalised

- **Do not print slendro or pelog as a fixed cents table and call it the tuning.** It is one
  ensemble's embat, and it must be labelled as such.
- Do not treat gamelan samples as generic "ethnic percussion". They are a tuned set with a
  specific embat, and mixing samples from two ensembles produces a set that is out of tune with
  itself.
- Do not sample or imitate consecrated ensembles or temple repertoire.
- Javanese, Balinese and Sundanese traditions are distinct and are not interchangeable.
- Do not use pelog as a "mode" over Western chord changes. The chord changes replace the system.

## Working with this in the studio

**Composer** sets: the tradition (Javanese, Balinese, Sundanese), the tuning as a named source
with its provenance, the pathet subset in use, the gongan length with kenong, kempul and kethuk
positions, the balungan, and the irama level with its density ratio.

**Performance Director** needs: the interlock assignment (which part is on-beat and which
off-beat), the ombak beat rate if paired detuning is used, and the drum cues for irama changes.

**MIDI Builder and Plugin Auditor** must check whether the chosen instrument **can be retuned at
all**, because a sampled gamelan locked to 12-tone equal temperament cannot play this material.
Verify the mechanism (scale file, MTS-ESP, per-note bend) and whether the instrument allows two
instances at slightly different tunings for ombak. See `shared/TUNING_AND_MPE.md`. Silent
re-quantisation to 12-tone equal temperament is not acceptable; if the instrument cannot be
retuned, say so and offer a substitution.

**Listener Model** should not treat the beating of paired instruments as a tuning defect, and
should not expect harmonic resolution as the source of arrival. The gong is the arrival.

## Sources and confidence

- Sumarsam, *Introduction, Theory, and Analysis: Javanese Gamelan*, and "Temporal and Density Flow
  in Javanese Gamelan" (Wesleyan). Open first for balungan, irama and colotomy from a
  practitioner-scholar.
- Tenzer, *Gamelan Gong Kebyar: The Art of Twentieth-Century Balinese Music*, Chicago, 2000; and
  "Theory and Analysis of Melody in Balinese Gamelan", *Music Theory Online* 6.2 (2000).
- Sorrell, *A Guide to the Gamelan*, Faber, 1990.
- On ombak and kotekan roles, and on etiquette around instruments: gamelan community and
  institutional sources, which are useful but are not scholarly citations.

Confidence: the absence of a canonical tuning, the colotomic form with the gong at the end, and
the irama density ratios are consistently reported. **To verify:** the exact irama stroke ratios
per level and the kethuk density schemes, which come from glossary-level sources here rather than
from Sumarsam's text; and any specific ombak beat rate in Hz, which is ensemble-specific and was
not confirmed. None of the primary sources were read in full during research.
