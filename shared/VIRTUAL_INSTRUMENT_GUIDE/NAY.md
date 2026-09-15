# Nay

Traditions: Arabic maqam practice (Egyptian, Levantine, Iraqi). Context:
`shared/MUSICAL_SYSTEMS/MAQAM.md`. The nay also exists in Turkish makam practice (commonly written
"ney") and in Persian dastgah music, each with a different mouthpiece added to the reed (wood or horn
in Turkey, metal in Iran) and its own repertoire and technique; neither is covered here, and this
page describes the mouthpiece-less Arabic reed only.

An open, obliquely end-blown cane flute, played entirely by breath and lip shaping across the open top
rim with no reed or mouthpiece fitted, and the only wind instrument in Arab art music. This page
covers Arabic practice only.

> Evidence: seven sources read for this pass, five at full depth: two tradition-institution pages
> (MaqamWorld's nay page and its instrument-family overview), a university Arab-music-ensemble
> teaching page, and two Michael Frishkopf ethnomusicology papers on the boundary between secular and
> Sufi/devotional Egyptian performance, in which the nay's own religious associations are directly
> relevant rather than incidental. An Arabic-language practitioner-platform course listing, naming a
> named contemporary nay teacher, was read only as a short promotional page (excerpt depth). The two
> standard reference texts named in the research spec were not opened in this pass. Source IDs
> resolve in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are recorded in
> `research/instruments/NAY.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Nay

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | An open-ended cane tube, blown obliquely across the rim of one open end; there is no reed, fipple or mouthpiece, so the player's own lips and airstream, against the bare rim, are the sound-generating edge tone mechanism | sourced: MAQAMWORLD-NAY; UCSB-MEE |
| attack_behavior | Onset is a breath articulation: the tongue starts and stops the airstream (as on other end-blown and rim-blown flutes this guide documents), shaped by lip position on the rim; no source read describes the nay's attack transient acoustically | inference |
| sustain_behavior | Sustains for as long as breath is supplied and the embouchure holds the edge tone, unlike a plucked instrument; breath is therefore the phrase-length limit (see `phrase_limits`) | inference |
| release_behavior | Ends when the airstream stops or the embouchure breaks contact with the edge; no source read describes a distinct release noise or mechanism beyond breath stopping | inference |
| dynamic_timbre_change | The tradition's own descriptive literature credits the nay with "subtle tonal and dynamic inflections" achieved through breath and embouchure control, without giving the acoustic mechanism (comparable rim-blown-flute mechanisms in this guide's other wind pages link breath pressure to overblowing and spectral brightening, but no source here states that for the nay specifically) | sourced: MAQAMWORLD-NAY + inference |
| register_character | Described as producing "a large variety of liquid sounds and ornaments" in skilled hands and as "one of the most difficult Arabic instruments to play," which the tradition's own literature attributes to the instrument's apparent simplicity concealing real technical difficulty | sourced: MAQAMWORLD-NAY |
| practical_range | **A single nay plays a limited compass; the instrument's actual range is covered by a set of differently-sized nays, not by one instrument.** One source gives nine joints, six front finger holes and one thumb hole as the standard construction, with the most common nay named for and pitched with its first fingerhole open at D4 and its lowest note at C4. A second source gives six or seven finger holes on top and one underneath, open at both ends, and states that a single player uses six or seven nays of different lengths to cover the different pitch levels a piece may need | sourced: MAQAMWORLD-NAY; UCSB-MEE |
| tessitura | No source read gives a tessitura account beyond noting that a player switches instruments (see `practical_range`) rather than playing far outside one nay's comfortable range; this is inference by analogy with other end-blown flutes in this guide, not a nay-specific finding | inference |
| articulation_logic | Breath/tongue articulation for note onset; finger-hole covering (open, closed, and partially covered for pitch shading) for pitch selection; embouchure and breath-pressure inflection for the "liquid," ornamented quality the tradition's literature describes, though no source names specific ornament figures | sourced: MAQAMWORLD-NAY; UCSB-MEE + inference |
| phrase_limits | Bounded by breath, as on any blown instrument; no source read gives a measured breath duration for the nay specifically | inference |
| transitions | Finger-hole covering gives discrete pitch changes; because it is an open tube blown across a bare rim rather than through a fixed fipple, embouchure and breath adjustment can also bend pitch continuously between adjacent notes, by the same general mechanism this guide documents for other rim-blown and lip-controlled wind instruments, though no source read states this for the nay by name | inference |
| repeated_note_behavior | No source read describes nay repeated-note or tonguing-pattern technique specifically | to-verify: a nay pedagogy or performer source on repeated-note articulation |
| vibrato | No source read describes a nay vibrato mechanism (breath vibrato is documented in general for blown instruments elsewhere in this guide, but not confirmed here for the nay specifically) | to-verify: a nay pedagogy or performer source on vibrato technique |
| pitch_instability | As an unfretted, unkeyed, breath- and lip-controlled aerophone, pitch is not fixed to a table the way a keyed or fretted instrument's is; embouchure, breath pressure and partial hole-covering all shift pitch continuously, by the general mechanism this guide documents elsewhere for breath-controlled winds. This is a "Continuous" pitch-behaviour case in `shared/TUNING_AND_MPE.md` section 7's sense, alongside the voice and the fretless oud | inference |
| resonance | Open at both ends (per one source) with no reed or resonating chamber beyond the cane tube itself; no source read describes body or sympathetic resonance for the nay, and its physical construction (a plain open tube) gives little basis to assume any beyond the tube's own air column | inference |
| physical_noise | Breath noise is part of the instrument's documented character: one source calls its sound "warm" and "breathy" directly, distinguishing it from a cleaner-toned wind instrument | sourced: MAQAMWORLD-NAY; UCSB-MEE |
| feasibility | One nay plays one note at a time; the instrument's full working range across a piece is achieved by a player owning and switching between several nays of different lengths, which is a real, physical, timed action (an instrument change), not a free extension of one instrument's range | sourced: UCSB-MEE |
| ensemble_behavior | Belongs to the sahb ("pulling or stretching") family with the violin, set against the naqr family (oud, qanun); it is "the only wind instrument used in Arab art music," inside the heterophonic takht texture described for the tradition generally | sourced: MAQAMWORLD-INSTR; MAQAMWORLD-NAY |
| recording_behavior | No source read describes nay-specific recording practice; breath noise and edge-tone character (see `physical_noise`) make close miking likely to be a meaningful choice, by analogy with other breath-driven instruments in this guide | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Sustains for as long as breath is modelled as continuing, unlike a plucked or struck instrument; holding a note with no breath-noise or dynamic shape under it reads as unnatural for a blown instrument | inference |
| overlap | A true legato transition (if a library records one) is monophonic and needs overlap to trigger, as with other single-line wind instruments in this guide; nothing nay-specific was found beyond that general principle | inference |
| velocity | On a sampled wind instrument, velocity commonly selects breath-attack strength or dynamic layer rather than a fixed loudness; no nay-specific source confirms this, so it is stated as general wind-instrument practice this guide documents elsewhere, not a nay-specific finding | inference |
| continuous_dynamics | A genuinely sustained, breath-driven instrument is exactly the case this guide's general wind and brass treatment says needs a continuous dynamic control to crossfade recorded dynamic layers under a long note, rather than a fixed velocity; no nay-specific source confirms the mechanism for this instrument, so it is applied here by analogy | inference |
| expression | Where exposed, a level trim distinct from the dynamic-layer crossfade above; not confirmed nay-specific | inference |
| articulation_switching | Likely keyswitches or an articulation list for breath-attack type and for the different-length-nay instrument changes described in `feasibility`; switching notes must stay non-sounding | inference |
| round_robins | Would matter for any repeated-note or tonguing pattern, per `COMMON_ERRORS.md` item 1, though this pass could not confirm what nay repeated-note technique looks like (see `repeated_note_behavior`) | to-verify: as above |
| release_samples | Breath and embouchure release character at the end of a note; lost if notes are glued end to end | inference |
| pedal_or_breath_behavior | **Breath is not incidental here, it is the primary continuous control**, carrying both dynamics and, through embouchure interaction, pitch shading; a patch with no breath-modelled continuous control loses the mechanism the tradition's own literature calls "subtle tonal and dynamic inflections" | sourced: MAQAMWORLD-NAY + inference |
| transition_samples | A recorded slide/bend transition, where a library has one, is the plausible carrier for the continuous embouchure-driven pitch shading described in `pitch_instability`; no source read confirms this specifically for the nay | to-verify: whether a modelled nay instrument records genuine embouchure-bend transitions or only discrete note changes |
| mic_or_room_behavior | A recorded or modelled choice; not confirmed nay-specific by any source read | inference |
| likely_fake_sounding_errors | No breath noise anywhere, which contradicts the instrument's documented "breathy" character; a single nay's sample set stretched across a range wider than one physical instrument covers, ignoring the multi-instrument reality in `feasibility`; quantising the variable, embouchure-shaded pitch to a fixed twelve-tone table; a held note with no dynamic or breath shape under it | sourced: MAQAMWORLD-NAY; UCSB-MEE + inference |
| organic_programming_methods | Model breath as the primary continuous control under every sustained note, not only as a velocity trigger; treat a wide-ranging part as several instrument changes (different physical nays) rather than one instrument's continuous range, per `feasibility`; keep the variable, embouchure-shaded pitch on a per-note pitch control rather than a fixed scale file, per `shared/TUNING_AND_MPE.md` section 7's "Continuous" case; leave breath noise audible under and around notes | sourced: MAQAMWORLD-NAY; UCSB-MEE + inference |

---

## Tradition and context

### Construction

A plain, open cane tube, played obliquely, with no reed, fipple or added mouthpiece. One source gives
the construction precisely: nine segments, formed by choosing a length of cane with eight natural
nodes, six finger holes on the front for the fingers and one thumb hole underneath, open at both ends
[sourced: UCSB-MEE]. A second source gives the same finger-hole count and adds that the nine-jointed
cane is played "with the pads of the fingers" [sourced: MAQAMWORLD-NAY]. Neither source gives a
measured tube diameter, wall thickness or bore taper.

### Tuning

There is no single nay tuning to give: each individual nay is built and named for one pitch, defined
by the note sounded with the first fingerhole open, and a player assembles a personal set of nays of
different lengths to cover a piece's needs [sourced: MAQAMWORLD-NAY; UCSB-MEE]. Within one nay, pitch
is not fixed the way a keyed instrument's is: embouchure and breath pressure shift pitch continuously
around each fingering, by the general mechanism this guide documents for breath-controlled winds
elsewhere, though this pass found no nay-specific measurement of how far that shading typically
reaches [inference]. See `shared/TUNING_AND_MPE.md` section 7 for how a continuous, embouchure-shaded
pitch source should be implemented (per-note pitch control, not a fixed scale file).

### Note production and technique

Breath and lip shaping against the open rim generate the tone; there is no reed to do it instead, which
is the nay's most basic difference from a Western flute-family instrument with a fipple or a keyed
head joint [sourced: MAQAMWORLD-NAY; UCSB-MEE]. The tradition's own literature is emphatic that this
apparent simplicity is deceptive: the nay is called "one of the most difficult Arabic instruments to
play," with a skilled player able to produce "a large variety of liquid sounds and ornaments"
[sourced: MAQAMWORLD-NAY].

### Idiomatic phrasing and ornamentation

Ornament in the broader tradition belongs to the jins in play, per `shared/MUSICAL_SYSTEMS/MAQAM.md`,
which this page does not repeat. The nay's own literature names "liquid sounds and ornaments" as a
mark of skilled playing without naming specific ornament figures this pass could confirm
[sourced: MAQAMWORLD-NAY].

### Performer interaction and ensemble role

Sahb family, with the violin, set against the naqr family (oud, qanun), inside the tradition's
heterophonic takht texture; described directly as "the only wind instrument used in Arab art music"
[sourced: MAQAMWORLD-INSTR; MAQAMWORLD-NAY].

### Repertoire contexts

Takht ensemble melody, song accompaniment and taqsim (solo instrumental improvisation), with named
historical exponents recorded by the tradition's own reference literature, including nay players
documented as long-serving members of major twentieth-century Egyptian orchestras
[sourced: MAQAMWORLD-NAY]. The nay also carries a documented devotional and mystical association in
the wider Near Eastern literary and religious tradition, discussed separately below under restricted
repertoire.

### Improvisation

Nay taqsim follows the same sayr-based structure `shared/MUSICAL_SYSTEMS/MAQAM.md` describes for the
tradition generally, and the tradition's own reference recordings are specifically of nay taqsim in
named maqamat [sourced: MAQAMWORLD-NAY]. No nay-specific refinement of the general taqsim account
was found beyond the instrument-switching constraint already noted under Tuning [to-verify: a
nay-specific performer or pedagogy source on taqsim phrasing].

---

## What virtual implementations commonly get wrong

The best-sourced failure for this instrument is treating the nay as one instrument with one continuous
range: the tradition's own literature is explicit that a player uses several physically different nays
for different pitch levels, so a sample set stretched across a range wider than one real nay
misrepresents the instrument [sourced: UCSB-MEE]. A second, well-sourced failure is stripping breath
noise: the instrument's documented character is "warm" and "breathy," and a clean, noiseless render
removes exactly what the sources call out [sourced: MAQAMWORLD-NAY; UCSB-MEE]. A third, not directly
stated by a source but consistent with the breath- and embouchure-driven construction: quantising the
nay's shaded pitch to a fixed twelve-tone table, which removes the continuous pitch-behaviour case
`shared/TUNING_AND_MPE.md` section 7 describes for breath-controlled instruments generally [inference].

## What must not be generalised outside the tradition

Do not assume the Turkish ney or the Persian nay use the same construction: both add a mouthpiece
(wood or horn in Turkey, metal in Iran) that the Arabic nay does not have, per the source read for this
family [sourced: UCSB-MEE]. Do not assume every nay is tuned or ranged like the "most commonly used"
one named here (first-fingerhole note D4, lowest note C4); that is one named reference instance, not
every nay in a player's set [sourced: MAQAMWORLD-NAY]. Do not generalise Egyptian, Levantine and Iraqi
practice as identical; no source read in this pass distinguished them at the construction or technique
level [to-verify: region-specific nay pedagogy or performer sources].

## Restricted and ceremonial repertoire

Under `shared/MUSICAL_SYSTEMS/INDEX.md` rule 5, applied per `MAQAM.md`'s sacred-genre caution:
recitation, the call to prayer, Sufi ritual and Eastern Christian chant are not source material, and
the studio declines to imitate, sample or set new words to them. **The nay's case is stronger than the
oud's or the qanun's, and the sources found here say so directly rather than only by contrast.** A
university teaching source records that the nay carries genuine "philosophical/mystical associations,"
citing the opening lines of Jalal al-Din Rumi's *Mathnawi*, in which the hollow reed instrument is
likened to the human body and its sound is said to express "man's yearning for union with God"
[sourced: UCSB-MEE]. Independently, the ethnomusicological sources read for this pass describe reed
flutes (nay, kawala), unlike the oud and violin, as instruments that *are* traditional in documented
Egyptian Sufi-chant (inshad) ensembles, carrying the wind role in that devotional performance context
[academic: FRISHKOPF-TARAB-2001; FRISHKOPF-MESA-2000]. Both findings are scoped to what their sources
actually document (one literary/religious association, one documented Egyptian ensemble tradition), not
generalised into "the nay is a sacred instrument" as a blanket claim; but taken together, and applying
`shared/MUSICAL_SYSTEMS/INDEX.md` rule 5's caution, this page recommends being deliberately cautious
about presenting a nay taqsim or ornament vocabulary as devotional or Sufi in character even in secular
use, and the studio declines to imitate, sample or set new words to recitation, the call to prayer, Sufi
ritual or Eastern Christian chant regardless of which instrument carries them. The adjacent secular
repertoire the studio does offer is the takht ensemble music, song accompaniment and taqsim this page
otherwise describes [sourced: MAQAMWORLD-NAY].

---

## What the instrument is

An open, mouthpiece-less, obliquely end-blown cane flute, whose tone is generated entirely by the
player's lips and breath against a bare rim, with a documented reputation in its own tradition for
being harder to play than its simple construction suggests [sourced: MAQAMWORLD-NAY; UCSB-MEE]. Its
central programming-relevant fact is that "the nay's range" is not one instrument's range: a player
owns a set of nays of different lengths and changes between them, and breath is the instrument's
primary continuous control for both dynamics and pitch shading [sourced: MAQAMWORLD-NAY; UCSB-MEE].

## Range and register

See `practical_range` above: the most commonly used nay is named for and pitched with its first
fingerhole open at D4, with a lowest note of C4; a full ensemble part's range is covered by several
different nays, not by extending one instrument past its physical compass [sourced: MAQAMWORLD-NAY; UCSB-MEE]. No source read gives a per-nay upper limit in absolute pitch terms [to-verify: what would settle this is not recorded].

## Articulation and note transitions

```text
breath/tongue attack        starts and stops the airstream; the basic articulation event
finger-hole covering        open, closed or partially covered, for discrete and shaded pitch selection
embouchure/breath shading   continuous pitch and timbre inflection around a fingered pitch
instrument change           switching to a different physical nay for a pitch level outside the current one's range
```
[sourced: MAQAMWORLD-NAY; UCSB-MEE]

## Physical constraints

```text
one note at a time; no chords
one physical nay covers one region of the full pitch range a piece may need
breath is finite: phrase length is bounded by lung capacity, as on any blown instrument
```
[sourced: UCSB-MEE + inference]

## Phrase behaviour

Bounded by breath, as with any blown instrument, though no source read gives a measured phrase-length
figure for the nay specifically [inference]. A part that ranges wider than one physical nay's compass
implies an instrument change, which is itself a phrase-boundary event worth planning for, not a free
extension of range [sourced: UCSB-MEE].

## Ensemble behaviour

Sahb family with the violin, the only wind instrument in the standard takht, inside the tradition's
heterophonic texture [sourced: MAQAMWORLD-INSTR; MAQAMWORLD-NAY].

## Recording behaviour

No nay-specific recording-practice source was found or is claimed here; breath and edge-tone noise are
part of the documented character and are plausibly a close-miking consideration by analogy with other
breath-driven instruments in this guide [inference].

## Programming it: the control model

Product specifics (controller identities, exact velocity curves) belong in the calibration profile,
not here [inference].

```yaml
breath_control: the primary continuous control, carrying dynamics and, through embouchure, pitch shading
instrument_set: a wide-ranging part implies several different modelled/sampled nays, not one instrument's continuous range
embouchure_pitch: a per-note pitch/modulation lane, not a fixed scale file, for the continuous shaded pitch
articulation_switching: likely keyswitches or an articulation list for breath-attack type and for nay changes
```
[sourced: MAQAMWORLD-NAY; UCSB-MEE]

## Programming it: what makes it sound real

- Drive dynamics and pitch shading from a modelled breath control under every sustained note, not
  from velocity alone. [sourced: MAQAMWORLD-NAY]
- Treat range beyond one nay's compass as an instrument change, matching the tradition's own
  multi-nay practice. [sourced: UCSB-MEE]
- Keep the shaded pitch on a per-note pitch control, per `shared/TUNING_AND_MPE.md` section 7, rather
  than quantising to a fixed table. [inference]
- Leave breath and edge-tone noise audible; do not clean a "warm, breathy" instrument into a pure
  tone. [sourced: MAQAMWORLD-NAY; UCSB-MEE]
- Shape a taqsim by the sayr (establish, dwell, modulate, return, close on a qafla), as for the
  tradition generally. [sourced: MAQAMWORLD-NAY]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Nay-specific tells:

- one sampled instrument stretched across a range wider than any single real nay covers;
  [sourced: UCSB-MEE]
- no breath or edge-tone noise anywhere, against the instrument's documented "breathy" character;
  [sourced: MAQAMWORLD-NAY; UCSB-MEE]
- a held note with a fixed velocity and no continuous dynamic or pitch shape under it; [inference]
- the variable, embouchure-shaded pitch quantised to a fixed twelve-tone table. [inference]

## What the Performance Director needs from this file

- `breath_or_bow_overruns`: check phrase length against a plausible breath limit, though this pass
  found no nay-specific figure to check against; flag as unverified rather than silent.
- A part spanning more than roughly an octave and a half to two octaves plausibly needs more than one
  modelled nay; check range against `practical_range` and treat a crossing point as an instrument
  change, per `shared/HUMAN_PERFORMANCE_SCHEMA.md`'s feasibility logic.
- `articulation_unavailable`: continuous embouchure-driven pitch shading is unlikely to be modelled by
  a general-purpose sampled flute; report rather than substitute plain pitch bend without checking.
- `intonation` per `shared/TUNING_AND_MPE.md` section 7 is the right record for the shaded pitch, not
  `pitch_system.degrees_cents` alone.
- Where a brief asks for devotional or Sufi-coded material on the nay, treat it under
  `shared/MUSICAL_SYSTEMS/INDEX.md` rule 5 and this page's restricted-repertoire section before
  proceeding.

## Sources and what to verify

Full citations are in `research/sources/INSTRUMENT_SOURCES.md`; claim-level detail and limitations
are in `research/instruments/NAY.md`.

- **Available and used**: construction, range-by-instrument-set, ensemble role and the "difficult to
  play" reputation from MaqamWorld's own nay page and instrument overview (MAQAMWORLD-NAY,
  MAQAMWORLD-INSTR); an independently-worded construction account (nine segments, eight nodes) and the
  Rumi/mystical-association note from a university Arab-ensemble teaching page (UCSB-MEE); the
  devotional-ensemble role of reed flutes from two Michael Frishkopf ethnomusicology papers
  (FRISHKOPF-TARAB-2001, FRISHKOPF-MESA-2000).
- **To verify**: nay-specific repeated-note/tonguing and vibrato technique; a measured or
  pedagogy-stated breath-phrase-length figure; whether a modelled nay instrument records genuine
  embouchure-bend transitions; region-specific (Egyptian v. Levantine v. Iraqi) construction or
  technique distinctions; a nay-specific performer or pedagogy source on taqsim phrasing.
- **Not opened, cited only as standard-reference where used elsewhere in this pack**: Farraj and Abu
  Shumays, *Inside Arabic Music* (FARRAJ-ABU-SHUMAYS-2019); Racy, *Making Music in the Arab World*
  (RACY-2003).
