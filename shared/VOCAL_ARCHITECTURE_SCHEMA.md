# Vocal Architecture Schema
## Version 1.0

What the voices do: how many, in what relationship, doing what, and where they stop.

Written by `vocal-director/SKILL.md`. Read by Composer, Lyric Generator, Producer, MIDI Builder, Mix
Engineer and the Track Diversity Ledger.

This schema covers **architecture and performance intent**. It does not cover words
(`lyric-generator/SKILL.md`), notes (`composer/SKILL.md`), processing (`producer/SKILL.md`) or
balance (`mix-engineer/SKILL.md`).

---

# 1. `vocal_architecture`

```yaml
vocal_architecture:
  singer:
    voices_available: 1        # how many real or guide voices this plan assumes
    declared_range: {low:, high:}      # from the brief or the profile; never assumed
    comfortable_tessitura: {low:, high:}
    registers_used: []         # chest, mix, head, falsetto, belt, whistle, spoken, whispered
    passaggio_notes: []        # where the brief says transitions sit, if known
    language_and_diction: []

  hierarchy:
    lead:                      # the line that carries the song
    secondary: []              # answers, counter-lines, pre-choruses handled by another voice
    background: []             # by function, not by "BVs"
    the_rule: "every added layer has a function, or it does not get added"

  by_section:
    - section:
      lead_behavior:           # register, intensity, delivery, phrasing character
      doubles: {count:, tightness:, purpose:}
      octave_doubles: {above:, below:, purpose:}
      stacks:
        - voicing: []          # intervals or note names, inside the declared range
          count:
          pan_plan:            # placement intent, not mix settings
          vowel:               # what the stack sings, which is often not the lyric
          purpose:
      call_and_response: {caller:, responder:, placement:}
      ad_libs: {placement: [], density:, purpose:}
      texture: []              # whisper, spoken, gang, choir, chant, hum, vocoded guide
      silence:                 # where the voice stops, and why
      breath_plan: []          # where breaths fall; staggered for groups
      intensity: 1-5           # relative, across the song
      imperfection_intent: []  # per shared/HUMAN_PERFORMANCE_SCHEMA.md section 4

  flow:                        # for rapped, chanted or spoken delivery
    subdivision:
    placement: ahead | on | behind
    rhyme_landing: []          # where the rhyme falls against the beat
    phrase_lengths: []
    breath_points: []
    density_curve: []

  choir:                       # only for choir and large-group writing
    parts: []                  # SATB or other, with counts
    divisi: []
    blend_intent:
    consonant_timing_ms:       # consonants land before the beat; see the guide
    vowel_plan: []
    staggered_breathing: true | false

  comp_strategy:               # for real recording sessions
    takes_planned:
    what_to_keep:              # e.g. the first take's verse energy, a later chorus for pitch
    punch_points: []

  tracks_for_midi_builder:
    - name:
      role: vocal_line | vocal_guide
      function:                # lead, double, harmony, ad_lib, gang, choir, spoken
      muted_in_instrumental: true
```

---

# 2. Rules

**Function before layer.** A double, a stack or an ad-lib enters because it does something: widens,
lifts, answers, confides, crowds, or contradicts. "Because the chorus needs more" is not a function.

**Range is declared, never assumed.** If the brief does not give a range, the Vocal Director asks once
or writes within a conservative range and says which it did. Stacks stay inside the declared range.

**Silence is part of the architecture.** The field exists so that a section with no voice is a
decision rather than an omission.

**Imperfection follows the performance schema.** Doubles are imperfect because two takes differ, not
because a randomiser moved them.

**No identity imitation.** The studio never plans a vocal to sound like a specific living artist. A
reference gives mechanisms: register contrast, stack density, how a phrase ends, where a voice stops.
It never gives an identity to reproduce. This follows `music-research/SKILL.md` section 13, and beyond
originality it is a legal exposure in jurisdictions that have extended publicity rights to voice.

**Ornament belongs to its tradition.** Melisma, gamaka, blues inflection, maqam ornamentation and
gospel runs are not interchangeable decoration. Route through `shared/MUSICAL_SYSTEMS/` and name the
system.

---

# 3. Diversity

The ledger stores the shape, so that five songs do not quietly share one chorus.

```yaml
track_dna.vocal_architecture:
  lead_register_strategy:      # e.g. verse low and close, chorus high and wide
  chorus_lift_mechanism:       # doubles, octave above, stack, group, register change, none
  background_density:          # none, sparse, moderate, dense, choral
  answer_strategy:             # call and response, counter-line, none
  ad_lib_density:
  texture_signature: []
  silence_used: true | false
```

Two consecutive songs sharing a chorus vocal architecture is a flag, not an error. The Director asks
whether it is project identity or habit (`shared/TRACK_DIVERSITY_LEDGER.md`).

---

# 4. Handoffs

| To | What it gets |
|---|---|
| Composer | requests to change contour, range or phrase length, with the reason |
| Lyric Generator | which lines carry the hook, where breaths are, what a stack sings |
| Performance Director | `performance_state` entries for each vocal part |
| MIDI Builder | the track list with roles, so an instrumental export mutes by role |
| Producer | what the layers are for, so processing serves the architecture |
| Mix Engineer | the intended hierarchy and where it changes by section |
