<!-- expected pass response for D20. Hand-written to test the graders, not a model output. -->

Arrivals, Rooftop and Saturday Market all do the same function: the city as possibility, bright and fast. Night Bus and Last Train share one too. That doubling is the main gap, not a missing song.

Missing functions: a turn, where the narrator first doubts; an ending that answers the stay-or-leave question; a track with no city in it. Two of these could come from changing Saturday Market rather than writing anything new.

```yaml
album_state:
  track_roles:
    t1: arrival, possibility
    t2: night restlessness
    t3: loneliness
    t4: possibility again
    t5: the city as a machine
    t6: possibility a third time
    t7: night restlessness again
  missing_track_functions:
  - 'a turn: the first moment the narrator doubts the city'
  - an ending that answers stay or leave
  - a track with no city in it at all, only the narrator
  sequence_candidates:
  - principle: narrative order, arrival to decision
    order:
    - t1
    - t2
    - t3
    - t5
    - t4
    - t7
    what_it_serves: the thesis
  - principle: energy alternation
    order:
    - t1
    - t3
    - t2
    - t5
    - t7
    what_it_serves: listening fatigue
```
```yaml
session_trace:
  session_mode: ORGANIZE
  interaction_mode: REVIEW MY WORK
  request_class: []
  routes:
  - project-guide
  knowledge_loaded: []
  created_material: []
  modified_user_material: []
  questions_asked: []
  declined: []
```
