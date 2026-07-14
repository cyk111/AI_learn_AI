# 一个律师用 AI 两周写完了对标 Harvey 的法律平台。我花了 8 小时审计他的代码，发现了 9 个 AI 生成代码的「通用病灶」

> 一个前 Latham & Watkins 律师，用 Claude 花了两周，写出了对标百亿美元估值 Harvey 的开源法律 AI 平台。
>
> 项目火了 — 72 小时 1000+ star，法律科技历史最快涨星纪录。国际媒体争相报道。
>
> 我用了 8 个小时，逐行审查了他这 30 万行代码。这篇文章不是来挑律师毛病的。**文章里写的这 9 个问题，你团队里 AI 写的代码 90% 也有。** 跟他会不会编程没关系 — 这是 AI 生成代码的 DNA 缺陷。

---

## 先给你看最触目惊心的几组数字

- **0 个测试文件**。后端 53 个 TS 文件，前端 162 个 TSX/TS 文件，42 个 SQL 迁移。0 个 `.test.ts`。0。
- **10 张核心业务表**的 `user_id` 全部是 `text` 而不是 `uuid`，并且**没有任何外键约束**。删一个用户，10 张表留下孤儿行。
- **7 个 P0 级别安全/数据风险** — 包括一个 OAuth 回调端点完全没有鉴权中间件，任何人都能访问。包括 JSON Body 大小限制函数永远返回 `"50mb"` 且**参数被直接忽略**。
- **1460 行**的单个函数 — `runToolCalls`，包含了 LLM 工具调度的所有逻辑。无法测试，无法维护。
- **19 个 P2 级别问题** — 代码重复、两套认证系统并存、异常被当成正常控制流来用。

**结论：⚠️ 不建议这个项目直接上线面向公众用户。**

但这不是重点。重点是**以下 9 种模式**。

---

## 9 种 AI 生成代码的通病

### 病 #1：大规模代码复制粘贴 — AI 不懂「复用」

`handleDocumentUpload`（~140 行）在 `documents.ts` 和 `projects.ts` 两个文件里**逐字重复**。`countPdfPages`（~15 行）也重复了两遍。

AI 在生成不同路由文件时，不理解项目已有共享模块。每次你让它写一个新端点，它倾向于生成完整的独立实现，而不是 `import` 已有函数。

**自查方法**：全局搜你项目里超过 40 行的函数名，看有没有出现两次。

---

### 病 #2：看着能跑的占位符 — AI 的「假装做完了」

```typescript
// backend/src/index.ts:87-89
function jsonLimitForPath(path: string): string {
  return "50mb"; // 参数 path 被完全忽略
}
```

函数签名完整、类型标注完美、代码能编译、测试也不会报错。但**功能根本没实现**。任何 POST 端点都能接收最大 50MB 的 body 直到服务器内存被耗尽。

AI 擅长写骨架。碰到「需要思考差异化的逻辑」，它经常留一个坑。

**自查方法**：搜只 `return` 一个常量的函数，看参数有没有被用上。

---

### 病 #3：AI 风格注释 — 把心理活动写成了注释

```typescript
// filterAccessibleDocumentIds 的注释：
// "Without this check, a caller with access to any review
//  could attach arbitrary document UUIDs..."
```

这不是给人看的 API 文档。这是 AI 的推理过程。它在跟自己解释「为什么要有这个检查」。高质量，但冗余。6 个月后代码改了、注释忘了改，就成了错误文档。

**自查方法**：如果你的注释在解释「如果没有这行会怎样」，而不是「这行做什么」 — 那是 AI 写的。

---

### 病 #4：零测试 — AI 默认不写测试

不是测试不够。是**完全没有**。0 个测试文件。

AI 生成代码时默认只管写功能。除非你在 System Prompt 或 `.cursorrules` 里明确说「请同时生成单元测试」。对于这个处理法律文件、API 密钥加解密、文档编辑追踪的生产级应用 — 核心模块 `access.ts`（鉴权）、`userApiKeys.ts`（AES-256-GCM 加解密）、`downloadTokens.ts`（HMAC 签名验证）全部没有测试覆盖。

**这可能也是你的项目里最大的定时炸弹。**

---

### 病 #5：数据库类型漂移 — AI 从不重构旧代码

这是整个审计里最有洞察力的发现。看这个对比：

| 10 张早期核心表 | 5 张后期新增表 |
|:--|:--|
| `user_id text` | `user_id uuid` |
| 无外键约束 | `REFERENCES auth.users(id)` |
| RPC 函数里全是 `::text` 补丁 | 不需要类型转换 |

AI 按时间顺序生成迁移文件：早期图省事用 `text`，后面学会用 `uuid` + 外键了，但**从没回头修过旧表**。

**这叫「AI 增量开发，从不重构」。** 你让它加功能，它就加。你让它改旧代码，它不改。除非你主动问它。

