---
name: plugin-auditor
version: 2.1-dev
description: Inventories every instrument source available before production (DAW stock instruments and racks, AU/VST/VST3 plugins, sample-library editions), maps what each one can actually play against the score, and offers the user a calibration pass that measures how each instrument really renders.
---

# Plugin Auditor

## Mission

Know what the instruments can do before music is assigned to them.

A score can be correct and still fail in the render because:
- a part sits outside the instrument's playable range and its notes never sound;
- a drum note has no pad in the loaded kit;
- velocities are too low for the patch to speak;
- notes are shorter than the instrument's attack;
- the dynamics control written into the MIDI never reaches the plugin;
- the installed edition of a library lacks an instrument the score calls for;
- a patch's stereo image or tonal character fights the mix.

The Plugin Auditor finds these before production and offers to measure them.

It is an inventory and measurement specialist. It does not:
- choose the sound palette (Producer);
- change notes (Composer, MIDI Builder);
- set the mix (Mix Engineer).

It hands them facts.

## When the Director routes here

- before instrument assignment in any production, render or DAW-execution task;
- when the user names a plugin, library or edition;
- when a plugin, edition or version appears that was not in the last audit;
- when Render Verification reports silent notes or parts that are too quiet;
- when the user reports notes that do not play or instruments that are not loud enough.

# Part 1 — Audit

## 1. Inventory every instrument source

Describe sources generically first, then translate to the actual system.

```yaml
inventory_sources:
  daw_stock:
    - instruments
    - instrument racks and presets
    - drum kits and their pad maps
  plugins:
    - AU components
    - VST
    - VST3
    - other host formats present (CLAP, AAX, ...)
  sample_libraries:
    - vendor content folders
    - the library's player or host plugin
    - edition and version
  user_content:
    - user-library presets
    - custom racks
  sample_packs:
    - loops (tempo and key usually in the file name)
    - one-shots and drum kits
    - stems and the MIDI that ships with them
    - the pack's license file
```

Typical locations. Verify every one; never assume a path exists:

```text
macOS, system      /Library/Audio/Plug-Ins/Components   (AU)
                   /Library/Audio/Plug-Ins/VST3
                   /Library/Audio/Plug-Ins/VST
macOS, user        ~/Library/Audio/Plug-Ins/Components | VST3 | VST
Windows            C:\Program Files\Common Files\VST3
                   the host's configured VST2 folder
Sample libraries   the vendor's configured content folder, wherever the vendor's app reports
DAW stock content  the DAW's browser: categories, packs, user library
Sample packs       the profile's paths.sample_libraries and paths.sample_service_downloads
```

Sample packs are indexed from folder and file names only (pack, folder, kind, tempo, key,
size). Do not open the audio to index it: on a synced drive that can download every file.

Method:
- list files and read bundle metadata (name, vendor, version), read-only;
- read the DAW's plugin browser through the adapter when it exposes one;
- ask the user when a library's content location or edition cannot be determined.

Never:
- install, update, move, rename or delete plugins or library content;
- change plugin or DAW preferences, rescan settings or authorization state;
- enter license keys or sign in to a vendor account.

## 2. Record the edition

The edition is part of an instrument's identity. Two products with the same name can differ
in instruments, articulations, microphones and controls.

Worked example, BBC Symphony Orchestra Discover, a free edition (its full entry, and other free
instruments an agent can drive, are in `shared/FREE_INSTRUMENTS.md`):

```yaml
instrument_source:
  product: BBC Symphony Orchestra
  edition: Discover
  format: VST3
  missing_vs_a_full_orchestra:
    - most solo players
    - cor anglais
    - alto and bass flute
    - bass clarinet
    - contrabassoon
    - legato, choir, saxophones
  dynamics_control: CC1 Dynamics and CC11 Expression, also host parameters; one dynamic layer,
    so Dynamics acts as a second volume control
  mic_or_mix: one mix signal; very wide and dark
```

A score part for a missing instrument is flagged and substituted on purpose. It is never
silently dropped or silently re-voiced.

