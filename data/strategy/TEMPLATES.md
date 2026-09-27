# Sleep Channel — Templates

*Off-the-shelf code for this exact pipeline, plus the monetisation mechanism.*

Compiled 2026-09-26. Stars/licenses from the GitHub API. X/Twitter searched and
came back empty — see §4.

---

## 1. The monetisation secret

The intuition — *"someone falls asleep to it"* — is the **mechanism**, not the
secret. The chain is:

```
watch time  →  ad impressions  →  money
```

Sleep content **breaks the middle link**, because you cannot interrupt sleep.
That single fact inverts the economics of everything else on YouTube:

### Inversion 1 — you rent background, you don't sell attention

Attention content must earn every second or lose the viewer. Sleep content gets
seconds for free. **A viewer who stays 8 hours hands you 48× the watch time of
a 10-minute viewer, and your marginal cost to produce it is zero** — the video
already exists. Nothing else on the platform has that shape.

### Inversion 2 — but watch time ≠ revenue

Because you can't interrupt, you give up mid-roll inventory (SemideCoco:
*"only in the beginning. Never in the middle and never at the end"*). So the
money has to come from four places the obvious read misses:

| Lever | Evidence |
|---|---|
| **Front-loaded ads** | SemideCoco — accepts lower revenue deliberately |
| **Catalog compounding** | Calming Tones: 11M views, **8 years old**, still earning. Sleep Stories: 13 years, 537 videos |
| **Nightly repeat** | Same viewer, same video, months at a time. **Zero re-acquisition cost per impression** |
| **Second legs** | SemideCoco Patreon **$654/mo from 218 patrons** · Mind Amend **sells MP3s** off a 20.9M-view track · memberships · affiliates |
| **YouTube Premium share** | Long ambient is disproportionately Premium minutes — pays **without any ad serving**, which sidesteps the no-midroll cap entirely. Under-discussed in every guide in `GUIDES.md` |

### Inversion 3 — the format is commoditised, so the *topic* is the moat

