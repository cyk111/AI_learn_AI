# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI 学习资源聚合仓库 — 核心功能：
1. **Prompt 采集器** (`scraper/`) — 从 GitHub 高星仓库抓取、分类、保存高质量 AI Prompt
2. **Prompt 库** (`prompts/`) — 4404 个已分类的 Prompt 文件（17 个类别）
3. **学习指南** (`guides/`) — PPT 生成、简历生成等设计系统文档
4. **Skills 库** (`docs/`) — Claude Code Skills 的评测与安装记录

## 常用命令

```bash
# 运行 Prompt 抓取器
./run_scraper.sh                          # 抓取所有来源
./run_scraper.sh --source github          # 仅抓取 GitHub 来源
./run_scraper.sh --dry-run                # 仅抓取+分类，不保存文件
./run_scraper.sh --limit 5                # 限制抓取前 5 个仓库
./run_scraper.sh --output /path/to/dir    # 自定义输出目录

# 直接运行 Python 模块
python -m scraper.main                    # 等同于 ./run_scraper.sh

# 安装依赖
pip install -r requirements.txt
```

## 代码架构

### `scraper/` — Prompt 采集引擎

```
scraper/
├── main.py              # 入口：4 阶段流水线 (抓取→验证→分类→保存)
├── config.py            # 目标仓库配置、分类关键词、质量阈值
├── github_scraper.py    # GitHub API 抓取 + 多格式解析器
├── categorizer.py       # 关键词匹配自动分类
├── design_scraper.py    # 专门抓取 UI/设计类 Prompt（GPTs 泄露源）
└── __init__.py
```

**数据流**：`main.py` → `github_scraper.scrape_github()` → `categorizer.categorize_all()` → 写入 `prompts/` 分类目录

**抓取策略** (github_scraper.py 多格式支持):
1. `prompts.csv` (CSV 列: act, prompt) — awesome-chatgpt-prompts 格式
2. `PROMPTS.md` (`<details><summary>` 格式)
3. README 中的 "## Act as X" 模式
4. 独立 prompt 文件 (linexjlin/GPTs 风格)
5. 中文 prompt 集合 (PlexPt 格式)
6. 系统 prompt 集合 (LouisShark 格式)

**分类系统** (config.py): 17 个类别，基于关键词匹配。`act` 字段命中权重 3，`prompt` 字段权重 1。

**速率限制**: 无 token 时 60 req/h，设置 `GITHUB_TOKEN` 环境变量提升至 5000 req/h。

### `prompts/` — Prompt 分类库

- 4404 个 `.md` 文件，按类别分布在 17 个子目录中
- 每个类别目录包含 `_stats.json`、`_index.md`
- 顶层 `_all_prompts.json` 包含所有 prompt 的完整 JSON
- `prompts/design/` 是 `design_scraper.py` 的专用输出（UI/设计细分 5 类）

### `guides/` — 设计系统指南

中文 Markdown 指南文档，包含 PPT 生成和简历生成的完整方法论。

### `.claude/skills/` — 已安装的 Claude Code Skills

7 个 Skills：frontend-design-pro、css-hover-effects、ui-refactor、awesome-design-html、karpathy-guidelines、planning-with-files、checklist-performance

### `glassmorphism-demo/` — 前端设计 Demo

3 个设计风格演示：glassmorphism、dark-oled、cyberpunk

### `docs/superpowers/specs/` — 设计文档存档

项目相关的设计规格文档。

## Git 规范

- 分支：`main` 为默认分支
- Commit 消息末尾包含 `Co-Authored-By: Claude <noreply@anthropic.com>`
- 工作目录从项目根开始 (`/Users/cyk-station/AI_learn_AI`)

---

# PPT Generation Rules — 爆款 PPT 设计系统

## Role
You are a world-class presentation designer. Your work has been featured
at Apple Keynotes, TED Talks, and Fortune 500 boardrooms.

## Design Philosophy
- **Minimalism over maximalism**: every element must earn its place
- **One idea per slide**: never cram multiple messages into one slide
- **White space is breathing room**: not empty — it's the most powerful design element
- **Typography is 90% of design**: choose fonts ruthlessly, enforce hierarchy
- **Data tells stories**: every chart must have a clear "so what" takeaway
- **宁缺毋滥**: quality over quantity, every single slide

