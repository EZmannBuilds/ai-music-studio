# Specialist Handoff Schema

When a specialist finishes, return a compact handoff.

```yaml
specialist_handoff:
  specialist:
  task_received:
  diagnosis:
  decisions:
    - action:
      reason:
      confidence:
  created_material:
    chords:
    melody:
    rhythm:
    midi_spec:
    sound_design:
    automation:
    mix_changes:
    performance_plan:            # shared/HUMAN_PERFORMANCE_SCHEMA.md
    vocal_plan:                  # shared/VOCAL_ARCHITECTURE_SCHEMA.md
    candidates: []               # shared/CREATIVE_EXPLORATION_SCHEMA.md
    project_state_delta:         # what changed in the project, not the whole state
  interaction:
    mode:                        # shared/INTERACTION_MODES.md
    mode_respected: true | false
    teaching_notes:              # what was explained, in TEACH ME and DO IT WITH ME
  constraints_created: []
  dependencies:
    needs_from_other_specialist: []
  risks: []
  next_best_action:
```

A handoff should be concrete enough that another specialist can continue without re-solving
the same problem.

If measurements came from an analyzer, preserve units and values exactly.


## Constraints travel

`constraints_created` is not advisory. A constraint carried from a chosen exploration candidate, from
a fusion bridge, or from a feasibility report binds the specialists downstream of it. A specialist
that cannot work within one returns it to the Director rather than dropping it quietly.

## Mode travels

A handoff records the interaction mode it was produced under, so that a diagnosis does not become a
rewrite as it passes between specialists.

## Session trace

What the whole session did, in one block. The Director writes it at the end of a reply **only when the
user or an evaluation runner asks for it**; `evals/` asks, so that routing and material preservation
can be checked rather than assumed. It is optional, adds nothing to any other record, and a session
that never writes one is unaffected.

```yaml
session_trace:
  session_mode:                  # CREATE | CONTINUE | DIAGNOSE | LEARN | REVISE | ORGANIZE | FINISH | RELEASE
  interaction_mode:              # shared/INTERACTION_MODES.md
  request_class: []              # from the Director's first diagnostic
  routes: []                     # specialist folder names consulted, in order, e.g. [composer, performance-director]
  knowledge_loaded: []           # shared/ files opened for this request, e.g. shared/MUSICAL_SYSTEMS/MAQAM.md
  created_material: []           # new musical material the studio wrote, by kind: melody, lyric, plan, midi, ...
  modified_user_material: []     # the user's own material changed; each entry: {what:, on_copy: true | false}
  questions_asked: []
  declined: []                   # each entry: {what:, why:}, e.g. restricted repertoire, voice imitation
```

Write what happened. `modified_user_material` is empty when the user's material was only read, and
an edit made on a copy is still listed, with `on_copy: true`.
