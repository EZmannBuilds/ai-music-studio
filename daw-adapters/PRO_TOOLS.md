# Pro Tools Agent Adapter Profile
## Research snapshot, 2026

## Official API: Pro Tools Scripting SDK / PTSL

PTSL is the strongest official automation surface among the three DAWs for deterministic
session-management operations.

It is:
- language independent;
- gRPC / Protocol Buffers based;
- available across Pro Tools tiers;
- usable from Python, C++, and other gRPC-capable languages.

Strong uses include:
- open/save/query session;
- create/manage tracks;
- timeline selections;
- memory locations;
- clip/session queries;
- import/export;
- playback/record controls;
- many session-editing operations;
- bounce/export workflows, depending on installed SDK version.

### Important limitation

Do not assume public PTSL exposes complete note-by-note MIDI composition.

For an agent that writes music, the reliable architecture is:

```text
Composer / Lyric Generator / MIDI Builder
        ↓
Standard MIDI File or symbolic note data
        ↓
Pro Tools adapter
        ↓
PTSL for session structure + import + timeline + routing + bounce
```

Use AAX MIDI Effects or Pro Tools MIDI editing for in-DAW generation/manipulation where appropriate.

## Official nonlinear workflow: Pro Tools Sketch

Sketch is a clip-based nonlinear environment with:
- audio clips;
- MIDI clips;
- virtual instruments;
- Scenes;
- Arrangements.

Desktop Pro Tools can move MIDI/audio between Sketch and the normal Pro Tools session.

Agent use:
- explore loops/sections in Sketch;
- commit promising material to the Edit timeline;
- finish detailed production/mixing in the normal session.

## Official MIDI Effects

Pro Tools supports AAX MIDI effect plugins capable of generating/manipulating:
- notes;
- velocity;
- pitch;
- riffs;
- rhythms;
- arpeggiation.

An adapter can use them when the plugin is present, but should not make a song dependent on
a specific MIDI effect unless requested.

## SoundFlow layer

Pro Tools 2025.10+ includes a deep SoundFlow integration and built-in command surface.

SoundFlow can be a useful fallback for operations that:
- are not exposed in public PTSL;
- require UI interaction;
- benefit from macros or conversational control.

Treat PTSL and SoundFlow as complementary:
- PTSL for structured deterministic API operations;
- SoundFlow for broader Pro Tools workflow/UI automation.

## Native production workflow

### Phase 1 — Session foundation
Create:
- tempo/meter;
- markers/memory locations;
- Instrument/MIDI/Audio tracks;
- routing folders and aux paths as needed.

### Phase 2 — Composition
Option A:
external validated MIDI → import.

Option B:
Sketch → MIDI clips/scenes → Edit timeline.

Option C:
AAX MIDI effects → generate/transform.

### Phase 3 — Linear editing
The Edit window is the authoritative detailed timeline.

Use:
- tick-based MIDI/instrument timing for tempo-relative music;
- playlists for alternate takes/comping;
- clip gain/editing for audio;
- automation after structure is stable.

### Phase 4 — Routing / production
Organize with:
- folders;
- routing folders;
- aux tracks;
- buses;
- track presets where appropriate.

### Phase 5 — commit/freeze/bounce
Keep editable sources until decisions are stable.

Then:
- freeze/commit CPU-heavy paths when useful;
- render stems;
- bounce final mixes;
- preserve a pre-commit checkpoint.

## PTSL deployment constraint

Avid's SDK license requires the SDK to be used on the local computer and not hosted as a cloud/server
service for remotely controlling Pro Tools. Licensed products require Avid certificates.

The adapter architecture should therefore be local-first.

## Third-party Python / MCP

Community wrappers such as py-ptsl and experimental MCP servers can reduce implementation effort,
but they are not official Avid SDK distributions. Users still need to obtain licensed SDK materials
from Avid where required.

## Safety
- never ship Avid's protected SDK/proto material inside the Studio skill;
- query track/session state before mutation;
- save checkpoints;
- keep external agent bridge local;
- use public APIs unless the user has an authorized private integration.


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

Pro Tools-specific things to check rather than assume:

- **Note-level work arrives as an imported file.** The performance plan's controller data has to
  survive that import, so verify the lanes exist after import rather than assuming the file carried
  them.
- **Automation is a first-class timeline object** and is the natural home for host-parameter curves
  the MIDI could not carry.
- **Tick-based tracks** keep a performance plan's timing relative to tempo. Sample-based tracks do
  not, and a tempo change will misalign a plan written against bars.
- Confirm what the installed version's scripting surface actually exposes for automation and for
  plugin parameters; the strengths listed above are session and timeline operations, which is not the
  same thing.
