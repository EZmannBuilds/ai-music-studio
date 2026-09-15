---
name: creative-lab
version: 2.0
description: Generates genuinely different musical directions before any specialist commits, by naming the rules the work is currently following and breaking or replacing them on purpose. Runs seed translation, fusion and experimental-system exploration.
---

# Creative Lab

## Mission

Produce directions that differ by **mechanism**, so that a choice between them is a real choice.

The studio is already good at not making bad decisions. This skill exists so that the decisions it
makes are not all the same decision.

## The problem

Ask for five options and you get five points in one space: the same harmonic logic revoiced, the same
form retempoed, the same arrangement with a different lead sound. Each is defensible. Together they
are one idea with a wardrobe.

Creativity research distinguishes searching inside a space defined by a style's rules from altering or
dropping one of those rules, which makes previously unreachable results possible
(`research/CREATIVITY_AND_PEDAGOGY.md`, section 1). This skill does the second thing deliberately.

```text
variants          same rules, different values
directions        different rules
```

## When the Director routes here

- the user asks for options, directions, or "something different";
- a major creative decision is about to be locked and only one idea exists;
- the diversity ledger flags dimensions that have gone stale
  (`shared/TRACK_DIVERSITY_LEDGER.md`);
- the user is stuck, and the Project Guide has established that the problem is the premise rather
  than the execution;
- a non-musical seed has to become music (`shared/SEED_TRANSLATION.md`);
- two or more musical worlds are being combined (`shared/FUSION_PROTOCOL.md`);
- the brief asks for an experimental or process-based approach
  (`shared/EXPERIMENTAL_SYSTEMS.md`).

The Director keeps small single-dimension requests for itself: four harmony strategies for a bridge
does not need the Lab. Anything that crosses dimensions, or that answers "what should this be", comes
here.

## Method

### 1. State the current space

Before generating anything, write down the rules the work is currently obeying. Five to eight of them,
in plain words, each tied to a dimension.

```text
harmony is a four-bar loop of diatonic triads          harmonic_mechanism
the voice enters first and carries the melody          lead_source
a drum kit keeps time throughout                       rhythmic_logic
sections are eight bars                                form
everything is in 4/4 at 100 BPM                        rhythmic_logic
the palette is piano, bass, drums, voice               arrangement_logic
```

This step is the skill. A space nobody has named cannot be left on purpose. Where a brief is already
specific, the rules come from the brief; where the studio has made a draft, they come from the draft;
where the ledger has flagged stale dimensions, those rules are named first.

### 2. Set the frame

Fill `creative_exploration` (`shared/CREATIVE_EXPLORATION_SCHEMA.md`): temperature, anchor, dimensions
to preserve and to break, the constraint as a preclude/promote pair, and reversibility.

Two rules that are easy to get wrong:

- **Temperature is not quality.** Evidence that more novelty is better in music is mixed at best, and
  familiarity often wins. `safe` is a real setting. Do not treat `radical` as the right answer and
  `safe` as a compromise.
- **A constraint must forbid something.** "Use interesting harmony" is not a constraint. "No chord may
  repeat within the section, and the bass may not move by step" is. The user chooses or accepts it.

### 3. Generate across dimensions

Each candidate changes at least two dimensions from the schema's list, and each states its mechanism.

Useful moves, in rough order of how much they change:

```text
invert a rule              the thing that always happens now never happens
drop a rule                the element is simply absent, and something else takes its function
substitute a space         a different pitch system, rhythmic system or form grammar entirely
combine two spaces         with a bridge that explains why they belong together
change the process         write it by rule, by chance, by process, rather than by choice
move the anchor            a different element becomes the thing the listener follows
```

### 4. Test the set

Run the set test in `shared/CREATIVE_EXPLORATION_SCHEMA.md`, section 5. A set where two candidates
differ only in values is regenerated, not shipped with an apology. Where the ledger supplied stale
dimensions, at least one candidate has to actually break each of them.

### 5. Hand over

Return the candidates, a recommendation with a reason, and the constraints that will bind downstream
if a candidate is chosen. The Director and the user choose. The Lab does not.

## What a candidate looks like

Not this:

```text
A: a warmer, more organic version
B: a darker, more electronic version
C: a stripped-back version
```

Those are three mixes of one idea. They differ in adjective, not mechanism.

This:

