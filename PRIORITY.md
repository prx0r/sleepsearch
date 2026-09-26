# Production Priority — Easiest First

## The Principle
Start with channels that:
1. Require the least production effort
2. Have the simplest content structure
3. Can be produced at scale immediately
4. Prove the pipeline works before adding complexity

---

## Priority 1: E4 Ambience (Effort: 1)
**No narration. No script. Just sound + visual loop.**

| Channel | Content | Why easiest |
|---|---|---|
| **Fly on the Wall** | Ambient room sounds + slow visual | No TTS, no script, no narration |
| **Anti-Sleep War** | Distant battle sounds + rain | Same as above |
| **Anti-Sleep Arguing** | Muffled voices + room tone | Same as above |
| **Fly on the Wall Pure** | Pure ambient, no concept | Simplest possible |

**Production per video:**
- Audio: Synthesize ambient bed (numpy) or source from freesound.org
- Visual: Slow loop (CSS animation or simple video)
- Duration: 2-8 hours
- Time to produce: ~30 minutes

---

## Priority 2: E2c Library (Effort: 2)
**PD text, chapter-by-chapter. Completionist.**

| Channel | Content | Why easy |
|---|---|---|
| **Meditations** | Marcus Aurelius, 12 books | Finite, structured, PD |
| **Darwin's Library** | Origin + Letters | Finite, structured, PD |
| **Seneca's Library** | Letters and essays | Finite, structured, PD |
| **Plato's Library** | 30 dialogues | Finite, structured, PD |

**Production per video:**
- Text: PD source (Gutenberg)
- TTS: Voice from registry (V01 Sage or V09 Archivist)
- Visual: Hand-drawn symbol or black screen
- Duration: 30-60 minutes
- Time to produce: ~1 hour

---

## Priority 3: E5d Reference (Effort: 2)
**Enumerated items, one per episode.**

| Channel | Content | Why easy |
|---|---|---|
| **Sleepy Periodic Table** | 118 elements | Structured data, infinite |
| **Sleepy Taxonomy** | Species | Structured data, infinite |
| **Sleepy Constellations** | Star patterns | Structured data, infinite |
| **Sleepy Numbers** | Mathematical constants | Structured data, infinite |

**Production per video:**
- Text: Structured data (API or database)
- TTS: Voice from registry (V03 Lecturer)
- Visual: Black screen or simple graphic
- Duration: 30-60 minutes
- Time to produce: ~45 minutes

---

## Priority 4: E5b Words (Effort: 3)
**Word origins, etymology, vocabulary.**

| Channel | Content | Why medium |
|---|---|---|
| **Sleepy Etymology** | Word origins | Need source data |
| **Thesaurus Sleep** | Synonyms | Need source data |
| **Roots Sleep** | Prefixes/roots | Need source data |
| **Idioms Sleep** | Idiom origins | Need source data |

**Production per video:**
- Text: Etymonline/Wiktionary
- TTS: Voice from registry (V03 Lecturer or V10 Companion)
- Visual: Hand-drawn word transforming
- Duration: 15-30 minutes
- Time to produce: ~1.5 hours

---

## Priority 5: E2a Reading (Effort: 3)
**PD text, read slow. The workhorse.**

| Channel | Content | Why medium |
|---|---|---|
| **Fairy Tales** | Grimm, Andersen | PD, needs sourcing |
| **Foreign Folklore** | Global tales | PD, needs sourcing |
| **Alchemical Secrets** | Alchemy texts | PD, needs sourcing |
| **Sleepy Buddha** | Buddhist texts | PD, needs sourcing |

**Production per video:**
- Text: PD source (Gutenberg/LibriVox)
- TTS: Voice from registry (V01-V10 based on shelf)
- Visual: Hand-drawn symbol
- Duration: 30-60 minutes
- Time to produce: ~1.5 hours

---

## Priority 6: E5a Essay (Effort: 5)
**Topics discussed. Needs script writing.**

| Channel | Content | Why harder |
|---|---|---|
| **AGI Scenarios** | AI futures | Needs original script |
| **Sleepy Maths** | Mathematical concepts | Needs original script |
| **Sleepy Architecture** | Buildings | Needs research |
| **Sleepy Recipes** | Historical cooking | Needs research |

**Production per video:**
- Text: Original script + research
- TTS: Voice from registry
- Visual: Hand-drawn or black screen
- Duration: 30-120 minutes
- Time to produce: ~3 hours

---

## The Build Order

```
Week 1: E4 (ambience) — prove the pipeline
  Fly on the Wall × 2
  Anti-Sleep War × 1
  
Week 2: E2c (library) — prove TTS works
  Meditations × 3 (Books 1-3)
  
Week 3: E5d (reference) — prove data pipeline
  Sleepy Periodic Table × 5 (first 5 elements)
  
Week 4: E5b (words) — prove word sourcing
  Sleepy Etymology × 5
  
Week 5: E2a (reading) — prove PD sourcing
  Fairy Tales × 3 (Grimm)
  
Week 6: E5a (essay) — prove script writing
  AGI Scenarios × 2
```

---

## Resource Requirements

### Immediate (Week 1)
- YouTube API key ✅ (you have one)
- Kaggle account ✅ (you have one)
- freesound.org account (for ambient sounds)

### Week 2-3
- Qwen3 TTS running on Kaggle
- Voice references designed

### Week 4+
- More PD source material
- Visual generation pipeline
