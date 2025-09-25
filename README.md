# Awesome System Prompts [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

An opinionated list of awesome system prompts from various AI models.

## LLMs

### [Aider](https://www.aider.ai): AI-powered coding assistant that helps developers modify codebases efficiently through natural language prompts and context-aware code changes

- [Architect Mode](docs/assets/aider/architect-mode.md): outlining how an AI acts as an expert architect engineer to provide clear, concise, and change-focused instructions to an "editor engineer" for modifying code within a git repository
- [Ask Mode](docs/assets/aider/ask-mode.md): as an expert code analyst AI, detailing its read-only nature for code analysis and question answering, its emphasis on brief responses, and its capability to request additional files for analysis.
- [File Mode](docs/assets/aider/file-mode.md): "file listing" format for an AI assistant, which involves returning the entire content of a file (either existing or new) within a specific fenced code block structure to propose code changes.
- [Patch Mode](docs/assets/aider/patch-mode.md): "V4A Diff Format Rules" used by an expert software developer agent, detailing how it should propose code changes, create new files, and refactor existing ones using a unified patch format with context-aware diffs for Add, Update, and Delete operations.
- [System Prompt](docs/assets/aider/system-prompt.md): AI software developer coding best practices, interaction rules, and the precise `SEARCH/REPLACE` block format for code modifications.
- [Udiff Mode](docs/assets/aider/udiff-mode.md): "udiff-mode" system prompt for an AI assistant, which instructs the assistant to output code changes in a unified diff format similar to `diff -U0`.

### [Alan](https://alan.estsoft.ai/): AI assistant developed by ESTsoft that provides advanced conversational and productivity features for users and businesses

- [Prompt](docs/assets/alan/prompt.md): outlines the detailed rules and limitations for "Alan Assistant" (also known as "Gepeto"), covering its response characteristics, information gathering capabilities, output formatting, and content generation restrictions.

### [Augment Code](https://www.augmentcode.com): AI-powered coding assistant platform that leverages advanced agentic models and tool integrations to help developers efficiently analyze, edit, and manage codebases

- [Agent GPT-5](docs/assets/augment/agent-gpt-5.md): outlines the role, identity, output formatting, preliminary tasks, information-gathering tools, planning and task management, editing guidelines, package management, instruction following, testing, execution and validation, code display, communication, recovery from difficulties, cost balancing, final workflow, and success criteria for the Augment Agent, an agentic coding AI assistant based on GPT 5.
- [Agent Sonnet 4](docs/assets/augment/agent-sonnet-4.md): outlines the role, identity, preliminary tasks, planning and task management guidelines, editing instructions, package management rules, and general instructions for Augment Agent, an AI assistant based on Claude Sonnet 4.
- [Tools GPT-5](docs/assets/augment/tools-gpt-5.json): defines a collection of tools, including functions for file and directory viewing, searching, editing, process management, diagnostics, browser interaction, web search and fetch, task list management, and memory storage, each with specified parameters and descriptions.
- [Tools Sonnet 4](docs/assets/augment/tools-sonnet-4.json): defines a collection of tools, including a file editor (`str-replace-editor`), a browser opener (`open-browser`), a diagnostics tool, terminal interaction tools, Git commit retrieval, web search, web fetch, codebase retrieval, file removal, file saving, and task management tools, each with specific parameters and descriptions for their usage.
- [Tools](docs/assets/augment/tools.json): describes a set of tools and various prompt templates for an Augment AI coding assistant.

### [Blackbox.AI](https://www.blackbox.ai)

- [Template 1](docs/assets/blackbox/agent-template-1.md)
- [Template 2](docs/assets/blackbox/agent-template-2.md)
- [Template 3](docs/assets/blackbox/agent-template-3.md)
- [Template 4](docs/assets/blackbox/agent-template-4.md)
- [Template 5](docs/assets/blackbox/agent-template-5.md)
- [Template 6](docs/assets/blackbox/agent-template-6.md)
- [Template 7](docs/assets/blackbox/agent-template-7.md)
- [Template 8](docs/assets/blackbox/agent-template-8.md)
- [Template 9](docs/assets/blackbox/agent-template-9.md)
- [Template 10](docs/assets/blackbox/agent-template-10.md)
- [Template 11](docs/assets/blackbox/agent-template-11.md)
- [Template 12](docs/assets/blackbox/agent-template-12.md)
- [Template 13](docs/assets/blackbox/agent-template-13.md)
- [Template 14](docs/assets/blackbox/agent-template-14.md)
- [Template 15](docs/assets/blackbox/agent-template-15.md)
- [Template 16](docs/assets/blackbox/agent-template-16.md)
- [Template 17](docs/assets/blackbox/agent-template-17.md)
- [Template 18](docs/assets/blackbox/agent-template-18.md)
- [Template 19](docs/assets/blackbox/agent-template-19.md)
- [Extract](docs/assets/blackbox/extract.py)
- [Prompt](docs/assets/blackbox/prompt.md)

### [Bolt](https://bolt.new)

