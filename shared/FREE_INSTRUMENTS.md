# Free Instruments and Plugins
## Version 1.0

A reference for the Plugin Auditor and the Producer: free instruments and effects the studio can
**suggest** when the user's palette lacks something the score needs, and **how an agent can drive
each one**.

**Checked in September 2026, mostly on vendor pages.** Prices, terms and availability change.
Before suggesting anything, check the vendor page again, and say when the entry was last checked.

## Rules

- **Suggest; never install.** The user downloads, installs, signs in, activates and accepts every
  licence. The agent never creates an account, enters credentials, or clicks through a licence.
- **Prefer what an agent can drive.** Suggest a screen-only instrument only when nothing
  drivable fits, and say that it needs the screen.
- **Say what a person has to do** before the agent can use it: the "Needs a person" column.
- **Licences for released music differ.** Quote the vendor's terms where they are stated here;
  where they are not, tell the user to read them before releasing.
- **Record what the user installs** in the plugin audit (`plugin-auditor/SKILL.md`), with its
  `agent_control` block (`shared/PLUGIN_CALIBRATION_SCHEMA.md`).

## How an agent can drive a plugin

| Level | What it means | Examples below |
| --- | --- | --- |
| **Code** | Renders from a MIDI file or a script with no GUI and no person, once installed | SFZ libraries through an SFZ renderer; Surge XT through surgepy; FluidSynth; DrumGizmo |
| **API** | Exposes host-automatable parameters and MIDI; a DAW adapter or a plugin host library can set them and render. May need a person once, to install or activate | BBC SO Discover, Dexed, Vital, the Melda bundle, most effects |
| **Screen** | Needs its own window for a step, such as loading a sound or signing in at every start | Login-gated players; instruments that load silent until a patch is chosen |

### Hosts that let code play a plugin

| Tool | What it does | Licence and OS | Source |
| --- | --- | --- | --- |
| **pedalboard** (Spotify) | Python. Loads VST3 on macOS, Windows and Linux, and AU on macOS. Since 0.7.4 an instrument takes a list of MIDI messages and returns audio. Parameters are Python attributes; `load_preset()` reads `.vstpreset`; `show_editor()` opens the plugin window so a person can sign in or pick a sound | GPLv3 | https://spotify.github.io/pedalboard/ |
| **DawDreamer** | Python. Hosts VST2, VST3 and AU; loads MIDI, sets parameters, loads presets and renders | GPLv3; macOS, Windows, Linux | https://github.com/DBraun/DawDreamer |
| **sfizz_render** | Command line: an SFZ instrument and a MIDI file to a stereo WAV | BSD-2. **The sfizz project was archived in June 2026**; the renderer still works but gets no fixes | https://github.com/sfztools/sfizz-render |
| **surgepy** | Python bindings for Surge XT, built from its source: load patches, set parameters, play notes, render to arrays | GPL-3 | https://github.com/surge-synthesizer/surge |
| **FluidSynth** | Command line: `-F` renders a MIDI file through a SoundFont (SF2) to audio | LGPL-2.1 | https://www.fluidsynth.org/ |
| **DrumGizmo** | Command line: a MIDI file to one WAV per drum microphone, through an XML note map | LGPLv3 | https://drumgizmo.org/ |

**Tested with pedalboard 0.9.17 on macOS, September 2026:** BBC SO Discover (VST3) loaded
headlessly, exposed 45 parameters and played a test note. Several instruments loaded but made no
sound until a patch was chosen in their window (SampleTank 4, Analog Lab, Cymatics Pandora).
Vital's VST3 failed to scan and its AU hung, and an iLok-protected effect would not load. Plan
for those through the DAW instead.

## Orchestra

