# 代码审查/重构 Skills 与工具全景图

> 整理日期：2026-07-14
> 涵盖：Claude Code Skills 生态 + GitHub 开源工具 + AI 代码审查平台

---

## 一、Claude Code 内置 & 官方 Skills

### 1. `/code-review` — 最常用，首选

| 维度 | 说明 |
|------|------|
| **来源** | Anthropic 官方 Plugin |
| **原理** | 启动 5 个并行 Agent 同时审查：① CLAUDE.md 合规 ② Bug 检测 ③ Git blame 历史上下文 ④ PR 历史分析 ⑤ 代码注释审查 |
| **亮点** | 每个发现带 **0-100 置信度评分**，低于阈值（默认 80）自动过滤，大幅降低误报噪音 |
| **使用场景** | **日常提交前的质量门禁** — 你改完代码，跑一遍，只看高置信度问题 |
| **安装** | `/plugin install code-review@claude-plugins-official` |
| **费用** | 免费 |

### 2. `/simplify` — 审查 + 自动修复

| 维度 | 说明 |
|------|------|
| **来源** | Claude Code 内置 |
| **原理** | 3 个并行审查 Agent：复用性 / 代码质量 / 效率。**找到问题后直接帮你修好** |
| **与 code-review 的区别** | code-review 是「找出问题给你看，你自己决定修不修」；simplify 是「找到能简化的地方，AI 直接帮你改了」 |
| **使用场景** | 功能写完觉得代码太啰嗦 — 跑一遍自动精简。重构后检查是否还有冗余 |

### 3. `security-review` — 专注安全

| 维度 | 说明 |
|------|------|
| **来源** | Anthropic 官方 |
| **原理** | 针对 diff 做安全专项审查：注入、认证、密钥泄露、不安全数据处理 |
| **使用场景** | 代码涉及鉴权/加密/支付/用户数据 — 提交前必跑 |

### 4. `/review` — 通用审查

| 维度 | 说明 |
|------|------|
| **来源** | Claude Code 内置 |
| **原理** | 通用代码审查，不限特定维度 |
| **使用场景** | 不需要安全/简化等专项审查，就想让 AI 整体看一遍 |

---

## 二、Superpowers 体系（社区最高安装量）

### 5. `superpowers:requesting-code-review`

| 维度 | 说明 |
|------|------|
| **来源** | obra/superpowers（GitHub 192K+ stars，476K+ 安装量） |
| **原理** | 开发流程中的质量检查节点，TDD + Review Pipeline |
| **使用场景** | **开发中途的代码审查** — 不是等全部写完才审，而是在开发流程中嵌入审查节点 |

### 6. `superpowers:receiving-code-review`

| 维度 | 说明 |
|------|------|
| **来源** | obra/superpowers |
| **原理** | 接收 AI 审查结果后的处理流程 |
| **使用场景** | 跑完 code-review 后，指导你如何处理反馈、哪些优先修 |

### 7. `comprehensive-review:full-review`

| 维度 | 说明 |
|------|------|
| **来源** | Superpowers |
| **原理** | 架构 + 安全 + 代码质量 + 性能 **四维度并行审查** |
| **使用场景** | **里程碑节点/大版本发布前** — 不是日常用，是重要节点用 |

---

## 三、GitHub 社区高质量 Skills

### 8. `timi-ty/agent-forge` — 可复用的 code-review skill

| 维度 | 说明 |
|------|------|
| **来源** | GitHub 社区 |
| **原理** | 8 阶段 PR 审查流程，集成 `gh` CLI，直接在 GitHub PR 上工作 |
| **亮点** | 可移植 — 复制 repo URL 到 Agent Chat 即可安装 |
| **使用场景** | 需要直接在 GitHub PR 上做代码审查（不只是本地 diff） |

### 9. `trailofbits/skills` — 专业安全审计

| 维度 | 说明 |
|------|------|
| **来源** | Trail of Bits（顶级安全审计公司） |
| **原理** | 专业级安全审计 Skill：自动生成 Semgrep 规则、解析 SARIF 文件、供应链风险审计 |
| **亮点** | 这是真正的安全公司做的，不是社区玩具 |
| **使用场景** | 安全关键项目、合约审计、合规审查 |
| **安装** | `/plugin marketplace add trailofbits/skills` |

### 10. `addyosmani/agent-skills` — Google 品质

| 维度 | 说明 |
|------|------|
| **来源** | Addy Osmani（Google 工程师，42K+ stars） |
| **原理** | 覆盖完整 SDLC 生命周期：性能、调试、架构、测试 |
| **亮点** | 来自 Google 内部工程最佳实践 |
| **使用场景** | 性能审查、架构审查 — 需要 Google 级的工程标准 |

### 11. `pbakaus/impeccable` — 前端审查专用

| 维度 | 说明 |
|------|------|
| **来源** | pbakaus（27.6K stars） |
| **原理** | 21 条命令：audit、polish、critique、animate、distill |
| **亮点** | **纯前端设计/交互审查**，跟后端代码审查互补 |
| **使用场景** | 审查前端 UI 质量、交互流畅度、设计一致性 |

### 12. `forrestchang/andrej-karpathy-skills` — 编程哲学

| 维度 | 说明 |
|------|------|
| **来源** | 社区（基于 Karpathy 编程理念） |
| **原理** | 70 行 `CLAUDE.md`：Think Before Coding / Simplicity First / Surgical Changes |
| **使用场景** | **不是跑审查，是改变 AI 写代码的行为模式** — 让 AI 先思考再编码，写出来的代码质量更高 |