- [Prompt 2024-10-09](docs/assets/bolt/prompt-2024_10_09.md)
- [Prompt](docs/assets/bolt/prompt.md)

### [Brave Leo](https://brave.com/leo/)

- [Prompt 2025-09-01](docs/assets/brave/prompt-2025-09-01.md)
- [Prompt 2024-06-01](docs/assets/brave/prompt-2024_06_01.md)

### [Canva](https://www.canva.com)

- [2025-05-19](docs/assets/canva/canva-2025_05_19.md)

### [Claude](https://claude.ai)

- [API Tools 2025-01-19](docs/assets/claude/api-tools-2025_01_19.md)
- [Artifacts 2024-06-20](docs/assets/claude/artifacts-2024_06_20.md)
- [Available Tools](docs/assets/claude/available-tools.md)
- [Bash Security](docs/assets/claude/bash-security.md)
- [Citations](docs/assets/claude/citations.md)
- [Claude 4.1 (2025-08-05)](docs/assets/claude/claude-4-1-2025-08-05.md)
- [Claude](docs/assets/claude/claude.md)
- [Copyright Safety](docs/assets/claude/copyright-safety.md)
- [Core Persona](docs/assets/claude/core-persona.md)
- [Guidelines](docs/assets/claude/guidelines.md)
- [Injections](docs/assets/claude/injections.md)
- [Memory](docs/assets/claude/memory.md)
- [Search Reminders](docs/assets/claude/search-reminders.md)
- [Sonnet 3.5 (2024-07-12)](docs/assets/claude/sonnet-3_5-2024_07_12.md)
- [Sonnet 3.5 (2024-09-09)](docs/assets/claude/sonnet-3_5-2024_09_09.md)
- [Sonnet 3.5 (2024-10-22)](docs/assets/claude/sonnet-3_5-2024_10_22.md)
- [Sonnet 3.7 (2025-02-24)](docs/assets/claude/sonnet-3_7-2025_02_24.md)
- [Sonnet 3.7 (2025)](docs/assets/claude/sonnet-3_7-2025.txt)
- [Sonnet 3.7 (Artifacts)](docs/assets/claude/sonnet-3_7-artifacts.md)
- [Sonnet 3.7 (System Message)](docs/assets/claude/sonnet-3_7-system-message.txt)
- [Sonnet 3.7 (Tool Usages)](docs/assets/claude/sonnet-3_7-tool-usages.txt)
- [Sonnet 3.7 (Tools)](docs/assets/claude/sonnet-3_7-tools.txt)
- [Sonnet 3.7 (User Preferences)](docs/assets/claude/sonnet-3_7-user-preferences.md)
- [Sonnet 3.7](docs/assets/claude/sonnet-3_7.md)
- [Sonnet 4 (Persona)](docs/assets/claude/sonnet-4-persona.md)
- [Sonnet 4 (Personalization)](docs/assets/claude/sonnet-4-personalization.md)
- [Sonnet 4 (Tools)](docs/assets/claude/sonnet-4-tools.txt)
- [Sonnet 4](docs/assets/claude/sonnet-4.txt)
- [Style Modes](docs/assets/claude/style-modes.md)
- [Tool Usage](docs/assets/claude/tool-usage.md)
- [Web Search Instructions](docs/assets/claude/web-search-instructions.md)

### [Claude Code](https://www.anthropic.com/claude-code)

- [Agent Tool](docs/assets/claude-code/agent-tool.js)
- [Batch Execution Tool](docs/assets/claude-code/batch-execution-tool.js)
- [Bug Report Tool](docs/assets/claude-code/bug-report-tool.js)
- [Claude Code](docs/assets/claude-code/claude-code.js)
- [Clear Tool](docs/assets/claude-code/clear-tool.js)
- [Edit Tool](docs/assets/claude-code/edit-tool.js)
- [LS Tool](docs/assets/claude-code/ls-tool.js)
- [Memory Tool](docs/assets/claude-code/memory-tool.js)
- [Persona Modes](docs/assets/claude-code/persona-modes.txt)
- [Prompt 2025-07-06](docs/assets/claude-code/prompt-2025-07-06.txt)
- [Prompt 2025-09-01](docs/assets/claude-code/prompt-2025-09-01.md)
- [Read Notebook](docs/assets/claude-code/read-notebook.js)
- [System Prompt 0.2.9](docs/assets/claude-code/system-prompt-0_2_9.txt)
- [System](docs/assets/claude-code/system.js)
- [Tool Claude Code](docs/assets/claude-code/tools-claude-code.json)
- [Bash Tool](docs/assets/claude-code/tool-bash.txt)
- [Edit Tool](docs/assets/claude-code/tool-edit.txt)
- [Exit Plan Mode Tool](docs/assets/claude-code/tool-exit-plan-mode.txt)
- [Glob Tool](docs/assets/claude-code/tool-glob.txt)
- [Grep Tool](docs/assets/claude-code/tool-grep.txt)
- [LS Tool](docs/assets/claude-code/tool-ls.txt)
- [Multi Edit Tool](docs/assets/claude-code/tool-multi-edit.txt)
- [Notebook Edit Tool](docs/assets/claude-code/tool-notebook-edit.txt)
- [Notebook Read Tool](docs/assets/claude-code/tool-notebook-read.txt)
- [Read Tool](docs/assets/claude-code/tool-read.txt)
- [Task Tool](docs/assets/claude-code/tool-task.txt)
- [Todo Read Tool](docs/assets/claude-code/tool-todo-read.txt)
- [Todo Write Tool](docs/assets/claude-code/tool-todo-write.txt)
- [Web Fetch Tool](docs/assets/claude-code/tool-web-fetch.txt)
- [Web Search Tool](docs/assets/claude-code/tool-web-search.txt)
- [Write Tool](docs/assets/claude-code/tool-write.txt)

