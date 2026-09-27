# Sleep Channel — Daily Formats

*What actually makes fresh content every day, and how to research habit
channels — a method that is NOT search volume.*

Compiled 2026-09-26. Search quota exhausted at query 86 (`Search Queries`
metric, resets **2026-09-27 07:00 UTC**). Round 5 of `CATEGORIES` probes is
**blocked until then**. Everything below used `videos.list` /
`channels.list` / `playlistItems.list` — **1 unit each**, unaffected.

---

## 1. Why the "verse of the day" formats are wrong — and it's not taste

Your instinct that bible-verse / tarot-of-the-day / gratitude-prompt are
"bullshit" **is the inauthentic-content policy restated as taste.**

| Format | Pool size | Exhausts in | Then? |
|---|---|---|---|
| Tarot | **78 cards** | 78 days | repeats |
| I Ching | **64 hexagrams** | 64 days | repeats |
| Daily stoic quote | ~366 passages | 1 year | repeats |
| Bible verse | large but **finitely enumerated** | ~2 yrs | repeats |

Repetition is the flag. From `RESEARCH.md` §3, YouTube's detection signals
include *"titles follow formulaic templates"* and content *"that looks like it's
made with a template with little to no variation across videos."*

> A finite-pool daily channel **guarantees its own repetition** on a fixed
> schedule. It is a template that counts down to the moment it becomes
> detectable.

**A genuinely fresh daily source has no pool to exhaust.** That's the selection
criterion — not "is it daily" but **"does tomorrow's material already exist
without me inventing it."**

---

## 2. The formats that pass that test

### ✅ Tier A — new by nature, rights-clean, sleep-shaped

| Format | Why it's genuinely fresh | Source / rights |
|---|---|---|
| **Tonight's sky** | The sky changes every night: moon phase, visible planets, meteors, what's rising. **Nothing to write — the content arrives** | Ephemeris (computed, PD) · NASA (PD) |
| **NASA APOD** | **A brand-new image every single day since 1995**, with an API. Cosmos is inherently bedtime | **Public domain** |
| **Earth from space / ISS** | New imagery daily | **NASA, public domain** |
| **Good news / heartwarming** 🚩 *your idea* | New stories daily — the wire never stops | ⚠️ **rewrite, never read verbatim** (`CHANNELS.md` §3) |

**NASA APOD is the sleeper pick:** ~9,500 days of existing public-domain
material *plus* one new item daily, forever, free, with an API. A "cosmos to
sleep to" channel built on it has **zero sourcing cost and zero rights risk**.

### ✅ Tier B — new daily, but rights or feed diligence needed

| Format | Freshness | Watch out |
|---|---|---|
| **Live nature cams** (aquarium, aurora, volcano, nest cams) | *Literally* live | each cam has its own owner/license |
| **Aurora / space weather** | new daily (solar wind) | geo-dependent; renders best at high latitudes |
| **Volcano / seismic report** | new eruptions daily | great ambient visuals, but earthquakes = distress risk |
| **Weather around the world** | new storms/fog/snow | attribution; don't monetise disasters |
| **Ocean / buoy conditions** | new daily | thin narrative |

### ❌ Tier C — looks daily, isn't

Anything where *you* generate the material on a schedule: affirmations,
gratitude prompts, "thought of the day," horoscopes, re-rendered ambience with
a new date stamp. **That's a template with a counter.**

---

## 3. The research method — search volume is the wrong instrument

**Habit channels are not discovered, they're returned to.** `CATEGORIES.md`
measures *what people search for*. A daily channel lives on *whether people come
back*. Those are different questions needing different instruments.

**New instrument: `routine.py`** — cadence + consistency, from 1-unit calls only.
Ran it over all 142 channels reachable from our stored probes.

### 3.1 Cadence buckets — the opposite of the gurus' claim

| Median gap | n | Median views | View-CV |
|---|---|---|---|
| **<0.5d (multi/day)** | 8 | **1,195** | 1.16 |
| 0.5–2d (daily-ish) | 35 | 11,872 | 1.10 |
| 2–4d | 40 | 12,098 | **0.79** |
| 4–7d | 10 | 18,945 | 0.75 |
| >7d | 46 | **25,546** | 1.18 |

**Multi-per-day channels get ~21× *fewer* median views than the slowest bucket.**
Neither end of the spectrum is where you want to be; **2–7 days is the stable
band on both view count and view consistency.**

*(Caveat: survivorship. Big channels upload less because they're big. But the
multi/day bucket being the worst on every axis is not explained by that.)*

### 3.2 Regularity → predictability — the real mechanism

| Cadence regularity | n | Median **view-CV** |
|---|---|---|
| **Regular** (`gap_cv` < 0.5) | 50 | **0.775** |
| **Irregular** (`gap_cv` ≥ 1.5) | 18 | **1.185** |

**Keeping a steady schedule produces a steadier outcome** — 33% less variance.

**This is the defensible version of the thread's "trust score" claim** from
`SCHEDULE.md`. Not an algorithmic score — *predictability of results*. Keep the
interval, and you can read the signal.

### 3.3 The working daily channels, measured