---

## 四、开源 AI 代码审查工具（独立运行，不依赖 Claude Code）

### 13. Qodo Merge / PR-Agent — 最流行

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/Codium-ai/pr-agent`（Apache 2.0） |
| **能力** | Agentic diff review、PR 内命令交互、支持 GitHub/GitLab/Bitbucket/Azure DevOps |
| **亮点** | 模型无关（OpenAI/Anthropic/本地模型都行）、可自托管 |
| **使用场景** | **CI/CD 集成** — 每个 PR 自动触发 AI 审查，结果直接评论在 PR 里 |

### 14. Alibaba OpenCodeReview — 企业级精度

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/alibaba/open-code-review`（免费开源） |
| **能力** | 混合架构：确定性管线 + LLM Agent，精准行级评论 |
| **亮点** | 阿里内部上万开发者验证、识别数百万缺陷、**精确率和 F1 显著高于通用 Agent、Token 消耗仅 1/9** |
| **使用场景** | **企业级代码审查** — 需要极高的精确率和低 Token 成本 |

### 15. Gito — 最灵活

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/Nayjest/gito`（MIT，41 个 release） |
| **能力** | 真正的厂商无关 — 支持任何 LLM（OpenAI/Anthropic/Google/Ollama/vLLM/LM Studio） |
| **亮点** | 隐私优先 — 代码直接到你的 LLM，无中间服务器 |
| **使用场景** | **需要数据不出本地的企业**、或者想用本地模型降低 Token 成本 |

### 16. Mira — 全套自托管

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/miracodeai/mira`（MIT） |
| **能力** | 自托管审查引擎 + 代码库索引 + 漏洞扫描 + 自定义规则 + Dashboard |
| **亮点** | 无付费版/无 License Key/无 SaaS 追加销售、中位审查速度 ~77 秒/PR（竞品 5-10 分钟） |
| **使用场景** | **需要一站式解决方案** — 审查 + 漏洞 + 依赖分析 + Dashboard 全有 |

### 17. Ivy Tendril — 质量门禁编排

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/ivy-tendril`（开源） |
| **能力** | 在 PR 到人之前自动运行 build → test → lint → format → AI review 全套验证 |
| **亮点** | 编排 Claude Code / Codex / Antigravity / Copilot / OpenCode 多个 Agent |
| **使用场景** | **CI/CD 质量门禁** — 代码不合规连人眼都到不了 |

### 18. Reviewdog — 老牌 Lint 集成

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/reviewdog/reviewdog`（MIT） |
| **能力** | 将任何 Linter 的输出自动作为 PR 评论发布 |
| **使用场景** | **传统静态分析工具的 PR 集成层** — ESLint/RuboCop 的结果直接评论在 PR 对应行上 |

### 19. h5i — Rust 沙箱多 Agent 审查

| 维度 | 说明 |
|------|------|
| **来源** | `github.com/h5i`（开源，Rust CLI） |
| **能力** | 在隔离沙箱中运行多个编码 Agent，互相做 Peer Review |
| **使用场景** | **多模型交叉验证** — 用不同模型审同一份代码，取交集提高置信度 |

### 20. claude-code-multi-model-review — 多模型并发审查

| 维度 | 说明 |
|------|------|
| **来源** | 社区 Skill |
| **能力** | Claude Code Skill：同时调用 DeepSeek / 豆包 / Qwen / OpenAI 做并发审查，交叉验证结果 |
| **使用场景** | **关键代码用多个模型交叉审查** — 单一模型可能漏的问题被其他模型补上 |

---

## 五、快速索引：按场景选工具

| 你的场景 | 首选 | 备选 |
|---------|------|------|
| **日常提交前快速审查** | `/code-review` | `/simplify` |
| **代码太啰嗦想自动精简** | `/simplify` | — |
| **涉及安全敏感代码** | `/security-review` | `trailofbits/skills` |
| **大版本发布前全面审查** | `comprehensive-review:full-review` | Mira |
| **PR 自动触发审查** | Qodo Merge | Gito |
| **企业级审查（高精度+低成本）** | Alibaba OpenCodeReview | Mira |
| **代码不能出本地** | Gito | Mira |
| **前端 UI/交互审查** | `pbakaus/impeccable` | — |
| **多模型交叉验证** | `claude-code-multi-model-review` | h5i |
| **需要 Dashboard/一站式** | Mira | Qodo Merge SaaS |
| **CI/CD 质量门禁** | Ivy Tendril | Reviewdog |

---

## 六、参考基准

[Code Review Bench](https://github.com/withmartian/code-review-benchmark)（开源，MIT）— 当前行业标准评测基准。使用 **50 个真实 PR**（来自 Sentry/Grafana/Cal.com/Discourse/Keycloak，跨 5 种语言），**1,505 个人工标注的真值问题**（80+ 高级工程师交叉验证）。按 F1、精确率、召回率、速度和 Token 效率排名。

---

## 七、Skill 安装速查

```bash
# 官方市场
/plugin install code-review@claude-plugins-official
/plugin marketplace add trailofbits/skills
/plugin marketplace add anthropics/skills

# npx 一键安装
npx antigravity-awesome-skills --claude    # 1901+ skills 合集
npx skills add vercel-labs/agent-skills

# 社区集合安装（JackyST0）
curl -sL https://raw.githubusercontent.com/JackyST0/awesome-agent-skills/main/install.sh | bash

# 手动克隆到 .claude/skills/
git clone <repo-url> ~/.claude/skills/<skill-name>
```
