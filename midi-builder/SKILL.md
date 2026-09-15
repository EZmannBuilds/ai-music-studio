---
name: midi-builder
version: 2.1-dev
description: Converts composition, arrangement, and production plans into validated multi-track DAW-ready MIDI with track naming, markers, control data, and import notes.
---

# MIDI Builder

## Mission

Produce usable MIDI artifacts rather than textual pseudo-MIDI.

The MIDI Builder receives musical decisions from Composer, Arranger, and Producer and
encodes them for DAW continuation.

## Responsibilities

- exact tempo/meter;
- form markers;
- multiple named tracks;
- melody/harmony/bass/drum data;
- velocity design;
- MIDI CC where useful;
- pitch-bend gestures where useful;
- channel/port allocation;
- duration validation;
- track-count validation;
- DAW notes.

## Do not decide the artistic brief alone

The MIDI Builder is an execution specialist.

It should not silently replace:
- harmony;
- melody;
- song structure;
- orchestration;
- sound identity.

Return upstream if the musical plan is incomplete.

## Representing layers separately

Roles, not track counts. Three worked lists follow; the principle is the same in each, and a style not
listed here gets its own list built the same way.

### Pop and electronic

```text
lead guide
double/harmony guide
vocal chop guide
main hook
secondary hook
pads
saws
pluck
arp
counterline
sub
mid/distorted bass
guitar/piano
FX guide
kick
snare/clap
closed hats
open hats
percussion
glitch fills
cymbals
```

### Band

```text
lead vocal guide
backing vocals
lead guitar
rhythm guitar
bass
keys or organ
kick, snare, hats, toms, cymbals as the kit's parts
percussion
```

### Orchestral and acoustic ensemble

```text
melody line, by instrument
counter-line
inner harmony, by section
bass line
pedal or drone
percussion, by instrument
keyswitch tracks where a library needs them, marked non-sounding
```

Do not add tracks merely to satisfy a high count.
Every track should have a role.

## Hyper-detailed rhythmic MIDI

For electronic/pop genres the MIDI can encode:
- 16th hats;
- syncopated kick;
- alternate snare/clap;
- fills;
- ghost percussion;
- stutters;
- triplets;
- pitch-bend chop gestures.

Keep the musical grid readable.

## Automation

Use generic MIDI controls when useful:

```text
CC11 expression
CC74 brightness/filter intent
CC1 modulation
CC64 sustain
pitch bend
```

A DAW/plugin may interpret CC mappings differently.
Describe the artistic intent in the accompanying notes.

## Verification

Before delivery:

```text
verify file opens
verify duration
verify requested track count
verify every required track contains note/control events
verify no impossible MIDI note/channel values
verify conductor events
```

## Output pair

Prefer:

```text
<song>.mid
<song>_DAW_Notes.txt
```


# MIDI Instrument-Safety Validation

## General MIDI percussion rule

In General MIDI:

```text
channel 10
=
zero-based MIDI channel index 9
=
percussion
```

Never place a pitched/melodic instrument such as:
- sub bass;
- piano;
- synth;
- strings;
- guitar;
- vocal guide;

on channel 10 when using GM-compatible playback.

## Required validator

Before delivery, inspect every pitched track:

```text
if pitched_track.channel == GM_percussion_channel:
    FAIL
    reassign channel/port
```

Drum/percussion tracks may use channel 10.

## Program/channel validation

For every track verify:
- MIDI port;
- MIDI channel;
- program change;
- track role;
- note-event count.

When more than 15 pitched instruments are required, use additional MIDI ports rather than
placing pitched material onto the percussion channel.

## Rough-mix disclaimer

CC7/velocity values should provide a usable starting balance but must be labeled as a rough
MIDI mix.

Final mix decisions require the actual assigned sounds and preferably a rendered audio file.


# Lyric-aware MIDI

When Lyric Generator supplies an alignment:

## Standard MIDI lyric events
Where compatible, place Lyric Meta Events at syllable onsets.

For a melisma:
- write the lyric event on the first note;
- do not invent a new syllable for continuation notes;
- preserve exact continuation mapping in the sidecar JSON.

## Required sidecar
Prefer:

```text
<Song>.mid
<Song>_lyric_alignment.json
<Song>_DAW_Notes.txt
```

