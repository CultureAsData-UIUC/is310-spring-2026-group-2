
## Initial documentation

This project looks into how AI-related games on Steam stand out from other games regarding genres and metadata, and if we can predict AI-related content based on tags and descriptions. We consider Steam games as digital cultural artifacts, where the store metadata—like release dates, genres, tags, and popularity metrics—shows how developers and platforms present AI to players. We kick things off with a large, cleaned Steam dataset (games_march2025_cleaned.csv) that compiles info on thousands of games, including appid, name, release date, genres, tags, price, owners, and playtime stats. Instead of viewing this dataset as unbiased, we review and enhance it by cross-referencing each game's appid with SteamDB's AI-focused tags, such as 'AI Content Disclosed' (for games whose developers have revealed the use of generative AI on Steam) and the 'Artificial Intelligence' gameplay tag. Our initial custom dataset includes about 75 games taken from this file: a selected group of AI-tagged titles and genre-matched comparison games lacking AI tags, each marked with a derived AI_related label and notes on how AI is represented (or not) in its store listing.

## Initial Dataset

I will be working with PC games released on Steam, as represented in games_march2025_cleaned.csv. Each row in this file corresponds to a Steam application and includes structured fields such as:

appid, name
release_date and required_age
price, dlc_count
categories, genres
tags (stored as a dictionary of tag names and counts)
popularity and engagement metrics such as estimated_owners, peak_ccu, num_reviews_total, and playtime summaries, etc.

I would treat this metadata as a cultural lens on how games are positioned and perceived (e.g., via genres and tags like “Action”, “Simulation”, “Multiplayer”), and focus specifically on how AI is surfaced through tags and disclosures.

Some key points to consider:
- Prioritize releases between roughly 2015 and March 2025, where AI and generative AI have become more salient in game marketing.

- Focus on a subset of widely represented genres (e.g., Action, Strategy, RPG, Simulation, Indie) to make comparisons meaningful.

## Approach
I am not collecting data from scratch, instead, I will audit and enrich an existing dataset:

- Use games_march2025_cleaned.csv as our base “canonical” Steam metadata, taking advantage of its standardized columns (appid, genres, tags, owners, playtime, etc.).

- Audit and enrich this base by adding an AI‑related label, derived from SteamDB’s AI‑specific tags:

    - SteamDB exposes an “AI Content Disclosed” tag that aggregates games where developers have filled out Valve’s generative AI disclosure on their store pages.

    - SteamDB also has an “Artificial Intelligence” tag that marks games where AI is a core gameplay theme.

Cross‑reference these SteamDB tag lists with the appids from games_march2025_cleaned.csv to create new fields in our bespoke subset:

- steamdb_ai_content_disclosed (1/0)

- steamdb_ai_gameplay_tag (1/0)

- AI_related (1 if either of the above is 1; 0 otherwise)

Our initial 75‑game subset is built by selecting a set of AI‑related games (where AI_related = 1) from the cleaned file and pairing each with at least one non‑AI comparison game from similar genres and release periods (AI_related = 0).

## Computational tools and limitations

- Using games_march2025_cleaned.csv as the primary data source, loaded into tools like Python (pandas) or spreadsheet software for filtering and sampling.

- The SteamDB web interface and tag pages (e.g., “AI Content Disclosed”, “Artificial Intelligence”) to identify AI‑tagged appids and manually or semi‑automatically map them to entries in the cleaned dataset.

#Limitations:

- SteamDB’s “AI Content Disclosed” tag is based on developers’ self‑reported use of generative AI; games that use AI but are not disclosed or not yet tagged will be invisible to this method.

- The “Artificial Intelligence” gameplay tag may indicate traditional AI behaviors (e.g., enemy AI) rather than generative AI tools in production; grouping these under one AI_related label mixes different meanings of “AI”.

- games_march2025_cleaned.csv is itself a snapshot as of March 2025, so it captures a particular historical moment in the AI‑in‑games discourse; later shifts in disclosure practices won’t be reflected.


## Definition of 'AI_related':
i assigned AI_related = 1 to a game if it meets at least one of these criteria:

Its appid appears under SteamDB’s “AI Content Disclosed” tag (indicating some form of generative AI used in art, audio, or code, as disclosed to Valve).

Its appid appears under SteamDB’s “Artificial Intelligence” tag, and we judge, from its name/description in the cleaned dataset, that AI is a central thematic or gameplay element.

All other games in our initial subset are labeled AI_related = 0.

Though some challenges we may encounter:
- Some AI‑using games may not disclose their AI use or may not yet be tagged on SteamDB, which means they will be mis‑classified as non‑AI in our scheme.

- Games with highly ambiguous descriptions force us to decide whether to include them as AI‑related or not, and we record these edge cases in brief notes fields in the bespoke dataset.

## Scaling Plan (Using games_march2025_cleaned.csv)

- Develop a script to gather or parse lists of appids associated with SteamDB’s “AI Content Disclosed” and “Artificial Intelligence” tags and join them against the full games_march2025_cleaned.csv by appid, populating steamdb_ai_content_disclosed, steamdb_ai_gameplay_tag, and AI_related for hundreds or thousands of rows.

- At scale, we lose the ability to individually read each game’s description so, i'll rely heavily on how SteamDB and the cleaned dataset tokenize genres, tags, and owners, which may embed their own biases and omissions.

- I also anticipate inconsistencies in AI tagging (e.g., games added after March 2025, late disclosures, or changing tag usage) and will need to document gaps where our labels likely under‑ or over‑estimate AI involvement.