# Culturally Specific Instruments

> **This file is a research protocol, not content.**
>
> It contains no summaries of any tradition, and it must not acquire any. An instrument that belongs
> to a living tradition is not described here in a paragraph, because a paragraph is the failure this
> file exists to prevent. What is here is the set of questions to answer, and where to go to answer
> them, before a single note is written.

> Evidence: `musicianship` for the protocol itself, which is a working method rather than a finding.
> The governing reasoning is in `shared/MUSICAL_SYSTEMS/INDEX.md`, whose rule 1 is the basis of this
> file. `shared/FUSION_PROTOCOL.md` carries the bridge requirement when such an instrument is being
> combined with another world.

Cross-family failures are in `COMMON_ERRORS.md`. They all still apply. They are not sufficient here.

---

## 1. Why this file is different from the other thirteen

`musicianship`. The other files in this folder generalise, and generalisation is safe there because a
cello is a cello wherever it is played. It is not safe here, for two reasons.

**The instrument is not separable from its system.** `shared/MUSICAL_SYSTEMS/INDEX.md` rule 1: a
tradition is not a scale. The operative units are cells, behaviours, cycles and areas, not note
lists. An instrument built for one of those systems carries the system in its construction, its
tuning, its ornaments and its idiom, and stripping that out leaves a timbre with a label on it.

**The research surface is bad.** English-language search results about non-Western instruments are
dominated by summaries written for buyers and for sample library marketing. They agree with each
other and are frequently wrong, which is the worst combination available, because agreement reads as
corroboration. So the protocol below replaces the summary: a list of things that must be **found
out**, not a list of things already known.

---

## 2. The protocol

### Step 0: name the thing precisely, before anything else

`musicianship`. Three names, written down, before any note is written.

```text
region          and often a smaller unit than a country
school/lineage  the tradition within the region; performance practice varies between them
repertoire      what is actually being played, and in what context
```

An instrument name alone is not enough to write for. The same instrument in two schools is two
instruments in every way that matters to a part.

### Step 1: route the sources

`musicianship`. Preference order, and it is a hard order.

```text
1. practitioners, teachers and performers of the tradition
2. institutions run by the tradition: conservatories, archives, festival and ensemble bodies
3. ethnomusicological scholarship that names its fieldwork and its informants
4. recordings by recognised performers, listened to, with the performer and school named
5. general-interest English-language summaries and SEO pages
```

Level 5 is where the search engine starts, and it is where this protocol says not to stop. A source
that does not name a school, a teacher or a recording is a source that has already generalised.

`shared/RESEARCH_RULES.md` governs how the findings are labelled once they exist.

### Step 2: the five checks

`musicianship`. These are the questions. Answer all five before writing.

**1. What is the tuning system? Is it twelve-tone equal temperament?**

Usually not. Intervals may be fixed in a way that has no equal-tempered equivalent, or they may be
context-dependent pitch areas rather than fixed points, or they may be set per ensemble or per
instrument. Assume nothing. If the answer is anything but twelve-tone equal, the pitch intent is
carried in cents from a stated reference and reaches the instrument through
`shared/TUNING_AND_MPE.md`. **Never silently quantise it.**

**2. Is the instrument monophonic, and is there a fixed drone?**

Many are one-line instruments with no harmonic function at all. Many are played against a drone that
is structurally the tonal centre rather than an accompaniment. A part written as chords for a
monophonic instrument, or written without the drone that defines its pitch relationships, is wrong at
the level of what the instrument is. See `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`.

**3. What is the ornament vocabulary, and what does an ornament do?**

In many traditions ornaments are **structural, not decorative**: the movement between pitches is the
identity of the phrase, and removing it removes the music rather than simplifying it. An ornament may
be a required approach to a note, a pitch contour that occupies the note's whole duration, or a
marker of a particular melodic cell. Constant Western-style vibrato applied over the top of it is not
a neutral default, it is a different instrument.

**4. What is the rhythmic framework? It is a cycle, not a bar.**

Metrical organisation in many traditions is a cycle with internal structure, marked positions and a
point of resolution, not a repeating bar of equal weight. The cycle may not divide evenly into
Western meter, and the accent structure is usually the point. See
`shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`, `RAGA_AND_TALA.md`,
`ADDITIVE_METERS_BALKAN_TURKISH.md` and `WEST_AFRICAN_POLYRHYTHM.md` for the studio's files on
several such frameworks, and `shared/RHYTHM_SYSTEMS/` for the implementation side.

**5. Is the repertoire restricted, ceremonial or sacred?**

Some repertoire is not for general use, and some instruments are not played outside a context or by
people outside a lineage. This is a real constraint and it is not the studio's to waive. If the
answer is yes or unclear, the finding goes back to the user as a decision, not into the arrangement
as a texture.

### Step 3: write what you found, with its evidence label

`musicianship`. The findings go into the project, not into this file. They carry the labels from
`INDEX.md` and from `shared/RESEARCH_RULES.md`, and they name the school and the source they came
from. A finding about one school is a finding about one school.

