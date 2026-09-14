# DAW Agent Adapter Contract
## Version 1.0

The core Music Studio skills remain DAW-neutral.

A DAW adapter translates an accepted musical/production plan into the native concepts of one DAW.
It MUST NOT silently rewrite the musical intent to fit the software.

```text
Music Director / Specialists
        ↓
generic musical state
        ↓
DAW Adapter Contract
        ↓
Ableton / FL Studio / Pro Tools / future DAW
```

## 1. Capability discovery first

Before making changes, the adapter should report what its current connection can actually do.

```yaml
daw_capabilities:
  daw:
  version:
  operating_system:
  connection_layer:
  read_session_state:
  create_tracks:
  create_midi_notes:
  edit_midi_notes:
  create_audio_clips:
  edit_audio_clips:
  create_markers:
  change_tempo_meter:
  load_instruments:
  load_effects:
  edit_device_parameters:
  routing:
  automation:
  nonlinear_scene_workflow:
  linear_arrangement_workflow:
  render_or_bounce:
  analyze_audio:
  undo_or_rollback:
  limitations: []
```

Do not infer capabilities from the DAW name alone.

## 2. Read before write

For an existing project:

```text
READ
→ summarize current state
→ plan mutations
→ validate targets
→ WRITE
→ re-read affected state
→ verify
```

Never assume:
- track index;
- selected clip;
- current pattern;
- current playlist lane;
- current edit selection;
- plugin slot;
- routing;
- tempo;
- project key.

## 3. Native-concept rule

Do not pretend all DAWs use the same object model.

Examples:

```text
Ableton
Session clip / Scene / Arrangement

FL Studio
Channel / Pattern / Playlist Clip / Mixer Track / Automation Clip

Pro Tools
Track / Clip / Playlist / Edit timeline / Sketch / Memory Location
```

The adapter should translate intent into these native objects.

## 4. Mutation safety

Default to:
- create instead of overwrite;
- duplicate before destructive transformation;
- preserve original clips/takes;
- save/version before bulk operations;
- local-only bridges where practical;
- explicit confirmation for destructive bulk edits.

High-risk actions:
- deleting many tracks/clips;
- flattening/committing with source removal;
- destructive audio processing;
- overwriting a session/project;
- replacing plugin chains across many tracks;
- destructive quantization across a full performance.

## 5. Musical object operations

Adapters should expose a compact semantic layer when supported:

```yaml
operations:
  inspect_project:
  set_tempo_meter:
  create_role_track:
  create_section_marker:
  create_midi_clip_or_region:
  write_notes:
  transform_notes:
  place_section:
  set_track_level_pan:
  load_instrument:
  load_effect:
  edit_parameter:
  create_bus_or_group:
  set_routing:
  create_automation:
  render_preview:
  export_stems:
  save_checkpoint:
```

The specialist should request:
> "Create an 8-bar syncopated bass clip in the chorus."

The adapter decides whether that means:
- an Ableton Session clip;
- an FL Pattern/Piano Roll;
- a Pro Tools MIDI clip on the Edit timeline or Sketch.

## 6. State verification

After a write, verify:
- object exists;
- name/role is correct;
- timing is correct;
- routing is correct;
- notes landed on intended instrument;
- no pitched part is accidentally on a percussion-only channel;
- operation affected the intended section only.

## 7. Feedback loop

If the adapter can render/capture:

```text
write
→ render/capture
→ listen/analyze
→ specialist diagnosis
→ revision
```

A DAW adapter does not become the Mix Engineer merely because it can read meters.

## 8. Local security

Third-party MCP/OSC/socket bridges can directly alter sessions.

Recommended posture:
- bind to localhost;
- do not expose a DAW bridge to the public network;
- use authentication/token fencing when available;
- keep project backups;
- inspect third-party code before installing;
- never distribute vendor SDK files when the vendor license forbids it.

## 9. Tool independence

A project should still be representable as:
- musical state;
- track-role state;
- MIDI/audio artifacts;
- automation intent;

even if the target DAW changes.

DAW-specific identifiers belong in adapter state, not in the composition itself.
