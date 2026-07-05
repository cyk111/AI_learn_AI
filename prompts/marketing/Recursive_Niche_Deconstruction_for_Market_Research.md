# Recursive Niche Deconstruction for Market Research

**Category:** analysis, marketing
**Source:** github:f/awesome-chatgpt-prompts#csv
**Repo Stars:** ⭐ 100,000

---

## Prompt

{
  "industry": "${industry}",
  "region": "${region}",
  "tree": {
    "level": "Macro",
    "name": "...",
    "market_valuation": "$X",
    "top_players": [
      {
        "name": "Company A",
        "type": "Incumbent",
        "focus": "Broad"
      },
      {
        "name": "Company B",
        "type": "Incumbent",
        "focus": "Broad"
      }
    ],
    "children": [
      {
        "level": "Sub-Niche/Micro",
        "name": "...",
        "narrowing_variable": "...",
        "market_valuation": "$X",
        "top_players": [
          {
            "name": "Startup C",
            "type": "Specialist",
            "focus": "Verticalized"
          },
          {
            "name": "Tool D",
            "type": "Micro-SaaS",
            "focus": "Hyper-Specific"
          }
        ],
        "children": []
      }
    ]
  },
  "keyword_analysis": {
    "monthly_traffic": "{region-specific traffic data}",
    "competitiveness": "{region-specific competitiveness data}",
    "potential_keywords": [
      {
        "keyword": "...",
        "traffic": "...",
        "competition": "..."
      }
    ]
  }
}

---

*Collected by Prompt Skills Scraper · Quality verified via GitHub stars ⭐100,000*