# Render Verification Protocol
## Version 1.0

Run after EVERY audio export: every pass, not only the last.

A mix can measure well while single parts are silent, missing notes, or buried.
Verification is per track and per note, not only per mix.

## Why this exists

A full-mix analysis cannot show a note that never sounded, or a part buried under the others.
Listening often finds both on passes that were only measured as a mix. This protocol checks
every track and every note.

## 1. Export

```text
1. export the full mix, with tracks muted as the deliverable mode requires
2. export every track on its own (stems): same time range, same sample rate, same
   processing state as the mix, starting at the same sample
3. keep the note schedule the render was made from
```

The note schedule is the `.mid` plus its tempo map. If notes were edited in the DAW after
import, read the schedule from the DAW's state instead, and say which source was used.

If the adapter cannot export stems, say so, then render each track solo or ask the user to
export them. Never skip the per-track checks silently.

Ableton Live: Export Audio/Video with Rendered Track set to "All Individual Tracks"
(`daw-adapters/ABLETON_LIVE.md`).

## 2. Note audit: MIDI against audio

Every scheduled note on an unmuted track must produce audible energy on that track's stem.

```yaml
note_check:
  track:
  pitch:                 # MIDI number and name, e.g. 31 (G1)
  start:                 # bar:beat and seconds
  duration:              # beats and ms
  velocity:
  result: sounded | silent | weak | unverified
  evidence:              # onset rise in dB, pitch-band energy, window level
  likely_cause:
```

Method, tool-neutral:
- convert the schedule to seconds with the tempo map;
- examine the stem from the note's onset to its end; for very short notes, to the onset plus
  the instrument's attack time plus 50 ms;
- `sounded`: an energy rise at the onset, or energy in the note's pitch band clearly above the
  stem's local floor;
- `silent`: neither;
- `weak`: sounded, but more than 20 dB below the track's median note level (default;
  CREATIVE INFERENCE);
- `unverified`: the note cannot be separated from its neighbours on this stem.

State the thresholds used.

Limitations to report, not hide:
- inside a dense chord, or a fast repeated note, one note can hide under the others: mark it
  `unverified`, not `sounded`;
- reverb and release tails can make a silent note look sounded: test the onset rise, not only
  the energy;
- long drum samples overlap: use onset detection for percussion.

Measurement traps. Each of these produces confident, wrong results:
- **Measure at the stem's full bandwidth.** Downsampling a stem (to 8 kHz, say) removes
  hi-hats, cymbals, shakers and air, and reports every one of their notes silent.
- **Combine the channels' power.** Folding a stem to mono cancels wide or out-of-phase parts.
- **Before believing "silent", check the stem's overall level.** A stem with real energy where
  every note reads silent means the measurement is wrong, not the render.
- **A pitch test is a hint, not proof.** Unison detune, chorus, glide, ring modulation and
  pitch-swept effects all read off-pitch on a peak test. At low pitches a short window cannot
  tell a quarter-tone apart. Use the energy-centred pitch, report the median offset in cents,
  and ask for a listen before calling a part out of tune.

Exclude from the audit, and list separately:
- keyswitch notes;
- notes on tracks the deliverable mode mutes (vocal lines in an instrumental export);
- notes outside the exported range.

### Likely cause of each silent note

Check in this order; report the first that fits, with its evidence:

```text
1. out of instrument range        pitch outside the calibrated sounding range, or the
                                  documented range when no profile exists
2. missing drum pad               the note has no pad in the kit's map
3. velocity too low               below the calibrated velocity floor
4. too short for the attack       duration below min_reliable_note_ms
5. same-pitch overlap             an overlapping note's note-off cut it, or it retriggered
6. routing                        wrong channel or port, instrument not loaded, track muted
                                  or disabled, clip outside the arrangement
7. dynamics control at minimum    CC or host parameter at zero at that moment
8. unknown                        say so, and offer calibration for that instrument
```

## 3. Level and masking, per track

Measure each stem only over the regions where its track plays. A sparse part averaged over
the whole song reads quiet when it is not.

```yaml
track_level_check:
  track:
  role:                          # from track state: foreground | midground | background, and function
  active_regions: []
  stem_loudness_lufs_active:
  relative_to_mix_lu:            # stem minus mix, over the same regions
  rank_in_section: {}            # loudness rank among stems, per section
  masking_ratio_db:              # stem energy in its main band against all other stems there
  flags: []                      # too_quiet_for_role | masked | role_inversion | too_loud_for_role
```

Default flags. These are starting values (CREATIVE INFERENCE); tune them to the genre and the
brief and state the values used:
- `role_inversion`: a background part measures louder than a foreground part in the same section;
- `too_quiet_for_role`: a foreground part more than 10 LU below the mix in its sections, or any
  part meant to be heard more than 20 LU below;
- `masked`: other stems exceed the part in its own main band by more than 6 dB during its active
  regions. A part can be loud enough and still be unreadable.

Fix in the pack's upstream order (`shared/MIX_FEEDBACK_PROTOCOL.md`): register and arrangement
density, then velocity and dynamics control, then instrument choice, then level, then EQ.

## 4. Analyzer: the mix and every stem

Run the reference analyzer on the mix AND on every stem: the analyzer named in the user's profile
(`analyzer`). With none configured, use this protocol's own measurements.

- Keep exact values, and keep MEASURED, INFERRED and RECOMMENDED apart
  (`shared/MIX_FEEDBACK_PROTOCOL.md`).
- If analyzing every stem is too slow for one pass, analyze every foreground stem and every
  flagged stem, and list the stems skipped.
- Compare with the previous pass when one exists, so a fix that broke another part shows.

## 5. Instrumental deliverable check

When the deliverable is instrumental (`music-director/SKILL.md`):
- confirm every vocal-line and vocal-guide track was muted for the mix;
- confirm those tracks contribute no energy to the mix;
- confirm the file name says "Instrumental".

## 6. Report

```yaml
render_verification:
  song:
  pass:
  exported_at:                   # date, time and time zone
  deliverable_mode: instrumental | vocal_guide | full_with_vocal
  mix_file:
  stems: []
  schedule_source: midi_file | daw_state
  thresholds: {}
  notes_scheduled:
  notes_sounded:
  notes_silent: []               # note_check entries
  notes_weak: []
  notes_unverified:
  excluded: []
  track_level_flags: []
  analyzer:
    tool:
    version:
    mix_report:
    stem_reports: []
    skipped_stems: []
  listened_to: true | false
  release_gate: open | blocked
  blocking_items: []
  accepted_by_user: []           # item, the user's words, date and time
  calibration_offer: made | not_needed | declined_earlier
```

## 7. Release gate

A pass may not be named FINAL, called the release, or delivered as finished while it has:
- a silent note that is neither fixed nor explicitly accepted by the user;
- a foreground part flagged `too_quiet_for_role` or `masked` that is neither fixed nor accepted.

Acceptance:
- comes from the user in the current conversation, per item or per listed group;
- is recorded with the date, the time and the user's words;
- is never inferred. The agent deciding a note "does not matter" is not acceptance.

Weak notes, unverified notes and flags on background parts are reported; they do not block.

## 8. Re-offer calibration

If a pass finds silent notes or quiet parts on instruments with no current calibration
profile, the Director re-offers calibration for those instruments
(`plugin-auditor/SKILL.md`, section 5).

## 9. Listening

Verification is a diagnostic. It can find a silent note; it cannot say whether the music works.
Report what was measured and what was not. A pass nobody has listened to is described as
"measured, not listened to".
