# 🎯 爆款 PPT 生成完全指南

> **核心原则：宁缺毋滥，高端大气有品位**
> 拒绝模板感、拒绝花哨、拒绝信息过载。
> 追求：极简美学 × 叙事节奏 × 数据可视化 × 品牌一致性

---

## 一、模型选择：谁最适合做 PPT？

| 模型 | PPT 生成能力 | 最佳用途 | 推荐度 |
|------|:-----------:|----------|:------:|
| **Claude Sonnet 4.5** | ⭐⭐⭐⭐⭐ | 全流程：内容+设计+文件生成 | 🥇 首选 |
| **Claude Opus 4.8** | ⭐⭐⭐⭐⭐ | 复杂叙事、高端策略 deck | 🥇 高端首选 |
| **GPT-5 / GPT-4o** | ⭐⭐⭐⭐ | 大纲构思、内容结构化 | 🥈 |
| **Gemini 3.0** | ⭐⭐⭐⭐ | 设计灵感、视觉描述生成 | 🥈 |
| **Kimi K2** | ⭐⭐⭐⭐ | 中文 PPT 快速生成（非敏感数据） | ⚠️ 注意隐私 |

### 🥇 为什么 Claude 是首选？

1. **原生 PPTX 文件生成**（2025年9月上线）：直接在对话中生成 `.pptx` 文件，无需复制粘贴
2. **官方 `pptx` Skill**（`anthropics/skills`）：python-pptx + html2pptx + OOXML 三层架构
3. **Taste-Driven Development（品味驱动开发）**：Microsoft Office Agent 基于 Claude，从高端样本中提取设计模式
4. **文件格式互转**：上传 PDF/Word/CSV → 直接生成 PPT

---

## 二、Skills 配置：Claude Code PPT 技能栈

### 2.1 安装官方 pptx Skill

```bash
# 克隆 Anthropic 官方 Skills
git clone https://github.com/anthropics/skills.git
cp -r skills/pptx ~/.claude/skills/
```

安装后 Claude Code 自动识别，支持：
- 创建新 PPT（封面、正文、图表、表格、封底）
- 18 种内置配色方案（商务风、科技感、暗黑风、极简风等）
- 自动插入表格和图表（柱状图、折线图、饼图）
- 批量替换文案、调整幻灯片顺序、合并多份 PPT
- 自动生成演讲备注

### 2.2 安装 reveal.js Skill（网页 PPT）

```bash
# 在 Claude Code 中执行
/plugin marketplace add ryanbbrown/revealjs-skill
/plugin install revealjs@revealjs-skill
```

适用场景：交互式演示、包含 Chart.js 动态图表、需要部署到 Web

### 2.3 推荐：设置 CLAUDE.md 项目级别 Skill

在项目根目录创建 `.claude/CLAUDE.md`，定义 PPT 生成的默认风格：

```markdown
# PPT 生成规范

## 默认设计系统
- 色彩：主色 #1A1A2E（深邃藏蓝）+ 强调色 #E2B04A（香槟金）+ 辅助色 #F8F9FA（极浅灰）
- 字体：标题 Playfair Display / 正文 Inter 或系统默认无衬线
- 布局：大量留白，每页幻灯片不超过 3 个信息点
- 图表：扁平化设计，禁用 3D 效果
- 动画：仅使用淡入（Fade），禁用花哨转场
- 图片：高质量 Unsplash 图片，拒绝 clip art

## 输出要求
- 每页一个核心观点
- 标题 ≤ 8 个字
- 正文每行 ≤ 15 个字
- 数据必须标注来源
- 最后一页必须是行动号召（CTA）
```

---

## 三、Prompt 模板：从构思到成品

### 🅰️ 快速方案：Claude 直接生成 PPTX

**适用场景**：已有明确内容大纲，需要快速产出 `.pptx` 文件

