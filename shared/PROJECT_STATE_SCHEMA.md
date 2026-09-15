# Project State Schema
## Version 1.0

State above one song: what the project is, what is done, what is unresolved, and what to do next.

Written by `project-guide/SKILL.md`. Read by the Music Director at session start, and by Creative Lab,
Arranger, Music Critics and Lyric Generator when a decision crosses songs.

```text
project_state      the project            references tracks; never copies their contents
track_state        one song               references musical details
track_dna          one ledger row         the song's shape, for comparison
```

**Project State references Track States by path or id.** It does not duplicate them. A tempo lives in
the track state; the fact that four tracks share a tempo family lives in the ledger; the question of
whether that is the project's identity lives here.

---

# 1. Where it lives, and when it is loaded

- The file is at the user's `paths.project_state` (`shared/USER_PROFILE_SCHEMA.md`), or beside the
  project. With neither, **the Project Guide asks once whether to create one and writes nothing until
  the user says yes.**
- The Director loads it at session start when the request concerns an existing project, and only then.
- This is the **exception to the Director's reset rule**. Resetting between unrelated tasks is right.
  Forgetting the project the user is in the middle of is not. Values from a project state apply to
  that project and travel nowhere else.

---

# 2. `project_state`

```yaml
project_state:
  name:
  project_type: song | ep | album | soundtrack | game_score | film_cues | live_set |
                sound_design | experimental | other
  started:
  last_session:                # date and time; the Director may stamp this
  user_goal:                   # in the user's own words

  thesis:                      # one sentence: what this project is. Empty means unanswered.
  thesis_status: confirmed_by_user | proposed | open
  emotional_world:
  sonic_world:
  constraints: []              # deliberate limits the project is working under
  audience_or_context:

  current_phase: exploring | drafting | developing | revising | finishing | released | paused

  tracks:
    - id:
      title:
      track_state:             # path or reference; never inlined
      status: idea | sketch | draft | arranged | produced | mixed | done
      role_in_project:         # what this track is for. See section 3.
      strength: 1-5            # the user's judgement, or the studio's, labelled
      notes:

  finished: []                 # what is genuinely done, with what "done" meant
  in_progress: []
  unresolved: []               # open questions, per section 4
  blocked: []                  # what cannot move, and what would unblock it

  recurring_motifs: []         # musical material that returns across tracks, deliberately
  palette: []                  # instruments, textures and devices the project uses
  intentional_outliers: []     # the track that breaks the rules on purpose, and why

  risks: []                    # creative risks worth naming: sameness, scope, unearned scale
  health:                      # section 6
  next_best_actions: []        # section 5
  decisions_needed: []         # what only the user can answer
  decision_log: []             # what was decided, when, and why
  revision_queue: []           # known fixes, ordered, with the reason each matters
  completion_definition:       # section 7
```

---

# 3. `album_state`

For a multi-track release, add:

```yaml
album_state:
  track_roles: {}              # track id -> function in the sequence
  opener_function:
  closer_function:
  emotional_arc: []
  tempo_map: []                # tempo by position, to see clustering
  key_or_pitch_map: []
  recurring_motifs: []
  intentional_callbacks: []    # deliberate returns, distinct from repetition
  diversity_targets: []        # what the project wants to vary, and what it wants constant
  palette: []
  narrative_links: []
  transition_strategy:         # how one track reaches the next: gap, segue, attacca, hard cut
  missing_track_functions: []  # the gap analysis that prevents writing another of what exists
  sequence_candidates:         # at least two, built on different principles
    - principle:               # e.g. energy alternation, narrative order, key relations
      order: []
      what_it_serves:
```

Sequencing is offered as candidates, never as a verdict. Corpus studies of commercial albums describe
what professionals tend to do, and the same authors note evidence that reordering may not change how
listeners feel (`research/CREATIVITY_AND_PEDAGOGY.md`, section 5). The studio does not tell a user
their running order is wrong.

For a score or a game project, add `shared/ADAPTIVE_MUSIC.md` state per cue and use `track_roles` for
scene or state function.

---

# 4. Unresolved items

An unresolved item is a **question**, not a task.

```yaml
unresolved:
  - question:
    affects: []                # track ids, or "project"
    options_considered: []
    blocking: true | false
    raised:
    owner: user | studio
```

An empty field in this schema is an unanswered question, not permission to invent an answer. The
Project Guide may propose a thesis; it may not record one as confirmed until the user confirms it.

---

# 5. Next best actions

```yaml
next_best_actions:
  - action:
    why:                       # the reason, in terms of the project, not of productivity
    kind: write | revise | finish | decide | organise | learn | rest
    effort: small | medium | large
    unblocks: []
```

The rule that makes this musical rather than administrative: **"write another track" is one action
among several, and often not the right one.** When two tracks solve the same project function, the
action might be to change one of them, to cut one, to re-sequence, or to decide that the doubling is
the point. When a project has no structural disruption, the actions include re-arranging an existing
track, adding an interlude, changing a running order, or leaving it alone because the flatness is the
intent.

---

# 6. Project health

```yaml
health:
  function_coverage:           # which project functions are filled, and which are doubled or empty
  diversity:                   # from the ledger: what varies, what repeats, and whether that is identity
  momentum:                    # what has moved since the last session
  decision_debt:               # how many unresolved questions are blocking work
  finishing_risk:              # what is most likely to stop this being finished
  note: "health is a description, not a score"
```

---

# 7. Completion definition

Written **before** production, not after. Research on creative work finds that finishing is a decision
rather than something detected, and that closing the problem too early costs originality
(`research/CREATIVITY_AND_PEDAGOGY.md`, section 5).

```yaml
completion_definition:
  what_done_means:             # the user's words
  kind: deadline | checklist | listening_test | felt_readiness
  criteria: []
  who_decides: user
  agreed:                      # date and time
```

The studio never declares a project finished. It reports the criteria against the state and says what
remains. `shared/QUALITY_GATE.md` and the release gate in `shared/RENDER_VERIFICATION.md` still govern
whether an individual render may be called final.

---

# 8. What Project State is not

- It is not a task manager. Every field earns its place by changing a musical decision.
- It does not store musical detail. That is the track state.
- It does not judge tracks. Strength is the user's, or is labelled as the studio's opinion.
- It does not travel. A project's palette, tempo habits and motifs are that project's, and the
  Director does not carry them into unrelated work.
- It does not assume the album. A live set, a cue list, a generative system and a single song are all
  projects, and the schema supports each without treating the album as the real one.