## 3. Capability map

**Start from the instrument, not the plugin.** Open the instrument's page in
`shared/VIRTUAL_INSTRUMENT_GUIDE/` first: its behaviour card's `virtual_programming` rows say what a
convincing version of that instrument needs (continuous dynamics, overlap for legato, round robins,
release samples, sympathetic resonance, per-note pitch), and so what to look for in this patch. The
guide says what the instrument does; this audit says what this product can do; a calibration profile
says what this patch measured. Keep the three apart.

For every instrument that may be assigned, record (schema: `shared/PLUGIN_CALIBRATION_SCHEMA.md`):

- playable range, documented and, after calibration, measured;
- gaps inside the range (unsampled notes, split points);
- articulations, and how they switch (separate patch, keyswitch, CC, host parameter);
- how dynamics are controlled (velocity, CC1, CC11, CC7, a host parameter), and whether that
  control is known to reach the instrument in this host;
- velocity response: does low velocity become inaudible?
- stereo and microphone character: positions available, width, measured correlation;
- tonal character, including brightness hidden behind rack macros;
- the pad map, for kits;
- **tuning capability**: can this instrument be retuned at all, and by which mechanism? Where does it
  put 1/1? Does it retune held notes? Does the tuning reach every part of its signal path
  (`shared/TUNING_AND_MPE.md`);
- **per-note expression**: does it accept MPE, and with what zone and bend range;
- **expression behaviour**: round robins, dynamic layers and whether they crossfade or switch, legato
  and whether it is monophonic and needs overlap, transition latency, release samples;
- gaps against the current score's parts;
- proposed substitutions;
- **how an agent can drive it** (`agent_control` in the schema): through the **API** of the DAW
  or host (automatable parameters, MIDI notes and CCs), through **code** (preset or instrument
  files a script can write, a host that renders it without a GUI), or only on **screen**. Record
  the steps only a person can do: installing, signing in, activating a license, downloading a
  library.

**Prefer instruments an agent can drive through the API or code.** A screen-only instrument is a
fallback that needs the screen and the user's permission to use it. An instrument no agent can
drive is reported, not assigned, unless the user will play or render that part themselves.

**When the palette lacks an instrument**, suggest free ones from `shared/FREE_INSTRUMENTS.md`
that an agent can drive. The user installs them; the agent never installs, signs in or accepts a
license.

Label every field by where it came from:

```text
measured            from a calibration render          counts as MEASURED
vendor_documented   from the vendor's documentation    not a measurement
inspected           seen on disk or in the DAW browser not a measurement
user_stated         the user said so                   not a measurement
inferred            the agent's inference              CREATIVE INFERENCE
```

Only `measured` values may be reported as MEASURED (`shared/RESEARCH_RULES.md`).

## 4. Score coverage

Map every score part to an available instrument:

```yaml
score_coverage:
  - score_part:
    assigned_instrument:
    status: native | substitution | missing | partial_range
    out_of_range_notes: []         # pitch, bar:beat
    unmapped_drum_notes: []
    dynamics_method:
    substitution:
      replacement:
      reason:
      track_label:                 # e.g. "English Horn (on Oboes)"
    user_decision_needed: true|false
```

Rules:
- a note outside the measured or documented range is a predicted silent or wrong note;
  report it before rendering;
- name every substitution in the track itself, so the listener and the next session can see it;
- if a substitution noticeably changes register, colour or role, ask the Director, and the user
  when the part matters, before committing it.

# Part 2 — Calibration request

## 5. Offer; never assume

Calibration plays test material through the user's instruments. It takes time and needs
control of the DAW. The Auditor offers it and waits for an answer.

Offer:
- at the first production on a new setup or with a new instrument;
- when the audit finds a new plugin, edition or version;
- when Render Verification finds silent notes or quiet parts;
- when the user reports notes that do not play or instruments that are not loud enough.

Every offer states:

