# Sleep Channel — Script DNA

*Testing the "extract structural DNA from top 3 competitor videos" method
against actual top-performing sleep content.*

Compiled 2026-09-26. Raw data: `/tmp/opencode/yt/dna_raw.json`,
`dna_chapters.json`.

> **Method, taken seriously.** The thread's *procedure* is sound and we ran it:
> select outliers by view count (not recency), pull structure, ignore topic.
> What we did **not** assume is that its *findings* transfer — because the
> thread describes a different genre.
>
> Same funnel as `SCHEDULE.md` (`elevate(.)uno` / TubeChef). Its own caveat
> applies: *"he's not gospel, but good probes."*

---

## 1. What we measured

Probed our **Tier A** queries with `order=viewCount`, kept videos **≥30 min**
(sleep format floor), pulled full descriptions and parsed chapter markers.

```
9 Tier A queries → 63 candidates → 29 videos ≥30 min
Median runtime: 169 minutes
Videos with ≥3 parseable chapters: 9 of 29 (31%)
```

**n=9. Treat this as directional, not conclusive.** Flagged again in §6.

---

## 2. The headline number

**Chapter-label sentiment across all parseable chapters:**

| Category | Count | Share |
|---|---|---|
| **Neutral / scene-setting** | **161** | **93%** |
| High-tension (`war, death, crisis, secret, collapse, fall, betray…`) | 7 | **4%** |
| Low/breath (`intro, outro, summary, close…`) | 5 | 2% |

**The thread's whole method rests on identifying *tension type* — crisis vs
mystery vs status disruption. In top-performing sleep content, tension is 4%.**

That single number is the finding.

---

## 3. The three structures that actually repeat

### A. The quarterly divide — 11.8M + 9.5M views

```
"3+ Hours Of WW2 Facts To Fall Asleep To"    205m   0% · 25.1% · 50.1% · 75.0%
"3 Hours Of WW2 Facts To Fall Asleep To"     202m   0% · 24.7% · 49.5% · 74.3%
```

**Two separate videos, both cutting at almost exactly the quarters.** Four
equal movements, no climax, no rising action — just four peer segments of
equal weight. This is the most cleanly reproducible structure in the set, and
it's the one most directly usable.

### B. The uniform enumeration — 5.5M views

```
"Level 1 to 100 Philosophy Concepts to Fall Asleep To"
185m · 100 chapters · 0.0% 1.0% 2.0% 3.0% 4.0% 5.1% 6.3% … 98.4% 99.2%
```

**~1.1% intervals — mathematically uniform.** One hundred peer concepts at
constant spacing. **A structure incapable of a climax.** It's a list, and the
list *is* the format.

### C. The topic ladder — 8.8M views

```
"Graham Hancock: Lost Civilization…"  153m  13 chapters
0 · 1 · 5.7 · 13.5 · 16.8 · 24.3 · 36.3 · 49.7 · 55.8 · 71.6 · 76.4 · 92.1 · 96.9
```

Front-loaded intro, then progressively widening intervals. Discrete topics,
each self-contained — no dependency on the previous one.

Also observed: `soft spoken space facts` (6.9M) at
`0 · 1 · 14.4 · 22.8 · 33.6 · 46.1 · 54.7 · 70.3 · 81.9 · 89.8` — near-even
again.

> **Common denominator: peer units at roughly constant spacing.** Not
> tension and release. Not rising action. Not a climax.

---

## 4. The principle — *"interesting enough to choose; forgiving enough to
drift away from"*

> Owner's formulation, 2026-09-26. **It replaces the framing below, which was
> only half right.**

Two tests, both required:

| Test | What it means | Failure mode |
|---|---|---|
| **Interesting enough to choose** | gives the viewer a *reason to click* out of everything else | nobody opens it |
| **Forgiving enough to drift away from** | losing the thread costs **nothing** | they leave at minute 7 |

**This corrects two things we'd been asserting:**

1. ~~*"facts beat plots"*~~ — **not proven.** `LEADS.md` §1's examples mix
   both (Oliver's history, Jung's feelings, Bub's calculus) and all perform.
2. ~~*"difficulty induces sleep"*~~ — **not proven either.** Nothing in the
   data isolates difficulty as the sleep agent.

**What the examples actually share:** listeners pick content they can **stop
following without feeling they missed something important.**

That's a better lens than "absence of anticipation" (which wrongly implies
*boring*). The content must be **good enough to open** and **loose enough to
drop.** A plot that punishes inattention fails test 2. A fact list that never
earns a click fails test 1.

**Every skeleton in §3 passes both:** quarterly (four independent movements),
enumeration (each unit self-contained), ladder (topics don't depend on each
other). **That's *why* those three shapes dominate — not because sleep hates
plot, but because sleep can't afford dependency.**

---

## 5. Why the thread's model inverts for sleep

The thread describes **story-driven watch-time content** — true crime,
military history, romance. Retention there comes from **wanting to know what
happens next.**

