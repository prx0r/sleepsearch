# Sleep Channel — Upload Schedule

*A claim-by-claim audit of that thread against YouTube's own documentation,
then the schedule that actually follows from it for this niche.*

Compiled 2026-09-26.

> **Source note:** the thread ends in `elevate(.)uno` — it's a funnel. That
> doesn't make it wrong, but every unsourced number in it reads as marketing
> copy until verified. This file tests them.

---

## 1. The verdict up front

**Four of the thread's six core claims are directly contradicted by YouTube's
own help documentation.**

| # | Thread claim | YouTube's documentation | Verdict |
|---|---|---|---|
| 1 | *"scheduling time: **6pm EST. every video. every channel.**"* | *"publish time is **not known to impact a video's long-term performance**"* | ❌ **contradicted** |
| 2 | *"trust damage from uploading 5 videos in 3 days in the first 2 weeks is **PERMANENT**"* | *"**growth in views across uploads is not correlated with time between uploads**"* | ❌ **contradicted** |
| 3 | *"each new upload **benefits from the audience model built by the previous 14**"* | *"the algorithm judges **each video on its own fresh data** rather than your channel's past results"* | ❌ **contradicted** |
| 4 | *"the **3-hour gap rule**... **cannibalizes the impressions**"* | same as #2 | ❌ **contradicted** |
| 5 | Ramp post-monetisation, **only if per-video performance holds** | No official contradiction; matches audience-fatigue literature | ✅ **reasonable** |
| 6 | 55+ drives faceless RPMs of **$15–$35** | Not stated by YouTube. Our sourced sleep figures: **$3.15–$10.92** | ⚠️ **unsourced, above our range** |

---

## 2. YouTube's words, verbatim

### `support.google.com/youtube/answer/16533387` — *The recommendation system*

> **publish time:** The algorithm aims to deliver the right content to viewers
> whenever they visit YouTube, regardless of upload time. While publishing when
> your audience is most active might lead to more immediate views, **we haven't
> observed any evidence that it affects long-term viewership. This is to say
> that publish time is not known to impact a video's long-term performance.**
> Note, however, that **if you're scheduling a Premiere or going live, consider
> your audience's active times to maximise engagement.**

### `support.google.com/youtube/answer/141805` — *Performance FAQ*

> **Publish time is not known to impact a video's long-term performance.**
> Our recommendation system aims to deliver the right videos to the right
> viewers, regardless of when that video was uploaded.

> No, we've done analyses over the years and found that **growth in views
> across uploads is not correlated with time between uploads.** Many creators
> have established reliable connections with their audience through **quality
> over quantity.**

### The three things Gyre's walkthrough of the same doc retires

1. publish time is not known to affect long-term performance
2. **the algorithm judges each video on its own fresh data**, not your channel's past results
3. **taking a break carries no penalty**

**Claims 1–4 of the thread are all in that list.** The thread is confident,
specific, and wrong on precisely the points where it is most confident and
specific. That's the signature of a well-written funnel, not a practitioner.

---

## 3. What actually survives

### ✅ Consistency beats frequency

`fulhar` (100K+ videos, 50+ niches): channels with a **regular schedule — same
day, same time — grow 40% faster** than irregular ones, *regardless of the
specific upload time.*

**The schedule matters. The clock time doesn't.**

### ✅ Day of week — the only timing effect with independent replication

| Source | Method | Finding |
|---|---|---|
| [youtubeproducer](https://youtubeproducer.app/articles/upload-timing-study) | 3,531 videos, 34 channels, 7 niches, via API | **Thursday 2.18×** · Sunday 2.06× · Wednesday 3rd · **Friday worst (1.40×)**. Best-vs-worst gap **56%** |
| `fulhar` | 100K+ videos | **Thursday** highest initial views · Wednesday mid-week · Friday weakest |

Sunday is the interesting one: **only 7.3% of uploads land there, yet it
performs 2nd** — less competition, same appetite. **Friday is worst in both.**

**Caveat: neither study covered sleep content.**

### ✅ Upload 2–3 hours *before* your audience peaks

`fulhar`: *"Upload 2-3 hours before the peak activity shown in your analytics."*
MilX: *"post when your audience is online **so the early window counts**."*

And YouTube's own exception — the one place they *do* say timing matters:

> *"if you're scheduling a **Premiere or going live**, consider your audience's
> active times to maximise engagement."*

**For 24/7 streams and premieres, timing is officially relevant.** For uploads,
it isn't. That distinction matters enormously for this niche, where
`GUIDES.md` §7 says live is a separate growth engine.

### ✅ There *is* a frequency ceiling

AIR (3,000+ channels): overloading viewers produces *diminished returns* —
*"viewers might start skipping your videos because they feel overwhelmed."*
Their line: **"the algorithm rewards long-term engagement patterns, not
short-term posting frequency."**

Gyre: *"any rhythm needs **two months** before it tells you anything."*
Older guides that said "just double your output" have aged badly.

**The thread's cadence instinct is right; its mechanism ("trust score",
"permanent damage") is invented.** You should pace — because *audiences* tire,
not because an algorithm keeps a score.

