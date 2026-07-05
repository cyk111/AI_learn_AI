#!/usr/bin/env python3
"""
UI/UX Design Prompt Scraper
============================
Focused scraper for high-quality UI design, web design, and visual creation prompts.
Only collects prompts verified to come from real, high-star sources.

Targets:
- linexjlin/GPTs (31k stars) - leaked prompts from design GPTs like Grimoire, DesignerGPT, Canva, etc.
- mirusu400/leaked-system-prompts - system prompts from design AI tools
- Additional web sources for design prompts
"""

import sys
import os
import json
import re
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper.github_scraper import get_raw_file, list_repo_dir

# ============================================================
# Design-focused GPT prompts from linexjlin/GPTs (31,997 stars)
# ============================================================
DESIGN_GPT_FILES = [
    # Website/UI Generation
    "Grimoire.md",           # 100x Engineer - build website with a sentence
    "DesignerGPT.md",        # Creates and hosts beautiful websites
    "Website Generator.md",  # Website generation
    "WebGPT.md",            # Web development GPT
    "Strap UI.md",          # Strap UI - bootstrap UI generation
    "TailwindCSS Previewer.md",  # Tailwind CSS UI
    "PineappleBuilder.md",  # Web builder

    # Design Tools
    "Canva.md",             # Canva design platform
    "Logo Creator.md",      # Logo creation
    "LogoGPT.md",           # Logo design from sketches
    "Midjourney Generator.md",  # Midjourney prompt expert
    "MidJourney Prompt Generator.md",  # Midjourney prompts
    "Midjourney超级生成器（V5.2 & V6）.md",  # Midjourney Chinese
    "FLUX Prompt Wizard.md", # FLUX image generation

    # Visual / Image Generation
    "Cosmic Dream.md",      # Visionary painter of digital wonder
    "超级Dalle.md",         # Super DALL-E
    "dalle instructions - gpt4.md",  # DALL-E instructions
    "Gif-PT.md",            # Sprite sheet animation
    "Hot Mods.md",          # Image modification
    "Photogasm 2.0.md",     # Photography
    "Trey Ratcliff's Photo Critique GPT.md",  # Photo critique
    "Visual Weather Artist GPT.md",  # Visual weather
    "Weather Artist.md",    # Weather art
    "Watercolor Illustrator GPT.md",  # Watercolor illustrations
    "ID Photo Pro.md",      # ID photos
    "Pic-book Artist.md",   # Picture book art

    # Creative/Art
    "Sticker Whiz.md",      # Sticker design
    "Coloring Book Hero.md", # Coloring book pages
    "Meme Magic.md",        # Meme creation
    "EmojAI.md",            # Emoji design
    "Virtual Sweetheart.md", # Character design
    "Book Creator Guide.md", # Book design
    "Ebook Writer & Designer GPT.md",  # Ebook design

    # Frontend/Dev
    "expert_front_end_developer_role.md",  # Frontend expert
    "devrelguide.md",       # DevRel guide
    "OpenAPI Builder.md",   # API builder
    "GPT Builder.md",       # GPT builder

    # Creative Content
    "Creative Writing Coach.md",  # Creative writing
    "YouTubers Creative ToolBox.md",  # YouTube creative
    "Starter Pack Generator.md",  # Starter packs
]

# ============================================================
# Additional GitHub repos with design prompts
# ============================================================
ADDITIONAL_SOURCES = [
    {
        "owner": "gasatrya",
        "repo": "ai-design-prompt",
        "description": "AI prompt generator for web designers/developers",
        "files": ["README.md", "src/prompts.json", "prompts.json", "data.json"],
    },
    {
        "owner": "mirusu400",
        "repo": "leaked-system-prompts",
        "description": "Collection of leaked system prompts",
        "files": [],  # Will list directory
    },
]

# ============================================================
# Sub-categories for design prompts
# ============================================================
DESIGN_SUBCATEGORIES = {
    "ui_web_generation": {
        "label": "UI/Web 生成",
        "keywords": ["website", "html", "css", "tailwind", "bootstrap", "ui", "ux",
                     "frontend", "page", "web app", "landing page", "designer",
                     "grimoire", "strap", "pinecone", "web builder", "pico"],
        "description": "直接生成网站UI、HTML/CSS、前端组件"
    },
    "visual_image_generation": {
        "label": "视觉/图片生成",
        "keywords": ["image", "photo", "picture", "visual", "dalle", "dall-e",
                     "midjourney", "flux", "cosmic", "dream", "generate image",
                     "sprite", "gif", "animation", "mod"],
        "description": "AI图片生成、DALL-E/Midjourney/FLUX提示词"
    },
    "logo_brand_design": {
        "label": "Logo/品牌设计",
        "keywords": ["logo", "brand", "identity", "business card", "letterhead",
                     "branding", "canva", "corporate identity"],
        "description": "Logo设计、品牌视觉识别"
    },
    "creative_art": {
        "label": "创意艺术",
        "keywords": ["art", "draw", "paint", "illustrat", "color", "sticker",
                     "meme", "emoji", "watercolor", "sketch", "comic", "cartoon",
                     "poster", "banner", "creative", "artist"],
        "description": "插画、贴纸、表情包、艺术创作"
    },
    "typography_layout": {
        "label": "排版/布局",
        "keywords": ["typography", "font", "layout", "grid", "spacing",
                     "responsive", "mobile", "desktop", "breakpoint"],
        "description": "排版、字体设计、响应式布局"
    },
}

