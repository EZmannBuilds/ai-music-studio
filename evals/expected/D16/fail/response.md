<!-- expected fail response for D16. Hand-written to test the graders, not a model output. -->
<!-- must_fail: no_random_humanization, feasibility, named_models, dynamic_arc, routes_include -->

Humanize the timing by 15% and randomise velocities slightly so it sounds played.

```yaml
performance_state:
  part: Cello
  articulation:
    default: legato
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - composer
  - midi-builder
  knowledge_loaded: []
  created_material:
  - cello part
  modified_user_material: []
  questions_asked: []
  declined: []
```
