# AI Music Studio

Agent skills for making music, and for developing the music you have already started: one Music
Director that routes each problem to the right specialist, and fifteen specialists behind it. Works
with or without a DAW, for any genre, any user.

Version 2.1-dev. MIT licensed.

> **Status: `main` is 2.1, in development and testing. It is not a release.**
>
> | Want | Use |
> |---|---|
> | the stable studio | **1.0**: the latest release on this repository's Releases page, or `git checkout v1.0` |
> | the current architecture, knowing it is being tested | `main` |
>
> 2.0 was a development milestone (commit `8017f2b`) and was never published as a release. 2.1
> hardens it: better-sourced instrument knowledge, tradition-specific instrument pages, and an
> evaluation harness that tests what the studio does rather than only whether its files are tidy.
> Nothing on `main` should be treated as stable until a 2.1 release is published.

## Create, continue, learn, finish

The studio is not only a generator. Four kinds of request, all first class:

**CREATE.** "Write a chorus that lifts." "Give me three directions for this idea, without rewriting
what I have." "Turn this painting into a piece." The Creative Lab produces directions that differ by
*mechanism* rather than by adjective, and the composition chain builds the one you choose.

**CONTINUE.** "What was I doing?" "What should I work on next?" "Look at everything I have and tell me
what this project is becoming." The Project Guide keeps the project's thesis, its unresolved
decisions and its state, and tells you what is actually missing. Often that is not another song.

**LEARN.** "Teach me why this arrangement is weak." "Why does that chorus work?" The studio explains
on your material, demonstrates the alternative on a copy, and leaves you to do the work. Diagnosis
requests return causes and stop rather than quietly rewriting your song.

**FINISH.** "Help me finish this EP." "Is this done?" You agree what done means, and the studio
reports the state against it. It never declares your project finished for you.

## What is in it

One user-facing orchestrator, `music-director`, and fifteen specialists:

| Skill | Handles |
| --- | --- |
| `project-guide` | the project over time: thesis, state, gaps, next actions, finishing |
| `creative-lab` | directions that differ by mechanism; seeds, fusion, experimental systems |
| `composer` | chords, melody, bass, rhythm, motifs, form, pitch and rhythm systems |
| `arranger` | section order, contrast, energy, transitions, orchestration, adaptive form |
| `vocal-director` | what the voices do: hierarchy, stacks, ad-libs, flow, breath, silence |
| `performance-director` | how it is played: articulation, phrasing, feel, feasibility |
| `producer` | sound choice, synthesis, layering, effects, automation, sample packs |
| `lyric-generator` | lyrics fitted to a melody: syllables, stress, rhyme, cross-song uniqueness |
| `mix-engineer` | balance, masking, dynamics, stereo, loudness, per-track evidence |
| `reference-analyst` | what a reference or analyzer report shows, and what transfers |
| `music-critics` | originality, theory, groove, performance, diversity, preference-neutral critique |
| `listener-model` | expectation, surprise, memorability, groove, attention, a listener panel |
| `midi-builder` | validated multitrack MIDI that executes a performance plan |
| `plugin-auditor` | what is installed, what it can play and tune, and an optional calibration pass |
| `music-research` | basic or deep research on an artist's creative system, saved as a pack |

Shared protocols, schemas and knowledge live in `shared/`, DAW adapters in `daw-adapters/`, the
research behind the skills in `research/`, examples in `examples/`, and release checks in `tools/`.

You speak to the Music Director as if it were one skill. It decides which specialists are needed and
keeps them from solving the wrong kind of problem.

## Quick start

1. **Put the folder where your agent can read it**, for example by cloning this repository.
2. **Make your profile:** copy `profiles/user-profile.example.yaml` to `profiles/local/<you>.yaml`
   (git ignores that folder) and fill in what you know: where songs go, your DAW, your
   instruments, your analyzer, your default deliverable. Leave the rest empty.
3. **Tell your agent about both**, in its instructions file (for example `CLAUDE.md` or
   `AGENTS.md`):

   ```text
   For music tasks, read <path>/music-director/SKILL.md and follow it. Paths inside the pack are
   relative to <path>. My profile is <path>/profiles/local/<you>.yaml.
   ```

4. **Ask for music, or for help with the music you have.** "Write a chorus that lifts", "why does my
   mix sound small?", "give me three directions for this", "what should I work on next?", "help me
   finish this EP".