### [Cline](https://docs.cline.bot)

- [Prompt](docs/assets/cline/prompt.txt)
- [System](docs/assets/cline/system.ts)
- [Access MCP Resource Tool](docs/assets/cline/tool-access-mcp-resource.txt)
- [Ask Question Tool](docs/assets/cline/tool-ask-question.txt)
- [Attempt Completion Tool](docs/assets/cline/tool-attempt-completion.txt)
- [Bash Tool](docs/assets/cline/tool-bash.txt)
- [Browser Action Tool](docs/assets/cline/tool-browser-action.txt)
- [Grep Tool](docs/assets/cline/tool-grep.txt)
- [List Code Definition Names Tool](docs/assets/cline/tool-list-code-definition-names.txt)
- [Load MCP Documentation Tool](docs/assets/cline/tool-load-mcp-documentation.txt)
- [LS Tool](docs/assets/cline/tool-ls.txt)
- [Multi Edit Tool](docs/assets/cline/tool-multi-edit.txt)
- [New Task Tool](docs/assets/cline/tool-new-task.txt)
- [Plan Mode Respond Tool](docs/assets/cline/tool-plan-mode-respond.txt)
- [Read Tool](docs/assets/cline/tool-read.txt)
- [Use MCP Tool](docs/assets/cline/tool-use-mcp-tool.txt)
- [Web Fetch Tool](docs/assets/cline/tool-web-fetch.txt)
- [Write Tool](docs/assets/cline/tool-write.txt)

### [Cluely](https://cluely.com)

- [Default](docs/assets/cluely/default.txt)
- [Enterprise](docs/assets/cluely/enterprise.txt)
- [Prompt 2025-05-12](docs/assets/cluely/prompt-2025_05_12.txt)
- [Prompt 2025-06-11](docs/assets/cluely/prompt-2025_06_11.txt)

### [CodeBuddy](https://www.codebuddy.ai)

- [Prompt Chat](docs/assets/codebuddy/prompt-chat.md)
- [Prompt Craft](docs/assets/codebuddy/prompt-craft.md)

### [Codex](https://openai.com/blog/openai-codex)

- [Codex Prompt 2025-09-01](docs/assets/codex/codex-prompt-2025-09-01.md)
- [Prompt System](docs/assets/codex/prompt_system.md)
- [Prompt 2025-08-01](docs/assets/codex/prompt-2025-08-01.md)
- [Prompt](docs/assets/codex/prompt.md)

### [Google Colab](https://colab.google)

- [Colab 2024-01-08](docs/assets/colab/colab-2024_01_08.txt)
- [Colab 2024-05-11](docs/assets/colab/colab-2024_05_11.txt)

### [Cue](https://cueai.app)

- [Cue 2023-09-20](docs/assets/cue/cue-2023_09_20.txt)

### [Cursor](https://www.cursor.com)

- [Agent CLI (2025-08-07)](docs/assets/cursor/agent-cli-2025-08-07.md)
- [Agent Tools v1](docs/assets/cursor/agent-tools-v1.txt)
- [Agent v1.0](docs/assets/cursor/agent-v1_0.txt)
- [Agent v1.1](docs/assets/cursor/agent-v1_1.txt)
- [Agent v1.2](docs/assets/cursor/agent-v1_2.txt)
- [Available Tools](docs/assets/cursor/available-tools.txt)
- [Chat](docs/assets/cursor/chat.txt)
- [Code Modification](docs/assets/cursor/code-modification.txt)
- [Memory Rating](docs/assets/cursor/memory-rating.txt)
- [Memory System](docs/assets/cursor/memory-system.txt)
- [Memory](docs/assets/cursor/memory.txt)
- [Personas](docs/assets/cursor/personas.txt)
- [Sonnet 3.5 (2024-12-24)](docs/assets/cursor/sonnet-3_5-2024_12_24.txt)
- [Sonnet 3.7 (2025-03-09)](docs/assets/cursor/sonnet-3_7-2025_03_09.txt)
- [Sonnet 3.7 (Agent Prompt)](docs/assets/cursor/sonnet-3_7-agent-prompt.txt)
- [Tool Usage](docs/assets/cursor/tool-usage.txt)
- [Prompt (2025-09-03)](docs/assets/cursor/prompt-2025-09-03.md)

