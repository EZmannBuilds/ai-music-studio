# Recording and Lineage Schema
## Version 1.0

Two authored facts about a sound's identity over time, in one schema: the recording perspective a
section is deliberately given, and what happened to a sound across production passes, and why.

Written by the Producer (`producer/SKILL.md`). Read by Plugin Auditor, which checks patch choices
against a declared recording scene; by Mix Engineer, which reads the scene as context it does not
own; and by Project Guide, which surfaces lineage during REVISE mode. See section 5.

**Why one file covers both.** A recording scene and a lineage entry look unrelated — one is a spatial
choice for a section, the other is a change log for a sound — but both answer the same kind of
question: not what a sound *is* right now, but what was decided about it and when, on purpose. Neither
is a passive fact sitting on a patch; both are authored, timestamped decisions the rest of the studio
can read back.

---

# 1. `recording_scene`

```yaml
recording_scene:
  section:
  perspective: close | roomy | distant | hybrid
  why:
```

A `recording_scene` entry is the Producer setting a mic/room perspective for a section on purpose —
"this section should sound like it was captured in a small room, close" — not a report of whatever a
patch happens to ship with.

# 2. `sound_lineage`

```yaml
sound_lineage:
  element:
  log:                        # ordered, oldest to newest
    - change:
      reason:
      from_pass:
      to_pass:
```

`sound_lineage.log` is ordered oldest to newest. Each entry names what changed about the element
(resampled, re-amped, layered, replaced, retuned, re-recorded), why, and the two passes the change
sits between, so a later session can read the element's history rather than reconstruct it from
memory.

---

# 3. Failure behavior

**Purely additive.** The recording facts the Producer already tracks keep working exactly as they do
today with no `recording_scene` or `sound_lineage` entry written. `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md`
already carries `mic_or_room_behavior` — what the recorded positions and room change, including width
— as a passive fact about an instrument's captured character, in section 2's
`virtual_instrument_programming` block. `shared/PLUGIN_CALIBRATION_SCHEMA.md` already carries the
equivalent measured fact in section 3, `calibration_profile.mic_or_mix_setting`. Neither field is
touched, renamed, or superseded by this schema, and both keep answering the question they already
answer: what a patch's recorded perspective actually is.

**This schema is where those facts become a decision.** `mic_or_room_behavior` and
`mic_or_mix_setting` describe what a patch already sounds like. A `recording_scene` entry is different
in kind, not degree: the Producer choosing a perspective for a section on purpose, which may match
what a patch already offers or may call for a different patch, mic position, or treatment to reach.
Write a `recording_scene` entry only when the brief calls for that decision to be explicit and
tracked; most sections use whatever perspective their instruments already have, undeclared, exactly as
before.

---

# 4. Rules

**A scene is a decision, not an inventory.** `recording_scene.perspective` states what the Producer
wants a section to sound like it was captured as. It is distinct from `mic_or_room_behavior`
(what a patch's recording already is) and from `mic_or_mix_setting` (what a calibration measured); a
`recording_scene` entry may agree with either, or may be the reason a different patch gets chosen.

**Lineage records the change, not just the result.** `sound_lineage.log` exists so a later pass can
see that an element was, for example, resampled and re-amped for grit, and why — not only what the
element sounds like now. An element with no interesting history needs no `sound_lineage` entry.

**`from_pass` and `to_pass` are the project's own pass labels**, whatever the project already uses to
name a production pass (`shared/PROJECT_STATE_SCHEMA.md`, `shared/TRACK_STATE_SCHEMA.md`). This
schema does not invent a separate versioning scheme.

**Never a substitute for the audit or the calibration profile.** Plugin Auditor's `score_coverage`
and Plugin Calibration's measured values remain the record of what an instrument actually is and does
(`plugin-auditor/SKILL.md`, `shared/PLUGIN_CALIBRATION_SCHEMA.md`). `recording_scene` is read
alongside them as an additional, authored constraint — never in place of the measurement.

---

# 5. Who reads this

| Reader | What it gets |
|---|---|
| Plugin Auditor | a declared `recording_scene`, checked against the assigned patch's actual capability, alongside its ordinary capability map and divisi-feasibility work (`plugin-auditor/SKILL.md`) |
| Mix Engineer | `recording_scene` as context for depth and space decisions it does not own — the same "does not own the song" boundary as `shared/SPATIAL_INTENT_SCHEMA.md` |
| Project Guide | `sound_lineage`, surfaced during REVISE mode so a revision queue can show an element's production history, not only its current state |
