# User Profile Schema
## Version 1.1

The studio's skills are written for any user. Everything that belongs to **one** user or **one**
machine lives in a **user profile**, kept outside the skill folder:

- file paths;
- which DAWs, plugins, sample libraries and editions are installed;
- the analyzer they use, if any;
- default deliverables and formats;
- how their output folders are laid out;
- naming overrides;
- private boundaries;
- measurements and notes gathered while working with them.

**No skill file may name a specific user, machine, path, library purchase, or song.** If a rule
needs one of those, it reads the profile. `tools/privacy_check.py` enforces this before a release.

## Where the profile lives

- Anywhere outside the skill folder. The runner tells the Music Director where, for example in
  its own instructions file.
- Or inside the skill folder at `profiles/local/`, which `.gitignore` keeps out of any repository.
- `profiles/user-profile.example.yaml` is the template. Copy it, rename it and fill it in.

**When there is no profile**, the Director asks for the few values the task needs: the output
location, the DAW, and the deliverable mode. It writes nothing until it has them.

## Schema

```yaml
profile_version: "1.1"         # quoted, so that a future "1.10" is not read as 1.1
user:
  display_name:            # how the studio addresses the user; never written into skill files
  pronouns:                # optional
paths:
  output_root:             # where songs are written
  sample_libraries: []     # folders of loops, one-shots, stems, MIDI packs
  sample_service_downloads: []   # e.g. a sample service's download folder
  artist_research: []     # folders of artist research packs the Director may draw on
  calibration_store:       # where plugin calibration profiles are kept
  project_state:           # where project state files live (shared/PROJECT_STATE_SCHEMA.md)
  diversity_ledger:        # where the track ledger lives; defaults beside output_root
  tools:                   # helper scripts, if any
  excluded_roots: []       # music that must never be filed under output_root
output_layout:
  generation_types:        # folder per way of making a song
    - {folder: "DAW Generated", means: "multitrack MIDI built or rendered in a DAW"}
    # add genre_folders: false to a type whose files are experiments with no genre
  genres: []               # genre folders in use
  genre_rule: first_named  # a song naming two genres files under the first
daw:
  primary:
  others: []
  adapter_notes:           # installation-specific quirks, or a path to them
instruments:
  audit_file:              # last plugin audit (plugin-auditor)
  editions: []             # {name, edition, gaps: []}
  tuning_capable: []       # instruments that can be retuned, and by which mechanism
analyzer:
  name:                    # optional; WavRead (https://wavread.com) is recommended; none is a valid answer
  endpoint:                # e.g. a local address
  mode_notes:
deliverables:
  default_mode:            # instrumental | vocal_guide | full_with_vocal
  final_format: {codec: mp3, bitrate_kbps: 320, sample_rate: 48000}
  master_format: {codec: wav, bit_depth: 24}
  loudness_note:           # optional target or "measure, don't target"
naming:
  overrides: {}            # token or pattern overrides for shared/FILE_NAMING.md
  legacy_names: keep       # keep | rename_on_approval
privacy:
  boundaries_files: []     # files that define what must stay private
  private_terms: []        # names, paths and titles that must never appear in skill files
  never_upload: []         # material that must stay on the user's machine
preferences:
  standing_instructions: []   # e.g. "no lyric versions until told otherwise"
  default_interaction_mode:   # DO IT | DO IT WITH ME | TEACH ME | REVIEW MY WORK |
                              # GIVE ME OPTIONS | DIAGNOSE ONLY. Default: DO IT
  expertise:                  # self-declared and optional: beginner | developing |
                              # experienced | professional | unspecified. A starting point only.
                              # The vocabulary is shared/INTERACTION_MODES.md section 3.
  explanation_depth:          # minimal | normal | full
  diversity_ledger: on        # on | off. Off means earlier songs are never consulted.
  realism_default:            # realistic | stylised | deliberately_mechanical, when the brief
                              # does not say
notes:
  installation_notes:      # path to measurements and findings from this user's work
```

## How specialists use it

| Specialist | Reads |
| --- | --- |
| Music Director | `deliverables`, `preferences`, `output_layout`, `paths.output_root`, `paths.artist_research` |
| Plugin Auditor | `paths.sample_libraries`, `paths.sample_service_downloads`, `instruments`, `daw`, `paths.calibration_store` |
| Producer | `instruments`, `paths.sample_libraries` |
| MIDI Builder | calibration profiles found through `paths.calibration_store` |
| Mix Engineer | `deliverables`, `analyzer` |
| Reference Analyst | `analyzer` |
| Lyric Generator, Composer | `paths.output_root`, for the earlier-songs corpus |
| Music Research | `paths.artist_research`, where packs are written and read |
| Project Guide | `paths.project_state`, `preferences.default_interaction_mode` |
| Creative Lab | `paths.diversity_ledger`, `preferences.diversity_ledger` |
| Performance Director | `preferences.realism_default`, calibration through `paths.calibration_store` |
| Vocal Director | `paths.diversity_ledger`, `privacy`. The singer's range comes from the brief, not the profile |
| every specialist | `privacy`, and `naming` through `shared/FILE_NAMING.md` |

## Writing back

- The studio may add measurements and findings to the file named in `notes.installation_notes`.
- It may update `instruments.audit_file` after an audit the user ran or approved.
- **It never writes user-specific facts into skill files.** A finding that generalises goes into a
  skill file in general terms, with no name, path or title.


## Version 1.1

Additive. A 1.0 profile stays valid, and every key below is optional.

Two things a 1.0 profile may contain are read as follows, and neither needs editing:

- **`deliverables.default_mode: vocal`**, which the 1.0 template wrote, means `full_with_vocal`. The
  deliverable modes have always been `instrumental`, `vocal_guide` and `full_with_vocal`, and
  `shared/FILE_NAMING.md` already names the `full_with_vocal` version "Vocal".
- **An unquoted `profile_version: 1.0` or `1.1`** is accepted. From 2.1 the template quotes the
  version, because YAML reads an unquoted `1.10` as the number 1.1.

`tools/compat_check.py` holds both promises against `evals/fixtures/compatibility/`.

| Key | What it does |
|---|---|
| `paths.project_state` | where project state lives; with none, the Project Guide asks before writing |
| `paths.diversity_ledger` | where the track ledger lives; defaults beside `output_root` |
| `instruments.tuning_capable` | which instruments can be retuned, and how, from audits |
| `preferences.default_interaction_mode` | how much the studio does and explains by default |
| `preferences.expertise` | a starting point for calibration, not a verdict |
| `preferences.explanation_depth` | how much reasoning to include |
| `preferences.diversity_ledger` | `off` means earlier songs are never consulted |
| `preferences.realism_default` | the performance realism target when the brief is silent |

**Expertise is a starting point, never a setting to trust.** Support that helps a beginner degrades
an expert's performance, and self-reports are unreliable, so the studio calibrates from what the user
actually does and updates as it goes (`shared/INTERACTION_MODES.md`, section 3). Expertise is also per
domain: an expert producer may be new to orchestration.
