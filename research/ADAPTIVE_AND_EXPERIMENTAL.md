# Research: Adaptive, Generative and Experimental Music, Seeds and Fusion

## Purpose

The research behind `shared/ADAPTIVE_MUSIC.md`, `shared/EXPERIMENTAL_SYSTEMS.md`,
`shared/SEED_TRANSLATION.md` and `shared/FUSION_PROTOCOL.md`.

## Evidence note

The adaptive-middleware and game-composer sections were confirmed from documentation and talk
descriptions. The generative, sound-based, improvisation, seed and fusion sections were written from
bibliographic knowledge with the sources unreachable, and are marked as such in this page. Quotations
are paraphrase until the texts are opened.

---

# 1. Adaptive music: the primitives, stated tool-neutrally

## Research

From interactive-audio middleware documentation:

- a musical segment has a **pre-entry** region, an **entry cue**, an **exit cue** and a **post-exit**
  region, and the post-exit of one segment may sound over the pre-entry of the next. This is how a
  reverb tail or a cymbal survives a transition;
- transitions resolve at a **sync point**, chosen from immediate, the next grid division, the next
  bar, the next beat, the next cue, or the exit cue, with a matching rule for where the destination
  starts;
- a **stinger** is a brief musical phrase superimposed over whatever is currently playing;
- a **parameter** binds a game value to a property through a curve, in real time;
- one system additionally offers a transition timeline: a short bridge inserted between leaving and
  arriving, able to carry its own content, automation and crossfades, and transitions can be
  quantised to the musical pulse.

## Skill translation

`shared/ADAPTIVE_MUSIC.md` uses neutral terms — segment, sync point, tail overlap, layer mask,
parameter curve — and carries a mapping table to the common middleware vocabularies, marked to verify
against current documentation. The studio plans music, not one vendor's project file.

The **transition latency budget** is the quantity that actually constrains composition:

```text
latency = time until the next permitted sync point + engine look-ahead
```

Combat needs a beat, an area change tolerates a bar, an ending can wait for the exit cue. Choosing the
sync granularity is a musical decision with a gameplay consequence, so it is stated per trigger rather
than set once for the project.

---

# 2. What game composers say they actually do

## Research

Described in conference talks and interviews:

- on one large action title, the composer avoided the term dynamic music in favour of a description
  where the player should not feel in control; every piece has an authored ending while its middle is
  variable, and a neutral "glue" cue can transition between any two pieces;
- on a puzzle title, an orchestra was recorded in phrases, sub-phrases and individual notes, and about
  half the production happened inside the middleware, with real-time reverb used for cohesion;
- on a creature-building game, the team worked with a generative-music composer and described the task
  as "composing in probabilities", aiming at music people could hear for a long time;
- on an exploration game, a band's recorded material was recombined algorithmically into soundscapes;
  the system does not synthesise, it re-composes recorded variations;
- narrative titles bind a motif to a character or a mechanic and transform instrumentation, harmony
  and intensity while the identity survives.

## Skill translation

Four schema fields come straight from this:

```yaml
motif_invariants:      # what must survive every variation
glue_state:            # a neutral state reachable from everywhere
authored_endings:      # one per loopable middle
failure_states:        # resolve, suspend or drop to glue - never a hard cut by default
```

Long-exposure material also gets no-immediate-repeat rules, because the thing that makes endless
music tolerable is the absence of a strong periodic closure the listener can count.

---

# 3. Generative and process music are two different things

## Research (sources not opened; bibliography verified)

- Reich, "Music as a Gradual Process" (1968): the wish to hear the process happening in the sounding
  music; once the process is set up it runs by itself. *Piano Phase*, *Clapping Music*, the tape
  pieces.
- Eno, "Generative Music" (1996) and *Discreet Music*: a system of parts of unequal length, designed
  and then left running; the wind-chime analogy, where you design the chimes and how they hang.
- Riley, *In C* (1964): fifty-three patterns, each player advancing independently but staying close to
  the group, over a shared pulse.
- Cage: chance operations used to *compose* a determinate score, distinct from indeterminacy in
  performance. Cardew's *Treatise*: a graphic score whose performers agree a reading in advance.
  Xenakis: probability distributions governing masses of events.
- Lucier, *I am sitting in a room*: a process whose result is the room.
- Nyman, *Experimental Music: Cage and Beyond* (1974): experimental action as action whose outcome is
  not foreseen.

## Skill translation

```text
process           a deterministic rule that the listener is meant to hear running
generative        rules bounding a space; each realisation differs
```

A piece is represented as **seed + rule set + stopping condition + what the listener should perceive**.
"Correct" means different things in the two families: the rule is audible, or the space was explored.

The constraint-to-freedom ratio is what keeps identity: a fixed pitch set and pulse in *In C*, fixed
melodic material in *Discreet Music*, a fixed text and room in Lucier. `EXPERIMENTAL_SYSTEMS.md`
therefore flags a design with fewer than two fixed elements as likely to lose identity.

---

# 4. Sound-based composition: every technique answers a question

Each tradition is in the guide with its **purpose**, because without one these become novelty buttons:

