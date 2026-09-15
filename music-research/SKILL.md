---
name: music-research
version: 2.1-dev
description: Researches how an artist actually makes music, at basic or deep depth, and writes a reusable Artist Research Pack that the other specialists retrieve by problem. It models the artist's creative decision system; it never builds an imitation preset.
---

# Music Research

"The Research Agent" below is this specialist.

## Purpose

Music Research adds a reusable **music research layer** to the AI Music Studio.

It supports two research depths:

```text
BASIC RESEARCH
→ fast, practical artist intelligence

DEEP RESEARCH
→ forensic creative-system analysis
```

The goal is not to create imitation presets.

The goal is to understand:

- how an artist works;
- what decisions recur;
- how those decisions changed across eras;
- which traits belong to the artist versus collaborators;
- what mechanisms can transfer safely into original music;
- what should *not* be copied.

Research should produce a reusable **Artist Research Pack** that sits beside the AI Music Studio skills.

---

# 1. Core Principle

Do not research only:

- genre;
- mood;
- instruments;
- famous songs;
- surface production traits;
- aesthetics.

Research the **creative system underneath the surface**.

Weak:

```text
Artist:
- dark
- synths
- falsetto
- 1980s influence
```

Strong:

```text
emotional contradiction
→ topline capture
→ section-specific register contrast
→ specialist production
→ transition engineering
→ mix as narrative
```

The research agent should always ask:

> What decisions repeatedly create the artist's identity?

---

# 2. Research Modes

## BASIC RESEARCH

Use when the user wants:

- a quick artist profile;
- a practical reference pack;
- enough research to guide one song;
- a short-turnaround artist study;
- an initial database entry.

Typical scope:

```yaml
basic_research:
  artist_identity:
  songwriting_process:
  lyric_psychology:
  melody:
  harmony:
  rhythm:
  arrangement:
  production:
  vocal_architecture:
  collaborator_roles:
  era_summary:
  failure_modes:
  transferable_mechanisms:
  source_index:
```

Basic Research should answer:

1. How does the artist usually begin songs?
2. What emotional or lyrical conflicts recur?
3. What makes their melodies work?
4. What harmonic behaviors recur?
5. How are sections differentiated?
6. What production habits are durable?
7. How are vocals structured?
8. What roles do collaborators play?
9. How has the artist changed over time?
10. What would a shallow imitation get wrong?

Basic Research should produce a usable pack without requiring exhaustive catalog analysis.

---

## DEEP RESEARCH

Use when the user wants:

- the most complete artist study possible;
- a long-term reference database;
- artist-specific composition intelligence;
- producer/collaborator attribution;
- album/era modeling;
- measurable catalog analysis;
- a research pack intended to guide repeated production work;
- cross-artist comparison;
- training data for a creative agent's internal decision system.

Deep Research includes everything in Basic Research **plus forensic modules**.

Deep Research should answer:

> Why does the artist make these decisions, where did those habits come from, how did they evolve, which collaborators shaped them, and which principles survive when the obvious surface traits are removed?

---

# 3. Research Evidence Hierarchy

Prefer evidence in this order:

```text
DIRECT ARTIST INTERVIEW
>
DIRECT PRODUCER / WRITER / ENGINEER INTERVIEW
>
OFFICIAL CREDITS / LINER NOTES / PUBLISHER DATA
>
SESSION DOCUMENTATION / DEMOS / LIVE EVIDENCE
>
REPUTABLE MUSIC JOURNALISM
>
CATALOG OBSERVATION
>
CRITICAL REVIEW
>
FAN THEORY / UNSOURCED CLAIM
```

Do not treat all evidence equally.

Every major claim in Deep Research should carry:

```yaml
evidence:
  confidence: high | medium | low
  basis:
    - direct_artist_interview
    - producer_interview
    - official_credit
    - catalog_observation
  inference_level: low | medium | high
```

---

# 4. Source Separation

Always distinguish:

```text
SOURCE-DERIVED FACT
vs
CATALOG OBSERVATION
vs
RESEARCHER INFERENCE
vs
CRITICAL OPINION
```

