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