| Tradition | What it makes audible |
|---|---|
| musique concrète, reduced listening | the sound itself, detached from its cause |
| spectromorphology | shape and motion, where pitch-and-rhythm vocabulary fails |
| spectral thinking | harmony derived from an acoustic model; time scaled to perception |
| granular composition | the continuum between rhythm and timbre |
| prepared instruments | a whole ensemble inside one body; estrangement of the familiar |
| noise | negation, saturation, the ethics of listening |
| drone | tuning and duration, heard rather than passed through |
| soundscape and found sound | place, and ecological attention |

The rule this generates: **any experimental-texture request must answer "what is this making audible?"
in one sentence.** If it cannot, it is decoration, and the studio says so rather than supplying it.

---

# 5. Rule-based improvisation

Game pieces, language-type systems, text scores and cueing scores share four properties that make a
rule set musically productive rather than merely constraining:

1. the rules govern **relationships and attention**, not notes;
2. there is a shared, legible vocabulary of signals or actions;
3. the rules set a state of mind as well as a procedure;
4. there are few enough of them to hold while playing.

Failure modes, named in the guide: vagueness, deadlock, dominance by one player, sterility.

---

# 6. Translating non-musical seeds

## Research

- Cross-modal correspondence research documents statistical, structural and semantically mediated
  mappings: pitch with elevation and with size, loudness with brightness, angularity with sharpness.
  These are **weak average tendencies**, with asymmetries: descent maps to spatial descent more
  strongly than ascent maps upward.
- Synaesthesia proper is idiosyncratic and consciously experienced, and is not what these
  correspondences are.
- Film-composer practice: short flexible phrases rather than long melodies against picture;
  orchestration as dramaturgy; one theme re-harmonised across a life; music saying what a character
  does not.

## Skill translation

The default cross-modal mappings are exactly the clichés. `SEED_TRANSLATION.md` therefore requires at
least five translations drawn from **different channels**:

```text
a  cross-modal default          high, bright, small, fast
b  motion                        approach, recession, gait, acceleration
c  structural                    contradiction as incompatible key areas or forms
d  behavioural                   what the subject does, as metre and articulation
e  procedural                    the story's process as the music's process
f  material                      the object's physics as the instrument's physics
g  negation                      what is absent, unsaid, or refused
```

A first translation that is purely channel (a) is rejected as a candidate and kept only as a layer.
The chosen mapping is then held as an invariant, which is what "commit to it" means. Each mapping is
tagged empirical, craft or metaphor.

---

# 7. Fusion needs a bridge

## Research

Genre is a social category maintained by communities, not a property of the audio. The critical
literature on hybridity documents the failure case precisely: a recording of people who are not
partners is sampled or imitated, the sound is detached from the people, and the revenue and the
attribution go elsewhere.

The successful cases documented in practitioner accounts share a structure. There is a **bridge**: an
element both sides already own — a rhythmic cycle, a mode, an instrument's physics, a shared history,
or an existing audience that already dances to both — and a person with standing in both traditions
through training, residence, collaboration or invitation.

## Skill translation

`FUSION_PROTOCOL.md` gates on this:

1. **name the bridge before writing.** If there is no bridge, stop or find a partner;
2. assign carrier roles so that one genre does not silently supply rhythm, harmony, form and timbre;
3. run the provenance check: are source-tradition musicians credited, consulted, paid? Is any sampled
   recording of people who are not party to this?
4. run the strip test: remove each source's contribution in turn. If the piece survives intact without
   one of them, that one was decoration;
5. decline "in the style of" for sacred, ceremonial or community-restricted repertoire.

---

# 8. Cautions

- Middleware names are product facts. The behaviour is the music; the vendor's noun is not.
- Latency budgets are per project. A bar is nothing in exploration and unusable in a rhythm game.
- "Composing in probabilities" does not mean randomness improves music. In every documented case the
  material was composed and the constraints were tight.
- Process music's virtue is that the rule is audible. That does not generalise to music that needs a
  shaped arc.
- Cross-modal correspondences license defaults, not rules, and the defaults are the clichés.
- An agent is especially exposed on appropriation, because it can produce a tradition's surface
  markers with no partner in the room. Hence the bridge gate and the provenance check.

---

# 9. Sources

- Interactive-audio middleware documentation for interactive music hierarchies, transitions, stingers
  and real-time parameters
- Conference talks and interviews by game composers on adaptive scores, recorded in the studio's notes
  as described rather than quoted
- Collins, *Game Sound*, 2008; Sweet, *Writing Interactive Music for Video Games*, 2014; Phillips,
  *A Composer's Guide to Game Music*, 2014
- Reich, 1968; Eno, 1996; Riley, 1964; Cage; Cardew, 1963–67; Xenakis; Lucier, 1969; Nyman, 1974
- Schaeffer and Chion on the sound object; Smalley, 1997, on spectromorphology; Grisey and Murail on
  spectral music; Roads, *Microsound*, 2001; Schafer, 1977, and Westerkamp on soundscape
- Zorn, Braxton, Stockhausen, Oliveros, Wolff — rule-based and text-score improvisation
- Spence, 2011, on cross-modal correspondences; Eitan & Granot, 2006, on music and motion
- Holt, 2007; Brackett, 2016 on genre; Feld, 1996; Born & Hesmondhalgh, 2000 on appropriation
