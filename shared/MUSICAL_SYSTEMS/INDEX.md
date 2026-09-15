# Musical Systems

This folder holds one file per musical system that the studio can work in. This page holds the
rules that govern all of them. Read it before opening any system file.

## Rule 1: a tradition is not a scale

This is the finding that shapes the whole folder. Independent sources in unrelated traditions say
the same thing in different words:

| Source | What it says |
|---|---|
| Abu Shumays (2013) | ajnas, three to five note cells, are the operative units of maqam, not octave scales |
| Bor (1999); Clayton (2000) | a raga is behaviour and a tala is a cycle |
| Sumarsam; Tenzer (2000) | gamelan tuning is per ensemble, and form is colotomic |
| Titon (1977); Evans (1982); Cutting (2018) | blue notes are pitch areas, not flattened degrees |
| Marcus (1993); Akkoc | 24-EDO and 53-comma theory are notations, not measured practice |
| Breathnach (1971); Bronson | gapped scales are the point, not an absence |

The operative units are cells, behaviours, cycles and areas. A file or an agent that emits "System
X equals these seven notes" has failed, even if the seven notes are correct.

What to encode instead: phrase grammar, pivots and stations, cycle markers, ornament as pitch
contour, and intonation as a context-dependent range.

## Rule 2: name the tradition and its people precisely

Never "world", "ethnic", "tribal", "oriental", or a continent used as a genre. Ewe dance-drumming,
Mande jembe music and Cuban rumba are three different practices with different repertoires and
different social functions. Javanese and Balinese gamelan are distinct. Hindustani and Carnatic
are distinct. Arabic maqam, Turkish makam and Persian dastgah are not interchangeable
vocabularies.

## Rule 3: separate learning the logic from presenting output as the tradition

Learning cycle structure, cell-based melody, density gradients, drone relationships and unequal
beats is ordinary musical study. Labelling the result with the tradition's name is a claim about
who made it and how. The studio may do the first freely. The second requires the user to decide,
knowingly.

## Rule 4: credit, and collaborate where possible

Name the sources. Where a project is being released, recommend crediting tradition bearers and,
where the budget and the timeline allow, commissioning or collaborating with them rather than
emulating.

## Rule 5: decline sacred, ceremonial and community-restricted repertoire

Consecrated gamelan sets and temple repertoire, certain ritual drumming, and lineage-held
repertoire are not sampling material. When a request touches this, say so and offer the adjacent
secular or concert repertoire instead.

## Rule 6: never use a tradition as exotic flavour

A characteristic instrument sample laid over otherwise unchanged Western pop harmony and form is
the most common failure mode. If the harmonic language, the phrase structure, the cycle and the
intonation are unchanged, the tradition is decoration. Say that plainly rather than shipping it
quietly.

## Rule 7: every cents table is one measured instance

Any table of cents in this folder describes one ensemble, one performer, or one theorist's
proposal. It is never "the tuning of" the tradition. Label it with whose it is. If the provenance
is unknown, say the provenance is unknown.

## Rule 8: state which system you are in

When explaining theory, name the system the explanation belongs to. Western functional tonality is
one system among the ones documented here, not the neutral background against which the others are
variants. This extends `composer/SKILL.md`, "Cultural caution".

## Rule 9: carry uncertainty forward

The research behind this folder could not read most primary sources in full. Items marked "to
verify" in a system file are to be repeated as "to verify" in output, not quietly promoted to
fact. See `shared/RESEARCH_RULES.md` for the three levels of claim.

## Common section template

Every system file follows this order. A section that does not apply says so in one line rather
than being padded.

```text
# <System name>
## Cultural context
## Pitch organisation
## Rhythm and cycle
## Phrase structure and form
## Ornamentation
## The role of improvisation
## Ensemble behaviour
## What generalises
## What must not be casually universalised
## Working with this in the studio
## Sources and confidence
```

## The system files

| File | The logic it teaches |
|---|---|
| `MAQAM.md` | melodic identity as three to five note cells with a tonic and a pivot, joined into a path |
| `RAGA_AND_TALA.md` | mode as grammar rather than pitch set; form as a density gradient over a cycle |
| `CLAVE_AND_TIMELINES.md` | an asymmetric reference ostinato that every other part is heard against |
| `EWE_DANCE_DRUMMING.md` | a bell timeline, simultaneous four- and six-beat hearings of one cycle, and a lead drum's calls and answers |
| `MANDE_JEMBE_MUSIC.md` | non-isochronous subdivision as metre, measured per piece, and the jembe soloist over the dunun |
| `WEST_AFRICAN_POLYRHYTHM.md` | a pointer only: 2.0's regional bucket, split into the two files above |
| `GAMELAN.md` | nested punctuating cycles, fixed density ratios, interlock, and per-ensemble tuning |
| `ADDITIVE_METERS_BALKAN_TURKISH.md` | unequal beats as the primary metrical level, with the grouping named |
| `BLUES_SYSTEM.md` | pitch areas and a melodic frame that is independent of the chords under it |
| `DRONE_TRADITIONS.md` | harmony as interval-against-a-fixed-reference, with intonation made audible |
| `MODAL_FOLK_SYSTEMS.md` | melody carrying the mode, gapped frames, and ornament as pitch-and-rhythm |
| `JUST_INTONATION.md` | ratios, limits, otonality and utonality, commas, and why JI does not transpose freely |
| `HISTORICAL_TEMPERAMENTS.md` | the trade among pure intervals, note count and transposability; key colour |
| `EDO_SYSTEMS.md` | reading an equal division by the just intervals it approximates and the commas it tempers |
| `CONTEMPORARY_MICROTONALITY.md` | designing timbre and tuning together; notation systems; non-octave periods |

## Who reads this folder

- **Composer** sets the pitch system, cycle and phrase grammar for the brief.
- **Creative Lab** uses these as generative constraints and as sources of unfamiliar structure.
- **Vocal Director** needs the ornament and intonation sections, which are often the vocal line
  itself.
- **Performance Director** needs the cycle, the ornament and the microtiming sections.
- **Listener Model** needs the "what must not be casually universalised" sections, so that
  expectation and surprise are modelled against the right listener.
- **Music Critics, Cultural-Context Critic** audits output against rules 1 to 8.

The Director loads only the file the request needs. Do not load the folder.

Implementation questions (scale files, MTS-ESP, MPE, retuning instruments in a DAW) live in
`shared/TUNING_AND_MPE.md`, not here.
