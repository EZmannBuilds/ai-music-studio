# Prompt template

What the command adapter sends to an agent for each case. It is kept in a file, not in code, so that
anyone can see exactly what the studio was asked, and so that a change to the wording is a visible,
reviewable change. The text below the marker is sent, with `{pack_path}`, `{context}` and `{brief}`
filled in.

Two things are deliberate:

- **The brief is sent as the user would write it.** The prompt does not tell the agent what the test
  is looking for; a studio that behaves well only when told the grading criteria has not been tested.
- **The session trace is requested**, because routing and material preservation cannot be checked
  from prose alone. The trace is defined in `shared/SPECIALIST_HANDOFF_SCHEMA.md` and the Director
  writes it only when asked.

<!-- template -->
You are working with the AI Music Studio skill pack at {pack_path}. Read
{pack_path}/music-director/SKILL.md and follow it as the Music Director. Paths inside the pack are
relative to {pack_path}. No user profile is set, so use the pack's defaults. There is no DAW
connection and no audio analyzer in this session: work in text, and write any structured record the
pack defines (a performance plan, a track DNA row, a tuning export) as a fenced yaml block.

Material the user supplied:

{context}

The user's request:

{brief}

At the end of your reply, add the session trace defined in
{pack_path}/shared/SPECIALIST_HANDOFF_SCHEMA.md, as a fenced yaml block.
