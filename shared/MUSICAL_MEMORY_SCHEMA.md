# Musical Memory Schema

Track identity at multiple timescales.

```yaml
musical_memory:
  global:
    tonal_center:
    meter:
    tempo:
    core_palette:
    primary_emotion:
    structural_identity:
  section:
    form: []
    section_functions: {}
    section_lengths: {}
    section_harmonic_profiles: {}
    section_energy_profiles: {}
  motifs:
    - id:
      pitch_shape:
      rhythm:
      lyric_or_vocal_shape:
      timbral_identity:
      first_use:
      repetitions:
      transformations: []
  hooks:
    - id:
      type:
      section:
      salience_source:
      memorability_source:
      repetitions:
  rhythmic_cells: []
  bass_cells: []
  harmonic_devices: []
  production_signatures: []
  transition_signatures: []
  mix_signatures: []
```

## Timescale rule

Do not reason only note-to-note.

Music has nested timescales:

```text
note
→ beat
→ bar
→ motif
→ phrase
→ section
→ song
```

A good local decision may still damage long-range identity.

Before inventing new material, ask whether existing material can be transformed instead.


# Above the song

Where a project exists, the timescale list continues:

```text
note → beat → bar → motif → phrase → section → song → project
```

```yaml
musical_memory:
  project_level:
    project_state:               # a reference, not a copy: shared/PROJECT_STATE_SCHEMA.md
    recurring_motifs: []         # material that returns across songs, deliberately
    palette: []
    intentional_callbacks: []
  performance_signatures: []     # timing and articulation habits that identify this project,
                                 # from performance_state.performer_character
```

The same rule applies one level up: a good decision for this song can damage the project's identity,
and a good decision for the project can damage this song. Neither automatically wins, and the studio
names the conflict rather than resolving it silently.