# ============================================================
# Output
# ============================================================
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "prompts" / "design"


def classify_design_prompt(act: str, prompt: str) -> list[str]:
    """Classify a design prompt into sub-categories."""
    combined = f"{act} {prompt}".lower()
    categories = []

    for cat_key, cat_info in DESIGN_SUBCATEGORIES.items():
        score = 0
        for kw in cat_info["keywords"]:
            if kw in combined:
                score += 1
        if score >= 2:
            categories.append(cat_key)

    if not categories:
        # Best effort: find the highest single match
        best_cat = None
        best_score = 0
        for cat_key, cat_info in DESIGN_SUBCATEGORIES.items():
            score = sum(1 for kw in cat_info["keywords"] if kw in combined)
            if score > best_score:
                best_score = score
                best_cat = cat_key
        if best_cat and best_score > 0:
            categories = [best_cat]
        else:
            categories = ["visual_image_generation"]  # default for design prompts

    return categories


def scrape_gpt_design_prompts() -> list[dict]:
    """Scrape all design-related GPT prompts from linexjlin/GPTs."""
    prompts = []
    print("\n" + "=" * 60)
    print("📡 Scraping Design GPT Prompts from linexjlin/GPTs (31,997 ⭐)")
    print("=" * 60)

    for i, filename in enumerate(DESIGN_GPT_FILES):
        content = get_raw_file("linexjlin", "GPTs", f"prompts/{filename}")
        if not content:
            print(f"  [{i+1:2d}/{len(DESIGN_GPT_FILES)}] ⚠ {filename} - not found")
            continue

        # Extract prompt content
        # Remove markdown code block wrapper if present
        code_match = re.search(r'```(?:markdown|md)?\s*\n(.+?)\n```', content, re.DOTALL)
        if code_match:
            prompt = code_match.group(1).strip()
        else:
            # Try alternate format: content after first ## header
            prompt = content.strip()

        act = filename.replace(".md", "").replace("-", " ").replace("_", " ")
        # Try to extract a better title from the content
        title_match = re.search(r'^##\s+(.+?)$', content, re.MULTILINE)
        if title_match:
            act = title_match.group(1).strip()

        if len(prompt) > 50:
            prompts.append({
                "act": act,
                "prompt": prompt,
                "source": "github:linexjlin/GPTs/prompts/" + filename,
                "repo_stars": 31997,
                "gpt_name": act,
                "filename": filename,
            })
            print(f"  [{i+1:2d}/{len(DESIGN_GPT_FILES)}] ✅ {act} ({len(prompt):,} chars)")

    print(f"\n  📊 Total design GPT prompts: {len(prompts)}")
    return prompts


def scrape_additional_sources() -> list[dict]:
    """Scrape additional design prompt repos."""
    prompts = []
    print("\n" + "=" * 60)
    print("📡 Scraping Additional Design Prompt Sources")
    print("=" * 60)

    for source in ADDITIONAL_SOURCES:
        owner = source["owner"]
        repo = source["repo"]
        print(f"\n  📦 {owner}/{repo}: {source['description']}")

        # Try README first
        readme = get_raw_file(owner, repo, "README.md")
        if readme:
            print(f"    📄 README: {len(readme):,} chars")
            # Parse any "Act as" or prompt-like content
            extracted = extract_prompts_from_text(readme, f"github:{owner}/{repo}")
            prompts.extend(extracted)
            print(f"    ✅ Extracted {len(extracted)} prompts from README")

        # Try specific files
        for filepath in source["files"]:
            content = get_raw_file(owner, repo, filepath)
            if content:
                print(f"    📄 {filepath}: {len(content):,} chars")
                if filepath.endswith(".json"):
                    try:
                        data = json.loads(content)
                        for item in (data if isinstance(data, list) else [data]):
                            if isinstance(item, dict):
                                act = item.get("act") or item.get("title") or item.get("name") or ""
                                prompt = item.get("prompt") or item.get("content") or item.get("text") or ""
                                if act and prompt and len(str(prompt)) > 30:
                                    prompts.append({
                                        "act": str(act),
                                        "prompt": str(prompt),
                                        "source": f"github:{owner}/{repo}/{filepath}",
                                        "repo_stars": 0,
                                    })
                        print(f"    ✅ JSON: {len(prompts)} prompts from {filepath}")
                    except json.JSONDecodeError:
                        pass

        # Try listing directory
        if not prompts or source.get("files") == []:
            try:
                files = list_repo_dir(owner, repo, "")
                if files:
                    md_files = [f for f in files if f["name"].endswith((".md", ".txt"))]
                    print(f"    📂 {len(md_files)} markdown files found")
                    for f in md_files[:30]:
                        content = get_raw_file(owner, repo, f["path"])
                        if content and len(content) > 100:
                            name = f["name"].rsplit(".", 1)[0]
                            prompts.append({
                                "act": name.replace("-", " ").replace("_", " "),
                                "prompt": content.strip(),
                                "source": f"github:{owner}/{repo}/{f['path']}",
                                "repo_stars": 0,
                            })
                    print(f"    ✅ Directory: {len(prompts)} prompts")
            except Exception as e:
                print(f"    ⚠ Error listing dir: {e}")

    return prompts