| Instrument | What it holds | Free terms · Needs a person | Formats | Agent control | Source |
| --- | --- | --- | --- | --- | --- |
| **BBC Symphony Orchestra Discover** (Spitfire Audio) | Full-orchestra sections plus piano, harp, celeste and percussion; 47 techniques; one mix signal; about 240 MB. Sources give 33 to 35 instruments | Free for Spitfire email subscribers · Spitfire account, Spitfire Audio app, authorisation | VST3, AU, AAX (no VST2); macOS 11–15, Windows 10/11 | **API.** CC1 Dynamics, CC11 Expression, CC7 gain, CC19 reverb; keyswitches. Discover has **one dynamic layer**, so Dynamics works like a second volume control. Tested headless: 45 parameters, renders | https://www.spitfireaudio.com/en-us/products/bbc-symphony-orchestra-discover |
| **Spitfire Symphony Orchestra Discover** (Spitfire Audio, 2025) | 44 instruments, 74 techniques, 3 legatos, 11 solos, including cor anglais and bass clarinet; 5.68 GB | Free for email subscribers · Spitfire account, app, Native Access serial | Kontakt Player 7.5.2+ (VST3, AU, AAX, standalone) | **API** through Kontakt Player; CC map unverified | https://www.spitfireaudio.com/en-us/products/spitfire-symphony-orchestra-discover |
| **Berlin Free Orchestra, SINEfactory, Layers** (Orchestral Tools) | Solos and ensembles from the Berlin series; SINEfactory's 15 instruments include choir, pianos, organs, strings, guitars, basses and drums | Free once added to an account · account, SINE login and activation | SINE Player: VST, VST3, AU, AAX, standalone | **Screen** first (login-gated), then MIDI and keyswitches; host automation undocumented | https://www.orchestraltools.com/free-virtual-instruments |
| **The Free Orchestra 1 and 2** (ProjectSAM) | Cinematic strings, horns, choir, winds and hits; 1.8 GB and 8.6 GB | Free · account, Native Access. Commercial use in music allowed | Kontakt Player | **API** through Kontakt Player | https://projectsam.com/libraries/the-free-orchestra |
| **VSCO 2 Community Edition** (Versilian Studios) | Chamber orchestra: strings, woodwinds, brass, timpani, harp, organ, piano, mallets; about 3 GB | Free, no sign-up · **CC0**: no restrictions, no credit needed | SFZ and WAV | **Code.** Plain-text SFZ; renders with an SFZ renderer; nothing needs a person | https://github.com/sgossner/VSCO-2-CE |
| **Virtual Playing Orchestra 3** (Paul Battersby) | Strings, solo violin, woodwinds including English horn, brass, timpani; 603 MB | Free · music use unrestricted; source samples keep their own CC licences | SFZ | **Code.** "Performance" patches: CC1 volume, velocity picks articulation | http://virtualplaying.com/virtual-playing-orchestra/ |
| **Sonatina Symphonic Orchestra 4** | Solo and ensemble strings with many articulations, brass, woodwinds, percussion, piano, harp, organ | Free · CC Sampling Plus 1.0: commercial use of the sounds allowed | SFZ | **Code.** CC1 volume or attack by mode; CC21 string vibrato | https://github.com/peastman/sso |

**What BBC SO Discover lacks,** from its manual: solo players except piccolo and tuba; cor
anglais; alto and bass flute; bass clarinet; contrabassoon; cimbasso and contrabass brass;
legato; choir; saxophones; separate microphones. Score those parts on the nearest section and
name the substitution in the track, or use Spitfire Symphony Orchestra Discover or Virtual
Playing Orchestra for them.

**In Ableton Live,** CC1 written as clip envelopes may not reach the BBC SO VST3. Automate the
plugin's own Dynamics and Expression parameters instead (`daw-adapters/ABLETON_LIVE.md`).

## Players and multi-instrument bundles

