---
name: music-critics
version: 2.1-dev
description: Provides specialized theory, originality, melody, groove, arrangement, production, emotional-impact, and mix criticism without collapsing everything into one generic quality score.
---

# Music Critics

## Mission

Diagnose musical problems and compare alternatives.

Critics do not automatically rewrite or override artistic intent.

Use only relevant critics.

## Critic output

```yaml
finding:
  critic:
  issue:
  evidence:
  severity: low|medium|high
  why_it_matters:
  possible_fixes: []
  preserve_if_intentional:
```

## Theory Critic

Checks:
- harmonic interpretation;
- voice leading;
- unresolved dissonance;
- melodic/harmonic conflict;
- key/mode assumptions;
- modulation clarity;
- note-function explanations.

Rule:
"Outside the key" is not enough to call something wrong.

## Melody Critic

Checks:
- motif;
- contour;
- range;
- rhythmic identity;
- repetition/variation;
- phrase shape;
- climax;
- singability/playability when relevant;
- relationship to harmony.

## Groove Critic

Checks:
- pocket;
- rhythmic hierarchy;
- kick/bass interaction, where the music has those roles;
- syncopation, and pulse clarity alongside it;
- microtiming concept, and whether it is a named template or arbitrary;
- competing rhythmic complexity, and the harmonic load against it;
- subdivision consistency;
- body-movement affordance;
- repetitive loop fatigue;
- whether percussion competes rather than interlocks;
- for cyclic, non-isochronous or layered metres: whether the anchor layer is audible
  (`shared/RHYTHM_SYSTEMS/`).

Do not score groove from syncopation alone, and do not assume a backbeat or a kick-and-bass
relationship exists to be judged.

## Arrangement Critic

Checks:
- section purpose;
- contrast;
- energy;
- density;
- transitions;
- register;
- overlong sections;
- underdeveloped repetitions;
- whether the piece's high point, where it has one, is earned. Named for the mechanism, not for a
  chorus or a drop: much music has neither, and "no high point" is a real and common answer for a
  drone, a process piece or a long ambient form. Do not report its absence as a defect.

## Production Critic

Checks:
- timbral identity;
- sound-role clarity;
- layering;
- automation;
- transition language;
- editing;
- sound-design consistency;
- cliché production devices.

## Mix Critic

Checks:
- hierarchy;
- masking;
- low-end conflict;
- harshness;
- mud;
- transient balance;
- stereo/depth;
- dynamics;
- translation.

Must identify upstream problems.

## Originality Critic

Checks whether distinctiveness comes from:
- harmony;
- melody;
- rhythm;
- form;
- timbre;
- performance;
- editing;
- production behavior;
- combination of familiar elements.

Flag:
- stock four-chord use without transformation;
- identical eight-bar phrasing throughout;
- predictable build/riser/drop grammar;
- generic arpeggio + pad + trap-hat combinations;
- melody always resolving to chord root;
- "weird" sound choice with otherwise generic structure.

Do not punish genre conventions that are functioning intentionally.

## Emotional Impact Critic

Checks:
- whether musical choices support intended feeling;
- whether tension/release is earned;
- whether production overwhelms emotional focus;
- whether contrast matches narrative/emotional movement;
- whether lyrics/vocals and harmony conflict productively or accidentally.

## Expectation Critic

Checks predictability, uncertainty, surprise, whether deviations are meaningful, and whether constant
novelty prevents the listener learning anything to deviate from.

Track rough curves:

```yaml
listener_expectation:
  familiarity:
  surprise:
  harmonic_tension:
  rhythmic_stability:
  energy:
  density:
  emotional_intensity:
```

Do not maximize all.
Look for shape.

## Critic Leader

When several critics disagree:

1. protect artistic intent;
2. identify the layer each critic is addressing;
3. prioritize upstream causes;
4. prefer high-impact changes;
5. preserve successful irregularities;
6. reject advice that makes the track more generic.

## Anti-overcorrection

Do not revise until every critic is happy.

A track with no friction can become anonymous.

Keep:
- deliberate dissonance;
- unusual balance;
- asymmetry;
- silence;
- roughness;
- imperfect performance;
- strange structure;

when those are part of the identity.


# Research-Integrated Critics

## Hook / Memorability Critic

Checks:
- short recognizable unit;
- motif repetition;
- rhythmic chunking;
- section placement;
- topline salience;
- compound-hook interaction;
- distinction from other hooks.

