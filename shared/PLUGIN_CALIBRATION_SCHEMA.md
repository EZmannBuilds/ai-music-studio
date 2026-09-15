# Plugin Audit and Calibration Schema
## Version 1.0

> Used by `plugin-auditor/SKILL.md`.

Three records:

```text
plugin_audit          what is installed and what it claims to do     (per setup, per audit)
calibration_offer     what was offered and what the user answered    (per offer)
calibration_profile   what one instrument measured when rendered     (per instrument/patch/version)
```

## 1. Plugin audit

```yaml
plugin_audit:
  audit_id:
  performed_at:                    # date, time and time zone
  machine:
  operating_system:
  daw:
    name:
    version:
    connection_layer:              # e.g. an MCP bridge, OSC, scripting API, manual
  sources_scanned:
    - kind: daw_stock | au | vst | vst3 | sample_library | user_content | other
      location:
      method: filesystem_listing | daw_browser | vendor_app | user_statement
  instruments:
    - id:                          # stable id, e.g. vendor.product.edition.patch
      display_name:
      vendor:
      product:
      edition:
      version:
      format: stock | au | vst | vst3 | clap | aax | sampler_library
      location:
      loadable_by_agent: true | false | unknown
      load_note:                   # e.g. "the loader only reaches the User Library"
      agent_control:               # how an agent can drive it (plugin-auditor, section 3)
        api:                       # through the DAW or host: parameters a script can set
          automatable_parameters: []   # e.g. ["Dynamics", "Expression", "Reverb"]
          reached_through: []          # e.g. the DAW adapter's set-parameter call
        midi:
          cc: []                   # e.g. ["CC1 dynamics", "CC11 expression"]
          keyswitches: []
        code:
          preset_format:           # e.g. "JSON", "SFZ text", "XML", "proprietary binary"
          code_can_write_presets: true | false | unknown
          headless_render: []      # hosts that render it without a GUI, if any
        screen: usable | login_gated | unknown   # the GUI as a last resort
        person_only_steps: []      # install, account sign-in, license activation, library download
        verdict: api | code | screen_only | none
      family:                      # strings, brass, keys, synth, drums, ...
      patches_or_presets: []
      capability:
        playable_range:
          documented: {low:, high:}
          measured: {low:, high:}
          range_gaps: []
        articulations:
          available: []
          switching: separate_patch | keyswitch | cc | host_parameter | none
          keyswitch_notes: []      # sounding-silent by design; excluded from note audits
        dynamics_control:
          method: velocity | cc1 | cc11 | cc7 | host_parameter | none
          host_parameters: []      # e.g. ["Dynamics", "Expression"]
          reaches_instrument: true | false | unknown
        velocity_response:         # e.g. "inaudible below 30", or a curve reference
        drum_map: {}               # note -> pad name, kits only
        stereo:
          mic_positions_available: []
          width_note:
          measured_correlation:
        tone:
          measured_centroid_hz:
          brightness_controls: []  # e.g. rack macros that hold the filter cutoff
          note:
        known_gaps: []
        expression:              # what this instrument needs from a performance plan
          round_robins: true | false | unknown
          round_robin_count:
          dynamic_layers:
          dynamics_crossfade: true | false | unknown   # layers crossfade, or switch
          legato:
            present: true | false | unknown
            monophonic: true | false | unknown
            requires_overlap: true | false | unknown
            transition_latency_ms:          # compensate with a negative track delay
            transition_selected_by: velocity | cc | speed | none | unknown
          release_samples: true | false | unknown
          per_note_expression: true | false | unknown
        tuning_support:          # shared/TUNING_AND_MPE.md
          mechanisms: []         # tuning_master_client | scl | kbm | tun | mts_sysex |
                                 # per_note_bend | none
          notes_per_period:      # some products accept only 7 or 12
          reference_note_behavior:        # where this product puts 1/1
          retunes_held_notes: true | false | unknown
          caveats: []            # e.g. "filters do not track the tuning"
        mpe:
          supported: true | false | unknown
          zones:
          default_bend_range_semitones:
          per_note_controllers: []
        pitch_bend_range_semitones:
      evidence:
        - field:
          value:
          source: measured | vendor_documented | inspected | user_stated | inferred
          reference:               # file, render, documentation page, the user's words
      calibration_profile_id:      # empty until calibrated
  new_since_previous_audit: []
  removed_since_previous_audit: []
  score_coverage:
    - score_part:
      assigned_instrument:
      status: native | substitution | missing | partial_range
      out_of_range_notes: []
      unmapped_drum_notes: []
      dynamics_method:
      substitution:
        replacement:
        reason:
        track_label:
      user_decision_needed: true | false
```

