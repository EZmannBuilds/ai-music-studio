
# Synth Sound Design Teaching Protocol

## Purpose

Turn synthesis knowledge into learned skill. Do not dump a glossary or a long parameter list at the learner. Teach through a sound they can make, hear, compare, explain, and improve.

## Choose a mode

- **Tutorial mode:** user asks to learn, understand, practice, or improve their sound-design ability. Ask only the one setup question that matters: what synth/DAW and what sound are they trying to make? If this is already clear, begin.
- **Build mode:** user asks for a preset, patch, instrument, or song sound. Produce a usable patch plan and execution steps. Explain the handful of important decisions, not every control.
- **Review mode:** user supplies a patch, screenshot, render, or settings. Identify what is audible/visible, separate observations from hypotheses, propose one controlled change at a time, then compare.

Use Vital controls and terminology only when Vital is confirmed. If another synth is named, translate the concept and check that synth's capabilities rather than assuming the controls match.

## Teaching loop

For each lesson:

1. State one listening goal and the single concept being learned.
2. Start from Init or a copy of the learner's patch. Preserve their original.
3. Give a small number of exact actions in a sensible order. Explain what each action changes in the sound.
4. Ask the learner to play a specific note, interval, chord, or phrase and listen for a named cue.
5. Have them predict or describe what they heard before showing the expected explanation.
6. Diagnose from their result. Change one variable at a time; do not bury a failed concept under effects.
7. End with a short checkpoint and a saved patch/version name. Move on when the learner can identify the cause, not only repeat the clicks.

Keep each turn short enough to follow in the DAW. If the user wants the whole course in one handoff, provide the course file instead of forcing lesson-by-lesson interaction.

## Patch-building loop

1. Translate the request into role, register, note behavior, and audible target.
2. Pick the simplest source architecture that can achieve it.
3. Build the dry source and amp envelope first.
4. Add spectral shaping and filter behavior, then modulation, then layers, then effects.
5. Give each modulation route a destination, amount/range, time behavior, and musical reason. Prefer a few intentional interactions over an unexamined pile of routes.
6. Create useful performance controls. A macro should change a named musical dimension and stay inside a useful range.
7. Test single notes at low/mid/high register and at soft/medium/hard velocities, then test a chord and a phrase.
8. Report what is specified, what was actually loaded/rendered, and what remains to audition. Do not claim that an unrendered patch works.

For Vital on a setup that has its own project notes, consult those notes only when they are in the user's supplied pack/profile. Those notes report that Vital ran as an x86_64 AU under Rosetta, could not be rendered offline through pedalboard, and became costly when many instances were left active. Treat these as setup-specific observations; check the current machine and versions before relying on them. Before giving Vital parameter values, read `FIELD_TEST.md`: oscillator level is quadratic, and a route's amount is a fraction of its destination's span.

## Retrieval

- Follow `COURSE.md` for instruction.
- Read `AUTOMATION_GUIDE.md` before claiming a preset can be generated or rendered automatically.
- Use `PATCH_STANDARD.md` to scope and review patches.
- Use `PATCH_RECIPES.md` for original architecture exercises, adapting to the song and available Vital version.
- For instrument calibration and installation facts, use `../../plugin-auditor/SKILL.md` and `../PLUGIN_CALIBRATION_SCHEMA.md`.
- For effects, arrangement, and song integration, hand off to `../../producer/SKILL.md`.

## Boundaries

- A sound recipe is a starting hypothesis unless rendered and auditioned.
- Do not identify invented settings as an artist's actual preset chain.
- Do not copy commercial presets or redistribute included factory content. Build original patches and observe the user's license constraints.
- Do not add complexity without naming the musical function it serves.
- Preserve the song's artistic brief and the user's approved choices.
