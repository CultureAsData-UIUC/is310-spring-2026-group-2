# Steam Genre Popularity Over Time

This project analyzes how Steam game genres change over time using a cleaned Steam dataset from March 2025. The notebook prepares a reusable year‑by‑genre dataset so charts, subset comparisons, and interpretation of long‑term changes in Steam’s content mix can build on a consistent foundation.

## Project Overview

The project uses `games_march2025_cleaned.csv`, a cleaned dataset containing almost 85,000 Steam games and fields such as app ID, game name, release date, categories, genres, tags, estimated owners, and review activity. Because the dataset is broad and platform‑level, it is well suited for descriptive trend analysis across many years rather than a case study limited to a small number of games.

The central goal is to transform raw release and genre information into analysis‑ready files that support year‑based genre tracking. In practice, that means converting dates into release years, cleaning the genre field, expanding games into multiple game‑genre records when needed, and preparing outputs that can be reused in additional analyses.

## Files Included

- `01_genre_popularity_over_time.ipynb` — the main notebook for this project.
- `games_march2025_cleaned.csv` — cleaned Steam dataset used as the notebook input.
- `output/steam_games_year_genres_base.csv` — preprocessed base file with game IDs, names, release years, original genres, and parsed genre lists.
- `output/steam_games_genres_long.csv` — long‑format file where each row represents one game‑genre pair.
- `output/steam_genre_trends_by_year.csv` — yearly genre counts, yearly totals, and normalized genre proportions for visualization and comparison.
- `steamdb_data.txt` — a SteamDB‑style text file in the folder that is not part of the workflow for this project.

## Research Goal

This project is designed to answer a foundational descriptive question: how have Steam game genres shifted over time? The notebook approaches that question by building yearly genre counts and yearly genre proportions, which makes it possible to study whether a genre becomes more or less common across different periods.

Using proportions is especially important because the total number of games released on Steam changes dramatically over time. A genre’s raw count may rise simply because more games are released overall, while a proportion helps show whether the genre itself is taking up a larger or smaller share of the platform in a given year.

## Methods

The notebook follows a structured preprocessing workflow. It imports `pandas`, `ast`, and `Path`; loads the cleaned dataset; inspects relevant columns; parses release dates into datetime values; extracts a `release_year` variable; removes rows without usable years; converts the `genres` column from a string representation of a Python list into an actual list; explodes those lists into long format; calculates yearly genre counts; calculates yearly genre proportions; previews selected genres; and saves outputs for reuse.

This workflow turns raw metadata into a consistent analytical structure. Instead of leaving genres in their original string form, the notebook converts them into machine‑readable lists and then separates them so each game can contribute to every genre it belongs to.

## Manual and Computational Work

This project combines manual analytical decisions with computational processing. The manual work included defining the research question, deciding to focus on genre change over time, choosing `release_year` as the key time variable, deciding to compare proportions instead of only raw counts, and selecting genres such as Action, Adventure, RPG, Strategy, Simulation, Indie, and Casual for preliminary inspection.

The computational work was completed in Python using `pandas`, `ast`, and `Path`. The notebook automated the parsing of release dates, the creation of release years, the conversion of genre strings into real lists, the expansion of those lists into long format, the calculation of yearly counts and yearly proportions, and the export of reusable CSV files for further analysis.

This distinction matters because the notebook did not “discover” the project question by itself. The analytical framing, normalization choices, and interpretation goals were human decisions, while the code handled the repetitive and large‑scale preprocessing needed to apply those decisions consistently across almost 85,000 games.

## Data Processing Details

One of the most important technical steps is handling the `genres` column correctly. In the source data, genres are stored as string representations of Python lists, so the notebook converts them into actual list objects before analysis.

That converted genre field is then exploded into long format, where each row represents one game‑genre combination. This is important because many Steam games belong to multiple genres, and treating a combined genre list as a single label would distort counts and reduce analytical flexibility.

The notebook also creates a `release_year` field from parsed release dates. That standardization makes yearly aggregation possible and provides a consistent time axis for trend charts and comparisons.

## Outputs

The notebook saves three reusable outputs in the `output/` folder.

| File                              | Purpose                                                                                           |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `steam_games_year_genres_base.csv` | Stores preprocessed base data with IDs, names, release years, original genres, and parsed genre lists. |
| `steam_games_genres_long.csv`     | Stores one row per game‑genre combination for flexible aggregation and visualization.            |
| `steam_genre_trends_by_year.csv`  | Stores yearly genre counts, total games per year, and genre proportions for trend analysis.      |

Together, these files provide a complete, reusable foundation for describing how Steam genres have changed over time and for producing publication‑style charts and comparisons.

## In-Depth Analysis

By transforming release dates and genre labels into consistent yearly measures, the project creates a framework for asking whether visible changes in genre popularity reflect genuine shifts in Steam’s content mix or only the platform’s overall expansion. The resulting trend data can be used to identify periods where particular genres rise, fall, or remain stable.

The decision to calculate yearly proportions is central to that framework. Steam has grown substantially over time, so a genre’s increase in raw count does not automatically mean that the genre has become more dominant. A proportion‑based measure gives a better view of relative presence within each year and supports fairer comparisons across early and later periods.

The long‑format structure also improves analytical quality. Because a single title can belong to multiple genres, exploding the data ensures that Action, Adventure, RPG, Strategy, Simulation, Indie, Casual, and other genres are counted separately rather than being trapped inside combined labels. This makes charting and interpretation more accurate, especially when comparing broad genre families over long spans of time.

