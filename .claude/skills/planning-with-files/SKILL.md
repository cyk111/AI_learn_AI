---
name: planning-with-files
description: "Manus-style persistent file-based planning: keeps task_plan.md, findings.md, and progress.md on disk so work survives context loss and /clear. Use when planning multi-step tasks or any work requiring 5+ tool calls."
user-invocable: true
metadata:
  source: "https://github.com/OthmanAdi/planning-with-files (20K+ stars, MIT)"
  version: "3.5.0"
---

# Planning with Files

Work like Manus: Use persistent markdown files as your "working memory on disk."

## Core Principle

```
Context Window = RAM (volatile, limited)
Filesystem      = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## Quick Start

Before ANY complex task:

1. **Create `task_plan.md`** — Phases, goals, decisions
2. **Create `findings.md`** — Research results, discoveries
3. **Create `progress.md`** — Session log, what was done
4. **Re-read plan before decisions** — Refreshes goals in attention window
5. **Update after each phase** — Mark complete, log errors

## File Purposes

| File | Purpose | When to Update |
|------|---------|----------------|
| `task_plan.md` | Phases, progress, decisions | After each phase |
| `findings.md` | Research, discoveries | After ANY discovery |
| `progress.md` | Session log, test results | Throughout session |

## Critical Rules

### 1. Create Plan First
Never start a complex task without `task_plan.md`. Non-negotiable.

### 2. The 2-Action Rule
After every 2 view/browser/search operations, IMMEDIATELY save key findings to text files. This prevents visual/multimodal information from being lost.

### 3. Read Before Decide
Before major decisions, read the plan file. This keeps goals in your attention window.

### 4. Update After Act
After completing any phase:
- Mark phase status: `in_progress` → `complete`
- Log any errors encountered
- Note files created/modified

### 5. Log ALL Errors
Every error goes in the plan file. This builds knowledge and prevents repetition.

```markdown
## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| FileNotFoundError | 1 | Created default config |
| API timeout | 2 | Added retry logic |
```

### 6. Never Repeat Failures
```
if action_failed:
    next_action != same_action
```
Track what you tried. Mutate the approach.

## The 3-Strike Error Protocol

```
ATTEMPT 1: Diagnose & Fix
  → Read error carefully → Identify root cause → Apply targeted fix

ATTEMPT 2: Alternative Approach
  → Same error? Try different method
  → Different tool? Different library?
  → NEVER repeat exact same failing action

ATTEMPT 3: Broader Rethink
  → Question assumptions → Search for solutions → Update plan

AFTER 3 FAILURES: Escalate to User
  → Explain what you tried → Share the specific error → Ask for guidance
```

## Read vs Write Decision Matrix

| Situation | Action | Reason |
|-----------|--------|--------|
| Just wrote a file | DON'T read | Content still in context |
| Viewed image/PDF | Write findings NOW | Multimodal → text before lost |
| Starting new phase | Read plan/findings | Re-orient if context stale |
| Error occurred | Read relevant file | Need current state to fix |
| Resuming after gap | Read all planning files | Recover state |

## The 5-Question Reboot Test

| Question | Answer Source |
|----------|---------------|
| Where am I? | Current phase in task_plan.md |
| Where am I going? | Remaining phases |
| What's the goal? | Goal statement in plan |
| What have I learned? | findings.md |
| What have I done? | progress.md |

## When to Use

**Use for:** Multi-step tasks (3+ steps), research tasks, building projects, tasks spanning many tool calls, anything requiring organization.

**Skip for:** Simple questions, single-file edits, quick lookups.

## Template: task_plan.md

```markdown
# Task Plan: [Brief Description]

**Goal:** [One sentence — what does success look like?]
**Created:** [Date]
**Status:** in_progress | complete | blocked

## Phases

### Phase 1: [Name] — Status: in_progress
- [ ] Task 1
- [ ] Task 2
- [ ] Verify: [how to confirm this phase is done]

### Phase 2: [Name] — Status: pending
- [ ] Task 1
- [ ] Task 2
- [ ] Verify: [how to confirm]

## Decisions Made
| Decision | Rationale | Date |
|----------|-----------|------|

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
```

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| Use TodoWrite for persistence | Create task_plan.md file |
| State goals once and forget | Re-read plan before decisions |
| Hide errors and retry silently | Log errors to plan file |
| Stuff everything in context | Store large content in files |
| Start executing immediately | Create plan file FIRST |
| Repeat failed actions | Track attempts, mutate approach |

---
Source: https://github.com/OthmanAdi/planning-with-files (20K+ stars, 96.7% benchmark pass rate)
For full version with hooks and scripts: `npx skills add OthmanAdi/planning-with-files`