### [Databricks](https://www.databricks.com)

- [Prompt](docs/assets/databricks/prompt.txt)

### [Devin](https://www.cognition-labs.com/introducing-devin)

- [Prompt (09-08-2025)](docs/assets/devin/prompt-09-08-2025.md)
- [Available Commands](docs/assets/devin/available-commands.txt)
- [Coding Security](docs/assets/devin/coding-security.txt)
- [Persona](docs/assets/devin/persona.txt)
- [Planning](docs/assets/devin/planning.txt)
- [Prompt](docs/assets/devin/prompt.txt)
- [Reasoning Reflection](docs/assets/devin/reasoning-reflection.txt)

### [Discord](https://discord.com)

- [Clyde (2023-04-20)](docs/assets/discord/clyde-2023_04_20.txt)
- [Clyde (2023-05-19)](docs/assets/discord/clyde-2023_05_19.txt)
- [Clyde (2023-07-15)](docs/assets/discord/clyde-2023_07_15.txt)
- [Clyde (2023-07-16)](docs/assets/discord/clyde-2023_07_16.txt)

### [Google Gemini](https://ai.google/gemini)

- [Gemini 2.5 Pro Webapp](docs/assets/gemini/gemini-2.5-pro-webapp.txt)
- [Gemini Diffusion](docs/assets/gemini/gemini-diffusion.txt)
- [Google Gemini 1.5 (2024-04-11)](docs/assets/gemini/google-gemini-1_5-2024_04_11.txt)
- [Google Gemini CLI (2024-07-03)](docs/assets/gemini/google-gemini-cli-2024-07-03.txt)
- [Google Stitch (2025-07-09)](docs/assets/gemini/google-stitch-2025_07_09.txt)
- [Prompt Gemini 2.5 Flash Image Preview](docs/assets/gemini/prompt-gemini-2.5-flash-image-preview.md)
- [Edit Tool](docs/assets/gemini/tool-edit.txt)
- [Glob Tool](docs/assets/gemini/tool-glob.txt)
- [Grep Tool](docs/assets/gemini/tool-grep.txt)
- [LS Tool](docs/assets/gemini/tool-ls.txt)
- [Memory Tool](docs/assets/gemini/tool-memory.txt)
- [Read File Tool](docs/assets/gemini/tool-read-file.txt)
- [Read Many Files Tool](docs/assets/gemini/tool-read-many-files-tool.txt)
- [Shell Tool](docs/assets/gemini/tool-shell.txt)
- [Web Fetch Tool](docs/assets/gemini/tool-web-fetch.txt)
- [Web Search Tool](docs/assets/gemini/tool-web-search.txt)
- [Write File Tool](docs/assets/gemini/tool-write-file.txt)

### [ChatGLM](https://chatglm.cn)

- [ChatGLM 2024-08-21](docs/assets/glm/glm-2024_08_21.txt)

### [Gordon](https://docs.docker.com/ai/gordon)

- [Gordon 2025-06-29](docs/assets/gordon/gordon-2025_06_29.txt)

### [Dia](https://www.dia.com)

- [Prompt](docs/assets/dia/prompt.txt)

### [Grok](https://grok.x.ai)

- [Ask Grok Summarizer](docs/assets/grok/ask-grok-summarizer.j2)
- [Deepsearch Final Summarizer Prompt](docs/assets/grok/deepsearch-final-summarizer-prompt.j2)
- [Grok2](docs/assets/grok/grok-2.txt)
- [Grok3 2025-02-23](docs/assets/grok/grok-3_2025_02_23.txt)
- [Grok3 0330](docs/assets/grok/grok-3-0330.j2)
- [Grok3 2024-03-07](docs/assets/grok/grok-3-2024_03_07.txt)
- [Grok3 2024-10-03](docs/assets/grok/grok-3-2024_10_03.txt)
- [Grok3 2024-12-18](docs/assets/grok/grok-3-2024_12_18.txt)
- [Grok3 2025-01-11](docs/assets/grok/grok-3-2025_01_11.txt)
- [Grok3 With Deep Search](docs/assets/grok/grok-3-with-deep-search.txt)
- [Grok3](docs/assets/grok/grok-3.txt)
- [Grok4 2025-07-13](docs/assets/grok/grok-4-2025-07-13.txt)
- [Grok4](docs/assets/grok/grok-4.txt)
- [Grok Analyze Button](docs/assets/grok/grok-analyze-button.j2)
- [Grok Jailbreak Prompt](docs/assets/grok/grok-jailbreak-prompt.txt)
- [Grok Personas](docs/assets/grok/grok-personas.txt)
- [Grok3 2025-04-23](docs/assets/grok/grok3-2025_04_23.txt)
- [Grok3 2025-05-04](docs/assets/grok/grok3-2025_05_04.txt)
- [Grok3 2025-05-09](docs/assets/grok/grok3-2025_05_09.txt)
- [Grok3 2025-06-05](docs/assets/grok/grok3-2025_06_05.txt)
- [Code Fast 2025-08-01](docs/assets/grok/prompt-code-fast-2025-08-01.md)