| Player or bundle | What it holds | Free terms · Needs a person | Formats | Agent control | Source |
| --- | --- | --- | --- | --- | --- |
| **Komplete Start / Kontakt Player** (Native Instruments) | Kontakt Player, Massive X Player, Leap, a factory selection with synths, drums, band instruments and choirs | Free · NI account, Native Access, activation | Standalone, VST3, AU (macOS), AAX | **API**, but each knob must be assigned to a host slot in the Automation tab, a screen step; `.nki` is proprietary | https://www.native-instruments.com/products/komplete-start |
| **Splice INSTRUMENT, free plan** (successor to Spitfire LABS) | 500+ free presets including the LABS packs, plus monthly free drops | Free tier · Splice account; **sign-in at every start** | VST3, AU, AAX, standalone | **Screen** to start (login), then **API**: host-automatable Dynamics (CC1), Expression and macros | https://splice.com/instrument |
| **Soundpaint free engine** (8Dio) | Two grand pianos, guitars, percussion and ambiences | Free · account, sign-in | VST2, VST3, AU, AAX, standalone | **Screen** (login); host automation unverified | https://soundpaint.com/pages/free-engine |
| **Heavyocity Foundations** | Piano, nylon guitar, emotive choir, synth bass, staccato strings and brass | Free · Native Access | Kontakt Player | **API** through Kontakt Player | https://heavyocity.com/collections/foundations |
| **Plogue sforzando** | The maintained free SFZ player | Free, direct download | VST3, AU, AAX, CLAP, standalone; macOS, Windows, Linux beta | **API.** SFZ-defined CCs appear as controls; offline render only in its GUI | https://www.plogue.com/products/sforzando.html |
| **Decent Sampler** + **Pianobook** libraries | Free player and a large community library | Player free (vendor page blocked automated checks; confirm); Pianobook needs an account to download, and its terms limit use to your own new recordings | VST, VST3, AU, AAX, standalone; macOS, Windows, Linux | **API/Code.** `.dspreset` files are XML a script can write; no command-line renderer. Pianobook's Kontakt packs need full Kontakt | https://www.decentsamples.com/product/decent-sampler-plugin/ |
| **HALion Sonic, free** (Steinberg) | The player; free content list unverified | Free · Steinberg account, Activation Manager | VST3, AU, AAX, standalone | **API** through its Automation page | https://www.steinberg.net/vst-instruments/halion/sonic/ |
| **SampleTank 4 CS** (IK Multimedia) | Free edition, 50 instruments | Free · IK account, IK Product Manager | Unverified for the free edition | **Screen** then **API**: loaded silent in a headless test until an instrument was chosen; the tested installation exposed 1,601 host parameters | https://www.ikmultimedia.com/products/st4cs/ |
| **Analog Lab Play** (Arturia) | Free edition, 100 sounds | Free · account (steps unverified) | Unverified for the free edition | **Screen** then **API**: loaded silent in a headless test until a sound was chosen; the tested installation exposed 547 host parameters | https://www.arturia.com/products/software-instruments/analoglab/free |

## Pianos, choirs, guitar and bass

| Instrument | What it holds | Free terms · Needs a person | Agent control | Source |
| --- | --- | --- | --- | --- |
| **Salamander Grand Piano V3** | Yamaha C5, 16 velocity layers | Free · **CC BY 3.0: credit required** | **Code.** SFZ and SF2; its SFZ uses player extensions, so render it in an ARIA-based player for fidelity | https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html |
| **Upright Piano KW** | Kawai upright, 2 layers | Free · **CC0** | **Code.** SFZ and SF2 | https://github.com/freepats/upright-piano-KW |
| **Free choirs** | OT Manifold (SINEfactory), NI Jacob Collier Audience Choir, Heavyocity Emotive Choir, ProjectSAM Luminous Choir | See each vendor above | API through their players, after a person installs them. **No free SFZ choir was found** | vendor pages above |
| **Ample Guitar M Lite v4, Ample Bass P Lite v4** | Martin D-41 acoustic; Precision bass | $0 through third-party stores · store account, activation | **API.** Keyswitches (C0 sustain, D0 palm mute, E0 slide, F0 hammer-on); most controls MIDI-learnable | https://www.amplesound.net/en/download.asp |
| **Shreddage 3 Stratus FREE** (Impact Soundworks) | Electric guitar | Free through checkout · Kontakt Player 6.7+; activation unverified | API through Kontakt Player | https://impactsoundworks.com/product/shreddage-3-stratus-free-kp/ |

## Synths

