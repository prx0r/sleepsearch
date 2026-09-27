# Sleep Channel — How the Farm Is Organised

*Applying `/root/influence`'s architecture to a 25-channel sleep network.*

Compiled 2026-09-26. Companion to `CHANNELS.md` (which channels) and
`STRATEGY.md` (why it's not a slop farm). **This file is the wiring.**

> The channel *list* is being written in parallel at
> `powvid/docs/SLEEP_CHANNELS.md`. This file does not duplicate it — it defines
> the structure that list hangs on. If a channel appears here it's an example,
> not the roster.

---

## 1. The one idea worth stealing from `influence`

> **"An identity is not a primitive: it is what a resolved function chain
> terminates at. No chain, no identity."**
> — `influence/dependency-graph.md`

Translated: **a channel is not a thing we build. A channel is what one shared
pipeline resolves to when you vary five fields.**

```
THE CHAIN (shared, written once)
  read source → draft → fact-lint → render → approve → upload → readback
       │                                                        │
       └──────────── varies per channel ───────────────────────┘
              accent · corpus · skeleton · voice · audience
```

**This is the structural answer to "it's not a bot farm."** A bot farm builds
25 pipelines. We build **one** and resolve it 25 times with different
parameters. The *outputs* differ because the *inputs* differ — not because a
template got its nouns swapped.

Which is exactly the distinction `STRATEGY.md` draws, now with a mechanism.

---

## 2. The layer map

Direct translation of influence's L0–L7 into this domain:

| Layer | Influence | **Sleep** | Gate |
|---|---|---|---|
| **L0** | law: receipts, gates, journal | **`facts.md` + `lint_script()` + `runs/<id>/manifest.json`** — powvid already has this | none (pure) |
| **L1** | observe (read-only) | source intake · RSS/arXiv sweep · **`CATEGORIES` fresh_pct re-probe** | read-only |
| **L2** | acquire | **channel creation** · handle · brand assets · OAuth | 🔒 **human** |
| **L3** | make | script → TTS → ambient → render → MP4 | none |
| **L4** | send | **upload** · schedule · first comment | 🔒 **human** |
| **L5** | judge (Choice/Score/Noul) | skeleton pick · distinctness · rights · publish-ready | never executes |
| **L6** | learn | retention reweight · skeleton selection | proposes only |
| **L7** | endpoints | **CHANNEL** | a resolution, never an input |

Influence's binding rules carry over unchanged:

- **Edges point down-to-up** — a layer may only depend on lower layers
- **L2 and L4 always carry a human gate plus a grant**
- **L5 never executes anything. L6 proposes, never promotes — promotion is a receipt**
- **L7 nodes are resolutions, never inputs**

Read the last one against our own roster: **a channel can never be an input to
its own pipeline.** The moment "because it's the Corbin channel" starts
overriding the fact gate, we're a farm with better fonts.

---

## 3. `simulate` vs `embody` — the split that matters most

Influence's sharpest distinction:

> `simulate(freak)` = L3 + L5 + L6 + corpus. **No socials, no money, no humans.**
> `embody(freak)` = `simulate` + L1 + L2 + L4. **The moat is exactly this layer —
> accumulated claimed identities with verified histories.**

For us:

| | `simulate` | `embody` |
|---|---|---|
| What | write → lint → render MP4 | channel exists, branded, uploaded, read back |
| Cost | ~zero (compute only) | OAuth, brand assets, **reputation accrues over weeks** |
| Parallelism | **run all 25 at once, freely** | **one at a time** |
| Failure mode | wasted render | ⚠️ fleet pattern, `CHANNELS.md` §5 |

> ### 🔑 Operating rule
> **Simulate wide. Embody narrow.**
>
> You may render all 25 channels' back-catalogue tonight. You may **not** stand
> up 25 YouTube channels this week — that is precisely the "batch of new
> accounts, similar videos in the same time window" pattern that
> `CHANNELS.md` §6 identifies as the linkage signal.

**Sequence:** simulate a channel to ≥3 lint-passing scripts and 1 rendered MP4
*before* it's allowed to become real. Nothing gets a handle it hasn't earned.

---

## 4. One product schema, applied to a channel

Influence fits every product to one schema (`products/product-schemas.md`).
Do the same — every channel is this shape, filled in:

```yaml
channel: <NAME>
intent:        the channel in one line
in  → out:     source corpus → episodes
passport:      intake → script → lint → render → approve → upload → readback
connectors:
  have:        [facts.md pattern, scenes.yaml, lint, render, 6 voices]
  need:        [YouTube OAuth, thumbnail generator, Studio readback]
judges:        skeleton(Choice) · rights(Choice) · distinctness(Noul)
               publish_ready(Noul) · retention(Score)
lens:          one dashboard tab, not one dashboard
qp:            human confirms every upload; delivery settles on readback only
accent:        #HEX
skeleton:      quarterly | enumeration | ladder
```

**Enforce the schema mechanically.** A channel directory that's missing a
field isn't "in progress" — it's *not a channel yet*. Same discipline as
influence's `gates_live` vs `gates_future`: **named so promotion arrives as a
new gate id, never an edit.**

### Graduation — `designed → partial → live`, receipt by receipt

| State | Definition of done |
|---|---|
| **designed** | accent + corpus + skeleton chosen · **10 episode titles listed in ≤20 min** (the `facelessos` narrowing test, `GUIDES.md` §3.4) |
| **partial** | ≥3 scripts lint-passing · ≥1 MP4 rendered · thumbnail made |
| **live** | channel exists · first upload published · **readback receipt** |

> **Promotion is a receipt or it didn't happen.** Docs, optimisers and judges
> never promote by themselves.

Track it in one table — this *is* the roster, one row per channel:

```markdown
| # | Channel | Accent | Skeleton | Titles | Lint | MP4 | Live | Readback |
|---|---------|--------|----------|--------|------|-----|------|----------|
```

---

## 5. Judges — written Jev-style

powvid already ships `jev.py` (generator never judges; humans judge on
`outputs.moltwork.com`). Same contract, five judges:

| Judge | Type | Question |
|---|---|---|
| `skeleton` | **Choice** | quarterly · enumeration · ladder — *for this channel* |
| `rights` | **Choice** | `PD_CLEAN` · `TRANSFORMATIVE_SUMMARY` · **`RED`** |
| `distinctness` | **Noul** | runtime within 1% of a prior upload? thumbnail perceptually near-duplicate? `#NN` in title? |
| `publish_ready` | **Noul** | lint PASS **and** human approved **and** rights ≠ RED |
| `retention` | **Score** | from Studio readback — *never* self-reported |

**Two rules imported verbatim from influence:**

- **Delivery claims settle on readback only, never on attempt.** "Uploaded" is
  an attempt. *"Published and playable at URL X, verified"* is a settlement.
- **Actuality is TRUE / FALSE / UNKNOWN**, false dominating unknown dominating
  true — so a timeout never becomes a false success. (Our `snapshot.py`
  already fails only when >50% of sources fail; same spirit.)

---

## 6. THREADS — machine vs human, the `influence/THREADS.md` shape

### 🤖 Machine (runs unattended)

| Pri | Thread | Definition of done |
|---|---|---|
| A1 | **Source intake sweep** | feeds fresh, 0 errors (existing `snapshot.py`) |
| A2 | **`fresh_pct` re-probe** | monthly: re-run `CATEGORIES` probes; **alert when a niche drops below 60%** — the door is closing |
| A3 | **Script gen + lint** | batch → gate; failures parked, never auto-relaxed |
| A4 | **Render queue** | MP4 + manifest receipt per episode |
| A5 | **Readback poll** | views/retention pulled → `retention` Score written back |
| A6 | **Threshold alarm** | YPP hours tracked against **8,000 (from 2027-02-01)**, not 4,000 |

### 🧑 Human (keys, clicks, confirm — each 2–15 min)

| Pri | Thread | Action | Unblocks |
|---|---|---|---|
| H1 | **YouTube OAuth** | one Brand Account, channels created under it | everything L2 |
| H2 | **Brand assets per channel** | logo + banner in accent, approved | `partial → live` |
| H3 | **Publish confirm** | every upload, no exceptions | L4 |
| H4 | **`CF_API_TOKEN`** | scenes (blocks both this and powvid) | original visuals |

### 📋 Standing

- **`powvid/docs/SLEEP_CHANNELS.md`** — owned by the other box; this file is its
  frame, not its content.
- **Rights review per channel before first upload** (`CHANNELS.md` §3) — human,
  always.

---

## 7. One dashboard, lenses — not 25

Influence's rule, verbatim:

> *"One shell with lenses over the same queue rather than forks that drift...
> **same task IDs everywhere.**"*

So: **one ops view, five lenses.** Not twenty-five.

| Lens | Shows |
|---|---|
| **Production** | intake → script → lint → render queue, per channel |
| **Channels** | the graduation table (§4), one row each |
| **Publish** | drafts awaiting H3 confirm · readback receipts |
| **Rights** | `rights` judge output; anything `RED` is a blocker, not a warning |
| **Money** | YPP hours vs 8,000 · RPM by pillar · second legs |

Every row carries the **same task ID** across all five. That's what stops the
fork-and-drift that kills multi-channel ops.

---

## 8. The rules that keep it beautiful instead of automated

Carried from `influence/AGENTS.md` + our own `STRATEGY.md`:

1. **Additive only.** Never rename a channel's accent, skeleton or corpus once
   live — add a new channel instead. Drift is what makes a network look
   manufactured.
2. **Drafts everywhere; publish needs explicit human confirm.** No exceptions,
   any autonomy level.
3. **Secrets in vault/env, never in tree.** Secret-scan before every push:
   `grep -rIlE "cf[a]t_|gh[p]_|sk-[A-Za-z0-9]{10,}" --exclude-dir=node_modules .`
   *(character classes written so the scan pattern does not self-match when the
   pattern itself is committed — a real footgun once a doc quotes its own grep)*
4. **Actuality over booleans.** UNKNOWN ≠ FALSE ≠ TRUE.
5. **Attempt is not observation.** Upload ≠ published.
6. **Promotion is a receipt.**
7. **Keep the queue human-sized** — batch to a morning review, never realtime.
   Alert fatigue is a correctness bug.
8. **One kernel, two consumers** — the skeleton definition lives in one file
   and drives both the renderer and the dashboard. Copy, never fork.

---

## 9. Sequencing — where organisation meets reality

Influence graduates products **receipt by receipt, one lens at a time.**
Same here:

```
WAVE 0   Simulate ONE channel end to end.
         proves: lint → render → MP4 → manifest.  No YouTube yet.
              ↓
WAVE 1   Embody TWO channels.  (flagships per CHANNELS.md §7)
         proves: OAuth, brand assets, publish gate, readback receipt.
              ↓
WAVE 2   Simulate the remaining roster to `partial` — back-catalogue built
         while only two channels are live.
              ↓
WAVE 3   Embody at ≤1/week, gated on per-video performance holding
         (SCHEDULE.md §5) and `fresh_pct` still ≥60% (CATEGORIES).
              ↓
ALWAYS   One dashboard. One queue. Same task IDs. Human confirms every send.
```

**Wave 0 is the entire near-term task and it needs no credentials.**
`TEMPLATES.md` §3 already identified it: clone `sleep-learning-engine`,
render one 30-minute video end to end. That's `simulate(channel)` proven.

Everything above is organisation for something that has **not yet produced a
single frame.** Wave 0 first.
