# Reference Translation Schema

Use when a user supplies a song, playlist, URL, audio file, analysis report, or named work as a
creative reference.

The goal is to extract transferable musical principles and produce an original result.

```yaml
reference_translation:
  source:
    title:
    artist:
    source_type:
    direct_audio_available:
    metadata_sources: []
  verified_facts:
    tempo:
    key_or_tonal_center:
    duration:
    meter:
    genre_labels: []
    other_measured_or_published_traits: []
  observed_audio_traits: []
  inferred_traits: []
  community_descriptions: []
  transferable_principles: []
  protected_or_identity_specific_material:
    melody:
    lyrics:
    signature_riff:
    exact_chord_sequence:
    exact_sound_recording:
    exact_arrangement:
  new_work:
    different_key_or_pitch_system:
    different_tempo_if_useful:
    new_harmony:
    new_melody:
    new_form:
    new_sound_identity:
```

## Evidence discipline

If direct audio is not available:

- do not claim to hear production details;
- use verified metadata, published analysis, and clearly labeled community descriptions;
- distinguish facts from inference.

Example:

```text
VERIFIED:
119 BPM, B major, 2:46.

COMMUNITY DESCRIPTION:
Some listeners describe it as hyperpop/digicore or chiptune-adjacent.

CREATIVE INFERENCE:
Use a compact, high-energy, digitally abrasive hook-forward design.
```

## Originality rule

A reference should influence dimensions, not be traced.

Prefer transformations such as:

```text
high energy
→ different drum grammar with comparable intensity

bright/dark emotional contradiction
→ new harmonic mechanism

digital abrasion
→ new sound-design family

compact hook-forward form
→ new section proportions
```

Do not reproduce an identifiable melody, lyric, signature riff, or exact musical sequence.
