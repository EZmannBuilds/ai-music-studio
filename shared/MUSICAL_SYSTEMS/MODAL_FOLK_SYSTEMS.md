# Modal folk systems

## Cultural context

This file covers the melody-led modal practices of Ireland, Scotland, England, Anglo-America and
Scandinavia. They are separate traditions with separate repertoires, separate instruments and
separate communities, grouped here only because they share a structural logic.

"Celtic" is a marketing umbrella. Irish, Scottish, Welsh, Breton and Galician musics are distinct,
and within Ireland the regional styles (Sligo, Clare, Donegal, Sliabh Luachra) differ audibly in
ornament and in rhythm. Scandinavian fiddling similarly divides by country and region, with the
Norwegian Hardanger fiddle tradition and the Swedish polska traditions as separate practices.

Transmission is largely aural, through sessions, dances and family lines, with printed collections
as a secondary record rather than as the source.

## Pitch organisation

**Melody carries the mode.** Harmony is optional, and where it exists it is a later addition and
is itself modal.

Breathnach (1971) holds that beyond Ionian, three modes are relevant for Irish folk music: Dorian,
Mixolydian and Aeolian. Irish and Scottish traditional melody often uses **gapped scales** of five (pentatonic) or six
(hexatonic) tones, and a good many Irish tunes are hexatonic in a way that makes a single mode
label ambiguous.

**The gap is the point, not an absence.** Bronson puts it directly: the gapped scales provide the
channels through which, with fewest obstacles, a tune may pass from mode to mode. A missing sixth
or seventh lets a tune be heard as Dorian and Aeolian at once, and lets variants of one tune sit
in different modes without becoming different tunes.

Bronson's survey of Anglo-American ballad tunes found them overwhelmingly modal: about five per
cent had unsystematic gaps and about five per cent had accidentals, usually an inflected seventh,
with the remaining ninety per cent purely modal. **Those percentages describe collected
Anglo-American ballad tunes, not folk music in general.**

**Intonation is not equal-tempered.** (The instrument itself, its understrings and scordaturas, is on
`shared/VIRTUAL_INSTRUMENT_GUIDE/HARDANGER_FIDDLE.md`.) Hardanger fiddle music is modal, with intonation patterns
characterised by great variability, conditioned by shifting contextual factors: melodic formulas,
local tonal centres that often coincide with the open strings, and string resonance. Most tunes
use A-D-A-E tuning, with sympathetic understrings. A scheme attributed to Sven Ahlback divides a
semitone into five positions, each with an accidental, with the microtonally altered notes
primarily C and G in Swedish fiddle tunes; **the original publication was not reachable and this
is to verify.**

Where harmony is used (DADGAD guitar, bouzouki, piano accompaniment), the vocabulary is modal:
open fifths, drones, I to flat VII, i to VII, i to IV in Dorian, double-tonic tunes that alternate
between two centres, and avoidance of the leading tone and the dominant seventh pull.

## Rhythm and cycle

Dance tune types, each with its own metre, phrase length and lilt: reels, jigs, slip jigs,
hornpipes, polkas, strathspeys, polskas, waltzes. The lilt is microtiming and is not written in
the notation. The Scandinavian polska in particular has an asymmetric triple feel whose beat
lengths are uneven by style and region; that is performance practice, not a notational matter.

Most tunes are in eight-bar strains, usually two, each repeated, giving the familiar AABB. This is
regular enough that departures from it are noticeable.

## Phrase structure and form

**Tune-family variation** is the core formal idea. A tune exists as a family of variants across
players, regions and modes, rather than as a fixed text. Variation happens between repetitions and
between players, not as a written-out development section. This is the folk analogue of theme and
variation, and it is collective rather than authorial.

In a session or a dance set, form is made by stringing tunes together and by the number of
repetitions, which is signalled rather than fixed.

## Ornamentation

**Ornament is pitch and rhythm together, not "grace notes" added to a line.** Irish rolls and
cuts, Scottish and piping gracings, and Hardanger trills change the rhythmic articulation of a
note as much as its pitch, and they are how a regional style is recognised. A transcription that
writes them as small notes to be played lightly misrepresents them.

Ornament is also how a repeated note is separated on instruments that cannot rearticulate cleanly,
which makes it structural rather than optional.

