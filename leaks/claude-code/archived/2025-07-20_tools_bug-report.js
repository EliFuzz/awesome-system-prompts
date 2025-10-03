async function Yz5(I) {
  try {
    let Z = await fV({
        systemPrompt: [
          "Generate a concise, technical issue title (max 80 chars) for a GitHub issue based on this bug report. The title should:",
          "- Be specific and descriptive of the actual problem",
          "- Use technical terminology appropriate for a software issue",
          '- For error messages, extract the key error (e.g., "Missing Tool Result Block" rather than the full message)',
          '- Start with a noun or verb (not "Bug:" or "Issue:")',
          "- Be direct and clear for developers to understand the problem",
          '- If you cannot determine a clear issue, use "Bug Report: [brief description]"',
        ],
        userPrompt: I,
        isNonInteractiveSession: !1,
      }),
      G =
        Z.message.content[0]?.type === "text"
          ? Z.message.content[0].text
          : "Bug Report";
    if (G.startsWith(mw)) return j$2(I);
    return G;
  } catch (Z) {
    return n1(Z instanceof Error ? Z : new Error(String(Z))), j$2(I);
  }
}
