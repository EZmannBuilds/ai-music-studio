---
name: lyric-generator
version: 1.0
description: Writes original lyrics that fit the song's narrative, section roles, vocal melody, MIDI note timing, syllable capacity, lexical stress, breaths, rhyme, and singability.
---

# Lyric Generator

## Mission

Write lyrics that behave as part of the composition rather than prose pasted onto notes.

The Lyric Generator can work:
- before a melody exists;
- with a rough melodic contour;
- with an exact MIDI vocal track;
- during revision after a vocal demo.

When an exact MIDI melody exists, melody fit outranks preserving a first-draft lyric.

## Inputs

Accept whichever are available:

```yaml
lyric_brief:
  theme:
  story_or_character:
  point_of_view:
  emotional_arc:
  language:
  explicitness:
  imagery_world:
  forbidden_topics_or_phrases: []
  reference_principles: []
  form:
  vocal_melody:
  midi_track:
  vocal_range:
  rhyme_preference:
  repetition_preference:
```

Do not require artist references.

## Core pipeline

```text
1. READ SONG INTENT
2. READ SECTION FUNCTION
3. PARSE VOCAL MELODY / MIDI
4. BUILD PHRASE + SYLLABLE-SLOT MAP
5. PLAN NARRATIVE / IMAGE / HOOK
6. GENERATE MULTIPLE LINE CANDIDATES
7. COUNT + PRONOUNCE SYLLABLES
8. ALIGN WORD STRESS TO MUSIC
9. TEST SINGABILITY
10. TEST RHYME / REPETITION
11. REVISE TO A SINGABLE FIT
12. EXPORT TEXT + ALIGNMENT + OPTIONAL MIDI LYRIC EVENTS
```

## Melody-first mode

When a vocal MIDI track is provided:

### A. Detect phrases

Use:
- rests;
- note gaps;
- section markers;
- long notes;
- repeated motifs;
- cadence points.

### B. Build syllable slots

Default:
```text
one note onset ≈ one new syllable
```

But allow:
```text
one syllable → multiple notes
```
for intentional melisma.

Do not force a strict 1:1 model when the melody clearly contains melismas.

**The fit to aim for is singable, not exact:** every syllable has a home (a note, a melisma, a
pickup or a held note), and the fit is judged by stress, breath and meaning, not by a syllable
count equal to the slot count.

If the supplied melody fails Composer's melody-variety gate, for example uniform eight-note
lines on one rhythm, return it to the Composer through the Director instead of filling it.

### C. Read musical stress

Prefer important lexical syllables on:
- strong beats;
- longer notes;
- melodic peaks;
- accented leaps;
- cadence notes;
- harmonically important changes.

Prefer articles, prepositions, auxiliary words, and other weak syllables on:
- pickups;
- weak subdivisions;
- shorter passing notes.

This is not absolute. Syncopation may intentionally displace language.

## Syllable counting

### English

Prefer a pronunciation dictionary with stress information when available.

Fallback:
1. pronunciation/G2P model;
2. language-aware syllabifier;
3. heuristic count;
4. flag uncertain words.

Never hide uncertainty around:
- contractions;
- dialect pronunciation;
- names;
- slang;
- compressed singing pronunciation;
- words with multiple accepted pronunciations.

Example:

```yaml
word: "every"
possible_syllables: [2, 3]
chosen: 2
performance_pronunciation: "ev-ry"
confidence: medium
```

## Stress alignment

Track lexical stress:

```text
0 = unstressed
1 = primary stress
2 = secondary stress
```

Score candidates for:
- strong syllable on strong music;
- phrase endpoint on intentional word;
- hook word on memorable note;
- natural conversational accent.

Bad prosody example:
> "I LOVE the way YOU forGET me"

when the intended sentence stress is incompatible with the melody.

The tool may preserve a deliberate mismatch when it creates a desired unstable effect, but it
must label it intentional.

## Singability

Check:
- vowel quality on long/high notes;
- consonant clusters on rapid notes;
- plosives on exposed sustained entrances;
- breath length;
- repeated difficult consonants;
- range + vowel interaction;
- word boundary at large leaps;
- tongue-twister risk.

Prefer open/sonorous vowels on long sustained notes when semantic options allow.

## Rhyme

Rhyme is a musical device, not a mandatory end-of-line decoration.

Plan:
- rhyme position;
- rhyme strength;
- stability vs instability;
- chorus repetition;
- internal rhyme where rhythm benefits.

Do not force perfect rhyme at the expense of natural stress or meaning.

## Section behavior

### Verse
Prioritize:
- information;
- imagery;
- specificity;
- progression.

### Pre-chorus
Prioritize:
- narrowing language;
- tension;
- repeated syntax;
- unfinished thought.

### Chorus
Prioritize:
- hook;
- vowel clarity;
- lower semantic load;
- high recall;
- tight melodic fit.

### Bridge
Prioritize:
- perspective change;
- new syntax/rhyme density;
- revelation or destabilization.

These are defaults, not laws.

## Music matching

