# Raga and tala

## Cultural context

Raga and tala organise the classical musics of South Asia. **Hindustani** (North Indian) and
**Carnatic** (South Indian) are two distinct systems with different repertoires, different tala
vocabularies, different ornament practice and different performance formats. They share ancestry
and some terminology. They are not one tradition with regional accents.

Within Hindustani music there are further distinctions that matter: **dhrupad** and **khyal** are
different vocal genres with different forms, and instrumental practice (sitar, sarod, bansuri,
sarangi) has its own conventions. Transmission is by lineage, from teacher to student, over years.

## Pitch organisation

**A raga is a grammar, not a scale.** Each raga carries:

- **aroha** and **avaroha**, the ascending and descending forms, which are often not mirror
  images;
- **vadi** (the principal note) and **samvadi** (the second most important);
- **pakad**, an identifying phrase that names the raga to a listener in a few notes;
- **vakra** or crooked motion, where the line is required to bend back rather than move stepwise;
- characteristic **gamaka**, the ornament that belongs to particular notes of this raga.

Bor's *The Raga Guide* (1999) lists exactly these fields per raga. Two ragas can share all seven
svaras and be entirely different pieces of musical behaviour, because the grammar differs.

On microtonal detail: **shruti** theories, including the 22-shruti schemes, are contested and are
not a fixed microtonal tuning table. Do not present a shruti chart as the tuning of the system.

In Carnatic practice the oscillation is not decoration applied to a note. **It is the note.**
Schachter (MTO 21.4) describes gamaka as two basic operations, passing motion (jaru, slides
between svaras) and neighbouring motion (kampita, oscillation between a svara and a neighbour).
Pitch-tracking work treats a Carnatic svara as a contour rather than a point.

## Rhythm and cycle

**Tala** is a cycle. Its structure is what a drummer, a soloist and a listener all count against.

- **Sam** is the first matra of the cycle and is simultaneously the end of one cycle and the
  beginning of the next. It is an arrival, not merely a start.
- **Khali** is an unstressed section, marked by a wave rather than a clap. It creates orientation
  by absence: you know where you are because a stress is missing.
- **Theka** is the conventional pattern of drum syllables and divisions that defines a tala in
  practice. It is the right anchor for drum programming.

Carnatic tala is built from **angas** (laghu, drutam, anudrutam), with the variable length of the
laghu producing the scheme of 35 talas; adi tala is 8 beats as 4+2+2. **This is standard textbook
content but it is to verify**, for example against Pesch, *The Oxford Illustrated Companion to
South Indian Classical Music*, before any output states it as fact.

## Phrase structure and form

Hindustani instrumental form is a **density gradient over fixed pitch material**:

| Stage | What changes | What stays |
|---|---|---|
| alap | unmetred, unaccompanied except for the drone, exploring the raga | the raga's grammar |
| jor | a steady pulse enters | the raga's grammar |
| jhala | tempo greatly increased, or the rhythmic element overtakes the melodic | the raga's grammar |

Then a composition enters in a tala, with improvised development around it. The material does not
get replaced as the piece proceeds. Its treatment gets denser.

This is a general compositional template worth having: hold the pitch material constant and let
density, pulse and rhythmic saturation carry the whole arc.

## Ornamentation

Structural, not optional. Gamaka is raga-specific: which notes oscillate, how wide, and how fast
is part of what identifies the raga. A rendering that plays the svaras as steady pitches with
vibrato added has not simplified the music; it has removed the level on which the identity lives,
especially in Carnatic music.

## The role of improvisation

Most of a performance is improvised, and the improvisation is tightly bounded: by the raga's
grammar, by the tala's cycle and its sam, and by the conventions of the genre and lineage. The
dhrupad alap is improvised within the raga, unmetred and accompanied only by the tanpura drone.

Freedom here is freedom of realisation inside a strict grammar, which is the opposite of "anything
goes" and closer to how a jazz musician improvises inside a form.

## Ensemble behaviour

A soloist (voice or melody instrument), a drummer (tabla in Hindustani, mridangam in Carnatic),
and a drone (tanpura, or an electronic sruti box). The drummer and soloist relate through the
cycle and the approach to sam, not through harmony. The drone does not change. See
`DRONE_TRADITIONS.md`.

## What generalises

- A mode can be defined as behaviour: permitted ascent and descent, a hierarchy of emphasis, an
  identifying phrase, and characteristic ornament. This gives a composer far more to work with
  than a pitch set.
- A form can be a density gradient over unchanging material. Unmetred, then pulsed, then
  saturated.
- A cycle whose downbeat is an arrival changes how phrases are written: the line aims at the cycle
  point from before it, rather than starting on it.
- Orientation by absence (khali) is a usable device in any metre: remove the expected marker to
  tell the listener where they are.

## What must not be casually universalised

- **Time-of-day and rasa associations are tradition to respect, not acoustics to explain.** A
  raga's performance time is a cultural fact carried by the tradition. Do not present it as a
  psychological or physical effect of the pitch set, and do not "discover" a mechanism for it.
- **Shruti theories are contested** and are not a fixed microtonal tuning to load into a synth.
- Hindustani and Carnatic tala vocabularies are not interchangeable.
- Do not generate "a raga" by picking a scale and adding a sitar patch. Without aroha/avaroha, a
  pakad, an emphasis hierarchy and gamaka, there is no raga present.
- Do not harmonise a raga line with chord changes and call the result the tradition. See the note
  in `DRONE_TRADITIONS.md` on what chord changes remove.

## Working with this in the studio

**Composer** sets: the raga with its aroha, avaroha, vadi, samvadi, pakad and vakra motion; the
tala by name with its matra count, sam position and khali position; the theka for the drum; and
the density plan across sections.

**Performance Director** needs: which notes carry gamaka and of what kind (slide or oscillation),
the approach to sam, and the fact that steady-pitch rendering is a failure rather than a neutral
default.

**MIDI Builder and Plugin Auditor** must check whether the instrument supports continuous pitch,
since gamaka is pitch contour and cannot be written as discrete notes. Per-note bend (MPE) or a
monophonic bend line is the minimum. Verify the bend range is declared. See
`shared/TUNING_AND_MPE.md`. A sampler locked to 12 discrete pitches per octave cannot render this
material and the audit should say so.

**Listener Model** should not score a gamaka-heavy line as "unstable pitch" or as expressive
deviation from a target. The contour is the target.

## Sources and confidence

- Bor (ed.), *The Raga Guide: A Survey of 74 Hindustani Ragas*, Nimbus, 1999. Open this first: its
  per-raga fields are the schema.
- Clayton, *Time in Indian Music: Rhythm, Metre, and Form in North Indian Rag Performance*, Oxford
  University Press, 2000. The standard treatment of tal as cyclic metre.
- Schachter, "Structural Levels in South Indian Music", *Music Theory Online* 21.4 (2015), on
  gamaka.
- Sanyal and Widdess, *Dhrupad: Tradition and Performance in Indian Music*, 2004, for dhrupad
  form.

Confidence: the raga-as-grammar and tala-as-cycle accounts are well supported. **To verify:** the
Carnatic 35-tala anga scheme and adi tala's 4+2+2 division (standard textbook content, unconfirmed
in this research pass); Widdess, *The Ragas of Early Indian Music* (1995), which was not
reachable. None of the sources above were read in full during research.