---

## 4. Sleep-specific timing — where this niche differs

None of the cited studies covered sleep. So derive it from the actual audience.

### When Americans go to bed

[AASM Sleep Prioritization Survey 2024](https://aasm.org/wp-content/uploads/2024/12/sleep-prioritization-survey-2024-bedtime.pdf),
n=2,006 US adults, ±2pp:

- **55% have a set bedtime of 10pm (31%) or 11pm (25%)**
- 21% are at 9pm — so **76% start bed between 9 and 11pm**
- **Baby Boomers (60%) most likely to report 10pm/11pm**
- **People 55–64: 59% at 10pm/11pm** — the exact demo the thread says carries
  the RPM

2019 wave (n=2,003) is stable: 54% between 10–11pm.

### What that means for upload time

The thread's **6pm EST is optimized for general primetime, not for sleep.**
Sleep consumption peaks **9–11pm EST**.

Applying *"upload 2–3 hours before peak"*:

> **Upload ~7–8pm EST.**

Not 6pm (too early, general primetime), not 10pm (too late — the video needs
indexing before the bedtime window opens).

**But hold this loosely.** YouTube says publish time doesn't affect long-term
performance, and — as `CATEGORIES.md` established — **sleep discovery is
search-led and long-tail** (90% of Tier A top-10 results are under 18 months
old; the format's hits are 8 years old). vidIQ's caveat is exactly our case:

> *"This can undoubtedly be true of **search-based content, which needs time to
> establish itself** before momentum starts to kick in."*

**Translation: publish time matters far less here than in browse-driven niches.**
It's a second-order variable we're choosing for consistency, not performance.

---

## 5. The schedule to actually run

| | Setting | Why |
|---|---|---|
| **Cadence** | **1 video / week** (Mon–Thu, prefer **Thursday**) | Thursday replicated across two studies; weekly is inside AIR's sustainable band; `STRATEGY.md` already said slow + irregular |
| **Clock time** | **19:00–20:00 EST**, same every week | Consistency (+40% growth per fulhar), positioned 2–3h before the 9–11pm sleep window |
| **Never** | **Friday** | Worst day in both studies |
| **Day variety** | Vary the *day* month to month; keep the *hour* fixed | Stops cadence signal, keeps consistency signal |
| **Volume gate** | Scale to 2/wk **only if** median views/video holds or rises | The thread's one good rule — but gate on 8 weeks of data, not vibes (Gyre: two months) |
| **Live / premiere** | **This is where timing actually matters** — YouTube says so explicitly. Aim 20:00–22:00 EST | `GUIDES.md` §7; 5 concurrent viewers ≈ 3,600 watch hrs/month |
| **Cold start** | First 2 weeks: **1 video every 5–7 days.** Not 48–72h — see below | |

### On the cold-start claim specifically

The thread says 48–72h in weeks 1–2. The *caution* is defensible (AIR's
audience-fatigue finding), but the **"PERMANENT, not recoverable" framing is
unsupported** — YouTube says growth isn't correlated with time between uploads
and that breaks carry no penalty.

**Run it anyway, for the real reason:** a new channel has no audience model and
no data. Publishing 5 videos in 3 days means you can't attribute *anything* —
you won't know which topic, thumbnail or title worked. **Pace for measurement,
not for a trust score.**

---

## 6. What actually ranks, in order

Everything above is second-order. This is the first-order list:

1. **`fresh_pct` / niche choice** — `CATEGORIES.md`. A closed door beats any
   schedule.
2. **Thumbnail + title** — the 7-day experiment's own #1 stated fix, with
   **81.8 watch hours already banked and €0 earned**
3. **Retention curve** — Gyre's funnel diagnosis: *impressions steady + CTR
   falling = thumbnail* · *CTR steady + AVD falling = content* · *impressions
   falling = distribution narrowed*
4. **Distinctness** — `STRATEGY.md` R1. The only thing that gets you *removed*,
   as opposed to just underperforming
5. **Publish day (Thu)** — real but ~1.5×
6. **Publish hour** — YouTube: **not known to affect long-term performance**

Position 6 is where the thread put its most emphatic claim.

---

## 7. Live competitor data point

Pulled while writing this — **`Relaxing Boring History For Sleep`**,
[Social Blade](https://socialblade.com/youtube/handle/relaxingboringhistoryforsleep):

- Created **2025-10-23** — 11 months old
- **7,320 subs · 1,158,837 views · 79 videos**
- ≈ **7 uploads/month**, 1.16M views from a standing start

That is a **direct competitor in `history to sleep to` — our Phase 1 primary
(`CHANNELS.md` §7)** — operating at roughly the cadence this file recommends,
and it works. It also confirms the category is open *and* being taken: the
door is open **now**, and `fresh_pct` will start decaying as incumbents
establish.

**Which is the real argument for schedule discipline:** not a phantom trust
score, but that someone else is filling the shelf while we deliberate.
