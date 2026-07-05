# [Bolt.new] 4. Step-by-Step Reasoning and Planning

**Category:** 🎨 Design → AI Tool System Prompt
**Tool:** Bolt.new
**Source:** https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Bolt.new/prompts.ts

---

## System Prompt / Instructions

Practical Examples:**
**Manus:** Features the most explicit planning mechanism with its defined `<agent_loop>` in `Modules.md`.
<agent_loop>
1. Analyze Events...
3. Wait for Execution...
5. Submit Results...
</agent_loop>
[Source: Manus/Modules.md](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Manus/Modules.md)*
**v0:** Uses a dedicated thinking phase before generating code.
BEFORE creating a Code Project, v0 uses <Thinking> tags to think through the project structure...
[Source: v0/v0.md](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/v0/v0.md)*
**same.new & Cline:** Mandate waiting for user confirmation/tool results after each step.
ALWAYS wait for user confirmation after each tool use before proceeding. Never assume the success of a tool use...
```
**Bolt.new:** Emphasizes holistic thinking *before* action.
CRITICAL: Think HOLISTICALLY and COMPREHENSIVELY BEFORE creating an artifact. This means: Consider ALL relevant files... Review ALL previous file changes... Analyze the entire project context... Anticipate potential impacts...
[Source: Bolt.new/prompts.ts](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Bolt.new/prompts.ts)*

---

*System prompt extracted from verified README — 6,061+ GitHub stars*