```text
你是一位世界级演示设计专家，曾为 Apple、Airbnb、Stripe 等顶级公司设计 keynote 和投资人演示。

请基于以下内容大纲，生成一份 12 页的 PowerPoint 演示文稿：

【主题】{填写主题，如：Q3 产品增长策略}
【受众】{填写受众，如：C-level 高管}
【时长】{填写时长，如：20 分钟}
【品牌色】主色 #{主色}，强调色 #{强调色}
【内容大纲】
1. 封面：标题 + 副标题
2. 现状分析：3 个关键数据
3. 问题定义：1 个核心痛点
4. 解决方案：产品方案概述
...（以此类推）

【设计要求】
- 风格：Apple Keynote 极简风，大量留白，每页不超过 3 个信息点
- 色彩：背景纯白 #FFFFFF，主色深灰 #1A1A2E，强调色香槟金 #E2B04A
- 字体：标题使用 Playfair Display Bold，正文使用 Inter Regular 14pt
- 间距：组件间距 ≥ 32px，内边距 ≥ 24px
- 图片：每页配一张高质量代表性图片（Unsplash 风格）
- 图表：使用扁平化柱状图/折线图，禁用 3D 效果和多余网格线
- 动画：仅使用淡入（Fade In），禁用弹跳、旋转等花哨效果
- 最后一页：明确的行动号召 + 联系信息

【输出格式】直接生成 .pptx 文件
```

### 🅱️ 深度方案：从零构思到成品

**适用场景**：只有初步想法，需要 AI 从调研到设计全流程

```text
# Phase 1: 内容策略（用 GPT-5 或 Claude Opus）

你是一位顶级商业策略顾问（前 McKinsey 合伙人级别）。
我需要准备一份关于 {主题} 的演示文稿，受众是 {受众描述}，
时长 {X} 分钟，目标是 {目标描述}。

请完成以下分析：
1. 受众画像：他们的知识水平、关注点、可能的反对意见
2. 叙事弧线：开场钩子 → 问题揭示 → 解决方案 → 证据支撑 → 行动号召
3. 关键信息层级：必须传达的 3 个核心信息
4. 数据需求清单：需要用哪些数据支撑论点
5. 竞品/对标分析：同主题的演讲通常如何组织？（分析 3 个案例）

# Phase 2: 幻灯片架构（用 Claude Opus）

基于 Phase 1 的分析，设计 12 页幻灯片的详细架构。
每页包含：
- 标题（≤ 8 字）
- 核心信息（1 句话）
- 内容形式（文字/图表/图片/引用）
- 视觉建议（配色/构图/留白策略）

# Phase 3: 生成 PPTX（用 Claude + pptx Skill）

基于 Phase 2 的架构，生成最终的 .pptx 文件。
应用以下设计系统：
- {你的品牌设计系统}
```

### 🅲️ 极速方案：一句话出片

```text
帮我生成一份关于 {主题} 的 PPT：
- 风格参考：Apple Keynote 极简风
- 配色：深色背景 + 金色点缀
- 页数：10 页
- 覆盖：封面 → 问题 → 方案 → 数据 → 案例 → 路线图 → 团队 → CTA
- 直接输出 .pptx 文件
```

---

## 四、设计系统：确保"高端大气有品位"

### 4.1 配色方案（3 套经典方案，宁缺毋滥）

#### 方案 A：极简商务（Apple 风格）
```
主色:   #1D1D1F (深邃黑灰)
辅助色: #F5F5F7 (极浅灰)
强调色: #0071E3 (苹果蓝)
文字色: #1D1D1F / #86868B (次级文字)
```
适用：产品发布、投资人演示、企业战略

#### 方案 B：奢华质感（奢侈品风格）
```
主色:   #1A1A2E (午夜藏蓝)
辅助色: #F8F9FA (奶油白)
强调色: #C9A96E (香槟金)
文字色: #2D2D2D / #999999 (次级文字)
```
适用：高端品牌、房地产、金融路演

#### 方案 C：科技未来（暗黑风格）
```
主色:   #0A0A0A (纯黑)
辅助色: #1A1A2E (深蓝黑)
强调色: #00F0FF (赛博青) / #7B61FF (电光紫)
文字色: #FFFFFF / #888888 (次级文字)
```
适用：AI/Web3 项目、技术大会、产品 Demo

### 4.2 排版法则

| 层级 | 字号 | 字重 | 用途 |
|------|:----:|:----:|------|
| H1 封面标题 | 48-72px | Bold 700 | 封面主标题 |
| H2 页标题 | 32-40px | Bold 700 | 每页幻灯片标题 |
| H3 节标题 | 24-28px | SemiBold 600 | 段落标题 |
| Body 正文 | 14-18px | Regular 400 | 正文内容 |
| Caption 注释 | 11-13px | Regular 400 | 数据来源、脚注 |

