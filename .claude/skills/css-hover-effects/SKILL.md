---
name: css-hover-effects
description: Pure CSS hover effects and micro-interactions — Float, Glow, Sweep, Shutter, Pop, Wobble, Underline, Ripple, Bubble tooltips and more. Auto-detects design style and matches effects. Zero JS, zero dependencies. Use when the UI "feels flat", needs hover states, interactive feedback, or micro-interactions on buttons/cards/nav/links/icons.
---

# CSS Hover Effects & Micro-Interactions

Zero-dependency, SSR-safe hover patterns. Auto-matches effects to existing design style.

## Step 1 — Detect Design Style

Check CSS signals and classify into ONE category:

| Style | Signals |
|-------|---------|
| **MINIMAL** | muted colors + large radius + no shadow + system font (Notion, Linear) |
| **BOLD** | vivid colors + any radius + strong shadow + display font (Stripe, creative) |
| **PLAYFUL** | vivid + large radius + playful font + colorful (Duolingo, consumer apps) |
| **CORPORATE** | muted/navy colors + small radius + tight density (B2B SaaS, dashboards) |
| **DARK-PREMIUM** | dark bg + glow accents + medium radius (Raycast, dev tools) |

## Step 2 — Effect Compatibility Matrix

| Effect | MINIMAL | BOLD | PLAYFUL | CORPORATE | DARK-PREMIUM |
|--------|---------|------|---------|-----------|--------------|
| Float (translateY) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Float Shadow | ❌ | ✅ | ✅ | ❌ | ✅ |
| Glow | ❌ | ✅ | ✅ | ❌ | ✅ ★ |
| Underline From Center | ✅ ★ | ✅ | ✅ | ✅ | ✅ |
| Sweep To Right | ❌ | ✅ | ✅ | ❌ | ❌ |
| Grow (scale) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pulse Grow | ❌ | ✅ | ✅ | ❌ | ❌ |
| Pop (spring scale) | ❌ | ✅ | ✅ ★ | ❌ | ❌ |
| Wobble | ❌ | ✅ | ✅ | ❌ | ❌ |
| Background Fade | ✅ ★ | ✅ | ✅ | ✅ ★ | ✅ |
| Shutter In | ❌ | ✅ ★ | ✅ | ❌ | ✅ |
| Border Fade | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ripple Out | ❌ | ✅ | ✅ | ❌ | ✅ |
| Shadow Radial | ❌ | ✅ | ❌ | ❌ | ✅ ★ |
| Bubble (tooltip) | ✅ | ✅ | ✅ | ✅ | ✅ |

**Rules:** MINIMAL: max 2 effects, ≤250ms. CORPORATE: only subtle effects. DARK-PREMIUM: prioritize Glow/Shadow Radial. PLAYFUL: combine 2 effects. Never Wobble/Buzz on elements >3× per page.

## Step 3 — Effect Library (Copy-Ready CSS)

### 2D Transforms

**Float** — Universal lift on hover:
```css
.hvr-float { transition: transform 0.3s ease; }
.hvr-float:hover { transform: translateY(-6px); }
/* MINIMAL: -4px, BOLD: -8px */
```

**Float Shadow** — Float + matching shadow (only when design has shadows):
```css
.hvr-float-shadow { transition: transform 0.3s ease, box-shadow 0.3s ease; }
.hvr-float-shadow:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.12);
}
```

**Grow** — Subtle scale up, safe everywhere:
```css
.hvr-grow { transition: transform 0.2s ease; }
.hvr-grow:hover { transform: scale(1.05); }
```

**Pop** — Spring scale with overshoot (PLAYFUL/BOLD only):
```css
.hvr-pop { transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); }
.hvr-pop:hover { transform: scale(1.15); }
```

**Bob** — Floating animation (always-on, not hover):
```css
.hvr-bob { animation: hvr-bob 1.5s ease infinite; }
@keyframes hvr-bob {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
```

### Background Transitions

**Background Fade** — Color wash, safest background effect:
```css
.hvr-bg-fade { transition: background-color 0.25s ease; }
.hvr-bg-fade:hover { background-color: rgba(99, 102, 241, 0.08); }
```

**Sweep To Right** — Solid color sweep (BOLD/PLAYFUL only):
```css
.hvr-sweep-right {
  position: relative; z-index: 1; overflow: hidden;
  transition: color 0.3s ease;
}
.hvr-sweep-right::before {
  content: ''; position: absolute; inset: 0;
  background: var(--accent);
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.3s ease; z-index: -1;
}
.hvr-sweep-right:hover::before { transform: scaleX(1); }
.hvr-sweep-right:hover { color: white; }
```

