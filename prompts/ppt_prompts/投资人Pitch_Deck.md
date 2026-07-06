# 投资人 Pitch Deck Prompt

**用途**：面向投资人的融资演示文稿
**适用模型**：Claude Opus 4.8 / Sonnet 4.5
**需要 Skill**：官方 pptx Skill

---

## Prompt

```text
You are a former Sequoia Capital partner who has reviewed 10,000+ pitch decks
and invested in 50+ unicorns. You know exactly what makes investors lean in
versus tune out.

Create a 12-slide investor pitch deck for {STARTUP_NAME}.

【Company】{一句话描述你的公司做什么}
【Stage】{种子轮 / A轮 / B轮}
【Raised to date】{已融资金额}
【Ask】{本轮融资金额}
【Use of Funds】{资金用途，如：40% 工程 + 30% GTM + 20% 运营 + 10% 储备}

---

## Slide Structure

1. **Title Slide**
   - Company name + one-line value proposition
   - Your name + title
   - Contact info (email)

2. **Problem**
   - The acute pain point (1 shocking stat + 1 user story)
   - "Current solutions suck because..."

3. **Solution**
   - What you built (1 product screenshot)
   - 3 bullet benefits (outcome-focused, not feature-focused)

4. **Why Now**
   - Market timing (1 timeline visual)
   - Technological / regulatory / behavioral shifts enabling this

5. **Market Size**
   - TAM / SAM / SOM (1 nested circle diagram)
   - Bottom-up calculation, not top-down fantasy

6. **Product**
   - 3 key features (screenshots + captions)
   - What makes it 10x better (not 10% better)

7. **Traction**
   - Growth metrics (1 compelling line chart)
   - 3-4 key KPIs with month-over-month growth rates

8. **Business Model**
   - Revenue model (1 simple flow diagram)
   - Unit economics: CAC, LTV, payback period

9. **Competitive Landscape**
   - 2×2 positioning matrix or feature comparison table
   - Our unfair advantage (moat)

10. **Team**
    - 3-5 key people (photos + 1-line bio each)
    - Why this team? (relevant experience, founder-market fit)

11. **Financial Projections**
    - 3-year projection (1 bar chart: revenue + burn)
    - Key assumptions clearly stated

12. **The Ask**
    - Amount raising + use of funds (1 simple pie/bar)
    - Milestones this round unlocks
    - Contact info

---

## Design System

- **Style**: Clean, confident, no clutter. Let the numbers speak.
- **Colors**: Navy #1A1A2E (primary) + Gold #C9A96E (accent) + White #FFFFFF (background)
- **Typography**: Inter or SF Pro Display, Bold for headlines, Regular for body
- **Charts**: Flat 2D, no 3D effects, minimal gridlines
- **Images**: High-quality Unsplash or product screenshots
- **Spacing**: Generous whitespace, 32px minimum between elements

## Anti-Patterns
- ❌ No "Thank You" slide — end with The Ask
- ❌ No TAM of "$500 billion" without bottom-up justification
- ❌ No team slides with 10+ people — show only key 3-5
- ❌ No clip art or cheesy stock photos
- ❌ No walls of text — if it looks like a document, it's wrong

【Output】Directly generate a .pptx file
```
