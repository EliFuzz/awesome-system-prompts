# Memory System: CLAUDE.md

Claude Code utilizes a file-based memory system centered around a `CLAUDE.md` file located in the current working directory. If this file exists, it is automatically added to the agent's context for every interaction.

## Purpose of `CLAUDE.md`

This file serves three primary purposes:

1. **Command Storage:** It stores frequently used bash commands, such as those for building, testing, and linting the project. This allows the agent to use them without having to search for them each time.
2. **Preference Recording:** It records the user's code style preferences, including naming conventions, preferred libraries, and other stylistic choices.
3. **Codebase Information:** It maintains useful information about the codebase's structure and organization.

## Proactive Memory Updates

The agent is encouraged to be proactive in keeping the `CLAUDE.md` file up to date.

- **Finding Commands:** When the agent spends time searching for commands to perform common tasks (typechecking, linting, building, testing), it should ask the user for permission to add those commands to `CLAUDE.md`.
- **Learning Preferences:** Similarly, when the agent learns about the user's code style preferences or important details about the codebase, it should ask for permission to add that information to `CLAUDE.md` to remember it for the future.
