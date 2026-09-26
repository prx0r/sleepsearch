"""
YouTube API Research Script
Search queries, analyze videos, check freshness
"""

import os
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta

API_KEY = os.environ.get("YTA")
API_BASE = "https://www.googleapis.com/youtube/v3"

def youtube_get(endpoint, **params):
    """Make a YouTube API request."""
    params["key"] = API_KEY
    url = f"{API_BASE}/{endpoint}?" + urllib.parse.urlencode(params)
    
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=25) as response:
                return json.load(response)
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()[:200]
            if "Quota exceeded" in error_body:
                print(f"QUOTA EXCEEDED: {error_body[:100]}")
                return None
            if e.code in (403, 429, 500, 503):
                time.sleep(1.5 * (attempt + 1))
                continue
            print(f"Error {e.code}: {error_body[:100]}")
            return None
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    
    print("Max retries exceeded")
    return None


def search_videos(query, max_results=10, order="relevance"):
    """Search for videos."""
    results = youtube_get(
        "search",
        part="snippet",
        q=query,
        type="video",
        order=order,
        maxResults=str(max_results),
        relevanceLanguage="en",
        regionCode="US"
    )
    
    if not results:
        return []
    
    videos = []
    for item in results.get("items", []):
        video_id = item.get("id", {}).get("videoId")
        if not video_id:
            continue
        
        snippet = item.get("snippet", {})
        videos.append({
            "video_id": video_id,
            "title": snippet.get("title", ""),
            "channel_id": snippet.get("channelId", ""),
            "channel_title": snippet.get("channelTitle", ""),
            "published_at": snippet.get("publishedAt", ""),
            "description": snippet.get("description", "")[:200]
        })
    
    return videos


def get_video_stats(video_ids):
    """Get statistics for videos."""
    if not video_ids:
        return []
    
    results = youtube_get(
        "videos",
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids[:50])
    )
    
    if not results:
        return []
    
    videos = []
    for item in results.get("items", []):
        stats = item.get("statistics", {})
        content = item.get("contentDetails", {})
        snippet = item.get("snippet", {})
        
        # Parse duration (PT1H23M45S -> seconds)
        duration_str = content.get("duration", "PT0S")
        duration_seconds = parse_duration(duration_str)
        
        # Parse published date
        published_at = snippet.get("publishedAt", "")
        days_old = None
        if published_at:
            pub_date = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
            days_old = (datetime.now(pub_date.tzinfo) - pub_date).days
        
        videos.append({
            "video_id": item.get("id"),
            "title": snippet.get("title", ""),
            "channel_id": snippet.get("channelId", ""),
            "channel_title": snippet.get("channelTitle", ""),
            "view_count": int(stats.get("viewCount", 0)),
            "like_count": int(stats.get("likeCount", 0)),
            "comment_count": int(stats.get("commentCount", 0)),
            "duration_seconds": duration_seconds,
            "duration_minutes": round(duration_seconds / 60, 1),
            "days_old": days_old,
            "published_at": published_at
        })
    
    return videos


def parse_duration(duration_str):
    """Parse ISO 8601 duration (PT1H23M45S) to seconds."""
    import re
    
    match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration_str)
    if not match:
        return 0
    
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    
    return hours * 3600 + minutes * 60 + seconds


def get_channel_stats(channel_id):
    """Get channel statistics."""
    results = youtube_get(
        "channels",
        part="snippet,statistics,contentDetails",
        id=channel_id
    )
    
    if not results or not results.get("items"):
        return None
    
    item = results["items"][0]
    stats = item.get("statistics", {})
    
    return {
        "channel_id": item.get("id"),
        "title": item.get("snippet", {}).get("title", ""),
        "description": item.get("snippet", {}).get("description", "")[:200],
        "subscriber_count": int(stats.get("subscriberCount", 0)),
        "video_count": int(stats.get("videoCount", 0)),
        "view_count": int(stats.get("viewCount", 0)),
        "created_at": item.get("snippet", {}).get("publishedAt", "")
    }


def calculate_freshness(videos, days_threshold=540):
    """Calculate freshness percentage for a set of videos."""
    if not videos:
        return 0
    
    recent_count = sum(1 for v in videos if v.get("days_old", 9999) <= days_threshold)
    return round(recent_count / len(videos) * 100, 1)


def analyze_query(query, max_results=10):
    """Full analysis of a search query."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {query}")
    print(f"{'='*60}")
    
    # Search
    videos = search_videos(query, max_results=max_results)
    if not videos:
        print("No results found")
        return None
    
    # Get stats
    video_ids = [v["video_id"] for v in videos]
    video_stats = get_video_stats(video_ids)
    
    if not video_stats:
        print("Could not get video stats")
        return None
    
    # Calculate metrics
    view_counts = [v["view_count"] for v in video_stats]
    durations = [v["duration_minutes"] for v in video_stats]
    days_old = [v["days_old"] for v in video_stats if v.get("days_old") is not None]
    
    median_views = sorted(view_counts)[len(view_counts) // 2]
    median_duration = sorted(durations)[len(durations) // 2]
    freshness = calculate_freshness(video_stats)
    median_age = sorted(days_old)[len(days_old) // 2] if days_old else None
    
    # Views per day
    views_per_day = []
    for v in video_stats:
        if v.get("days_old") and v["days_old"] > 0:
            vpd = v["view_count"] / v["days_old"]
            views_per_day.append(vpd)
    
    median_vpd = sorted(views_per_day)[len(views_per_day) // 2] if views_per_day else 0
    
    # Print results
    print(f"\nResults:")
    print(f"  Videos found: {len(video_stats)}")
    print(f"  Median views: {median_views:,}")
    print(f"  Median duration: {median_duration:.0f} min")
    print(f"  Median age: {median_age} days" if median_age else "  Median age: N/A")
    print(f"  Freshness: {freshness}%")
    print(f"  Median views/day: {median_vpd:,.0f}")
    
    # Tier classification
    if freshness >= 90 and median_views < 500000:
        tier = "A — ENTER"
    elif freshness >= 60:
        tier = "B — VIABLE"
    elif freshness <= 30:
        tier = "C — CLOSED"
    else:
        tier = "B — BORDERLINE"
    
    print(f"  Tier: {tier}")
    
    # Top videos
    print(f"\nTop videos:")
    for v in sorted(video_stats, key=lambda x: -x["view_count"])[:5]:
        print(f"  {v['view_count']:>12,} views | {v['duration_minutes']:>6.0f} min | {v['days_old'] or '?':>5} days | {v['title'][:50]}")
    
    return {
        "query": query,
        "video_count": len(video_stats),
        "median_views": median_views,
        "median_duration": median_duration,
        "median_age_days": median_age,
        "freshness": freshness,
        "median_views_per_day": median_vpd,
        "tier": tier,
        "videos": video_stats
    }


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python search.py <query>")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    result = analyze_query(query)
    
    if result:
        # Save results
        os.makedirs("queries", exist_ok=True)
        filename = query.replace(" ", "_").replace("'", "")[:50]
        with open(f"queries/{filename}.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nSaved to queries/{filename}.json")
