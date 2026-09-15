<!-- expected pass response for E1. Hand-written to test the graders, not a model output. -->

Bars 1 to 24: a solo oboe opens alone, and the orchestra fills in choir by choir until the tutti
lands on the last bar. That is one gesture with five different answers to it, not one crescendo
curve copied onto forty parts.

```yaml
ensemble_gesture:
  id: buildup-1-24
  type: crescendo
  origin_bar: 1
  target_bar: 24
  responses:
  - part: Oboe I (solo)
    lag_beats: 0
    curve: linear
    role: lead
  - part: Violins I and II
    lag_beats: 4
    curve: exponential
    role: follow
  - part: Woodwinds (flutes, clarinets, bassoons)
    lag_beats: 8
    curve: stepped
    role: follow
  - part: Brass (horns, trumpets, trombones)
    lag_beats: 16
    curve: delayed_onset
    role: held_back
  - part: Percussion and low brass (tuba, timpani)
    lag_beats: 20
    curve: delayed_onset
    role: held_back
  why: an intimate solo opening has to visibly cede the foreground as the orchestra fills in, so
    each choir enters later and steeper than the one before it, rather than the whole orchestra
    swelling as one undifferentiated block
```

```yaml
performance_state:
  part: Oboe I (solo)
  instrument: oboe
  performer_count: 1
  realism_target: realistic
  timing_character:
    models:
    - model: phrase_arch
      magnitude: 2% tempo lean into the phrase ends of bars 1-4
    gesture_ref: buildup-1-24
    grid_reference: the quarter-note pulse at 96 BPM
```

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - performance-director
  knowledge_loaded:
  - shared/HUMAN_PERFORMANCE_SCHEMA.md
  - shared/VIRTUAL_INSTRUMENT_GUIDE/ORCHESTRAL.md
  created_material:
  - ensemble gesture
  - performance plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
