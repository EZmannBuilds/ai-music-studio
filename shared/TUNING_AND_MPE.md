# Tuning, Microtonality and Per-Note Expression
## Version 1.0

How a pitch system that is not twelve-tone equal temperament actually reaches an instrument, and what
to do when it cannot.

The musical systems themselves are in `shared/MUSICAL_SYSTEMS/`. This page is implementation.

```text
Composer              chooses the pitch system
Plugin Auditor        reports whether each instrument can be tuned, and by which mechanism
MIDI Builder          writes it, by the highest tier the target supports
DAW adapter           imports scales, routes MPE, writes automation
Producer              chooses timbres that suit the tuning
```

---

# 1. The rule

**Never silently quantise a pitch system to twelve-tone equal temperament.**

If the chosen instrument cannot be retuned, the studio says so, and then: proposes a fallback,
proposes a substitution, or asks. A microtonal piece rendered in equal temperament without a word is
a wrong deliverable that looks like a right one.

---

# 2. Cents are the interchange format

Pitch intent is stored in **cents from a stated reference**, because that survives every tier below.

```yaml
pitch_system:
  name:                        # e.g. 31-EDO, 5-limit JI on C, a measured maqam intonation
  kind: edo | ji | temperament | measured | scale_file | 12tet
  period: 2/1                  # the repeat interval; not always the octave
  degrees_cents: []            # cents from 1/1, ascending
  reference: {note:, hz:}      # what 1/1 actually is
  source:                      # where this tuning came from
  evidence: measured | documented | constructed | to-verify
  scale_file:                  # path to a .scl, if one exists
  keyboard_map:                # path to a .kbm, if one exists
```

A tuning taken from a recording of one performer or one ensemble is **one measured instance**, and the
file says so (`shared/MUSICAL_SYSTEMS/INDEX.md`).

---

# 3. The four tiers

Use the highest tier the target actually supports. The Plugin Auditor reports which.

### Tier 1: a session-wide tuning master

A master plugin retunes every client plugin in the session, in real time, including notes already
sounding. Ordinary MIDI notes are written; no channel juggling, and any number of notes per period.

Use when every instrument in the project is a client. Note that a client with no master present falls
back to its own local table, which is twelve-tone equal by default.

### Tier 2: per-instrument scale files

Load a scale file into each instrument.

```text
.scl    the scale: a description line, the note count, then one pitch per line as cents
        (a value containing a period) or a ratio. 1/1 is implicit; the last line is the period.
.kbm    the keyboard mapping: which MIDI notes are retuned, which key is 1/1, and which
        note and frequency are the reference.
```

**A `.scl` without a `.kbm` is key-ambiguous.** Products differ in where they put 1/1: some at a fixed
MIDI note, some near the middle of the range, some at the reference frequency. The same file therefore
lands in different keys in different instruments, and not every product reads `.kbm` at all. Verify the
sounding reference after loading, in every instrument, and record it.

### Tier 3: per-note pitch bend, MPE

An MPE zone gives each note its own channel, and therefore its own pitch bend.

```text
zones          a lower zone with master channel 1, an upper zone with master channel 16
per note       pitch bend, channel pressure and CC74 on member channels
bend range     ±48 semitones by default on member channels, ±2 on the master,
               configurable through RPN 0
resolution     about 0.586 cents per unit at 14-bit across ±48
polyphony      at most 15 simultaneously expressive notes in a single zone
```

**Always declare the bend range alongside bend data.** A receiver assuming ±2 will play a ±48 gesture
as noise. Reducing the range increases resolution, which is worth doing for fixed retuning where large
gestures are not needed.

### Tier 4: one voice per channel

Set a bend range per channel with RPN 0, put one voice on each channel, and bend each to its target.
This costs polyphony and is fragile, but it works almost everywhere. It is the fallback, not the plan.

A further option for fixed retuning is the MIDI Tuning Standard: a bulk dump to retune a whole table,
or real-time single-note retuning, at a resolution near 0.0061 cents. Support is uneven, so the
Auditor checks rather than assuming.

---

# 4. What the Plugin Auditor records

Added to the capability map in `shared/PLUGIN_CALIBRATION_SCHEMA.md`:

```yaml
capability:
  tuning_support:
    mechanisms: []             # tuning_master_client | scl | kbm | tun | mts_sysex | per_note_bend | none
    notes_per_period:          # some products accept only 7 or 12
    reference_note_behavior:   # where this product puts 1/1
    retunes_held_notes: true | false | unknown
    caveats: []                # e.g. "filters do not track the tuning"
    evidence: measured | vendor_documented | inspected | user_stated | inferred
  mpe:
    supported: true | false | unknown
    zones:
    default_bend_range_semitones:
    per_note_controllers: []
  pitch_bend_range_semitones:
  per_note_expression: true | false | unknown
```

The caveat field matters. A product can accept a scale file and still not apply it to every part of
its signal path, which sounds like a tuning bug and is not.

---

# 5. What MIDI Builder does

```yaml
tuning_export:
  tier_used: master | scale_file | mpe | per_channel_bend | none
  mechanism:
  scale_file_shipped:          # path, when one travels with the deliverable
  bend_range_declared_semitones:
  channels_used:
  what_happens_if_ignored:     # the honest sentence: what a receiver that ignores this will play
  verified_on:                 # what it was checked against, or "not verified"
```

Standard MIDI Files carry tuning sysex and per-channel bends, but only if the receiver honours them,
and they cannot carry a session tuning master or MIDI 2.0 per-note controllers. So the export names
its tier and states the failure mode. Where a scale file exists, it ships beside the MIDI, named per
`shared/FILE_NAMING.md`.

Render Verification's pitch test needs to know the tuning, or it will report every correctly tuned
note as out of tune. The tuning record is part of the note schedule handed to it
(`shared/RENDER_VERIFICATION.md`).

---

# 6. Timbre and tuning are one decision

Consonance depends on how a timbre's partials line up with the scale being used. For inharmonic
timbres, and for stretched or compressed partials, the intervals that sound stable change
(`research/MUSICAL_SYSTEMS_AND_TUNING.md`, section 3).

Consequences the Producer acts on:

- a bright sawtooth in an unfamiliar equal division will beat in ways a softer timbre will not;
- bell-like and metallophone timbres suit scales built for their partials, which is part of why
  gamelan tunings and gamelan timbres belong together;
- a drone's own overtone structure sets what the melody can lock to;
- if a tuning sounds wrong, changing the timbre is a legitimate fix and sometimes the right one.

---

# 7. Practical checks

Before relying on a tuning:

1. **Sound a reference interval and listen.** A just fifth beats slowly or not at all. If it beats
   fast, the tuning did not take, or 1/1 landed somewhere unexpected.
2. **Check the reference pitch per instrument**, not once for the project.
3. **Check the range of the scale.** Some products apply a scale only across part of the keyboard.
4. **Check held notes**, if the piece retunes during a sustain.
5. **Record what you did** in the track state, so the next session does not re-derive it.

---

# 8. What this page does not decide

- Which pitch system to use. That is the Composer, working from the brief and, where relevant, from
  `shared/MUSICAL_SYSTEMS/`.
- Whether a tradition's intonation can be represented by a fixed table. Often it cannot: intonation
  can belong to a phrase and a context rather than to a scale degree. A `.scl` may be the wrong object
  entirely, and a bend-based, phrase-shaped approach the right one.
- Which products support what today. That is the Auditor's job, and the answer changes.
