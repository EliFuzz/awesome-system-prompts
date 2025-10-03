```typescript
// --- Common Context Interface ---
interface VscodeEditorContext {
  selection?: string;
  fullCode: string;
  languageId: string;
  prefix: string; // Code before cursor
  suffix?: string; // Code after cursor
  neighboringCode?: { above: string; below: string };
  gitDiff?: string;
  multipleFileContents?: { filePath: string; content: string }[];
  chatHistory?: { user?: string; blackbox?: string }[];
}
```

## Inline Code Editing/Generation (Ctrl+I)

```typescript
const INLINE_EDIT_SYSTEM_PROMPT = `You are a coding assistant specializing in code completion and editing. Your task is to modify the selected code based on the prompt, considering the entire code file for context. Follow these guidelines:

- Generate the modified code that should replace the selected portion.
- Return ONLY the modified code snippet, without any markdown formatting, natural language explanations, or triple backticks.
- Ensure the modified code integrates seamlessly with the rest of the file.
- Maintain consistent style, indentation, and naming conventions with the existing code.
- Strictly answer with code only`;

function createInlineEditUserPrompt(
  prompt: string,
  context: VscodeEditorContext
): string {
  return `## Selected Code
[START SELECTION]
${context.selection || ""}
[END SELECTION]

## Entire Code File
[START ENTIRE FILE]
${context.fullCode}
[END FILE]

Generate the modified code that should replace the selected portion. If there is no selection, generate code that should be inserted at the cursor position. Strictly answer with code only:

Prompt: ${prompt}`;
}

/*
 * Conceptual API Call Structure:
 * [
 *   { role: "system", content: INLINE_EDIT_SYSTEM_PROMPT },
 *   { role: "user", content: createInlineEditUserPrompt(userInstruction, context) }
 * ]
 */
```

## Code Completion (Typing Pause)

Note: Actual prompt structure is internal to the Blackbox API.

```typescript
function createCodeCompletionInput(
  context: VscodeEditorContext,
  userId: string,
  premiumStatus: boolean,
  autocompleteVersion: "quality" | "speed"
): any {
  return {
    userId: userId,
    languageId: context.languageId,
    prompt: context.prefix,
    contextAbove: context.neighboringCode?.above,
    contextBelow: context.neighboringCode?.below,
    source: "visual studio",
    premiumStatus: premiumStatus,
    autocompleteVersion: autocompleteVersion,
  };
}
```

## Code Search (// ? Query)

Note: Actual prompt structure is internal to the Blackbox API.

```typescript
function createCodeSearchInput(query: string, userId: string): any {
  return {
    userId: userId,
    textInput: query,
    source: "visual studio",
  };
}
```

## Blackbox AI Chat (Side Panel / Commands)

Note: Uses a webview; prompts are handled by the webview's backend.
Context is passed from the extension to the webview.

```typescript
interface ChatMessage {
  user?: string;
  blackbox?: string;
}

interface ChatPromptInput {
  // Structure passed *to* webview or used by its backend
  userMessage: string;
  context?: VscodeEditorContext;
  chatHistory: ChatMessage[];
  commandTrigger?: string; // e.g., 'explain_code', 'comment_code'
  workspaceId?: string;
}

// --- Example User Prompts Sent to Chat ---
const explainCodePrompt = (code: string, languageId: string) =>
  `\`\`\`${languageId}\n${code}\n\`\`\`\n\nExplain this code`;

const improveCodePrompt = (code: string, languageId: string) =>
  `\`\`\`${languageId}\n${code}\n\`\`\`\n\nRewrite this code better`;

const suggestCodePrompt = (codeAbove: string, languageId: string) =>
  `\`\`\`${languageId}\n${codeAbove}\n\`\`\`\n\ngive 1 suggestion to continue this code. give code only.`;

const commentCodeInstruction = `give me this code with proper commenting. comments should clear consice. stay focused, this is very important for my career.`; // Code provided as context
```

## Commit Message Generation (SCM Integration)

```typescript
function createCommitMessageInput(
  context: VscodeEditorContext,
  userId: string
): any {
  return {
    userId: userId,
    diff: context.gitDiff,
    source: "visual studio", // or 'source control'
  };
}
```

## README Generation (Command)

```typescript
function createReadmeInput(context: VscodeEditorContext, userId: string): any {
  const allFilesString = context.multipleFileContents
    ?.map((file) => `File: ${file.filePath}\n\n${file.content}`)
    .join("\n\n---\n\n");

  return {
    userId: userId,
    allFiles: allFilesString,
  };
}
```

## Code Review / Editor Chat (Older Command)

```typescript
function createEditorChatInput(context: VscodeEditorContext): any {
  let userContentWithLine = "";
  context.fullCode.split("\n").forEach((line, index) => {
    userContentWithLine += `${index + 1}: ${line}\n`;
  });

  return {
    language: context.languageId,
    code: userContentWithLine,
  };
}
```
