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

- **Mixer volume, pan and sends are read-only over this connection.** If the user's profile names
  a sidecar Remote Script for mixer work (next section), use it. Without one, set level with EQ
  Eight's output gain (up to +12 dB), and placement and width with Utility, on each track. Return
  tracks can exist in the set and still be unusable from AbletonMCP alone.
- **Loading an instrument while an audio track is selected does not fail.** Live makes a new MIDI
  track holding the instrument. Select a MIDI track before loading any instrument, and count the
  tracks before and after.
- **The loader finds browser items only under Live's own browser categories and the User
  Library, not in the Current Project folder.** To load a generated clip or preset, place it in
  the User Library for the load, remove it afterwards, and keep a copy with the project.
- **Export without the screen: use the bridge's `export_audio` where it's installed** (measured 2026-11-12, Live
  12.4.16). It drives File > Export Audio/Video through macOS Accessibility in the background and renders offline:
  8 bars at 140 BPM in about 9 s. Give it start and length as bar.beat.sixteenth and a new file path. Without it,
  the Export and Save dialogs are not reachable through the connection: drive them on screen, with the user's
  permission. The Rendered Track menu is a pop-up, which background control cannot open, so export renders the
  Main only. Positions depend on the display layout: take a screenshot before every click.

## Mixer, returns, sends, routing and racks: a sidecar Remote Script

> Measured on Live 12.4.16 with a second, loopback-only Remote Script beside AbletonMCP (built for
> this pack's user; where it lives and how to reach it is in the user's profile, `daw.control`).
> Every number below was measured audibly in a scratch set, before and after a save and reopen.

**Why a sidecar.** It adds what AbletonMCP lacks without changing a byte of the working script:
another script, another port, another control-surface slot. Rolling back means clearing the slot.

