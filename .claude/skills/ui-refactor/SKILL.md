---
name: ui-refactor
description: Tactical UI design rules from "Refactoring UI" — fix hierarchy, layout, typography, color, and depth. Use when the user asks to "make this look better", needs CSS/styling decisions, wants design system foundations, or fixes a cluttered/broken interface. Start from features, not shell.
---

# UI Refactoring & Design System

Tactical, logical rules for professional UI design. No "artistic talent" required.

## Core Workflow

1. **Feature First** — Never start with nav bars/sidebars. Start with the specific functionality (search form, contact card, data table)
2. **Low Fidelity** — Design in grayscale first. Ignore color, shadows, fonts. Solve layout and spacing
3. **Define Systems** — No arbitrary values. Restrictive scales for spacing, type, and color
4. **Refine** — Apply tactics for hierarchy, depth, and polish

## Hierarchy Rules

### Make Elements Stand Out
- **Size**: not just bigger font — bigger padding, wider margins, more space around it
- **Weight**: bold key text, regular secondary text, lighter/colored tertiary
- **Contrast**: high-contrast for primary actions, lower contrast for secondary
- **Color**: one accent color for the most important action. Everything else grayscale
- **Whitespace**: the more space around something, the more important it feels

### The Squint Test
Squint at your UI. If every element has similar visual weight, there's no hierarchy. The CTA should dominate.

### De-emphasize, Don't Remove
Secondary info doesn't need to go away — it just needs to be lighter, smaller, or lower contrast than primary content.

## Layout & Spacing

### Use a Spacing Scale (not arbitrary px values)
```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;
}
```
- Elements that are related should be closer together
- Section gaps should be 2-3× larger than element gaps within sections
- White space is not wasted space — it's the most powerful design tool

### Grid System
- 12-column grid with consistent gutter
- Align everything to a 4px or 8px baseline grid
- Never center-align text longer than 2-3 lines — use left alignment
- Line length: 45-75 characters for body text (use `max-width: 65ch`)

## Typography Rules

### Type Scale
```css
:root {
  --text-xs: 0.75rem;    /* 12px - labels, captions */
  --text-sm: 0.875rem;   /* 14px - secondary body */
  --text-base: 1rem;     /* 16px - body */
  --text-lg: 1.125rem;   /* 18px - emphasized body */
  --text-xl: 1.25rem;    /* 20px - small headings */
  --text-2xl: 1.5rem;    /* 24px - card titles */
  --text-3xl: 1.875rem;  /* 30px - section headings */
  --text-4xl: 2.25rem;   /* 36px - page titles */
  --text-5xl: 3rem;      /* 48px - hero titles */
}
```

### Key Rules
- **Never use more than 2 font families**
- Headings: `line-height: 1.2`, Body: `line-height: 1.5-1.6`
- Letter-spacing: `-0.02em` for large headings, `0` for body, `0.05em` for uppercase labels
- **Avoid pure black text** on white — use `#1a1a2e` or `#2d3748`. Pure black (`#000`) strains eyes
- Font weight jumps: 400→600 or 400→700. Don't use 500 as your only bold

## Color Rules

### The 60-30-10 Rule
- 60% dominant color (background)
- 30% secondary color (cards, sidebars)  
- 10% accent color (CTAs, links, highlights)

### HSL Over Hex
Always use HSL for themeable colors:
```css
:root {
  --color-primary: 250 85% 60%;        /* vibrant blue-purple */
  --color-primary-light: 250 85% 95%;  /* tint */
  --color-gray-50: 210 20% 98%;
  --color-gray-900: 220 20% 10%;
}
```
Then use: `background: hsl(var(--color-primary) / 0.1);`

### Gray Wisdom
- Pure gray (`#808080` or `hsl(0,0%,50%)`) looks dead. Tint your grays with your brand hue
- Saturated grays (slightly blue or purple) look more intentional
- Cool grays for dark backgrounds, warm grays for light backgrounds

### Accessible Contrast
- Body text: ≥ 4.5:1 against background
- Large text (≥18px bold): ≥ 3:1
- NEVER use light gray text on white — it fails contrast and looks broken

## Depth & Polish

### Shadows Tell a Story
```css
/* Subtle card — "slightly above the page" */
--shadow-sm: 0 1px 2px rgba(0,0,0,0.06);

/* Standard card — "clearly elevated" */
--shadow-md: 0 4px 6px rgba(0,0,0,0.07);

/* Dropdown/modal — "floating above everything" */
--shadow-lg: 0 10px 25px rgba(0,0,0,0.1);

/* Modal backdrop — "separated from the page" */
--shadow-xl: 0 20px 50px rgba(0,0,0,0.15);
```

### Shadow on Colored Backgrounds
Don't use black shadows on colored backgrounds. Use a darker shade of the background's hue:
```css
/* Blue card on blue background */
box-shadow: 0 8px 16px hsl(220 80% 30% / 0.25);
```

### Images & Polish
- Add a subtle inner shadow or border to images for depth
- Use `border-radius` consistently (0, 4px, 8px, 12px, 16px, 9999px)
- Icons should all be from one set, one weight, one size
- Empty states: an icon + heading + 1-line description + one CTA

## Quick Heuristics

- **If you can't decide between two options**, you have too many choices. Constrain to a scale
- **Personality**: Serious/Elegant = serif + sharp corners + gold/blue. Playful = rounded sans + large radius + pink/orange
- **Design the happy path first**, iterate for edge cases
- **Never use more than 3 colors** on a single screen (excluding grays)
- **Remove borders**. Use shadows, background color differences, or spacing instead
- **Labels > placeholder text**. Placeholder disappears on focus, label stays

## Anti-Patterns
- ❌ Double borders (border on parent + border on child)
- ❌ Pure black text on pure white background
- ❌ Using opacity to make a color lighter (use HSL + increase lightness)
- ❌ Centered paragraphs longer than 2 lines
- ❌ Icons that are different sizes/weights/styles mixed together
- ❌ Box shadows that use pure black at full opacity