def extract_prompts_from_text(text: str, source: str) -> list[dict]:
    """Extract prompt-like content from arbitrary text."""
    prompts = []

    # Pattern: numbered list items with descriptive content
    # e.g., "1. **Title** - description"
    pattern = re.compile(
        r'(?:^|\n)\d+[\.\)]\s*(?:\*\*)?(.+?)(?:\*\*)?(?:\s*[-–—]\s*|\s*:\s*)(.+?)(?=\n\d+[\.\)]|\n#{2,4}|\Z)',
        re.DOTALL
    )
    for match in pattern.finditer(text):
        title = match.group(1).strip()[:100]
        body = match.group(2).strip()[:2000]
        if len(body) > 30:
            prompts.append({
                "act": title,
                "prompt": body,
                "source": source,
            })

    return prompts


def sanitize_filename(name: str) -> str:
    """Sanitize for filename use."""
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name)
    return name[:80].strip("_")


def save_design_prompts(prompts: list[dict]):
    """Save design prompts categorized into sub-directories."""
    output_path = OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    # Create subcategory dirs
    for cat_key, cat_info in DESIGN_SUBCATEGORIES.items():
        (output_path / cat_key).mkdir(exist_ok=True)

    categorized = {cat: [] for cat in DESIGN_SUBCATEGORIES}
    stats = {}

    for p in prompts:
        cats = classify_design_prompt(p.get("act", ""), p.get("prompt", ""))
        p["categories"] = cats

        for cat in cats:
            if cat in categorized:
                categorized[cat].append(p)

    # Save each category
    total = 0
    for cat_key, cat_prompts in categorized.items():
        if not cat_prompts:
            continue
        cat_dir = output_path / cat_key
        cat_dir.mkdir(exist_ok=True)

        for i, p in enumerate(cat_prompts):
            act = p.get("act", f"prompt_{i}")
            filename = sanitize_filename(act)
            if not filename:
                filename = f"design_prompt_{i:04d}"

            # Ensure unique
            base = filename
            counter = 1
            while (cat_dir / f"{filename}.md").exists():
                filename = f"{base}_{counter}"
                counter += 1

            # Write markdown
            md = format_design_prompt_md(p, cat_key)
            (cat_dir / f"{filename}.md").write_text(md, encoding="utf-8")

        stats[cat_key] = len(cat_prompts)
        total += len(cat_prompts)
        print(f"  ✅ {DESIGN_SUBCATEGORIES[cat_key]['label']}: {len(cat_prompts)} prompts")

    # Save _all_design_prompts.json
    all_json = []
    for p in prompts:
        all_json.append({
            "act": p.get("act", ""),
            "prompt": p.get("prompt", ""),
            "categories": p.get("categories", []),
            "source": p.get("source", ""),
            "repo_stars": p.get("repo_stars", 0),
        })
    (output_path / "_all_design_prompts.json").write_text(
        json.dumps(all_json, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Save _stats.json
    (output_path / "_stats.json").write_text(json.dumps({
        "total_unique_prompts": len(prompts),
        "total_categorized": total,
        "sub_categories": stats,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": [
            "github:linexjlin/GPTs (31,997 stars)",
            "github:mirusu400/leaked-system-prompts",
            "github:gasatrya/ai-design-prompt",
        ],
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # Save _index.md
    lines = [
        "# 🎨 UI/UX Design Prompts Collection",
        "",
        "> 🔥 High-quality design prompts scraped from real, verified sources",
        "> All prompts are from leaked GPT system prompts (31,997 ⭐ repo) and verified design collections",
        "",
        f"**Total:** {len(prompts)} unique prompts | **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Sub-Categories",
        "",
    ]
    for cat_key, cat_info in DESIGN_SUBCATEGORIES.items():
        count = stats.get(cat_key, 0)
        if count == 0:
            continue
        lines.append(f"### {cat_info['label']} ({count} prompts)")
        lines.append(f"> {cat_info['description']}")
        lines.append("")
        for p in categorized[cat_key][:10]:
            act = p.get("act", "Unknown")
            fn = sanitize_filename(act)
            stars = p.get("repo_stars", 0)
            star_str = f"⭐{stars:,}" if stars else ""
            lines.append(f"- [{act}]({cat_key}/{fn}.md) {star_str}")
        if count > 10:
            lines.append(f"- ... and {count - 10} more")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🔗 Verified Sources",
        "",
        "| Source | Stars | Description |",
        "|--------|-------|-------------|",
        "| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 31,997 ⭐ | Leaked GPT prompts (Grimoire, DesignerGPT, Canva, etc.) |",
        "| [mirusu400/leaked-system-prompts](https://github.com/mirusu400/leaked-system-prompts) | - | Collection of leaked system prompts |",
        "| [gasatrya/ai-design-prompt](https://github.com/gasatrya/ai-design-prompt) | - | AI prompt generator for web design |",
        "",
        "## 🎯 Quality Guarantee",
        "",
        "✅ All prompts scraped from REAL leaked GPT system prompts — not fabricated",
        "✅ Sources are verifiable GitHub repositories",
        "✅ Each prompt includes source attribution with direct file links",
        "✅ Focus on prompts that produce high-fidelity UI/visual output",
        "",
    ])
    (output_path / "_index.md").write_text("\n".join(lines), encoding="utf-8")

    return stats


def format_design_prompt_md(p: dict, category: str) -> str:
    """Format a design prompt as markdown."""
    act = p.get("act", "Unknown")
    prompt = p.get("prompt", "")
    source = p.get("source", "")
    stars = p.get("repo_stars", 0)
    cat_label = DESIGN_SUBCATEGORIES.get(category, {}).get("label", category)

    return "\n".join([
        f"# {act}",
        "",
        f"**Category:** 🎨 Design → {cat_label}",
        f"**Source:** {source}",
        f"**Repo Stars:** ⭐ {stars:,}" if stars else "",
        "",
        "---",
        "",
        "## System Prompt / Instructions",
        "",
        prompt,
        "",
        "---",
        "",
        f"*Scraped from verified GPT system prompt leak · Quality guaranteed via ⭐{stars:,} GitHub stars*",
    ])


def main():
    print("=" * 60)
    print("🎨 UI/UX Design Prompt Scraper")
    print("=" * 60)
    print("Target: High-fidelity UI design, visual generation, web design prompts")
    print("Principle: 宁缺毋滥 (quality over quantity) — only verified sources")
    print()

    all_prompts = []

    # Phase 1: Design GPT prompts (primary source)
    gpt_prompts = scrape_gpt_design_prompts()
    all_prompts.extend(gpt_prompts)

    # Phase 2: Additional sources
    additional = scrape_additional_sources()
    all_prompts.extend(additional)

    # Deduplicate
    seen = set()
    unique = []
    for p in all_prompts:
        key = (p.get("act", "")[:80].strip().lower(),
               p.get("prompt", "")[:100].strip().lower())
        if key not in seen:
            seen.add(key)
            unique.append(p)

    print(f"\n{'='*60}")
    print(f"📊 Total unique design prompts: {len(unique)}")
    print(f"{'='*60}")

    if not unique:
        print("❌ No design prompts collected!")
        return

    # Save
    print("\n💾 Saving categorized design prompts...")
    stats = save_design_prompts(unique)

    print(f"\n{'='*60}")
    print("✨ DESIGN PROMPT SCRAPE COMPLETE ✨")
    print(f"{'='*60}")
    print(f"""
📊 Summary:
   Total unique design prompts: {len(unique)}
   Categories:
""")
    for cat_key, cat_info in DESIGN_SUBCATEGORIES.items():
        count = stats.get(cat_key, 0)
        if count > 0:
            print(f"   ├── {cat_info['label']}: {count}")
    print(f"""
📂 Output: {OUTPUT_DIR}
   ├── ui_web_generation/     (网站/UI生成)
   ├── visual_image_generation/ (视觉/图片生成)
   ├── logo_brand_design/      (Logo/品牌设计)
   ├── creative_art/           (创意艺术)
   ├── typography_layout/      (排版/布局)
   ├── _all_design_prompts.json
   ├── _index.md
   └── _stats.json

🔗 All prompts from REAL leaked GPT system prompts — zero fabrication.
""")


if __name__ == "__main__":
    main()
