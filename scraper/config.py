"""
Configuration for the Prompt Skills Scraper.
All target sources are real, verifiable repositories and websites.
"""

# ============================================================
# High-Star GitHub Repositories (verified real repositories)
# ============================================================
GITHUB_TARGETS = [
    {
        "owner": "f",
        "repo": "awesome-chatgpt-prompts",
        "min_stars": 100000,
        "category_hint": "general",
        "description": "The most famous ChatGPT prompts collection - 100k+ stars",
    },
    {
        "owner": "dair-ai",
        "repo": "Prompt-Engineering-Guide",
        "min_stars": 45000,
        "category_hint": "engineering",
        "description": "Comprehensive prompt engineering guide by DAIR.AI",
    },
    {
        "owner": "linexjlin",
        "repo": "GPTs",
        "min_stars": 25000,
        "category_hint": "general",
        "description": "Leaked prompts of GPTs - huge collection",
    },
    {
        "owner": "LouisShark",
        "repo": "chatgpt_system_prompt",
        "min_stars": 8000,
        "category_hint": "system-prompt",
        "description": "Collection of ChatGPT system prompts",
    },
    {
        "owner": "PlexPt",
        "repo": "awesome-chatgpt-prompts-zh",
        "min_stars": 50000,
        "category_hint": "chinese",
        "description": "Chinese ChatGPT prompts collection - 50k+ stars",
    },
    {
        "owner": "yunwei37",
        "repo": "Prompt-Engineering-Guide-zh-CN",
        "min_stars": 3000,
        "category_hint": "engineering-zh",
        "description": "Chinese prompt engineering guide",
    },
    {
        "owner": "promptslab",
        "repo": "Awesome-Prompt-Engineering",
        "min_stars": 2000,
        "category_hint": "engineering",
        "description": "Awesome prompt engineering resources",
    },
    {
        "owner": "snwfdhxp",
        "repo": "awesome-chatgpt-prompts-zh",
        "min_stars": 2000,
        "category_hint": "chinese",
        "description": "Another high-quality Chinese prompt collection",
    },
    {
        "owner": "EmbraceAGI",
        "repo": "ChatGPT-Prompts",
        "min_stars": 1000,
        "category_hint": "general",
        "description": "Curated ChatGPT prompts collection",
    },
    {
        "owner": "mattnigh",
        "repo": "ChatGPT3-Free-Prompt-List",
        "min_stars": 2000,
        "category_hint": "general",
        "description": "Free prompt list for ChatGPT",
    },
    {
        "owner": "git-ak",
        "repo": "awesome-chatgpt-prompts",
        "min_stars": 500,
        "category_hint": "general",
        "description": "Curated list of ChatGPT prompts",
    },
    {
        "owner": "thinkingjimmy",
        "repo": "ChatGPT-Prompts",
        "min_stars": 500,
        "category_hint": "general",
        "description": "Organized ChatGPT prompts",
    },
]

# ============================================================
# Web Sources - Real prompt collection sites (for reference)
# ============================================================
WEB_SOURCES = [
    {
        "url": "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv",
        "name": "awesome-chatgpt-prompts-csv",
        "format": "csv",
    },
    {
        "url": "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/README.md",
        "name": "awesome-chatgpt-prompts-readme",
        "format": "markdown",
    },
]

# ============================================================
# Output Configuration
# ============================================================
OUTPUT_DIR = "prompts"  # Relative to project root

# Categories for prompt classification
CATEGORIES = [
    "programming",
    "writing",
    "business",
    "education",
    "creative",
    "analysis",
    "productivity",
    "roleplay",
    "technical",
    "marketing",
    "health",
    "finance",
    "legal",
    "chinese",
    "system-prompt",
    "engineering",
    "general",
]