### [Hume](https://hume.ai)

- [Prompt 2024-04-05](docs/assets/hume/prompt-2024-04-05.txt)
- [Prompt 2024-05-05](docs/assets/hume/prompt-2024-05-05.txt)

### [Junie](https://junie.co)

- [Prompt](docs/assets/junie/prompt.txt)

### [Kagi](https://kagi.com)

- [Prompt](docs/assets/kagi/prompt.txt)

### [Kiro](https://kiro.dev)

- [Mode Classifier](docs/assets/kiro/prompt-mode-clasifier.md)
- [Specification](docs/assets/kiro/prompt-spec-design-document.md)
- [Implementation Plan](docs/assets/kiro/prompt-spec-implementation-plan.md)
- [Requirement Clarification](docs/assets/kiro/prompt-spec-requirement-clarification.md)
- [Task Execution](docs/assets/kiro/prompt-spec-task-execution.md)
- [System Prompt](docs/assets/kiro/prompt.md)

### [Leap.new](https://leap.new)

- [Prompt](docs/assets/leap/prompt.md)
- [Tools](docs/assets/leap/tools.json)

### [Lovable](https://lovable.ai)

- [Agent Prompt](docs/assets/lovable/agent-prompt.txt)
- [Agent Tools](docs/assets/lovable/agent-tools.txt)
- [Core Principles](docs/assets/lovable/core-principles.txt)
- [Driven Development](docs/assets/lovable/driven-development.txt)
- [File Operations](docs/assets/lovable/file-operations.txt)
- [Included Codebase](docs/assets/lovable/included-codebase.txt)
- [Modes of Operation](docs/assets/lovable/modes-operation.txt)
- [Persona](docs/assets/lovable/persona.txt)
- [Prompt 2025](docs/assets/lovable/prompt-2025.txt)
- [Prompt](docs/assets/lovable/prompt.txt)
- [Response Structure](docs/assets/lovable/response-structure.txt)
- [Special Instructions](docs/assets/lovable/special-instructions.txt)

### [Manus](https://www.manus.io)

- [Agent Loop](docs/assets/manus/agent-loop.txt)
- [Environment](docs/assets/manus/environment.txt)
- [Guidelines](docs/assets/manus/guidelines.txt)
- [Modules](docs/assets/manus/modules.txt)
- [Persona](docs/assets/manus/persona.txt)
- [Prompt 2025 (03-09)](docs/assets/manus/prompt-2025_03_09.txt)
- [Prompt 2025 (03-10)](docs/assets/manus/prompt-2025_03_10.txt)
- [Prompt](docs/assets/manus/prompt.txt)
- [Prompting Guide](docs/assets/manus/prompting-guide.txt)
- [Tools](docs/assets/manus/tools.txt)

### [Mistral](https://mistral.ai)

- [Chat](docs/assets/mistral/chat.txt)
- [Mistral 2025-04-25](docs/assets/mistral/mistral-2025_04_25.txt)
- [Prompt](docs/assets/mistral/prompt.md)

### [Moonshot KIMI](https://www.kimi.com)

- [KIMI 2024-11-06](docs/assets/moonshot/kimi-2024_11_06.txt)

### [MultiOn](https://multion.ai)

- [Prompt](docs/assets/multion/prompt.txt)

### [MyAI](https://my.ai.se)

- [MyAI 2023-04-30](docs/assets/myai/myai-2023_04_30.txt)

### [Notion](https://www.notion.so)

- [Prompt 2025-09-01](docs/assets/notion/prompt-09-01-2025.md)
- [Tools](docs/assets/notion/tools.json)
- [Prompt 2024-12-28](docs/assets/notion/prompt-2024_12_28.txt)
- [Prompt](docs/assets/notion/prompt.txt)

### [Notte](https://www.notte.ai)

- [Prompt](docs/assets/notte/prompt.txt)

### [OpenAI](https://openai.com)

