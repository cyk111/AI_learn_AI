# [same.new] 5. Environment and Context Awareness

**Category:** 🎨 Design → AI Tool System Prompt
**Tool:** same.new
**Source:** https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/same.new/same.new.md

---

## System Prompt / Instructions

Practical Examples:**
**Cline:** Includes a `SYSTEM INFORMATION` section.
SYSTEM INFORMATION
Operating System: ${osName()}
Home Directory: ${os.homedir().toPosix()}
```
**Bolt.new:** Provides detailed `<system_constraints>` about the WebContainer environment.
<system_constraints>
</system_constraints>
[Source: Bolt.new/prompts.ts](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Bolt.new/prompts.ts)*
**Manus:** Details the sandbox environment.
<sandbox_environment>
- Ubuntu 22.04 (linux/amd64), with internet access
...
- Python 3.10.12...
</sandbox_environment>
[Source: Manus/Modules.md](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/Manus/Modules.md)*
**same.new:** Notes the OS and specific IDE context.
The OS is Linux 5.15.0-1075-aws (Ubuntu 22.04 LTS). Today is Tue Apr 08 2025.
USER can see a live preview... in an iframe...
[Source: same.new/same.new.md](https://github.com/dontriskit/awesome-ai-system-prompts/blob/main/same.new/same.new.md)*

---

*System prompt extracted from verified README — 6,061+ GitHub stars*
