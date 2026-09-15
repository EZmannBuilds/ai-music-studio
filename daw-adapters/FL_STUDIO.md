# FL Studio Agent Adapter Profile
## Research snapshot, 2026

## Official APIs

### MIDI Scripting API
Python scripts execute inside FL Studio and can access DAW domains such as:
- channels;
- mixer;
- patterns;
- playlist;
- transport;
- UI;
- plugins;
- general project state.

The API originated around controller scripting, so agent integrations should verify which project
operations are actually writable in the installed FL version.

### Piano Roll Scripting API
Python can directly:
- create notes;
- modify notes;
- delete notes;
- create/delete markers;
- inspect PPQ and time signature.

Per-note fields include:
- pitch;
- start time;
- duration;
- velocity;
- pan;
- release velocity;
- color/channel group;
- filter/mod values;
- fine pitch;
- slide;
- portamento.

This is the cleanest official surface for symbolic note generation.

### Third-party MCP bridges
Community projects can bridge the official scripting surfaces, virtual MIDI, and additional
automation into MCP.

Treat them as optional execution layers, not part of core musical reasoning.

## The most important FL Studio concept

By default:

```text
Playlist Track
IS NOT
Mixer Track
```

A Pattern Clip can contain notes for multiple Channel Rack instruments, and those instruments
can route to different Mixer tracks.

An agent trained on linear DAWs can easily make routing mistakes here.

## Recommended agent mode

Unless the user explicitly prefers FL's free-form routing, default substantial generated projects to
**Instrument Track / Track Mode**:

```text
Instrument Channel
↕
Playlist Track
↕
Mixer Track
```

This creates a more deterministic 1:1 relationship and makes:
- naming;
- colors;
- routing;
- plugin loading;
- later agent inspection

more reliable.

## Native composition workflow

### Phase 1 — Channels / instruments

Create the instrument or sample source first.

Assign:
- role;
- name;
- mixer destination;
- intended pattern ownership.

### Phase 2 — Patterns / Piano Roll

Use short patterns for:
- drum grooves;
- bass motifs;
- chord loops;
- hooks;
- fills.

Use Piano Roll scripting for exact note generation.

Do not assume a Pattern equals one instrument unless Track Mode policy says so.

### Phase 3 — Playlist

Arrange Pattern Clips, Audio Clips, and Automation Clips into song form.

Automation Clips are timeline objects and should be treated separately from musical note patterns.

### Phase 4 — Mixer

Confirm Channel Rack → Mixer routing.

Use buses/sends intentionally.

Never infer mixer routing from a Playlist lane unless the project is explicitly using linked
Instrument/Audio Track mode.

### Phase 5 — Render / feedback

Render a preview or stems, then analyze.

## Agent state to read

```yaml
fl_state:
  current_pattern:
  selected_channel:
  channel_to_mixer_map:
  playlist_track_mode_links:
  pattern_contents:
  playlist_clip_placements:
  automation_clips:
  mixer_routing:
  focused_window:
  tempo:
  time_signature:
```

FL operations can be context-sensitive. Read focus/current selection before invoking a script that
operates on the current Piano Roll or Pattern.

## Practical adapter strategy

```text
Music Director
→ FL adapter semantic plan
→ MIDI/Piano Roll script for note operations
→ MIDI Scripting API for project state/routing/transport where supported
→ optional local MCP bridge
```

## Safety
- make a checkpoint FLP before broad edits;
- do not overwrite the current Pattern without confirming target;
- avoid free-form Playlist assumptions;
- verify every Channel's Mixer destination after creating tracks;
- prefer semantic IDs/names over fragile visual indices where possible.


# Performance and tuning

`shared/HUMAN_PERFORMANCE_SCHEMA.md` produces plans that a Standard MIDI File cannot fully carry, and
`shared/TUNING_AND_MPE.md` produces pitch systems that need a mechanism. Both land here.

**These are capability questions, not claims.** The contract's first rule applies: discover what this
connection can actually do before promising any of it, and report what it cannot
(`shared/DAW_ADAPTER_CONTRACT.md`, section 10).

```yaml
ask_this_connection:
  automation_lanes_per_cc:       # can it write a controller curve at all, and how many
  host_parameter_automation:     # can it automate a plugin's own parameters
  per_note_expression:           # can it write per-note pitch, pressure or timbre
  mpe_routing:                   # can it route an MPE zone to an instrument
  tuning_import:                 # scale files, tuning sysex, a tuning master, or none
  articulation_switching:        # keyswitches, channel changes, track splits, or a device
  negative_track_delay:          # needed to compensate sampled legato transition latency
```

FL-specific things to check rather than assume:

- **Automation Clips are Playlist objects**, separate from note data in a Pattern. A performance
  plan's controller curves therefore live somewhere different from the notes they shape, and the
  Playlist-versus-Mixer distinction above applies to them too.
- **Per-note properties are unusually rich here.** The Piano Roll's per-note pan, fine pitch, slide
  and mod values are a direct route for parts of a performance plan that would otherwise need
  separate lanes. Check which of them the installed version exposes to scripting.
- **Slide notes** are a native mechanism for portamento and for pitch gestures; prefer them to a
  channel-wide bend where the instrument supports them.
- Confirm the microtuning route before committing to a pitch system: some instruments accept a scale
  file, some take fine pitch per note, and the two behave differently under transposition.
