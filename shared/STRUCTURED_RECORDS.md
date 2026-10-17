# Structured Records Extension
## Version 1.0 (optional, additive)

The human-facing instructions remain in Markdown. Runtime records may be saved as YAML or JSON; machines validate JSON documents against `schemas/analysis_finding.schema.json` and `schemas/decision_event.schema.json`. The validator is `tools/validate_records.py` (stdlib only). These schemas describe **new optional records**; do not require existing YAML track/project states to conform or migrate them blindly.

## Observations to verified revisions

Use `analysis_finding` to preserve the chain: reported observation, measured/listened/inferred basis, original artifact and render, possible cause, creative intervention, user approval, replacement render, and recheck. Do not label an inference a measurement. Never claim a fix was verified without a new render or a real listening comparison. An analyzer is optional. Follow `shared/MIX_FEEDBACK_PROTOCOL.md` and its upstream-first rule. A `recheck` marked improved is not automatically approved by the user.

## Decision events

`decision_event` augments, never replaces, `project_state.decision_log` (and never renames its old keys). Add an event only when persistent auditability is useful. Existing decision entries remain valid. Events are ordered, append-only; supersession adds a *new* event that references the prior event id. An agent cannot silently change `approved_by` to `user`: record explicit user approval or leave it unapproved. Keep events within project scope; never import unrelated track decisions. Event ids must be unique within a project.

## File conventions

Keep these records beside project state in project-specific locations, respecting profile paths and privacy boundaries. Never export private user music or analysis to the public skill repository. `schemas/` holds formats only; `examples/` contains fictional demonstrations. No database server is necessary.
