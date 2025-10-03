import os
import re


def is_likely_code_or_markup(text, text_lower):
    """
    Heuristically checks if a string is more likely code, HTML, or CSS
    than a natural language prompt. Adjusted to be less sensitive to syntax
    if strong prompt indicators are present elsewhere.
    """
    # Reduced list of very common code keywords that might appear in prompts
    # but less likely to dominate unless it *is* code.
    code_keywords = [
        "function(",
        " class ",
        " constructor(",
        " Symbol(",
        ".prototype",  # Structure
        "addEventListener",
        "querySelector",
        "getElementById",
        "createElement",  # DOM specific
        "Object.assign",
        "Object.defineProperty",
        "Promise.resolve",
        "Promise.reject",  # Object/Promise
        "module.exports",
        "export default",
        "import {",  # Module system
        "console.log",
        "console.error",  # Logging (less reliable on its own)
        " try {",
        "} catch (",
        " for (",
        " while (",  # Control flow
        ".map(",
        ".filter(",
        ".reduce(",
        ".forEach(",  # Array methods often in code blocks
        "JSON.stringify",
        "JSON.parse",
        "new Error(",
        "throw new ",
        "# sourceMappingURL=",  # Definite noise
    ]
    # Keywords strongly suggesting JS/TS but could appear in prompts describing code
    ambiguous_code_keywords = ["async (", "await ", "this.", "=> {"]

    code_keyword_count = sum(1 for kw in code_keywords if kw in text_lower)
    ambiguous_code_keyword_count = sum(
        1 for kw in ambiguous_code_keywords if kw in text_lower
    )

    # Check for common HTML/CSS patterns
    html_css_keywords = [
        "<!DOCTYPE html>",
        "<html",
        "<head>",
        "<body",
        "</script>",
        "</style>",  # Closing tags added
        "padding:",
        "margin:",
        "color:",
        "background-color:",
        "font-size:",
        "display: flex",
        "position: absolute",
        "z-index:",
        "border-radius:",
        ".CodeMirror",
        "w-button",
        "w-form",
        "::placeholder",
        ":-ms-input-placeholder",  # Added from examples
    ]
    html_css_keyword_count = sum(1 for kw in html_css_keywords if kw in text_lower)

    # Symbol/Tag Ratios
    code_symbols = len(re.findall(r"[{}()\[\];=.,+\-*/&|!<>?:%]", text))
    words = len(re.findall(r"\b\w+\b", text))
    word_count = words if words > 0 else 1
    symbol_ratio = code_symbols / (code_symbols + word_count)

    html_tags = len(re.findall(r"<[/!]?\s*\w+", text))
    html_tag_ratio = html_tags / word_count if word_count > 0 else 0

    css_rules = len(re.findall(r"[{};:]", text))
    css_char_ratio = css_rules / len(text) if len(text) > 0 else 0

    html_entities = len(re.findall(r"&[#a-zA-Z0-9]+;", text))
    entity_ratio = html_entities / len(text) if len(text) > 0 else 0

    # --- Decision Logic for Noise ---
    # Very high symbol ratio, few code words -> likely data/minified (like Template 607-609)
    if (
        symbol_ratio > 0.45
        and code_keyword_count < 1
        and ambiguous_code_keyword_count < 1
    ):
        return True
    # Multiple specific code keywords + high symbol ratio suggests actual code block
    if code_keyword_count >= 2 and symbol_ratio > 0.25:
        return True
    # Or several ambiguous ones + high symbols
    if ambiguous_code_keyword_count >= 2 and symbol_ratio > 0.30:
        return True
    # Web/CSS keywords are strong indicators of noise
    if html_css_keyword_count >= 2 or html_tag_ratio > 0.1:
        return True
    if css_char_ratio > 0.07:
        return True
    # High density of HTML entities (like Template 4)
    if entity_ratio > 0.05 and html_entities > 15:
        return True

    return False  # Otherwise, might be a prompt