This is the actionable one, from [Medium's "The Money Guide," Dec 2025](https://medium.com/the-money-guide/people-are-making-10k-on-youtube-with-sleep-videos-heres-how-the-system-actually-works-13f4dc87ec00):

> **Avoid:** rain sounds · ocean waves · meditation · generic sleep stories ·
> "sleep to this history" *(flooded)*
>
> **Instead:** Psychology to Sleep To · Deep Sea Lore · Forgotten Religions ·
> Mythology Sleep Narratives · Video Game Lore to Sleep To · Phobias Explained
> Slowly · Ancient Civilizations Sleep Study
>
> **"Search `___ to sleep to` on YouTube and see what autofills. That's your
> niche."**

That autofill trick is the best single tactic found in the whole search. It is
also a direct restatement of `STRATEGY.md` R1 — variation must be **structural**
(the subject), not cosmetic (the adjectives).

### The honest counter — same article

> "Why it dies: very saturated · niche burns out quickly · most channels peak
> then drop · not sustainable long-term · requires speed + volume.
> **Think of this niche as a cash wave, not a career.**"

**Reconciliation:** the *format* is a cash wave (commoditised, everyone has it).
The *catalog* is a career (compounds for 8–13 years — see §2.1 of
`RESEARCH.md`). Ride the wave, but only ship things that compound. That is
exactly the distinction `STRATEGY.md` draws between a pipeline and a farm.

### What it does NOT come from

More hours. More uploads. Longer videos. The 7-day experiment shipped six
2–3-hour videos and earned **€0** — the hours were already there (81.8 of
them); the **thumbnail** was the stated failure and the stated #1 fix. Hours
get you *eligible*. Topic, thumbnail and distinctness get you *paid*.

---

## 2. GitHub templates

### ⭐ `fernandojjq/sleep-learning-engine` — **this is the one**

★★ **2 stars** · **MIT** · **87 commits** · Python 3.11+ · uv

> *"Turn a short topic into a multi-hour, sleep-friendly learning video.
> Generates calm narration, mixes in a soft ambient bed, paints a frame-accurate
> progress bar, and writes a clean MP4 ready for YouTube... **Zero platform
> lock-in, runs free or fully local.**"*

**This is `PIPELINE.md` already built.** What it has that we'd otherwise write:

| Feature | Note |
|---|---|
| **Provider-agnostic LLM** | Default **NVIDIA NIM free tier (DeepSeek V4, 40 RPM, no cost)**. Also OpenAI / Anthropic / Ollama / LM Studio / any OpenAI-compatible URL |
| **Edge-TTS by default** | **No key, no rate limit, no quota.** First render works with zero credentials |
| **Sidechain ducking** | Ambient bed **ducks automatically when the voice is active** — this is dev.to's 35% mix, automated |
| **14 procedural ambient tracks** bundled, synthesised locally | Plus a scanner that keyword-matches rain/ocean/alpha/lofi/fire/brown to the script |
| **Sleep-optimised defaults** | Voice **slowed −5%**, low-light procedural backdrop, progress bar confined to bottom 6px |
| **Frame-accurate progress bar** | Translucent player card, channel avatar, elapsed/total `HH:MM:SS` — this is the *visual identity* layer for free |
| **Hardware auto-detect** | NVENC → QuickSync → AMF → libx264 |
| **Cloud render notebooks** | **Colab T4 free** (12.7 GB RAM + NVENC) — 1080p in 1–2 min |
| **CLI for headless batch** | `run.py render --topic "..." --output-stem ...` emits one-line JSON, "easy to wire into CI" |
| **Real engineering** | pytest (15 tests incl. full end-to-end mini-render), ruff, mypy, tenacity retry, pydantic settings |

**Performance:** first render ~30s · 30-min narration ≈ **4 min on NVENC**,
10–15 min libx264 @720p.

**Its own stated RAM warning** (relevant to our 96%-full disk):
> *"Bad fit: 8 GB Windows laptops with Chrome open. The render OOMs at 1080p...
> the `geq` progress bar filter holds ~150 MB of pixel buffers regardless of
> resolution."*

**What it lacks — and why we don't just fork it:** no fact gate, no provenance,
no human-publish gate, no SEO/metadata stage, no distinctness check.
`STRATEGY.md` R1/R5 still have to be built *around* it. **Take the render
engine, keep our guardrails.**

**Not verified:** has not been run here. No claim that it works.

### `sanyabeast/sleeptale` (SleepTeller)

**0 stars** · **MIT** · 46 commits · Windows-leaning (`menu.bat`, `venv.bat`)

LLM story → TTS → video. Useful specifics worth stealing:

- **Duration heuristic: ~1.2 minutes per sentence** — better than wpm for
  planning a target runtime
- **`utils/make_loopable.py`** — crossfades end→start for a seamless loop
  (`--duration 5.0` crossfade). Solves the `-stream_loop` seam problem for
  *visuals* (our `PIPELINE.md` noted stream copy can't crossfade audio)
- **Audio post-processing chain:** normalization to **−20 dB** · tempo **0.9** ·
  light echo (`delay 0.1`, `decay 0.05`)
- Story generator *"avoids excitement, drama, or narrative tension **by design**"*
  — the policy-safe default, built in
- TTS providers: Zonos, Orpheus (presets `jess/mia/leo/zac`, `speed 0.9`),
  StyleTTS2

**Weaker than sleep-learning-engine** (no tests, no CLI discipline, 0 stars).
Use it as a **reference for the audio chain and the loop utility**, not as a base.

### Supporting cast

| Repo | ★ | Use |
|---|---|---|
| [`noisetool`](https://pypi.org/project/noisetool) (PyPI) | — | 6 noise types + **BS.1770-4 LUFS normalization**. `pip install noisetool && noisetool --type brown --lufs -14` |
| [`gregoryjpark/ambient-factory`](https://github.com/gregoryjpark/ambient-factory) | — | Noisli-style ambient mixer (rain, wind, fire, thunderstorms) |
| [`blastshielddown/ambient-python`](https://github.com/blastshielddown/ambient-python) | — | **Algorithmic/evolving soundscapes** — variety without repetition, directly serves R1 |
| [`AsadNoul/sleep-tracker-sounds`](https://github.com/AsadNoul/sleep-tracker-sounds) | 2 | ~30 ready MP3s (brown/pink/white, rain×4, ocean×4, wind×3, forest, fire). **License unverified — reference only, do not ship** |
| [`pranavrathod07` YT Automation Pro](https://yt-automation-pro.netlify.app/) | — | Open-source Shorts pipeline: Pixabay + Groq + YouTube Data API v3, cron, multi-channel, **never repeats a clip**. Solves the *upload plumbing* if we stay Shorts-shaped |
| [`jakeolschewski/faceless-content-guide`](https://github.com/jakeolschewski/faceless-content-guide) | 7 | MIT. Its niche RPM table: **relaxation/ambient $3–8** — sits inside our `RESEARCH.md` §1 planning band |

---

## 3. Recommended composition

```
sleep-learning-engine      ← render engine (MIT, tested, free TTS + free LLM)
  + our guardrails         ← distinctness gate, SEO stage, human publish gate
  + noisetool / Slo recipe ← foundation beds at −14 LUFS
  + sleeptale's loop util  ← seamless visual crossfade
  + powvid's voice matrix  ← 6 voices × 6 accents, already gate-passing
```

**Build order change:** `PIPELINE.md` §Build order said start with bed synth.
That's now step 2 — **step 1 is clone `sleep-learning-engine` and render one
30-minute video end to end.** It answers the "does it actually produce
something shippable" question for free, with no credentials.

---

## 4. X / Twitter — searched, nothing usable

Queried for sleep-niche build-in-public threads and monetization discussion.
**Results were unrelated accounts** (`@sleeprealsleep` = digital art,
`@sleepdeprived` = a comedy channel). The web-search path into X returns
profile cards rather than post content, so **this is a search limitation, not
proof that nothing exists.**

**Not concluded either way.** If X threads matter, they need a logged-in search
or Nitter instance — worth doing properly rather than reporting a false
negative.
