# Virtual Instrument Guide

What instruments actually do, and what a sampled or modelled version of one needs from the notes in
order to sound like the real thing.

The structure of every page here is defined in `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md`. Read that
first if you are adding or editing a page.

---

# 1. What this folder is, and is not

This folder holds **instrument behaviour**. That is general and portable: it stays true whoever made
the library on the machine. It is not a vendor list, a buying guide or a patch reference.

```text
instrument behaviour     shared/VIRTUAL_INSTRUMENT_GUIDE/   general, portable, here
product capability       plugin audit                       this machine, this edition
measured response        calibration profile                this patch, this version
product names, formats   shared/FREE_INSTRUMENTS.md         acquisition and licensing
```

The line is drawn like this: "a horn player breathes" belongs here; "this patch's dynamics arrive on
a particular controller and its legato lags a particular number of milliseconds" belongs in a
calibration profile, because the next user has a different library. **What players can do belongs
here too**: breath length, roll speed, reach and the harp's pedal constraint are facts about people,
and a calibration render, which measures a patch, cannot supply them.

**No page in this folder names a commercial product**, and no source ID on a page does either. Where
the research rests on a manufacturer's manual, the page cites a neutral ID such as
`STRINGS-LIBRARY-MANUAL-1`, and the product's name appears only in the source register.

---

# 2. Evidence

Every claim carries a label, as a tag at the end of the sentence, bullet or paragraph it covers, and
every behaviour-card row carries one in its evidence column. The labels (`sourced`, `academic`,
`manual-derived`, `standard-reference`, `inference`, `to-verify`) are defined once, in
`shared/RESEARCH_RULES.md`, with what each maps to among MEASURED, RESEARCH-SUPPORTED and CREATIVE
INFERENCE. `measured` never appears here: it is reserved for the user's own calibration.

Three files hold the evidence:

- `research/sources/INSTRUMENT_SOURCES.md`: every source once, with **how much of it was read**
  (full, section, excerpt, abstract, not read);
- `research/instruments/<page>.md`: one research record per claim, with its scope and its limits;
- `research/sources/WAVE2_SOURCE_SURVEY.md`: what sources exist for instruments not yet written.

`tools/evidence_check.py` checks all of it, so a claim cannot carry a stronger label than its source
was read for. When a page says `inference`, it means no source that was read states the claim; that
is common, and it is honest. When it says `to-verify`, do not use the claim as fact, and say so if
you use it.

Numbers here are **typical ranges from named sources**, never facts about the reader's instrument.
Where the research gave no range, the page says so rather than inventing one.

---

# 3. The pages

**Families** (orchestral, band, studio and keyboard instruments):

| Page | Covers |
|---|---|
| `PIANO_AND_KEYBOARDS.md` | grand and upright piano, harpsichord, celesta, accordion and harmonium, tine and reed electric piano, clavinet |
| `ORGANS.md` | pipe organ; tonewheel and drawbar organ with a rotating speaker |
| `SYNTHS_AND_SAMPLERS.md` | response and change rather than acoustic imitation; glide, voice modes, envelopes, per-note expression |
| `GUITAR.md` | steel-string acoustic, nylon-string classical, electric |
| `BASS.md` | electric bass, fretless, double bass pizzicato |
| `HARP.md` | pedal harp, with a note on the lever harp |
| `STRINGS.md` | violin, viola, cello, double bass, solo and section |
| `BRASS.md` | horn, trumpet, trombones, tuba, the section, mutes |
| `WOODWINDS.md` | flutes, oboe and cor anglais, clarinets, bassoons, saxophones |
| `CHOIR_AND_VOICE.md` | the solo voice and the choir |
| `DRUM_KIT.md` | kick, snare, toms, hi-hat, cymbals; rudiments, ghost layers, brushes |
| `PERCUSSION.md` | orchestral percussion: timpani, snare, bass drum, cymbals, tam-tam, triangle, tambourine, blocks, castanets |
| `MALLETS.md` | marimba, vibraphone, xylophone, glockenspiel, tubular bells, crotales |
| `HAND_PERCUSSION.md` | a frame page: the physics hand drums share, and which page each tradition's drums are on |

**Instruments of named traditions**, on the same footing as the families. Each passed the source gate
in `CULTURALLY_SPECIFIC_INSTRUMENTS.md` section 3, names its tradition under its title, and links its
`shared/MUSICAL_SYSTEMS/` file for context:

| Tradition | Pages | Context |
|---|---|---|
| Hindustani and Carnatic | `TANPURA.md` (both), `SITAR.md` (Hindustani, Maihar gharana), `TABLA.md` (Hindustani), `MRIDANGAM.md` (Carnatic) | `RAGA_AND_TALA.md`, `DRONE_TRADITIONS.md` |
| Arabic maqam | `OUD.md`, `QANUN.md`, `NAY.md` | `MAQAM.md` |
| Ewe dance-drumming | `EWE_DANCE_DRUMS.md` | `EWE_DANCE_DRUMMING.md` |
| Mande jembe music | `JEMBE_AND_DUNUN.md` | `MANDE_JEMBE_MUSIC.md` |
| Central Javanese gamelan | `JAVANESE_GAMELAN_INSTRUMENTS.md` | `GAMELAN.md` |
| Balinese gamelan | `BALINESE_GAMELAN_INSTRUMENTS.md` | `GAMELAN.md` |
| Cuban son and rumba | `CUBAN_HAND_PERCUSSION.md` | `CLAVE_AND_TIMELINES.md` |
| Norwegian Hardanger fiddle music | `HARDANGER_FIDDLE.md` | `MODAL_FOLK_SYSTEMS.md` |
| Scottish Highland piping | `HIGHLAND_BAGPIPE.md` | `DRONE_TRADITIONS.md` |

**Protocol and shared failures:**

| Page | Covers |
|---|---|
| `CULTURALLY_SPECIFIC_INSTRUMENTS.md` | the protocol for an instrument with no page, and the gate a new page must pass |
| `COMMON_ERRORS.md` | the cross-family failures, held once |

## Coverage record

What 2.1 attempted and did not write, so nobody reads an absence as an oversight or a judgement:

| Instrument | Tradition | Status |
|---|---|---|
| Bansuri | Hindustani | **did not pass the gate**: practitioner sources exist but could not be read; only retailer summaries were reachable |
| Kora, shakuhachi, sarangi, Yoruba dùndún | Mande jeliya; Japanese; Hindustani; Yoruba | surveyed, likely to pass next cycle (`research/sources/WAVE2_SOURCE_SURVEY.md`) |
| Balafon, Shona mbira, koto, shamisen, erhu, guzheng, pipa, sarod, steelpan, Turkish ney, Black Sea kemençe | various | surveyed, borderline on reachable sources |
| Dizi, bağlama, klasik kemençe | Chinese; Anatolian; Ottoman | surveyed, likely to fail on reachable sources |
| Frame drums, darbuka, cajón, udu | several traditions each | not yet researched (`HAND_PERCUSSION.md`) |

Most instruments of most traditions have no page. The protocol is the default until one does.

---

# 4. Who reads this folder, and for what

| Reader | Uses it for |
|---|---|
| Performance Director | articulation choice, phrase limits, feasibility, what organic means here |
| Producer | character, register colour, ensemble behaviour, recording behaviour |
| Composer | practical range, idiom, what falls under the hand, written and sounding pitch |
| Vocal Director | `CHOIR_AND_VOICE.md`, and the voice sections elsewhere |
| MIDI Builder | note overlap, what velocity means, articulation switching, release handling |
| Plugin Auditor | what to look for in a patch, and what a calibration pass can and cannot measure |
| Music Critics | whether a part is playable, and whether "fake" is a real finding |

The Performance Director is the heaviest reader. Every page ends with a section addressed to it,
naming the feasibility checks that page supports in `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 5.

---

# 5. Standing rules for this folder

1. **Behaviour before programming.** The instrument comes first; the virtual instrument is the second
   half.
2. **Ranges, not constants.** Every number carries a label and a way to check it.
3. **Name what you do not know.** A `to-verify` line is more useful than a confident invention, and a
   card row nobody could fill says `unresolved:`.
4. **Organic is not random.** Humanisation means systematic, caused deviation at natural magnitude.
   The causes the studio recognises are listed in `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4. An
   imperfection with no cause is a bug, and `deliberately_mechanical` is a legitimate target that
   produces an empty imperfection list.
5. **An instrument of a named tradition gets a page only through the gate**, and otherwise the
   protocol, never a summary (`CULTURALLY_SPECIFIC_INSTRUMENTS.md`).
6. **No product names**, on a page or in a source ID shown on a page.

## Every instrument is culturally specific

A cello belongs to a tradition, has lineages of teaching and a repertoire, and is as specific as an
oud. What differed in 2.0 was not the instruments but the evidence the pack could reach: the
orchestral and studio instruments sit on a large written pedagogy, and many others did not have
readable sources. 2.1 moved that line by researching instruments of ten traditions to the
same standard as the families. It has not closed the gap, and the coverage record above says where
it still is. **An instrument's absence here says something about this pack's sources, not about the
instrument.**