- [Advanced Voice Mode](docs/assets/openai/advanced-voice-mode.txt)
- [Agent Mode GPT-5](docs/assets/openai/agent-mode-gpt5.md)
- [Automation Context](docs/assets/openai/automation-context.txt)
- [ChatGPT 5 (2025-08-08)](docs/assets/openai/chat-gpt-5-2025-08-08.md)
- [Codex](docs/assets/openai/codex.txt)
- [DALL·E](docs/assets/openai/dalle.txt)
- [Edit Audio](docs/assets/openai/edit-audio.py)
- [Edit Text](docs/assets/openai/edit-text.py)
- [Function Schema](docs/assets/openai/function-schema.py)
- [GPT-4o Mini (2024-06-01)](docs/assets/openai/gpt-4o_mini-2024_06_01.txt)
- [GPT-4o Mini (2025-06-04)](docs/assets/openai/gpt-4o_mini-2025_06_04.txt)
- [GPT-4o Advanced Voice Mode](docs/assets/openai/gpt-4o-advanced-voice-mode.txt)
- [GPT-4o Image Safety Policies](docs/assets/openai/gpt-4o-image-safety-policies.txt)
- [GPT-4o Legacy Voice Mode](docs/assets/openai/gpt-4o-legacy-voice-mode.txt)
- [GPT-4o Mini](docs/assets/openai/gpt-4o-mini.txt)
- [GPT-4o](docs/assets/openai/gpt-4o.txt)
- [GPT-4o Mini](docs/assets/openai/gpt-41_mini.txt)
- [GPT-4o](docs/assets/openai/gpt-41.txt)
- [GPT-4o Base Information](docs/assets/openai/gpt-45-base-information.txt)
- [GPT-4o Guidelines](docs/assets/openai/gpt-45-guidelines.txt)
- [GPT-4o Image Capabilities](docs/assets/openai/gpt-45-image-capabilities.txt)
- [GPT-4o Tools](docs/assets/openai/gpt-45-tools.txt)
- [GPT-4o](docs/assets/openai/gpt-45.txt)
- [GPT-4o Automation Tool](docs/assets/openai/gpt-automation-tool.txt)
- [GPT-4o API Variations](docs/assets/openai/gpt-o3-api-variations.txt)
- [GPT-4o Canmore Canvas Tool](docs/assets/openai/gpt-o3-canmore-canvas-tool.txt)
- [GPT-4o Other Tools](docs/assets/openai/gpt-o3-other-tools.txt)
- [GPT-4o Python Tools](docs/assets/openai/gpt-o3-python-tools.txt)
- [GPT-4o](docs/assets/openai/gpt-o3.txt)
- [GPT-4o Mini](docs/assets/openai/gpt-o4-mini.txt)
- [GPT-4o Image Safety Policies](docs/assets/openai/image-safety-policies.txt)
- [Meta Audio](docs/assets/openai/meta-audio.py)
- [Meta Schema](docs/assets/openai/meta-schema.py)
- [Meta Text](docs/assets/openai/meta-text.py)
- [OpenAI 2022-12-01](docs/assets/openai/openai-2022_12_01.txt)
- [OpenAI 2023-06-14](docs/assets/openai/openai-2023_06_14.txt)
- [OpenAI 2023-11-06](docs/assets/openai/openai-2023_11_06.txt)
- [OpenAI 2024-02-07](docs/assets/openai/openai-2024_02_07.txt)
- [OpenAI 2024-05-20](docs/assets/openai/openai-2024_05_20.txt)
- [OpenAI 2025-03-24](docs/assets/openai/openai-2025_03_24.txt)
- [OpenAI 2025-05-06](docs/assets/openai/openai-2025_05_06.txt)
- [OpenAI DALL·E 3 (20231007-1)](docs/assets/openai/openai-dall-e-3_20231007-1.txt)
- [OpenAI DALL·E 3 (20231007-2)](docs/assets/openai/openai-dall-e-3_20231007-2.txt)
- [OpenAI Deep Research (20250204)](docs/assets/openai/openai-deep-research_20250204.txt)
- [OpenAI Deep Research](docs/assets/openai/openai-deep-research.txt)
- [OpenAI Voice Mode (2025-07-06)](docs/assets/openai/openai-voice-mode-2025_07_06.txt)
- [Persona Tone](docs/assets/openai/persona-tone.txt)
- [Prompt GPT-5 Thinking](docs/assets/openai/prompt-gpt5-thinking.md)
- [Summary](docs/assets/openai/summary.txt)
- [System](docs/assets/openai/system.txt)
- [Tool Canvas](docs/assets/openai/tool-canvas.txt)
- [Tool Channels](docs/assets/openai/tool-channels.txt)
- [Tool Chat History](docs/assets/openai/tool-chat-history.txt)
- [Tool Deep Research](docs/assets/openai/tool-deep-research.txt)
- [Tool File Search](docs/assets/openai/tool-file-search.txt)
- [Tool Image Generation](docs/assets/openai/tool-image-gen.txt)
- [Tool Memory Bio](docs/assets/openai/tool-memory-bio.txt)
- [Tool Python](docs/assets/openai/tool-python.txt)
- [Tool Study Together](docs/assets/openai/tool-study-together.txt)
- [Tool Web Search](docs/assets/openai/tool-web-search.txt)
- [Web Browsing Policy](docs/assets/openai/web-browsing-policy.txt)

### [Opera Aria](https://www.opera.com/features/aria)

- [Aria 2023-06-17](docs/assets/opera/aria-2023_06_17.txt)

### [Orchids](https://www.orchids.app/)

- [Decision Making](docs/assets/orchids/decision-making.txt)
- [Prompt](docs/assets/orchids/prompt.txt)

### [Parahelp](https://parahelp.com)

- [Manager Tool](docs/assets/parahelp/manager.txt)
- [Planning Tool](docs/assets/parahelp/planning.txt)

### [Perplexity](https://www.perplexity.ai)

