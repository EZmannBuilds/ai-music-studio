# Ableton Live Agent Adapter Profile
## Research snapshot, 2026

## Recommended integration stack

### Official: Ableton Extensions SDK
Best for:
- discrete context-menu actions;
- reading/editing tracks and clips;
- MIDI transformations;
- project analysis/reorganization;
- one-shot generative operations.

Current limitation:
Extensions are currently a Live 12 Suite beta feature and run as discrete invoked tasks rather
than a continuously running background agent.

### Official: Max for Live + Live Object Model
Best for:
- persistent in-Live devices;
- observing Live state;
- manipulating Live objects;
- custom control and generative systems;
- MIDI generation/transformation.

### Official: Live 12 MIDI Tools
Best for:
- in-clip note generation;
- transformations;
- scale-aware musical operations;
- editable custom Max for Live generators/transforms.

### Third party: AbletonOSC / MCP bridges
Best for:
- external agent control;
- natural-language session manipulation;
- bidirectional state loops.

Treat all third-party bridges as untrusted until inspected.

## Native object model

```text
Live Set
├── Session View
│   ├── Tracks
│   ├── Clip Slots
│   ├── MIDI/Audio Clips
│   └── Scenes
└── Arrangement View
    ├── linear clips
    ├── automation
    └── locators
```

Do not flatten Session and Arrangement into one timeline concept.

## Agent-native composition workflow

### Phase 1 — Session sketch

Create:
- role-based tracks;
- short clips;
- scene rows for musical sections.

Example:

```text
Scene 1  Intro
Scene 2  Verse
Scene 3  Pre
Scene 4  Chorus A
Scene 5  Chorus B variant
Scene 6  Bridge
```

Generate multiple clip candidates without committing to final chronology.

### Phase 2 — Audition

Launch scenes/clips and compare:
- groove;
- harmony;
- density;
- hook strength;
- transition potential.

Preserve rejected variants in unused clip slots when inexpensive.

### Phase 3 — Commit to Arrangement

Record Session performance into Arrangement or deliberately place selected clips.

Now solve:
- exact song length;
- micro-transitions;
- fills;
- automation;
- dropouts;
- pickup bars.

### Phase 4 — Production

Use:
- device chains/racks;
- sends/returns;
- resampling;
- audio-to-MIDI or MIDI transformation as appropriate;
- clip automation / track automation.

### Phase 5 — Mix / render loop

Group logical families, balance, render/capture, analyze, revise.

## Agent rules

- Use Session View for divergent search.
- Use Arrangement View for final chronology.
- Read clip loop length before replacing notes.
- Respect scale state when generating scale-aware material.
- Prefer duplicate/variant clips before destructive MIDI transformation.
- Separate device parameter automation from note-generation intent.
- If using Extensions SDK, design one-shot tools with explicit input and output.
- If using OSC/MCP, re-read state after writes.

## Strong bridge choices

### Long-term official route
Extensions SDK + Live API concepts.

### Deep in-DAW generative route
Max for Live + Live Object Model + MIDI Tools.

### Agent bridge today
A local MCP/OSC bridge on top of AbletonOSC / Remote Script / LOM.

## Security
Keep OSC/socket control on localhost unless there is a deliberate authenticated remote setup.
Back up Sets before granting an agent broad write access.


# Field notes: Ableton Live 12 with the AbletonMCP remote script

> Checked with Ableton Live 12 and the third-party AbletonMCP remote script. Re-check on any other
> connection or Live version before relying on it.

## Connection limits (AbletonMCP remote script)

- **Mixer volume, pan and sends are read-only over this connection.** Set level with EQ Eight's
  output gain (up to +12 dB), and placement and width with Utility, on each track. Return tracks
  can exist in the set and still be unusable from the agent.
- **The loader finds browser items only under Live's own browser categories and the User
  Library, not in the Current Project folder.** To load a generated clip or preset, place it in
  the User Library for the load, remove it afterwards, and keep a copy with the project.
- **Export and Save dialogs are not reachable through the connection.** Drive them on screen,
  with the user's permission. The Rendered Track menu is a pop-up, which screen control that does
  not take over the display cannot open. Positions depend on the display layout: take a
  screenshot before every click. In the save panel, Cmd+Shift+G goes straight to a folder.

## Stock instruments

- **Stock Instrument Racks can hide brightness behind macros.** Open these before adding EQ
  shelves:
  - Ac Strings Orch: "Tone";
  - Harp Concert and Celeste: "Filter Cutoff", which default to 26 and 0;
  - Grand Piano: "Bright".

  EQ shelves barely move the top end until those macros are opened.
- **The stock Grand Piano's wide stereo image can pull the mix's L/R correlation negative.**
  Narrow the piano with Utility (width about 0.5) with Bass Mono on, and narrow wide leads too.

## Spitfire BBC Symphony Orchestra (VST3) in Live

The Discover edition is free; its entry is in `shared/FREE_INSTRUMENTS.md`.

- **MIDI CC1 written as clip envelopes does not reach the BBC SO VST3 in Live**, so a part
  written that way renders with no dynamics.
- **Clip envelopes aimed at the plugin's own host parameters, Dynamics and Expression, work.**
  They can be written into the `.als` file's XML with the set closed, then the set reopened.
- **Discover's single mix signal is very wide and dark.** Narrow it by measured correlation, not
  by a fixed amount.

## Stems

**Live exports stems itself: Export Audio/Video with Rendered Track set to "All Individual
Tracks".** One export writes every track, every return track and the Main mix into the chosen
folder, over the same time range; the Main mix takes the file name given in the save panel, and
each track adds its own name. Use it on every pass for `shared/RENDER_VERIFICATION.md`.

## Calibration passes in Live

For a `plugin-auditor` calibration pass:
- build a new scratch set from a template; never calibrate inside a song's set;
- one MIDI track per instrument, no effects, mixer left at its defaults (it cannot be set over
  this connection anyway);
- write the test clips: range sweep, velocity ladder, dynamics sweep, sustained note;
- for an instrument whose dynamics are host parameters, write the dynamics sweep as an envelope
  on that parameter;
- a limiter on the Main track caps the ff measurements: bypass it for calibration where levels
  allow, or record it in the profile;
- export All Individual Tracks and analyze each file.

## Sample packs in Live

- Sample folders come from the user's profile (`paths.sample_libraries`).
- **The AbletonMCP loader finds browser items only under Live's own categories and the User
  Library, not under Places or Current Project.** A pack is reachable by that loader only through
  a folder or link inside the User Library. Live's own browser can also see it through Places >
  Add Folder, which is a user action in Live.
- **Ask before adding a large pack to Live's browser.** Live reads what it indexes, and on a
  synced drive that can start downloading every file.
- A dragged or loaded sample on a synced drive downloads on first use. For packs in regular use,
  keep the folder downloaded locally.


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

Live-specific things to check rather than assume:

- **Clip envelopes and plugin parameters are different targets.** A controller written as a clip
  envelope may not reach a plugin at all, while an envelope on that plugin's own host parameter does.
  This is the single most common cause of a part rendering with no dynamics, and it is per plugin.
  Test it once per instrument and record the answer in the calibration profile.
- **Session and Arrangement hold automation differently.** A performance plan committed in Session
  View may not survive the move to Arrangement in the way a linear timeline would.
- **Track delay** is the right place to compensate sampled legato latency, not dragging notes.
- Live 12 has its own tuning-system support and its own scale-file handling, including a native
  format. Confirm which file types this version accepts, and where it places the reference pitch,
  before relying on it: `shared/TUNING_AND_MPE.md`, section 3.
