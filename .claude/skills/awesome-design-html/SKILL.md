---
name: awesome-design-html
description: Brand-faithful design reference library with 118 design systems (Stripe, Linear, Apple, Notion, Vercel, Figma, Airbnb, Spotify, Tesla, Ferrari + 22 Chinese brands: 飞书, 抖音, DeepSeek, 小米汽车, 蔚来, 哔哩哔哩 + 22 iOS mockups). Use when the user says "做个Linear风格的页面", "参考Stripe的hero", "飞书风的设计", "Spotify风格的播放器", or any brand-name + design/page/UI/screen. Read matching HTML, extract tokens, adapt to request.
---

# Awesome Design HTML — 118 Brand Design Systems

A reference library of brand-faithful design tokens and HTML templates. Every brand has a self-contained design system: `:root` CSS tokens, brand colors, typography, border-radius, shadow style, and component patterns.

## How to Use

When the user mentions a brand + design/page/UI/style:

1. **Match the brand** — Find the closest brand in the index below
2. **Extract tokens**: colors (`:root` custom properties), fonts (Google Fonts CDN), radius, shadow, hero archetype, button shape
3. **Adapt to the request** — Apply tokens to the user's specific project. Don't copy the HTML verbatim; use the design DNA
4. **Don't homogenize** — Each brand has a unique feel. Linear ≠ Stripe ≠ Apple ≠ 飞书

## Brand Index — Global (73)

### Design Benchmark (study these first)
- **stripe** — Gradient hero, blur-heavy, blue-purple, Inter, border-radius: 8px, subtle shadows
- **linear** — Dark-first, minimal, #5E6AD2 accent, Inter, sharp corners, borderline-zero chrome
- **notion** — Clean white, emoji-heavy, Inter, rounded: 4px, no shadows, generous whitespace

### SaaS / Productivity
airtable, cal, intercom, miro, slack, superhuman, webflow, zapier, figma, framer, raycast, sanity

### Dev Tools / AI
**claude** (Anthropic brand), cursor, vercel, warp, bun, opencode, lovable
**AI platforms**: cohere, elevenlabs, minimax, mistral, ollama, runwayml, together, voltagent, xai

### Infra / Dev
clickhouse, composio, hashicorp, mintlify, mongodb, posthog, replicate, resend, sentry, supabase

### Fintech / Crypto
binance, coinbase, kraken, mastercard, revolut, **stripe**, wise

### Consumer / Commerce
**airbnb**, nike, pinterest, shopify, **spotify**, starbucks, uber

### Auto / Luxury
bmw, bmw-m, bugatti, **ferrari**, lamborghini, renault, **tesla**

### Enterprise
ibm, meta, nvidia, expo, playstation, spacex, theverge, wired, vodafone

## Brand Index — Chinese (22)

### 字节系
- **feishu (飞书)** — Blue primary, clean, functional, Chinese typography
- **douyin (抖音)** — Dark mode, pink/magenta accents, short-video energy
- **doubao (豆包)** — AI assistant, friendly rounded design

### 阿里系
- **aliyun (阿里云)** — Orange accent, enterprise cloud
- **alipay (支付宝)** — Blue, financial trust, minimal
- **dingtalk (钉钉)** — Blue, enterprise communication
- **yuque (语雀)** — Green/teal, knowledge management, clean reading

### 腾讯系
- **tencent-cloud (腾讯云)** — Blue, cloud platform
- **wechat (微信)** — Green, messaging ecosystem

### 国产 AI
- **deepseek** — Dark, minimal, code-focused, teal accent
- **kimi** — Purple gradient, friendly AI
- **wenxin (文心一言)** — Blue-purple gradient, Baidu AI
- **qwen (通义千问)** — Alibaba AI, purple-blue, clean

### 新能源车
- **xiaomi-ev (小米汽车)** — Xiaomi orange, automotive, premium
- **nio (蔚来)** — Dark premium, blue accent, luxury EV
- **li-auto (理想)** — Green, family SUV focus
- **zeekr (极氪)** — Dark, neon green, performance EV

### 内容 / 消费
- **bilibili (哔哩哔哩)** — Pink/blue brand, ACG culture, playful
- **mihoyo (米哈游)** — Gaming, Genshin/Honkai aesthetic
- **xiaomi (小米)** — Orange, consumer electronics
- **xiaohongshu (小红书)** — Red, lifestyle, waterfall (瀑布流) explore feed

## Brand Index — iOS Mockups (22)

spotify-ios, apple-music-ios, youtube-ios, netflix-ios, tiktok-ios, instagram-ios, threads-ios, x-twitter-ios, snapchat-ios, whatsapp-ios, telegram-ios, discord-ios, chatgpt-ios, notion-ios, uber-ios, airbnb-ios, tinder-ios, hinge-ios, starbucks-ios, doordash-ios, robinhood-ios, duolingo-ios

## Design DNA Extraction

When you don't have the actual HTML, extract design DNA from memory:

```
BRAND: [name]
PRIMARY COLOR: [hex]
ACCENT: [hex]
BACKGROUND: [hex] (light mode) / [hex] (dark mode)
FONT FAMILY: [Google Fonts name]
FONT WEIGHTS: [list]
BORDER RADIUS: [px] — sharp | medium | rounded | pill
SHADOW STYLE: none | subtle | medium | dramatic
HERO ARCHETYPE: gradient | illustration | photo | typography | product screenshot
BUTTON STYLE: filled | outlined | ghost | gradient
LAYOUT: centered | asymmetric | grid | single-column
SIGNATURE ELEMENT: [unique detail that defines this brand]
```

## Anti-Patterns

- ❌ Mixing two brands' tokens into one design
- ❌ Using a brand's accent color without their typography system
- ❌ Generic gradient hero when the brand uses photo heros
- ❌ Centering everything when the brand uses asymmetric layouts
- ❌ Defaulting to Inter when the brand has a distinctive font

## When to Reach for Each Brand

| User says | Reference |
|-----------|-----------|
| "SaaS landing page", "payment UI" | Stripe |
| "Dark mode app", "dev tool UI" | Linear |
| "Clean knowledge base", "docs" | Notion |
| "Premium", "luxury" | Ferrari, Tesla |
| "Creative", "portfolio" | Figma, Framer |
| "AI app", "chat interface" | Claude, ChatGPT |
| "Enterprise dashboard" | IBM, Meta |
| "飞书风格" | feishu (飞书) |
| "AI产品落地页" | deepseek, kimi |
| "新能源车官网" | nio (蔚来), xiaomi-ev |
| "游戏/二次元风格" | bilibili, mihoyo |
| "短视频/社交" | douyin (抖音), xiaohongshu |

---
Full reference library: https://github.com/yzfly/awesome-design-html (118 files)
