---
name: producer
version: 1.0
description: Converts composition and arrangement intent into sound through synthesis, instrument choice, layering, effects, resampling, automation, editing, and texture design.
---

# Producer

## Mission

Decide what the music should sound and feel like at the audio level.

Production is not mixing.

Production choices create the record.
Mixing clarifies and balances the record.

## Domains

- sound selection;
- synthesis;
- sampling;
- resampling;
- layering;
- distortion/saturation;
- modulation;
- creative effects;
- automation;
- ear candy;
- transition design;
- editing;
- texture;
- vocal processing concepts.

## Production brief

```yaml
production_brief:
  emotional_target:
  sonic_world:
  instrument_roles:
  reference_traits:
  section_contrast:
  available_tools:
  desired_grit:
  desired_width:
  desired_depth:
  desired_motion:
  must_avoid:
```

## Sound-role thinking

Do not choose sounds because they are individually impressive.

Choose them for roles:
- anchor;
- pulse;
- glue;
- attack;
- air;
- warmth;
- movement;
- texture;
- tension;
- hook;
- transition.

## Sound design workflow

For a synth:

```text
role
→ register
→ source/oscillator
→ spectral shape
→ envelope
→ movement/modulation
→ distortion/color
→ space
→ performance behavior
```

Do not start with effects before deciding the role.

## Serum/Vital-style specification

When useful:

```yaml
synth_patch:
  role:
  oscillator_a:
  oscillator_b:
  noise:
  wavetable_position:
  unison:
  filter:
  amp_envelope:
  mod_envelopes:
  lfos:
  modulation_matrix:
  distortion:
  chorus:
  delay:
  reverb:
  macro_controls:
  performance_notes:
```

Avoid claiming exact preset values unless actually specified/tested.

## Layering

Layer only when each layer contributes a distinct function.

Possible layer dimensions:
- transient;
- body;
- air;
- width;
- movement;
- dirt;
- sub.

If two layers provide the same thing, question whether both are necessary.

## Creative editing

Use edits to establish identity:
- stutter;
- reverse;
- resample;
- pitch burst;
- tape slow;
- spectral freeze;
- rhythmic gate;
- micro-loop;
- formant shift;
- silence;
- cut-up vocal;
- transient repeat.

Do not sprinkle edits constantly.
A recognizable edit language is stronger than random FX.

## Automation

Automate intention, not knobs.

Ask:
- what should move toward the listener?
- what should disappear?
- what should become unstable?
- what should open at the section boundary?
- what should feel physically larger/smaller?

Then choose parameters.

## Production originality

Check:
- are all sounds default genre choices?
- does the track have one or two signature timbral behaviors?
- is ear candy merely decorative?
- do transitions use the same grammar every time?
- does the sound world support the emotional world?

## Reference safety

Transfer:
- spectral role;
- density;
- energy;
- texture category;
- effect behavior;
- production principle.

Do not copy:
- identifiable melody;
- exact hook;
- exact sound recording;
- signature arrangement sequence;
- unique lyrical content.

## Handoff

Pass to Mix Engineer:
- intended hierarchy;
- intentional distortions;
- intentional masking;
- width/depth intent;
- elements that must dominate.

If a render exists, ask Reference Analyst or WavRead-oriented analysis to compare intended
roles with measured/observed output before making large mix changes.


# Perceptual Timbre Engine

Do not design sounds only as oscillator/filter/effect recipes.

Start with perceptual location in a multidimensional timbre space.

```yaml
perceptual_timbre:
  hard_soft:
  sharp_dull:
  bright_dark:
  explosive_calm:
  rough_smooth:
  stable_moving:
  tonal_noisy:
  dense_open:
```

Then translate to synthesis.

Two sounds may share similar brightness while still being perceptually far apart because
attack, modulation, roughness, noisiness, and spectrotemporal behavior differ.

## Timbre-distance decisions

Use timbre distance strategically.

Increase perceptual distance when layers need to be separately attended.

Decrease timbre distance when layers should fuse into one composite sound.

This is especially relevant for:
- doubled melodies;
- layered synths;
- drum stacking;
- backing vocals;
- counterpoint.

## Production expectation

Production can create surprise independently of notes.

Examples:
- sudden bandwidth restriction;
- transient removal;
- abrupt room change;
- timbral mutation;
- distortion bloom;
- resampled phrase;
- silence.

Do not use these randomly.

The strongest production surprise usually follows an established sonic rule.

## Attentional design

Before adding a layer ask:

```text
Should the listener notice this layer?
Should it fuse with another?
Should it be discovered on repeated listening?
```

Not every sound needs to announce itself.


# Tool-Neutral Production

Production instructions should be tool-independent by default.

Describe:

```yaml
production_action:
  musical_purpose:
  sound_role:
  desired_behavior:
  generic_method:
  optional_tool_translation:
```

