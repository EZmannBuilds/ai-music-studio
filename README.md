# AI Music Studio

Agent skills for writing, arranging, producing, mixing and checking music: one Music Director
that routes each problem to the right specialist, and eleven specialists behind it. Works with or
without a DAW, for any genre, any user.

## What is in it

One user-facing orchestrator, `music-director`, and eleven specialists:

| Skill | Handles |
| --- | --- |
| `composer` | chords, melody, bass, rhythm, motifs, form, and a melody-variety gate |
| `arranger` | section order, contrast, energy, transitions, orchestration |
| `producer` | sound choice, synthesis, layering, effects, automation, sample packs |
| `lyric-generator` | lyrics fitted to a melody: syllables, stress, rhyme, cross-song uniqueness |
| `mix-engineer` | balance, masking, dynamics, stereo, loudness, per-track evidence |
| `reference-analyst` | what a reference song or analyzer report shows, and what transfers |
| `music-critics` | originality, theory, groove and preference-neutral critique |
| `listener-model` | expectation, surprise, memorability, groove, attention |
| `midi-builder` | validated multitrack MIDI, lyric events, instrument-safe building |
| `plugin-auditor` | what instruments are installed, what they can play, how an agent can drive them, and an optional calibration pass |
| `music-research` | basic or deep research on an artist's creative system, saved as a reusable pack |

Shared protocols and schemas live in `shared/`, DAW adapters in `daw-adapters/`, the research
behind the skills in `research/`, a lyric-alignment example in `examples/`, and a release
check in `tools/`.

You speak to the Music Director as if it were one skill. It decides which specialists are needed
and keeps them from solving the wrong kind of problem.

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

4. **Ask for music.** "Write a chorus that lifts", "why does my mix sound small?", "build a
   24-track MIDI for this idea", "export an instrumental and check every note".

Nothing is required beyond an agent that can read files. A DAW connection, Python 3 (for the
tools) and an audio analyzer each unlock more.

## How work flows

Do not treat music creation as:

`prompt -> generic chords -> generic drums -> polish`

Use:

`artistic intent -> reference/constraint analysis -> divergent musical search -> composition ->
arrangement -> production -> render/analysis -> criticism -> revision`

The studio keeps apart:

- composition problems from arrangement problems;
- arrangement problems from mix problems;
- theory explanation from theory policing;
- originality from randomness;
- reference analysis from imitation;
- production intent from measurable rendered results.

For rendered work it audits the instruments first, exports every track as well as the mix,
checks every note against the MIDI (`shared/RENDER_VERIFICATION.md`), and does not call anything
final while a note is silent or a part is buried.

## Routing

| User request | Route |
|---|---|
| chord progression, melody, bassline, rhythm, motif | Composer |
| weak chorus, section flow, transitions, instrumentation | Arranger |
| synth patch, texture, layering, creative effects, automation | Producer |
| mud, harshness, masking, stereo, loudness, balance | Mix Engineer |
| analyze a song, a reference or a WavRead report | Reference Analyst |
| "is this generic?", theory check, groove check, critique | Music Critics |
| which instruments and plugins are available, what they can play, calibration | Plugin Auditor |
| research an artist, build or extend an artist research pack | Music Research |
| notes that do not play, parts too quiet, checking each track after an export | Render Verification protocol |
| substantial track work | Music Director coordinates several |

Specialists pass structured handoffs rather than repeating the whole conversation
(`shared/TRACK_STATE_SCHEMA.md`, `shared/SPECIALIST_HANDOFF_SCHEMA.md`).

## Your profile: what is yours stays out of the skills

The skills are the same for every user. Paths, DAWs, installed plugins and library editions,
sample folders, artist research packs, the analyzer, default deliverables, output layout, naming
overrides and private terms all live in a **user profile**, kept outside the skill files:

- schema and which specialist reads what: `shared/USER_PROFILE_SCHEMA.md`;
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

## Before publishing a fork

1. `python3 tools/privacy_check.py --profile <your profile>` must report 0 findings.
2. `profiles/local/` must not exist in the published copy, or must be ignored.
3. Keep `LICENSE` with the folder.
4. Update `CHANGELOG.md` and the version in `manifest.json`.

## License

MIT. See `LICENSE`. Free to use, change and share, including commercially, as long as the
license and copyright notice travel with it.
