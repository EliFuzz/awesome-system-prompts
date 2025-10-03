## General Tool Usage Policy

- **Parallel Calls:** If the agent intends to call multiple tools and there are no data dependencies between them, it should make all the independent calls within the same `function_calls` block.
- **Prefer Agent Tools for File Search:** When searching for files, the agent should prefer using its own integrated tools to reduce context usage.

## Tool-Specific Prompts

The system uses specific prompts to guide the agent's behavior for certain tasks.

### Tool Usage Prompt for Agent

This prompt is used when the agent needs to select a tool to answer a user's question.

- **Goal:** Use the available tools to answer the user's prompt.
- **Key Instructions:**
  - Be concise, direct, and to the point. Avoid elaboration, explanations, introductions, or conclusions. One-word answers are best.
  - Share relevant file names and code snippets.
  - All file paths in the final response **must** be absolute.
- **Environment Details:** The prompt includes context about the environment, such as the working directory, git status, platform, date, and model name.

### Extract File Paths from Command Output

This prompt is used to parse the output of a command and extract any file paths that were read or modified.

- **Goal:** Extract file paths from the command's output.
- **Rules:**
  - Use paths verbatim; do not add slashes or try to resolve them.
  - Do not infer paths that were not explicitly listed.
  - The response must be formatted with `<filepaths>` tags, even if it's empty.
  - No other text should be included in the response.