Another important point is scope. Since the source data includes almost 85,000 Steam games and many metadata fields, the project supports broad descriptive insights about Steam as a platform, but it does not test causal explanations for why genres rise or fall.

## Why This Project Matters

This project matters because good analysis depends on good structure. Before charts or comparisons can say anything meaningful, the underlying data has to be cleaned, normalized, and reshaped in a way that matches the research question.

It also highlights an important data science principle: preprocessing choices affect interpretation. Choosing proportions over only counts and exploding multi‑genre records both change what can be concluded from the data, so those preprocessing decisions are part of the analysis rather than just technical cleanup.

## Ethics and Privacy

This project uses game‑level platform metadata rather than personally identifying information about individual players, which keeps direct privacy risk relatively low. The analysis focuses on titles, genres, release timing, and aggregated platform characteristics instead of private user records. Even so, the dataset should be interpreted carefully. Fields such as estimated owners, tags, and review‑related activity are useful indicators, but they are still approximations and may reflect platform bias, tagging behavior, storefront conventions, or incomplete signals rather than exact measurements of player preference.

There are also ethical limits on interpretation. This project is descriptive, not judgmental: it aims to identify broad shifts in Steam genre composition over time, not to make claims about the value of specific developers, communities, or players based only on aggregated metadata.

## Limitations

This project is descriptive rather than causal. It shows what genres appear more or less frequently over time, but it does not explain why those shifts happened.

The dataset is also platform‑specific because it represents Steam rather than the full video game industry. In addition, because games can belong to multiple genres, total genre counts can exceed the number of unique games in a given year.

Another limitation is that the work here focuses on preparation and measurement more than visualization. The saved outputs make interpretation possible, but the strongest comparisons and narrative explanations will come from subsequent charts and statistical summaries built on these files.

## Scholarly Context

This project was informed by scholarship on video game genres, Steam metadata, and trend analysis over time. One especially relevant study is *Analyzing Video Game Trend Evolutions through Steam Tags*, which uses Steam tag data to study how game trends emerge, grow, and stabilize over time. That work helped frame this project as a time-based analysis of platform metadata, even though this project focuses on genres rather than tags.

This project was also shaped by Dominic Arsenault’s *Video Game Genre, Evolution and Innovation*, which argues that video game genres are not fixed categories and instead change through design innovation and technological development. That perspective was useful for thinking about genre as something that can shift historically rather than as a static label.

A third helpful source was *A Preliminary Network Analysis on Steam Game Tags: Another Way of Understanding Game Genres*, which shows how Steam’s classification systems can be studied computationally through relationships between tags and genres. That paper helped support the idea that Steam metadata can be treated as meaningful cultural data, while also reminding us that these categories are constructed and imperfect.

## Individual Data Essay and Dataset

This project is designed to function as both a dataset submission and a data essay. The dataset component consists of structured, reusable CSV outputs derived from the cleaned Steam source file, including a base file, a long-format game-genre file, and a yearly trend file with genre counts and normalized proportions.

The manual component of the dataset includes the research framing, the decision to analyze genre popularity over time, the choice to use `release_year` as the main time unit, and the decision to normalize genre frequency using yearly proportions rather than relying only on raw counts. The computational component includes parsing release dates, converting genre strings into list objects, exploding multi-genre records into long format, aggregating yearly counts, and producing reusable outputs at platform scale across almost 85,000 Steam games.

As a data essay, this project explains not only how the dataset was created, but also what the dataset represents, what it reveals, and what it conceals. It reveals broad shifts in Steam genre composition over time and creates a structured way to compare relative genre presence across years. At the same time, it conceals many aspects of game culture that are not fully captured by platform metadata alone, including player motivation, community meaning, design intent, and the social context behind genre labels.

This project also reflects on how computation shaped the dataset. Computational methods made it possible to process, restructure, and normalize a large platform dataset efficiently, but those methods also depended on human choices about what to count, how to define time, and how to interpret genre categories. Scale is therefore both a strength and a limitation: it allows broad platform-level analysis, but it can also flatten local nuance and obscure differences between individual games.

The project further addresses limitations, ethical considerations, and methodological lessons. Because the dataset is platform-specific and descriptive, it supports analysis of Steam as a marketplace and cultural platform without claiming to represent the entire game industry. It also highlights the importance of treating estimated ownership, tags, and other metadata fields as interpretive signals rather than perfect measures of cultural meaning or player behavior.

Taken together, the dataset and documentation show how cultural materials can be transformed into structured data while still requiring critical reflection. The project demonstrates how manual interpretation and computational processing work together in building a cultural dataset, and it situates that process as part of a broader scholarly effort to understand digital platforms, classification systems, and media circulation through data.


## References

- Arsenault, Dominic. “Video Game Genre, Evolution and Innovation.” *Eludamos: Journal for Computer Game Culture* 3, no. 2 (2009): 149–176.
- Grelier, Nicolas, Johannes Pfau, Nicolas Mathieu, and Stéphane Kaufmann. *From Fads to Classics: Analyzing Video Game Trend Evolutions through Steam Tags*. arXiv, 2025.
- Li, Xiaozhou, and Boyang Zhang. “A Preliminary Network Analysis on Steam Game Tags: Another Way of Understanding Game Genres.” In *Proceedings of the 23rd International Academic Mindtrek Conference*, 2020.