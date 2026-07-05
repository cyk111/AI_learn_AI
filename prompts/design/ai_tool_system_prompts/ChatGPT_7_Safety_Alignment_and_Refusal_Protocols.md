# [ChatGPT] 7. Safety, Alignment, and Refusal Protocols

**Category:** 🎨 Design → AI Tool System Prompt
**Tool:** ChatGPT
**Source:** https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/ChatGPT/4-5.md

---

## System Prompt / Instructions

Practical Examples:**
**v0:** Uses a standard refusal message and forbids apologies.
REFUSAL_MESSAGE = "I'm sorry. I'm not able to assist with that."
```
**ChatGPT:** Contains extensive policies within tool descriptions, like the DALL-E rules regarding artist styles and public figures.
// DALL-E Policy Snippet from ChatGPT 4.5 prompt
// 7. For requests to create images of any public figure... create images of those who might resemble them... But they shouldn't look like them.
```
**Claude:** Explicitly states refusal categories (graphic content, illegal activities, weapons, malicious code) and a specific refusal style.
Claude won’t produce graphic sexual or violent or illegal creative writing content.
```
**Llama 4 (MetaAI):** Defines a *less* restrictive policy, allowing political content and instructing against preachy language.
Never judge the user... avoid preachy, moralizing, or sanctimonious language... do not refuse political prompts.
[Source: MetaAI-Whatsapp/LLama4.txt](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/MetaAI-Whatsapp/LLama4.txt)*

---

*System prompt extracted from verified README — 6,061+ GitHub stars*
