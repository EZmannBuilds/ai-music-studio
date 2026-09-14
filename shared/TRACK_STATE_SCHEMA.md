# Track State Schema

Use this shared structure when a task spans more than one specialist.

```yaml
track_state:
  identity:
    title:
    artist_project:
    intended_use:
    genre:
    subgenres: []
    references: []
    emotional_target:
    originality_target:
    audience_context:
  musical:
    tempo_bpm:
    meter:
    key_or_tonal_center:
    mode_or_scale:
    tuning:
    harmonic_language:
    chord_progression:
    harmonic_rhythm:
    motifs: []
    melody_notes_or_description:
    bass_concept:
    rhythmic_cells: []
    groove_notes:
  arrangement:
    current_section:
    form: []
    section_lengths: {}
    energy_curve: []
    density_curve: []
    contrast_plan:
    transition_plan: []
  production:
    instrument_palette: []
    sound_roles: {}
    sound_design_notes: []
    automation_plan: []
    spatial_plan:
    texture_plan:
  mix:
    hierarchy:
    masking_risks: []
    frequency_roles: {}
    dynamics_notes:
    stereo_notes:
    depth_notes:
    loudness_target:
  lyrical_vocal:
    lyrical_theme:
    point_of_view:
    narrative_arc:
    vocal_range:
    vocal_character:
    language:
    hooks: []
    locked_lyrics: false
    locked_vocal_melody: false
    source_vocal_midi_track:
    phrase_map: []
    syllable_alignment:
    pronunciation_uncertainties: []
    stress_conflicts: []
  daw_execution:
    target_daw:
    daw_version:
    adapter:
    connection_layer:
    capability_snapshot:
    project_checkpoint:
    native_object_map:
    last_verified_state:
  evidence:
    wavread_findings: []
    reference_findings: []
    rendered_audio_findings: []
  constraints:
    must_keep: []
    must_avoid: []
    available_tools: []
  decisions:
    accepted: []
    rejected: []
    unresolved: []
```

Only populate fields relevant to the task.
Do not invent measurements that were not observed or supplied.


# Session Scope

Track state is project-specific.

Do not carry values into unrelated projects unless the user explicitly requests persistence.

Add:

```yaml
session_scope:
  current_project:
  current_user_preferences_explicitly_given: []
  assumptions_made: []
  variables_left_open: []
```


# Deliverable, instruments and verification

Add to `track_state`:

```yaml
track_state:
  deliverable:
    mode: instrumental | vocal_guide | full_with_vocal
    also_export: []
    muted_for_export: []           # vocal-line and vocal-guide tracks, by role
  instruments:
    plugin_audit_id:
    calibration_profiles: {}       # track -> profile_id, or "unmeasured"
    substitutions: []
    calibration_offer:             # latest offer and the user's answer
  verification:
    last_render_verification:      # shared/RENDER_VERIFICATION.md report
    release_gate: open | blocked
    accepted_by_user: []
    listened_to: true | false
  variety:
    melody_variety_report: {}
    lyric_uniqueness_report: {}
```

Track roles gain `vocal_line` and `vocal_guide`, so an instrumental export mutes by role, not by
guessing from track names.
