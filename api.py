"""
sleepsearch — MCP-compatible research API platform
Modular, extensible, compatible with sleepintel.

Each source becomes a tool that can be called by sleepintel's JEV system.
All sources are free (PD, CC0, CC-BY, or free API tier).
"""

import json
import os
import urllib.request
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent

# ============================================================
# TOOL REGISTRY — each tool is a research source
# ============================================================

TOOLS = {
    # === FAIRY TALES & FOLKLORE ===
    "search.gutenberg.fairy_tales": {
        "desc": "Search Project Gutenberg for fairy tales and folklore",
        "input": {"query": "str", "author": "str?", "language": "str?"},
        "source": "gutenberg.org",
        "license": "PD",
        "cost": "free"
    },
    "search.sacred_text.folklore": {
        "desc": "Search Sacred Texts for folklore and mythology",
        "input": {"query": "str", "tradition": "str?"},
        "source": "sacred-texts.com",
        "license": "PD",
        "cost": "free"
    },
    
    # === PHILOSOPHY & SPIRITUAL ===
    "search.gutenberg.philosophy": {
        "desc": "Search Project Gutenberg for philosophical texts",
        "input": {"query": "str", "author": "str?", "era": "str?"},
        "source": "gutenberg.org",
        "license": "PD",
        "cost": "free"
    },
    "fetch.stoic.texts": {
        "desc": "Fetch Stoic texts (Marcus Aurelius, Seneca, Epictetus)",
        "input": {"author": "str?", "work": "str?"},
        "source": "gutenberg.org",
        "license": "PD",
        "cost": "free"
    },
    
    # === ETYMOLOGY & WORDS ===
    "fetch.etymonline": {
        "desc": "Fetch word etymology from Etymonline",
        "input": {"word": "str"},
        "source": "etymonline.com",
        "license": "proprietary",
        "cost": "free (web scraping)"
    },
    "fetch.wiktionary.etymology": {
        "desc": "Fetch word etymology from Wiktionary",
        "input": {"word": "str", "language": "str?"},
        "source": "en.wiktionary.org",
        "license": "CC BY-SA",
        "cost": "free (API)"
    },
    
    # === SCIENTIFIC DATA ===
    "fetch.pubchem.element": {
        "desc": "Fetch element data from PubChem",
        "input": {"element": "str"},
        "source": "pubchem.ncbi.nlm.nih.gov",
        "license": "public domain",
        "cost": "free (API)"
    },
    "fetch.nasa.apod": {
        "desc": "Fetch NASA Astronomy Picture of the Day",
        "input": {"date": "str?"},
        "source": "api.nasa.gov",
        "license": "public domain",
        "cost": "free (API key required)"
    },
    "fetch.nasa.exoplanets": {
        "desc": "Fetch exoplanet data from NASA",
        "input": {"query": "str?"},
        "source": "exoplanetarchive.ipac.caltech.edu",
        "license": "public domain",
        "cost": "free (API)"
    },
    
    # === AMBIENT SOUNDS ===
    "search.freesound": {
        "desc": "Search Freesound for ambient sounds",
        "input": {"query": "str", "license": "str?"},
        "source": "freesound.org",
        "license": "CC0/CC-BY",
        "cost": "free (API key required)"
    },
    
    # === NEWS ===
    "fetch.goodnews": {
        "desc": "Fetch positive news from Good News Network",
        "input": {"category": "str?"},
        "source": "goodnewsnetwork.org",
        "license": "proprietary",
        "cost": "free (RSS)"
    },
    "fetch.freenewsapi": {
        "desc": "Fetch news from FreeNewsApi",
        "input": {"query": "str", "country": "str?", "language": "str?"},
        "source": "freenewsapi.io",
        "license": "proprietary",
        "cost": "free (5K req/day)"
    },
    
    # === HISTORICAL DATA ===
    "fetch.historylabs.events": {
        "desc": "Fetch historical events by date or year",
        "input": {"date": "str?", "year": "int?"},
        "source": "events.historylabs.io",
        "license": "MIT",
        "cost": "free (API)"
    },
    "fetch.chronicling_america": {
        "desc": "Search historic American newspapers",
        "input": {"query": "str", "year": "int?", "state": "str?"},
        "source": "chroniclingamerica.loc.gov",
        "license": "public domain",
        "cost": "free (API)"
    },
    
    # === SCIENCE FICTION ===
    "search.gutenberg.scifi": {
        "desc": "Search Project Gutenberg for science fiction",
        "input": {"query": "str", "author": "str?"},
        "source": "gutenberg.org",
        "license": "PD",
        "cost": "free"
    },
    "fetch.agi.predictions": {
        "desc": "Fetch AGI timeline predictions",
        "input": {"source": "str?"},
        "source": "skynetcountdown.com",
        "license": "free",
        "cost": "free (web)"
    },
    
    # === CHESS ===
    "fetch.lichess.openings": {
        "desc": "Fetch chess opening data from Lichess",
        "input": {"opening": "str?"},
        "source": "lichess.org",
        "license": "CC BY-SA",
        "cost": "free (API)"
    },
    
    # === PRODUCT DATA ===
    "fetch.openproductdata": {
        "desc": "Fetch product data from OpenProductData",
        "input": {"query": "str"},
        "source": "openproductdata.org",
        "license": "free",
        "cost": "free (API)"
    },
    "fetch.gsmarena.specs": {
        "desc": "Fetch phone specifications from GSMArena",
        "input": {"phone": "str"},
        "source": "gsmarena.com",
        "license": "proprietary",
        "cost": "free (web scraping)"
    },
    
    # === MATH & NUMBERS ===
    "fetch.oeis.sequence": {
        "desc": "Fetch integer sequences from OEIS",
        "input": {"query": "str", "sequence": "str?"},
        "source": "oeis.org",
        "license": "CC BY-SA",
        "cost": "free (API)"
    },
    
    # === WEATHER ===
    "fetch.openmeteo": {
        "desc": "Fetch weather data from Open-Meteo",
        "input": {"latitude": "float", "longitude": "float", "days": "int?"},
        "source": "open-meteo.com",
        "license": "CC BY-SA",
        "cost": "free (API)"
    }
}

