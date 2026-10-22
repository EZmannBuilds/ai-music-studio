# Optional Patch Automation and Delivery Plan

This guide describes how an agent could turn a patch brief into an editable preset plus a test report. AI Music Studio does not include a `.vital` generator or builder scripts. Treat this as an implementation plan and capability boundary, not as a working tool already shipped.

## Default path: learn and build in the instrument UI

Use the interactive course and the user's installed synthesizer. The user or DAW operator saves the preset, then the agent reviews screenshots, settings, or renders. This path is slower but works without reverse-engineering a plugin state format and keeps the instrument's own interface visible.

## Optional headless path to investigate

The third-party `DBraun/Vita` Python bindings describe a workflow to initialize the Vital engine, inspect/control parameters, connect modulation, render audio, and load/save `.vital` JSON presets. This could support a separate patch builder and automated audition harness. It is unofficial and not part of the Vital product.

Before adopting it:

1. Check current Vital and Vita versions, Python version, OS/CPU architecture, binary availability, and license obligations.
2. Confirm an initialized patch loads and saves in both the test renderer and the user's installed Vital UI. Do not assume a generated file is compatible merely because it is valid JSON.
3. Confirm each control name, value range, enum, modulation source/destination, and behavior against the installed version or Vital's source/docs. Do not use hand-guessed internal units.
4. Render a clean oscillator test, then a single modulation test, then a complete patch. Compare sample rate, note-on, note-off, tuning, stereo behavior, and effects against the DAW render.
5. Keep the first delivery non-destructive: export `.vital` preset, MIDI audition phrase, dry render, processed render, patch card, and a test report. Import into the DAW only after the file passes checks.
6. Record whether the exact patch was generated, loaded, rendered, and auditioned. These are separate states.

## Builder interface to implement

A future script or MCP tool should accept:

```yaml
patch_request:
  role:
  register:
  note_behavior:
  audible_target:
  song_context:
  constraints: []
  synth_name:
  synth_version:
  output_directory:
```

It should return:

```yaml
patch_delivery:
  preset_file:
  patch_card:
  midi_test_file:
  render_files: []
  validation_report:
  generation_status: generated | failed
  load_status: not_tested | loaded | failed
  render_status: not_tested | rendered | failed
  audition_status: not_tested | human_reviewed
  known_issues: []
```

The implementation should have separate, testable operations:

- `initialize`: start from the synth's known Init patch and record version.
- `set_parameters`: validate control IDs and value ranges before writing.
- `connect_modulation`: validate source/destination, amount, polarity, and routing.
- `save_preset`: write to a new path; never overwrite a user's approved preset.
- `render_test`: render the fixed range/velocity/phrase suite and preserve the exact MIDI.
- `analyze_render`: detect silence, clipping, clicks, bad tails, and channel-correlation outliers.
- `package_delivery`: include the preset, patch card, test phrase, dry/processed audio, and report.

## License and distribution

Vital's source repository is GPLv3, while the Vital application and its included presets have separate distribution conditions. The Vital repository explicitly says not to redistribute its included factory presets. Vita is an unofficial GPLv3 Python binding. A future tool can call an installed product or use a GPL component only after checking the applicable license and distribution model; do not bundle Vital binaries, factory presets, or a dependency in a way that conflicts with its terms.

## Workstation-specific note

One user's project notes report that their tested setup ran Vital as an x86_64 AU under Rosetta, that offline rendering through pedalboard hung, and that many simultaneously loaded instances used substantial CPU. Those observations explain why the prior workflow exported through Live and disabled unused instances. Re-measure on the current workstation before building around those constraints. The optional Vita route is promising from its published API, but it has not been tested against that installation. `FIELD_TEST.md` records a build-and-render run on that setup through a DAW set: the parameter units it measured and what the test protocol caught.
