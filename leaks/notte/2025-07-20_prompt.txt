# --- Notte Task Prompt ---

## Objective Definition:
Define the single, specific, and verifiable goal of this task. State the exact outcome that must be achieved for completion.
Goal: {Describe the precise end-goal with measurable success}

## Required Starting Context (Mandatory if not default):
Specify the exact URL, application state, active session identifier, or unique resource name that defines the mandatory starting condition for this task.
Start State: {Exact URL, Specific Application View/State, Session ID, or Resource Identifier}

## Essential Input Data:
List all absolutely essential data parameters required for successful execution. Provide exact values or references. Accuracy is critical.
- Input Parameter Name 1: {Exact Value 1}
- Input Parameter Name 2: {Exact Value 2}
- Required Credentials: {Username/ID and Password/API Key - provide directly OR specify precise reference name if using an external credential manager}
- Input Content/Payload: {Exact text, data structure (e.g., JSON), or specific file path/reference}
- Target Identifier: {Unique ID, name, or selector for the specific target entity (e.g., product SKU, user ID, DOM element ID)}

## Mandatory Workflow Sequence (If specific order is critical):
Define the non-negotiable, high-level logical sequence of operations. Focus strictly on the required order of functional steps, not UI interactions. Omit if standard agent reasoning is sufficient.
1. {First critical operation/functional stage}
2. {Second critical operation/functional stage}
3. {Final critical operation/functional stage}

## Required Outcome & Verification Criteria:
Describe the exact, verifiable final state, output artifact, or confirmation signal. Specify the precise method for confirming success. Define output format if structure is required.
Success Criteria: {Precise description of the mandatory end state, required output data structure/format, expected confirmation message/signal, or artifact to be generated}

## Strict Operational Constraints:
Define absolute, non-negotiable boundaries, rules, limits, or forbidden actions/elements for this task execution.
- Must Strictly Adhere To: {Mandatory rule, condition, or operational parameter}
- Must Strictly Avoid: {Forbidden action, interaction pattern, data pattern, or target element}

## Failure Handling Guidance (Optional):
Provide explicit instructions for scenarios where the primary workflow is blocked or fails unexpectedly.
If Failing:
- Primary Fallback Action: {Specify the first alternative high-level strategy to attempt}
- Information To Log/Report on Failure: {Define critical details needed for diagnosis}
- Retry Condition (If applicable): {Specify conditions under which a retry is permitted}
- Final Action on Persistent Failure: {e.g., Abort, Notify, Save partial state}

# --- End Prompt ---