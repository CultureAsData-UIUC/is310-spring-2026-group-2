# Mainstream Video Games Dataset (1978–2025)

## Project summary
This dataset contains **84 curated video game records** spanning from **1978 to 2025**. It was designed as a **small bespoke dataset** for an initial humanities/data assignment rather than an exhaustive census of every popular game ever made.

The organizing idea is simple: **which games became "mainstream" enough to matter historically, commercially, or culturally?**  
To answer that question, I built a sample that mixes:
- blockbuster best-sellers
- critically canonical titles
- award winners
- esports and live-service titles
- mobile or social phenomena that reached broad public visibility

## Why this topic?
Video games are a strong cultural-data topic because they let you study several overlapping questions:
- How have dominant genres changed over time?
- What kinds of games become mass-market successes?
- When do critics, sales, and cultural visibility align — and when do they diverge?
- How did the medium move from arcade hits to console blockbusters, online competitive games, and live-service ecosystems?

This topic is also good for later scaling because it can be expanded using APIs, web scraping, store metadata, review data, and award archives.

## Approach
**Approach used:** Create Data from Scratch (with computational assistance)

I did **not** simply download a ready-made dataset and submit it as-is. Instead, I manually selected and normalized records using web research and computational organization. The dataset is therefore interpretive by design.

## What counts as “mainstream” in this dataset?
A game was eligible for inclusion if it met **at least one** of these criteria:
1. It appears on a major **best-selling games** list.
2. It appears on a well-known **“best games” / all-time critical canon** list.
3. It won or strongly aligns with major **Game of the Year** recognition.
4. It had outsized **cultural impact**, such as defining esports, mobile play, live-service play, or pandemic-era social play.

Because "mainstream" is not a neutral category, this dataset treats it as an **interpretive label** rather than a purely objective fact.

## Fields
- `id`: row id
- `title`: game title
- `release_year`: initial release year used for consistency
- `decade`: decade bucket for easier period analysis
- `primary_genre`: one normalized genre label
- `subgenre`: more specific descriptive genre/mode
- `primary_platform`: one lead platform or platform grouping
- `developer`: lead developer/studio
- `publisher`: lead publisher
- `mainstream_signal`: the main reason(s) for inclusion
- `inclusion_reason`: short human-readable rationale
- `discovery_source`: the source list used to help identify the title

## Computational tools used
- Web search and source comparison to identify candidate games
- Python / spreadsheet-style normalization to structure records consistently
- Manual review to decide:
  - which titles to include
  - which year to use
  - how to collapse multi-genre games into one primary genre
  - how to represent cross-platform releases

## Key interpretive decisions
### 1. This is a **curated sample**, not a full universe
The original idea of “all mainstream games from the 20th century to now” is too large and too unstable for a 50–100 item assignment. So I turned it into a **defensible sample of 84 titles**.

### 2. I used the **initial release year**
Many games have ports, remasters, re-releases, deluxe editions, and platform migrations. To avoid chaos, I used the **initial release year** as the standard year whenever possible.

### 3. I assigned **one primary genre**
Many games could fit 2–4 genres. For example, *Breath of the Wild* could be tagged as action, open-world, adventure, and RPG-adjacent. I forced each entry into **one primary genre** and one supporting subgenre so the dataset stays analyzable.

### 4. I allowed more than sales to define mainstreamness
Some culturally dominant games are not best captured by boxed sales alone. Titles like *League of Legends*, *Dota 2*, *Fortnite*, *Among Us*, and *Pokémon GO* matter because of **player attention, public discourse, and platform reach**, not just traditional unit sales.

### 5. I intentionally kept a cross-era mix
The dataset includes arcade, console, PC, mobile, esports, indie breakout, and live-service titles to make later comparisons more meaningful.

## Exclusions
To keep the dataset manageable, I generally excluded:
- annual sports/franchise iterations unless historically exceptional
- DLC and expansions as separate entries
- remasters/remakes unless treated as distinct mainstream phenomena
- very niche cult classics without broad historical or public visibility
- duplicate entries for the same core game across multiple platforms

## Limitations
This dataset has several important limitations:
- It is **not exhaustive**
- “Mainstream” is culturally biased toward highly visible global markets
- English-language source discovery tends to privilege North American, Japanese, and European gaming histories
- Genre labels flatten games that are inherently hybrid
- Sales, awards, and cultural influence do not always measure the same thing
- Recent games are harder to stabilize because their long-term historical position is still forming

## Early patterns already visible
Even before deeper analysis, a few patterns show up:
- Early mainstream games lean heavily toward **arcade, platformer, puzzle, and early action-adventure**
- The 2000s and 2010s show the rise of **open-world action** and **prestige blockbuster design**
- PC-driven mainstreamness often appears through **strategy, shooters, MMOs, and esports**
- The 2010s onward show the importance of **live-service**, **mobile reach**, and **social play**
- RPGs become especially visible in the 2010s–2020s, suggesting a strong relationship between scope, prestige, and mainstream attention

## Suggested repository structure
```text
data/
  mainstream_video_games_dataset.csv

docs/
  dataset_documentation.md
  next_steps_plan.md
```

## Source lists used for discovery
- Best-selling games: https://en.wikipedia.org/wiki/List_of_best-selling_video_games
- Best-selling PC games: https://en.wikipedia.org/wiki/List_of_best-selling_PC_games
- Best-selling Nintendo Switch games: https://en.wikipedia.org/wiki/List_of_best-selling_Nintendo_Switch_video_games
- Games listed among the best: https://en.wikipedia.org/wiki/List_of_video_games_listed_among_the_best
- Game Awards GOTY page: https://thegameawards.com/winners/game-of-the-year