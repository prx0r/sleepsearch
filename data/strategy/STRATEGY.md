# Sleep Channel — Strategy

*How to build at volume without building the thing YouTube is deleting.*

---

## The contradiction, stated plainly

The request is a **farm**. The policy (see `RESEARCH.md` §2) removes
**content farming** from YPP, and Halprin says so by name.

So the question is not *"can we automate"* — it's *"where is the line between
a production pipeline and a content farm?"* YouTube answered that for us in
its own detection signals (`RESEARCH.md` §3). Design against them explicitly.

> **Working definition:** a *pipeline* produces many **distinct works**. A
> *farm* produces many **copies of one work**. The machine is not the problem.
> The sameness is.

---

## The design rules

### R1 — Variation is structural, not cosmetic

Swapping nouns in a title template is exactly the flagged pattern
(`"Lofi Mix #47"`). Variation has to live in the *substance*:

| Sameness (flagged) | Distinctness (defensible) |
|---|---|
| Same loop, different filter | Different sound source, scene, and structure per upload |
| `Forest Rain #1..#30` | Each video a specific, nameable place *and* situation |
| Same thumbnail, hue-shifted | Distinct composition per upload |
| Same 10h loop stretched | Varying runtime: 90m / 2h / 3h / 8h as fits the piece |

**Gate:** every upload must pass *"would a human listener consider this a
distinct piece of content?"* If no, it doesn't ship. This is YouTube's own
test — borrow it as ours.

### R2 — Narration is the moat and the money

Ambient-only loops are the most automated, lowest RPM (`$8–10`), and sit
directly in the flagged category. Narrated sleep stories are **`$10–15`** and
are *inherently* not a template — a story is a story.

**Decision: lead with narrated content.** Ambient becomes the low-effort
back-catalog tier, not the product.

This also reuses what we already have: powvid's script discipline, fact lint,
and TTS voice work transfer almost directly.

### R3 — Original visual per upload, no exceptions

OutlierKit's checklist: *"Stock loops paired with stock AI music is the
fastest path to demonetization."*

Every video gets a **generated or commissioned scene**, not a reused loop.
Cost is near zero (Flux/SDXL or a still-image slow-pan) and it is the single
cheapest policy insurance available.

### R4 — Disclose synthetic audio

Toggle **Altered or synthetic content** in YouTube Studio on every AI-voice
or AI-music video. Non-disclosure is an explicit policy violation — this is
free compliance, and skipping it is indefensible.

### R5 — Human judgment on the publish step, always

Every tool surveyed in `../synthetic/TOOLS.md` and every policy source converge:
**a person decides what ships.** Not a scheduler.

Our version — borrowed from powvid, which already runs this pattern:

```
generate → lint (fail-closed) → human approves → render → upload
```

powvid's `lint_script()` refusing any digit not in `facts.md` is the same
shape as what this needs: **an automated step that can say no, plus a human
step that must say yes.**

### R6 — Diversify before it matters

AdSense is one leg. Sleep audiences support:

- **Memberships** — ad-free cuts, extended versions, downloadable audio
- **Affiliates** — pillows, mattresses, sleep masks, white-noise machines
  (soft, description-level CTAs; never in the video)
- **Own digital product** — offline audio bundles
- **YouTube Premium watch time** — long-form ambient is disproportionately
  Premium minutes, which pay without any ad serving at all

A channel with no mid-rolls (the `NO ADS` positioning) is still viable *if*
it's on Premium share. Don't treat ad RPM as the only revenue line.

---

## The channel architecture

**One channel, multiple content pillars — not many identical channels.**

Running ten copy-paste channels is the highest-risk structure possible: the
policy is assessed **per channel**, and ten thin channels gives ten chances to
fail rather than one diversified one.

```
CHANNEL
├── Pillar A — Narrated sleep stories (2h, chaptered)      ← primary, $10–15
├── Pillar B — Placed-based ambient with a written intro   ← $8–10, differentiated
├── Pillar C — Seasonal / topical one-offs                 ← breaks cadence signals
└── Shorts — 30–45s hooks cut from A                       ← discovery only, not revenue
```

**Cadence:** slow and irregular. `RESEARCH.md` §3 flags *"upload rate abnormally
high relative to channel age."* Target **2/week at launch, tapering to 1/week**
once the catalog passes 30, with deliberate gaps. Volume is a later problem.

**Length ladder:** ship some at 90m, some at 2h, some at 8h. Uniform runtime
(`all exactly 3:08:09`, as one live competitor does) is a detection signal.

---

## What we will NOT do

- **No raw Suno/Udio dumps.** Dead niche at `$0.30–1`, and squarely flagged.
- **No 60-second-loop-repeated-60-times runtime inflation.** YouTube now reads
  that as **reused content**, not long-form.
- **No identical-template channel fleet.** See above.
- **No kids content left unmarked** as Kids — COPPA. (The `$45k in 30 days`
  video's own comment section caught this one.)
- **No fake testimonials or health claims.** *"Cures insomnia"* makes this
  medical-adjacent, and health is on the sensitive-topics list for AI personas.
  Language stays "for sleep / to relax / to focus." Channel carries a
  liability disclaimer — every established competitor has one.
- **No copyrighted audio.** Content ID on a 10-hour video is worse than a
  slow start. Sources: own synthesis, CC0, or paid-license only.

---

## How we'll know it's working

**Do not read view count first.** Ranked by what actually predicts survival:

| # | Metric | Why |
|---|---|---|
| 1 | **YPP application accepted** | The whole gate. Everything else is downstream |
| 2 | **Avg view duration ÷ runtime** | The flagged "runtime vs watch" signal — low is a warning, not just a loss |
| 3 | **Retention graph shape** | Tells us where mid-rolls hurt (§4 of RESEARCH) |
| 4 | **CTR on thumbnail** | Verifies R3 (original visuals) are actually distinct |
| 5 | **RPM by pillar** | Confirms narration premium is real for *our* audience |
| 6 | **Views** | Last, not first |

**Explicit kill criteria:** if the YPP application is rejected for
inauthentic content, **stop publishing to that channel** and diagnose against
`RESEARCH.md` §3 before adding a single video. Do not upload more and hope.

---

## Open questions

1. **Mid-rolls on or off?** `RESEARCH.md` §4 documents both strategies live
   in the niche. Plan: A/B a spaced-midroll cut against a no-midroll cut of
   the same story, judge on retention + revenue per viewer, not views.
2. **Does 150wpm narration suit sleep?** The cited sleep pace is **0.7–0.9×**.
   powvid runs normal rate for shorts. This is a *different* TTS setting, not
   a different pipeline.
3. **How much does the baby-sleep vertical out-earn general sleep?** The
   reported numbers ($2.8–4.5K/mo on one channel) are second-hand. Worth one
   probe channel before committing.
4. **Geography.** TubeTube's data says geo is worth ~20×. Do we publish in
   EN only, or run language variants? **Hold this until the EN channel
   proves out** — language variants are exactly the fleet pattern we're avoiding.