def extract_prompt_templates(
    filepath, output_filepath="extracted_prompts_filtered_v4.txt", min_length=150
):
    """
    Extracts potential prompt templates, attempting to strongly filter out non-prompts.
    Version 4: Fine-tuned noise detection and keyword priority.
    """
    if not os.path.exists(filepath):
        print(f"Error: Input file not found at {filepath}")
        return -1

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file {filepath}: {e}")
        return -1

    template_literal_regex = r"`((?:\`|[^`])*)`"

    # Keywords indicating a high probability of being a prompt
    very_strong_prompt_keywords = [
        "you are blackboxai",  # Case insensitive check below
        "you are a helpful assistant",
    ]
    # Structure markers are also very strong indicators
    structure_markers = [
        "====\nTOOL USE\n====",
        "====\nRULES\n====",
        "====\nSYSTEM INFORMATION\n====",
        "====\nOBJECTIVE\n====",
        "====\nCAPABILITIES\n====",
        "====\nMCP SERVERS\n====",
        "--- START OF EXAMPLE ---",
        "--- END OF EXAMPLE ---",
    ]
    # Specific tool tags
    tool_tags = [
        "<execute_command>",
        "<read_file>",
        "<create_file>",
        "<edit_file>",
        "<replace_in_file>",
        "<ask_followup_question>",
        "<attempt_completion>",
        "<brainstorm_plan>",
        "<search_code>",
        "<search_files>",
        "<list_files>",
        "<browser_action>",
        "<use_mcp_tool>",
        "<access_mcp_resource>",
        "<tool_name>",
    ]
    other_prompt_keywords = [
        "parameters:",
        "usage:",
        "description:",
        "current working directory",
        "tool use formatting",
        "tool use guidelines",
        "# tools",
        "mcp servers are not always necessary",
    ]

    very_strong_lower = {kw.lower() for kw in very_strong_prompt_keywords}
    structure_lower = {kw.lower() for kw in structure_markers}
    tool_tags_lower = {kw.lower() for kw in tool_tags}
    other_lower = {kw.lower() for kw in other_prompt_keywords}

    templates_saved_count = 0
    total_literals_found = 0

    try:
        matches = re.findall(template_literal_regex, content, re.DOTALL)
        total_literals_found = len(matches)
        print(f"Found {total_literals_found} total template literals in the source.")

        with open(output_filepath, "w", encoding="utf-8") as outfile:
            outfile.write(
                f"--- Extracted Potential Prompt Templates from: {filepath} ---\n"
            )
            outfile.write(
                f"--- (Filtered from {total_literals_found} total template literals found, v4 logic) ---\n\n"
            )

            for i, match_content in enumerate(matches):
                template = match_content.strip()
                template_lower = template.lower()
                is_potential_prompt = False

                # --- Filtering Logic ---
                if len(template) < min_length:
                    continue

                # 1. Check for VERY strong starting keywords first
                # Use slicing for performance if templates are huge
                prefix_lower = template_lower[:100]  # Check first 100 chars
                starts_with_very_strong = any(
                    prefix_lower.startswith(kw) for kw in very_strong_lower
                )

                # 2. If not starting strongly, check if it looks like noise
                likely_noise = False
                if not starts_with_very_strong:
                    likely_noise = is_likely_code_or_markup(template, template_lower)

                if likely_noise:
                    continue

                # 3. Check for other strong prompt indicators (structure, tools)
                has_structure_marker = any(
                    kw in template_lower for kw in structure_lower
                )
                has_tool_tag = any(kw in template_lower for kw in tool_tags_lower)
                has_other_prompt_keywords_count = sum(
                    1 for kw in other_lower if kw in template_lower
                )

                # --- Decision ---
                # Keep if:
                # - It starts with a very strong keyword
                # - OR it has structure markers OR multiple tool tags (strong indicators)
                # - OR it has at least one tool tag AND multiple other keywords
                # - OR it has many (4+) other keywords (might be a prompt without tags)
                if starts_with_very_strong:
                    is_potential_prompt = True
                elif not likely_noise:  # Only proceed if not flagged as noise
                    tool_tag_count = sum(
                        1 for tag in tool_tags_lower if tag in template_lower
                    )
                    if has_structure_marker or tool_tag_count >= 2:
                        is_potential_prompt = True
                    elif tool_tag_count >= 1 and has_other_prompt_keywords_count >= 2:
                        is_potential_prompt = True
                    elif has_other_prompt_keywords_count >= 4:
                        is_potential_prompt = True

                if is_potential_prompt:
                    templates_saved_count += 1
                    outfile.write(
                        f"--- Template {templates_saved_count} (Original Index: {i + 1}) ---\n"
                    )
                    outfile.write(template)
                    outfile.write("\n\n--------------------\n\n")
                    # --- End Filtering Logic ---

        print(
            f"Successfully saved {templates_saved_count} potential templates to: {output_filepath}"
        )
        return templates_saved_count

    except Exception as e:
        print(f"An error occurred during extraction or writing to file: {e}")
        return -1


# --- Main Execution ---
if __name__ == "__main__":
    file_to_analyze = "extension.js"
    output_file = "extracted_prompts_filtered_v4.txt"  # New output name

    print(f"Analyzing file: {file_to_analyze}")
    count = extract_prompt_templates(file_to_analyze, output_file)

    if count > 0:
        print(f"Extraction complete. Check the file '{output_file}' for results.")
    elif count == 0:
        print(
            f"\nNo likely prompt templates matching the v4 criteria found or saved to '{output_file}'."
        )
        print(
            "Consider adjusting filtering keywords or min_length if prompts are missed."
        )
    else:
        print("Extraction failed due to an error.")