**Setting one up (the user's step, or with their permission):**
- Copy the script folder into `~/Music/Ableton/User Library/Remote Scripts/`.
- **Live scans Remote Scripts only at startup.** A newly copied or updated script shows up only
  after Live restarts, and re-picking it in a slot does not reload its code.
- Pick it in an empty slot under Settings > Tempo & MIDI > Control Surface, with Input and Output
  set to None. The slot's list is a pop-up menu: background screen control can't open it, so it
  needs full-screen control or the user's click. Live keeps the choice for later starts.

**What it covers** (the profile's tool reference has the exact commands):
- return tracks: create, rename, load native devices (`Track.insert_device`, Live 12.3+) or plugins
  (browser load with the return selected), set their parameters in display units;
- sends in dB, faders in dB, pan, mute, solo;
- routing: read and set input, output and monitoring; audio submix buses (Input "No Input",
  Monitor "In", Output "Main"); a routing-graph check for loops, double routing and silent buses;
- device chains: insert at a position, move, bypass, snapshot and restore, parameters inside
  nested racks by a chain path;
- meters for audible proof.

It can't create a native Group Track (the 12.4 LOM has no call for it), and the LOM can't save:
save through the File menu.

### Three scales for one send

| Live shows | LOM `send.value` (knob position) | `.als` `TrackSendHolder/Send/Manual` |
|---|---|---|
| 0 dB (the maximum) | 1.0 | 1.0 |
| -6 dB | 0.85 | 0.501 |
| -12 dB | 0.70 | 0.251 |
| -20 dB | 0.50 | 0.100 |
| off | 0.0 | 0.000316 (-70 dB, Live's floor) |

- The LOM knob follows `dB = 40·v − 40` from 0.4 to 1.0 and bends below 0.4. Never compute it:
  write `display_value` in dB and read back `str_for_value`.
- The saved set's `Manual` is linear amplitude, `10^(dB/20)`. A saved-set editor that writes
  linear gain is right; a reading of 0.70 through the LOM is the same -12 dB.
- Track and return faders: LOM 0.85 is 0 dB (the fader goes to +6 dB).

### Meters, mute and solo: what Live actually does

- Output meters: `dBFS = 76 × output_meter_level − 70`. The slope is confirmed: a -12 dB fader and
  sends of -12 and -20 dB measured within 0.01 dB. The absolute offset isn't checked against an
  external meter. Meters hold peaks about 1 s, so wait 2 s after a change.
- **A track's own meter reads before its mute and solo.** A muted return or bus still meters
  its input. Judge a mute by the Main or the bus it feeds, never by the muted track's meter.
- **Solo overrides mute:** a soloed, muted track still plays.
- Sends are post-fader by default: a source at -70 dB sends nothing.
- Muting a return or a bus drops the Main exactly as much as pulling its fader to -inf.
- Soloing a track that feeds a bus keeps the bus audible, carrying that track only.
- Live leaves feedback targets out of a bus's output choices, so a loop can't be routed.
- Routing lists fill on the next tick after a track is created: retry for a moment.

**The audible send check** proves a send's dB: bypass the return's effect, play one source at a
time, and the return's peak minus the source's peak equals the send in dB (±0.5).

### Parameters, racks and plugins

- `DeviceParameter.display_value` is writable on 12.4 and takes dB, Hz, ms and %. Read
  `str_for_value` back. Fall back to bisection where a device's display isn't linear.
- **Tempo-synced note values don't parse in display units.** A synced time parameter that shows "1/8" or
  "1/4" takes "1/8" as the number 1. Write it raw and read `str_for_value` back. Measured on Live 12.4.16:
  Echo's "L/R Synced" raw -3 = 1/8 and -2 = 1/4.
- **Inside racks**, address a device by a path: the chain index, then the device index in that
  chain, then the next chain, and so on. A stock Instrument Rack preset can nest a Sampler two
  racks deep (rack, chain 0, device 1 is a rack, its chain 0, device 0). Read the chain tree first
  and never guess a path. Sampler's LFO amounts appear as `Filt < LFO`, `Pan < LFO`,
  `Pitch < LFO` and `Vol < LFO`.
- **Sampler's aux LFO routes in the modulation matrix are not parameters at all.** Only LFO 1's
  fixed amounts above are exposed. The aux LFOs' routes (`AuxLfos` > `ModConnections` > `Amount` in
  the saved set) can't be read or written through the LOM at any rack depth. Change them in the
  closed `.als`, then reopen and confirm by ear or render.
- **Some plugins expose only Device On to Live.** They load, but nothing can set their
  controls until their parameters are added with the device's Configure button and the set is
  saved. Check the parameter count after loading before promising any plugin automation or
  setting. The user's plugin facts list which plugins do this.
- A plugin's authorization can't be read through the LOM: a demo loads like a licensed copy.
- In a browser walk, Live's category roots (`browser.plugins` and the like) report `is_folder`
  False although they have children: always recurse into children.

### Automation, sidechain, racks and recording (measured on Live 12.4.16)

The user's profile names the tool reference and its capability matrix. These facts hold for any bridge:

- **Session clip automation is fully scriptable:**
  - `clip.create_automation_envelope(param)`;
  - ramps with `envelope.create_event(EnvelopeEvent(beat, value))` (two events at one time make a jump);
  - steps with `insert_step`;
  - read back with `value_at_time(beat + 1e-4)` (exactly on a border it returns the value before it).

  Time is clip-local beats. Values are the parameter's raw range: convert dB, Hz or % through `str_for_value`.
  Curve tension (`control_coefficients`) does nothing, so shape with dense points.
- **Arrangement automation can't be drawn through the API. Record it.**
  - Turn Automation Arm on, then Arrangement Record.
  - Write the parameter every tick inside `begin_gesture` / `end_gesture`.
  - Three traps, each measured:
    - a gesture begun in the tick recording starts is dropped: wait half a beat;
    - **an armed or controller-armed MIDI track records silence over its clips:** select a non-MIDI track and
      refuse while anything is armed;
    - stopping Session clips leaves tracks detached from the Arrangement: press Back to Arrangement before playing
      it back.
- **Copying a Session clip to the Arrangement on an instrument track drops its envelopes.**
- **Prove automation by sampling inside Live.** A script on Live's own tick (`schedule_message`), reading
  `output_meter_level` and the parameter about 10 times a second against `current_song_time`, follows the curve
  bar by bar. External polling manages about one reading a second.
- **Large plugins hide their parameters** until they're in the device's Configure list. The list lives in the saved
  set as placeholder `PluginFloatParameter` slots (ParameterId -1). A configured parameter is the same slot with the
  plugin's parameter ID and name: for an AU, `auval -v` lists them. Editing a closed copy of the set this way is
  reliable.
  - **Live pushes each slot's stored value into an AU plugin when the set opens:** write the intended starting
    value, or set it right after. A VST3 restores its own state over those values, so set them through the API
    after opening. For a plugin built on the same framework, the AU's parameter IDs worked unchanged for its VST3.
  - A VST3 usually shows real units in Live ("69.6 semitones", "FILTER 1"); an AU may show only 0..1 numbers.
- **After a plugin update, check two things before re-rendering old songs:** the browser address any script
  loads it by, and whether the new version reads the old saved patch state. Then compare one preset by render
  against a stem from the old version.
  - Re-render from a copy of the set, never the original.
  - Compare loudness, peak and band balance.
  - **Null the new version against itself before reading anything into a failed null:** a patch with per-note
    randomness (random oscillator phase, unison) doesn't cancel even against a second render of itself.
- **Parallel "corruption" around a clean lead:** distort first, then high-pass the distorted copy above the lead's
  notes. Measured: this left the lead's band unchanged (0.0 dB) and added texture above the cutoff. High-passing
  before the distortion leaves nothing to corrupt on a pure tone. High-passing below the lead's notes lets the
  copy overlap the lead and partly cancel it (centre correlation 0.72, 1.2 dB lost). Check the lead's own band
  before and after.
- **Device facts that change chain designs** (Live 12 manual and makers' manuals, checked 2026-11-10):
  - MeldaProduction's MCompressor has no external key input: use Live's Compressor for sidechains.
  - Echo switches itself off about 8 s after its input stops, unless its Noise and Gate are both on.
  - Utility's Mid/Side width can't create sides from a mono source: decorrelate first (chorus, Mid/Side delay,
    jitter).
  - Saturator's Bass Shaper curve is the manual's suggestion for 808s.
  - Auto Pan-Tremolo with a ramp shape and Invert gives a kick-free pump.
- **Arrangement clip editing:** the API has no move or resize, but these work:
  - `Track.duplicate_clip_to_arrangement` (returns the new clip, pastes over whatever is there),
    `Track.delete_clip` and `Track.create_midi_clip(start, length)`.
  - **For an unlooped clip, its span is `loop_start` / `loop_end`.** Setting only the start/end markers didn't
    carry into a copy. Set both.
  - Move = a verified copy to a spot past the track's last clip, delete the original, copy to the destination,
    delete the temporary copy. A short shift copied straight to its destination pastes over its own source.
  - Split = trim the original's end, plus a head-trimmed copy moved into place.
  - Prove an edit by rendering deterministic audio before and after and nulling: split −215 dB, move −45 dB. A
    trimmed head nulls to about −39 dB because Live adds a short fade at a new clip edge.
  - Many soft synths free-run their oscillators, so they won't null against themselves: test edits on audio.
  - No clip fades in the API.
- **Export dialog:**
  - Its switches, formats and Export button are reachable with background control.
  - Render Start and Render Length are number fields that can't be set directly or clicked in the background, but
    they take the accessibility actions Increment and Decrement: step each part to its target and read it back.
    Focusing a field and typing the bar number also works. The dialog ignores the loop brace.
  - The save panel runs as a separate macOS service: background keystrokes (Cmd+Shift+G) don't reach it, and a path
    typed into the name becomes part of the name. Save under a unique name, read the folder from Live's
    `NSOSPLastRootDirectory` preference (a bookmark; changing it from outside Live doesn't move the panel), then move
    the file. Pressing Export reports an error because the save panel is modal: wait for the panel instead.
  - Exports of soft synths differ slightly run to run (free-running oscillators: two runs of one passage differed
    by an RMS of -39 dB). Length and loudness repeat exactly.
  - Check the file after every export.
- **Playback starts from the start marker (`Song.start_time`), not the playhead.** A render cued only by setting
  `current_song_time` while stopped starts at the marker (beat 0). Set both before launching a recording.
- **Check a plugin's architecture before blaming the plugin.** Native Apple Silicon Live doesn't list an Intel-only
  VST3. It runs the Intel AU through macOS's bridge (`lipo -archs` on the binary).
- **Sidechain:** Compressor exposes its sidechain source (`input_routing_type` from its own routing list, then
  "S/C On"). Prove it by ear-equivalent:
  - ducking with the trigger playing;
  - none with the trigger stopped;
  - none with S/C off.

  Heavy saturation after the compressor can hide the ducking (12 dB measured down to 1.75 dB).
- **Racks can be built** (`insert_device("Audio Effect Rack")`, `insert_chain()`, `chain.insert_device(name)`,
  chain mixer), but **mapping a macro to a parameter isn't in the API**. In the saved set, a mapping lives on the
  target parameter:
  - a `<KeyMidi>` block with `Channel` 16 and `NoteOrController` = the macro's 0-based index, placed after its
    `<LomId>`;
  - its `MidiControllerRange` Min/Max, which become the mapped range.

  The saved set's tags don't match API names (Saturator "Drive" is `<PreDrive>`), and values are stored in display
  units (dB) while the API's raw value is 0..1. So find the target by marking it: set a sentinel display value
  through the API, save, then edit a copy of the set where that value sits. Set the macro's own value to match the
  restored parameter, or the sound jumps on load. Tested: audible, and it survives Live's own save.
- **A/B a production choice without fooling yourself:**
  - Preserve every value the alternatives touch.
  - Render A and B identically (same start, same length, by resampling).
  - Restore, or keep the chosen version.
  - Compare at matched loudness (integrated LUFS).

  Report loudness, peak and true peak, crest, spectral balance by band, and L/R correlation as information. A
  louder or brighter version isn't better by itself: choose by listening to the matched files.
- **Recording a track or the Main into a clip:**
  - Set the input to the source track (or "Resampling" for the Main) with monitoring off.
  - Arm the track, then `clip_slot.fire(record_length=beats)`. It records the exact length.
  - Set the playhead while stopped, and don't press play afterwards: the launch starts the transport, and a play
    call restarts it and cuts the recording.
- **That is also a render with no dialogs.** Resample the Main, then measure the file offline. The file's peak
  matched Live's meter to 0.01 dB.
- **Live's engine runs at the audio device's rate, and a recording or resample takes that rate.** Check it
  matches the project's delivery rate before a render.
- No clip reverse, fades, consolidate or freeze in the API. Reverse a file offline and load it back as a clip.
- Live ignores start-marker writes on an unlooped clip: write markers while it loops, then switch looping off.

### Protecting the user's Sets (any bridge that can edit)

- **Live 12.4 exposes what's needed to tell Sets apart:**
  - `Song.file_path` and `Song.name`;
  - `Song.set_data` / `get_data`, which store a value inside the Set itself (a per-Set id that survives a reopen).
- **Live re-creates the control script on every Set load.** Anything held in memory, an edit permission included,
  ends with the Set. Measured: a new session key after opening another Set.
- **A safe design** classifies every command as read, write, meta or transport, treats unknown commands as writes,
  refuses writes to an unsaved (untitled) Set, and runs deletes only in a Set marked as disposable.
- Launching an empty clip slot on an armed track records, so treat that case as a write. Playing or continuing
  while record mode or Session record is on records too. Stopping never does, so always allow stop.
- **A control script's status-bar message (`show_message`) vanishes after a few seconds.** To keep something
  visible, show it again every second until it's no longer needed, then clear it.
- **Don't make users read approval codes.** A per-Set one-time code shown in Live's status bar was built, tested and
  removed (2026-11-10): users found it tiring, and an assistant with screen access could read it anyway. What
  protects a user instead: refuse unsaved Sets, keep deletes to disposable Sets, stay on loopback, and **ask the
  user before editing a song that matters, with a backup suggested.** The WavRead MCP Bridge works this way from
  0.5.0.
- Keep the bridge on loopback, and validate paths and parameter types.
- Before editing, tell the user which Set will change and suggest a backup.

### Safety rules that held up

- Test only in a disposable scratch set. Destructive commands should refuse unless the set
  carries a marker track.
- One agent drives Live at a time. Message any other session using Live before taking it, and again
  when Live is free.
- A set made from an older default template refuses a plain Save and asks for Save As. Save it
  under a new name inside its project folder.

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
