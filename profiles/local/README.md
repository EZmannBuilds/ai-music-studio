# Local profiles

**Your profile goes here**, and nothing in this folder reaches a repository: `.gitignore` excludes
`profiles/local/` except for this page.

```bash
cp profiles/user-profile.example.yaml profiles/local/<your-name>.yaml
```

Then fill in what you know and leave the rest empty. The schema, and which specialist reads which
key, is in `shared/USER_PROFILE_SCHEMA.md`.

You can keep the file anywhere else instead. This folder exists so that the default location the
Music Director looks in is a real path rather than a suggestion, and so that a fresh clone does not
begin by pointing at something that is not there.
