# Instrument source register

Every source the instrument pages cite, listed once. A guide page cites a source by its ID; this
register says what the source is and, above all, **how much of it was actually read** for this
pack. The label a claim may carry depends on that (`shared/RESEARCH_RULES.md`): `sourced`,
`academic` and `manual-derived` need `section` or `full`; anything read less is
`standard-reference` at best. `tools/evidence_check.py` holds every page to this table.

| Read depth | Means |
|---|---|
| `full` | the whole work, or the whole of a short work, was read |
| `section` | the part that supports the claim was read |
| `excerpt` | a preview, snippet or quotation elsewhere; not the work itself |
| `abstract` | only the abstract or summary |
| `not-read` | cited by attribution only |

Product names are allowed here, because a manual is a product's manual. They are not allowed in the
guide pages.

A source that could not be reached when it was tried stays in the register with `not-read`, so the
next person knows it was tried. Accessed dates are the date of reading.

## Sources

| id | citation | type | read | url | accessed |
|---|---|---|---|---|---|
| STRINGS-LIBRARY-MANUAL-1 | Spitfire Audio, Spitfire Symphonic Strings User Manual (26 pages; the sections on basic principles, legato, performance legato, articulations, round robins and controls) | manual | section | https://spitfire-www-assets.s3.amazonaws.com/manuals/SpitfireSymphonicStrings_UserManual.pdf | 2026-09-15 |