**铁律**：
- 每页幻灯片不超过 3 个信息层级
- 正文每行不超过 15 个中文字
- 标题和正文之间保留 1.5 倍行距
- 不使用超过 2 种字体（标题 1 种 + 正文 1 种）

### 4.3 视觉系统

```
圆角：统一 8px（卡片）、16px（大容器）
阴影：box-shadow: 0 1px 3px rgba(0,0,0,0.08) — 极度克制
边框：1px solid #E5E7EB — 仅用于必要分隔
动画：仅淡入（Fade）- 禁用弹跳/旋转/飞入
图片：全出血（Full Bleed）或 16:9 裁切
图表：扁平化 2D、禁用 3D、网格线透明化
图标：SF Symbols 风格（细线条、统一粗细）
```

---

## 五、工作流推荐

### 推荐流程：3 步法（总耗时 20-30 分钟）

```
Step 1: 内容构思（5 分钟）
  ├── 工具：GPT-5 或 Claude Opus
  ├── 产出：叙事大纲 + 关键数据 + 受众分析
  └── Prompt：使用 Phase 1 模板

Step 2: 视觉设计（10 分钟）
  ├── 工具：Claude Sonnet 4.5 + pptx Skill
  ├── 产出：完整 .pptx 文件（含设计系统）
  └── Prompt：使用方案 A/B 模板 + 设计系统参数

Step 3: 人工精修（10-15 分钟）
  ├── 替换占位图片为实际素材
  ├── 微调图表数据
  ├── 添加演讲备注
  └── 最终审校
```

### 进阶流程：多 Agent 协作（总耗时 30-40 分钟，品质最高）

```
CLAUDE.md（"创意总监" Agent）
  │
  ├── "分析师" SubAgent
  │   ├── 模型：Claude Sonnet 4.5
  │   ├── 任务：数据处理、竞品分析、数据可视化
  │   └── 产出：分析报告 + 图表数据
  │
  ├── "文案师" SubAgent
  │   ├── 模型：Claude Opus 4.8
  │   ├── 任务：叙事线设计、标题提炼、故事包装
  │   └── 产出：每页演讲稿 + 关键信息
  │
  └── "设计师" SubAgent
      ├── 模型：Claude Sonnet 4.5 + pptx Skill
      ├── 任务：应用设计系统、生成 PPTX 文件
      └── 产出：最终 .pptx 文件
```

---

## 六、开箱即用的 PPT 生成项目文件

### 6.1 CLAUDE.md（放在项目根目录 `.claude/`）

```markdown
# PPT Generation Rules

## Role
You are a world-class presentation designer. Your work has been featured
at Apple Keynotes, TED Talks, and Fortune 500 boardrooms.

## Design Philosophy
- Minimalism over maximalism: every element must earn its place
- One idea per slide: never cram multiple messages
- White space is not empty — it's a design element
- Typography is 90% of design: choose fonts ruthlessly
- Data tells stories: every chart must have a clear "so what"

## Default Design System
- Colors: Navy #1A1A2E + Gold #C9A96E + White #FFFFFF
- Title font: 32px Bold (system sans-serif)
- Body font: 16px Regular (system sans-serif)
- Corner radius: 12px for cards
- Shadow: subtle, multi-layer, never harsh black
- Animation: Fade only, 0.3s duration, no bounce/rotate
- Grid: 8px base unit
- Image style: Unsplash quality, full-bleed or 16:9 crop

## Content Rules
- Title ≤ 8 words (Chinese) or ≤ 12 words (English)
- Body ≤ 15 characters per line (Chinese)
- Max 3 info points per slide
- Every chart must have labeled axes + data source
- Last slide must be a clear Call to Action

## Anti-Patterns (NEVER DO)
- ❌ 3D charts or effects
- ❌ Bullet-point overload (>5 per slide)
- ❌ Clashing colors (>3 colors on one slide)
- ❌ Low-res/stretched images
- ❌ Comic Sans / novelty fonts
- ❌ "Thank you" as the last slide (use CTA instead)
- ❌ Wall of text (if it looks like a Word doc, it's wrong)
```

### 6.2 PPT Prompt 卡片（可直接复制使用）

保存为 `prompts/ppt_prompts/` 下的文件，随时调用。

