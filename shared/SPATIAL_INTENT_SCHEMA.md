# Spatial Intent Schema
## Version 1.0

Where an element sits in compositional space — near or far, narrow or wide — decided upstream of
mixing, as part of the arrangement.

Written by the Arranger (`arranger/SKILL.md`). Read by Mix Engineer, as an input constraint it does
not own, and by Producer, whose sound choice can be informed by the intended space. See section 5.

**This is not mixing-time depth and stereo work.** Mix Engineer's `mix-engineer/SKILL.md` already
owns depth and stereo image as mixing decisions — its Depth section lists the mixing tools (level,
high-frequency content, transient sharpness, predelay, reverb, early reflections, compression,
automation) and states "Depth should support the arrangement hierarchy," and its Stereo section
gives the standing example that "A chorus may feel larger because the arrangement widens, not
because a stereo widener was placed on the master." Both already point at an arrangement decision
sitting upstream of the mix move. Mix Engineer's own "Does not own" section draws the boundary
explicitly: "**the song.** Composition, arrangement and production problems go back upstream. A mix
that redesigns the record has stopped being a mix." This schema is where that upstream decision — the
one Mix Engineer's prose gestures at but does not itself make — gets written down, by the specialist
that owns it.

---

# 1. `spatial_intent`

```yaml
spatial_intent:
  section:
  elements:
    - element:
      depth: foreground | mid | background
      width: narrow | wide | full
      reason:               # a compositional justification, not a mix technique
```

`reason` names why the element belongs at that depth and width in the arrangement — a role, a
narrative point, a moment of focus or retreat — never a mix mechanism. "The verse narrator should
feel close and alone before the chorus opens the room" is a reason. "Push it back with reverb" is not
a reason; it is the mix move that section 5 leaves to Mix Engineer once the intent is set.

---

# 2. Gating

Write a `spatial_intent` entry only where the Arranger has an actual compositional reason for an
element's placement in near/far, narrow/wide space — a section that should feel intimate, a hook that
should open outward, a texture meant to stay at the edges. It is not a default entry for every
element in every section; most elements have no compositional stake in their depth or width and are
left to Mix Engineer's ordinary hierarchy and stereo judgment.

---

# 3. Failure behavior

**Absent, Mix Engineer's existing depth and stereo sections behave exactly as today.** With no
`spatial_intent` entry for a section or an element, Mix Engineer places it using the hierarchy,
masking and stereo-image reasoning already in `mix-engineer/SKILL.md`, unchanged. Nothing here adds a
requirement, a default, or a new step to a mix pass that has no `spatial_intent` to read.

**This is upstream input only, never a requirement.** A `spatial_intent` entry states what the
Arranger wants; it does not obligate Mix Engineer to build it through any particular processing, and
it does not override a mix decision Mix Engineer makes for masking, translation, or feasibility
reasons. Where the two conflict, that is a handoff conversation, the same way any other upstream
constraint meeting a mixing-time problem is.

---

# 4. Rules

**Compositional, not technical.** `depth` and `width` describe where an element should sit in the
listener's sense of space, in the same vocabulary the Arranger already uses for foreground and
background (`arranger/SKILL.md`, Section role). They are not reverb sends, pan values, or widener
settings — those stay Mix Engineer's to choose.

**One element, one entry.** `spatial_intent.elements` names individual instrument roles or voices
within a section, not the section as a whole. A section-wide spatial statement is still written as a
list of its elements, even when every element shares the same depth and width, so a later change to
one element does not require rewriting the section's intent.

**Does not restate hierarchy.** `foreground_level` in the Arranger's instrument role map
(`arranger/SKILL.md`) already says what a listener attends to. `spatial_intent` answers a different
question — where that element sits in near/far, narrow/wide space — and the two can agree or
deliberately diverge: an element can be foreground in attention and still sit far in depth, if that
distance is the point.

---

# 5. Who reads this

| Reader | What it gets |
|---|---|
| Mix Engineer | `spatial_intent` as upstream context for its own depth and stereo-image work, not as something it owns or is required to follow literally; with no entry, its existing depth/stereo reasoning is unchanged |
| Producer | the intended space per element, so sound selection (a close, dry patch versus a distant, reverberant one; a narrow mono source versus an already-wide one) can be chosen to fit the compositional intent before any mix processing is applied |
