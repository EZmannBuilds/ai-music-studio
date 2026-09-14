# File Naming System
## Version 1.0

Every file and folder the studio creates follows this system, so a person or an agent can tell
what a file is, which song it belongs to, which version it is and whether it is the approved one
without opening it.

Where the user's profile (`shared/USER_PROFILE_SCHEMA.md`) sets a naming override, the override
wins. Otherwise this page is the rule.

## 1. Principles

- **Readable first.** A name says what the file is in plain words.
- **Portable.** Use only letters, digits, spaces, hyphens, underscores, parentheses and a single
  period before the extension. Never use `/ \ : * ? " < > |`, emoji, leading or trailing spaces,
  or two spaces in a row. Keep a name to 100 characters or fewer.
- **One song, one folder.** Everything about a song lives in its folder.
- **Versions are always visible.** Every derived artifact carries `v<N>`, counting 1, 2, 3 per
  artifact line with no leading zeros. The version never lives only in a folder name.
- **`FINAL` means approved.** The word appears only on the file the user is meant to hear or
  send, and there is at most one `FINAL` per song per mode.
- **Dates only where time matters.** Logs and journals start with an ISO date,
  `YYYY-MM-DD - <Subject>`. Song artifacts do not carry dates, because versions order them.
- **Source names survive.** Files that come from an outside generator or collaborator keep their
  names until the user approves a rename (§6).

## 2. Tokens

| Token | Meaning | Form |
| --- | --- | --- |
| `<Song>` | the song's title | Title Case with spaces: `Paper Moons`. No genre, track count or tool in the title |
| `<Artifact>` | what the file is | one term from §3 |
| `<Mode>` | which version of the arrangement | `Vocal`, `Instrumental`, `Vocal Guide`, `A Cappella`, `TV`, or a profile-defined mode. The Director's deliverable modes map as `full_with_vocal` → `Vocal`, `vocal_guide` → `Vocal Guide`, `instrumental` → `Instrumental` |
| `<Variant>` | a second build of the same mode with different instruments | one or two words naming what differs: `Stock`, `Orchestral Library`. Only used once a mode has been built more than one way |
| `<Part>` | one track or instrument | the track's name, as in the session: `Bass`, `Violin I`, `Lead Vocal` |
| `<Tool>` | the program a session belongs to | `Ableton`, `Logic`, `FL Studio`, `Pro Tools`, ... |
| `v<N>` | the version of that artifact | `v1`, `v2`, ... |

## 3. Artifact terms

| Term | What it names | Extension |
| --- | --- | --- |
| `MIDI` | the song's multitrack MIDI | `.mid` |
| `Lyrics` | the lyric sheet | `.txt` or `.md` |
| `Lyric Alignment` | syllable-to-note map | `.json` |
| `Production Notes` | the brief and production decisions | `.md` or `.txt` |
| `Track State` | the shared track state (`shared/TRACK_STATE_SCHEMA.md`) | `.json` |
| `Session` | a DAW project | the DAW's own |
| `Mix` | a full render of one pass | `.wav` (masters), `.mp3` (listening copies) |
| `Stem` | one part's render | `.wav` |
| `Analysis` | an analyzer's report on a render | the analyzer's own suffixes |
| `Verification` | the per-track check (`shared/RENDER_VERIFICATION.md`) | `.json` or `.md` |
| `Variety Report` | the melody-variety gate result, when stored alone | `.json` |
| `Calibration` | a plugin calibration profile (`shared/PLUGIN_CALIBRATION_SCHEMA.md`) | `.json` |
| `Plan` | what a pass sets out to build | `.json` |
| `Build Map` | which track, device and part a session built | `.json` |
| `Rename Map` | old name to new name, for every file renamed (§6) | `.json` |

**A document with no term above** (a review, a brief, a set of notes) takes a short description
in Title Case: `<Song> - Fresh Ear Review.md`, `<Song> - Visual Era Brief.txt`. Add `v<N>` when it
belongs to one version only: `<Song> - Mix Notes v2.txt`.

## 4. Patterns