The sidecar should include:
- lyric line;
- syllable;
- lexical stress;
- MIDI note indices/pitches;
- onset;
- duration;
- phrase;
- melisma status;
- pronunciation confidence.

## Vocal MIDI verification

```text
verify lyric syllable count
verify mapped note indices exist
verify no syllable is accidentally orphaned
verify melisma continuation notes are documented
verify phrase boundaries agree with rests/markers
```

Do not silently change the melody to make lyrics fit unless Composer/Music Director authorizes it.


# Calibration-aware building and variety verification

## Build against the instruments that will play it

Before writing notes for a known instrument, read its entry in the plugin audit and its
calibration profile when one exists (`plugin-auditor/SKILL.md`,
`shared/PLUGIN_CALIBRATION_SCHEMA.md`). With no profile, use the documented values and label
them unmeasured in the DAW notes.

```text
range          keep every note inside the sounding range
velocity       lift velocities below the velocity floor, keeping the relative contour
note length    lengthen notes shorter than min_reliable_note_ms, or flag them
drums          write drum notes only on pads in the kit's map
dynamics       write dynamics through the control that reaches the instrument
keyswitches    list keyswitch notes as non-sounding, so the note audit excludes them
```

### Range

A note outside the range is a predicted silent or wrong note. Handle it in this order:
1. report it: track, pitch, bar:beat;
2. propose an octave shift that keeps the part's role, or a different instrument;
3. apply it only when the Composer or Director authorizes a change to the part; otherwise
   leave the note and mark it as a known risk for Render Verification.

Never drop or move notes silently.

### Velocity

Generated MIDI often arrives with part velocities averaging well under 50, which renders dull
and quiet on many instruments. Check it every time.

- compare each track's velocity range with the instrument's velocity floor;
- lift the whole contour, not single notes, so dynamics survive;
- record the lift in the DAW notes.

### Dynamics control

CC1 and CC11 are not universal. Some sampled instruments take dynamics only through their own
host parameters.

In some hosts a controller written as clip automation never reaches a plugin at all, and the plugin's
own host parameters have to be automated instead. This is a real and common failure, it is specific to
a host and a plugin, and it renders as a part with no dynamics rather than as an error. Confirm which
control reaches the instrument, from the audit or a calibration pass, before relying on it. Known
cases for a particular setup belong in that DAW's adapter and the user's installation notes, not
here.

When the verified control is a host parameter, a Standard MIDI File cannot carry it. Write the
dynamics intent into the DAW notes or a sidecar, as a curve per track, for the DAW adapter to
apply as automation:

```yaml
dynamics_automation_intent:
  track:
  target: host_parameter | cc1 | cc11 | cc7
  parameter_name:            # e.g. "Dynamics"
  points: [{bar_beat:, value:}]
  derived_from: velocity | score_dynamics | composer_curve
```

## Mark vocal lines by role

Name and tag every vocal-line and vocal-guide track so an instrumental export can find them:
lead guide, doubles, harmonies, rap guide, ad-libs, vocal chops, choir or vocal-pad guides.

```yaml
tracks:
  - name:
    role: vocal_line | vocal_guide | instrument | percussion | fx
```

Carry the role into the DAW notes and the track state. A track name alone is not enough.

## Melody-variety check on the artifact

Before delivery, run the Composer's `melody_variety_report` (`composer/SKILL.md`)
on every lead and vocal-guide track in the finished `.mid`, including the cross-song comparison.

MIDI Builder reports; it does not rewrite the melody. A flagged report goes back to the Composer
through the Director.

## Verification output

Report:

```yaml
midi_verification:
  file_opens:
  duration_verified:
  track_count_verified:
  every_required_track_has_events:
  gm_percussion_collisions:
  notes_outside_sounding_range: []
  notes_below_velocity_floor: []
  notes_shorter_than_attack: []
  unmapped_drum_notes: []
  dynamics_method_per_track: {}
  vocal_line_tracks: []
  lyric_mapping_complete:            # every syllable has a note, melisma or held note
  melody_variety_report: {}          # per lead / vocal-guide track
  calibration_profiles_used: []
  unmeasured_instruments: []
```

`exact_syllable_fit: true` alone is not a pass. Uniform syllable counts across every line are
themselves a flag.