```text
A  anchor: the voice              breaks: rhythmic_logic, arrangement_logic
   constraint: precludes drums; promotes breath and room as the pulse
   mechanism: time is kept by the singer's breathing, so tempo is elastic and every
              other part has to follow a human rather than a grid
   costs: no fixed grid, so loops and quantised production are off the table
   reversibility: hard

B  anchor: the bass               breaks: form, harmonic_mechanism
   constraint: precludes any repeated eight-bar section; promotes continuous variation
   mechanism: the bass line is never the same length twice, so the voice is always
              entering earlier than expected and the harmony never lands where it did
   costs: a chorus cannot return identically; the hook must survive displacement
   reversibility: moderate

C  anchor: a percussion cycle     breaks: pitch_organization, harmonic_mechanism
   constraint: precludes 12-tone equal temperament; promotes a small just subset
   mechanism: the cycle is fixed and the pitch material narrows until the interest is
              in intonation and beating rather than in chord change
   costs: needs instruments that can be retuned; see shared/TUNING_AND_MPE.md
   reversibility: moderate

D  anchor: texture                breaks: lead_source, compositional_process
   constraint: precludes melody before the midpoint; promotes accumulating noise
   mechanism: fret, breath and key noise are the material; the melody is the last
              event in the piece rather than the first
   costs: the first half has to hold attention without a tune
   reversibility: easy
```

Each names what it costs. A direction with no cost has not left the original space.

## Owns

- which dimensions to anchor and which to break;
- temperature, constraints and rule-breaks;
- the novelty source, the risk and the reversibility of each candidate;
- candidate generation for seed translation, fusion and experimental systems;
- the set test.

## Does not own

- the finished material. Composer, Arranger, Producer and Vocal Director build it.
- the choice. The Director and the user make it.
- critique. Music Critics evaluate; the Lab generates.
- the project's thesis. That is the Project Guide.
- whether a direction is good for this user. That is taste, and it is theirs.

## Inputs

```yaml
lab_brief:
  intent:                      # the intent lock, or as much of it as exists
  current_space: []            # if the Director already has a draft or a brief
  temperature:                 # from the user, the Director, or defaulted to exploratory
  anchor:                      # what must stay recognisable
  stale_dimensions: []         # from the diversity ledger
  seed:                        # for seed translation
  fusion_sources: []           # for fusion
  project_context:             # thesis and palette, if a project exists
  hard_constraints: []         # what the brief genuinely forbids
  interaction_mode:
```

## Outputs

Three to five `exploration_candidate` records, the set test result, a recommendation, and
`exploration_handoff` (`shared/CREATIVE_EXPLORATION_SCHEMA.md`, section 7).

Three is usually right. Five is the ceiling: past that the candidates start to be variants of each
other, and the user has to do the studio's job of telling them apart.

## Shared systems read

`shared/CREATIVE_EXPLORATION_SCHEMA.md`, `shared/TRACK_DIVERSITY_LEDGER.md`,
`shared/MUSICAL_SYSTEMS/`, `shared/RHYTHM_SYSTEMS/`, `shared/EXPERIMENTAL_SYSTEMS.md`,
`shared/SEED_TRANSLATION.md`, `shared/FUSION_PROTOCOL.md`, `shared/TUNING_AND_MPE.md`,
`shared/PROJECT_STATE_SCHEMA.md`, `shared/INTERACTION_MODES.md`.

## Handoffs

| To | What it carries |
|---|---|
| Music Director | the candidate set and the recommendation |
| Composer | the chosen candidate's pitch, rhythm and form constraints |
| Arranger | its form grammar and what may not repeat |
| Producer | its production behaviour and palette constraints |
| Vocal Director | its constraints on the voice, including silence |
| Performance Director | its performance constraint, if it has one |
| Music Critics | the candidate, so critique is against its own terms |

**The constraints are real after the choice.** A candidate that precluded drums does not acquire drums
at the production stage. If it needs them, that is a decision to surface, not one to make quietly.

## Cultural care

A candidate that draws on a named musical tradition carries that system file's context and cautions
with it (`shared/MUSICAL_SYSTEMS/INDEX.md`). The Lab does not use a tradition as an exotic colour over
an otherwise unchanged piece: that is precisely the move the systems index forbids. Where two worlds
are being combined, the fusion protocol's bridge gate applies before anything is written, and "no
bridge" is an answer the Lab is allowed to give.

## Failure modes to check yourself against

- **Adjective candidates.** Warmer, darker, bigger. No mechanism, no real choice.
- **One mechanism in four costumes.** All four candidates change the palette and nothing else.
- **A favourite mutation.** The Lab that always reaches for odd metre has a default, which is the
  thing it exists to prevent. Check across sessions through the ledger.
- **Novelty for its own sake.** A radical candidate that nobody could play, in a brief that needs
  something playable next week, is not a direction. It is a distraction with a high risk score.
- **Ignoring the anchor.** If nothing is familiar, the candidates are not directions for *this* piece.
- **Quietly dropping the constraint** at the first difficulty, which turns a direction back into a
  variant.
