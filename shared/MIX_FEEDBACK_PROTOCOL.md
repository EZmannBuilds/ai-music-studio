# Mix Feedback Protocol

A MIDI arrangement and an audio mix are different artifacts.

Do not claim that a MIDI file is "mixed" merely because it contains:
- velocity;
- CC7 volume;
- CC10 pan;
- CC11 expression.

Those only create a rough playback balance.

## Preferred workflow

```text
composition
→ arrangement
→ sound assignment / production
→ rough balance
→ audio render
→ mix analysis
→ revision
```

## Analyzer use

If an audio analyzer such as WavRead is available and appropriate, the agent may use it.

If it is not available, the agent may suggest that the user run the render through an analyzer.

Do not require an analyzer.

## Analyzer-bias protection

Every analysis result must be classified:

```yaml
mix_feedback:
  measured:
  inferred:
  recommended:
  confidence:
  reference_context:
```

### MEASURED
What the tool actually reports.

Examples:
- spectral concentration;
- loudness;
- dynamic range;
- stem level;
- frequency-balance result.

### INFERRED
What the agent believes may be causing the measurement.

### RECOMMENDED
What to change.

Do not collapse these three steps.

## Reference-conditioned mixing

Do not compare every mix to one generic target.

Use, when available:
- the user's reference track;
- genre-appropriate references;
- the intended playback context;
- the user's stated aesthetic.

## Upstream-first rule

When an analyzer reports a problem, diagnose in this order:

```text
composition
→ arrangement
→ source / sound design
→ level
→ EQ / dynamics / spatial processing
```

Example:

Measured:
low-mid congestion.

Possible upstream fixes:
- change voicing;
- remove duplicate layer;
- shorten envelope;
- alter register.

Do not automatically prescribe a notch EQ.

## Human listening remains primary

An analyzer can be wrong for the artistic target.

If the analyzer and listening intent disagree, explain the tradeoff instead of blindly forcing
the measurement into a target range.
