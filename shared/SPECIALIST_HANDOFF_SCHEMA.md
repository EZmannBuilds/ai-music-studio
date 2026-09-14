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
  constraints_created: []
  dependencies:
    needs_from_other_specialist: []
  risks: []
  next_best_action:
```

A handoff should be concrete enough that another specialist can continue without re-solving
the same problem.

If measurements came from an analyzer, preserve units and values exactly.
