# Listener State Schema

Use this schema when a creative decision depends on how the listener is likely to experience
the music over time.

These values are planning estimates, not objective measurements.

```yaml
listener_state:
  familiarity:
  predictability:
  uncertainty:
  surprise:
  harmonic_tension:
  rhythmic_tension:
  groove_drive:
  memorability:
  salience:
  emotional_valence:
  emotional_arousal:
  perceived_power:
  density:
  attentional_focus:
  source_separability:
```

## Definitions

### Familiarity
How strongly the current material resembles already-established material in this track or
genre context.

### Predictability
How likely the next event feels from the current context.

### Uncertainty
How many plausible continuations the listener may be entertaining.

### Surprise
How unexpected the event is after it occurs.

### Harmonic / rhythmic tension
Expected pressure for continuation or resolution.

### Groove drive
The pleasurable urge to move with the pulse. Do not equate this with raw syncopation.

### Memorability
How likely a musical object is to be retained and recognized.

### Salience
How strongly an event or layer captures attention.

### Attentional focus
The intended foreground object at that moment.

### Source separability
How easily the listener can perceptually segregate important concurrent layers.

## Planning curves

For important sections, optionally create a time series:

```yaml
bar_1_4:
  familiarity: medium
  uncertainty: low
  surprise: low
  groove_drive: medium
bar_5_8:
  familiarity: medium
  uncertainty: rising
  surprise: medium
  groove_drive: high
```

Do not maximize all dimensions.

Musical pleasure often depends on changing relationships between expectation, uncertainty,
surprise, repetition, and resolution.
