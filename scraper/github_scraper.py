"""
GitHub API scraper - fetches real prompts from high-star GitHub repositories.
All content is fetched from verified, real repositories via the GitHub API.

Supports multiple prompt formats:
1. CSV format: act,prompt columns (awesome-chatgpt-prompts)
2. PROMPTS.md: <details><summary> format
3. Markdown "## Act as" headers
4. Individual prompt files (GPTs repo)
"""

import os
import re
import csv
import io
import time
import json
from typing import Optional

import requests

from .config import (
    GITHUB_TARGETS,
    GITHUB_API_BASE,
)


def get_headers() -> dict:
    """Get GitHub API headers with optional auth token."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "prompt-skills-scraper/1.0",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def get_repo_info(owner: str, repo: str) -> Optional[dict]:
    """Get repository metadata from GitHub API."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    resp = requests.get(url, headers=get_headers(), timeout=30)
    if resp.status_code == 404:
        print(f"  ⚠ Repo not found: {owner}/{repo}")
        return None
    if resp.status_code == 403:
        print(f"  ⚠ Rate limited. Waiting 60 seconds...")
        time.sleep(60)
        resp = requests.get(url, headers=get_headers(), timeout=30)
    if resp.status_code != 200:
        print(f"  ⚠ HTTP {resp.status_code} for {owner}/{repo}")
        return None
    return resp.json()


def get_raw_file(owner: str, repo: str, path: str, branch: str = "main") -> Optional[str]:
    """Fetch a raw file from GitHub."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    resp = requests.get(url, headers={"User-Agent": "prompt-skills-scraper/1.0"}, timeout=30)
    if resp.status_code == 200:
        return resp.text
    # Try master
    if branch == "main":
        return get_raw_file(owner, repo, path, "master")
    return None


def get_readme_content(owner: str, repo: str) -> Optional[str]:
    """Fetch the README content from a GitHub repo."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/readme"
    resp = requests.get(url, headers=get_headers(), timeout=30)
    if resp.status_code != 200:
        return get_raw_file(owner, repo, "README.md")

    import base64
    content = resp.json().get("content", "")
    if content:
        return base64.b64decode(content).decode("utf-8", errors="replace")
    return None


def list_repo_dir(owner: str, repo: str, path: str = "") -> list[dict]:
    """List contents of a directory in a repo via GitHub API."""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    resp = requests.get(url, headers=get_headers(), timeout=30)
    if resp.status_code != 200:
        return []
    return resp.json()


# ============================================================
# Format-specific parsers
# ============================================================

def parse_csv(content: str, source_name: str) -> list[dict]:
    """Parse CSV with act,prompt columns (awesome-chatgpt-prompts format)."""
    prompts = []
    # Increase field size limit for large prompts
    csv.field_size_limit(1048576)  # 1MB
    try:
        reader = csv.DictReader(io.StringIO(content))
        for row in reader:
            act = row.get("act", "").strip().strip('"').strip()
            prompt = row.get("prompt", "").strip().strip('"').strip()
            if act and prompt and len(prompt) > 15:
                prompts.append({
                    "act": act,
                    "prompt": prompt,
                    "source": f"{source_name}#csv",
                })
    except Exception as e:
        print(f"  ⚠ CSV parse error: {e}")
    return prompts


def parse_propmts_md(content: str, source_name: str) -> list[dict]:
    """
    Parse PROMPTS.md format:
    <details>
    <summary><strong>Title</strong></summary>
    ## Title
    ```md
    prompt content
    ```
    </details>
    """
    prompts = []
    # Pattern: <summary><strong>Title</strong></summary> ... ```md ... ``` </details>
    # Match details blocks
    detail_pattern = re.compile(
        r'<details[^>]*>\s*<summary><strong>(.+?)</strong></summary>\s*(.+?)</details>',
        re.DOTALL
    )
    for match in detail_pattern.finditer(content):
        act = match.group(1).strip()
        body = match.group(2)
        # Extract prompt from markdown code block
        code_match = re.search(r'```(?:md|markdown)?\s*\n(.+?)\n```', body, re.DOTALL)
        if code_match:
            prompt = code_match.group(1).strip()
        else:
            # Try to extract any meaningful text
            prompt = body.strip()
            # Remove HTML tags
            prompt = re.sub(r'<[^>]+>', '', prompt).strip()

        if act and prompt and len(prompt) > 15:
            prompts.append({
                "act": act,
                "prompt": prompt,
                "source": f"{source_name}#propmts-md",
            })
    return prompts


