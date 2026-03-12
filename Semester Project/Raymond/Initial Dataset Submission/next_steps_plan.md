# Next Steps Plan

## Goal after Spring Break
Scale this bespoke dataset from **84 curated records** to **500–1,000+ records** so I can analyze historical change in mainstream game design more systematically.

## Research direction
A larger version of this dataset could support questions like:
- Which genres are most likely to become mainstream in different decades?
- When do critic prestige, commercial success, and cultural impact overlap?
- Do certain platforms favor certain genres?
- How did gaming shift from arcade/console products to online ecosystems and live-service models?
- What periods show the fastest genre diversification?

## Scaling strategy
### Option 1: Scale up through automation
I would expand the dataset by collecting many more games from:
- Wikipedia lists of best-selling games and platform-specific sales pages
- Game award archives
- critic-ranking lists
- game databases such as IGDB / RAWG / MobyGames (if accessible)
- storefront metadata where legally and technically appropriate

### Possible computational methods
- Web scraping of structured list pages
- API collection for metadata like genres, platforms, developers, and release dates
- Pattern matching and entity normalization for platform/genre labels
- LLM-assisted cleaning to map messy genre labels into a smaller controlled vocabulary
- Deduplication logic for ports, remasters, and duplicate titles

## What would change at scale?
At 84 items, I can make almost every interpretive decision by hand.  
At 1,000 items, I would need to automate:
- title matching
- genre normalization
- platform normalization
- developer/publisher normalization
- deciding whether remasters/ports count as the same game

That means the project would shift from **close reading and hand curation** to **rule-based and model-assisted abstraction**.

## Anticipated technical challenges
- Duplicate titles across platforms and editions
- Conflicting release years between sources
- Genre labels that are too broad or too specific
- Distinguishing full games from expansions, remasters, and bundles
- Bias toward games with better online documentation
- Pages that block scraping or change structure over time

## Anticipated interpretive challenges
- “Mainstream” may become too dependent on what data is easiest to collect
- Sales-heavy sources may overvalue blockbuster console titles
- Critic lists may overrepresent prestige and underrepresent casual/mobile play
- Recent games may appear more important than they ultimately prove to be
- Regional differences in popularity may be flattened into a single global dataset

## Proposed additions to the schema
For the scaled version, I would add:
- franchise
- series installment number
- region of origin
- multiplayer / single-player / hybrid
- online / offline
- monetization model
- critic score
- award count
- sales estimate (if available)
- source confidence / provenance notes

## Why this scaling plan matters for the course
This next phase would let me test exactly what the assignment is asking:
- Which interpretive decisions can be automated?
- Which decisions become more fragile at scale?
- What kinds of distortion appear when culture is turned into larger, machine-readable data?

In other words, the scaled dataset would not just answer a gaming question. It would also show how **scale transforms cultural data work itself**.