# Claude Code Skills 技能库文档

> 2026-07-13 | 宁缺毋滥原则 | 从 GitHub/X 社区筛选的顶级 Claude Code Skills

---

## 📋 目录

1. [已安装 Skills（7个）](#已安装-skills)
2. [UI/设计 Skills 详情](#ui设计-skills-详情)
3. [评估但未安装的高质量 Skills](#评估但未安装的高质量-skills)
4. [Skills 安装方式对比](#skills-安装方式对比)
5. [推荐组合方案](#推荐组合方案)
6. [数据来源与星标排行](#数据来源与星标排行)

---

## 已安装 Skills

### 🎨 UI / 前端设计（4个）

| # | Skill | Stars | 来源 | 核心能力 |
|---|-------|-------|------|----------|
| 1 | `frontend-design-pro` | — | [claudekit/frontend-design-pro-demo](https://github.com/claudekit/frontend-design-pro-demo) | 11 种美学风格引擎 |
| 2 | `css-hover-effects` | 29.4K | [dabaibian/css-skills](https://github.com/dabaibian/css-skills) | 20+ 纯 CSS 悬停特效，自动风格匹配 |
| 3 | `ui-refactor` | — | [LovroPodobnik/refactoring-ui-skill](https://github.com/LovroPodobnik/refactoring-ui-skill) | Refactoring UI 方法论 |
| 4 | `awesome-design-html` | — | [yzfly/awesome-design-html](https://github.com/yzfly/awesome-design-html) | 118 品牌设计系统参考库 |

### 🛠️ 工程方法论（3个）

| # | Skill | Stars | 来源 | 核心能力 |
|---|-------|-------|------|----------|
| 5 | `karpathy-guidelines` | 131K | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | 4 条编码行为准则 |
| 6 | `planning-with-files` | 20K | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Manus 风格持久化任务规划 |
| 7 | `checklist-performance` | 42K | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Web 性能优化清单 |

---

## UI/设计 Skills 详情

### 1. frontend-design-pro — 11 种美学风格

**安装路径**: `.claude/skills/frontend-design-pro/SKILL.md` (6.3KB)

支持的 11 种美学方向：

| # | 风格 | 关键词 | 标志性效果 |
|---|------|--------|-----------|
| 1 | **Glassmorphism** 毛玻璃 | frosted glass, translucent, blur | `backdrop-filter: blur()`, 发光边框, 浮动层 |
| 2 | **Dark OLED Luxury** 暗黑奢华 | deep black, glow, premium | #000 背景, 琥珀/翡翠/电光蓝点缀, 聚光灯效果 |
| 3 | **Neumorphism** 新拟物 | soft UI, embossed, concave/convex | 多层柔和阴影, 按压释放动画 |
| 4 | **Brutalism** 野兽派 | raw, asymmetric, high contrast | 尖锐边角, 巨大粗体, 暴露网格 |
| 5 | **Cyberpunk** 赛博朋克 | neon glow, CRT scanlines, glitch | 扫描线, 色差, 故障转场, 霓虹阴影 |
| 6 | **Swiss Minimalism** 瑞士极简 | grid-based, typography-first | 剃刀般锐利的层级, 微妙悬浮, 完美对齐 |
| 7 | **Claymorphism** 粘土风 | chunky 3D, toy-like, bubbly | 内外阴影, 软塌按键效果, 超大圆角 |
| 8 | **Aurora/Mesh Gradient** 极光渐变 | mesh gradient, luminous, flowing | 动画 CSS/SVG 渐变, 色彩呼吸 |
| 9 | **3D Hyperrealism** 3D 超写实 | WebGL, realistic textures | Three.js, 物理运动, 逼真光照 |
| 10 | **Vibrant Maximalist** 撞色极繁 | bold blocks, duotone, geometric | 大色块, scroll-snap, 戏剧性悬浮 |
| 11 | **Organic/Biomorphic** 有机流体 | fluid shapes, blobs, curved | SVG 变形, gooey 效果, 不规则边框 |

**核心规则**:
- 禁止 Inter/Roboto/Arial — 使用 Clash Display, Space Grotesk, Satoshi
- CSS 自定义属性系统（`:root` 令牌）
- 至少一个不可忘记的标志性细节（噪点、自定义光标、动画网格、对角分割）
- 打破居中卡片网格：不对称、重叠、对角线流
- 英雄级动画 > 散落微交互
- 极端字体层级：3 倍+ 大小跳跃，粗细对比（100 vs 900）

**触发词**: "landing page", "hero section", "dashboard UI", "redesign", "make it look premium", "stunning UI"

---

### 2. css-hover-effects — 20+ CSS 悬停特效

**安装路径**: `.claude/skills/css-hover-effects/SKILL.md` (8.1KB)

**自动风格检测 → 效果匹配流程**:
1. 读取现有 CSS 信号（border-radius, saturation, transitions, shadows, fonts）
2. 归类为 MINIMAL / BOLD / PLAYFUL / CORPORATE / DARK-PREMIUM
3. 从兼容性矩阵选择匹配效果
4. 输出可复制的 CSS

**效果库**:

| 类别 | 效果名称 | 适用场景 |
|------|---------|----------|
| 2D 变换 | Float, Grow, Pop, Shrink, Bob, Wobble, Buzz | 卡片、按钮、图标 |
| 背景过渡 | Background Fade, Sweep to Right, Shutter In, Radial Out | CTA 按钮、导航项 |
| 边框底线 | Underline From Center/Left, Border Fade, Ripple Out, Reveal | 导航链接、输入框 |
| 阴影发光 | Glow, Shadow, Shadow Radial | 暗色主题、高级卡片 |
| 图标 | Icon Forward/Float/Spin/Grow | 工具栏、侧边栏图标 |
| 气泡 | Bubble Top/Bottom | 工具提示、悬停说明 |

**关键原则**:
- MINIMAL 风格最多 2 个效果，duration ≤ 250ms
- CORPORATE 仅 Background Fade + Underline + Border + 微妙 Float
- DARK-PREMIUM 优先 Glow 和 Shadow Radial
- PLAYFUL 可组合 2 个效果
- 永远不混合 Sweep+Float, Wobble+Buzz

**触发词**: "hover effect", "feels flat", "add interaction", "card hover", "button hover", "micro-interaction"

---

### 3. ui-refactor — UI 重构方法论

**安装路径**: `.claude/skills/ui-refactor/SKILL.md` (5.9KB)

基于 "Refactoring UI" 经典原则：

**四步工作流**:
1. **Feature First** — 不设计外壳（导航栏、侧边栏），从功能开始
2. **Low Fidelity** — 灰度设计，先解决布局间距
3. **Define Systems** — 间距量表、字体阶梯、配色系统
4. **Refine** — 应用层级、深度、润色策略

**核心系统**:
- 间距量表：`4px → 8px → 16px → 24px → 32px → 48px → 64px → 96px`
- 字体阶梯：`12px → 14px → 16px → 18px → 20px → 24px → 30px → 36px → 48px`
- 60-30-10 配色法则
- HSL 色彩体系（不用 Hex）
- 阴影语言：sm → md → lg → xl 四级深度

**快速启发式**:
- 两个选项选不定 → 约束到预定义量表
- 严肃/优雅 = 衬线 + 尖角 + 金/蓝，俏皮/友好 = 圆体 + 大圆角 + 粉/橙
- 先设计快乐路径，再迭代边缘情况
- 单个屏幕不超过 3 种颜色（不含灰度）

**触发词**: "make this look better", "fix this UI", "design system", "cluttered interface", "CSS help"

---

### 4. awesome-design-html — 118 品牌设计参考

**安装路径**: `.claude/skills/awesome-design-html/SKILL.md` (5.9KB)

**品牌索引**:

**🇨🇳 中国品牌（22个）**:
- 字节系: 飞书, 抖音, 豆包
- 阿里系: 阿里云, 支付宝, 钉钉, 语雀
- 腾讯系: 腾讯云, 微信
- 国产 AI: DeepSeek, Kimi, 文心一言, 通义千问
- 新能源车: 小米汽车, 蔚来, 理想, 极氪
- 内容/消费: 哔哩哔哩, 米哈游, 小米, 小红书

**🌍 全球品牌（73个）**:
- 设计标杆: Stripe, Linear, Notion
- SaaS: Airtable, Slack, Figma, Framer, Webflow
- AI: Claude, Cursor, Lovable, Mistral
- 金融: Stripe, Coinbase, Revolut
- 汽车: Tesla, Ferrari, BMW, Bugatti
- 消费: Airbnb, Nike, Spotify, Starbucks

**📱 iOS 应用（22个）**: Instagram, Spotify, TikTok, WhatsApp, ChatGPT, Notion, Netflix...

**使用方法**: 匹配品牌 → 提取设计令牌（颜色、字体、圆角、阴影、Hero 原型）→ 适配到用户项目

**触发词**: "做个Linear风格的页面", "参考Stripe的hero", "飞书风的设计", "Spotify Now Playing"

---

## 评估但未安装的高质量 Skills

这些 skills 同样优秀，但因为复杂度、使用场景、或与已安装的重复而暂未安装。

| 仓库 | Stars | 未安装原因 | 推荐安装方式 |
|------|-------|-----------|-------------|
| **garrytan/gstack** | 97K | 太重：需编译二进制、Playwright 浏览器、~200MB 工具链。团队级项目才需要 | `git clone` + `./setup` |
| **pbakaus/impeccable** | 27.6K | 完整的 npm 包，有 21 个命令（audit/polish/critique/animate/distill）。与 frontend-design-pro 有部分重叠 | `npx impeccable` |
| **mattpocock/skills** | 84K | 文档式方法论（非标准 SKILL.md 格式），TypeScript 工程工作流。需要额外安装器 | `npx skills add mattpocock/skills` |
| **anthropics/skills** | 135K | 官方仓库（PDF/DOCX/PPTX/webapp-testing/algorithms）。你的项目已有部分能力 | `/plugin install anthropics/skills` |
| **nextlevelbuilder/ui-ux-pro-max** | 62.6K | 240+ 样式、127 字体配对。与已安装的 frontend-design-pro 高度重叠 | `/plugin add nextlevelbuilder/ui-ux-pro-max-skill` |
| **obra/superpowers** | 192K | 已内置于 Claude Code 系统级别（brainstorming/writing-plans/TDD 等 14 个 skills） | 已内置 |
| **addyosmani/agent-skills** | 42K | Agents 已内置于系统中（code-reviewer/test-engineer 等）。仅提取了 checklist-performance | — |
| **freshtechbro/claudedesignskills** | — | 23 种动画引擎（GSAP/Three.js/Framer Motion 等），专业动画项目才需要 | `/plugin marketplace add freshtechbro/claudedesignskills` |
| **sasaki-ta-instyle/skill-design-system-liquid** | — | Liquid Glass 设计系统，700+ 行规范。仅适合玻璃态特定项目 | Clone 到 `~/.claude/skills/` |
| **xiaopu-ai/web-design** | — | 先写 DESIGN.md → 审批 → 生成。适合需要设计审批流程的团队 | Clone 使用 |

---

## Skills 安装方式对比

| 方式 | 适用场景 | 示例 |
|------|---------|------|
| **手动复制 SKILL.md** | 轻量 skill，无外部依赖 | karpathy-guidelines, ui-refactor |
| **`/plugin install`** | 官方/社区插件，需要自动更新 | `anthropics/skills`, `superpowers` |
| **`/plugin marketplace add`** | 第三方插件市场 | `freshtechbro/claudedesignskills` |
| **`npx skills add`** | npm 生态的 skills | `mattpocock/skills`, `addyosmani/agent-skills` |
| **`git clone` + `./setup`** | 需要编译二进制的大型工具 | `garrytan/gstack` |
| **`claude mcp add`** | MCP 服务器集成 | Playwright, GBrain |

---

## 推荐组合方案

### 方案 A: 全栈开发者（当前安装 ✅）
```
工程方法: karpathy-guidelines + planning-with-files
UI 设计:   frontend-design-pro + css-hover-effects + ui-refactor + awesome-design-html
性能:      checklist-performance
```
> 7 个 skills，共 37KB。零依赖，即装即用。

### 方案 B: 重前端/设计导向
在方案 A 基础上增加：
```bash
npx impeccable                          # 21 个前端设计命令
/plugin add nextlevelbuilder/ui-ux-pro-max-skill  # 240+ 样式
claude mcp add playwright -s user -- npx @playwright/mcp@latest  # 浏览器预览
```

### 方案 C: 团队/企业级
在方案 A 基础上增加：
```bash
git clone https://github.com/garrytan/gstack.git  # 23 角色 + 完整 sprint 流程
/plugin install anthropics/skills                  # 官方文档处理能力
```

### 方案 D: 极简主义
仅安装最核心的 3 个：
```
karpathy-guidelines + frontend-design-pro + planning-with-files
```
> 总共 14KB，覆盖 90% 的日常需求。

---

## 数据来源与星标排行

### 主要参考仓库（按 GitHub Stars 排序，截至 2026-07）

| 排名 | 仓库 | Stars | 类型 |
|------|------|-------|------|
| 1 | **obra/superpowers** | 192K | TDD 工程方法论 |
| 2 | **affaan-m/everything-claude-code** | 182K | 综合 skills 集合 |
| 3 | **anthropics/skills** | 135K | 官方 skills |
| 4 | **forrestchang/andrej-karpathy-skills** | 131K | 编码行为准则 |
| 5 | **garrytan/gstack** | 97K | 全栈开发套件 |
| 6 | **mattpocock/skills** | 84K | TypeScript 工程 |
| 7 | **nextlevelbuilder/ui-ux-pro-max** | 62.6K | UI/UX 设计 |
| 8 | **shanraisshan/claude-code-best-practice** | 53.6K | 百科全书参考 |
| 9 | **ruvnet/ruflo** | 51K | 多 Agent 编排 |
| 10 | **hesreallyhim/awesome-claude-code** | 46.4K | 精选列表 |
| 11 | **addyosmani/agent-skills** | 42K | SDLC 全生命周期 |
| 12 | **ComposioHQ/awesome-claude-skills** | 34.5K | 850+ SaaS 集成 |
| 13 | **anthropics/claude-plugins-official** | 29.8K | 官方插件注册表 |
| 14 | **dabaibian/css-skills** | 29.4K | CSS 悬停效果 |
| 15 | **pbakaus/impeccable** | 27.6K | 前端设计语言 |
| 16 | **OthmanAdi/planning-with-files** | 20K | 文件持久化规划 |
| 17 | **supermemoryai/supermemory** | 16.7K | 跨会话记忆引擎 |
| 18 | **alirezarezvani/claude-skills** | 15.4K | 313+ skills |
| 19 | **Lum1104/Understand-Anything** | 12K | 代码 → 知识图谱 |
| 20 | **slavingia/skills** | 7.5K | 创始人 skills |

### 搜索关键词记录

```
"best Claude Code skills custom slash commands GitHub 2025 2026"
"Claude Code .claude/skills workflow pack popular github repository"
"Claude Code superpowers skills plugin development community best practices"
"best Claude Code UI design skills stunning frontend CSS 2025 2026 github"
"Claude Code impeccable frontend design skill animations glassmorphism"
"claude code frontend design skill beautiful UI components CSS effects 2025"
```

### 社区资源链接

- **Claude Code 官方插件市场**: https://claude.com/plugins
- **前端设计技能博客**: https://claude.com/blog/improving-frontend-design-through-skills
- **前端美学编码 Cookbook**: https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics
- **awesome-claude-code 精选列表**: https://github.com/hesreallyhim/awesome-claude-code
- **Claude Code 前端设计工具包**: https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit
- **Skills Playground**: https://skillsplayground.com

---

## 选型原则

1. **宁缺毋滥**: 7 个而非 70 个，每个都必须经过验证
2. **轻量优先**: 全部 skills 共 37KB，无需编译、无外部依赖
3. **不重复**: 已有 superpowers 系统级 skills，不装重复功能
4. **实用主义**: 每个 skill 必须有明确的触发场景和「安装后立刻能用到」的价值
5. **炫酷效果优先**: UI skills 选择能产出 $50k+ 代理商级别视觉效果的

---

> 最后更新: 2026-07-13 | 维护者: @cyk-station
