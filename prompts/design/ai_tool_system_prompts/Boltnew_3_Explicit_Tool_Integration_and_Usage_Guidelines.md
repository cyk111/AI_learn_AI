# [Bolt.new] 3. Explicit Tool Integration and Usage Guidelines

**Category:** 🎨 Design → AI Tool System Prompt
**Tool:** Bolt.new
**Source:** https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Bolt.new/prompts.ts

---

## System Prompt / Instructions

Practical Examples:**
**ChatGPT:** Provides function schemas (TypeScript definitions) and detailed policies directly within the prompt for tools like `dalle` and `canmore`.
// Example for dalle tool policy within ChatGPT prompt
// Create images from a text-only prompt.
// The size of the requested image...
// The number of images to generate...
// The detailed image description...
// If the user references a previous image...
}) => any;
```
**same.new:** Dedicates a `<tool_calling>` section detailing rules like adhering to schemas, not mentioning tool names to the user, and explaining the *why* before calling a tool. References `functions-schema.json` (not shown in full, but implied structure).
<tool_calling>
1. ALWAYS follow the tool call schema exactly...
5. Before calling each tool, first explain to the USER why you are calling it.
```
**Manus:** Defines tools externally in `tools.json` (schema provided) and includes rules in `Modules.md` like prioritizing data APIs over web search.
// Snippet from Manus/tools.json
"type": "function",
"name": "shell_exec",
"parameters": { ... }
}
[Source: Manus/tools.json](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Manus/tools.json)* | *[Rules: Manus/Modules.md](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Manus/Modules.md)*
**Cline & Augment:** Integrate detailed tool descriptions, parameters, and usage examples directly into the main system prompt using XML-like tags or structured text.
// Cline example tool definition
Description: Request to execute a CLI command...
- command: (required) The CLI command...
Usage:
<command>Your command here</command>
true or false</requires_approval>
```
**Bolt.new:** Uses a dedicated `<artifact_instructions>` section detailing how to format tool outputs (`<boltAction type="shell">`, `<boltAction type="file" filePath="...">`) within a main `<boltArtifact>` tag.
**v0:** Defines custom MDX components like `<CodeProject>`, `<QuickEdit>`, `<DeleteFile />` as its 'tools', with rules on when and how to use them within responses.

---

*System prompt extracted from verified README — 6,061+ GitHub stars*