- [Deep Research](docs/assets/perplexity/deep-research.md)
- [Perplexity 2022-12-08](docs/assets/perplexity/perplexity-2022_12_08.txt)
- [Perplexity 2024-03-11](docs/assets/perplexity/perplexity-2024_03_11.txt)
- [Perplexity 2024-05-13](docs/assets/perplexity/perplexity-2024_05_13.txt)
- [Perplexity 2024-06-07](docs/assets/perplexity/perplexity-2024_06_07.txt)
- [Perplexity 2025-01-12](docs/assets/perplexity/perplexity-2025_01_12.txt)
- [Prompt Comet](docs/assets/perplexity/prompt-comet.md)
- [Prompt](docs/assets/perplexity/prompt.txt)
- [Voice Assistant](docs/assets/perplexity/voice-assistant.txt)

### [Phind](https://www.phind.com)

- [Phind 2024-04-27](docs/assets/phind/phind-2024_04_27.txt)

### [Poke](https://poke.dev)

- [Agent](docs/assets/poke/agent.md)
- [Prompt Agent Protocol](docs/assets/poke/prompt_agent_protocol.md)
- [Prompt Email Protocols](docs/assets/poke/prompt_email_protocols.md)
- [Prompt Guidelines](docs/assets/poke/prompt_guidelines.md)
- [Prompt Integration Policies](docs/assets/poke/prompt_integration_policies.md)
- [Prompt Memory Guidelines](docs/assets/poke/prompt_memory_guidelines.md)
- [Prompt Platform Guidelines](docs/assets/poke/prompt_platform_guidelines.md)

### [Proton](https://proton.me/)

- [Prompt (2025-07-24)](docs/assets/proton/prompt-2025-07-24.txt)
- [Prompt (2025-07-27)](docs/assets/proton/prompt-2025-07-27.txt)

### [Qoder](https://www.qoder.com)

- [Quest Action](docs/assets/qoder/quest-action.md)
- [Quest Design](docs/assets/qoder/quest-design.md)
- [Prompt](docs/assets/qoder/prompt.md)

### [Raycast](https://www.raycast.com)

- [Prompt](docs/assets/raycast/prompt.txt)

### [Remoteli](https://remoteli.io)

- [Remoteli 2023-08-06](docs/assets/remoteli/remoteli-2023_08_06.txt)

### [Replit](https://replit.com)

- [Prompt 2025](docs/assets/replit/prompt-2025.txt)
- [Prompt](docs/assets/replit/prompt.txt)
- [Tools](docs/assets/replit/tools.txt)

### [Roblox Studio Assistant](https://create.roblox.com/docs/assistant/guide)

- [Roblox 2024-03-20](docs/assets/roblox/roblox-2024_03_20.txt)

### [Roo-Code](https://www.roo.com)

- [Prompt 2025-07-06](docs/assets/roo-code/prompt-2025-07-06.txt)
- [Prompt](docs/assets/roo-code/prompt.txt)
- [Ask Followup Question Tool](docs/assets/roo-code/tool-ask-followup-question.txt)
- [Attempt Completion Tool](docs/assets/roo-code/tool-attempt-completion.txt)
- [Browser Action Tool](docs/assets/roo-code/tool-browser-action.txt)
- [Execute Command Tool](docs/assets/roo-code/tool-execute-command.txt)
- [Insert Content Tool](docs/assets/roo-code/tool-insert-content.txt)
- [List Files Tool](docs/assets/roo-code/tool-list-files.txt)
- [New Task Tool](docs/assets/roo-code/tool-new-task.txt)
- [Read File Tool](docs/assets/roo-code/tool-read-file.txt)
- [Search and Replace Tool](docs/assets/roo-code/tool-search-and-replace.txt)
- [Search Files Tool](docs/assets/roo-code/tool-search-files.txt)
- [Switch Mode Tool](docs/assets/roo-code/tool-switch-mode.txt)
- [Write to File Tool](docs/assets/roo-code/tool-write-to-file.txt)

### [Same-Dev](https://www.same.dev)

- [Prompt](docs/assets/same-dev/prompt.txt)
- [Tools](docs/assets/same-dev/tools.txt)

### [ScamGuard](https://www.thescamguard.com/)

- [Prompt 2025-06-08](docs/assets/scamguard/prompt-2025_06_08.txt)

### [Maya Sesame](https://www.sesame.com/)

- [Prompt](docs/assets/sesame/prompt.txt)

### [Telegram](https://telegram.org)

- [Grok 4](docs/assets/telegram/prompt-bot-grok4.md)
- [Perplexity](docs/assets/telegram/prompt-bot-perplexity.md)

### [Tracer AI](https://www.tracer.ai/)

- [Prompt Phase](docs/assets/tracerai/prompt-phase-mode.md)
- [Prompt Plan](docs/assets/tracerai/prompt-plan-mode.md)
- [Tools Phase](docs/assets/tracerai/tools-phase-mode.json)
- [Tools Plan](docs/assets/tracerai/tools-plan-mode.json)

### [Trae](https://trae.ai)

