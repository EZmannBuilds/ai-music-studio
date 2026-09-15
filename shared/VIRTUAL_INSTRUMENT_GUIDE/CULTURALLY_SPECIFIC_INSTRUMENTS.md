# Culturally Specific Instruments

> **This file is the protocol for an instrument this guide has no page for, and the gate a new page
> has to pass.** It contains no summary of any tradition. An instrument that belongs to a living
> tradition either gets a researched page beside `STRINGS.md`, on the same footing, or it gets this
> protocol. It does not get a paragraph, because a paragraph written from thin sources is the failure
> this file exists to prevent.

> Evidence: the protocol is a working method, not a finding [inference]. The governing rules are in
> `shared/MUSICAL_SYSTEMS/INDEX.md`, whose rules 1 (a tradition is not a scale), 2 (name the tradition
> precisely), 5 (decline sacred, ceremonial and restricted repertoire) and 7 (every cents table is one
> measured instance) apply throughout. `shared/FUSION_PROTOCOL.md` carries the bridge requirement
> when such an instrument is combined with another tradition.

Cross-family failures are in `COMMON_ERRORS.md`. They all still apply. They are not sufficient here.

---

## 1. Why a protocol

Every instrument is culturally specific. A cello belongs to a tradition, has lineages of teaching and
a repertoire, and is as specific as an oud [inference]. The difference this file answers is not the
instrument's but the evidence's: the orchestral and studio instruments in this guide sit on a large
body of written pedagogy, orchestration and acoustics that can be read, and for many other
instruments the reachable written sources are thin, secondhand or written to sell a sample library
[inference]. Two things follow.

**The instrument is not separable from its system.** An instrument built for a system carries the
system in its construction, its tuning, its ornaments and its idiom, and stripping that out leaves a
timbre with a label on it (`shared/MUSICAL_SYSTEMS/INDEX.md`, rule 1).

**The research surface is misleading.** General-interest search results about instruments outside
the orchestral and studio canon are dominated by summaries for buyers and for sample-library
marketing. They agree with each other and are frequently wrong, which is the worst combination,
because agreement reads as corroboration [inference]. So the protocol replaces the summary with the
things that must be **found out**.

---

## 2. The protocol

### Step 0: name whose practice, before anything else

Four names, written down, before any note is written. They go into the plan as
`performance_state.performance_reference` (`shared/HUMAN_PERFORMANCE_SCHEMA.md`).

```text
tradition       the named practice, e.g. Hindustani, Ewe dance-drumming, Javanese court gamelan
school/lineage  a gharana, a regional style, a named teacher's practice; "unknown" is an answer
repertoire      what is actually being played, and in what context
region          where it matters, and often a smaller unit than a country
```

An instrument name alone is not enough to write for. The same instrument in two schools is two
instruments in every way that matters to a part.

### Step 1: route the sources

Preference order, and it is a hard order.

```text
1. practitioners, teachers and performers of the tradition
2. institutions run by the tradition: conservatories, archives, festival and ensemble bodies
3. ethnomusicological scholarship that names its fieldwork and its informants
4. recordings by recognised performers, listened to, with the performer and school named
5. general-interest summaries and search-optimised pages
```

Level 5 is where a search engine starts, and it is where this protocol says not to stop. A source that
does not name a school, a teacher or a recording has already generalised. Acoustics papers are
specialist sources, useful for the physics, and never a substitute for level 1 to 3 on practice.
`shared/RESEARCH_RULES.md` governs how the findings are labelled once they exist.

### Step 2: the five checks

Answer all five before writing.

**1. What is the tuning, and who sets it?**

It may be fixed in a way that has no equal-tempered equivalent, context-dependent pitch areas rather
than points, set per ensemble or per instrument, or twelve-tone equal after all. Assume nothing. If
it is anything but twelve-tone equal, the pitch intent is carried in cents from a stated reference,
or as an `intonation` record where it is phrase-shaped, and reaches the instrument through
`shared/TUNING_AND_MPE.md` (section 7 covers what the real instrument allows). **Never silently
quantise it.**

