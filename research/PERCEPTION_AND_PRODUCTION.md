# Research: Listener Perception, Groove, Timbre and Evaluation

## Purpose

The research behind the studio's composition, arrangement, production, mixing and critique
procedures.

The guiding question:

> Which findings can be converted into useful composition, arrangement, production, mixing,
> and critique procedures?

It covers listener expectation, groove, hooks and memory, long-range musical structure, timbre,
auditory scene analysis, intelligent music production, and evaluation.

---

# 1. Musical Expectation

## Research

Recent work comparing computational expectancy models with ratings of more than a thousand
chords from Billboard pop songs found that cognitive/style-based and sensory/acoustic
expectations independently contributed to musical expectancy and pleasure.

IDyOM-style models distinguish:

- information content: surprise of an event after it occurs;
- entropy: uncertainty about possible upcoming events before one occurs.

The cognitive model explained substantially more variance in perceived chord surprise than
the sensory model in that study.

Other work found nonlinear relationships between predictability/uncertainty and musical
pleasure, supporting the idea of manageable predictive challenge rather than maximal
predictability or maximal surprise.

Another pop-harmony study found high pleasure in at least two expectation configurations:

- low uncertainty + high surprise;
- high uncertainty + low surprise.

## Skill translation

Added:

- Listener Model;
- expectation event schema;
- uncertainty vs surprise distinction;
- intermediate-complexity reasoning;
- complexity-budget rule.

## Important caution

Do not create a universal "50% surprise" target.

Expectation depends on:
- listener history;
- genre;
- cultural exposure;
- local track context.

---

# 2. Groove

## Research

Witek et al. found an inverted-U relationship between syncopation and both pleasure and
wanting to move in funk drum-breaks: moderate syncopation performed best.

Matthews et al. found a similar inverted-U relationship for rhythmic complexity and groove;
harmonic complexity interacted with this relationship, with very high harmonic complexity
attenuating rhythmic groove effects.

Later replication work reproduced the inverted-U groove pattern in reduced stimulus sets,
while other research cautions that perceived complexity is not identical to syncopation.

## Skill translation

Added Groove Model:

- pulse clarity;
- syncopation;
- subdivision stability;
- kick/bass coordination;
- harmonic load;
- microtiming;
- body-movement affordance.

Added a complexity-budget principle:
if rhythm is already demanding, question whether harmony also needs maximal complexity.

## Caution

"Moderate syncopation" is not a universal recipe.

Genre and listener training matter.

---

# 3. Hooks and Memorability

## Research

Research on involuntary musical imagery found frequently reported earworm tunes tended to
combine relatively common global melodic contours with less common local pitch-gradient
features, while popularity/exposure also mattered.

Melodic-memory studies support motif repetition as useful for explicit recall.

A 2025 Music Perception study found excerpts were rated more memorable/salient when they
involved:

- topline material;
- choruses;
- compound hooks.

Repetition research also shows greater repetition increases familiarity/processing fluency,
though familiarity is not identical to liking or originality.

## Skill translation

Added:

- Hook / Memorability Model;
- explicit hook types;
- motif repetition + transformation;
- "strip the production away" hook test;
- common global shape + distinctive local feature heuristic.

## Caution

Do not promise "earworms" from a formula.

Exposure and individual memory matter.

---

# 4. Musical Structure

## Research

Reviews of symbolic music generation consistently identify long-term structure as a major
problem.

Work on hierarchical generation shows benefits from coarse-to-fine representations, e.g.:

```text
bar profile
→ beat profile
→ notes
```

Recent structure surveys emphasize motifs, phrases, repetition, and sub-task decomposition
where high-level form is planned separately from local content generation.

Loop-generation work likewise treats meaningful repetitive units as basic compositional
objects.

## Skill translation

Added:

```text
note
→ beat
→ bar
→ motif
→ phrase
→ section
→ song
```

The system should transform existing material before inventing endless new material.

Arrangement now explicitly tracks structural returns and what is preserved vs changed.

---

# 5. Tension and Emotion

## Research

Musical tension is multidimensional.

Studies/models associate tension changes with:
- harmony;
- dynamics;
- pitch height;
- onset density;
- tempo;
- tonal distance;
- dissonance;
- rhythmic instability.

Farbood's work on continuous tension ratings found that different features may operate over
different temporal windows, with harmony integrating over a considerably longer time window
than many performance/acoustic features.

Music-emotion research also warns against reducing emotion to one tonal variable.

## Skill translation

