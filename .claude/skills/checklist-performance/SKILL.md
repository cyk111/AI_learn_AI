---
name: checklist-performance
description: Web performance optimization checklist covering Core Web Vitals, frontend, backend, and measurement. Use when auditing or improving page speed, LCP, INP, CLS, or general web performance.
---

# Web Performance Checklist

Quick reference checklist for web application performance.

> Source: [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills) (42K+ stars)

## Core Web Vitals Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| INP (Interaction to Next Paint) | ≤ 200ms | ≤ 500ms | > 500ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | ≤ 0.25 | > 0.25 |

## TTFB Diagnosis

When TTFB is slow (> 800ms):
- DNS resolution slow → `<link rel="dns-prefetch">` or `<link rel="preconnect">`
- TCP/TLS handshake slow → HTTP/2, edge deployment, verify keep-alive
- Server processing slow → profile backend, check slow queries, add caching

## Frontend Checklist

### Images
- [ ] Modern formats (WebP, AVIF)
- [ ] Responsive sizing (`srcset` and `sizes`)
- [ ] Explicit `width` and `height` on images (prevents CLS)
- [ ] Below-fold images: `loading="lazy"` + `decoding="async"`
- [ ] Hero/LCP images: `fetchpriority="high"`, no lazy loading

### JavaScript
- [ ] Bundle < 200KB gzipped (initial load)
- [ ] Code splitting with dynamic `import()` for routes
- [ ] Tree shaking enabled
- [ ] No blocking JS in `<head>` (use `defer` or `async`)
- [ ] Long tasks (> 50ms) broken up — main lever for INP
- [ ] `scheduler.yield()` or `yieldToMain` for long loops
- [ ] Third-party scripts: `async`/`defer`, facade for heavy embeds

### CSS
- [ ] Critical CSS inlined or preloaded
- [ ] No CSS-in-JS runtime cost in production

### Fonts
- [ ] 2–3 families max, WOFF2 only, self-hosted when possible
- [ ] `font-display: swap` to avoid FOIT
- [ ] Subsetted via `unicode-range`
- [ ] Fallback font metrics adjusted (`size-adjust`, `ascent-override`)

### Network
- [ ] Static assets: long `max-age` + content hashing
- [ ] HTTP/2 or HTTP/3 enabled
- [ ] `<link rel="preconnect">` for known origins
- [ ] No unnecessary redirects

### Rendering
- [ ] No layout thrashing (forced synchronous layouts)
- [ ] Animations use `transform` and `opacity` only (GPU-accelerated)
- [ ] Long lists use virtualization
- [ ] `content-visibility: auto` for off-screen sections

## Backend Checklist

### Database
- [ ] No N+1 queries (use eager loading/joins)
- [ ] Appropriate indexes on filtered/sorted columns
- [ ] List endpoints paginated
- [ ] Connection pooling configured

### API
- [ ] Response times < 200ms (p95)
- [ ] No sync heavy computation in request handlers
- [ ] Response compression (gzip/brotli)
- [ ] Appropriate caching (in-memory, Redis, CDN)

## Common Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| N+1 queries | Joins, includes, batch loading |
| Unbounded queries | Always paginate, add LIMIT |
| Missing indexes | Add for filtered/sorted columns |
| Layout thrashing | Batch DOM reads, then batch writes |
| Unoptimized images | WebP, responsive sizes, lazy load |
| Large bundles | Code split, tree shake, audit deps |
| Blocking main thread | `scheduler.yield()`, Web Workers |
| Memory leaks | Clean up listeners, intervals, refs |
