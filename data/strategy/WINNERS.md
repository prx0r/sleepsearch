# Sleep Channel — The Winners

*Synthesis. Everything above this line was research; this is the decision.*

2026-09-26. Sixteen files, 4,194 lines, ~110 API queries, live autocomplete,
a running analysis engine, and six owner-supplied competitor examples —
collapsed to five formats and one first episode.

**Selection criteria** (each drawn from a different file):

| # | Criterion | From |
|---|---|---|
| 1 | **Leave-it-on** — people just leave it running | owner, `RPM.md` §2 (6 min = **$2.68**, 49 min = **$18.00**) |
| 2 | **Interesting to choose · forgiving to drift** | owner, `DNA.md` §4 |
| 3 | **Structural variation** — different *place/piece/unit*, not different adjectives | `STRATEGY.md` R1 |
| 4 | **Rights clean** — write it, analyse it, or use PD. Never recite | `CHANNELS.md` §3 |
| 5 | **Demand proven** — API, autocomplete, or a named competitor | `CATEGORIES.md` |
| 6 | **Buildable with what's on the box** | `PIPELINE.md`, `TEMPLATES.md` §3 |

---

## 🥇 1 · Rain in weird places

**The owner's format, and the strongest overall.**

> *rain in a weird place — add ambience — doesn't need to be sleep — people
> just leave it on*

| Criterion | |
|---|---|
| Leave-it-on | ✅✅ maximal — nothing interrupts |
| Drift | ✅✅ no plot at all |
| Variation | ✅ **rain constant, place variable** — one engine, N locations |
| Rights | ✅✅ **assembled, therefore ours** |
| Demand | ✅✅ **autocomplete:** `rain in a tent / car / cave / cabin / tin roof` |
| Buildable | ✅ scene + loop + numpy rain |

**Widens beyond sleep** to study / work / focus — which Bub Explains' commenters already are (`LEADS.md` §1).

**Shortlist** (`SCENARIOS.md` §10): tent · cave mouth · ship's cabin · **bunker** · lighthouse · sleeper train · observatory · greenhouse · capsule hotel · Victorian kitchen.

---

## 🥈 2 · Classical / piano breakdowns

**The only one where the engine already runs.**

| Criterion | |
|---|---|
| Leave-it-on | ✅✅ |
| Drift | ✅ enumeration skeleton — one piece, one reading |
| Variation | ✅✅ every piece is different music |
| Rights | ✅✅ **PD corpus + our narration** — zero licences |
| Demand | 🟡 unprobed; but Bub's *calculus 1.98M* proves "explained gently" works |
| **Buildable** | ✅✅ **`music_engine.py` proven this session** |

```
3,194 bundled PD pieces · music21 10.5.0 · fluidsynth + 148MB soundfont
→ key confidence, Roman-numeral harmony, dynamic arc → MIDI → 82.8s WAV
```

**Format:** piece **+** lore **+** theory, narrated over the piece itself.
**"Sleep album breakdowns" narrowed correctly:** PD classical 🟢 · pop without
audio 🟡 · pop with audio 🔴.

**Gap:** Satie/Debussy not bundled — pull from IMSLP/Mutopia (both PD).
**Bundled and ready: 10 John Field nocturnes** — *the inventor of the genre.*

---

## 🥉 3 · Scenario narratives — *"fall asleep here"*

**Highest measured velocity in any example we hold.**