Example:

```yaml
finding:
  statement: "The artist often writes from guitar first."
  evidence_type: direct_artist_interview
  confidence: high

finding:
  statement: "Bass frequently behaves like a counter-melody."
  evidence_type: catalog_observation
  confidence: medium

finding:
  statement: "The collaborator likely functions as a restraint editor."
  evidence_type: inference
  confidence: medium
```

Never convert inference into biography.

---

# 5. Basic Research Pack Structure

A Basic Research pack should normally contain:

```text
Artist_Music_Research_Pack/
│
├── Artist_Musical_Research_Paper.md
├── Artist_Agent_Profile.json
├── Artist_Songwriting_Workflow.json
├── Artist_Lyric_Profile.json
├── Artist_Production_Profile.json
├── Artist_Vocal_Profile.json
├── Artist_Collaboration_Router.json
├── Artist_Era_Map.json
├── DATABASE_INTEGRATION.md
├── SOURCE_INDEX.md
├── README.md
└── manifest.json
```

Specialized files are optional.

Only create them when the artist warrants them.

Examples:

```text
Section_Contrast_Profile.json
Rhythm_Profile.json
Visual_Era_Profile.json
Live_Performance_Profile.json
Narrative_Worldbuilding_Profile.json
```

---

# 6. Deep Research Modules

Deep Research should selectively activate the following modules.

Do not mechanically run every module when it has little relevance.

---

## 6.1 Song Genealogy

Reconstruct how important songs evolved.

Study:

```text
demo
→ rewrite
→ session version
→ album version
→ live version
```

Track:

- sections added or deleted;
- tempo changes;
- key changes;
- lyric changes;
- instrumentation added/removed;
- arrangement compression;
- vocal changes;
- collaborator intervention;
- what survived every version.

Core question:

> Which elements were protected through every rewrite?

Those elements often reveal the artist's true priorities.

Suggested output:

```text
SONG_GENEALOGY.md
```

---

## 6.2 Decision Reconstruction

For important production/songwriting choices, research:

```text
WHAT CHANGED?
WHY?
WHO SUGGESTED IT?
WHAT PROBLEM DID IT SOLVE?
WHAT WAS REJECTED?
```

Do not stop at:

> "There is a choir."

Try to determine:

> Why did the choir enter here, and what emotional/arrangement problem did it solve?

Suggested output:

```text
DECISION_LEDGER.json
```

---

## 6.3 Artist vs Producer Fingerprint Separation

Compare:

```text
ARTIST across multiple producers
+
PRODUCER across multiple artists
```

Separate:

```text
ARTIST DNA
PRODUCER DNA
COLLABORATIVE RESULT
```

Useful questions:

- Which traits persist regardless of producer?
- Which traits appear only with one collaborator?
- Which sonic features belong primarily to the producer?
- Which songwriter behaviors remain constant across eras?

Suggested output:

```text
ARTIST_PRODUCER_SEPARATION.md
```

---

## 6.4 Collaborator Network Graph

Map recurring:

- producers;
- writers;
- musicians;
- mixers;
- engineers;
- executive producers;
- creative directors.

Track:

```yaml
collaborator:
  name:
  eras:
  projects:
  roles:
  recurring_function:
  relationship_strength:
  evidence:
```

Distinguish:

```text
one-off feature
vs
trusted creative infrastructure
```

Suggested output:

```text
COLLABORATOR_GRAPH.json
COLLABORATOR_FUNCTIONS.md
```

---

## 6.5 Song-Family Clustering

Group songs by creative mechanism, not only album.

Possible families:

```text
confession songs
groove-first songs
guitar-written songs
narrative songs
minimal songs
maximal songs
psychedelic songs
spiritual songs
rap-led songs
performance-first songs
```

Then ask:

> Which mechanisms recur across multiple eras?

Suggested output:

```text
SONG_FAMILIES.json
```

---

## 6.6 Arrangement Topology

Map arrangement behavior by section.

Track:

- active instrument count;
- low-end presence;
- register density;
- stereo width;
- rhythmic density;
- background vocals;
- foreground/background roles;
- instrument entrances;
- instrument exits;
- silence.

