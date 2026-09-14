---
name: music-critics
version: 1.0
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
- kick/bass interaction;
- syncopation;
- microtiming concept;
- subdivision consistency;
- repetitive loop fatigue;
- whether percussion competes rather than interlocks.

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
- whether chorus/drop payoff is earned.

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

## Listener Expectation Critic

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

## Expectation Critic

Checks:
- predictability;
- uncertainty;
- surprise;
- whether deviations are meaningful;
- whether constant novelty prevents learning.

## Groove Critic

Checks:
- pulse clarity;
- syncopation;
- competing rhythmic complexity;
- harmonic load;
- body-movement affordance;
- repetition.

Do not score groove from syncopation alone.

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