`gap 0.5–2d` **AND** `view_cv < 1.0` (routine, not lottery), sorted by views:

| Med views | Gap | gap_CV | view_CV | v/sub | Subs | Vids | Channel |
|---|---|---|---|---|---|---|---|
| **56,939** | 1.00d | **0.0** | 0.67 | 0.15 | 388K | 1,136 | **ASMR Historian** |
| 52,587 | 2.00d | 0.24 | 0.84 | 0.15 | 344K | 324 | Sleepy Science Channel |
| 51,350 | 1.29d | 3.15 | 0.67 | 0.01 | 6.5M | 1,801 | Meditative Mind |
| 46,761 | 1.23d | 0.51 | 0.55 | 0.10 | 460K | 215 | Alchemy Healing |
| **38,561** | 2.00d | 0.19 | **0.37** | **1.59** | 24K | 66 | **Nick at Midnight** |
| 37,332 | 2.00d | 0.27 | 0.69 | 0.05 | 722K | 908 | Get Sleepy |
| 28,046 | 1.00d | 0.42 | 0.69 | 0.31 | 90K | 340 | Order 77 |
| 27,073 | 2.00d | 1.79 | 0.40 | 0.47 | 57K | 139 | Sleepy Monk |
| 26,068 | 2.00d | 0.20 | 0.77 | 0.50 | 52K | 127 | Sleepy History Channel |
| 20,373 | 1.98d | 0.43 | **0.33** | 0.03 | 714K | 361 | Sleepless Historian |
| **17,672** | 2.00d | 0.23 | 0.70 | **1.33** | 13K | 63 | **Midnight Monk** |
| 16,156 | 2.00d | 0.21 | 0.49 | 0.01 | 1.6M | 771 | The Relaxed Guy |
| 11,872 | 1.00d | 0.72 | 0.90 | 0.03 | 382K | 721 | Stoic Journal |
| 6,704 | 1.01d | **0.07** | 0.93 | 0.22 | 30K | 173 | Cosmo Explains |
| 3,966 | 1.00d | **0.0** | 0.40 | 0.05 | 83K | 1,604 | The Lucid Mystic's Sleep Music |

**Read the last row pattern first:** `gap_cv = 0.0` means *perfectly* scheduled
— these are automated, and it works.

**The two to study hardest:**
- **Nick at Midnight** — 24K subs, **38.5K median views, view_CV 0.37,
  v/sub 1.59.** A small channel whose every video outperforms its own audience.
  That's the shape to copy: *consistent, and watched beyond the subscriber base.*
- **ASMR Historian** — 1,136 videos at exactly 1.00d, `gap_cv 0.0`,
  56.9K median views. Proof the daily machine runs at scale.

### 3.4 The three-metric definition of a working daily channel

```python
routine_ok = (
    0.5 <= median_gap_days <= 2.0   # daily-ish, not frantic
    and gap_cv < 0.6                # the interval is kept
    and view_cv < 1.0               # every video lands in a band (not a lottery)
    and median_views / subs > 0.10  # beyond the dormant subscriber base
)
```

**`view_cv` is the one that matters most.** A high-variance daily channel isn't
a routine — it's a slot machine with extra uploads.

---

## 4. How to research the next one (blocked ~16h)

Round 5 probes are queued at `/tmp/opencode/yt/queries5.txt`, ready to fire
when search quota resets **2026-09-27 07:00 UTC**:

```
good news every day to sleep to · heartwarming stories to sleep to
daily meditation to sleep to · today in history to sleep to
sleep stories new every night · new sleep story every day  ← autofill-confirmed
```

**Already confirmed from autofill tonight:** `new sleep story every day` is a
real completion — **the audience asks for the daily format by name.**

**Method for daily formats, going forward:**

1. **Autofill** — does anyone type it? *(done: yes for daily sleep stories)*
2. **`routine.py`** on candidate channels — cadence, `gap_cv`, `view_cv`
3. **Only then** `fresh_pct` via `CATEGORIES` — but read it as *churn*, not
   demand, for this format
4. **Pool test** — can the material exhaust? If yes, reject

**The pool test is the one that has no equivalent in the search-data method,
and it's the one that catches bible-verse-of-the-day.**

---

## 5. On the operator you pasted (@egoo_58)

Noted, and treated as **self-reported** — his audience and earnings numbers are
claims, not receipts.

What's worth taking from it is **the operating model, not the numbers**:

> Treat channels as **experiments**. Buy/obtain ones that already have
> impressions. Test fast. Concentrate on the ones that attract an audience.
> Repeat.

**The transferable idea:** *test cheaply, double down on signal.* That's
already `ORGANISE.md` §9's wave structure — except his version **buys**
pre-impressed channels rather than earning them.

**Two flags before adopting the acquisition angle:**
1. **Purchased channels inherit history** — prior strikes, prior audience,
   prior content. Cheap channels are cheap for reasons.
2. It's a **capital** strategy (`$2,000 / 2 months`), which contradicts our
   free-tools posture — and it competes directly with the
   `CHANNELS.md` §6 conclusion that **multiple weak channels lose to one
   well-run one.**

**Take: the test-fast-then-concentrate loop. Leave: the buying.**