Listener Model tracks:
- harmonic tension;
- rhythmic tension;
- surprise;
- uncertainty;
- arousal;
- valence;
- perceived power.

The system must design curves, not static labels.

---

# 6. Timbre

## Research

Perceptual timbre is multidimensional.

Patil et al. found a five-dimensional perceptual timbre space for sustained orchestral tones
and linked perception to combined spectrotemporal patterns rather than single spectral or
temporal measures.

Important perceptual distinctions involved combinations of qualities such as:
- hard/soft;
- sharp/dull;
- frequency-energy balance;
- explosive/calm.

## Skill translation

Producer now starts from a perceptual timbre target before synthesis parameters.

Added dimensions such as:
- bright/dark;
- rough/smooth;
- stable/moving;
- tonal/noisy.

## Caution

These descriptors are not a universal complete timbre ontology.

They are a better creative interface than "pick wavetable 37."

---

# 7. Auditory Scene Analysis

## Research

Music listeners can perceptually integrate several layers or segregate them into separate
streams.

Segregation is influenced by:
- timbre;
- frequency/register;
- temporal behavior;
- spatial cues;
- selective attention.

Research using polyphonic music shows greater timbre distance can facilitate segregation.

Other work found lead vocals are unusually robust attractors of attention in popular-music
mixtures, even when low-level acoustical factors such as filtering or level are manipulated.

## Skill translation

Added an auditory-scene model.

Production/mixing must decide:

```text
should fuse
should separate
should remain background
should be discovered
```

Mixing is no longer defined as "remove every overlap."

Vocal balance is treated as an attention problem as well as a level/frequency problem.

---

# 8. Intelligent Music Production

## Research

Reviews of intelligent music production emphasize that useful systems must define:

- what the target/goal is;
- how the system interacts with audio;
- how the human interacts with the system.

Black-box optimization without controllability can be difficult to integrate creatively.

Recent automatic-mixing research also supports task decomposition.
A 2026 two-stage automatic-mixing study found explicit separation of local/intra-group and
global/inter-group processing improved quality over corresponding single-stage baselines,
while poor grouping caused downstream degradation.

## Skill translation

Mix Engineer now works in:

```text
local group balance
→ global balance
```

Music Director retains human-editable goals.

---

# 9. Cultural Calibration

## Research

Cross-cultural work shows some emotional responses to music share broad structure, while
specific associations vary with cultural exposure.

GlobalMood (2025) found a valence-arousal structure across five culturally distinct listener
groups, but substantial differences in how apparently equivalent mood words were used.

Other cross-cultural work found Western major/minor emotional associations can weaken or
change in listeners with different musical exposure.

## Skill translation

Added:
- target-listener context;
- cultural-context critic;
- warnings against universal "major = happy / minor = sad" logic.

---

# 10. Evaluation

## Research

Music-generation evaluation surveys emphasize poor correlation between many objective
metrics and human perception.

A 2025 large-scale benchmark used thousands of human pairwise comparisons to evaluate
music-generation systems and metrics.

Workflow-oriented research argues music-generation tools should be evaluated inside the
iterative production process, not only as isolated final outputs.

## Skill translation

Evaluation should include:

```text
human pairwise preference
+
diagnostic metrics
+
workflow usefulness
+
diversity across repeated generations
```

Do not use one automatic quality score.

---

# 11. Primary Sources

- Matthews et al., 2019 — groove and rhythmic/harmonic complexity
- Witek et al., 2014 — syncopation, movement, pleasure
- Gold et al., 2019 — predictability, uncertainty, musical pleasure
- Cheung et al., 2019 — uncertainty and surprise in pop harmony
- Harrison et al./related expectancy modeling work, 2023 — sensory and cognitive expectations
- Patil et al., 2012/2013 — perceptual dimensions of timbre
- Disbergen et al., 2018 — stream segregation/integration in polyphonic music
- Madsen et al., 2021 — vocal attention in popular music mixtures
- Jakubowski et al., 2017 — melodic features of earworms
- Byron, 2025 — memorability/salience of hooks
- Bhandari & Colton, 2024 — structure in symbolic music generation
- Wu et al., 2017 — hierarchical melody generation
- De Man et al., 2019 — intelligent music production overview
- Shi et al., 2026 — two-stage automatic mixing
- Lee et al., 2025 — GlobalMood
- Kader & Karmaker, 2025 — survey of music-generation evaluation
- Grötschla et al., 2025 — human preference benchmark for music generation
