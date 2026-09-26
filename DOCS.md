# sleepsearch Documentation

## Overview

sleepsearch is the research API platform for the sleepintel network. It provides modular, extensible tools for finding sources, validating content, and compiling data for channel production.

## Architecture

```
sleepsearch/
├── api.py              # MCP-compatible API server
├── SOURCES.md          # Master source registry (100+ sources)
├── CHANNELS.md         # Channel-to-source mapping
├── scripts/            # Research scripts
├── queries/            # Saved search results
├── niches/             # Niche analysis
├── competitors/        # Competitor analysis
├── keywords/           # Keyword research
└── reports/            # Analysis reports
```

## Quick Start

### List all tools
```bash
python3 api.py list
```

### Call a tool
```bash
python3 api.py fetch.etymonline '{"word": "salary"}'
python3 api.py fetch.pubchem.element '{"element": "gold"}'
python3 api.py search.gutenberg.fairy_tales '{"query": "snow queen"}'
```

### Integration with sleepintel
```python
from sleepsearch.api import call_tool

# Research a topic
result = call_tool("fetch.historylabs.events", date="2026-09-26")

# Validate source
source = call_tool("search.gutenberg.fairy_tales", query="grimm")
# Check license in source metadata
```

## Tools Reference

### Fairy Tales & Folklore

| Tool | Description | Source | License |
|---|---|---|---|
| `search.gutenberg.fairy_tales` | Search Gutenberg for fairy tales | gutenberg.org | PD |
| `search.sacred_text.folklore` | Search Sacred Texts for folklore | sacred-texts.com | PD |

**Usage:**
```bash
python3 api.py search.gutenberg.fairy_tales '{"query": "snow queen", "author": "andersen"}'
```

**Returns:** URL to search results, list of matching texts

### Philosophy & Spiritual

| Tool | Description | Source | License |
|---|---|---|---|
| `search.gutenberg.philosophy` | Search Gutenberg for philosophical texts | gutenberg.org | PD |
| `fetch.stoic.texts` | Fetch Stoic texts | gutenberg.org | PD |

**Usage:**
```bash
python3 api.py fetch.stoic.texts '{"author": "marcus aurelius", "work": "meditations"}'
```

### Etymology & Words

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.etymonline` | Fetch word etymology | etymonline.com | Free (web) |
| `fetch.wiktionary.etymology` | Fetch etymology from Wiktionary | wiktionary.org | CC BY-SA |
| `fetch.dictionaryapi` | Fetch definitions, pronunciation | dictionaryapi.dev | CC BY-SA |

**Usage:**
```bash
python3 api.py fetch.etymonline '{"word": "salary"}'
python3 api.py fetch.wiktionary.etymology '{"word": "etymology", "language": "en"}'
```

### Scientific Data

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.pubchem.element` | Fetch element data | pubchem.ncbi.nlm.nih.gov | PD |
| `fetch.nasa.apod` | NASA Astronomy Picture of the Day | api.nasa.gov | PD |
| `fetch.nasa.exoplanets` | Exoplanet data | exoplanetarchive.ipac.caltech.edu | PD |
| `fetch.oeis.sequence` | Integer sequences | oeis.org | CC BY-SA |

**Usage:**
```bash
python3 api.py fetch.pubchem.element '{"element": "gold"}'
python3 api.py fetch.nasa.apod '{"date": "2026-09-26"}'
```

### Ambient Sounds

| Tool | Description | Source | License |
|---|---|---|---|
| `search.freesound` | Search Freesound for sounds | freesound.org | CC0/CC-BY |

**Usage:**
```bash
python3 api.py search.freesound '{"query": "rain city night"}'
```

### News & Current Events

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.goodnews` | Positive news | goodnewsnetwork.org | Free RSS |
| `fetch.freenewsapi` | Global news | freenewsapi.io | Free (5K/day) |
| `fetch.gdelt` | Global news events | gdeltproject.org | Free |

**Usage:**
```bash
python3 api.py fetch.freenewsapi '{"query": "good news", "country": "us"}'
```

### Historical Data

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.historylabs.events` | Historical events | events.historylabs.io | MIT |
| `fetch.chronicling_america` | Historic newspapers | chroniclingamerica.loc.gov | PD |

**Usage:**
```bash
python3 api.py fetch.historylabs.events '{"date": "2026-09-26"}'
python3 api.py fetch.historylabs.events '{"year": 1776}'
```

### Science Fiction & AGI

| Tool | Description | Source | License |
|---|---|---|---|
| `search.gutenberg.scifi` | Search Gutenberg for sci-fi | gutenberg.org | PD |
| `fetch.agi.predictions` | AGI timeline predictions | skynetcountdown.com | Free |

### Chess & Games

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.lichess.openings` | Chess opening data | lichess.org | CC BY-SA |

### Product Data

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.openproductdata` | Product specifications | openproductdata.org | Free |
| `fetch.gsmarena.specs` | Phone specifications | gsmarena.com | Free (web) |

### Weather

| Tool | Description | Source | License |
|---|---|---|---|
| `fetch.openmeteo` | Weather forecast | open-meteo.com | CC BY-SA |

## Channel-to-Source Mapping

See `CHANNELS.md` for the complete mapping of every channel to its research sources.

## Adding New Sources

1. Add tool definition to `TOOLS` dict in `api.py`
2. Implement the fetch function
3. Add to `DISPATCH` table
4. Update `SOURCES.md` with source details
5. Update `CHANNELS.md` with channel mapping

## API Key Management

Some tools require API keys:
- **NASA API**: Get free key at api.nasa.gov
- **FreeNewsApi**: Get free key at freenewsapi.io
- **Freesound**: Get free key at freesound.org/docs/api

Store keys in environment variables:
```bash
export NASA_API_KEY=your_key
export FREENEWSAPI_KEY=your_key
export FREESOUND_KEY=your_key
```

## License

All tools use free sources (PD, CC0, CC-BY, or free API tiers).
No paid APIs required for core functionality.