# ============================================================
# TOOL IMPLEMENTATIONS
# ============================================================

def search_gutenberg(query, author=None, subject=None):
    """Search Project Gutenberg."""
    params = {"query": query}
    if author: params["author"] = author
    if subject: params["subject"] = subject
    
    url = f"https://www.gutenberg.org/ebooks/search/?{urllib.parse.urlencode(params)}"
    # In production, parse the HTML response
    return {"url": url, "results": "See URL for results"}

def fetch_etymonline(word):
    """Fetch word etymology from Etymonline."""
    url = f"https://www.etymonline.com/word/{urllib.parse.quote(word)}"
    # In production, parse the HTML response
    return {"url": url, "word": word}

def fetch_wiktionary_etymology(word, language="en"):
    """Fetch word etymology from Wiktionary."""
    url = f"https://en.wiktionary.org/api/rest_v1/page/definition/{urllib.parse.quote(word)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "sleepsearch/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_pubchem_element(element):
    """Fetch element data from PubChem."""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/element/series/{urllib.parse.quote(element)}/JSON"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_nasa_apod(date=None):
    """Fetch NASA Astronomy Picture of the Day."""
    api_key = os.environ.get("NASA_API_KEY", "DEMO_KEY")
    params = {"api_key": api_key}
    if date: params["date"] = date
    
    url = f"https://api.nasa.gov/planetary/apod?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_historylabs_events(date=None, year=None):
    """Fetch historical events."""
    if date:
        url = f"https://events.historylabs.io/date?date={urllib.parse.quote(date)}"
    elif year:
        url = f"https://events.historylabs.io/year/{year}"
    else:
        return {"error": "Either date or year required"}
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_goodnews(category=None):
    """Fetch positive news from Good News Network RSS."""
    url = "https://www.goodnewsnetwork.org/feed/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "sleepsearch/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            # Parse RSS XML in production
            return {"status": "ok", "source": "goodnewsnetwork.org"}
    except Exception as e:
        return {"error": str(e)}