Nothing is required beyond an agent that can read files. A DAW connection, Python 3 (for the
tools) and an audio analyzer each unlock more.

## How work flows

Do not treat music creation as:

`prompt -> generic chords -> generic drums -> polish`

Use:

`artistic intent -> reference/constraint analysis -> divergent musical search -> composition ->
arrangement -> vocal architecture -> production -> performance planning -> render/analysis ->
criticism -> revision`

The studio keeps apart:

- composition problems from arrangement problems;
- arrangement problems from mix problems;
- notes from performances;
- what the voices sing from what the voices do;
- theory explanation from theory policing;
- originality from randomness;
- reference analysis from imitation;
- production intent from measurable rendered results;
- this task from this project.

For rendered work it audits the instruments first, exports every track as well as the mix, checks
every note against the MIDI (`shared/RENDER_VERIFICATION.md`), and does not call anything final while
a note is silent or a part is buried.

## Routing

| User request | Route |
|---|---|
| directions, options, "something different", a seed, a fusion | Creative Lab |
| what should I do next, why am I stuck, what is this becoming, help me finish | Project Guide |
| chord progression, melody, bassline, rhythm, motif, pitch system | Composer |
| weak chorus, section flow, transitions, instrumentation, game-music states | Arranger |
| backgrounds, stacks, ad-libs, rap flow, choir, what the voices do | Vocal Director |
| it sounds fake, it sounds stiff, articulation, feel, is this playable | Performance Director |
| synth patch, texture, layering, creative effects, automation | Producer |
| lyrics, syllable fit, rhyme, prosody | Lyric Generator |
| mud, harshness, masking, stereo, loudness, balance | Mix Engineer |
| analyze a song, a reference or an analyzer report | Reference Analyst |
| "is this generic?", theory check, groove check, critique | Music Critics |
| will a listener remember it, where attention drops, how it will be heard | Listener Model |
| a multitrack MIDI file, a performance plan written to notes | MIDI Builder |
| which instruments are available, what they can play and tune, calibration | Plugin Auditor |
| research an artist, build or extend an artist research pack | Music Research |
| notes that do not play, parts too quiet, checking each track after an export | Music Director, by `shared/RENDER_VERIFICATION.md` |
| substantial track work | Music Director coordinates several |

Specialists pass structured handoffs rather than repeating the whole conversation
(`shared/TRACK_STATE_SCHEMA.md`, `shared/SPECIALIST_HANDOFF_SCHEMA.md`).

## Shared systems

Reusable protocols and knowledge that several specialists need. A specialist owns a **kind of
decision**; a shared system is a **representation or a body of knowledge**.

| Area | Files |
|---|---|
| state | `TRACK_STATE_SCHEMA`, `PROJECT_STATE_SCHEMA`, `MUSICAL_MEMORY_SCHEMA`, `SPECIALIST_HANDOFF_SCHEMA` |
| creativity | `CREATIVE_EXPLORATION_SCHEMA`, `SEED_TRANSLATION`, `FUSION_PROTOCOL`, `EXPERIMENTAL_SYSTEMS` |
| diversity | `TRACK_DIVERSITY_LEDGER` |
| performance | `HUMAN_PERFORMANCE_SCHEMA`, `VOCAL_ARCHITECTURE_SCHEMA`, `INSTRUMENT_BEHAVIOR_SCHEMA`, `VIRTUAL_INSTRUMENT_GUIDE/` |
| musical knowledge | `MUSICAL_SYSTEMS/`, `RHYTHM_SYSTEMS/`, `TUNING_AND_MPE` |
| interactive music | `ADAPTIVE_MUSIC` |
| working with the user | `INTERACTION_MODES` |
| quality and evidence | `QUALITY_GATE`, `RESEARCH_RULES`, `GENERALIZATION_RULES`, `RENDER_VERIFICATION` |
| artifacts and tools | `MIDI_EXPORT_SCHEMA`, `LYRIC_ALIGNMENT_SCHEMA`, `PLUGIN_CALIBRATION_SCHEMA`, `DAW_ADAPTER_CONTRACT`, `FILE_NAMING`, `FREE_INSTRUMENTS` |

## Three rules worth knowing before you use it

**Organic performance is not random humanization.** Studies that shifted timing systematically found
groove and naturalness went *down* against an exact grid, and where looseness is preferred it has
long-range structure rather than being noise. So the studio models phrase arcs, metrical accent,
tempo-dependent swing and ensemble spread, each with a magnitude you can read and argue with. There is
no randomness control (`shared/HUMAN_PERFORMANCE_SCHEMA.md`).

