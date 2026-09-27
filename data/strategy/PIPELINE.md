# Sleep Channel — Pipeline

*Technical build. Commands marked ✅ were run on this box (ffmpeg 8.0.1,
numpy 2.5.2). Commands marked 📋 are cited and untested.*

---

## Shape

```
             ┌── Pillar A: narrated story ── TTS ──┐
idea → facts │                                     ├→ mix → loop → scene → lint → human → upload
             └── Pillar B: ambient bed ── synth ───┘
                   (NumPy)                         (ffmpeg)      (Flux/SDXL)
```

Three independent stages — swap any one without breaking the others
(dev.to build log). **No render-path LLM**, same rule powvid already runs.

---

## Stage 1 — Audio

### Ambient bed (NumPy) ✅ core available

Brown/white noise and binaural are a few lines. Delta band for sleep is
**0.5–4 Hz** — one sine per ear, offset by the beat frequency.

```python
import numpy as np, wave, struct

SR = 44100

def brown(n, amp=0.25):
    w = np.cumsum(np.random.randn(n)); w /= np.max(np.abs(w)) or 1.0
    return (w * amp).astype(np.float32)

def binaural(n, base=200.0, beat=2.0, amp=0.12):
    t = np.arange(n) / SR
    l = np.sin(2*np.pi*base*t); r = np.sin(2*np.pi*(base+beat)*t)
    return (np.stack([l, r], 1) * amp).astype(np.float32)
```

Write raw float32 → let ffmpeg encode (avoids numpy/wav bit-depth traps).

### The loop trick — ✅ **verified on this box**

Re-encoding a 10-hour file the obvious way takes minutes. `-stream_loop`
**copies the stream instead**:

```
ffmpeg -stream_loop 9 -i base.mp3 -c copy out.mp3
```

Measured here: `4934 B → 47306 B`, **1s → 10.4s in 0.079s**.
Extrapolates to dev.to's reported **68 MB → 680 MB in under 30s**. ✅

**Caveat:** stream copy means no crossfade at the loop seam. For a rain bed
that's inaudible; for a narrated story it is *not* — see below.

### Narration over bed 📋 (cited: dev.to)

```bash
ffmpeg -i narration.mp3 -i bed.mp3 \
  -filter_complex "[0:a]volume=1.0[narr];[1:a]volume=0.35[bed];[narr][bed]amix=inputs=2:duration=longest[out]" \
  -map "[out]" -c:a libmp3lame -q:a 2 final.mp3
```

**Ambient at 35% under voice.** This is the whole RPM delta (`$8–10` →
`$10–15`), so it's worth getting right.

### TTS options

| | Notes |
|---|---|
| **powvid's existing voice stack** | Reuse. 6 voices + 6 accents already chosen and tested |
| Voxtral (Mistral) | Cited by dev.to. **Rate-limits at 50+ calls**; a 2,200-word story is 60–80 segments — batch and back off |
| Kokoro | Local, free — used by `edwardyen724-g/paper2video` |

**Sleep pace is 0.7–0.9× normal**, not the 150 wpm we use for shorts. This is
a TTS rate parameter, not a new pipeline. (Open question #2 in `STRATEGY.md`.)

---

## Stage 2 — Visual

Original per upload, no exceptions (`STRATEGY.md` R3).

- **Generated:** Flux / SDXL per scene — this is what `CF_API_TOKEN` unblocks
  in powvid too. One token, both projects.
- **Stock:** Pexels / Pixabay video — acceptable *only* paired with an
  original audio bed. Stock+stock is the flagged combination.
- **Motion:** slow pan/zoom (Ken Burns) on a still, or a genuinely looping clip.

**Never** reuse one loop across uploads. That's detection signal #4.

---

## Stage 3 — Guardrails before publish

### Automated, fail-closed (powvid pattern)

```
runtime        within declared block?  (90m / 2h / 3h / 8h — must VARY)
audio non-empty   ✅ the dev.to silent-video bug: check size, not existence
                   `if p.stat().st_size < 10_000: abort`
distinctness    runtime not within 1% of a prior upload (blocks 3:08:09 ×30)
thumbnail hash   perceptual distance from last N (blocks template drift)
title pattern    no `#NN` / `Vol. NN` formulaic numbering
rights           audio source in allowlist (own synth / CC0 / paid license)
disclosure       Altered-or-synthetic toggle set
```

### Human, mandatory

Approve → render → upload. **No scheduler that publishes unreviewed.**
(`STRATEGY.md` R5; also the single consensus point across every policy source
surveyed.)

---

## What exists already

| Need | Status |
|---|---|
| ffmpeg 8.0.1 | ✅ installed, `-stream_loop` verified |
| numpy 2.5.2 | ✅ installed |
| TTS voices + accents | ✅ powvid, 6×6 matrix, gate-passing |
| Fact lint / receipt pattern | ✅ powvid `lint_script()` |
| Loop/chapter structure | 📋 spec'd here, not built |
| Scene generation | ⛔ blocked on `CF_API_TOKEN` |
| Upload (YouTube Data API) | ⛔ no OAuth credentials yet |
| Music bed | ⛔ no licensed source selected |

---

## Build order

1. **Bed synth + `-stream_loop`** — hours of work, unblocks everything, zero
   dependencies. Prove a 10-hour rain file end to end.
2. **Narration mix at 35%** — one ffmpeg graph, and it's the RPM decision.
3. **Distinctness gate** — cheap, and it's the policy insurance. Build it
   *before* volume, not after.
4. **First 90-minute narrated story, one channel, reviewed by a human.**
5. Only then: `CF_API_TOKEN` for scenes, YouTube OAuth for upload.
