---
name: listener-model
version: 2.1-dev
description: Models musical expectation, uncertainty, surprise, groove, memorability, salience, emotion, and auditory-scene perception to guide composition, arrangement, production, and mixing.
---

# Listener Model

## Mission

Estimate how a target listener may experience musical events over time.

This is not a taste oracle.
It is a cognitive design tool.

Use it when the task involves:
- "catchy";
- "boring";
- "predictable";
- "surprising";
- "groovy";
- "tense";
- "emotional";
- "too busy";
- "hard to focus on";
- "the hook does not land";
- "everything blends together."

---

# 1. Expectation Architecture

Model two partially independent sources of musical expectation:

```text
COGNITIVE EXPECTATION
Long-term learned knowledge of musical style and syntax.

SENSORY EXPECTATION
Short-term acoustic continuation based on the immediately heard signal.
```

Do not assume they produce identical predictions.

A chord can be:
- stylistically surprising but acoustically smooth;
- stylistically ordinary but sonically shocking because of voicing/timbre;
- surprising in both;
- expected in both.

For planning, track:

```yaml
expectation_event:
  expectedness_from_style:
  expectedness_from_local_context:
  uncertainty_before_event:
  surprise_after_event:
  resolution_effect:
```

---

# 2. Information-Style Reasoning

When no statistical model such as IDyOM is available, use qualitative approximations.

## Surprise

Ask:
"Given the preceding context and target listener, how probable would this event feel?"

## Uncertainty

Ask:
"Before the event happens, how many continuations feel plausible?"

This distinction matters.

A section can have:

```text
LOW UNCERTAINTY + HIGH SURPRISE
The path seemed obvious, then the track violates it.

HIGH UNCERTAINTY + LOW SURPRISE
Many outcomes seemed possible, and the track chooses a conventional one.
```

Both configurations can be pleasurable in the right context.

---

# 3. Intermediate Complexity

Research frequently finds preference for manageable predictive challenge rather than maximal
simplicity or maximal unpredictability.

Use this as a design question:

```text
Is the listener learning the track?
```

If everything is obvious:
- add a controlled deviation;
- delay a resolution;
- transform the motif;
- alter phrase ending;
- shift accent;
- change harmonic function.

If everything is unstable:
- repeat;
- establish a pulse;
- preserve a motif;
- simplify harmony;
- provide a predictable anchor.

Do not mechanically target the middle.
Genres and artistic goals differ.

---

# 4. Groove Model

Groove is the pleasurable desire to move with the music.

Rhythmic complexity and syncopation are important, but groove is not equivalent to an
arithmetic syncopation score.

Research suggests a common inverted-U pattern where moderate syncopation often produces
stronger groove and pleasure than very low or very high syncopation.

Use:

```yaml
groove_profile:
  pulse_clarity:
  metric_type: isochronous | non_isochronous | cyclic | layered | free
  anchor_layer:                # what the listener holds on to; required where layers conflict
  syncopation:
  subdivision_stability:
  low_end_coordination:        # kick and bass where those roles exist; the equivalent where not
  backbeat_strength:           # where the style has a backbeat at all
  microtiming_character:       # a named template and its corpus, or none
  repetition:
  rhythmic_complexity:
  harmonic_complexity:
  body_movement_affordance:
```

Not every music has a backbeat, a kick or a bass. A groove profile that assumes them will report their
absence as a defect. Where the metre is cyclic, non-isochronous or layered, the question that replaces
backbeat strength is whether the anchor layer is audible (`shared/RHYTHM_SYSTEMS/`).

## Groove repair

Too rigid:
- introduce off-beat accents;
- ghost notes;
- anticipations;
- delayed attacks;
- call-response across drum voices.

Too chaotic:
- strengthen pulse;
- reduce competing syncopations;
- simplify one layer;
- let one rhythmic anchor repeat.

High harmonic complexity can compete with rhythmic groove in some contexts.
If the rhythm is already cognitively demanding, question whether the harmony also needs to
be maximally dense.

---

# 5. Hook / Memorability Model

Hooks involve both salience and memory.

Potential hook sources:
- topline/vocal phrase;
- instrumental motif;
- bass figure;
- rhythmic cell;
- production gesture;
- lyric phrase;
- compound hook combining several layers.

Track:

```yaml
hook:
  recognizable_unit:
  repetition:
  variation:
  contour:
  rhythm:
  placement:
  topline_or_backing:
  chorus_association:
  compound_layers:
  contrast_before_hook:
  recall_test:
```

Research supports:
- motif repetition as helpful for explicit melodic memory;
- chorus/topline placement as often salient;
- compound hooks as potentially more memorable/salient;
- repeated exposure increasing familiarity.

But repetition can reduce novelty.

Design a hook as:

```text
stable identity
+
controlled variation
```

not:

```text
copy-paste forever.
```

---

# 6. Earworm Heuristics

Do not promise an earworm.

Potential contributors:
- common/global contour that is easy to encode;
- distinctive local interval movement;
- clear rhythmic chunk;
- repeatable phrase length;
- repeated motif;
- singable range;
- exposure/familiarity.

A memorable melody may combine a familiar global shape with one unusual local feature.

---

# 7. Tension Model

Musical tension can emerge from multiple features operating over different time scales:

- harmony;
- pitch height;
- dynamics;
- onset density;
- tempo;
- register;
- dissonance/roughness;
- syncopation;
- tonal distance;
- phrase compression;
- repetition without resolution.

Do not assume all tension must come from dissonant chords.

Long-range harmonic tension can evolve over many seconds or sections, while onset density
or dynamics may act much faster.

---

# 8. Timbre Perception

Timbre is multidimensional and depends on spectrotemporal patterns.

Use perceptual descriptors before plugin parameters. The canonical dimensions are defined once, in
`shared/LISTENER_STATE_SCHEMA.md`, and the Producer uses the same list.

```yaml
perceptual_timbre:
  hard_soft:
  sharp_dull:
  bright_dark:
  explosive_calm:
  rough_smooth:
  stable_moving:
  tonal_noisy:
  dense_open:
```

Then translate into synthesis/production choices.

Avoid reducing timbre to "brightness" alone.

---

# 9. Auditory Scene Model

Listeners can either integrate layers into one percept or segregate them into separate streams.

Separation is influenced by:
- timbre distance;
- register/frequency separation;
- timing;
- spatial location;
- attention;
- structural role.

Use:

```yaml
auditory_scene:
  foreground:
  secondary_streams: []
  fused_layers: []
  intentionally_masked_layers: []
  segregation_problem:
  integration_problem:
```

A mix is not automatically better when every layer is maximally separable.

Sometimes layers should fuse.

---

# 10. Vocal Salience

Lead vocals are often unusually robust attractors of auditory attention in popular-music
mixtures.

Implication:

If the vocal is meant to be secondary, simply lowering it may not fully remove its attentional
pull.

If the vocal is meant to dominate, not every backing element needs to be aggressively carved
away.

Treat vocal presence as an attention decision, not only a dB decision.

---

# 11. Cultural Calibration

Do not universalize emotional mappings.

The listener model should record:

```yaml
target_listener:
  culture_or_scene:
  genre_familiarity:
  musical_training:
  age_context:
  expected_listening_environment:
```

Major/minor, consonance/dissonance, mood labels, and harmonic expectation can depend on
cultural learning and exposure.

Some broader dimensions such as valence/arousal may travel better across cultures than
specific verbal mood labels.

---

# 12. Output

Return:

```yaml
listener_model_report:
  strongest_attention_anchor:
  most_memorable_material:
  predictability_problem:
  uncertainty_problem:
  surprise_opportunity:
  groove_profile:
  tension_curve:
  scene_separation:
  emotional_fit:
  cultural_assumptions:
  recommended_experiments: []
```

Prefer testable alternatives over absolute claims.


# General Listener Calibration

The listener model must not assume the previous user's musical taste.

For every new task, derive expectations from:

```yaml
listener_context:
  target_audience:
  genre_familiarity:
  listening_environment:
  purpose:
```

If these are unknown, keep the analysis probabilistic and avoid claims such as:

```text
"listeners will definitely find this catchy."
```

Prefer:

```text
"This design increases repetition and contour clarity, which may improve memorability for
listeners familiar with this style."
```


# Listener panel

One simulated listener hides disagreement, and the disagreement is the useful part.

```yaml
listener_panel:
  perspectives:
    - name: scene_native | casual | musician | producer | live_crowd | headphone_listener
      attention_channels: []   # affect_and_gist, structure_and_harmony,
                               # production_and_timing, body_and_groove
      what_they_notice:
      how_it_feels:
      what_they_would_not_notice:
  agreements: []
  disagreements: []            # returned, never averaged
  confidence: low
```

## What the perspectives are

They are **attention channels**, not demographic caricatures. Research finds untrained listeners
perceive tension, structure and emotion at levels close to trained ones; the reliable difference is in
what they can *name* (`research/CREATIVITY_AND_PEDAGOGY.md`, section 7).

| Perspective | Weights | Does not |
|---|---|---|
| `casual` | affect and gist | use theory terms, or notice structure as structure |
| `scene_native` | genre-specific timing, production signatures, what is expected here | judge against another scene's conventions |
| `musician` | structure, harmony, melodic and rhythmic detail | speak for how it feels to someone not listening that way |
| `producer` | arrangement, sound choice, mix decisions | say whether the song is good |
| `live_crowd` | body, energy, dynamics, the shared moment | hear detail |
| `headphone_listener` | detail, stereo, depth, quiet events | feel a room |

## Rules

- **Return disagreements.** When the musician perspective and the live-crowd perspective conflict, that
  is the finding. Averaging produces a listener who does not exist.
- **The casual perspective reports feeling, not analysis.** It says it lost interest before the chorus.
  It does not say the pre-chorus lacks a lift.
- **This is not survey data.** It is qualitative modelling, and every report says so. Simulated
  listeners over-articulate: they name specifics that real listeners in the same position often do not
  notice at all, and untrained listeners in one study reported differences that were not there.
- **A real playback test with one person outranks the whole panel.** Say that too.

## When to use it

When a decision turns on who is listening: whether a reference is too obvious, whether an unusual
choice will read as intentional, whether a long intro is patient or slow. Not for every task; the
single listener context is enough for most.

# Long-form and process music

Expectation still applies to a twenty-minute ambient piece or a process piece, on a longer time scale.
The question is whether there is enough repetition for the listener to learn the pattern before it
changes. A process nobody can track is not surprising, it is uniform
(`shared/EXPERIMENTAL_SYSTEMS.md`).
