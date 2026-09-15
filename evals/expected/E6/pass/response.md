<!-- expected pass response for E6. Hand-written to test the graders, not a model output. -->

Five layers, five jobs. Strings carry the melodic and expressive weight, the synth pad sits under it
as harmonic colour rather than a second lead, the sub bass extends the low end past where an acoustic
bass instrument reaches, brass stabs mark the structural accents, and the vocal-texture layer builds
tension underneath without ever becoming its own melody.

```yaml
role_assignment:
- bar_range: "throughout"
  role: emotion_carrier
  instruments: [Strings]
- bar_range: "throughout, under the strings"
  role: color
  instruments: [Synth pad]
- bar_range: "throughout"
  role: scale_extender
  instruments: [Sub bass]
- bar_range: "structural downbeats and section changes"
  role: impact
  instruments: [Brass stabs]
- bar_range: "building under the second half of the cue"
  role: tension
  instruments: [Vocal-texture layer (wordless)]
  why: a sustained, wordless layer with no melodic identity of its own is better used to build
    anticipation than to compete with the strings for the emotional lead
```

The sub bass is doing something no instrument in this cue's string section can: `shared/VIRTUAL_
INSTRUMENT_GUIDE/STRINGS.md` curates the double bass down to written C1 (sounding an octave lower),
with a low extension to sounding C0 on some instruments. A synthesized sub bass has no such acoustic
floor, which is exactly why it is the `scale_extender` here rather than a doubled bass line.

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - arranger
  - producer
  knowledge_loaded:
  - shared/ORCHESTRATION_KNOWLEDGE.md
  - shared/VIRTUAL_INSTRUMENT_GUIDE/STRINGS.md
  created_material:
  - role assignment
  modified_user_material: []
  questions_asked: []
  declined: []
```