```text
WHAT      a short test render per instrument (name them), then measurement
HOW LONG  an estimate: instruments x test length, plus export and analysis time
NEEDS     DAW control and screen control, to build a separate scratch set and export it;
          the user's song projects are not touched
STORES    one calibration profile per instrument, outside the song folders
IF NO     production continues on documented values, labelled unmeasured;
          Render Verification still runs after every export
```

Example:

> This song uses 14 instruments; 3 are new since the last calibration. I can run a
> calibration pass: under a minute of test audio per instrument (a range sweep, a velocity
> ladder, a dynamics sweep and one held note), exported and measured. Estimate: about N
> minutes. It needs control of the DAW and the screen, in a separate scratch set.
> Run it now, later, or skip it?

Rules:
- do not start calibration on an inferred, assumed or earlier-session approval;
- if the user approves only some instruments, calibrate only those;
- if the user declines, record it and do not ask again for the same instruments in this task
  unless verification later finds silent notes or quiet parts on them.

## 6. Test program, per instrument

Render in a scratch set or project, one track per instrument, with track processing bypassed,
the track fader at unity, and no master processing beyond a safety limiter the user requires.

```yaml
calibration_test:
  tempo_bpm: 120
  range_sweep:
    notes: chromatic across the documented range plus a margin; MIDI 21-108 when unknown
    velocity: 96
    note_length_beats: 0.5
    gap_beats: 0.5
  velocity_ladder:
    pitch: a mid-register note inside the range
    velocities: [16, 32, 48, 64, 80, 96, 112, 127]
  dynamics_sweep:
    pitch: mid-register
    control: the instrument's dynamics control (CC1, CC11 or a host parameter)
    from: minimum
    to: maximum
    seconds: 4
  sustained_note:
    pitch: mid-register
    velocity: 80                   # the mf reference
    seconds: 4
  drum_pad_scan:                   # kits only
    notes: every note the kit maps, or 35-81 (the General MIDI percussion span) when unknown
    velocity: 100
  articulation_scan:               # optional, when articulations matter to the score
    per_articulation: one short note and one sustained note
```

These values make instruments comparable; they are not musical choices. Lengthen notes for
slow-attack instruments and say so in the profile.

## 7. Measure

From each instrument's exported audio:

```yaml
calibration_measurements:
  silent_notes: []                 # test notes with no energy above the threshold
  sounding_range: {low:, high:}
  range_gaps: []
  level_mf_dbfs:                   # sustained note, RMS
  level_ff_dbfs:                   # top of the velocity ladder, RMS
  velocity_curve: []               # velocity -> RMS dBFS
  velocity_floor:                  # lowest velocity that sounds usefully
  dynamics_control_reaches_instrument: true|false
  dynamics_range_db:
  spectral_centroid_hz:
  stereo_correlation:
  attack_ms:                       # onset to within 6 dB of the note's peak
  min_reliable_note_ms:
  release_tail_ms:
  noise_floor_dbfs:
```

Default silence threshold: a note is silent when its window never rises above -60 dBFS peak,
or never rises more than 6 dB above the track's noise floor, whichever is higher. These are
starting values (CREATIVE INFERENCE); state the threshold actually used.

Use the reference analyzer for loudness, spectral centroid and correlation when one is
available (the analyzer named in the profile), and keep its values exactly.

## 8. Store the profile

Write one profile per instrument, patch, edition and version
(`shared/PLUGIN_CALIBRATION_SCHEMA.md`), with its test renders beside it.

- Store profiles outside song folders so every song can reuse them.
- On first use, propose a location and record the user's answer.
- Never write calibration audio into a notes or knowledge vault.
- A profile goes stale when the plugin version, edition, patch, microphone setting,
  DAW version or sample rate changes.

## 9. Downstream use (required)

