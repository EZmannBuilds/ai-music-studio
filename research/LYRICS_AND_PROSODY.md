# Research: Lyrics and Prosody
## Melody-Conditioned Lyrics, Syllable Alignment, Prosody and MIDI

## Core finding

A useful lyric generator cannot treat lyrics and melody as independent text/music layers.

Research on melody-conditioned lyric generation consistently treats alignment as a core problem.
Useful representations include:
- note ↔ syllable;
- word boundaries;
- phrase/sentence boundaries;
- rests;
- melody duration and pitch;
- higher-level phrase structure.

## 1. Syllable counts are necessary but insufficient

A line can contain the correct number of syllables and still sing badly.

Example:

```text
MUSICAL stress:  STRONG weak STRONG weak
LANGUAGE stress: weak STRONG weak STRONG
```

The count fits.
The prosody fights the sentence.

Therefore candidate validation needs:
- syllable count;
- lexical stress;
- musical metric strength;
- phrase placement.

## 2. Do not impose one-syllable / one-note universally

A common simplified symbolic model maps one syllable to one note.

That is useful as a default.

But songs also contain:
- melismas: one syllable over multiple pitches;
- repeated-pitch rearticulation;
- compressed pronunciation;
- pickup syllables;
- held syllables.

The alignment representation must therefore support one-to-many note mappings.

## 3. Rests carry language structure

Melody-conditioned lyric research has found relationships between rests and lyric boundaries.
Long rests especially make useful candidates for larger phrase/line boundaries.

Agent consequence:

```text
long rest
→ likely breath / phrase boundary
→ avoid forcing one word across it
```

unless interruption is intentional.

## 4. Melody features relevant to lyrics

For each candidate syllable slot, compute:

```yaml
slot:
  bar:
  beat:
  subdivision:
  pitch:
  interval_from_previous:
  duration:
  rest_before:
  rest_after:
  metric_strength:
  melodic_peak:
  phrase_end:
  harmonic_change:
```

Then align semantic/phonological importance.

## 5. Singability layer

Add vocal-phonetic checks beyond NLP fluency:
- long/high notes prefer vowels that sustain comfortably;
- dense runs dislike heavy consonant clusters;
- breaths should fit phrase duration;
- stressed hook words benefit from melodic emphasis;
- names/slang need explicit pronunciation choice.

## 6. Section-conditioned language

Melody fit and section function interact.

Chorus:
- fewer ideas;
- stronger repetition;
- high vowel clarity;
- focal word placement.

Verse:
- more information;
- more specific images;
- greater syntactic variation.

Pre:
- increasing compression or repetition.

Bridge:
- changed viewpoint/rhyme/prosodic density.

## 7. Candidate generation should be constrained search

Rather than:

```text
write lyric
→ hope it fits
```

use:

```text
melody
→ slot map
→ semantic plan
→ several line candidates
→ pronunciation
→ exact alignment
→ stress score
→ singability score
→ revise
```

## 8. MIDI integration

Standard MIDI Files support Lyric Meta Events.

The Studio pipeline therefore exports:
- vocal-note MIDI;
- Lyric Meta Events at syllable onsets when useful;
- sidecar JSON containing exact word/syllable/note mapping.

The JSON remains important because DAWs differ in how visibly they expose lyric metadata.

## 9. Quality metrics

Suggested weighted scoring:

```yaml
weights:
  semantic_fit: 0.20
  exact_syllable_fit: 0.20
  stress_alignment: 0.18
  singability: 0.16
  section_function: 0.10
  hook_or_rhyme_function: 0.08
  originality: 0.08
```

Change weights by genre and task.

## Sources

- SongMASS: Sheng et al., 2020/2021
  https://arxiv.org/abs/2012.05168

- Watanabe et al., "A Melody-Conditioned Lyrics Language Model," NAACL 2018
  https://aclanthology.org/N18-1015/

- Zhang et al., "Syllable-level lyrics generation from melody..." EACL Findings 2024
  https://aclanthology.org/2024.findings-eacl.89/

- SongGLM, 2024
  https://arxiv.org/abs/2412.18107

- Berklee Online, "Lyric Writing: Writing Lyrics to Music"
  https://online.berklee.edu/courses/lyric-writing-writing-lyrics-to-music

- MIDI Association, SMF Lyric Meta Event Definition
  https://midi.org/smf-lyric-meta-event-definition
