# Research: Agentic DAW Integration
## Ableton Live, FL Studio and Pro Tools

## Executive conclusion

All three DAWs can participate in an agentic music-generation pipeline, but they should not share
one fake universal automation model.

### Ableton Live
Best current architecture:
- official Extensions SDK for discrete tools;
- Max for Live / Live Object Model for persistent in-DAW control and custom generators;
- local OSC/MCP bridges for conversational external agents.

### FL Studio
Best current architecture:
- official Piano Roll Scripting for note generation;
- official MIDI Scripting for broader FL integration where supported;
- optional local MCP bridge;
- use Track Mode for deterministic generated projects unless the user explicitly wants free-form routing.

### Pro Tools
Best current architecture:
- PTSL for session/timeline/routing/import/export automation;
- MIDI Builder for exact note generation;
- Sketch/AAX MIDI effects for nonlinear/in-DAW composition;
- SoundFlow for automation gaps and macro/UI workflows.

## Why adapters must be DAW-native

The same request:

> "Create an alternate chorus."

maps differently.

Ableton:
- duplicate a Session clip/Scene or Arrangement clip.

FL Studio:
- duplicate/create Pattern, edit Piano Roll, place Pattern Clip.

Pro Tools:
- create/import MIDI clip, duplicate timeline region, or create a Sketch Scene.

An agent that only knows generic "tracks" will make project-structure mistakes.

## API findings

### Ableton Extensions SDK

Ableton introduced a public-beta JavaScript Extensions SDK in 2026. Extensions can read/edit
set structure including tracks, clips, MIDI, devices, tempo and more.

Its invocation model is currently discrete:
- user invokes Extension;
- Extension runs;
- applies/returns changes;
- stops.

This makes Extensions excellent for:
- generate variation;
- reharmonize selection;
- audit project;
- rename/reorganize;
- transform MIDI.

It is not, by itself, the ideal continuously listening autonomous bridge.

### Ableton Live Object Model / Max for Live

LOM exposes the Live hierarchy including Song, Track, Clip Slot, Clip, Device, parameters,
Scenes, mixer and other objects.

For continuous or embedded agent tools, this remains important.

Live 12 MIDI Tools also formalize generator/transformer behavior around MIDI clips.

### FL Studio MIDI + Piano Roll scripting

FL Studio's official Python surfaces provide unusually useful note-level control.

The Piano Roll scripting API exposes exact note:
- pitch;
- time;
- length;
- velocity;
- pan;
- fine pitch;
- slide/portamento;
- markers.

This is suitable for Composer/MIDI Builder output.

The broader MIDI Scripting API exposes multiple FL Studio domains, but the adapter must respect
its controller/event-oriented architecture and context sensitivity.

### FL structural warning

The Playlist is a container for Pattern, Audio and Automation clips.

By default:
- Playlist Track != Mixer Track.

For generated projects, Track Mode provides a safer semantic mapping:
Instrument Channel ↔ Playlist Track ↔ Mixer Track.

### Pro Tools PTSL

PTSL is a language-independent official API based on inter-process communication using gRPC /
Protocol Buffers.

Its strengths are deterministic project operations rather than being a complete symbolic composer.

A music agent should use PTSL for:
- sessions;
- tracks;
- memory locations;
- timeline;
- queries;
- import/export;
- bounce and related workflow operations supported by the installed SDK.

Exact vocal/instrument MIDI can remain the responsibility of MIDI Builder.

### Pro Tools SoundFlow

Pro Tools 2025.10+ integrates SoundFlow deeply, including a large command catalog and Session
Assistant.

This is relevant because a practical Pro Tools agent can combine:
- structured PTSL calls;
- SoundFlow macros/UI commands.

Do not confuse SoundFlow availability with an unrestricted public note-generation API.

## Third-party MCP projects

Community projects already demonstrate:
- Ableton via AbletonOSC / Remote Scripts;
- FL Studio via scripting bridges;
- Pro Tools via PTSL wrappers.

These prove feasibility but are not the same as official vendor APIs.

Before installation:
- inspect code;
- confirm supported DAW version;
- bind locally;
- back up sessions.

## Architecture

```text
Music intelligence
    |
    +-- Composer
    +-- Arranger
    +-- Producer
    +-- Lyric Generator
    +-- MIDI Builder
    |
DAW Adapter Contract
    |
    +-- Ableton profile
    +-- FL Studio profile
    +-- Pro Tools profile
```

This preserves the core rule:
software execution must not become musical reasoning.

## Source map

Official Ableton:
- https://www.ableton.com/en/blog/introducing-extensions-sdk/
- https://help.ableton.com/hc/en-us/articles/27303428331420-Ableton-Extensions-FAQ
- https://help.ableton.com/hc/en-us/articles/5402681764242-Controlling-Live-using-Max-for-Live
- https://www.ableton.com/en/live-manual/12/midi-tools/

Official FL Studio:
- https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm
- https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/pianoroll_scripting_api.htm
- https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/basics_workflow.htm
- https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/playlist.htm

Official Pro Tools / Avid:
- https://developer.avid.com/scripting/
- https://www.avid.com/resource-center/pro-tools-scripting-sdk
- https://www.avid.com/pro-tools/whats-new
- https://kb.avid.com/pkb/articles/en_US/Knowledge/Pro-Tools-Sketch-Support
- https://soundflow.org/integrations/pro-tools

Selected community bridges, for feasibility reference only:
- https://github.com/ideoforms/AbletonOSC
- https://github.com/bschoepke/ableton-live-mcp
- https://github.com/rosasynthesiz/flstudio-mcp
- https://github.com/iluvcapra/py-ptsl
- https://github.com/skrul/protools-mcp-server
