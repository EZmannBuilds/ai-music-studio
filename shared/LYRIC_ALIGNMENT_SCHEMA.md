# Lyric ↔ Melody Alignment Schema
## Version 1.0

Use when lyrics must fit an existing vocal melody or MIDI track.

```yaml
lyric_alignment:
  song:
    title:
    language:
    tempo_bpm:
    meter:
    key_or_tonal_center:
  source_melody:
    midi_track_name:
    note_count:
    phrase_count:
    vocal_range:
  section:
    name:
    role:
    bars:
    narrative_function:
    rhyme_strategy:
    repetition_strategy:
  phrases:
    - phrase_id:
      start_bar:
      end_bar:
      rest_before_beats:
      rest_after_beats:
      lyric_line:
      syllable_count:
      available_syllable_slots:
      fit_status:
      syllables:
        - text:
          word:
          syllable_index_in_word:
          lexical_stress: 0|1|2|null
          note_indices: []
          note_pitches: []
          start_beat:
          duration_beats:
          metric_strength:
          melodic_accent:
          melisma: false
          pronunciation_confidence:
```

## Slot model

A syllable slot is normally a note onset, but not every note onset must introduce a new syllable.

Supported mappings:

```text
1 syllable → 1 note
1 syllable → several notes (melisma)
several syllables → repeated/same-pitch note onsets
```

Avoid silently assigning several syllables to one sustained MIDI note unless the performance plan
explicitly subdivides the lyric rhythm without a new pitch onset.

## Metric strength

Estimate local strength from:
- downbeat / beat;
- subdivision;
- syncopation;
- note duration;
- phrase endpoint;
- harmonic change;
- melodic peak or leap.

Use this to align lexical stress to musical stress.

## Rests and boundaries

Longer rests are strong candidates for:
- word/phrase boundaries;
- breaths;
- line endings;
- sentence boundaries.

Do not force a word across a long rest unless that interruption is intentional.

## Verification output

A mapping check is not a pass. A melody built from one fixed syllable-slot template maps perfectly
on every line while every line shares one rhythm (`composer/SKILL.md`, melody-variety gate).

Every final lyric should provide:

```yaml
verification:
  mapping_complete:                # every syllable has a note, a melisma or a held note
  unresolved_pronunciations: []
  stress_conflicts: []
  awkward_consonant_clusters: []
  breath_risks: []
  melismas: []
  pickups: []
  held_syllables: []
  repeated_syllables: []
  rhyme_positions_verified:
  syllables_per_line: {min:, max:, distinct_values:}
  melody_variety_report: {}        # composer/SKILL.md
  lyric_uniqueness_report: {}      # lyric-generator/SKILL.md
  status: pass | flag
```

The same syllable count in every line is a flag, not a success.

Uncertainty is preferable to inventing a pronunciation.