def fetch_freenewsapi(query, country=None, language=None):
    """Fetch news from FreeNewsApi."""
    api_key = os.environ.get("FREENEWSAPI_KEY", "")
    if not api_key:
        return {"error": "FREENEWSAPI_KEY not set"}
    
    params = {"language": language or "en", "country": country or "us", "q": query}
    url = f"https://freenewsapi.com/v1/news?{urllib.parse.urlencode(params)}"
    
    try:
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_lichess_openings(opening=None):
    """Fetch chess opening data from Lichess."""
    if opening:
        url = f"https://explorer.lichess.ovh/masters?play={urllib.parse.quote(opening)}"
    else:
        url = "https://explorer.lichess.ovh/masters"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

def fetch_oeis_sequence(query=None, sequence=None):
    """Fetch integer sequences from OEIS."""
    if sequence:
        url = f"https://oeis.org/search?q={urllib.parse.quote(sequence)}&language=english&go=Search"
    elif query:
        url = f"https://oeis.org/search?q={urllib.parse.quote(query)}&language=english&go=Search"
    else:
        return {"error": "Either query or sequence required"}
    
    # In production, parse the HTML response
    return {"url": url, "results": "See URL for results"}

def fetch_openmeteo(latitude, longitude, days=7):
    """Fetch weather data from Open-Meteo."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }
    if days: params["forecast_days"] = days
    
    url = f"https://api.open-meteo.com/v1/forecast?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response)
    except Exception as e:
        return {"error": str(e)}

# ============================================================
# DISPATCH TABLE
# ============================================================

DISPATCH = {
    "search.gutenberg.fairy_tales": lambda **kw: search_gutenberg(kw.get("query", ""), kw.get("author"), "fairy tales"),
    "search.gutenberg.philosophy": lambda **kw: search_gutenberg(kw.get("query", ""), kw.get("author"), "philosophy"),
    "search.gutenberg.scifi": lambda **kw: search_gutenberg(kw.get("query", ""), kw.get("author"), "science fiction"),
    "fetch.etymonline": lambda **kw: fetch_etymonline(kw["word"]),
    "fetch.wiktionary.etymology": lambda **kw: fetch_wiktionary_etymology(kw["word"], kw.get("language", "en")),
    "fetch.pubchem.element": lambda **kw: fetch_pubchem_element(kw["element"]),
    "fetch.nasa.apod": lambda **kw: fetch_nasa_apod(kw.get("date")),
    "fetch.historylabs.events": lambda **kw: fetch_historylabs_events(kw.get("date"), kw.get("year")),
    "fetch.goodnews": lambda **kw: fetch_goodnews(kw.get("category")),
    "fetch.freenewsapi": lambda **kw: fetch_freenewsapi(kw["query"], kw.get("country"), kw.get("language")),
    "fetch.lichess.openings": lambda **kw: fetch_lichess_openings(kw.get("opening")),
    "fetch.oeis.sequence": lambda **kw: fetch_oeis_sequence(kw.get("query"), kw.get("sequence")),
    "fetch.openmeteo": lambda **kw: fetch_openmeteo(kw["latitude"], kw["longitude"], kw.get("days")),
}

def handle(tool_name, **kwargs):
    """Handle a tool call."""
    fn = DISPATCH.get(tool_name)
    if not fn:
        return {"error": f"Unknown tool: {tool_name}"}
    return fn(**kwargs)

# ============================================================
# MCP SERVER INTERFACE
# ============================================================

def list_tools():
    """List all available tools."""
    return {"tools": [{"name": k, "description": v["desc"], "input": v["input"]} for k, v in TOOLS.items()]}

def call_tool(name, arguments):
    """Call a tool by name."""
    return handle(name, **arguments)

# ============================================================
# CLI INTERFACE
# ============================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("sleepsearch — Research API for sleepintel")
        print("\nUsage:")
        print("  python3 api.py list              List all tools")
        print("  python3 api.py <tool> <json>     Call a tool")
        print("\nExample:")
        print('  python3 api.py fetch.etymonline \'{"word": "salary"}\'')
        sys.exit(0)
    
    if sys.argv[1] == "list":
        tools = list_tools()
        for tool in tools["tools"]:
            print(f"  {tool['name']}: {tool['description']}")
        sys.exit(0)
    
    tool_name = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    
    result = call_tool(tool_name, **args)
    print(json.dumps(result, indent=2))
