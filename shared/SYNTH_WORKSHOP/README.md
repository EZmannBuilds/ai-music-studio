# Vital Sound Design Workshop

A project-based course for learning to design, explain, test, and revise Vital patches. It is part of AI Music Studio 2.1-dev. The course uses Vital as a concrete teaching synth; its core sound-design reasoning is portable to other synths.

## Two ways to use it

- **Teach me:** follow `COURSE.md` one lesson at a time. The agent should demonstrate one idea, give you a task, and wait for what you hear before moving on.
- **Build a patch:** give the agent a role, song context, reference qualities, and plugin/DAW. It should use `TEACHER_PROTOCOL.md` and `PATCH_STANDARD.md` to make a playable, explained patch and test plan.

No Vital presets or builder scripts are bundled in this skill. The course therefore teaches the controls and verification process without pretending a written recipe has already been loaded and auditioned in your Vital installation.

## Learning sequence

1. Start from Init: sound source, amplitude envelope, note length.
2. Shape harmonics: oscillator level, wavetable position, spectral/wave warping, filter.
3. Make motion: envelopes, LFO shapes, random sources, and modulation ranges.
4. Build interaction: velocity, note tracking, aftertouch/MPE, macros, remapping.
5. Layer with a job: foundation, transient, body, noise, and stereo support.
6. Make it playable: mono/poly, glide, note range, chord behavior, automation.
7. Add effects after the source works; then audition in a musical context.
8. Diagnose, version, compare, and revise.
9. Capstone: create three contrasting patches, document them, and pass the listening checks.

## Files

- `TEACHER_PROTOCOL.md` — how the agent teaches or builds a patch.
- `COURSE.md` — lesson plans, exercises, checkpoints, and capstone.
- `PATCH_STANDARD.md` — a reusable patch brief and quality rubric.
- `PATCH_RECIPES.md` — three detailed, original architectures to build and customize.
- `RESEARCH_NOTES.md` — findings, source roles, and limitations.
- `AUTOMATION_GUIDE.md` — what a future preset builder would need to do, and what is not yet shipped or tested.
- `FIELD_TEST.md` — what building the recipes, the challenge and the capstone in Vital measured: parameter units, what the protocol caught, and traps in measuring it.
