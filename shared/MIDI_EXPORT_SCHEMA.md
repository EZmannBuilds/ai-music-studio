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
