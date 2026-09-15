<!-- expected pass response for D8. Hand-written to test the graders, not a model output. -->

Four players, six rules.

```yaml
rule_set:
  roles:
  - drone
  - pulse
  - two soloists
  signals:
  - 'raise a hand: drop out'
  - 'nod: next section'
  permitted_actions:
  - imitate
  - contrast
  - rest
  triggering_conditions:
  - when you hear the pulse stop, answer it
  override_or_escape: anyone may play the opening motif to reset
  ending_condition: when the drone player stops and nobody answers within ten seconds
  attention_instruction: listen for the quietest player
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - creative-lab
  knowledge_loaded: []
  created_material:
  - rule set
  modified_user_material: []
  questions_asked: []
  declined: []
```