#### 投资人 Pitch Deck Prompt

```text
You are a former Sequoia Capital partner who has reviewed 10,000+ pitch decks.
Create a 12-slide investor pitch deck for {startup_name}.

【Company】{一句话描述}
【Stage】{融资轮次}
【Ask】{融资金额}

Slide Structure:
1. Title: Company name + one-line value prop
2. Problem: The pain point (1 stat + 1 story)
3. Solution: What we built (1 screenshot + 3 bullet benefits)
4. Why Now: Market timing (1 timeline chart)
5. Market Size: TAM/SAM/SOM (1 visual)
6. Product: Key features (3 screenshots with captions)
7. Traction: Growth metrics (1 line chart + 3 KPIs)
8. Business Model: Revenue model (1 simple diagram)
9. Competitive Landscape: 2x2 matrix or comparison table
10. Team: 3-5 key people (photos + 1-line bio each)
11. Financials: 3-year projection (1 bar chart)
12. The Ask: Amount + use of funds + contact info

Design: Clean, confident, no clutter. Let the numbers speak.
```

#### 产品发布会 Keynote Prompt

```text
You are an Apple Keynote-level presentation designer.
Create a {N}-slide product launch presentation for {product_name}.

【Product】{产品一句话描述}
【Launch Date】{发布日期}
【Key Features】{3 个核心功能}

Style Reference:
- Apple Keynote aesthetic: dark background, large typography,
  full-bleed product images, dramatic reveals
- One feature reveal per slide
- Use "momentum building" structure:
  Tease → Reveal → Demo → Deep Dive → One More Thing → Availability

Slide Structure:
1. Opening: Apple-style event opener (event name + date)
2. Vision: Why we exist (1 sentence, massive type)
3. Problem: The current experience sucks (1 image + 1 stat)
4-6. Feature 1-3: One feature per slide (hero shot + 3-word headline)
7. Demo: Live demo-style screenshots with annotations
8. Technology: What makes it possible (1 architecture diagram)
9. Privacy/Security: Our commitment (1 clear statement)
10. One More Thing: Surprise announcement
11. Pricing & Availability: Date + price + pre-order
12. Closing: Product name + tagline, massive

Design: Dark background (#000000), SF Pro Display font, white text,
product images at enormous scale, minimal text on screen.
```

---

## 七、常见陷阱与避坑指南

| ❌ 错误做法 | ✅ 正确做法 |
|------------|------------|
| 一次性让 AI 生成 30 页 | 分批次：5-8 页一批，保证每批质量 |
| 用模糊的颜色描述（"好看的颜色"） | 提供精确 Hex 色值 + 风格参考对象 |
| 不提供受众信息 | 明确受众身份、知识水平、关注点 |
| 接受 AI 第一版不修改 | 至少迭代 2-3 轮，每轮聚焦不同维度 |
| 文字太多，像 Word 文档 | 每页不超过 15 个字/行，用图表替代文字 |
| 使用默认模板 | 定义专属设计系统（见第四节） |
| AI 生成图表数据编造 | 手动检查所有数据，标注来源 |
| 忽略移动端查看 | 确保在手机上也能看清关键信息 |

---

## 八、总结：最佳实践速查表

| 场景 | 模型 | Skill | 耗时 |
|------|------|-------|:----:|
| 投资人 Pitch | Claude Opus + pptx Skill | 官方 pptx | 10 min |
| 产品发布会 | Claude Opus + pptx Skill | 官方 pptx | 15 min |
| 周报/月报 | Claude Sonnet + pptx Skill | 官方 pptx | 5 min |
| 教学课件 | Claude Sonnet + reveal.js Skill | ryanbbrown/revealjs | 20 min |
| 学术海报 | Claude Opus + python-pptx | 官方 pptx | 15 min |
| 品牌提案 | Claude Opus 手动生成 + Canva 精修 | — | 30 min |
| 多页大型报告 | Claude Code + 多 Agent 协作 | 全套 Skills | 40 min |

---

> **最后的忠告**：AI 能给你 80% — 结构、设计、数据可视化。
> 剩下的 20% — 叙事节奏、情感共鸣、临场发挥 — 才是区分"不错"和"爆款"的关键。
> 把 AI 当作你的 Junior Designer，而你才是 Creative Director。