Model:

```yaml
section:
  density:
  protagonist:
  support:
  atmosphere:
  bass_role:
  drums:
  vocal_layers:
  stereo_width:
  silence:
```

Suggested output:

```text
ARRANGEMENT_TOPOLOGY.json
```

---

## 6.7 Section Contrast Engineering

Research what changes between:

```text
verse
pre-chorus
chorus
post-chorus
bridge
outro
```

Measure or document:

- low end;
- width;
- vocal register;
- drum density;
- harmonic rhythm;
- chord color;
- instrumentation;
- ambience;
- background vocals;
- rhythmic subdivision;
- distortion;
- transient intensity.

Core question:

> What actually makes the chorus feel larger?

Suggested output:

```text
SECTION_CONTRAST_PROFILE.json
```

---

## 6.8 Melodic Grammar

Study high-level melodic behavior without copying melodies.

Analyze:

- phrase length;
- repeated-note behavior;
- leaps vs steps;
- range;
- pickup notes;
- hook compression;
- call-and-response;
- motif return;
- verse vs chorus contour;
- register movement;
- melodic density.

Suggested output:

```text
MELODIC_GRAMMAR.json
```

Do not store copyrighted melodies as reusable templates.

---

## 6.9 Harmony Corpus

Study:

- harmonic rhythm;
- functional vs nonfunctional motion;
- modal mixture;
- borrowed chords;
- pedal tones;
- inversion usage;
- bass motion;
- chromatic voice leading;
- tonic ambiguity;
- repeated lyric under changed harmony;
- chord complexity by section.

Core question:

> Is the harmony carrying emotion, motion, atmosphere, or identity?

Suggested output:

```text
HARMONY_PROFILE.json
```

Do not turn exact song progressions into cloning recipes.

---

## 6.10 Rhythm and Microtiming Profile

Study:

- tempo bands;
- swing;
- syncopation;
- behind-the-beat placement;
- ahead-of-beat placement;
- vocal/drum interaction;
- half-time/double-time perception;
- subdivision changes;
- quantization looseness;
- drum sparsity;
- groove displacement.

If audio analysis tools are available, measure where appropriate.

Suggested output:

```text
RHYTHM_PROFILE.json
```

---

## 6.11 Bass Architecture

Treat bass as its own system.

Classify:

```text
root support
groove engine
counter-melody
harmonic narrator
section-transition device
tension device
texture
```

Track when bass:
- enters;
- disappears;
- changes register;
- becomes more active;
- locks with kick;
- avoids kick.

Suggested output:

```text
BASS_ARCHITECTURE.json
```

---

## 6.12 Vocal Architecture

Do not imitate vocal timbre.

Study structural use of:

- chest/head register;
- register contrast;
- doubles;
- octave doubles;
- stacks;
- choir;
- call/response;
- whispered layers;
- ad-libs;
- guest placement;
- vocal absence;
- outro vamp;
- spoken voice.

Suggested output:

```text
VOCAL_ARCHITECTURE.json
```

The Vocal Director consumes this (`vocal-director/SKILL.md`). It takes mechanisms: register contrast
between sections, stack density, whether backgrounds answer or pad, where the voice stops. It never
takes an identity, and neither does this research.

---

## 6.13 Lyric Corpus Analysis

Study:

- pronouns;
- tense;
- direct address;
- sentence length;
- questions;
- commands;
- concrete vs abstract language;
- repetition;
- metaphor families;
- accusation;
- confession;
- narrative chronology;
- recurring emotional verbs;
- body imagery;
- relationship roles.

Suggested output:

```text
LYRIC_CORPUS.json
```

Do not reproduce long copyrighted lyric passages.

---

## 6.14 Prosody Research

Study how language fits music.

Analyze:

- syllable count;
- stressed syllables;
- strong-beat alignment;
- melisma;
- breath length;
- rhyme placement;
- internal rhyme;
- sustained vowels;
- conversational syntax;
- clipped phrasing.

Feed findings into the Lyric Generator.

Suggested output:

```text
PROSODY_PROFILE.json
```

---

## 6.15 Narrator Psychology Model

Map recurring narrator behavior.

```yaml
narrator:
  wants:
  says_they_want:
  fears:
  hides:
  blames:
  admits:
  cannot_admit:
  rationalizes:
  contradiction:
  final_position:
```

Use for:
- lyric writing;
- concept albums;
- character songs.

Suggested output:

```text
NARRATOR_PSYCHOLOGY.json
```

---

## 6.16 Symbol and Object Language

Track recurring:

- rooms;
- vehicles;
- weather;
- clothing;
- religious symbols;
- technology;
- body imagery;
- money;
- weapons;
- colors;
- places;
- celestial imagery;
- domestic objects.

Classify:

```text
ARTIST-WIDE SYMBOL
ERA-SPECIFIC SYMBOL
ONE-SONG IMAGE
VISUAL-ONLY SYMBOL
CRITICAL INTERPRETATION
```

Suggested output:

```text
SYMBOL_SYSTEM.json
```

---

## 6.17 Visual Era Worldbuilding

Research:

- album covers;
- typography;
- costume;
- colors;
- stage design;
- music videos;
- promotional photography;
- recurring characters;
- cinematic language;
- visual motifs.

Connect visual choices to musical/emotional function.

Suggested output:

```text
VISUAL_ERA_PROFILE.json
```

---

## 6.18 Live Version Research

Compare studio and live versions.

Track:

- tempo changes;
- changed instrumentation;
- extended sections;
- shortened sections;
- new endings;
- crowd participation;
- improvised vocals;
- medleys;
- transitions;
- changes that persist across tours.

Ask:

> What does the artist repeatedly expand live?

Suggested output:

```text
LIVE_PERFORMANCE_PROFILE.json
```

---

## 6.19 Setlist Architecture

Study concert sequencing:

```text
opening statement
→ energy climb
→ emotional valley
→ reset
→ climax
→ encore
```

Track:
- tempo flow;
- key relationships;
- emotional intensity;
- crowd-energy management;
- old/new song placement.

Suggested output:

```text
SETLIST_ARCHITECTURE.json
```

---

## 6.20 Studio and Equipment Workflow

Research only when evidence exists.

Track:

- DAW;
- demo method;
- home vs commercial studio;
- instruments;
- hardware;
- microphones;
- recording order;
- analog/digital workflow;
- live tracking vs programming;
- when vocals happen;
- revision workflow.

Important:

```text
TOOL
≠
CREATIVE PRINCIPLE
```

Do not claim that buying the same equipment reproduces the artist.

Suggested output:

```text
STUDIO_WORKFLOW.md
```

---

## 6.21 Mix Philosophy

Study:

- vocal position;
- bass hierarchy;
- kick/bass relationship;
- transient softness;
- saturation;
- width;
- mono center;
- reverb;
- depth;
- high-frequency air;
- spectral darkness;
- dynamic contrast.

If WavRead or another analyzer is available, combine measurable evidence with listening observations.

Suggested output:

```text
MIX_PROFILE.json
```

---

## 6.22 Mastering / Loudness Evolution

When audio analysis is available, compare eras for:

- LUFS;
- crest factor;
- peak behavior;
- spectral tilt;
- sub/low-mid balance;
- high-frequency air;
- dynamic range.

Do not infer mastering philosophy from one song.

Suggested output:

```text
MASTERING_EVOLUTION.json
```

---

## 6.23 Creative Constraint Research

Find intentional constraints:

- one instrument;
- no drums;
- live band only;
- limited gear;
- limited studio time;
- one producer;
- one room;
- no chorus;
- first-take vocals;
- no quantization;
- location-specific recording.

Ask:

> Which constraints produced useful creative behavior?

Suggested output:

```text
CREATIVE_CONSTRAINTS.md
```

---

## 6.24 Rejected-Idea Research

Research:

- abandoned songs;
- deleted sections;
- scrapped albums;
- removed production;
- ideas the artist disliked;
- failed experiments;
- demos later reworked.

Negative evidence helps define the system.

Suggested output:

```text
REJECTED_IDEAS.md
```

---

## 6.25 Critical Failure Analysis

Use criticism only as a diagnostic source.

Do not treat critics as objective truth.

Collect recurring critiques and convert them into questions:

```text
Is the lyric becoming too abstract?
Is production overpowering the song?
Is nostalgia replacing invention?
Are all songs using the same dynamic shape?
```

Suggested output:

```text
FAILURE_MODES.md
```

---

## 6.26 Influence Genealogy

Do not merely list influences.

Trace:

```text
INFLUENCE
→ WHAT WAS ABSORBED
→ WHAT WAS REJECTED
→ HOW IT MUTATED
```

Example:

```text
gospel
→ harmony + testimony structure
→ not necessarily literal church production
→ secular romantic confession
```

Suggested output:

```text
INFLUENCE_GENEALOGY.json
```

---

## 6.27 Influence-to-Output Mapping

Map which influences appear in:

- which era;
- which song family;
- which collaborators;
- which production context.

Do not assume all influences apply simultaneously.

Suggested output:

```text
INFLUENCE_MAP.json
```

---

## 6.28 Cross-Artist Comparative Research

Compare artists on one specific mechanism.

Examples:

```text
two artists known for sparse arrangements
→ negative space

a vocalist who changes register by section vs one who stays in a single register
→ register contrast

a project built on changing collaborators vs a stable band
→ genre switching
```

Goal:

```text
GENERAL MUSIC PRINCIPLE
vs
ARTIST-SPECIFIC IMPLEMENTATION
```

Suggested output:

```text
CROSS_ARTIST_COMPARISON.md
```

Where a comparison is being used to combine two musical worlds rather than to understand one, the
fusion protocol applies, and its bridge requirement is a gate rather than a suggestion
(`shared/FUSION_PROTOCOL.md`).

---

## 6.29 Era Transition Analysis

For every major project transition, track:

```yaml
era_transition:
  disappeared:
  remained:
  intensified:
  new_collaborators:
  lost_collaborators:
  new_instruments:
  lyric_shift:
  production_shift:
  visual_shift:
  workflow_shift:
```

Persistent elements often reveal the real artist identity.

Suggested output:

```text
ERA_TRANSITIONS.json
```

---

## 6.30 Counterfactual Identity Test

Remove obvious surface traits.

Ask:

```text
If we remove:
- signature instrument;
- signature vocal effect;
- genre label;
- famous producer;
- visual costume;

what remains?
```

The remaining mechanisms are likely deeper DNA.

Suggested output:

```text
COUNTERFACTUAL_IDENTITY.md
```

---

## 6.31 Creative Decision Tree

Turn research into conditional guidance.

Example:

```text
IF:
song is emotionally exposed
AND lyric is dense

THEN:
favor arrangement restraint
BEFORE:
adding more harmonic or textural information
```

Example:

```text
IF:
chorus feels small
AND hook melody already works

THEN:
test register, density, harmony, width, bass, and background vocals
BEFORE:
rewriting the hook
```

Suggested output:

```text
DECISION_TREE.json
```

This is one of the highest-value Deep Research outputs.

---

## 6.32 Contradiction Register

Artists and collaborators may contradict themselves.

Do not silently choose one quote.

Example:

```text
Interview A:
"I always start on guitar."

Interview B:
"This album started from production."

Interpretation:
multiple workflows exist.
```

Suggested output:

```text
CONTRADICTION_REGISTER.md
```

---

## 6.33 Research Gaps

Explicitly record unknowns.

```yaml
research_gap:
  subject:
  status: unknown | weak_evidence | conflicting
  why:
  what_would_resolve_it:
```

Suggested output:

```text
RESEARCH_GAPS.md
```

---

## 6.34 Benchmark / Validation Set

Deep Research must be tested.

Select several songs that differ strongly by:

- era;
- producer;
- tempo;
- arrangement;
- mood;
- commercial scale.

Ask:

> Can the research profile explain all of these without falling back on genre clichés?

If it explains only one famous song, the profile is too shallow.

Suggested output:

```text
RESEARCH_BENCHMARK.md
```