Sleep content retention comes from **not wanting to know.**

| | Story content | Sleep content |
|---|---|---|
| Retention driver | Anticipation — pull forward | **Absence of anticipation** — no reason to leave, no reason to engage |
| Viewer's goal | See the payoff | **Stop caring** |
| Pacing shape | Tension ↑ / breath ↓ oscillation | **Flat** — neutrality is the product |
| Climax | Required. Too early = dead tail; too late = drop-off | **Absent.** A climax at minute 15 of a 169-min video is 90% epilogue by the thread's own logic |
| Chapter labels | Beats | **Topics** |

**Every sleep guide in `GUIDES.md` already says this**, in different words:

- fluxnote: *"avoid drama, rapid plot changes, and emotional provocation"*
- autotube: *"calm, predictable, low stakes... no sudden cuts"*
- sleeptale: story generator *"avoids excitement, drama, or narrative tension
  **by design**"*

**The thread would have us inject tension into a product whose entire value
proposition is its absence.** That's the "similar" failure mode it warns about,
applied one level up.

---

## 6. What *does* transfer

The method survives; the mechanism doesn't.

| From the thread | Verdict | Adapted for sleep |
|---|---|---|
| **Select top 3 by views, not recency** | ✅ sound | Unchanged. Outliers carry the signal |
| **Ignore topic, read structure** | ✅ sound | Unchanged |
| **Tension type (crisis/mystery/status)** | ❌ wrong genre | **Replace with *unit type*** — is it a story, a list, a concept ladder, a place tour? |
| **Tension/breath oscillation** | ❌ wrong genre | **Replace with *constant cadence***. The breath is structural neutrality, not relief |
| **Climax placement (15–18m / 28–35m)** | ❌ would hurt | **Delete.** Sleep structures in §3 have no climax and shouldn't |
| **Same skeleton, different content** | ✅ **sound, and already ours** | This is exactly `STRATEGY.md` R1 and powvid's `facts.md` + `scenes.yaml` pair |
| **DNA lives in the script, not the edit** | ✅ sound | Unchanged — matches powvid's no-LLM-in-render-path rule |

### The three sleep skeletons, extracted

```json
{
  "channel_dna": {
    "unit_type": "quarterly | enumeration | ladder",
    "hook_type": "topic_announce | soft_open | none",
    "climax": null,
    "cadence": "constant",
    "peer_units": "self_contained",
    "tension_budget": 0,
    "segment_map": {
      "quarterly":    [0, 25, 50, 75],
      "enumeration":  "uniform, ~N equal units across 100%",
      "ladder":       "dense 0-25%, widening 25-100%"
    },
    "invariants": [
      "no rising action",
      "no cliffhanger between units",
      "each unit survives being skipped",
      "closing = quiet, no summary, no call to action"
    ]
  }
}
```

`climax: null` is not a placeholder. It is the load-bearing field.

---

## 7. Caveats — stated before this is used

1. **n=9 with ≥3 chapters, from 29 videos.** Chapter markers are optional; 69%
   of sleep uploaders don't use them. We are reading the structure of the
   *organized* minority.
2. **Chapters describe intent, not retention.** Real structural DNA needs
   YouTube Studio retention curves, which require channel ownership. This file
   infers structure from metadata — a proxy.
3. **`order=viewCount` biases old.** Outliers by definition are survivors;
   we're reading what aged well, which may not be what's working *now*. Partially
   offset by `CATEGORIES.md`'s `fresh_pct`, which showed Tier A still turning over.
4. **Two of the top three hits were the same channel** (the WW2 pair). The
   quarterly pattern may be one creator's idiosyncrasy, not a genre norm.
5. **The thread's climax timings are unsourced** and precise in the way funnel
   copy usually is.

---

## 8. What to do

**1. Pick a skeleton per channel, not per video.**
`history to sleep to` → **quarterly** (the WW2 pattern, 21M views combined).
`stoicism / theology / philosophy` → **enumeration** (the 100-chapter pattern,
5.5M views, and a natural fit for "one idea per minute").
`alchemy / esoteric` → **ladder** (discrete texts, self-contained).

**2. Extract per channel before writing, using their real procedure.**
Top 3 by views → read the chapter map → pick the skeleton. ~10 minutes,
one API call set. Do it for each new channel in `CHANNELS.md` §7 Phase 1.

**3. Do not port the climax.** `climax: null` stays null.

**4. Wire it into what already exists.** powvid's `scenes.yaml` *is* the
skeleton; `facts.md` is the content. The skeleton was always supposed to be
reused and the facts always supposed to vary — which is precisely the thread's
point and precisely `STRATEGY.md` R1. **No new machinery required**; add the
`unit_type` and `segment_map` fields and the lint gate can enforce spacing.

**5. Measure what this can't.** The gap in this file is retention curves. First
channel's first 10 uploads should be read against Studio's "typical retention"
(YT benchmarks each video against your own last 10 of similar length) — that's
where real DNA lives, and it's the one input no public API gives us.
