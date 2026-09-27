# Sleep Channel — Category Research

*YouTube Data API v3 probe. 48 unique queries, top-10 results each, all pulled
2026-09-26.*

**Method:** `search.list` (EN, `regionCode=US`, relevance-ranked) → `videos.list`
(views / published / duration) → `channels.list` (subscriber counts).
~4,800 quota units of a 10,000 daily budget. **The API key was passed as an env
var and is not stored in this repository.**

**What "median of top 10" measures:** what currently *ranks*. It is a proxy for
the competitive bar, **not** total search volume. Treat it as "what you're up
against," not "how many people want this."

---

## 1. The headline

| Tier | n | Median views | **Fresh**<br>(≤18 mo) | Views/day | Duration | Views/sub |
|---|---|---|---|---|---|---|
| **A — enter here** | **16** | **195,580** | **90%** | 1,234 | 170m | 2.1 |
| B — viable, busier | 10 | 370,508 | 65% | 1,088 | 185m | 3.3 |
| **C — entrenched** | 8 | **3,429,088** | **15%** | 3,380 | 447m | 33.7 |
| D — wrong match | 2 | 56,318 | — | — | **9m** | — |
| E — no demand | 2 | 12,510 | 90% | 73 | 154m | 2.1 |

**Tier C is the entire generic sleep niche** — 3.4M median views but only
**15% of top results are less than 18 months old.** Those slots are held by
uploads years old. High demand, closed door.

**Tier A is 90% fresh with a 195K bar.** Newcomers are ranking, and the median
result is beatable.

`fresh_pct` = share of the top 10 published within the last 540 days. **It is
the single most useful number in this file** — it measures whether the door is
open, not how big the room is.

---

## 2. Tier A — the 16 to enter

| Median views | **Fresh** | Views/day | V/subs | Dur | Query |
|---|---|---|---|---|---|
| 62,718 | **100%** | 182 | 0.3 | 139m | geology to sleep to |
| 183,435 | **100%** | 1,337 | 3.7 | 149m | history to sleep to no ads |
| 190,853 | **100%** | 1,218 | 0.4 | 174m | mythology to sleep to |
| 200,308 | **100%** | 1,476 | 2.0 | 142m | **history to sleep to** |
| 348,927 | **100%** | 835 | 1.3 | 154m | psychology to sleep to |
| 814,753 | **100%** | 2,306 | 1.9 | 130m | nature documentary to sleep to |
| 94,939 | 90% | 831 | 3.9 | **307m** | sleep story for adults no ads |
| 120,159 | 90% | 1,530 | 0.5 | 214m | reddit stories to fall asleep to |
| 135,879 | 90% | 504 | **13.1** | 170m | **video game lore to sleep to** |
| 186,393 | 90% | 664 | 2.5 | 237m | star wars to sleep to |
| 399,548 | 90% | 1,453 | 1.2 | 171m | astronomy to sleep to |
| 815,807 | 90% | **3,054** | 2.5 | 175m | **minecraft to sleep to** |
| 158,707 | 80% | 637 | 6.5 | 115m | elden ring lore to sleep to |
| 438,316 | 80% | 1,250 | 2.3 | 139m | ancient civilizations to sleep to history |
| 478,852 | 80% | 1,274 | 1.2 | 172m | space to sleep to |
| 493,164 | 80% | 1,164 | **12.0** | 189m | philosophy to sleep to |

### The four standouts

