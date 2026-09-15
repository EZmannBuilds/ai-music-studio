"""Command adapter: run any agent that takes a prompt and prints a reply.

The command is given with --cmd and is run once per trial (and once per brief in a batch case). The
prompt goes to the command's standard input, and the reply is read from its standard output. If the
command contains {prompt_file}, the prompt is written to a file and the path substituted instead.

Nothing here knows about any particular model or vendor. evals/runners/examples/COMMAND_TEMPLATES.md
shows how some agent command-line tools can be called this way; none of them is required, and an
agent that cannot be driven from a command line can be graded with the manual adapter instead.

Every reply is saved under the run's output folder, so a run can be re-graded later with
`--adapter manual --responses <run>/responses`.
"""
import os, shlex, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT_TEMPLATE = os.path.join(HERE, '..', 'PROMPT_TEMPLATE.md')


def build_prompt(case, brief, fixtures_dir, pack_path):
    tpl = open(PROMPT_TEMPLATE, encoding='utf-8').read()
    tpl = tpl.split('<!-- template -->', 1)[1].strip()
    context = []
    for rel in case.get('supplied_context', []):
        path = os.path.join(fixtures_dir, rel)
        body = open(path, encoding='utf-8', errors='replace').read()
        context.append(f'File supplied by the user: {os.path.basename(rel)}\n\n```text\n{body.rstrip()}\n```')
    return (tpl.replace('{pack_path}', pack_path)
               .replace('{context}', '\n\n'.join(context) if context else '(none)')
               .replace('{brief}', brief.strip()))


def run(cmd, prompt, timeout, cwd=None):
    if '{prompt_file}' in cmd:
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(prompt)
            path = f.name
        try:
            proc = subprocess.run(cmd.replace('{prompt_file}', shlex.quote(path)), shell=True,
                                  capture_output=True, text=True, timeout=timeout, cwd=cwd)
        finally:
            os.unlink(path)
    else:
        proc = subprocess.run(cmd, shell=True, input=prompt, capture_output=True, text=True,
                              timeout=timeout, cwd=cwd)
    if proc.returncode != 0:
        raise RuntimeError(f'command exited {proc.returncode}: {proc.stderr.strip()[:300]}')
    return proc.stdout


def responses_for(case, opts, save_dir):
    """Run the case and return responses in the manual adapter's shape."""
    fixtures = opts['fixtures_dir']
    out_base = os.path.join(save_dir, case['id'])
    os.makedirs(out_base, exist_ok=True)
    trials = opts['trials'] or case.get('trials', 3)
    if case.get('batch'):
        sets = []
        for t in range(1, trials + 1):
            set_dir = os.path.join(out_base, f'trial-{t}')
            os.makedirs(set_dir, exist_ok=True)
            replies = []
            for i, brief in enumerate(case['batch']['briefs'], 1):
                reply = run(opts['cmd'], build_prompt(case, brief, fixtures, opts['pack_path']),
                            opts['timeout'], opts.get('cwd'))
                open(os.path.join(set_dir, f'{i:02d}.md'), 'w', encoding='utf-8').write(reply)
                replies.append(reply)
            sets.append(replies)
        return sets
    replies = []
    for t in range(1, trials + 1):
        reply = run(opts['cmd'], build_prompt(case, case['brief'], fixtures, opts['pack_path']),
                    opts['timeout'], opts.get('cwd'))
        open(os.path.join(out_base, f'trial-{t}.md'), 'w', encoding='utf-8').write(reply)
        replies.append(reply)
    return replies
