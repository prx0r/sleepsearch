# Sleep Channel — Channel Index

*The proposed channels, scored against the API, with rights status.*

Compiled 2026-09-26. Method and caveats in `CATEGORIES.md` §6 — same probe:
EN, `regionCode=US`, relevance-ranked, top-10, median.
`ideas.json` holds the raw numbers.

**How to read `fresh_pct`:** share of that query's top 10 published in the last
540 days. **≥80% = the door is open. ≤30% = incumbents are holding it shut.**
Read it before the view count — a big number behind a closed door is worse than
a small number behind an open one.

---

## 1. The twelve ideas, scored

| # | Idea | Query | Median views | **Fresh** | Dur | Call |
|---|---|---|---|---|---|---|
| 1 | Rudolf Steiner lectures | `steiner lectures to sleep to` | **3,445** | 20% | 40m | ❌ **no demand** |
| 1b | — | `anthroposophy to sleep to` | 3,797 | 10% | 40m | ❌ no demand |
| 2 | Near-death experience | `near death experience to sleep to` | **1,469,987** | 40% | 61m | ⚠️ big, busy |
| 3 | Diamond dreams (Plato) | `plato to sleep to` | 13,291 | **100%** | 131m | ❌ no supply, no demand |
| 3b | — | `proclus to sleep to` | **458** | 20% | 89m | ❌ dead |
| 3c | — | `neoplatonism to sleep to` | 5,045 | 90% | 124m | ❌ dead |
| 4 | Law of Ra | `law of ra to sleep to` | 65,786 | **10%** | 38m | ❌ small + shut |
| 4b | Channeled wisdom (wide) | `channelled wisdom to sleep to` | 271,657 | 60% | 147m | ✅ Tier B |
| 5 | Sleepy soul (Dolores Canon) | `dolores canon to sleep to` | 429,869 | **0%** | 77m | ⚠️ demand, **door welded** |
| 6 | Sleeping genius (quantum) | `quantum physics to sleep to` | 165,638 | **100%** | 161m | ✅ **ENTER** |
| 6b | Sacred geometry | `sacred geometry to sleep to` | 23,277 | 60% | 390m | ❌ no demand |
| 7 | Positive news | `positive news to sleep to` | 191,512 | 60% | 205m | ✅ Tier B |
| 8 | Alchemical secrets | `alchemy to sleep to` | 232,128 | **90%** | 45m | ✅ **ENTER** |
| 8b | Hermeticism | `hermeticism to sleep to` | 51,578 | 60% | 220m | ⚠️ thin |
| 9 | Angel sleep | `angels to sleep to` | 1,032,935 | **20%** | 380m | ⚠️ big, **shut** |
| 10 | Tantrāloka / Kashmir Shaivism | `kashmir shaivism to sleep to` | 16,781 | 20% | **20m** | ❌ wrong format |
| 10b | — | `tantraloka sleep` | **650** | 20% | 53m | ❌ **dead** |
| 12 | Sleepy shoggoth (Lovecraft) | `lovecraft to sleep to` | 671,266 | **20%** | 112m | ⚠️ big, **shut** |
| 12b | — | `cosmic horror to sleep to` | 59,446 | 60% | 113m | ⚠️ thin, open |

### The pattern in your own list

Three distinct groups, and the group matters more than the individual idea:

**🅰 Demand, closed door (4)** — NDE · Angels · Lovecraft · Dolores Canon.
Millions of views, ≤40% fresh. Someone already owns these.

**🅱 Real demand, open door (4)** — **quantum physics** · **alchemy** ·
channelled wisdom · positive news. These are the keepers.

**🅲 No measurable demand (8)** — Steiner · Plato · Proclus · Neoplatonism ·
Law of Ra · sacred geometry · Tantrāloka · Kashmir Shaivism.

The 🅲 result is the uncomfortable one, so let's be precise about it:

> **`tantraloka sleep` returns a median of 650 views. `proclus to sleep to`
> returns 458. `steiner lectures to sleep to` returns 3,445 at 2 views/day.**

Free source material does not create demand. The motherlode is real *as
content*; it is not currently real *as search*. Those are different claims and
the API only speaks to the second.

**Which is not a reason to drop them** — see §4. A 650-view category with zero
competition and a 100%-open door is a *test*, not a launch. Plato at 13,291
views and **100% fresh** means nobody has filled it, and one video that breaks
out owns the shelf.

---

## 2. Additions from our own material

| Idea | Source we already own | Query | Views | Fresh | Call |
|---|---|---|---|---|---|
| **Kashmir Shaivism readings** | `powvid/entities/anakhya` — **Tantrāloka is already its PRIMARY source**, verified 2026-09-26 | `kashmir shaivism to sleep to` | 16,781 | 20% | ❌ build it, but expect nothing |
| **Hermetic / traditional counts** | `powvid/entities/ochema` — Western/Hermetic, *"why every tradition counts the same way"* | `hermeticism to sleep to` | 51,578 | 60% | ⚠️ thin but open, 220m |
| **Scripture / commentary** | — | `bible to sleep to` | **1,040,838** | 60% | ✅ **Tier B, 3,200 views/day** |
| **Theology** | — | `theology to sleep to` | 166,042 | **80%** | ✅ **ENTER, 7.8 v/sub** |
| **Stoicism** | — | `stoicism to sleep to` | 112,903 | **80%** | ✅ **ENTER, 252m** |
| **Esoteric (wide)** | — | `esoteric to sleep to` | 64,158 | **80%** | ✅ **ENTER, 9.4 v/sub** |
| **Machine mind / synthetic life** | `/root/synthetic` + entities `synthetic-minds`, `ai-breakthroughs`, `ai-bio`, `ai-models` | not yet probed | — | — | 🔶 probe before committing |

**`anakhya` is already built and gate-passing** — Tantrāloka facts frozen,
scenes mapped, script written, fact-lint green. It is the one idea on your list
with **production-ready assets and zero market.** Ship it as a low-cost test
while the revenue plays do the earning.

---

## 3. Rights — the constraint that actually decides this

Your list is materially riskier than rain sounds, because most of it is
**someone's copyrighted translation being read aloud.**

| Channel idea | Rights status | Risk |
|---|---|---|
| Alchemy · Hermeticism | Pre-1930 texts (Paracelsus, Agrippa, Fludd, *Corpus Hermeticum*) — **public domain** | ✅ clean |
| Plato · Proclus · Neoplatonism | Ancient texts; **Jowett (1871), Long, and other 19th-c. translations PD** | ✅ clean *if you pick the PD translation* |
| Stoicism | Marcus Aurelius / Epictetus / Seneca — PD translations exist (Casaubon 1634, Long 1877) | ✅ clean |
| Bible / scripture | **KJV, ASV, WEB are public domain in the US** | ✅ clean |
| Cosmic horror / Lovecraft | Died 1937; **1930-and-earlier publications PD as of 2026** | ✅ mostly clean — but *not* posthumous additions |
| Quantum / science | Facts, not expression | ✅ clean with care |
| **Tantrāloka / Tantrasāra** | Text is 10th-c.; **every modern English translation is ©** (Muktananda, Singh…) | 🔴 **reading a translation aloud = infringement** |
| **Steiner lectures** | Died 1925, but English translations and the recordings are managed by Rudolf Steiner Nachfolger / SteinerBooks | 🔴 **not "free"** |
| **Law of Ra** | © L/L Research — freely distributed, still copyrighted and controlled | 🔴 |
| **Dolores Canon** | © Ozark Mountain Publishing, **actively enforced** | 🔴 |
| **NDE accounts** | Individual © per experiencer/author | 🔴 verbatim |
| **Positive news** | Individual articles © | 🔴 verbatim |
| **Game / film / TV lore** | Franchise © (FromSoftware, Bandai…) | ⚠️ **but** we're *summarising*, not reproducing |