**2. What is the instrument's texture, and what does it sound against?**

One line, two, a melody with its own drone strings, chords, or an interlocking part that only
makes sense with a second player. Is there a drone, from this instrument or another, that is
structurally the tonal centre? A part written as chords for a one-line instrument, as one player for
an interlocking pair, or without the drone that defines its pitch relationships, is wrong at the
level of what the instrument is. See `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`.

**3. What is the ornament vocabulary, and what does an ornament do?**

In many traditions ornaments are **structural, not decorative**: the movement between pitches is the
identity of the phrase, and removing it removes the music rather than simplifying it. An ornament may
be a required approach to a note, a pitch contour that occupies the note's whole duration, or a
marker of a particular melodic cell. A constant vibrato applied over it, in the manner of an
orchestral string or a pop voice, is not a neutral default; it is a different instrument.

**4. What is the rhythmic framework?**

Often a cycle with internal structure, marked positions and a point of resolution rather than a
repeating bar of equal weight; sometimes unmetred; sometimes a subdivision that is not isochronous.
The accent structure is usually the point. The studio's framework files are in
`shared/MUSICAL_SYSTEMS/` and the implementation side in `shared/RHYTHM_SYSTEMS/`.

**5. Is the repertoire restricted, ceremonial or sacred?**

Some repertoire is not for general use, and some instruments are not played outside a context or by
people outside a lineage. **If the answer is yes, the studio declines it** in one sentence, says
why, and offers the adjacent secular or concert repertoire (`shared/MUSICAL_SYSTEMS/INDEX.md`, rule 5;
`shared/FUSION_PROTOCOL.md`). That is not the studio's to waive, and it is not turned into a
question the user can answer away. **If the answer is unclear**, say that it is unclear, ask the user
what they know of the repertoire's context, and do not proceed as if it were unrestricted.

### Step 3: write what you found, where it belongs

Findings carry the labels of `shared/RESEARCH_RULES.md` and name the school and the source they came
from. A finding about one school is a finding about one school. Where they go:

- **for this project**: into the project's notes and the plan, always;
- **the instrument's physical and performance behaviour**, if it passes the gate in section 3: a new
  page in this folder, with its research records in `research/instruments/`;
- **the tradition's theory, history and aesthetics**: the tradition's file in
  `shared/MUSICAL_SYSTEMS/`, never the instrument page. The two link to each other and do not
  duplicate each other.

---

## 3. The gate for a new page

A page for a tradition-specific instrument is written only when all of these hold. Failing any, the
instrument stays on this protocol, and the coverage record in `INDEX.md` says why.

1. **At least two independent specialist sources, each read at section depth or more**, and entered
   in `research/sources/INSTRUMENT_SOURCES.md` with their read depth.
2. **At least one of them is practice**: a practitioner or teacher, an institution of the tradition,
   or ethnomusicology that names its fieldwork. Acoustics papers count as specialist, not as this one.
3. The page names its tradition precisely under its title, links its `shared/MUSICAL_SYSTEMS/` file,
   and carries the behaviour cards of `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md` with an honest
   `unresolved:` wherever the sources were silent.
4. It has three sections an orchestral page does not need: **what virtual implementations commonly
   get wrong**, **what must not be generalised outside the tradition**, and **restricted and
   ceremonial repertoire**. `tools/evidence_check.py` checks for them.
5. Every claim is labelled no more strongly than its source was read.

**Passing the gate does not make a page authoritative.** It makes it better sourced than a summary.
Review by a tradition bearer or teacher is the step that would, and a page says whether it has had
one.

---

## 4. The common failure

Stated plainly, because it is what usually happens:

> A twelve-tone-equal sample patch, played with keyboard chords and constant vibrato, labelled
> "ethnic".

Every part of that sentence is a separate error [inference]. The tuning is wrong. The texture is often
wrong: chords on an instrument that plays one line, one player where the tradition interlocks two, no
drone where there should be one. The ornamentation is wrong, because constant vibrato has replaced a
structural vocabulary. The rhythm is usually wrong, because it has been placed in bars. The label is
wrong, because it names a marketing category rather than a tradition, a school and a repertoire. A
patch can be perfectly recorded and still produce all five.