## Hand the schedule to Render Verification

The delivered `.mid` and its tempo map are the note schedule for the note audit
(`shared/RENDER_VERIFICATION.md`). If notes are later edited in the DAW, say so, so verification
reads the schedule from the DAW instead.

When Render Verification reports silent notes, MIDI Builder answers for the causes it owns:
range, velocity, note length, drum pads, dynamics control, channel and port.


# Executing a performance plan

**MIDI Builder executes expression. It does not invent it.**

Where a `performance_state` exists (`shared/HUMAN_PERFORMANCE_SCHEMA.md`), the builder is implementing
someone else's decisions:

```text
articulation        write keyswitches, controller values or track splits as the plan's map says
dynamics            write to the control the plan names, which the audit confirmed reaches it
overlap             apply legato_overlap_ms, so a monophonic legato patch actually transitions
separation          apply the plan's separation for detached playing
timing              apply the plan's models, in the plan's magnitudes
accents             write the plan's accent map, not a generic one
keyswitches         list as non-sounding, so the note audit excludes them
```

Where the plan and a calibration profile conflict, for example a velocity the plan wants and a floor
the instrument imposes, **report the conflict rather than silently overriding either**. The plan's
author decides.

Where **no plan exists**, write plain quantised notes with a usable rough balance and label the
artifact:

```yaml
unperformed: true
```

in the DAW notes, the verification output and the track state. That is an honest deliverable. An
artifact full of invented expression that nobody planned is not, and it is what used to happen by
default.

# Writing a pitch system

Where the piece is not in twelve-tone equal temperament (`shared/TUNING_AND_MPE.md`):

1. read what the target instrument supports, from the audit;
2. pick the highest tier it supports: a session tuning master, a scale file, per-note bend, or one
   voice per channel;
3. write it, and **declare the bend range wherever bend data is written**;
4. ship the scale file beside the artifact where one exists, named per `shared/FILE_NAMING.md`;
5. record the mechanism and the honest failure sentence in the export.

```yaml
tuning_export:                 # the block defined in shared/TUNING_AND_MPE.md section 5
  tuning_tier: master | scale_file | mpe | per_channel_bend | none
  mechanism:
  scale_file_shipped:
  bend_range_declared_semitones:
  channels_used:
  what_happens_if_ignored:     # e.g. "a receiver ignoring the bends plays this in 12-TET"
  verified_on:                 # what it was checked against, or "not verified"
```

**Never silently quantise to twelve-tone equal temperament.** A microtonal piece rendered in equal
temperament with no comment is a wrong deliverable that looks like a right one.

Hand the tuning to Render Verification with the note schedule, or its pitch test will report every
correctly tuned note as out of tune.

# Adaptive exports

For interactive work, export per state rather than once
(`shared/ADAPTIVE_MUSIC.md`, section 6): per-state stems on a common grid and start, segment files with
their tails recorded, stingers, and a transition matrix an implementer can read without the project
file. Render Verification then applies per state: a layer silent in one state is a silent part.

# Verification output, added fields

```yaml
midi_verification:
  performance_plan_executed: true | false
  unperformed: true | false
  controls_written: {}               # track -> the control dynamics were written to
  overlaps_applied: {}
  plan_conflicts: []                 # where the plan and the calibration profile disagreed
  tuning_export: {}
  expression_tier: midi2_per_note | mpe | midi1_channel
  bend_range_declared: {}
  adaptive_states_exported: []
  track_dna_matches_artifact: true | false    # the ledger row against what was built
```

The last field is a cheap and useful check: a row claiming a 7/8 metre on an artifact in 4/4 means one
of them is wrong, and it is worth knowing which before delivery.


## Does not own

- **the music.** Harmony, melody, form and orchestration arrive decided. Where the plan is incomplete,
  return it upstream rather than filling the gap.
- **expression.** The Performance Director and the Vocal Director decide it; this skill executes it,
  and labels the artifact `unperformed` when there is nothing to execute.
- **instrument facts.** What a patch can play, what control reaches it and what it measured come from
  the plugin audit and calibration profiles.
- **the mix.** Controller and velocity values give a rough playback balance, and the notes say so.
- **the pitch system.** Composer chooses it; this skill writes it by the highest tier the target
  supports and states the failure mode.