def parse_act_as_markdown(content: str, source_name: str) -> list[dict]:
    """Parse "## Act as X" or "## X" style markdown prompts."""
    prompts = []

    # Pattern 1: "## Act as Name" followed by blockquote or content
    pattern1 = re.compile(
        r'^#{2,4}\s+[Aa]ct\s+as\s+(.+?)$\s*\n((?:\s*(?:>|-)?.+?\n)+)',
        re.MULTILINE
    )
    for match in pattern1.finditer(content):
        act = match.group(1).strip()
        body = match.group(2).strip()
        # Clean blockquote markers
        body = re.sub(r'^>\s?', '', body, flags=re.MULTILINE)
        body = re.sub(r'^-\s?', '', body, flags=re.MULTILINE)
        body = body.strip()
        if len(body) > 20:
            prompts.append({
                "act": act,
                "prompt": body,
                "source": f"{source_name}#act-as",
            })

    # Pattern 2: "I want you to act as X" blocks
    pattern2 = re.compile(
        r'(?:^|\n)([> ]*[Ii]\s+(?:want|need|would like)\s+(?:you\s+)?to\s+act\s+as\s+(.+?))(?:\.|$)(.+?)(?=\n#{2,4}\s|\n[> ]*[Ii]\s+(?:want|need|would like)|\Z)',
        re.DOTALL
    )
    for match in pattern2.finditer(content):
        act = match.group(2).strip().rstrip(".")
        full_text = match.group(0).strip()
        full_text = re.sub(r'^>\s?', '', full_text, flags=re.MULTILINE)
        if len(full_text) > 30 and act:
            prompts.append({
                "act": act,
                "prompt": full_text,
                "source": f"{source_name}#i-want",
            })

    return prompts


def parse_from_individual_files(owner: str, repo: str, source_name: str) -> list[dict]:
    """
    For repos like linexjlin/GPTs where prompts are individual files in a directory.
    Reads the README to find links, then fetches each prompt file.
    """
    prompts = []
    readme = get_readme_content(owner, repo)
    if not readme:
        return prompts

    # Find markdown links to prompt files: [Title](./prompts/file.md)
    link_pattern = re.compile(r'\[([^\]]+)\]\(\.?/?prompts/([^)]+)\)')
    links = link_pattern.findall(readme)

    if not links:
        # Try without prompts/ prefix
        link_pattern = re.compile(r'\[([^\]]+)\]\(\.?/?([^)]+\.md)\)')
        links = link_pattern.findall(readme)

    print(f"  📎 Found {len(links)} individual prompt file links")

    for title, path in links[:100]:  # Limit to 100 files
        content = get_raw_file(owner, repo, path)
        if not content:
            # Try with "prompts/" prefix
            content = get_raw_file(owner, repo, f"prompts/{path}")

        if content and len(content) > 30:
            prompts.append({
                "act": title.strip(),
                "prompt": content.strip(),
                "source": f"{source_name}/{path}",
            })

    print(f"  ✅ Fetched {len(prompts)} individual prompt files")
    return prompts


def parse_system_prompts(content: str, source_name: str) -> list[dict]:
    """
    Parse system prompt collections (like LouisShark/chatgpt_system_prompt).
    These often have format:
    ## Title
    ```
    system prompt content
    ```
    """
    prompts = []
    # Pattern: ## Title followed by code block
    pattern = re.compile(
        r'^#{2,4}\s+(.+?)$\s*\n```(?:.*?)\n(.+?)\n```',
        re.MULTILINE | re.DOTALL
    )
    for match in pattern.finditer(content):
        title = match.group(1).strip()
        prompt_content = match.group(2).strip()
        if len(prompt_content) > 20:
            prompts.append({
                "act": title,
                "prompt": prompt_content,
                "source": f"{source_name}#system",
            })

    return prompts


