# MIDI Export Schema

Use for DAW-ready MIDI deliverables.

```yaml
midi_project:
  title:
  tempo:
  meter:
  key_or_pitch_system:
  bars:
  duration:
  smf_type: 1
  conductor_track:
    tempo_events:
    meter_events:
    key_events:
    markers:
  tracks:
    - name:
      role:
      program_or_patch_hint:
      midi_port:
      midi_channel:
      pitch_range:
      articulation_notes:
      controllers:
  automation:
    expression_cc11:
    brightness_cc74:
    modulation_cc1:
    sustain_cc64:
    pitch_bend:
  daw_notes:
    import_method:
    suggested_replacements:
    rendering_notes:
```

## Requirements

For substantial multi-track MIDI:

- use Standard MIDI File Type 1;
- include separate named tracks;
- include tempo and meter;
- include section markers when useful;
- use velocities intentionally;
- preserve automation as MIDI CC or pitch bend where useful;
- verify every required track contains events;
- verify rendered MIDI duration;
- include a human-readable DAW notes file.

## Track-count requests

If a user asks for more than N tracks:

- count musical/percussion tracks, not only the conductor track;
- validate the count programmatically before delivery.

## Guide tracks

A track named:
- Vocal Guide;
- Guitar Guide;
- FX Guide;

represents compositional/performance intent, not a claim that the MIDI produces a finished
human vocal, guitar performance, or sound-design render.

State this clearly in notes.


# Expression, tuning and adaptive exports

Added in 2.0, so that a performance plan and a pitch system survive the export.

```yaml
midi_project:
  expression:
    tier_used: midi2_per_note | mpe | midi1_channel      # the highest the target supports
    per_track:
      - track:
        dynamics_control: velocity | cc1 | cc11 | cc7 | host_parameter | per_note
        lanes: []                # controller number or parameter name, with its curve
        legato_overlap_ms:
        articulation_switching: keyswitch | cc | velocity | separate_track | none
        keyswitch_notes: []      # non-sounding by design; excluded from note audits
    mpe:
      zones: []                  # lower zone, upper zone, and their member channels
      bend_range_semitones:      # declared alongside any bend data
      per_note_controllers: []
    not_carried: []              # what the file cannot hold, handed to the DAW adapter instead
  tuning:                        # shared/TUNING_AND_MPE.md
    pitch_system:
    mechanism: master | scale_file | mts_sysex | per_note_bend | per_channel_bend | none
    scale_file_shipped:          # path, where one travels with the deliverable
    bend_range_declared_semitones:
    what_happens_if_ignored:     # the honest sentence
  performance_plan_sidecar:      # path to the performance state this file executes
  unperformed: true | false      # true when no plan existed; say so in the notes as well
  adaptive_exports:              # shared/ADAPTIVE_MUSIC.md
    per_state_files: []
    segment_tails_ms: {}
    stingers: []
    transition_matrix:
```

## Rules

- **A Standard MIDI File carries MPE only implicitly**, through preserved channel numbers, and cannot
  carry per-note controllers from the newer specification. The export names its tier and states the
  failure mode rather than assuming the receiver.
- **Declare the bend range wherever bend data is written.** A receiver assuming two semitones will play
  a wide-range gesture as noise.
- **Dynamics go to the control that reaches the instrument**, which the plugin audit or a calibration
  pass establishes. A curve written to an ignored controller renders flat, and the failure looks
  musical.
- **Keyswitch notes are listed as non-sounding**, so the note audit in `shared/RENDER_VERIFICATION.md`
  does not report them as silent.
- **Where no performance plan exists**, the artifact is labelled `unperformed`. MIDI Builder does not
  invent expression to fill the gap.