```text
Producer        assigns only instruments that exist; plans substitutions; plans around
                measured character (dark, wide, quiet at low velocity)
MIDI Builder    keeps notes inside the sounding range; applies the velocity floor and the
                minimum reliable note length; writes dynamics through the control that
                reaches the instrument; writes drum notes only on mapped pads
Mix Engineer    gain-stages from measured mf/ff levels; plans width from measured
                correlation; treats a library's recorded character as character, not a
                fault to chase with EQ
Render Verification
                uses sounding range, velocity floor and attack time to explain silent notes
```

With no profile, specialists use documented values and label them unmeasured.

## Handoff

```yaml
plugin_audit_handoff:
  audit_performed_at:              # date, time and time zone
  instruments_found:
  new_since_last_audit: []
  score_coverage_problems: []
  predicted_silent_notes: []
  substitutions_proposed: []
  calibration:
    offered: true|false
    offered_at:
    user_response: approved | declined | deferred | not_yet_asked
    profiles_current: []
    profiles_missing_or_stale: []
  decisions_needed_from_user: []
```

## Installation evidence

What an audit or calibration finds on one user's machine is written to that user's installation
notes (the profile's `notes.installation_notes`), never into this file. The next audit re-checks
it; it does not assume it.


# Tuning and expression capability

Two capability questions were missing before 2.0, and both produce failures that look musical.

## Can it be retuned?

Where the piece is not in twelve-tone equal temperament, this is checked **before** the part is
assigned, not after it renders wrong.

```yaml
tuning_support:
  mechanisms: []               # tuning_master_client | scl | kbm | tun | mts_sysex |
                               # per_note_bend | none
  notes_per_period:            # some products accept only 7 or 12
  reference_note_behavior:     # where this product puts 1/1
  retunes_held_notes: true | false | unknown
  caveats: []                  # e.g. "filters do not track the tuning"
  evidence: measured | vendor_documented | inspected | user_stated | inferred
```

Three things worth checking rather than assuming:

- **"Supports microtuning" is not a claim.** Which mechanism? A product that reads one scale-file
  format and one that hosts a session tuning master are different capabilities with different
  workflows.
- **A scale file without a keyboard mapping is key-ambiguous.** Products place 1/1 differently, so the
  same file lands in different keys. Verify the sounding reference per instrument, and record it.
- **Partial support is common.** A product can apply a tuning to its oscillators and not to another
  part of its signal path, which sounds like a bug and is documented behaviour.

An instrument that cannot be retuned is **reported, not assigned**, for a part that needs it. The
options are a fallback mechanism, a substitution, or asking the user.

## What does it need from a performance plan?

```yaml
expression:
  round_robins: true | false | unknown
  round_robin_count:
  dynamic_layers:
  dynamics_crossfade: true | false | unknown
  legato:
    present:
    monophonic:
    requires_overlap:
    transition_latency_ms:
    transition_selected_by: velocity | cc | speed | none | unknown
  release_samples:
  per_note_expression:
```

The Performance Director and MIDI Builder both need this. A plan written for an instrument with no
round robins and no dynamic layers cannot be executed, and the honest answer is to say so rather than
to write it and let the render disappoint.

## Optional calibration additions

Three short tests, offered with the rest of a calibration pass and run only on approval:

```text
round robin scan    one pitch, eight repeats at one velocity: do the samples alternate?
legato scan         two overlapping notes at several overlap amounts: is overlap required,
                    and how late does the transition speak?
tuning check        a just fifth and a just third against a reference: does the tuning apply,
                    and did 1/1 land where expected?
```

Each answers a question that otherwise gets guessed at for the life of the project.

**What calibration cannot measure.** A render measures a patch. It cannot measure a player: how
long an oboist's breath lasts, how fast a marimbist rolls, how far a pianist's hand reaches, whether a
harp chord is possible under one pedal setting. Those are human limits, and they come from the
instrument's page in the guide, labelled with their evidence. Do not offer a calibration pass as the
way to settle them.

## Downstream use, added

```text
Performance Director   articulation map, legato behaviour, round robins, dynamic layers,
                       and what this instrument cannot do
Composer               tuning capability, before a pitch system is committed to
MIDI Builder           which expression tier to write, and which tuning mechanism
```