1. **`history to sleep to`** — 200K, **100% fresh**, 1,476 views/day, 142 min.
   Every slot in the top 10 turned over in 18 months. Autofill-confirmed
   *(`to sleep to history` was the #1 completion)*. **The cleanest entry.**

2. **`video game lore to sleep to`** — 136K, 90% fresh, **13.1 views per
   subscriber.** That ratio means results are reaching far beyond each
   channel's own audience — pure search/browse discovery. Not subscriber-gated.

3. **`minecraft to sleep to`** — 816K median **and** 3,054 views/day, 90% fresh.
   Highest velocity in Tier A with an open door. (Autofill: `to sleep to
   minecraft`, `to fall asleep to minecraft`.)

4. **`nature documentary to sleep to`** — 815K, **100% fresh**, 2,306 views/day.
   Biggest demand in Tier A, fully churning.

### Read the v/subs column

`views ÷ channel subscribers`. **High = the video outperformed its channel =
discovered by strangers.** Low = it leaned on the existing subscriber base.

- `video game lore` **13.1** · `philosophy` **12.0** → search-driven, a new
  channel can win these slots
- `geology` **0.3** · `mythology` **0.4** → ranking, but views sit close to
  sub count. Slower, more grind-y

**Best combined entry signal: high fresh + high v/subs + 60 min+.**
`video game lore` and `philosophy` lead on that.

---

## 3. Tier C — the door is closed

| Median views | Fresh | Dur | Query |
|---|---|---|---|
| 2,904,634 | 30% | 540m | white noise to sleep to |
| 3,759,925 | 30% | 330m | forest sounds to sleep to |
| 395,142 | 20% | 180m | bedtime story for adults with rain |
| 4,264,290 | 20% | 660m | black screen sleep music no ads |
| 1,769,354 | 10% | 534m | trains to sleep to |
| 20,586,348 | 10% | 360m | thunderstorm sounds to sleep to |
| **34,902,647** | **10%** | 240m | **rain sounds to sleep to** |
| **3,098,252** | **0%** | 660m | **brown noise to sleep to** |

**`brown noise to sleep to`: 0% fresh.** Not a single top-10 result is under
18 months old. The slot has been closed since 2025.

These are the categories everyone recommends to beginners. **They are the
worst possible entry points** — 3.4M median views behind a 15%-fresh door.

---

## 4. The autofill oracle — and where Medium was wrong

Pulled live from `clients1.google.com/complete/search?client=youtube&ds=yt`.

### `to sleep to`
```
history · lore · no ads · games · music · facts · video
minecraft · fnaf · no ai · star wars
```

### `to fall asleep to`
```
history · no ads · games · lore · facts · minecraft
music · spongebob · asmr · reddit · star wars · stories
```

### `lore to sleep to` ← the strongest signal in the file
```
warhammer · elden ring · no ads · dark souls · 40k · warhammer 40k
elder scrolls · halo · bloodborne · star wars · resident evil
```

### `to sleep to history`
```
history to sleep to · ancient civilizations · fall asleep to history no ads
documentary to fall asleep to history · fall asleep to history ww2
fall asleep to history of london · fall asleep to history no ai
```

### `to sleep to mythology`
```
norse mythology · japanese mythology · hindu mythology · mythology sleep stories
```

### Scoring Medium's recommended list against the API

| Medium suggested | Autofill? | API result | Verdict |
|---|---|---|---|
| Psychology to Sleep To | ✗ | 349K, **100% fresh** | ✅ **works anyway** |
| Mythology Sleep Narratives | ✅ norse/japanese/hindu | 191K, **100% fresh** | ✅ confirmed |
| Video Game Lore to Sleep To | ✅ **11 specific titles** | 136K, 90%, **v/sub 13.1** | ✅ **confirmed, strongest** |
| Ancient Civilizations | ✅ | 504K, 70% fresh | ✅ confirmed |
| Deep Sea Lore | ✗ | 4.2M, **40% fresh** | ⚠️ works, but Tier B — busy |
| **Forgotten Religions** | ✗ | **133 median views** | ❌ **no supply, no demand** |
| **Phobias Explained Slowly** | ✗ | **9.4 min duration** | ❌ **not sleep content at all** |

**Medium's list was ~60% right.** Autofill validated 3 of 7; the API killed 2.
`forgotten religions to sleep to` returns a **median of 133 views** across the
top 10 — there is nothing there because nobody is searching for it.
`phobias explained slowly` returns ~9-minute videos, i.e. the query doesn't
land in sleep at all.

> **Lesson:** autofill is a strong signal, not proof. A query that neither
> autofills **nor** returns long results is a dead end. **Always run the API
> before committing to a topic.**

---

## 5. Two modifiers that are demand, not gimmicks

Every single seed we probed produced both of these:

### `no ads` — universal
```
to sleep to no ads · sleep sounds no ads · sleep story for adults no ads
sounds for sleeping no ads · bedtime story for adults no ads
black screen sleep music no ads · history to sleep to no ads
```
**The audience searches for ad-free.** The `NO ADS` title convention we
documented in `GUIDES.md` §6.1 is a *response to demand*, not a creator quirk.
Titles should carry it.

### `no ai` — the warning
```
to sleep to no ai · fall asleep to history no ai · 🔴 Gentle Night Rain — (NO AI)
```
**The audience is actively filtering out AI-looking content.** Two live results
carry `(NO AI)` or `NO AI` in the *title* as a selling point.

This bears directly on `STRATEGY.md`: AI generation is a *production* tool, and
the moment it's visible in the output, it becomes a **disadvantage with the
exact audience we're courting.** Reinforces R3 (original visual per upload) and
the whole distinctness argument — but now with audience evidence rather than
policy evidence.

Also surfaced: **language variants are real demand** —
`sleep story for adults` autofills *hindi · tamil · telugu · tagalog*.
Held deliberately: `STRATEGY.md` open question #4 said prove EN first.

---

## 6. Method notes & caveats

- **Relevance-ranked, not view-ranked.** `order` defaults to relevance, which
  mirrors what a real searcher sees. Sorting by `viewCount` would inflate
  everything.
- **`fresh_pct` uses 540 days.** Chosen over a 365-day window because sleep
  catalogs turn over on a ~1-year production cycle; 365 was too harsh and
  penalised healthy channels.
- **Median, not mean.** One 84M-view video (the `ocean waves` outlier) would
  have flattened every comparison.
- **`dur = 0` means a live stream.** `search.list` returns `secs=0` for live
  broadcasts — confirmed by the 🔴 markers in titles. `ocean waves to sleep to`
  and `sleep sounds black screen` are live-format, both Tier C anyway.
- **Not measured:** actual search volume (API has no keyword-tool endpoint),
  RPM, and whether these viewers monetise. This file measures **the competitive
  bar**, nothing else. `RESEARCH.md` §1 owns the money question.
- **Region-locked to US/English.** `RESEARCH.md` §1 says geo is worth ~20×.
  Everything here is the highest-value geo by construction — and therefore the
  most competitive.

---

## 7. Recommendation

**Primary:** `history to sleep to` — 100% fresh, autofill-confirmed, 1,476
views/day, 142-minute format, and it naturally subclasses (ancient
civilizations · ww2 · london · documentary) so one query template yields a
deep catalog without repeating itself.

**Secondary:** `video game lore to sleep to` — the autofill depth (11 distinct
franchises) plus **13.1 views/sub** is the best discovery signal measured.
Elden Ring · Dark Souls · Warhammer 40k · Elder Scrolls · Halo · Bloodborne ·
Resident Evil each stand alone as a video. That is *structural* variation —
`STRATEGY.md` R1 satisfied by construction, not by adjective-swapping.

**Avoid entirely:** everything in Tier C, plus `forgotten religions`
(133 views) and `phobias explained slowly` (wrong format).

**Before committing to any topic:** run the autofill probe *and* the API probe.
Two minutes, ~200 quota units, and it would have caught both of Medium's
misses.