# Keywords for auto-categorization
CATEGORY_KEYWORDS = {
    "programming": [
        "code", "programming", "python", "javascript", "debug", "function",
        "algorithm", "api", "software", "developer", "react", "sql", "database",
        "coding", "script", "bash", "html", "css", "java", "golang", "rust",
        "typescript", "web", "app", "docker", "kubernetes", "linux", "git",
    ],
    "writing": [
        "write", "essay", "article", "blog", "story", "poem", "content",
        "copy", "edit", "proofread", "grammar", "rewrite", "summarize",
        "paragraph", "novel", "fiction", "narrative", "manuscript",
    ],
    "business": [
        "business", "startup", "strategy", "revenue", "pitch", "investor",
        "sales", "negotiation", "enterprise", "ceo", "management", "kpi",
        "roi", "budget", "profit", "client", "stakeholder", "lean",
    ],
    "education": [
        "teach", "learn", "explain", "tutor", "lesson", "course", "study",
        "exam", "quiz", "curriculum", "student", "professor", "academic",
        "textbook", "homework", "education", "training", "concept",
    ],
    "creative": [
        "creative", "design", "art", "draw", "paint", "color", "illustration",
        "music", "song", "lyrics", "poetry", "imagine", "visual", "graphic",
        "ui", "ux", "interface", "logo", "brand", "aesthetic", "style",
    ],
    "analysis": [
        "analyze", "analysis", "data", "research", "insight", "trend",
        "statistics", "report", "evaluate", "assess", "review", "audit",
        "diagnostic", "metrics", "benchmark", "compare", "pattern",
    ],
    "productivity": [
        "plan", "organize", "schedule", "task", "todo", "goal", "habit",
        "workflow", "automate", "efficiency", "priority", "deadline",
        "calendar", "project", "manage", "focus", "routine", "meeting",
    ],
    "roleplay": [
        "act as", "pretend", "role", "character", "persona", "simulate",
        "impersonate", "you are a", "behave like", "扮演", "角色",
    ],
    "technical": [
        "technical", "engineering", "science", "math", "physics", "chemistry",
        "biology", "neural", "model", "training", "machine learning", "ai",
        "deep learning", "nlp", "computer vision", "robotics", "quantum",
    ],
    "marketing": [
        "marketing", "seo", "social media", "ad", "campaign", "brand",
        "audience", "conversion", "funnel", "content marketing", "email",
        "click", "traffic", "growth", "viral", "influencer", "copywriting",
    ],
    "health": [
        "health", "medical", "doctor", "patient", "diagnosis", "treatment",
        "fitness", "nutrition", "diet", "exercise", "mental health",
        "therapy", "wellness", "symptom", "medicine", "surgery",
    ],
    "finance": [
        "finance", "investment", "stock", "crypto", "trading", "portfolio",
        "tax", "accounting", "bank", "loan", "mortgage", "insurance",
        "retirement", "saving", "wealth", "dividend", "bitcoin", "ethereum",
    ],
    "legal": [
        "legal", "law", "contract", "compliance", "regulation", "patent",
        "copyright", "license", "attorney", "court", "litigation", "gdpr",
        "privacy", "terms", "agreement", "liability", "intellectual",
    ],
    "chinese": [
        "中文", "中国", "汉语", "普通话", "翻译", "chinese", "mandarin",
    ],
    "system-prompt": [
        "system prompt", "system message", "you are chatgpt", "you are a large",
        "custom instructions", "personality", "behavior", "tone",
    ],
    "engineering": [
        "prompt engineering", "few-shot", "zero-shot", "chain of thought",
        "cot", "react", "self-consistency", "tree of thought", "tot",
        "retrieval augmented", "rag", "fine-tune", "embedding",
    ],
}

# ============================================================
# Quality thresholds
# ============================================================
MIN_STARS_FOR_HIGH_QUALITY = 500
MIN_FORKS_FOR_HIGH_QUALITY = 100

# GitHub API (no auth = 60 req/hour, with token = 5000 req/hour)
# Set GITHUB_TOKEN env var for higher rate limits
GITHUB_API_BASE = "https://api.github.com"