def parse_chinese_prompts(content: str, source_name: str) -> list[dict]:
    """Parse Chinese prompt collections (PlexPt format)."""
    prompts = []

    # Chinese repos often use numbered lists with roles
    # Format: ## 角色名称 or ### 角色名称
    patterns = [
        # ## 担任 X / ## 作为 X / ## 充当 X
        (re.compile(r'^#{2,4}\s*(?:担任|作为|充当|我想让你担任|我要你担任)(.+?)$', re.MULTILINE), "#role"),
        # Numbered: 1. 担任 X
        (re.compile(r'^\d+[\.\)、]\s*(?:担任|作为|充当|我想让你)(.+?)$', re.MULTILINE), "#numbered"),
        # ## Title followed by blockquote
        (re.compile(r'^#{2,4}\s*(.+?)$\s*\n((?:\s*>.+?\n)+)', re.MULTILINE), "#blockquote"),
    ]

    for pattern, ptype in patterns:
        for match in pattern.finditer(content):
            if ptype == "#blockquote":
                act = match.group(1).strip()
                body = match.group(2).strip()
                body = re.sub(r'^>\s?', '', body, flags=re.MULTILINE)
            else:
                act = match.group(1).strip()
                # Get following content
                start = match.end()
                end = min(start + 2000, len(content))
                body = content[start:end]
                # Take content until next header
                next_header = re.search(r'^#{2,4}\s|\n\d+[\.\)]', body, re.MULTILINE)
                if next_header:
                    body = body[:next_header.start()]
                body = body.strip()

            if act and body and len(body) > 15:
                # Sometimes the act name contains the prompt content (if no body)
                if len(body) < 20 and len(act) > 100:
                    prompts.append({
                        "act": act[:60].strip(),
                        "prompt": act,
                        "source": f"{source_name}#chinese-{ptype}",
                    })
                else:
                    prompts.append({
                        "act": act[:80].strip(),
                        "prompt": body,
                        "source": f"{source_name}#chinese-{ptype}",
                    })

    # If no structured prompts found, try to extract role-based sections
    if not prompts:
        # Broad pattern: any ## header followed by explanatory text
        broad = re.compile(
            r'^#{2,4}\s*(.+?)$\s*\n((?:(?!^#{2,4}\s).+\n?){2,40})',
            re.MULTILINE
        )
        for match in broad.finditer(content):
            act = match.group(1).strip()
            body = match.group(2).strip()
            # Skip if it looks like a navigation header
            if act in ("目录", "Table of Contents", "Contents", "说明", "简介", "README",
                        "贡献", "License", "前言", "概述", "介绍", "使用说明", "免责声明"):
                continue
            if len(act) < 3 or len(act) > 100:
                continue
            if len(body) > 30:
                prompts.append({
                    "act": act[:80].strip(),
                    "prompt": body,
                    "source": f"{source_name}#chinese-broad",
                })

    return prompts


# ============================================================
# Main scraper logic
# ============================================================

def scrape_single_github_source(owner: str, repo: str) -> list[dict]:
    """Scrape a single GitHub repo for prompts. Tries multiple strategies."""
    all_prompts = []

    print(f"\n📦 Scraping: {owner}/{repo}")

    # Get repo info
    info = get_repo_info(owner, repo)
    if info:
        stars = info.get("stargazers_count", 0)
        forks = info.get("forks_count", 0)
        desc = (info.get("description") or "N/A")[:80]
        print(f"  ⭐ {stars:,} stars  🍴 {forks:,} forks  📝 {desc}")

    source_name = f"github:{owner}/{repo}"

    # Strategy 1: Try prompts.csv (most common for awesome-chatgpt-prompts)
    csv_content = get_raw_file(owner, repo, "prompts.csv")
    if csv_content:
        print(f"  📄 Found prompts.csv ({len(csv_content):,} chars)")
        prompts = parse_csv(csv_content, source_name)
        if prompts:
            print(f"  ✅ CSV: {len(prompts)} prompts")
            all_prompts.extend(prompts)

    # Strategy 2: Try PROMPTS.md (<details><summary> format)
    prompts_md = get_raw_file(owner, repo, "PROMPTS.md")
    if prompts_md:
        print(f"  📄 Found PROMPTS.md ({len(prompts_md):,} chars)")
        prompts = parse_propmts_md(prompts_md, source_name)
        if prompts:
            print(f"  ✅ PROMPTS.md: {len(prompts)} prompts")
            all_prompts.extend(prompts)

    # Strategy 3: README parsing
    if not all_prompts:
        readme = get_readme_content(owner, repo)
        if readme:
            print(f"  📄 README ({len(readme):,} chars)")

            # 3a: Check for individual file links (GPTs style)
            if '/prompts/' in readme and '.md)' in readme:
                print(f"  🔍 Detected individual file link pattern")
                prompts = parse_from_individual_files(owner, repo, source_name)
                if prompts:
                    all_prompts.extend(prompts)

            # 3b: Try act-as pattern
            if not all_prompts:
                prompts = parse_act_as_markdown(readme, source_name)
                if prompts:
                    print(f"  ✅ Act-as: {len(prompts)} prompts")
                    all_prompts.extend(prompts)

            # 3c: Try system prompt pattern
            if not all_prompts:
                prompts = parse_system_prompts(readme, source_name)
                if prompts:
                    print(f"  ✅ System prompts: {len(prompts)} prompts")
                    all_prompts.extend(prompts)

            # 3d: Try Chinese pattern
            if not all_prompts:
                prompts = parse_chinese_prompts(readme, source_name)
                if prompts:
                    print(f"  ✅ Chinese: {len(prompts)} prompts")
                    all_prompts.extend(prompts)

            # 3e: Fallback - any ## Act as pattern
            if not all_prompts:
                prompts = parse_markdown_fallback(readme, source_name)
                if prompts:
                    print(f"  ✅ Fallback: {len(prompts)} prompts")
                    all_prompts.extend(prompts)

    # Strategy 4: Check known subdirectories for prompt files
    if not all_prompts:
        for subdir in ["prompts", "data", "examples", "prompts-collection"]:
            try:
                files = list_repo_dir(owner, repo, subdir)
                if files and len(files) > 5:
                    print(f"  📂 Found {len(files)} files in {subdir}/")
                    for f in files[:50]:
                        if f["name"].endswith((".md", ".txt", ".csv")):
                            content = get_raw_file(owner, repo, f["path"])
                            if content and len(content) > 30:
                                all_prompts.append({
                                    "act": f["name"].rsplit(".", 1)[0].replace("-", " ").replace("_", " "),
                                    "prompt": content.strip(),
                                    "source": f"{source_name}/{f['path']}",
                                })
                    if all_prompts:
                        print(f"  ✅ Directory: {len(all_prompts)} prompts")
                        break
            except Exception:
                pass

    if not all_prompts:
        print(f"  ⚠ No prompts found for {owner}/{repo}")

    return all_prompts


