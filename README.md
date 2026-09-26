# sleepsearch

Market research, niche validation, and demand probing for the sleep content network.

## Purpose

- YouTube API research (search queries, video data, channel analysis)
- Niche validation (demand, competition, freshness)
- Keyword research (autofill, search volume, competition)
- Competitor analysis (what works, what doesn't)
- Content gap identification

## Structure

```
sleepsearch/
├── queries/          # Search queries and results
├── niches/           # Niche analysis and validation
├── competitors/      # Competitor channel analysis
├── keywords/         # Keyword research and autofill data
├── reports/          # Analysis reports
└── scripts/          # YouTube API scripts
```

## Usage

```bash
# Run a search
python scripts/search.py --query "history to sleep to"

# Analyze a niche
python scripts/analyze_niche.py --niche "fairy tales"

# Check freshness
python scripts/freshness.py --query "rain sounds to sleep to"
```