### The one rule that saves the whole plan

```
🔴  Reading a copyrighted TRANSLATION aloud   = reproduction = infringement
✅  RETELLING in your own words               = transformative = fair use holds
```

**`anakhya`'s `facts.md` already encodes this**, and it should be the house rule:

> *"Attribute every claim to the text or the tradition. Never present doctrine
> as established fact, and **never present a translation as if it were the
> original**."*

Concretely: for Tantrāloka, cite the Sanskrit term, *describe* the doctrine,
quote at most a line or two under fair use. **Do not read chapter 1 aloud for
four hours.** Same shape for Law of Ra, Dolores Canon, and Steiner.

**The uncomfortable overlap:** your 🅲 group (no demand) is largely the 🔴 group
(copyrighted), and the 🅱 group (open door) is largely the ✅ group (public
domain). **The market and the law agree with each other here**, which is
convenient — the safe channels are the ones worth building.

---

## 4. So: is it a motherlode?

**As content, yes.** Twelve ideas, and we already own two production-ready
entities (`anakhya`, `ochema`) before writing a single new script.

**As search demand, partially.** Four clear entries, four busy, eight empty.

The right frame is the one from `TEMPLATES.md` §1 — *the format is commoditised,
the topic is the moat*:

> A category with **100% fresh and 13K views** is an empty shelf in a
> populated store. A category with **20% fresh and 1M views** is a full shelf
> you'll never break into. The empty shelf is the opportunity; the API just
> can't tell you whether anyone walks down that aisle.

**Sequence, not scatter:**

| Phase | Channels | Why |
|---|---|---|
| **1 — earn** | `history` · `bible/theology` · `stoicism` · `quantum physics` | Tier A/B, open doors, public domain, big enough to hit YPP |
| **2 — own** | `alchemy` · `esoteric` · `cosmic horror` | Tier A, open, uniquely ours (ochema, Hermetic counts) |
| **3 — test cheaply** | `anakhya` (Tantrāloka) · `ochema` · Plato/Proclus | Assets already exist. Ship, measure, revisit. Cost ≈ one render |
| **4 — park** | Steiner · Law of Ra · Dolores Canon · Angels · NDE | Rights risk **and/or** a door someone else holds |

Phase 3 is the interesting one: **anakhya costs us nothing but render time**,
because the research, scenes and lint-passing script already exist. It's a free
option on a category that might be early rather than empty.

---

## 5. "Post the same video on 5 channels" — the evidence

You asked, so here's what the sources actually say.

**In favour (weak, short-term):**
- r/NewTubers: *"Technically, yes... YouTube won't immediately punish you for
  it. But it's not really recommended long-term."*
