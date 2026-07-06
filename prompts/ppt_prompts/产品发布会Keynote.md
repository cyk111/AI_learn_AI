# 产品发布会 Keynote Prompt

**用途**：产品发布会、Keynote 风格演示
**适用模型**：Claude Opus 4.8
**需要 Skill**：官方 pptx Skill
**风格参考**：Apple Keynote

---

## Prompt

```text
You are the presentation designer behind Apple's most iconic keynotes.
Your slides have been seen by billions. You understand that the best
slides are the ones the audience barely notices — because they're too
captivated by the story.

Create a {N}-slide product launch keynote for {PRODUCT_NAME}.

【Product】{产品一句话描述}
【Launch Date】{发布日期}
【Key Features】{3 个核心功能，每个用 3 个词描述}
【Tagline】{产品 Slogan}
【Price】{价格}

---

## Narrative Structure: The Momentum Arc

Tease → Reveal → Demo → Deep Dive → One More Thing → Availability

## Slide Structure

1. **Opening**
   - Event name + date
   - Dark background, minimal text
   - Apple-style event opener animation

2. **Vision**
   - Why this product exists
   - 1 sentence, massive type (72px+)
   - "We believe that..."

3. **The Problem**
   - The current experience
   - 1 powerful image + 1 stat
   - Make the audience FEEL the pain

4. **Feature 1: {Feature Name}**
   - Hero product shot (full-bleed)
   - 3-word headline (massive, centered)
   - 1 supporting sentence

5. **Feature 2: {Feature Name}**
   - Same format as Feature 1
   - Different angle / use case shown

6. **Feature 3: {Feature Name}**
   - Same format — the "tentpole" feature
   - Save the most impressive for last

7. **Live Demo Moment**
   - Screenshots simulating live demo
   - Annotations showing key interactions
   - "Here's what it looks like in real life"

8. **The Technology**
   - What makes it possible
   - 1 clean architecture diagram
   - "Powered by {chip / model / innovation}"

9. **Privacy & Security**
   - Our commitment (1 clear, bold statement)
   - "Privacy is a fundamental human right"

10. **One More Thing...**
    - Surprise announcement or bonus feature
    - Dramatic reveal — dark slide → single element appears

11. **Pricing & Availability**
    - Date + price + pre-order info
    - Clean price table, no clutter

12. **Closing**
    - Product name + tagline
    - Massive type, centered
    - Fade to black

---

## Design System

- **Background**: Pure black #000000
- **Text**: Pure white #FFFFFF, SF Pro Display
- **Accent**: Product hero color (use sparingly)
- **Product Images**: Full-bleed, enormous scale
- **Text on Screen**: Absolutely minimal — 1-5 words per slide is NORMAL
- **Transitions**: Fade only, 0.5s, cross-dissolve between sections
- **Typography Scale**:
  - Hero: 96px+ Bold
  - Section Title: 64px Bold
  - Body: 28px Regular (rarely used)
  - Caption: 18px Regular

## Keynote Rules
- ❌ No bullet points on stage — that's what the speaker is for
- ❌ No logos on every slide — it's distracting
- ❌ No slide numbers — nobody cares
- ✅ Every slide should evoke ONE emotion
- ✅ The speaker is the star, not the slides

【Output】Directly generate a .pptx file
```