---

## 3. The common failure

`musicianship`. Stated plainly, because it is what usually happens.

> A twelve-tone-equal sample patch, played with keyboard chords and constant vibrato, labelled
> "ethnic".

Everything in that sentence is a separate error. The tuning is wrong. The texture is wrong, because
the instrument is probably monophonic and probably has a drone. The ornamentation is wrong, because
constant vibrato has replaced a structural vocabulary. The rhythm is usually wrong, because it has
been placed in bars. The label is wrong, because it names a marketing category rather than a region,
a school and a repertoire. A patch can be perfectly recorded and still produce all five.

---

## 4. A worked example of the protocol

**These are the questions, not the answers.** This section illustrates what applying the protocol
looks like. It deliberately contains no findings, because findings would be a summary, and a summary
is what this file forbids. Read it as a shape to fill in, not as information.

Suppose a brief asks for "a bamboo flute".

```text
Step 0   Which bamboo flute? From where? Bamboo flutes exist across many unrelated traditions
         and share almost nothing but the material. Name the region. Then: which school, and
         which repertoire is the brief actually pointing at? Does the reference recording the
         brief cites name a performer? Which lineage did that performer study in?

Step 1   Who teaches this instrument, and is that teaching written down or recorded in a
         form reachable from here? Is there an institution, archive or ensemble body, or
         scholarship that names its fieldwork? Which recordings are canonical, by whom, and
         can they be listened to rather than read about?

Step 2.1 Is the instrument tuned to twelve-tone equal? If not, what are the intervals in
         cents from what reference, and are they fixed points or context-dependent areas?
         Is the instrument itself built in a fixed key, so that changing key means changing
         instrument?

Step 2.2 Monophonic, presumably, but confirm. Is there a drone, and if so what produces it
         and what is its relationship to the melodic centre? Is the drone optional?

Step 2.3 What are the ornaments called, what do they do, and are any of them obligatory
         approaches to particular pitches? Is there vibrato at all in this tradition, and if
         so is it continuous or is it a specific device? What does a phrase's beginning and
         ending sound like, and is that fixed?

Step 2.4 What is the rhythmic framework? Is there a cycle, how long, with what internal
         marked positions? Where is the point of resolution? Is the music metered at all in
         some sections, and how is a free section structured?

Step 2.5 Is any of this repertoire restricted, ceremonial or sacred? Who says so, and what
         did they say?

Then     Write the findings with labels and sources, take them to the user, and only then
         write a part. If the five checks cannot be answered, say so, and say what is
         missing. A part written on unanswered questions is a guess with a sample library
         on top of it.
```

An empty answer is an unresolved question, not permission to invent one.

---

## 5. Programming notes that do generalise

`musicianship`. Short on purpose.

- **Tuning first.** Whether the instrument can be retuned at all is a Plugin Auditor question, and
  `shared/TUNING_AND_MPE.md` covers the tiers and the fallbacks. If it cannot, the studio says so and
  proposes something, rather than rendering in equal temperament quietly.
- **Monophonic instruments get monophonic parts.** One line, with overlap where the library needs it.
- **Ornament vocabulary is articulation.** Where the library records the tradition's ornaments as
  articulations, use them and do not substitute. Where it does not, that is a finding to report, not
  a gap to fill with pitch bend and vibrato.
- **Drone is a part.** If the tradition has one, it is written, not implied.
- **Cycle is not bar.** The rhythmic framework goes into the project through `shared/RHYTHM_SYSTEMS/`,
  not by forcing a time signature.

## 6. When this instrument meets another world

`shared/FUSION_PROTOCOL.md` governs it, and its **bridge requirement** is the gate: there has to be a
reason the two belong together, expressed as a shared function, not as one tradition supplying
structure while the other supplies decoration. An instrument used as a decorative layer over an
unrelated structure is the interchangeable-decoration tell that protocol was written to catch.

## 7. What the Performance Director needs from this file

- **Do not proceed on an unanswered check.** If steps 0 to 2 are not answered, the feasibility report
  says `blocked`, and it says which of the five is missing.
- `articulation_unavailable` is the normal outcome when a general-purpose library is asked for a
  tradition's ornaments. Report it. Do not approximate it.
- Monophony, drone and cycle length belong in the plan as constraints, not as stylistic preferences.
- Restricted repertoire is a user decision, surfaced as a question, never resolved inside the plan.

## 8. Sources and what to verify

- The governing reasoning is `shared/MUSICAL_SYSTEMS/INDEX.md`, which names its sources per system.
  That folder, not this file, is where a system's findings live.
- **Nothing tradition-specific was researched for this file**, and nothing should be added to it.
  Findings go into the project and into `shared/MUSICAL_SYSTEMS/`.
- `shared/RESEARCH_RULES.md` governs the labels. `shared/TUNING_AND_MPE.md` governs the pitch path.
  `shared/FUSION_PROTOCOL.md` governs combination.