## 2. Calibration offer

```yaml
calibration_offer:
  offered_at:                      # date, time and time zone
  reason: first_use | new_plugin | new_edition | new_version | silent_notes_found |
          quiet_part_found | user_report
  instruments_in_scope: []
  test_seconds_per_instrument:
  estimated_minutes:
  needs: [daw_control, screen_control, export, analyzer]
  user_response: approved | approved_partly | declined | deferred
  approved_instruments: []
  responded_at:
  user_words:                      # quote the answer
```

An offer with no recorded `user_response` is not an approval.

## 3. Calibration profile

```yaml
calibration_profile:
  profile_id:
  instrument_id:                   # matches plugin_audit.instruments[].id
  instrument_version:
  edition:
  patch_or_preset:
  mic_or_mix_setting:
  daw:
    name:
    version:
  sample_rate_hz:
  performed_at:
  offer_ref:                       # the calibration_offer that approved it
  test_program:
    tempo_bpm:
    range_sweep: {low:, high:, velocity:, note_length_beats:, gap_beats:}
    velocity_ladder: {pitch:, velocities: []}
    dynamics_sweep: {pitch:, control:, from:, to:, seconds:}
    sustained_note: {pitch:, velocity:, seconds:}
    drum_pad_scan: {notes: [], velocity:}
    deviations_from_default: []
  measurement:                     # every value here is MEASURED
    silence_threshold:             # state it, e.g. "-60 dBFS peak or floor + 6 dB"
    silent_notes: []
    sounding_range: {low:, high:}
    range_gaps: []
    level:
      mf_rms_dbfs:
      ff_rms_dbfs:
      mf_peak_dbfs:
      velocity_curve: [{velocity:, rms_dbfs:}]
      velocity_floor:
    dynamics_control:
      control:
      reaches_instrument: true | false
      range_db:
    spectral_centroid_hz:
    stereo_correlation:
    attack_ms:
    min_reliable_note_ms:
    release_tail_ms:
    noise_floor_dbfs:
  derived_rules:                   # CREATIVE INFERENCE drawn from the measurement
    clamp_range: {low:, high:}
    velocity_floor:
    min_note_length_ms:
    gain_offset_db:                # against the set's reference instrument at mf
    dynamics_method:
    width_or_mono_note:
    brightness_note:
    substitution_note:
  analyzer:
    tool:
    version:
    files: []
  renders: []                      # test audio paths
  status: current | stale | superseded
  stale_when:
    - plugin version changes
    - edition changes
    - patch or mic setting changes
    - DAW version changes
    - sample rate changes
```

## Rules

- **A calibration profile describes a patch, never a player.** Human limits (breath length, roll
  speed, hand span, pedal and string constraints) are not calibration values; they come from the
  instrument's page in `shared/VIRTUAL_INSTRUMENT_GUIDE/`, with that page's evidence label.
- `measurement` holds only values read from the calibration renders. Nothing documented,
  inferred or remembered goes there.
- `derived_rules` are recommendations. Specialists follow them unless the Director records a
  reason not to.
- A stale profile is still evidence, but its values are labelled stale in every handoff.
- Keep units in every value (dBFS, LU, Hz, ms, beats). Preserve analyzer output exactly
  (`shared/SPECIALIST_HANDOFF_SCHEMA.md`).
- Store profiles and test renders outside song folders and outside any notes or knowledge
  vault, at a location the user has confirmed.

## Example: one instrument, documented but not yet calibrated

```yaml
- id: examplevendor.orchestra.essentials.bassoons
  display_name: Bassoons (Orchestra Essentials)
  vendor: ExampleVendor
  product: Orchestra
  edition: Essentials
  format: vst3
  capability:
    dynamics_control:
      method: host_parameter
      host_parameters: ["Dynamics", "Expression"]
      reaches_instrument: true
    known_gaps: ["no contrabassoon in this edition"]
  evidence:
    - field: dynamics_control.reaches_instrument
      value: true
      source: measured
      reference: render pass with CC1 (no dynamics) against a pass with host-parameter envelopes
    - field: known_gaps
      value: no contrabassoon
      source: inspected
      reference: installed library contents
  calibration_profile_id:
```