Lyrics must respond to:
- tempo;
- rhythmic density;
- section energy;
- harmony;
- melodic contour;
- arrangement density;
- vocal production plan.

Example:
A sparse 70 BPM line with long held notes can carry longer open words.
A 170 BPM sixteenth-note run may need short syllables, clipped syntax, or intentional rapid-fire
language.

## Narrative continuity

When the track has a story:
- track what the narrator knows;
- avoid repeating verse information unless the repetition changes meaning;
- reserve important images for appropriate sections;
- make chorus wording compatible with every chorus occurrence or intentionally revise later chorus.

## Reference use

If an artist/song reference is supplied, transfer only abstract lyric principles:
- density;
- directness;
- repetition;
- perspective;
- image logic;
- rhyme looseness.

Do not imitate recognizable lyric lines, signature phrasing, or an identifiable living artist's voice.

## Candidate scoring

```yaml
lyric_candidate:
  semantic_fit: 0-5
  syllable_fit: 0-5              # a singable home for every syllable
  stress_alignment: 0-5
  singability: 0-5
  hook_strength: 0-5
  rhyme_function: 0-5
  section_function: 0-5
  originality: 0-5
  cross_song_distinctness: 0-5
```

Reject candidates that score highly semantically but cannot be sung naturally over the melody.

## Revision order

When the line does not fit:

```text
1. preserve core meaning
2. preserve important hook/focal word
3. fix syllable count
4. fix lexical stress
5. fix breath/singability
6. restore rhyme if useful
7. re-check meaning
```

Do not solve a one-syllable overflow by arbitrarily cramming two syllables into a short note.

## MIDI output

When requested, hand off to MIDI Builder.

MIDI Builder may:
- add Standard MIDI File Lyric Meta Events at syllable onsets;
- preserve section markers;
- emit a sidecar alignment JSON;
- leave continuation notes without a new lyric event during a melisma.

The sidecar alignment is authoritative when a DAW does not display lyric events consistently.

## Quality gate

Before finalization:

```text
[ ] syllable counts verified
[ ] note/syllable mapping verified
[ ] stress conflicts reviewed
[ ] rests/breaths reviewed
[ ] rhyme positions intentional
[ ] hook words on useful musical events
[ ] no accidental tongue-twisters
[ ] section narrative function achieved
[ ] melody not silently changed unless authorized
[ ] uncertain pronunciations surfaced
[ ] earlier lyric corpus loaded and reuse ledger built
[ ] no spent word or image used as a title, hook word or verse opener
[ ] verse openers differ in shape from the last five songs
[ ] section form differs from the most recent song
[ ] syllables per line vary; pickups, held syllables or melisma used where the melody allows
[ ] melody passed Composer's variety gate, or was returned upstream
[ ] uniqueness report attached
```


# Cross-song uniqueness

## Why

An agent that keeps no memory of its earlier songs cannot notice reuse. Melody-first writing
faithfully fills a uniform melody, which yields uniform lines. Across a run of songs, that shows
as one section form, one verse-opener shape and one small vocabulary of images.

## Prior-corpus check, before writing

1. Load the studio's earlier lyrics: every lyric file and lyric-alignment file in the song
   folders under the profile's `paths.output_root`, newest first.
2. Build a reuse ledger:

```yaml
lyric_reuse_ledger:
  songs_checked: []
  spent_words: {}               # content words found in 2 or more earlier songs, with counts
  spent_images: []              # recurring scenes and objects: a room, a door, a light
  first_line_templates: []      # the syntactic shape of each verse opener
  section_forms: []             # lines per section, section order, ending device
  hook_devices: []              # e.g. inverting the hook in the final chorus
  line_length_profiles: []      # syllables per line, per song
```

3. When the user supplies an identity or artist corpus for the song, it is identity evidence.
   Lines the user wrote themselves are never reused.

## Rules

Defaults below are CREATIVE INFERENCE; the brief or the user may override any of them.

- A spent word or image may appear only where the brief needs it: never as a title image, a
  hook word or a verse opener, and at most once per song.
- No verse opener may share a syntactic shape with a verse opener from the last five songs.
- The section form must differ from the most recent song's in at least one structural way:
  lines per section, section order, whether there is a pre-chorus, what the bridge does, or how
  the song ends.
- Do not use the same hook device in consecutive songs unless the user asks.
- Vary syllables per line. Use pickups, held syllables and melisma; let a line run short or long
  when the phrase needs it.
- A deliberate callback across songs, such as an album motif, is allowed only when the user asks
  for it, and is recorded as intentional.

## Uniqueness report, with every final lyric

```yaml
lyric_uniqueness_report:
  corpus_checked: []
  spent_words_used: [{word:, count:, role: incidental | focal | hook}]
  shared_images: []
  first_line_template_matches: []
  section_form_matches: []
  hook_device_matches: []
  syllables_per_line: {min:, max:, distinct_values:}
  intentional_callbacks: []
  status: pass | flag
```

## Instrumental deliverable

When the deliverable is instrumental (`music-director/SKILL.md`), lyrics are written
only when the user asks for them.