**A tradition is not a scale.** Sources inside maqam, raga, gamelan, blues and modal folk practice all
say the same thing in different words: the operative units are cells, behaviours, cycles and pitch
areas, not pitch sets. The studio teaches the logic and names what must not be universalised, and it
will not use a tradition as a colour over an otherwise unchanged piece
(`shared/MUSICAL_SYSTEMS/INDEX.md`).

**Diversity is asked about, not enforced.** When several of your recent tracks share a shape, the
studio tells you which dimensions and asks whether that is your project's identity, a genre
convention, a deliberate callback, or a default nobody chose. Only the last one gets acted on
(`shared/TRACK_DIVERSITY_LEDGER.md`).

## Your profile: what is yours stays out of the skills

The skills are the same for every user. Paths, DAWs, installed plugins and library editions, sample
folders, artist research packs, the analyzer, default deliverables, output layout, naming overrides,
interaction preferences and private terms all live in a **user profile**, kept outside the skill
files:

- schema and which specialist reads what: `shared/USER_PROFILE_SCHEMA.md` (version 1.1);
- template: `profiles/user-profile.example.yaml`;
- findings from your own sessions go to your installation notes, never into a skill file.

## DAW adapters

Adapters translate accepted musical decisions into one DAW's actions; they never make the
musical decisions (`shared/DAW_ADAPTER_CONTRACT.md`). Included: `ABLETON_LIVE.md`,
`FL_STUDIO.md` and `PRO_TOOLS.md`, with `DAW_CAPABILITY_MATRIX.json`. Another DAW, synth or
analyzer gets its own adapter written to the same contract.

## Recommended analyzer: WavRead

The studio works without an audio analyzer, but its render verification, reference analysis and
mix feedback are only as good as what they can measure. **WavRead** (https://wavread.com) reads
a mix and its stems and is the analyzer these skills were built and tested with. Name it, or
any other analyzer, in your profile's `analyzer` section; leave it empty to work without one.

## Free instruments

When the palette lacks an instrument the music needs, the studio can suggest free ones, each
with what an agent can do with it: `shared/FREE_INSTRUMENTS.md`. You install them; the studio
never installs, signs in or accepts a licence.

## File naming

Every artifact the studio writes follows `shared/FILE_NAMING.md`. That covers song folders,
MIDI, lyrics, sessions, mixes, stems, finals, analyses, verification reports and calibration
profiles. The user's profile can override it.

## Checks

```bash
python3 tools/check_all.py --profile profiles/local/<you>.yaml
```

Runs ten checks and exits non-zero if any finds something: every manifest path exists, every named
path resolves, every skill is shaped like a skill and stays tool-neutral, every schema block parses
and the shared vocabularies agree, every example obeys the schema it illustrates, old profiles,
track states and paths still read, every instrument claim is labelled no stronger than its source was
read, the evaluation harness catches what it claims to, the Director's routing matches the folder and the README, and no
user-specific content has leaked into the skills. A GitHub Action runs them on push.

The standard library is enough for most of them. PyYAML adds the schema parse, the example and
compatibility checks and the evaluation self-test, and CI installs it.

**Behaviour is tested separately**, against a real agent, by `evals/` (`evals/README.md`): what the
studio actually does with forty-one briefs, from a coaching session that must not rewrite the user's
song to ten unrelated briefs that must not all come out the same shape. It grades structure and
behaviour; whether the music is good is left to a person listening.

## Before publishing a fork

1. `python3 tools/check_all.py --profile <your profile>` must report all checks passed.
2. `profiles/local/` must not exist in the published copy, or must be ignored.
3. Keep `LICENSE` with the folder.
4. Update `CHANGELOG.md` and the version in `manifest.json`.

## Versions

The pack version lives in `manifest.json`, and `tools/manifest_check.py` holds the README, the
CHANGELOG and every skill's front matter to it. A suffix marks a version that is not a release: `-dev` while
it is being built, `-beta.N` for a GitHub pre-release offered to testers, `-rc.N` for a release
candidate. Only a version without a suffix is published as a GitHub Release.

Shared schemas carry their own `## Version` headings. Those version the schema, not the pack, and
change only when the schema does.

## License

MIT. See `LICENSE`. Free to use, change and share, including commercially, as long as the
license and copyright notice travel with it.
