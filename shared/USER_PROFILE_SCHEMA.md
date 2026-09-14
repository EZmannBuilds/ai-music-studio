# User Profile Schema
## Version 1.0

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
profile_version: 1.0
user:
  display_name:            # how the studio addresses the user; never written into skill files
  pronouns:                # optional
paths:
  output_root:             # where songs are written
  sample_libraries: []     # folders of loops, one-shots, stems, MIDI packs
  sample_service_downloads: []   # e.g. a sample service's download folder
  artist_research: []     # folders of artist research packs the Director may draw on
  calibration_store:       # where plugin calibration profiles are kept
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
analyzer:
  name:                    # optional; WavRead (https://wavread.com) is recommended; none is a valid answer
  endpoint:                # e.g. a local address
  mode_notes:
deliverables:
  default_mode:            # instrumental | vocal | vocal_guide | ...
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
| every specialist | `privacy`, and `naming` through `shared/FILE_NAMING.md` |

## Writing back

- The studio may add measurements and findings to the file named in `notes.installation_notes`.
- It may update `instruments.audit_file` after an audit the user ran or approved.
- **It never writes user-specific facts into skill files.** A finding that generalises goes into a
  skill file in general terms, with no name, path or title.