```text
<output root>/<generation type>/<genre>/<Song>/                         song folder
  <Song> - MIDI v<N>.mid
  <Song> - Lyrics v<N>.txt
  <Song> - Lyric Alignment v<N>.json
  <Song> - Production Notes.md
  <Song> - Track State v<N>.json
  <Song> - FINAL <Mode> (v<N>).mp3                                       the approved file, at the top
  Notes/                                                                 notes about the whole song
    <Song> - Rename Map.json
  <Song> - <Tool> Session/                                               one DAW project folder
    <Song> - <Tool> Session <Mode>.<ext>                                  one session per mode
    Exports/
      <Song> - Mix <Mode> v<N>.wav                                       every pass
      <Song> - Mix <Mode> v<N> Stems/
        <Song> - Stem - <Part> v<N>.wav
      <Song> - FINAL <Mode> (v<N>) - superseded.mp3                      earlier finals, kept
    Analysis/
      <Song> - Mix <Mode> v<N>.<analyzer suffix>
      <Song> - Verification <Mode> v<N>.json
    Notes/
      <Song> - Plan <Mode> v1.json                                        what the first pass built
      <Song> - Pass <Mode> v<N> Changes.json                              what each later pass changed
      <Song> - Build Map <Mode>.json
```

Rules that go with the patterns:

- **The generation type folder** is how the song was made, for example
  `DAW Generated/` for multitrack MIDI built in a DAW and `<Service> Generated/` for audio
  from a generation service. **Genre folders** sit inside it. The user's profile lists both.
- **A song that names two genres** files under the first one it names.
- **Experiments with no genre** sit directly in their generation type folder when the profile
  marks that type `genre_folders: false`.
- **When a mode is the only one**, it may be left out of session, mix, final and note names.
  Once a second mode exists, both carry their mode.
- **A second build of the same mode** gets a variant word after the mode, on its session, mixes,
  finals and notes: `Paper Moons - Ableton Session Instrumental Stock.als`,
  `Paper Moons - Mix Instrumental Strings v3.wav`. The variant's passes count from v1.
- **A Logic project is a package**, so the package itself is the session:
  `<Song> - Logic Session.logicx`.
- **Files the DAW manages keep the DAW's names:** Live's `Backup/`, `Ableton Project Info/` and
  `Samples/`, everything inside a Logic package, and a folder's `Icon` file.
- **Versions count per artifact line.** Lyrics v2 does not force MIDI v2. The track state
  records which versions belong together.
- **Superseding a final.** Move the old final into `Exports/` with `- superseded` added, then
  write the new `FINAL`. Nothing is deleted.
- **Calibration profiles** go where the profile's `calibration_store` says:
  `<Plugin> - <Edition> - <Preset> - Calibration v<N>.json`.

## 5. Examples

```text
DAW Generated/Pop/Paper Moons/
  Paper Moons - MIDI v2.mid
  Paper Moons - Lyrics v2.txt
  Paper Moons - Lyric Alignment v2.json
  Paper Moons - FINAL Instrumental (v4).mp3
  Paper Moons - Ableton Session/
    Paper Moons - Ableton Session Vocal.als
    Paper Moons - Ableton Session Instrumental.als
    Exports/Paper Moons - Mix Instrumental v4.wav
    Exports/Paper Moons - Mix Instrumental v4 Stems/Paper Moons - Stem - Bass v4.wav
    Analysis/Paper Moons - Verification Instrumental v4.json
```

## 6. Files that arrive with other names

- Keep the original name and record what it is in the track state, until the user approves a
  rename.
- **A rename is recorded as a map, old name to new name, in `Notes/<Song> - Rename Map.json` at
  the top of the song folder**, so every earlier reference can still be followed. Files that
  mention an old name inside them are left as they are; the map is how a reader follows them.
- DAW sessions, and anything they point to, are renamed from inside the DAW (Save As), or
  together with every file the session references, and re-opened afterwards to prove nothing is
  missing.

## 7. Checking a name

A name passes when:

1. it matches one pattern in §4, or a profile override;
2. it uses only the characters in §1 and is 100 characters or fewer;
3. it carries `v<N>` if it is a derived artifact;
4. `FINAL` appears on at most one file per song and mode.
