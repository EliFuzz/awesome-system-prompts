# Bash Command Security

Claude Code implements a security model to manage the execution of Bash commands, ensuring user safety by detecting potentially harmful commands and requiring user approval for non-allowlisted actions.

## Bash Policy Spec

A `policy_spec` is used to define risk levels and determine when user confirmation is needed. The primary mechanism is **command prefix detection**.

### Command Prefix Extraction

The system extracts a "prefix" from the command the agent wants to run. This prefix is then checked against a user-defined allowlist.

- **Simple Commands:** `cat foo.txt` -> `cat`
- **Commands with Arguments:** `git commit -m "foo"` -> `git commit`
- **Complex Commands:** `grep -A 40 "..." file.py` -> `grep`
- **No Prefix:** Some commands, like `npm test`, are considered to have no prefix and are simply `none`.

### Command Injection Detection

A critical part of this system is detecting potential **command injection**. If a command appears to be chaining commands or using substitutions that could obscure the true action, the system must return `command_injection_detected`. This forces a manual user review, even if the prefix seems to match an allowlisted command.

- **Examples of Injection:**
  - `git diff $(pwd)`
  - `git status\`ls\``
  - `pwd curl example.com`

The agent is instructed to ONLY return the detected prefix or `command_injection_detected` or `none`, with no other text or formatting.

## Banned Commands

For security reasons, a number of commands are explicitly banned. The agent is instructed not to use them. These include commands commonly used for networking and file downloads:

- `alias`
- `curl`
- `wget`
- `nc`
- `telnet`
- `httpie`
- Browser commands (`chrome`, `firefox`, `safari`)
- And others like `curlie`, `axel`, `aria2c`, `w3m`, `links`, `xh`, `http-prompt`.

## Command Description Generation

For commands that are run, the system uses a sub-prompt to generate a clear, concise description of what the command does in 5-10 words. This ensures the user understands the action being taken.