## The role of improvisation

Limited in the sense used elsewhere in this folder. The tune is fixed in outline; the player
varies ornament, articulation, phrasing and small melodic details, and chooses which variant of
the tune to play. That variation is expected and is where individual and regional identity lives.

## Ensemble behaviour

Traditionally heterophonic: several players playing the same tune, each ornamenting differently,
with no part subordinate. Accompaniment instruments are a later addition and are optional. Where
accompaniment is present it supports the mode rather than reharmonising the tune.

## What generalises

- A melody can define a mode on its own, with harmony optional. This is directly useful wherever a
  writer reaches for chords before a tune.
- Deliberate gaps in a pitch set create productive ambiguity: a line that can be heard two ways at
  once is a resource, not a problem to be resolved.
- Modal harmonic vocabulary (flat VII to I, double tonic, open fifths, drones, no leading tone) is
  a complete alternative to functional progression, and it is available in any genre.
- Tune-family thinking, where a piece is a family of variants rather than a fixed text, is a way
  to develop material without writing a development section.
- Intonation conditioned by an instrument's open strings and sympathetic resonance is a general
  idea: let the instrument's resonance decide the tuning, rather than the keyboard.

## What must not be casually universalised

- **Do not "correct" a Mixolydian flat seventh into a leading tone.** It is the mode, not a
  missing accidental. The same applies to a Dorian sixth.
- **"Celtic" is a marketing umbrella** over distinct repertoires. Name the tradition, and where it
  matters, the region.
- Do not tune fiddle or pipe samples to 12-tone equal temperament and present the result as
  traditional.
- Do not treat a gapped scale as an incomplete scale to be filled in.
- Do not generalise Bronson's percentages beyond collected Anglo-American ballad tunes.
- Do not write out ornament as decorative small notes and expect the style to survive.

## Working with this in the studio

**Composer** sets: the tradition and region, the tune type with its metre and phrase length, the
final and the gaps (identify these **before** naming a mode), whether harmony is used and in which
modal vocabulary, and the variation plan across repetitions.

**Performance Director** needs: the ornament vocabulary by name for the instrument and style, the
lilt as a microtiming instruction rather than a notation, and the instruction that repeated
strains vary.

**MIDI Builder and Plugin Auditor** must check whether the instrument can be retuned away from
12-tone equal temperament, and whether it can express ornament at the required speed: rolls and
cuts are fast and short, and a sampled instrument with a slow attack or a fixed round-robin will
smear them. Verify that sympathetic resonance, where it is part of the instrument, is present
rather than implied by reverb. See `shared/TUNING_AND_MPE.md`.

**Listener Model** should not treat a flat seventh as a modal borrowing from a major key, should
not expect a dominant to resolve, and should not model an unaccompanied melody as harmonically
incomplete.

## Sources and confidence

- Breathnach, *Folk Music and Dances of Ireland*, Mercier, 1971. Open first for the Irish modal
  account.
- Bronson, *The Traditional Tunes of the Child Ballads*, Princeton, 1959 to 1972, and "A
  Simplified Mode Classification for Traditional Anglo-American Song Tunes", *Yearbook of the
  IFMC*.
- On Hardanger fiddle intonation: Lartillot, Johansson, Elowsson, Monstad and Cyvin, "A Dataset of
  Norwegian Hardanger Fiddle Recordings with Precise Annotation of Note and Beat Onsets", *TISMIR*
  6(1), 2023. It is an annotation dataset, and it does state that intonation is conditioned by
  shifting contextual factors: melodic formulas, local tonal centres and string resonance (read for
  2.1; see `shared/VIRTUAL_INSTRUMENT_GUIDE/HARDANGER_FIDDLE.md`). A 2019 Folk Music Analysis paper,
  "On measuring intonation in Hardanger fiddle tunes", may add to it and was not read. The Hardanger
  Fiddle Association of America tuning guide covers the A-D-A-E and related tunings.

Confidence: the melody-carries-the-mode account and the gapped-scale argument are supported across
Breathnach and Bronson. **Explicitly unverified:** the Ahlback five-positions-per-semitone scheme,
which reaches this file through a secondary summary and whose original publication was not
reached. None of the sources above were read in full during research.
