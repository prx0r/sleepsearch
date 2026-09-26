# Engine Specs — Detailed Production Guides

---

## E4: Ambience (Effort: 1)

### What it is
Pure ambient sound + slow visual loop. No narration. The room IS the content.

### Channels served
- Fly on the Wall (35)
- Anti-Sleep War (39)
- Fly on the Wall Pure (40)
- Anti-Sleep Arguing (48)

### Production pipeline
```
1. Source ambient audio
   - freesound.org (CC0/CC-BY)
   - numpy synthesis (brown noise, rain, etc.)
   - field recordings (if available)
   
2. Create visual loop
   - CSS animation (slow drift)
   - Simple video loop (5-10 seconds)
   - Black screen (simplest)
   
3. Combine
   - ffmpeg: loop audio + visual
   - Duration: 2-8 hours
   
4. Upload
   - Title: "[Concept] — [Duration] Ambient for Sleep"
   - Tags: ambient, sleep, [concept]
```

### Audio sources

| Source | License | What's available |
|---|---|---|
| freesound.org | CC0/CC-BY | City ambience, nature, rain |
| numpy synthesis | Free | Brown noise, rain, wind |
| BBC Sound Effects | Personal use | 33,000+ sounds |

### Example: Fly on the Wall
```
Audio: Room tone + distant traffic + occasional footsteps
Visual: Slow pan across empty room (CSS animation)
Duration: 4 hours
Title: "Empty Room at 3 AM — Ambient for Sleep"
```

### Example: Anti-Sleep War
```
Audio: Distant artillery + rain on concrete + generator hum
Visual: Dark bunker interior (static image, slow drift)
Duration: 8 hours
Title: "Bunker — Safe Inside, Storm Outside — 8 Hours"
```

---

## E2c: Library (Effort: 2)

### What it is
PD text, chapter-by-chapter. Completionist. Finite series.

### Channels served
- Meditations (23)
- Darwin's Library (99)
- Seneca's Library (102)
- Plato's Library (104)

### Production pipeline
```
1. Source PD text
   - Gutenberg.org
   - LibriVox
   - Internet Archive
   
2. Split into chapters
   - One chapter per episode
   - Or combine short chapters
   
3. TTS generation
   - Voice from registry (V01 Sage or V09 Archivist)
   - Rate: -30% for sleep pace
   - Provider: Qwen3 TTS (Kaggle)
   
4. Visual
   - Hand-drawn symbol (SVG)
   - Or black screen
   - Or simple gradient
   
5. Combine
   - ffmpeg: TTS audio + visual
   - Duration: 30-60 minutes per episode
   
6. Upload
   - Title: "[Author] — [Work], Book [N]"
   - Series playlist
```

### Example: Meditations
```
Source: Marcus Aurelius, Meditations (Gutenberg)
Voice: V01 Sage (British, wise, authoritative)
Visual: Simple candle flame animation
Episode format:
  "Book 1. Section 1.
   From my grandfather Verus I learned good morals and the government of my temper."
Duration: ~5 minutes per section
Playlist: "Meditations — Marcus Aurelius — Complete"
```

---

## E5d: Reference (Effort: 2)

### What it is
Enumerated items, one per episode. Structured data.

### Channels served
- Sleepy Periodic Table (72)
- Sleepy Taxonomy (73)
- Sleepy Constellations (77)
- Sleepy Numbers (76)

### Production pipeline
```
1. Source structured data
   - PubChem API (elements)
   - Wikipedia API (species, stars)
   - Mathematical constants database
   
2. Format each entry
   - Name, facts, story
   - Consistent structure per channel
   
3. TTS generation
   - Voice from registry (V03 Lecturer)
   - Rate: -30% for sleep pace
   
4. Visual
   - Black screen (simplest)
   - Or simple graphic per entry
   
5. Combine
   - Duration: 2-5 minutes per entry
   - Compile 10-20 entries per video
   
6. Upload
   - Title: "[Channel] — Entry [N] of [M]"
   - Series playlist
```

### Example: Sleepy Periodic Table
```
Source: PubChem API
Voice: V03 Lecturer (clear, neutral, American)
Visual: Black screen

Entry format:
  "Element 1 of 118.
   Hydrogen. Symbol H. Atomic number 1.
   The lightest element. The most abundant in the universe.
   Colorless, odorless, tasteless gas.
   Burns with an invisible flame.
   Makes up 75% of all normal matter by mass.
   First element. Simplest atom. One proton. One electron.
   Sleep well. Tomorrow: Helium."

Duration: ~2 minutes per element
Video: 20 elements per video = ~40 minutes
```

