# Orchestral Voicing and Divisi Schema
## Version 1.0

Once a chord's identity is fixed, who plays which tone of it, and why.

Written by the Arranger (`arranger/SKILL.md`). Read by MIDI Builder, which renders the distribution
into per-instrument note assignments, and by Plugin Auditor, which checks whether an assigned patch
can actually cover a divisi part. Performance Director is a light cross-reference only — see section 5.

**This is not choir divisi.** SATB and other vocal-group divisi is the Vocal Director's territory,
already built (`shared/VOCAL_ARCHITECTURE_SCHEMA.md`, the `choir` block). This page covers
instrumental sections — strings, brass, or any pitched group splitting a chord among its own parts.
The two are read by different specialists and never merge into one block.

---

# 1. `voicing`

```yaml
voicing:
  chord_ref:                # points at the Composer's harmony event; identity stays Composer's
  distribution:
    - instrument_group:
      voice_count: 1        # e.g. violin I split a2
      tone_assigned:        # root | third | fifth | seventh | tension | doubled_tone
      register:
      doubling_of: []        # other groups doubling this tone
  divisi_reason: unison_strength | tone_distribution | range_limit | color
```

`chord_ref` names the event; it does not restate it. The chord's root, quality and extensions stay
the Composer's, decided elsewhere. This schema only answers who plays which tone of a chord someone
else already wrote.

---

# 2. Gating

Write a `voicing` entry only when a section actually has **two or more simultaneous pitched
instrument parts sharing one chord** — a string section, a horn section, a vocal-plus-instrumental
doubling. That is a condition an arrangement either has or does not have, checked part by part, not a
property of the piece as a whole.

This does not assume a genre. A string section splitting a chord in a pop arrangement gates exactly
the same way as one in a film score or a jazz chart; per `shared/GENERALIZATION_RULES.md`'s genre
neutrality, the studio does not assume a style's form or production unless the brief asks for it. The
gate is the instrumentation actually on the page — how many pitched parts are sounding the same chord
at once — never "this is an orchestral piece" used as a trigger by name.

---

# 3. Failure behavior

**Distribution is opt-in per section, never assumed.** A chord with no `voicing` entry renders exactly
as today: MIDI Builder plays the Composer's block voicing, every part sounding the same notes. Nothing
about this schema changes that default. A section only gets a distribution when the Arranger decided
it should have one and wrote the entry.

---

# 4. Rules

**Identity stays Composer's.** `chord_ref` points at the harmony event; this schema redistributes who
plays it, and never restates or alters the chord itself. A disagreement between a `voicing` entry and
the Composer's chord is a routing error, not a voicing decision, and goes back to the Composer.

**Divisi is an Arranger decision.** Whether a string section splits a2 or a3, whether a horn section
covers a chord as one voice per player, is arrangement, in the same way section length and
instrumentation are — not a Composer decision (which tones exist) and not a Producer decision (which
patch renders them).

**Every distributed tone belongs to the chord.** `tone_assigned` names a function of the chord
(`chord_ref`) points at, not an invented note. A `tension` entry should be traceable to something the
Composer actually wrote into the harmony event.

**`doubling_of` is honest about unison.** When one group's tone is chosen for strength rather than
color, name the reason as `unison_strength` and list what it doubles in `doubling_of`, instead of
letting a plain doubling read as a distribution decision it was not.

---

# 5. Who reads this

| Reader | What it gets |
|---|---|
| MIDI Builder | the distribution, rendered as each instrument group's own note assignment instead of the block voicing |
| Plugin Auditor | `voice_count` and `doubling_of` per group, to check whether the assigned patch can actually cover a divisi or doubled part |
| Performance Director | notice that a `voicing` entry exists for a section, so double-stop and divisi-thinning feasibility (`shared/HUMAN_PERFORMANCE_SCHEMA.md`) is checked against what the Arranger actually distributed, not against the block voicing. This page does not decide performability; that stays Performance Director's, unchanged. |