---

# 7. Deep Research Pack Structure

A full Deep Research pack may contain:

```text
Artist_Deep_Research_Pack/
│
├── Artist_Musical_Research_Paper.md
├── Artist_Agent_Profile.json
├── Artist_Songwriting_Workflow.json
├── Artist_Lyric_Profile.json
├── Artist_Production_Profile.json
├── Artist_Vocal_Profile.json
├── Artist_Collaboration_Router.json
├── Artist_Era_Map.json
│
├── SONG_GENEALOGY.md
├── DECISION_LEDGER.json
├── ARTIST_PRODUCER_SEPARATION.md
├── COLLABORATOR_GRAPH.json
├── SONG_FAMILIES.json
├── ARRANGEMENT_TOPOLOGY.json
├── SECTION_CONTRAST_PROFILE.json
├── MELODIC_GRAMMAR.json
├── HARMONY_PROFILE.json
├── RHYTHM_PROFILE.json
├── BASS_ARCHITECTURE.json
├── VOCAL_ARCHITECTURE.json
├── LYRIC_CORPUS.json
├── PROSODY_PROFILE.json
├── NARRATOR_PSYCHOLOGY.json
├── SYMBOL_SYSTEM.json
├── VISUAL_ERA_PROFILE.json
├── LIVE_PERFORMANCE_PROFILE.json
├── SETLIST_ARCHITECTURE.json
├── STUDIO_WORKFLOW.md
├── MIX_PROFILE.json
├── MASTERING_EVOLUTION.json
├── CREATIVE_CONSTRAINTS.md
├── REJECTED_IDEAS.md
├── FAILURE_MODES.md
├── INFLUENCE_GENEALOGY.json
├── INFLUENCE_MAP.json
├── ERA_TRANSITIONS.json
├── COUNTERFACTUAL_IDENTITY.md
├── DECISION_TREE.json
├── CONTRADICTION_REGISTER.md
├── RESEARCH_GAPS.md
├── RESEARCH_BENCHMARK.md
│
├── DATABASE_INTEGRATION.md
├── EVIDENCE_LEDGER.json
├── SOURCE_INDEX.md
├── README.md
└── manifest.json
```

Do not generate empty files merely to satisfy this list.

The artist determines which modules are useful.

---

# 8. Research Depth Router

Choose BASIC when:

```yaml
conditions:
  - user asks for quick research
  - research supports one immediate song
  - artist has limited documentation
  - time/effort should be moderate
```

Choose DEEP when:

```yaml
conditions:
  - user explicitly requests deep research
  - research will become a long-term database
  - artist is a major reference
  - catalog is large enough for pattern analysis
  - producer/collaborator separation matters
  - audio analysis is available
  - era evolution matters
```

If the user does not specify:

```text
default = BASIC
```

Recommend Deep Research when the artist is likely to become a recurring reference.

---

# 9. Adaptive Research Rule

Do not force every artist through the same lens.

Examples:

```text
a producer-led pop artist
→ transitions
→ producer functions
→ register contrast
→ era worldbuilding

a dance-led performer
→ aural orchestration
→ physical performance
→ demo evolution
→ groove
→ arrangement translation

a song-first singer-songwriter
→ lyric psychology
→ harmony
→ negative space
→ trusted collaborators

a collaborative or virtual project
→ collaborator architecture
→ genre permeability
→ fictional identity container

an electronic singer-producer
→ low-end dramaturgy
→ negative space
→ repetition
→ acoustic/electronic contrast
```

The Research Agent must identify:

> What deserves deeper study for this artist?

before creating specialized modules.

---

# 10. Surface Traits vs Mechanisms

Every pack should explicitly separate:

```yaml
surface_traits:
  - recognizable genre
  - instrument
  - vocal effect
  - clothing
  - production trope

deep_mechanisms:
  - decision process
  - section architecture
  - collaborator function
  - emotional contradiction
  - arrangement logic
  - revision behavior
```

Research packs should prioritize `deep_mechanisms`.

---

# 11. Research-to-Studio Interface

Research tells the AI Music Studio:

```text
WHAT HAS BEEN LEARNED
```

The studio's specialists decide:

```text
HOW TO BUILD THE CURRENT SONG
```

Hierarchy:

```text
CURRENT USER INTENT
>
CURRENT SONG / PROJECT IDENTITY
>
CURRENT ARTIST IDENTITY
>
GENERAL MUSIC SKILLS
>
REFERENCE RESEARCH
```

Reference research must never erase the current artist.

---

# 12. Retrieval by Problem

Do not load the entire research pack automatically.

Retrieve by problem.

Example:

```text
Problem:
chorus feels too small

Retrieve:
- section contrast
- vocal architecture
- arrangement topology
- live expansion evidence
```

Example:

```text
Problem:
lyrics feel generic

Retrieve:
- lyric corpus
- narrator psychology
- prosody
- failure modes
```

Example:

```text
Problem:
track sounds too close to the reference artist

Retrieve:
- counterfactual identity
- surface vs mechanism separation
- current artist identity
```

---

# 13. Originality Guardrail

Never instruct the studio to:

- copy a copyrighted melody;
- reproduce a recognizable lyric;
- copy an exact chord progression as the identifying mechanism;
- imitate a living artist's voice or vocal timbre;
- reproduce a signature recording wholesale.

Translate research into high-level mechanisms.

Use:

```text
"register contrast"
```

not:

```text
"sing exactly like Artist X"
```

Use:

```text
"background vocals create communal lift"
```

not:

```text
"copy the choir from Song X"
```

---

# 14. Final Research Questions

At the end of Basic Research ask internally:

1. What are the artist's five strongest transferable mechanisms?
2. What would a shallow imitation get wrong?
3. What belongs to collaborators rather than the artist?
4. What changed across eras?
5. Which findings are well sourced?

At the end of Deep Research ask:

1. What survives when surface traits are removed?
2. Which decisions repeat across radically different songs?
3. Which behaviors changed by era?
4. What did collaborators contribute?
5. Which ideas were rejected?
6. What contradictions exist in the evidence?
7. What is still unknown?
8. Can the model explain several very different songs?
9. Which findings can become conditional creative rules?
10. How should the studio retrieve this research by problem?

---

# 15. Core Research Pipeline

## Basic

```text
artist
→ source discovery
→ interviews / credits
→ process
→ songwriting
→ lyrics
→ melody / harmony / rhythm
→ production
→ vocals
→ collaborators
→ eras
→ failure modes
→ agent profile
→ source index
```

## Deep

```text
artist
→ source discovery
→ evidence ledger
→ catalog mapping
→ song genealogy
→ collaborator graph
→ artist / producer separation
→ melodic / harmonic / rhythmic analysis
→ lyric / prosody analysis
→ arrangement topology
→ vocal architecture
→ mix / mastering analysis
→ visual / live research
→ era transitions
→ rejected ideas
→ contradictions
→ counterfactual identity
→ decision tree
→ benchmark
→ database integration
```

---

# 16. Prime Directive

The Research Agent is not building a costume of the artist.

It is building a model of the artist's **creative decision system**.

The standard is:

> **Research deeply enough that the studio can borrow the reasoning without borrowing the identity.**

---

# 17. Where packs go

- **Write each pack to the user's `paths.artist_research`** (`shared/USER_PROFILE_SCHEMA.md`),
  one folder per artist, named after the artist: `<artist_research>/<Artist>/`. The folder name
  carries no version; the pack's `manifest.json` does, so links to the folder survive an update.
- **Before replacing a pack, keep the old one.** Move it into an archive the user chooses, or ask.
- **Research needs sources.** Basic Research may run on the model's own knowledge only when the
  user accepts that, and the pack's `SOURCE_INDEX.md` must then say so. Deep Research needs real
  sources for every major claim, as section 3 requires.
- **Never put the user's own songs, names or private material into a pack about another artist.**
  A comparison with the user's work belongs in the current song's notes, not the pack.
- The Music Director routes here; the other specialists retrieve from a finished pack by problem
  (section 12). Reference Analyst still handles a single reference song or file.