- One creator re-uploaded an identical Short: **50 views → 6,000 views in 2
  hours.** They deleted the original anyway. *("If the view number is low,
  not worth the risk.")*

**Against (strong, policy-level):**
- r/PartneredYoutube: **"Multiple Channels Deactivated without warning
  (duplicate/copied content)"** — several channels, one strike pattern, gone.
- The Verge (2018): YouTube removing creators from YPP for *duplicative
  content* — explicitly a **YPP policy, not a copyright strike.**
- TechCrunch (2018): **YouTube launched a tool that scans every newly uploaded
  video** and checks if it's a re-upload or *"very similar"* to an existing one.
- GeeLark (2026): *"If multiple channels repeatedly use the same video file,
  similar title formulas, near-identical descriptions, and similar thumbnails,
  YouTube can more easily group the content as **repetitive distribution or
  low-differentiation content**."*
- r/NewTubers: *"it can confuse the algorithm about which video to push."*

**My read — three reasons not to:**

1. **The advice is pre-July-2025.** It describes the world before *inauthentic
   content* existed as a named policy. Since then this isn't a grey area — it's
   the exact pattern YouTube's trust & safety chief said they remove from YPP
   (`RESEARCH.md` §2).
2. **It's economically incoherent.** Five copies of one video cost the same to
   make as one video. You get 5× the ban exposure for **0× extra content.** If
   you have five videos, publish five videos.
3. **Proxies solve the wrong problem.** See §6.

**The legitimate version does exist:** YouTube officially supports up to **50
channels under one Brand Account**, and running *different* content for
*different* audiences across them is normal and fine. Multiple channels yes.
**The same video five times, no.**

---

## 6. Proxies — the honest answer

**What the guides say** (spyderproxy, dataimpulse, geelark, gologin, quantumproxies, send.win):

- **Datacenter IPs are pre-flagged** by Google's WAF in 2026 — *"the downgraded
  library."* Never use them for accounts.
- **One dedicated IP per channel.** Sticky sessions; *"real users do not
  teleport across the world between logins."*
- **Mobile (carrier 4G/5G) proxies for cold-start warm-up**, then static
  residential in the account's home region. $15–80/GB vs $1–3/GB residential.
- **Cascade-ban risk is the real danger**: shared cookies, fingerprint, or IP
  chains accounts together, and one removal takes all of them.
- Isolation table (GeeLark): regular browser profiles = **High** risk · proxy
  only, no fingerprint isolation = **Medium-high** · multi-account browser =
  **Low**.

**What they don't advertise:**

[IPinfo, 2026](https://ipinfo.io/reports/residential-proxy-infrastructure-research) —
Google **disrupted IPIDEA, the largest residential proxy network, in January
2026**. And:

> **46% of all residential proxy IPs appear in more than one provider's
> network simultaneously.** 92.7% cross-provider overlap · 550+ distinct threat
> groups used IPIDEA in a single week.

**The proxy ecosystem is itself a detectable cluster.** Buying a proxy does not
put you outside the graph; it puts you in the part of the graph Google is
actively mapping.

**And the framing problem:** proxy guides exist to hide *account linkage*. But
the linkage that kills a sleep network isn't IP — it's **content**. Identical
video files, identical title formulas, identical thumbnails. **No proxy hides a
hash match.**

> **If a strategy requires proxies to work, it's a farm.**
> `STRATEGY.md` says the machine isn't the problem and the sameness is.
> Proxies defend the sameness. They don't fix it.

**Recommendation: don't.** Not for policy reasons — for *economic* ones. Run
one channel properly. If a second channel is ever justified, give it genuinely
different content and let the Brand Account handle it. Spend the proxy budget
on a render.

---

## 7. Next probe

`synthetic-minds` / `ai-breakthroughs` / `/root/synthetic` have **no
`___ to sleep to` query yet.** Given `quantum physics to sleep to` came back at
**100% fresh / 165K**, the machine-consciousness cluster deserves the same
two-minute, ~200-quota-unit test before anyone commits production time.

**Standing rule, learned from Medium's two misses:** autofill *and* API,
always, before building. Two minutes.

---

## 8. New: early Buddhism / "Sleepy Buddha" — probed 2026-09-26

13 queries, same method. **This is a Tier A cluster.**

| Query | Median views | **Fresh** | Dur | V/sub | Call |
|---|---|---|---|---|---|
| `sleepy buddha` (name check) | 260,508 | 80% | 181m | 2.3 | ✅ name is usable |
| `early buddhism to sleep to` | 243,997 | **90%** | 183m | 2.5 | ✅ **ENTER** |
| `buddhist philosophy to sleep to` | 216,402 | **90%** | 192m | **4.3** | ✅ **ENTER** |
| `buddhism to sleep to` | 208,638 | **90%** | 183m | 2.5 | ✅ **ENTER** |
| `buddhist stories to sleep to` | 194,371 | **100%** | 200m | 3.4 | ✅ **ENTER** |
| `buddha to sleep to` | 170,603 | **100%** | 191m | 2.5 | ✅ **ENTER** |
| `dhamma to sleep to` | 138,423 | **100%** | 197m | 1.6 | ✅ **ENTER** |
| `marcus aurelius to sleep to` | 101,730 | 80% | 177m | 1.9 | ✅ ENTER |
| `pali canon to sleep to` | 24,143 | 80% | 180m | 1.7 | ⚠️ thin |
| `stoic meditation to sleep to` | 11,836 | 80% | 240m | 0.5 | ❌ thin |
| `sutta to sleep to` | **576** | 80% | 118m | 0.7 | ❌ dead |
| `zen to sleep to` | 3,683,354 | 40% | 182m | 9.4 | ⚠️ Tier C-ish |
| `meditation stories to sleep to` | 1,265,517 | 40% | 155m | 3.4 | ⚠️ busy |

**Profile compare:** `buddhism to sleep to` = 209K / 90% fresh — **statistically
identical to `history to sleep to` (200K / 100%)**, our Phase 1 primary. Seven of
thirteen grade ENTER. `buddhist philosophy` at **4.3 views/sub** is the best
discovery signal in this batch.

**Autofill is thin but present:** `buddhist stories to fall asleep to` ·
`fall asleep to buddhism` · `buddhist sleep`. Compare `lore to sleep to`'s 11
franchise completions — Buddhism has **less depth of demand but far less
saturation.** Early niche, not a crowded one.

**Watch out:** `sleep meditation for ___` autofills *depression · insomnia ·
pain relief · anxiety · healing*. Huge modifier space — and **medical claims
territory**, which is the third inauthentic-content category (AI personas on
sensitive topics, `RESEARCH.md` §2). **Do not chase those modifiers.**

### 8.1 Rights — the two figures you named are both 🔴

| Source | Status |
|---|---|
| **Pāli Canon (Tipiṭaka) original** | ✅ **public domain** — SuttaCentral: *"original texts of Buddhism in Pali... are in the public domain"* |
| **Bhikkhu Sujato** (four Nikāyas, Dhammapada, Khuddaka) | ✅ **CC0** — *"dedicated to the public domain via Creative Commons Zero. You are encouraged to copy, reproduce, adapt, alter, or otherwise make use of this translation"* |
| **Thanissaro** (Access to Insight) | ✅ free to distribute under stated terms |
| **Ñāṇavīra Thera** (*Clearing the Path*, *Notes on Dhamma*) | 🔴 **Path Press holds the copyrights** — *"a non-profit entity which handles legal matters and holds the copyrights of all Ven. Ñāṇavīra Thera's writings."* Site footer: *"Copyright 2009 All Rights Reserved"* |
| **Ñāṇamoli Bhikkhu** (*Middle Length Discourses*, *Path of Purification*) | 🔴 © **Wisdom Publications / BPS** |
| **Bhikkhu Bodhi** | 🔴 © Wisdom, actively enforced |
| **Pali Text Society** | 🔴 ©, enforced |

**So: the channel is buildable; the two names you led with are the two you
can't read aloud.** The clean corpus is **Sujato** — and it's large enough to
carry a channel: full four Nikāyas plus Khuddaka, all CC0, with source files
on GitHub.

### ⚠️ One genuine judgment call on Sujato

Sujato's CC0 page also carries a *request*:

> *"The translator respectfully requests that any use be in accordance with the
> values and principles of the Buddhist community. In particular, **please do
> not use this work in AI training datasets, for the development of any AI
> model or algorithm, or in any AI-derived technologies.**"*

- **Legally:** CC0 is an unconditional, irrevocable dedication. The request
  doesn't revoke it. Reading the text aloud is publishing it, which is what CC0
  invites.
- **Ethically:** the request is real, deliberate, and **directed at exactly the
  audience we'd be serving.** Our pipeline is AI-mediated.
- **Call:** it's a judgment, not a violation. If we proceed — **attribute
  Sujato prominently, state CC0, don't obscure the source**, and don't pretend
  the request isn't there. A sleep channel about the Dhamma that quietly
  disregards the translator's stated wish is a bad foundation for the audience
  it needs.

**Flagged for the owner to decide, not resolved here.**

### 8.2 Cadence and quotes

**Cadence — 3 days is fine, and not for the reason the gurus say.**

YouTube: *"growth in views across uploads is **not correlated with time
between uploads**."* So 3-day vs 7-day has **no algorithmic difference.**

Cadence is a **production-capacity** question:

| | 1/week | every 3 days |
|---|---|---|
| Videos/month | 4 | ~10 |
| Measurability | easy — isolate what worked | harder — confounds |
| Time to 8,000 hrs | slower | ~2.5× faster |
| Sustainable? | yes, hand-made | only if **rendering is automated** |

**Recommendation:** set cadence to *the fastest rate you can hold without
quality dropping*, then **keep the interval exact and never publish Friday**
(`SCHEDULE.md` §5). If the render pipeline runs unattended, 3 days is right.
If a human is reviewing every frame, it isn't.

**Quotes in descriptions — yes, and it's doing three jobs at once:**

1. **SEO** — description weight is **high** for long-form, tags are secondary
   (`CATEGORIES.md` §6.2)
2. **Distinctness** — every video's description differs by its own quote; that
   feeds the `distinctness` judge (`ORGANISE.md` §5)
3. **Positioning** — a quote from the tradition signals *what this channel is*
   in the first 150 characters before the fold

Format: **open with one line of the text, then the episode framing, then the
chapter list.** Never a keyword wall — Google's own guidance is that
misleading metadata gets deranked.

---

## 9. Failure playbook — "what if it just dies, make a similar channel?"

**Default answer: no — diagnose first, rename second, clone last.**

Most failures are not channel failures. Four different symptoms, four
different fixes:

| Symptom | What it actually is | Fix | New channel? |
|---|---|---|---|
| **No impressions** | discoverability | new **topic** / niche — re-probe `CATEGORIES` | ❌ same channel |
| **Impressions, low CTR** | packaging | new **thumbnails + titles** | ❌ same channel |
| **CTR but low AVD** | content or structure | new **skeleton** (`DNA.md` §5) | ❌ same channel |
| **YPP rejected** | positioning / policy | ⚠️ **stop publishing, diagnose** | ✅ **only then** |

The last row is `STRATEGY.md`'s kill criteria, unchanged: *if rejected for
inauthentic content, **stop, and diagnose against `RESEARCH.md` §3 before
adding a single video.** Do not upload more and hope.*

### Rename before you clone

YouTube channels **can be renamed and rebranded in place.** If "Sleepy Buddha"
doesn't land, rename it. Cost: zero, and the watch history, subs and
algorithmic learning all survive.

**Cloning costs everything** — you're back at zero subscribers, zero data, and
you've just created a second upload of the same file, which is the
duplicate-content path `CHANNELS.md` §5 already documented as getting
*"Multiple Channels Deactivated without warning."*

> **Move the *learning*, never the *content*.**

### The two cases where a new channel really is correct

1. **The corpus has to change** — e.g. we discover the rights position forces
   us off a source we've built the channel's identity around. The premise
   changed, not the execution.
2. **The niche genuinely closed** — `fresh_pct` fell below the entry bar
   (`ORGANISE.md` §6, A2 alarm). Someone else owns it now.

Both are premise failures. **Execution failures get fixed in place.**

### The sequencing rule that makes "what if it fails" moot

`ORGANISE.md` §9 already answers this structurally:

```
Wave 0   simulate ONE channel end to end     ← fails here? costs one render
Wave 1   embody TWO channels                 ← fails here? costs two channels
Wave 2   simulate the rest → partial
Wave 3   embody ≤1/week
```

**Wave 0 exists so that "what if it fails" is answered before anything is
live.** If the pipeline can't produce a shippable 30-minute video, no amount
of channel-making fixes it — and no channel exists to have failed.

**The cheapest possible failure is a render, not a channel.**
