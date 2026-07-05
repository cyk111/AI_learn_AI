"""
Categorizer - intelligently classify prompts into categories.
Uses keyword matching and heuristics to assign categories.
"""

import re
import json
from pathlib import Path
from collections import Counter

from .config import CATEGORIES, CATEGORY_KEYWORDS, OUTPUT_DIR


def classify_prompt(prompt_data: dict) -> list[str]:
    """
    Classify a single prompt into one or more categories.
    Returns a list of category names.
    """
    act = prompt_data.get("act", "").lower()
    prompt = prompt_data.get("prompt", "").lower()
    hint = prompt_data.get("category_hint", "general").lower()
    combined = f"{act} {prompt}"

    scores = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0
        for kw in keywords:
            kw_lower = kw.lower()
            if kw_lower in act:
                score += 3  # Stronger signal if keyword is in the title
            if kw_lower in prompt:
                score += 1
            # Whole word matching
            if re.search(rf"\b{re.escape(kw_lower)}\b", combined):
                score += 1
        if score > 0:
            scores[category] = score

    # Sort by score descending
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Get top categories (score >= 2)
    top_categories = [cat for cat, score in ranked if score >= 2]

    # If no strong match, use category hint
    if not top_categories:
        if hint in CATEGORIES:
            top_categories = [hint]
        else:
            top_categories = ["general"]

    # Limit to top 2 categories max
    return top_categories[:2]


def categorize_all(prompts: list[dict]) -> dict[str, list[dict]]:
    """
    Categorize all prompts and group them by category.
    Returns {category: [prompts]} dict.
    """
    categorized: dict[str, list[dict]] = {cat: [] for cat in CATEGORIES}

    stats = Counter()

    for p in prompts:
        cats = classify_prompt(p)
        p["categories"] = cats
        for cat in cats:
            if cat in categorized:
                categorized[cat].append(p)
                stats[cat] += 1

    # Print stats
    print("\n📊 Categorization Results:")
    print("-" * 50)
    for cat in sorted(CATEGORIES):
        count = stats.get(cat, 0)
        bar = "█" * min(count // 5, 30)
        print(f"  {cat:<20} {count:>4}  {bar}")

    return categorized


def sanitize_filename(name: str) -> str:
    """Sanitize a prompt title for use as a filename."""
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name)
    return name[:80].strip("_")


def save_categorized(categorized: dict[str, list[dict]], project_root: str):
    """
    Save categorized prompts to the output directory.
    Structure:
        prompts/
        ├── programming/
        │   ├── act_as_python_interpreter.md
        │   ├── act_as_sql_expert.md
        │   └── ...
        ├── writing/
        │   ├── ...
        ├── _all_prompts.json
        ├── _index.md
        └── _stats.json
    """
    output_path = Path(project_root) / OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    all_prompts = []
    category_stats = {}

    for category, prompts in categorized.items():
        if not prompts:
            continue

        cat_dir = output_path / category
        cat_dir.mkdir(exist_ok=True)

        for i, p in enumerate(prompts):
            # Generate filename from act title
            act = p.get("act", f"prompt_{i}")
            filename = sanitize_filename(act)
            if not filename:
                filename = f"prompt_{i:04d}"

            # Ensure unique filename
            base_filename = filename
            counter = 1
            while (cat_dir / f"{filename}.md").exists():
                filename = f"{base_filename}_{counter}"
                counter += 1

            # Write prompt as markdown
            md_content = format_prompt_markdown(p, category)
            (cat_dir / f"{filename}.md").write_text(md_content, encoding="utf-8")

            all_prompts.append({
                "id": f"{category}/{filename}",
                "act": p.get("act", ""),
                "prompt": p.get("prompt", ""),
                "categories": p.get("categories", []),
                "source": p.get("source", "unknown"),
                "repo_stars": p.get("repo_stars", 0),
            })

        category_stats[category] = len(prompts)
        print(f"  ✅ {category}/ ({len(prompts)} prompts)")

    # Save _all_prompts.json
    all_json_path = output_path / "_all_prompts.json"
    all_json_path.write_text(
        json.dumps(all_prompts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n📦 All prompts JSON: {all_json_path}")

    # Save _stats.json
    stats = {
        "total_prompts": len(all_prompts),
        "categories": category_stats,
        "generated_at": None,  # Will be set by caller
    }
    (output_path / "_stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Save _index.md
    generate_index(categorized, output_path)

    return all_prompts


def format_prompt_markdown(prompt_data: dict, category: str) -> str:
    """Format a single prompt as a beautiful markdown file."""
    act = prompt_data.get("act", "Unknown")
    prompt = prompt_data.get("prompt", "")
    source = prompt_data.get("source", "unknown")
    stars = prompt_data.get("repo_stars", 0)
    cats = prompt_data.get("categories", [category])

    lines = [
        f"# {act}",
        "",
        f"**Category:** {', '.join(cats)}",
        f"**Source:** {source}",
    ]
    if stars:
        lines.append(f"**Repo Stars:** ⭐ {stars:,}")
    lines.extend([
        "",
        "---",
        "",
        "## Prompt",
        "",
        prompt,
        "",
        "---",
        "",
        f"*Collected by Prompt Skills Scraper · Quality verified via GitHub stars ⭐{stars:,}*",
    ])

    return "\n".join(lines)


def generate_index(categorized: dict[str, list[dict]], output_path: Path):
    """Generate a master index markdown file."""
    lines = [
        "# Prompt Skills Index",
        "",
        "> 🎯 High-quality prompt skills collected from verified sources (GitHub repos with 500+ stars)",
        "",
        "## Categories",
        "",
    ]

    for category in sorted(CATEGORIES):
        prompts = categorized.get(category, [])
        if not prompts:
            continue
        lines.append(f"### {category.title()}  ({len(prompts)} prompts)")
        lines.append("")
        for p in prompts[:30]:  # Show first 30 per category
            act = p.get("act", "Unknown")
            filename = sanitize_filename(act)
            source = p.get("source", "")
            stars = p.get("repo_stars", 0)
            star_str = f"⭐{stars:,}" if stars else ""
            lines.append(f"- [{act}]({category}/{filename}.md) {star_str}")
        if len(prompts) > 30:
            lines.append(f"- ... and {len(prompts) - 30} more")
        lines.append("")

    lines.extend([
        "---",
        "",
        f"**Total:** {sum(len(v) for v in categorized.values())} prompts across {sum(1 for v in categorized.values() if v)} categories",
        "",
        "## Sources",
        "",
        "All prompts are scraped from real, verified GitHub repositories with high star counts:",
        "",
        "| Repository | Stars | Description |",
        "|-----------|-------|-------------|",
        "| [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 100k+ | Most famous prompt collection |",
        "| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 45k+ | Comprehensive PE guide |",
        "| [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) | 50k+ | Chinese prompts |",
        "| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 25k+ | GPTs leaked prompts |",
        "| [LouisShark/chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) | 8k+ | System prompts |",
        "",
    ])

    (output_path / "_index.md").write_text("\n".join(lines), encoding="utf-8")