**Shutter In** — Split shutter from center (high-impact CTAs):
```css
.hvr-shutter-in {
  position: relative; z-index: 1; overflow: hidden;
  transition: color 0.35s ease;
}
.hvr-shutter-in::before, .hvr-shutter-in::after {
  content: ''; position: absolute; top: 0; bottom: 0; width: 50%;
  background: var(--accent); transition: transform 0.35s ease; z-index: -1;
}
.hvr-shutter-in::before { left: 0; transform: scaleX(0); transform-origin: left; }
.hvr-shutter-in::after { right: 0; transform: scaleX(0); transform-origin: right; }
.hvr-shutter-in:hover::before, .hvr-shutter-in:hover::after { transform: scaleX(1); }
.hvr-shutter-in:hover { color: white; }
```

### Border & Underline

**Underline From Center** — Navigation links (universal):
```css
.hvr-underline-center { position: relative; }
.hvr-underline-center::after {
  content: ''; position: absolute; bottom: -2px;
  left: 50%; right: 50%; height: 2px;
  background: var(--accent);
  transition: left 0.25s ease, right 0.25s ease;
}
.hvr-underline-center:hover::after { left: 0; right: 0; }
```

**Border Fade** — Appears on hover:
```css
.hvr-border-fade { border: 2px solid transparent; transition: border-color 0.25s ease; }
.hvr-border-fade:hover { border-color: var(--accent); }
```

**Ripple Out** — Border ripple for circular buttons:
```css
.hvr-ripple-out { position: relative; }
.hvr-ripple-out::before {
  content: ''; position: absolute; inset: 0;
  border: 2px solid var(--accent); border-radius: inherit;
  opacity: 0; transform: scale(1);
  transition: transform 0.4s ease, opacity 0.4s ease;
}
.hvr-ripple-out:hover::before { transform: scale(1.12); opacity: 1; }
```

### Shadow & Glow

**Glow** — Signature DARK-PREMIUM effect:
```css
.hvr-glow { transition: box-shadow 0.3s ease; }
.hvr-glow:hover { box-shadow: 0 0 18px rgba(99, 102, 241, 0.5); }
```

**Shadow Radial** — Inward radial glow (DARK-PREMIUM):
```css
.hvr-shadow-radial { transition: box-shadow 0.4s ease; }
.hvr-shadow-radial:hover { box-shadow: 0 0 0 4px rgba(99,102,241,0.35), 0 0 40px rgba(99,102,241,0.35); }
```

### Icon Effects

**Icon Forward** — Arrow slides right:
```css
.hvr-icon-forward .icon { transition: transform 0.2s ease; }
.hvr-icon-forward:hover .icon { transform: translateX(4px); }
```

**Icon Spin** — Settings/refresh icons:
```css
.hvr-icon-spin .icon { transition: transform 0.3s ease; }
.hvr-icon-spin:hover .icon { transform: rotate(90deg); }
```

### Tooltips (Bubble)

**Bubble Top** — Pure CSS tooltip:
```css
.hvr-bubble-top { position: relative; }
.hvr-bubble-top::before {
  content: attr(data-tooltip);
  position: absolute; bottom: calc(100% + 10px); left: 50%;
  transform: translateX(-50%) translateY(6px);
  background: #1a1a2e; color: white;
  padding: 6px 12px; border-radius: 6px; font-size: 12px;
  white-space: nowrap; opacity: 0; pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.hvr-bubble-top:hover::before { opacity: 1; transform: translateX(-50%) translateY(0); }
```

## Step 4 — Quick Element Reference

| Element | MINIMAL | BOLD | CORPORATE | DARK-PREMIUM |
|---------|---------|------|-----------|--------------|
| Nav link | Underline Center | Sweep Right | Background Fade | Underline + Glow |
| Primary CTA | Grow + Border | Shutter In | Background Fade | Glow |
| Card | Float | Float Shadow | Background Fade | Glow |
| Icon button | Icon Float | Icon Spin | Icon Forward | Float + Glow |
| Image | Grow | Float Shadow | Grow | Glow |

## Step 5 — Rules

### Safe Combos
- Float + Border Fade, Float Shadow + subtle Grow, Underline + color transition, Glow + Shadow Radial (dark)

### Never Combine
- Sweep + Float, Wobble + Buzz, Pulse Grow + any other animation, Curl + Background

### Duration by Style
- MINIMAL: 150-200ms ease | CORPORATE: 200-250ms ease | BOLD: 250-350ms ease | PLAYFUL: 200-350ms cubic-bezier(0.34, 1.56, 0.64, 1)

### Always Add
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