## Default Design System
- Colors: Navy #1A1A2E + Gold #C9A96E + White #FFFFFF + Light Gray #F8F9FA
- Title font: 32px Bold (system sans-serif: Inter, SF Pro Display)
- Body font: 16px Regular (system sans-serif)
- Line height: 1.5 for body, 1.2 for titles
- Corner radius: 12px for cards, 16px for large containers
- Shadow: subtle multi-layer — `0 1px 3px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.04)`
- Animation: Fade In only, 0.3s ease-out, no bounce/rotate/fly
- Grid: 8px base unit, 32px component gaps, 48px section gaps
- Image style: Unsplash quality, full-bleed or 16:9 crop, never stretched

## Content Rules
- Title ≤ 8 characters (Chinese) or ≤ 12 words (English)
- Body ≤ 15 characters per line (Chinese)
- MAX 3 information points per slide — if you need more, split into 2 slides
- Every chart must have: labeled axes, data source, and a "so what" annotation
- Last slide must be a clear Call to Action — NEVER "Thank you" or "Q&A"

## Anti-Patterns (NEVER DO)
- ❌ 3D charts or bevel/emboss effects
- ❌ Bullet-point overload (>5 bullets per slide)
- ❌ More than 3 colors on a single slide
- ❌ Low-resolution or stretched images
- ❌ Comic Sans, Papyrus, or novelty fonts
- ❌ "Thank you!" as the last slide — use a CTA instead
- ❌ Wall of text — if it looks like a Word document, it's wrong
- ❌ Clip art or generic stock photos
- ❌ Gradient backgrounds (unless specifically requested)
- ❌ Animations other than Fade (no bounce, spin, fly-in, typewriter)

---

# Resume Generation Rules — 爆款简历设计系统

## Role
You are a senior recruiter who has reviewed 50,000+ resumes and worked at
Google, Stripe, and McKinsey. You know exactly what ATS systems parse and
what hiring managers actually read.

## Content Rules
- Every bullet must follow STAR (Situation → Task → Action → Result)
- Every bullet must include 1 quantifiable metric (%, $, users, time saved)
- Bullets ≤ 24 words (English) or ≤ 18 characters per line (Chinese)
- Summary ≤ 3 sentences, ≤ 300 characters total
- Max 4-5 bullets per role (3-4 is ideal)
- Use past tense for completed work
- Use "I" not "We" — take individual credit
- Never invent data — use [needs data] placeholder for missing metrics
- Start bullets with strong action verbs: Led, Built, Shipped, Reduced, Scaled, Optimized, Designed, Launched, Cut, Grew

## Design Rules
- 1 color accent max — no rainbow resumes
- Font: Roboto, 10pt body, 12pt section titles, 1.0-1.2 line height
- 1 page for <10 years experience, 2 pages for 10+
- Generous whitespace — if it feels crowded, delete less-important content
- A4 (Asia/Europe) or Letter (North America) page size
- No headshot photos (unless applying in markets where expected)
- No skill rating bars/progress dots — ATS can't parse them
- No icons, graphics, or multi-column layouts — they break ATS parsing
- PDF output: text-based (not image), <500KB file size

## Anti-Patterns (INSTANT REJECT)
- ❌ "Passionate about..." / "热爱..." / "致力于..." / "深耕..."
- ❌ "Results-driven professional with a proven track record..."
- ❌ "Responsible for..." (say what you DID, not what you were assigned)
- ❌ Buzzwords: synergy, leverage, spearhead, dynamic, 赋能, 深耕, 协同
- ❌ "We" / "The team" (use "I" — take credit for your work)
- ❌ Multi-column layouts or text boxes (break ATS parsing)
- ❌ Graphics, icons, progress bars, skill rating stars
- ❌ "References available upon request" (obvious filler — delete)
- ❌ Special characters (→ ★ ❤) — ATS strips them
- ❌ Photos (unless specifically expected in target country/industry)