def parse_markdown_fallback(content: str, source_name: str) -> list[dict]:
    """
    Fallback parser: try to find ANY prompt-like content in markdown.
    Looks for sections with actionable instructions following a title.
    """
    prompts = []
    lines = content.split("\n")

    # Find header-subsequent-content patterns
    i = 0
    while i < len(lines):
        # Match ## header
        match = re.match(r'^#{2,4}\s+(.+?)$', lines[i])
        if match:
            title = match.group(1).strip()
            # Skip non-content headers
            skip_titles = {
                "table of contents", "contents", "目录", "introduction", "getting started",
                "installation", "usage", "contributing", "license", "acknowledgements",
                "related", "references", "links", "resources", "faq", "about", "overview",
                "description", "features", "what is", "why", "how to use", "setup",
                "prerequisites", "requirements", "background", "disclaimer", "免责声明",
                "贡献", "参考", "说明", "许可", "相关", "常见问题",
            }
            if any(title.lower().startswith(s) for s in skip_titles):
                i += 1
                continue

            # Collect content until next header
            body_lines = []
            j = i + 1
            while j < len(lines):
                if re.match(r'^#{2,4}\s', lines[j]):
                    break
                if re.match(r'^---\s*$', lines[j]):
                    break
                body_lines.append(lines[j])
                j += 1

            body = "\n".join(body_lines).strip()
            # Remove blockquote markers
            body = re.sub(r'^>\s?', '', body, flags=re.MULTILINE)
            # Remove code block markers for content
            body = re.sub(r'^```.*?$', '', body, flags=re.MULTILINE)

            if len(body) > 40 and len(title) > 2:
                prompts.append({
                    "act": title[:100].strip(),
                    "prompt": body[:3000].strip(),
                    "source": f"{source_name}#fallback",
                })
            i = j
        else:
            i += 1

    return prompts


def scrape_github(targets: list[dict] = None) -> list[dict]:
    """Main entry point: scrape all configured GitHub sources."""
    if targets is None:
        targets = GITHUB_TARGETS

    all_prompts = []
    seen = set()

    for i, target in enumerate(targets):
        owner = target["owner"]
        repo = target["repo"]
        print(f"\n{'='*60}")
        print(f"[{i+1}/{len(targets)}] {owner}/{repo}")
        print(f"  🏷  Hint: {target['category_hint']} | Min stars: {target['min_stars']:,}")

        try:
            prompts = scrape_single_github_source(owner, repo)

            for p in prompts:
                # Dedup by act + first 80 chars of prompt
                key = (p["act"][:80].lower().strip(),
                       p["prompt"][:80].lower().strip())
                if key not in seen:
                    seen.add(key)
                    p["category_hint"] = target.get("category_hint", "general")
                    p["repo_stars"] = target.get("min_stars", 0)
                    all_prompts.append(p)

            print(f"  📊 Total unique so far: {len(all_prompts)}")
        except Exception as e:
            print(f"  ❌ Error: {e}")

        # Rate limit safety
        if i < len(targets) - 1:
            time.sleep(1.0)

    return all_prompts
