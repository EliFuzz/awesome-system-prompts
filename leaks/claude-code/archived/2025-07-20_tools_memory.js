function Xn2(I) {
  return `You have been asked to add a memory or update memories in the memory file at ${I}.
  
  Please follow these guidelines:
  - If the input is an update to an existing memory, edit or replace the existing entry
  - Do not elaborate on the memory or add unnecessary commentary
  - Preserve the existing structure of the file and integrate new memories naturally. If the file is empty, just add the new memory as a bullet entry, do not add any headings.
  - IMPORTANT: Your response MUST be a single tool use for the FileWriteTool`;
}
function I31(I) {
  let Z = C5();
  if (I === "ExperimentalUltraClaudeMd") return Xd1;
  switch (I) {
    case "User":
      return Xd1;
    case "Local":
      return Vg1(Z, "CLAUDE.local.md");
    case "Project":
      return Vg1(Z, "CLAUDE.md");
    case "ExperimentalUltraClaudeMd":
      return Vg1(Ni5(), ".claude", "ULTRACLAUDE.md");
  }
}
async function ii2(I, Z, G = "User") {
  let W = I31(G);
  if (G === "Local" && !Bg1(W)) s51(W);
  (Z.addNotification?.(
    { text: `Saving ${Ih(G)} memory…` },
    { timeoutMs: 30000 }
  ),
    x1("tengu_add_memory_start", {}),
    Ri5());
  let B = eu(W);
  if (!Bg1(Hn2(W)))
    try {
      Ui5(Hn2(W), { recursive: !0 });
    } catch (D) {
      n1(D instanceof Error ? D : new Error(String(D)));
    }
  let V = [wI],
    w = Q5({
      content: `Memory to add/update:
  ```
  ${I}
  ```
  
  Existing memory file content:
  ```
  ${B || "[empty file]"}
  ````,
    }),
    Y = await Gv([w], [Xn2(W)], 0, V, Z.abortController.signal, {
      permissionMode: "default",
      model: Z.options.slowAndCapableModel,
      prependCLISysprompt: !0,
      toolChoice: { name: wI.name, type: "tool" },
      isNonInteractiveSession: Z.options.isNonInteractiveSession,
    }),
    X = Y.message.content.find((D) => D.type === "tool_use");
  if (!X) {
    (n1(new Error("No tool use found in response")),
      Z.addNotification?.({
        text: "Failed to save memory: No tool use found in response",
        color: "error",
      }));
    return;
  }
  let H = eZ([
    await h_(
      q61(X, new Set(), Y, (D, K) => $i5(D, K, W), {
        options: Z.options,
        abortController: Z.abortController,
        readFileTimestamps: {
          [W]: Bg1(W) ? qi5(W).mtime.getTime() + 1 : Date.now(),
        },
        userProvidedHosts: Z.userProvidedHosts,
        setToolJSX: Z.setToolJSX,
        getToolPermissionContext: Z.getToolPermissionContext,
      })
    ),
  ])[0];
  if (
    H.type === "user" &&
    H.message.content[0].type === "tool_result" &&
    H.message.content[0].is_error
  )
    throw (
      x1("tengu_add_memory_failure", {}),
      new Error(H.message.content[0].content)
    );
  let J = eu(W);
  if (
    (x1("tengu_add_memory_success", {}),
    nw({
      filePath: W,
      fileContents: B,
      oldStr: B,
      newStr: J,
      ignoreWhitespace: !0,
    }).length > 0)
  )
    Z.addNotification?.(
      { jsx: wg1.createElement(vj2, { memoryType: G, memoryPath: W }) },
      { timeoutMs: 1e4 }
    );
  else Z.addNotification?.({ text: `No changes made to ${Ih(G)} memory` });
}
async function $i5(I, Z, G) {
  if (I !== wI) return { result: !1, message: "Used incorrect tool" };
  let { file_path: W } = wI.inputSchema.parse(Z);
  if (W !== G)
    return { result: !1, message: `Must use correct memory file path: ${G}` };
  return { result: !0, updatedInput: Z };
}