---

## E5b: Words (Effort: 3)

### What it is
Word origins, etymology, vocabulary. The "Sleepy Words" concept.

### Channels served
- Sleepy Etymology (75)
- Thesaurus Sleep (91)
- Roots Sleep (93)
- Idioms Sleep (94)

### Production pipeline
```
1. Source word data
   - Etymonline.com (etymology)
   - Wiktionary (definitions, origins)
   - Oxford Dictionaries API
   
2. Format each entry
   - Word → origin → journey → related words → story
   
3. TTS generation
   - Voice from registry (V03 Lecturer or V10 Companion)
   - Rate: -30%
   
4. Visual
   - Hand-drawn word transforming through languages
   - Or black screen
   
5. Combine
   - Duration: 2-5 minutes per word
   - Compile 5-10 words per video
   
6. Upload
   - Title: "Sleepy Words — [Theme]"
   - Series playlist
```

### Example: Sleepy Etymology
```
Source: Etymonline.com
Voice: V10 Companion (friendly, casual)

Entry format:
  "Salary. From Latin salarium. Salt money.
   Roman soldiers were paid in salt.
   This is why we say someone is 'worth their salt'.
   And this is why we say 'salad' — from Latin salata, salted things.
   The word travels through time, carrying the story of Roman commerce.
   Sleep well."

Duration: ~3 minutes per word
Video: 8 words per video = ~24 minutes
```

---

## E2a: Reading (Effort: 3)

### What it is
PD text, read slow. The workhorse engine.

### Channels served
- Fairy Tales (41)
- Foreign Folklore (42)
- Alchemical Secrets (8)
- Sleepy Buddha (26)
- 20+ more channels

### Production pipeline
```
1. Source PD text
   - Gutenberg.org
   - LibriVox
   - Internet Archive
   - Sacred-texts.com
   
2. Prepare text
   - Clean formatting
   - Split into episodes if needed
   - Add context/intro if needed
   
3. TTS generation
   - Voice from registry (V01-V10 based on shelf)
   - Rate: -30%
   
4. Visual
   - Hand-drawn symbol per tradition
   - Or black screen
   
5. Combine
   - Duration: 30-60 minutes per episode
   
6. Upload
   - Title: "[Source] — [Title]"
   - Series playlist
```

### Example: Fairy Tales
```
Source: Grimm's Fairy Tales (Gutenberg)
Voice: V02 Storyteller (warm, European)
Visual: Simple illustration of the tale

Episode format:
  "Grimm's Fairy Tales. The Snow Queen.
   Part 1. The Mirror.
   The mirror and the fragment.
   The mirror, it was so remarkable that everything reflected in it 
   was diminished and made worse..."
   
Duration: 15-30 minutes per tale
Playlist: "Grimm's Fairy Tales — Complete"
```

---

## E5a: Essay (Effort: 5)

### What it is
Topics discussed. Needs original script writing.

### Channels served
- AGI Scenarios (11)
- Sleepy Maths (27)
- Sleepy Architecture (74)
- Sleepy Recipes (79)
- 30+ more channels

### Production pipeline
```
1. Research topic
   - Wikipedia, academic sources
   - Books, articles
   - Expert interviews (if available)
   
2. Write script
   - 2000-4000 words per episode
   - Sleep-optimized pacing
   - No cliffhangers, no tension
   
3. TTS generation
   - Voice from registry (varies by channel)
   - Rate: -30%
   
4. Visual
   - Hand-drawn diagrams
   - Or black screen
   - Or simple graphics
   
5. Combine
   - Duration: 30-120 minutes per episode
   
6. Upload
   - Title: "[Topic] — [Episode]"
   - Series playlist
```

### Example: AGI Scenarios
```
Topic: What happens when AI surpasses us
Voice: V03 Lecturer (clear, precise)
Visual: Slow gradient or black screen

Script structure:
  1. Hook: "The singularity. The moment AI becomes smarter than humans."
  2. Context: "Right now, AI is narrow. It can do one thing well."
  3. The scenario: "But what happens when it can do everything well?"
  4. Implications: "Economics, society, consciousness..."
  5. Resolution: "Nobody knows. But we can think about it softly."
  6. Goodnight: "Sleep well."

Duration: 60-90 minutes
```
