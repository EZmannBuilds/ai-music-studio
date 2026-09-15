# Command templates

The command adapter runs any agent that reads a prompt and prints a reply. These are examples of how
a few command-line agents can be called that way. **None is required, none is endorsed, and nothing
in the harness depends on any of them.** Flags change between versions: check your tool's own help
before relying on a line here.

The prompt arrives on standard input, unless the command contains `{prompt_file}`, in which case the
prompt is written to a temporary file and its path substituted.

```bash
# An agent CLI with a non-interactive "print" mode that reads the prompt from standard input
python3 evals/runners/run_evals.py --adapter command --cmd "claude -p" --only D16,D18,N1-C

# An agent CLI whose non-interactive mode takes the prompt as an argument
python3 evals/runners/run_evals.py --adapter command --cmd 'codex exec "$(cat {prompt_file})"' --only D16

# Any OpenAI-compatible HTTP endpoint, through a small script of your own that reads standard input
# and prints the reply
python3 evals/runners/run_evals.py --adapter command --cmd "python3 my_endpoint_client.py" --trials 3
```

The agent must be able to read the pack's files. Run it from the repository root, or give the pack's
location with `--pack-path`, which is written into the prompt (`evals/runners/PROMPT_TEMPLATE.md`).

An agent that cannot be driven from a command line is still testable: send it the prompt yourself,
save each reply as `<responses>/<CASE_ID>/trial-1.md`, and run
`python3 evals/runners/run_evals.py --adapter manual --responses <responses>`.

**Cost.** A full run is 41 cases, most at three trials, and the batch cases B1 to B3 are ten
sessions per trial. Start with `--only` and one or two cases.