---

## 5. A worked example of the protocol

**These are the questions, not the answers.** Suppose a brief asks for "a bamboo flute".

```text
Step 0   Which bamboo flute? Bamboo flutes exist across many unrelated traditions and share
         little but the material. Name the tradition. Then: which school, and which repertoire
         is the brief pointing at? Does the reference recording name a performer? Which lineage
         did that performer study in?

Step 1   Who teaches this instrument, and is that teaching written down or recorded in a form
         reachable from here? Is there an institution, archive or ensemble body, or scholarship
         that names its fieldwork? Which recordings are canonical, by whom, and can they be
         listened to rather than read about?

Step 2.1 Is it tuned to twelve-tone equal? If not, what are the intervals in cents from what
         reference, and are they fixed points or context-dependent areas? Is the instrument built
         in a fixed key, so that changing key means changing instrument?

Step 2.2 One line, or more? Is it played against a drone, and if so what produces it and what is
         its relationship to the melodic centre? Does it ever play with a second instrument of its
         own kind, and how do the two relate?

Step 2.3 What are the ornaments called, what do they do, and are any obligatory approaches to
         particular pitches? Is there vibrato at all, and if so is it continuous or a specific
         device? What do a phrase's beginning and ending sound like?

Step 2.4 What is the rhythmic framework? Is there a cycle, how long, with what marked positions?
         Where is the point of resolution? How is a free section structured?

Step 2.5 Is any of this repertoire restricted, ceremonial or sacred? Who says so, and what did
         they say?

Then     Write the findings with labels and sources, take them to the user, and only then write a
         part. If the checks cannot be answered, say so, and say what is missing. A part written
         on unanswered questions is a guess with a sample library on top of it.
```

An empty answer is an unresolved question, not permission to invent one.

---

## 6. Programming notes that do generalise

Short on purpose [inference].

- **Tuning first.** Whether the instrument can be retuned at all is a Plugin Auditor question, and
  `shared/TUNING_AND_MPE.md` covers the tiers and the fallbacks. If it cannot, the studio says so and
  proposes something, rather than rendering in equal temperament quietly.
- **Write the texture the instrument has.** One line gets one line, with overlap where the library
  needs it; an interlocking part gets its partner.
- **Ornament vocabulary is articulation.** Where the library records the tradition's ornaments as
  articulations, use them and do not substitute. Where it does not, that is a finding to report, not
  a gap to fill with pitch bend and vibrato.
- **A drone is a part.** If the tradition has one, it is written, not implied.
- **A cycle is not a bar.** The framework goes into the project through `shared/RHYTHM_SYSTEMS/`, not
  by forcing a time signature.

## 7. When this instrument meets another tradition

`shared/FUSION_PROTOCOL.md` governs it, and its **bridge requirement** is the gate: there has to be a
reason the two belong together, expressed as a shared function, not as one tradition supplying
structure while the other supplies decoration.

## 8. What the Performance Director needs from this file

- **Do not proceed on an unanswered check.** If steps 0 to 2 are not answered, the feasibility report
  says `blocked`, and it says which check is missing.
- `articulation_unavailable` is the normal outcome when a general-purpose library is asked for a
  tradition's ornaments. Report it. Do not approximate it.
- Texture, drone and cycle length belong in the plan as constraints, not as stylistic preferences.
- Restricted repertoire is declined, per check 5; only an unclear case goes back to the user, as a
  question, and the plan waits for the answer.

## 9. Sources and what to verify

- The governing reasoning is `shared/MUSICAL_SYSTEMS/INDEX.md`, which names its sources per system.
- **Nothing tradition-specific is researched in this file**, and nothing should be added to it.
  Researched instruments have their own pages; `INDEX.md` lists them by tradition, with the ones that
  did not pass the gate.
- `shared/RESEARCH_RULES.md` governs the labels. `shared/TUNING_AND_MPE.md` governs the pitch path.
  `shared/FUSION_PROTOCOL.md` governs combination.