| | Views/**day** | Age |
|---|---:|---:|
| **Edwardian: Night Train to Edinburgh** | **3,678** | 78d |
| Marauder's Map | 1,543 | 13d |
| Space Marines (rate) | 335 | 939d |
| Pokémon (biggest franchise) | **180** | 12d |

> **Era + place + journey beats franchise size by 20×.** `SCENARIOS.md` §5b.

| Criterion | |
|---|---|
| Demand | ✅✅ best rate in the set **and** autocomplete (`sleep in a castle/spaceship`, `fall asleep in ancient egypt`) |
| Rights | ✅✅ **we write the room** — first format with no rights thread at all |
| Variation | ✅✅ every scenario a different place/era |
| Buildable | ✅ writing + music engine — **no new tooling** |

⚠️ **Title grammar:** use `sleep in a ___` or `[place] ambience`. **Not**
`fall asleep in ___` — that stem is owned by *"fall asleep in 3 minutes."*
(`SCENARIOS.md` §3)

---

## 4 · Cozy everyday history

**Our own Phase 1 primary, independently confirmed.**

`history to sleep to` = **200,308 / 100% fresh / 142 min** (`CATEGORIES.md`)
· **Oliver's *ordinary 1700s home* = 518,000** vs his abstract *medieval
marriage* = **505** — a **933× spread** (`LEADS.md` §1) · WW2-facts sleep
videos at **11.8M and 9.5M**, four years old, still ranking (`DNA.md` §3A).

**Rights:** PD historical material, analysed not recited.
**Live competitor:** `Relaxing Boring History For Sleep` — 1.16M views in
11 months (`SCHEDULE.md` §7).

---

## 5 · Advanced maths & hard papers

**Zero rights risk of anything proposed.**

`quantum physics to sleep to` = **166,138 / 100% fresh / 161 min** · Bub's
**calculus 1.98M, algebra 1.43M — both within 68 days of launch** ·
`/root/synthetic` already holds `PAPERS.md`, `READING.md`, `FEEDS.md`
(171 items / 18 sources).

Maths isn't copyrightable as expression. **Serves sleepers *and* the
intimidated-studier.**

---

## ❌ Not winners — and why

| Idea | Reason |
|---|---|
| **Film / movie lore** | worst RPM band (**$0.50–3**), film studios more litigious than game, demand **unprobed** — only a *game*-lore proxy |
| **French theory** (Lacan · Deleuze · Baudrillard) | rights fine **for discussion** (corrected §7e) — but not the owner's current preference, and **analysis needs writing** |
| **Steiner · Dolores Canon · Tantrāloka recitation** | 🔴 **reproduction** of modern translations — the use is the test |
| **Pure ambient with no place variation** | lowest band **and** highest template exposure (`RESEARCH.md` §3) |
| **25-channel fleet** | attention is the fixed cost; *"the work of managing $15/day is identical to $1,000/day"* (`FACTCHECK.md` FC-5) |
| **Binaural / "40Hz focus" claims** | drifts into cognition claims → sensitive topics |

---

## 🚀 The first episode — buildable TODAY, zero credentials

**Rain in a lighthouse, with a John Field nocturne.**

It composes winners 1, 2 and 3 into one asset, and **every component is
verified present:**

| Layer | Component | Status |
|---|---|---|
| **Visual** | procedural dark backdrop, slow drift — **Pillow** | ✅ installed |
| **Rain** | numpy synthesis → **ffmpeg** | ✅ installed |
| **Score** | **John Field nocturne** from bundled corpus (10 pieces) | ✅ in `music21` |
| **Analysis** | `music_engine.py` → key confidence, harmony, dynamics | ✅ **run this session** |
| **Bed render** | **fluidsynth** + FluidR3_GM 148 MB | ✅ installed this session |
| **Narration** | **edge_tts** — free, no key, no rate limit | ✅ installed |
| **Script** | written by us, ~400 words | 🟡 *the only work left* |
| **Encode** | ffmpeg | ✅ installed |

```bash
python3 scripts/music_engine.py --render     # ✅ already works
```

**Blocked by nothing.** No `CF_API_TOKEN`, no YouTube OAuth, no quota.

> **Wave 0 (`ORGANISE.md` §9) is this one file.** If it renders, the pipeline
> exists. If it doesn't, no amount of channel-making fixes it —
> **the cheapest possible failure is a render, not a channel.**

---

## Sequencing

```
WAVE 0   render "lighthouse + Field" end to end          ← TODAY
WAVE 1   5 more rain-in-a-place episodes (assemble, not write)
WAVE 2   one scenario narrative, written — trains the writing path
WAVE 3   channel exists → first upload → readback receipt   [human gate]
WAVE 4   second channel only when #1's per-video performance holds
```

**Then, and only then:** history (winner 4) or maths (winner 5) as the
second channel — **not** the other three.

**One dashboard. One queue. Human confirms every send.**
(`ORGANISE.md` §7)