---

### 病 #6：两套认证模式并存 — 不同 AI 会话留下不同痕迹

`middleware/auth.ts` 用 Express 的 `res.locals` 存储用户信息。但 `lib/supabase.ts` 里还有一个 `getUserIdFromRequest`，操作 Web 标准的 `Request` 对象。**两套机制解决同一个问题，用不同的方式，没有被统一。**

大概率是不同 AI 会话、不同 prompt 生成的。没有一个「全局架构一致性检查」的环节。

---

### 病 #7：用异常做控制流 — AI 选最快路径，不是最正确路径

```typescript
class AssistantStreamAskInputsPause extends Error { ... }
// 每次用户需要输入 → throw 一个 Error
// 这个 Error 在聊天流里被静默 catch 当成"正常暂停信号"
```

你的 APM / Sentry / Datadog 会报大量 「异常」，而你永远分不清哪个是真的 crash、哪个只是用户点了一个按钮。

---

### 病 #8：静默吞错误 — try/catch 然后 return null

```typescript
async function downloadFile(...): Promise<Buffer | null> {
  try { ... }
  catch { return null; } // 文件不存在？null。权限拒绝？null。网络超时？null。
}
```

调用方只能拿到一个 `null`，无法区分是什么错误。生产环境排障的时候，日志里一片空白。

**自查方法**：搜 `catch` + `return null`，看有多少地方在静默丢错误。

---

### 病 #9：幻觉依赖 — 19.7% 的 AI 推荐包名不存在

研究数据（CSA 2026）：AI 建议的 npm/pip 包名，**19.7% 不存在**。这个项目的 30+ 依赖碰巧全是真实包，因为用了主流 SDK。但如果是小众领域 — AI 的幻觉包名是真实的供应链风险（「slopsquatting」：有人提前注册了 AI 常幻觉的包名，往里放恶意代码）。

**自查方法**：把 `package.json` 里的依赖逐条跑 `npm view <pkg>`，确认每个包都存在。

---

## 公平地说，AI 做对的事情也值得承认

这个项目有几个设计让人眼前一亮：

- **53 个后端 TS 文件，零循环依赖**（madge 验证）
- **LLM Provider 策略模式**非常优雅 — 统一 OpenAI 风格接口，按 tier (MAIN/MID/LOW) 组织模型注册表
- **42 个数据库迁移文件**质量专业：类型检查后再 ALTER、去重后再加 UNIQUE、多阶段列迁移
- **安全做得对的地方**：AES-256-GCM 加密用户 API Key、HMAC-SHA256 + timingSafeEqual 保护下载链接、DOMPurify 清洗前端 HTML
- **访问控制中心化** — `access.ts` 四个函数被所有路由一致使用

**规律：AI 在「有明确对错」的模式上能做好。在「需要理解全局上下文、预判长期风险」的事情上做不好。**

---

## 9 项自查清单（比你项目里任何 lint 规则都有用）

```
□ 1. 全局搜重复函数体 — 超过 40 行且出现两次，就是 AI 的复制粘贴
□ 2. 搜单行 return 常量 — 参数被忽略就是占位符
□ 3. 搜 "Without this check" / "otherwise" 注释 — AI 的自言自语
□ 4. 快照测试覆盖率 — 0% 是红灯，不是你懒得写，是 AI 没生成
□ 5. 对比早期表 vs 后期表的 schema — 有没有类型漂移
□ 6. 确认认证机制只有一套 — 搜 res.locals、getUserId、req.user
□ 7. 搜 "extends Error" — 有没有用异常做控制流
□ 8. 搜 "catch" + "return null" — 有多少错误被静默吞掉
□ 9. npm view 每个依赖 ← 防幻觉包
```

---

## 写在最后

审计完这份代码，我反复想一个问题：

> **如果一个律师能用 AI 两周做出功能完整的法律平台，那工程师 15 年的经验到底值钱在哪？**

答案是：**知道什么会炸。**

那 10 张表的类型漂移 — SonarQube 扫不出来。OAuth 回调的无鉴权端点 — Semgrep 不关心路由中间件。那个永远返回 50mb 的占位函数 — 没有任何工具会觉得 「参数被忽略」 是个 bug。

AI 能把代码写出来。但它不知道这段代码在凌晨三点、流量峰值、数据库千万条数据的时候会怎么炸。

**知道「能跑」和「能上线」之间的差距 — 这是你被 AI 磨平所有技术壁垒之后，最后剩下的、也是最坚固的护城河。**

---

*本文基于 Mike OSS ([github.com/Open-Legal-Products/mike](https://github.com/Open-Legal-Products/mike)) 的实际代码审查。所有发现均有文件路径和行号可查。*
*作者：15 年软件工程从业者 | AI 代码审计 | 欢迎交流*