Question:
"If production were simplified, is there still a hook?"

## Timbre Critic

Checks perceptual distance and function.

Does every layer occupy the same:
- brightness;
- attack profile;
- roughness;
- motion;
- noisiness?

Or are supposedly fused layers too different to fuse?

## Auditory-Scene Critic

Checks:
- foreground clarity;
- source segregation;
- source integration;
- attention conflicts;
- vocal salience;
- excessive carving.

## Cultural-Context Critic

Flags claims such as:
- "minor means sad";
- "this chord is universally tense";
- "this rhythm is objectively complex."

Ask which audience/genre system the claim assumes.

## Automatic-evaluation warning

Do not collapse music quality into:
- spectral distance;
- chord accuracy;
- embedding similarity;
- novelty score;
- loudness;
- one LLM rating.

Human listening remains primary.


# Preference Neutrality

Critics must not smuggle personal taste into defect labels.

Each finding should identify:

```yaml
finding:
  type: defect|tradeoff|preference|intentional_choice|uncertain
  goal_assumed:
  evidence:
  recommendation:
```

Examples:

```text
"Too repetitive"
may be a preference, not a defect.

"Too loud"
depends on target and dynamics.

"Too simple"
depends on role and genre.

"Too weird"
is never sufficient criticism.
```

## General audience rule

When the user does not specify a target audience, do not invent one.

Use broad musical-function criteria and offer alternatives when taste-sensitive.


# Performance, diversity and project critics

## Performance Critic

Checks whether the notes were played or merely listed.

- Is there continuous dynamic movement where the instrument expects it, or is a long note flat?
- Do repetitions differ, or is the same sample firing?
- Does legato overlap, on a patch that needs overlap?
- Do attacks vary with dynamic and position, or is one articulation doing every job?
- Is the part physically possible, and if not, is that recorded as intentional?
- Are there breaths, releases and mechanism noise, or silence between notes?

And the one that matters most:

> **Is the timing random, or is it a model?**

Random offsets read as sloppy rather than human, and the research finds them worse than an exact grid
(`research/PERFORMANCE_AND_EXPRESSION.md`, section 1). A plan containing a percentage of humanisation
is a finding, not a style.

`type: defect` when the plan claims a model and the render shows jitter. `type: intentional_choice`
when the realism target is `deliberately_mechanical`: exactness is then the aesthetic, and calling it
stiff is the critic smuggling in taste.

## Diversity Critic

Reads the ledger, never the songs (`shared/TRACK_DIVERSITY_LEDGER.md`).

- Which dimensions do the recent tracks share?
- Is each shared dimension classified, or has nobody looked?
- Is anything classified as a project motif actually functioning as one, or was that a convenient label
  for a habit?

**Findings are questions, not defects.** "Five songs share a lift mechanism" is a finding. "This
album is repetitive" is a preference wearing a finding's clothes. Deliberate repetition, project
identity and genre convention all look identical in a table, and only the user can say which this is.

## Project Critic

Only where a project exists (`shared/PROJECT_STATE_SCHEMA.md`).

- Does this track serve a function no other track serves, or is the doubling deliberate?
- Does it fit the thesis, contradict it usefully, or contradict it by accident?
- Is it an intentional outlier, and is that recorded?
- Does it move the project's unresolved questions, or route around them?

A track can be good and wrong for its project, and it can be weak and necessary. Say which.

## Cultural-Context Critic, extended

The existing checks stand. Added: where the work uses a named musical system, read that system's file
and check the work against it rather than against a general idea of the tradition
(`shared/MUSICAL_SYSTEMS/`).

- Is the system named, or is it being used as an unnamed colour?
- Did the work take the grammar, or only the pitch set and an instrument?
- Does it carry the file's do-not-universalise cautions?
- For a fusion: is there a named bridge, or was a genre grafted on
  (`shared/FUSION_PROTOCOL.md`)?

## Critic Leader, addition

The existing rules stand, with one addition: **a critic must judge a piece against its own terms.**
"Not memorable" is not a finding about a process piece whose purpose is attention to a room. "The rule
is inaudible" is. Where a chosen exploration candidate carried constraints, the critic checks the work
against those constraints, not against the piece the candidate replaced
(`shared/EXPERIMENTAL_SYSTEMS.md`, `shared/CREATIVE_EXPLORATION_SCHEMA.md`).
