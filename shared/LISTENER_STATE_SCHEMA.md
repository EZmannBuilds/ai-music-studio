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


# Canonical perceptual timbre dimensions

Defined here once. The Producer and the Listener Model both reference this block rather than each
keeping their own list, which is how the two lists drifted apart before 2.0.

```yaml
perceptual_timbre:
  hard_soft:
  sharp_dull:
  bright_dark:
  explosive_calm:
  rough_smooth:
  stable_moving:
  tonal_noisy:
  dense_open:
```

Two sounds can share a brightness and still be perceptually far apart, because attack, roughness,
noisiness and spectrotemporal movement differ. Do not reduce timbre to brightness
(`research/PERCEPTION_AND_PRODUCTION.md`, section 6).

# Listener panel

One simulated listener hides disagreement, and disagreement is the useful part.

```yaml
listener_panel:
  perspectives:
    - name: scene_native | casual | musician | producer | live_crowd | headphone_listener
      attention_channels: []     # which of: affect_and_gist, structure_and_harmony,
                                 # production_and_timing, body_and_groove
      what_they_notice:
      how_it_feels:
      what_they_would_not_notice:
  agreements: []
  disagreements: []              # returned, never averaged
  confidence: low                # always low; these are tendencies, not data
```

## Rules

- **Perspectives are attention channels, not demographic caricatures.** Research finds untrained
  listeners perceive tension, structure and emotion at levels close to trained ones; the difference is
  largely in what they can *name* (`research/CREATIVITY_AND_PEDAGOGY.md`, section 7).
- **The casual perspective reports feeling and gist, not theory.** It does not say "the pre-chorus
  lacks a lift". It says it got bored before the chorus.
- **Return disagreements.** When the musician perspective and the live-crowd perspective conflict, that
  conflict is the finding. Averaging it produces a listener who does not exist.
- **Never present this as survey data.** It is qualitative modelling. Every panel report says so, and
  says that it over-articulates: simulated listeners name specifics that real listeners in the same
  position often do not notice at all.
- A real playback test with one person outranks the whole panel.