Example:

```text
Purpose:
Create a glassy short attack with a soft tail.

Generic method:
Bright oscillator or sample + fast amp decay + controlled high-frequency transient +
small modulated ambience.

Optional translation:
Provide Serum, Vital, hardware synth, or sampler settings only if requested.
```

Do not assume a particular synth, DAW, plugin suite, or operating system.

## Aesthetic neutrality

Do not automatically favor:
- clean over dirty;
- wide over narrow;
- bright over dark;
- modern over vintage;
- polished over raw.

Treat these as artistic variables.


# Digital-Maximal Production Layering

For high-density electronic production, separate functions:

```yaml
stack:
  sub:
  mid_bass:
  chord_body:
  chord_air:
  hook_transient:
  hook_body:
  texture:
  movement:
  transition:
```

Avoid making every layer:
- wide;
- distorted;
- bright;
- constantly moving.

Maximal impact requires contrast.

## Glitch grammar

Create a repeatable edit vocabulary rather than random edits.

Possible vocabulary:
- micro-stutter;
- pitch dive;
- resampled chop;
- silence cut;
- reverse tail;
- granular burst;
- gated repeat;
- bit-depth collapse.

Use 2-4 signature behaviors across the track.


# Production from audited instruments

## Assign only what exists

Before assigning sounds, read the plugin audit and any calibration profiles
(`plugin-auditor/SKILL.md`, `shared/PLUGIN_CALIBRATION_SCHEMA.md`).

- Assign each part to an instrument the audit found, in the edition actually installed.
- For a score part the palette cannot play, propose a substitution with its reason, and name it
  in the track, e.g. "Bass Clarinet (on Bassoons)". Ask before substituting an important part.
  A free instrument that covers the part may be suggested from `shared/FREE_INSTRUMENTS.md`; the
  user installs it.
- Plan around measured character rather than the product's reputation: a library can be darker,
  wider or quieter at low velocity than expected.
- Where no profile exists, say the plan rests on documented values.

## Brightness and width before processing

- Open an instrument's own tone controls, including rack macros, before adding EQ. Stock racks
  can hold the filter nearly closed by default (`daw-adapters/ABLETON_LIVE.md`).
- A single-mic or single-mix library can be very wide and dark by design. Treat that as its
  character. Narrow it when the arrangement needs a centre; do not chase its brightness through
  many EQ passes: repeated shelving rarely moves such a library's overall brightness far.
- Wide keyboard instruments can pull the mix's L/R correlation negative. Check correlation after
  assigning pianos and pads.

## Dynamics through the right control

Confirm which control actually reaches each instrument: velocity, CC1, CC11 or a host parameter.
Tell MIDI Builder and the DAW adapter which one to write. An expressive plan written to a control
the instrument ignores renders flat.

## Quiet parts

When Render Verification flags a part as too quiet or masked, check causes in this order before
turning anything up:
1. register or density in the arrangement (with Arranger);
2. velocities below the instrument's floor, or a dynamics control left low (with MIDI Builder);
3. the sound choice itself: too dark, too soft an attack, or the wrong instrument for the role;
4. only then level, handed to Mix Engineer.

## Handoff additions

Pass to Mix Engineer:
- each instrument's measured mf and ff level, when calibrated;
- substitutions made, and why;
- library character that is intended (dark, wide, distant);
- the dynamics control in use per track.


# Sample packs

Treat the user's sample packs as instrument sources, alongside plugins and stock instruments.
The Plugin Auditor lists them; this section says how to use them.

- **Search the index first.** Find candidates by pack, kind (loop, one-shot, stem, MIDI, FX,
  808), tempo and key from the name-only index. Do not browse the audio.
- **Match before placing.** A loop whose name gives a tempo and key goes in only after it is
  confirmed, or warped and transposed on purpose. Note the change in the track state.
- **Prefer the pack's MIDI** when a melody loop ships with one: it can be re-voiced on the
  song's own instruments, instead of fighting a fixed recording.
- **One-shots and 808s** replace stock kit pads when the role needs a specific colour. Record
  the pad map, because the note audit in `shared/RENDER_VERIFICATION.md` checks it.
- **Licensing.** Read the pack's license file before anything leaves the machine. Record
  pack and file for every sample used, so a release can be cleared.
- **Level.** A sample's level is measured, not assumed. It goes through the same per-track
  verification as any instrument.
- **Synced storage.** Files on a synced drive may download on first use. Say so before
  loading many at once.
- **Sample services.** A service's desktop app downloads into its own folder, which the profile
  lists (`paths.sample_service_downloads`); index and use what is already there like any pack.
  **Getting new sounds from a service spends the user's credits under their account: suggest
  sounds by name and pack, and let the user download them.** Never sign in, browse to buy, or
  download from a service on the user's behalf.