| Synth | Free terms · Needs a person | Formats | Agent control | Source |
| --- | --- | --- | --- | --- |
| **Surge XT** | Free, GPL-3, no account | Standalone, VST3, CLAP, AU (macOS), LV2 (Linux) | **Code.** Patches are XML inside `.fxp`; any parameter automatable or MIDI-learnable; **surgepy** renders with no DAW | https://surge-synthesizer.github.io/ |
| **Vital, Basic tier** | Free full synth with 75 presets · account to download. The free presets may not be redistributed | VST, VST3, AU, LV2 | **API.** Every control is a host parameter; **`.vital` presets are JSON** a script can write. Did not load in pedalboard; drive it through the DAW | https://vital.audio/ |
| **Dexed** | Free, GPL-3, no account | VST3, AU, CLAP, standalone | **Code.** 144 automatable DX7 parameters; `.syx` cartridges are a documented binary a script can write | https://github.com/asb2m10/dexed |
| **u-he TyrellN6** | Free, no serial; current download is a 2025 beta | CLAP, AU, VST3, AAX | **API.** CC1, CC2, CC11 by default; MIDI learn; `.h2p` presets are mostly text | https://u-he.com/products/tyrelln6/ |
| **u-he Podolski** | Free, no serial | AU, VST3, AAX (no CLAP) | **API.** MIDI Learn page; `.h2p` presets | https://u-he.com/products/podolski/ |
| **TAL-NoiseMaker** | Free, no account | VST, VST3, AU, AAX | **API.** MIDI learn for all knobs; host automation unverified | https://tal-software.com/products/tal-noisemaker |
| **Odin 2** | Free, GPLv3 | VST3, CLAP, AU, LV2 | **API.** Parameters marked automatable in its manual | https://thewavewarden.com/odin2 |
| **Cymatics Pandora** | $0 listing (launched as a giveaway; soundbanks are paid) · email sign-up | VST3, AU | **Screen:** loaded silent in a headless test | https://cymatics.fm/collections/vault-plugins |

## Drums

| Kit | Free terms · Needs a person | Agent control | Source |
| --- | --- | --- | --- |
| **MT Power Drum Kit 2** | Free, donation optional | **API.** Note map with MIDI learn; `.PDKmap` presets | https://www.powerdrumkit.com/ |
| **Steven Slate Drums 5.5 Free** | Free, never-expiring edition · Slate account and Audio Center app | **API.** Multi-output; note map with MIDI learn | https://stevenslatedrums.com/ssd5/free |
| **DrumGizmo** with CrocellKit or DRSKit | Free, LGPLv3 · kits are **CC BY 4.0: credit required** | **Code.** XML note maps; official command-line renderer | https://drumgizmo.org/ |

## General MIDI and notation fallbacks

| Tool | Use | Agent control | Source |
| --- | --- | --- | --- |
| **FluidSynth + GeneralUser GS** | A General MIDI sketch of any song; 261 presets and 13 kits; free for any music, commercial included | **Code.** `fluidsynth -F out.wav bank.sf2 song.mid` | https://github.com/mrbumpy409/GeneralUser-GS |
| **MuseScore Studio + Muse Sounds** | Notation playback with free sampled sounds; not a DAW plugin | **Code**, partly: `-o` exports audio without the GUI; command-line export with Muse Sounds has broken before | https://handbook.musescore.org/appendix/command-line-usage |

## Free effects and utilities

| Plugin | What it is | Needs a person | Agent control |
| --- | --- | --- | --- |
| **MeldaProduction MFreeFXBundle** | 38 effects and meters: EQ, compressor, saturator, stereo expander, loudness analyzer, utility and more | Melda account in the installer | **API.** Tested headless: parameters exposed (e.g. MEqualizer 55, MUtility 50). Preset files are undocumented; set parameters instead |
| **iZotope Ozone Imager 2** | Stereo width: Width, Stereoize, Time | iZotope account, activation | **API.** Tested headless: 4 parameters |
| **Cymatics Deja Vu, Diablo Lite, Memory, Origin** | Free effects | Email sign-up | **API.** Tested headless: 10 to 16 parameters each |
| **osci-render** (free edition) | Oscilloscope-music effect | None for the GitHub build | **API.** Tested headless: 720 parameters; `.osci` projects are XML |
| **Softube Saturation Knob** | One-knob saturation | Softube account, Softube Central, iLok | **Screen/API through a DAW only**: would not load in a headless host |

## No longer free, or no longer maintained

| Plugin | Status |
| --- | --- |
| **Spitfire LABS** | Winding down: no new content, updates, support or new installs after 2026-10-31. Use Splice INSTRUMENT's free plan |
| **Keyzone Classic** | Now paid (Keyzone Classic 4) |
| **Helm** | Repository archived February 2025 |
| **sfizz** (the player) | Archived June 2026; use sforzando as the player. `sfizz_render` still works |
| **NoiseWorks DynAssist** | Discontinued April 2026 |
| **Pianobook Kontakt packs** | Need full Kontakt; in the free Kontakt Player they run as a 15-minute demo |