- [Chat](docs/assets/trae/chat.md)
- [Prompt Builder](docs/assets/trae/prompt-builder.md)
- [Tools Builder](docs/assets/trae/tools-builder.json)

### [V0](https://v0.dev)

- [Instructions](docs/assets/v0/instructions.txt)
- [Model](docs/assets/v0/model.txt)
- [Prompt 2025-03-06](docs/assets/v0/prompt-2025_03_06.txt)
- [Prompt](docs/assets/v0/prompt.md)
- [System](docs/assets/v0/system.txt)
- [Tools](docs/assets/v0/tools.txt)

### [VSCode](https://code.visualstudio.com)

- [Chat Titles](docs/assets/vscode/chat-titles.md)
- [Copilot 2023-05-13](docs/assets/vscode/copilot-2023_05_13.txt)
- [Copilot 2024-03-10](docs/assets/vscode/copilot-2024_03_10.txt)
- [Copilot 2024-09-30](docs/assets/vscode/copilot-2024_09_30.txt)
- [Copilot 2024-12-19](docs/assets/vscode/copilot-2024_12_19.txt)
- [Nes Tab Completion](docs/assets/vscode/nes-tab-completion.md)
- [Prompt Claude Sonnet 4](docs/assets/vscode/prompt-claude-sonnet-4.md)
- [Prompt Gemini 2.5pro](docs/assets/vscode/prompt-gemini-2.5pro.md)
- [Prompt GPT-4o](docs/assets/vscode/prompt-gpt-4o.md)
- [Prompt GPT-5](docs/assets/vscode/prompt-gpt-5.md)
- [Prompt GPT-5mini](docs/assets/vscode/prompt-gpt-5mini.md)
- [Prompt GPT-4.1](docs/assets/vscode/prompt-gpt4.1.md)
- [Prompt](docs/assets/vscode/prompt.txt)

### [Warp](https://www.warp.dev)

- [Prompt](docs/assets/warp/prompt.txt)

### [Whatsapp](https://www.whatsapp.com)

- [Llama 4](docs/assets/whatsapp/llama4.md)
- [Meta AI](docs/assets/whatsapp/meta-ai.md)
- [Whatsapp 2025-08-19](docs/assets/whatsapp/whatsapp-2025-08-19.md)

### [Windsurf](https://windsurf.ai)

- [Communication](docs/assets/windsurf/communication.txt)
- [Examples](docs/assets/windsurf/examples.txt)
- [Guidelines](docs/assets/windsurf/guidelines.txt)
- [Persona](docs/assets/windsurf/persona.txt)
- [Prompt 2024-12-06](docs/assets/windsurf/prompt-2024_12_06.txt)
- [Prompt 2025-02-01](docs/assets/windsurf/prompt-2025_02_01.txt)
- [Prompt](docs/assets/windsurf/prompt.txt)
- [System](docs/assets/windsurf/system.txt)
- [Tools](docs/assets/windsurf/tools.txt)

### [WRTN](https://wrtn.ai)

- [WRNT 2023-06-03](docs/assets/wrtn/wrtn-2023_06_03.txt)
- [WRNT 2024-02-15](docs/assets/wrtn/wrtn-2024_02_15.txt)
- [WRNT 2024-02-16](docs/assets/wrtn/wrtn-2024_02_16.txt)

### [Xcode](https://developer.apple.com/xcode/)

- [Document Action](docs/assets/xcode/document-action.txt)
- [Explain Action](docs/assets/xcode/explain-action.txt)
- [Message Action](docs/assets/xcode/message-action.txt)
- [Playground Action](docs/assets/xcode/playground-action.txt)
- [Preview Action](docs/assets/xcode/preview-action.txt)
- [System Action](docs/assets/xcode/system-action.txt)

### [Z.ai](https://z.ai)

- [Prompt](docs/assets/z-ai/prompt.txt)

### [Zed](https://zed.dev)

- [Prompt](docs/assets/zed/prompt.txt)
- [Copy Path Tool](docs/assets/zed/tool-copy-path.txt)
- [Create Directory Tool](docs/assets/zed/tool-create-directory.txt)
- [Delete Path Tool](docs/assets/zed/tool-delete-path.txt)
- [Diagnostics Tool](docs/assets/zed/tool-diagnostics.txt)
- [Edit File Tool](docs/assets/zed/tool-edit-file.txt)
- [Fetch Tool](docs/assets/zed/tool-fetch.txt)
- [Find Path Tool](docs/assets/zed/tool-find-path.txt)
- [Grep Tool](docs/assets/zed/tool-grep.txt)
- [List Directory Tool](docs/assets/zed/tool-list-directory.txt)
- [Move Path Tool](docs/assets/zed/tool-move-path.txt)
- [Now Tool](docs/assets/zed/tool-now.txt)
- [Read File Tool](docs/assets/zed/tool-read-file.txt)
- [Terminal Tool](docs/assets/zed/tool-terminal.txt)
- [Thinking Tool](docs/assets/zed/tool-thinking.txt)
- [Web Search Tool](docs/assets/zed/tool-web-search.txt)
