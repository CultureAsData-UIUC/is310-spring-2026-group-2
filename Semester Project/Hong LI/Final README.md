# Roguelike and Roguelite Games on IGDB: What Metadata Can Tell Us

## Introduction

For this project, I created a dataset about roguelike and roguelite games collected from the IGDB (Internet Game Database) API. I chose this topic because my group's overall theme is gaming as culture and data. Our group examined video games not simply as entertainment products, but as cultural objects that are categorized, labeled, and understood through platforms and databases. My project fits into that theme because roguelike games are more than a mechanical genre. They are a set of design ideas that have evolved, expanded, and split into sub-categories over decades of game development.

How have roguelike and roguelite games developed over time, and how have their gameplay forms integrated systems? At first, roguelike seems like a straightforward label. But once I began building the dataset, I realized the category is much more complicated. Some games strictly follow the original roguelike formula. Others borrow only certain elements and are labeled roguelite. Many games carry both tags at once. The boundary between the two is not fixed.


## Dataset Overview

I built a dataset of roguelike and roguelite games collected through the IGDB API. Each row in the dataset represents one game. The final dataset includes the following columns: Name, Release Date, Rating, Genre(s), Platform(s), Theme(s), Keywords, Developer(s), Player Perspective, and Game Mode(s).

The Name and Release Date columns identify each game and place it in time. The Rating column reflects aggregated critic and user scores as recorded on IGDB. The Genre(s) and Theme(s) columns show the broader categorical labels attached to each game. The Platform(s) column records which systems each game was released on. The Keywords column is particularly important because it captures community- and editor-applied tags, including the roguelike and roguelite labels themselves. The Developer(s), Player Perspective, and Game Mode(s) columns provide additional context about how each game was made and how it is played.

This dataset is not simply a list of games. It is a record of how IGDB represents and organizes a genre category. The cultural material I studied was IGDB metadata, which combines editorial classification, developer input, and community contribution into a structured database.

## How I Made the Dataset

I collected the data using the IGDB API with Python. The process was not straightforward. IGDB's keyword system uses numeric IDs rather than plain text search, so I first had to identify the correct IDs for the roguelike (ID: 416) and roguelite (ID: 17292) keywords by querying the keywords endpoint directly. This step required multiple rounds of debugging, including discovering that IGDB does not support text search on the keywords endpoint and that array-matching syntax behaves differently from what standard SQL logic would suggest.

Once I confirmed the correct keyword IDs, I wrote a paginated query that retrieved all games tagged with either keyword, requesting fields including name, release date, rating, genres, platforms, themes, keywords, involved companies, player perspectives, and game modes. I used offset-based pagination with a limit of 500 results per request and added delays between calls to avoid rate limiting. The final dataset was saved as a CSV file.



## What the Dataset Represents

The dataset represents roguelike and roguelite games as they are recorded in IGDB's database. It does not represent every game that players would consider part of the genre, and it does not represent the full experience of playing these games. Instead, it represents a specific view of the genre as organized through IGDB's keyword and metadata system.

This distinction matters because IGDB is not a neutral archive. It is a structured database shaped by editorial choices, contributor behavior, and API design. Games that are missing keywords, have incomplete metadata, or were never added to IGDB will not appear in the dataset. The dataset therefore reflects IGDB's coverage and classification practices as much as it reflects the genre itself.

The dataset also shows that roguelike is a hybrid category. Many games in the dataset carry both the roguelike and roguelite keywords simultaneously, alongside other keywords such as dungeon crawler, permadeath, procedural generation, and bullet hell. This overlap suggests that the genre is understood through combinations of features rather than a single fixed definition.

## What the Dataset Reveals

The dataset reveals several patterns in how roguelike and roguelite games have developed and spread.

One pattern is growth over time. The release date column shows that the number of games tagged as roguelike or roguelite increased significantly in the 2010s and continued growing into the 2020s. This matches broader trends in independent game development, where the accessibility of game engines and digital distribution platforms made it easier for small teams to release games inspired by classic roguelike design.

Another pattern is platform distribution. While many games in the dataset appear on PC, a significant number have also been released on consoles and mobile platforms. This suggests that roguelike mechanics have moved beyond their origins as a PC-exclusive genre and have been adapted for a wider range of devices and player contexts.


## What the Dataset Conceals

The dataset also hides a significant amount of information. In particular, it does not reveal the process behind keyword assignment. Although IGDB keywords can be added by editors and contributors, the dataset does not indicate who applied each tag, when it was added, or whether there was any disagreement about the classification. As a result, one game might be labeled as “roguelite” by one contributor and “roguelike” by another, but these differences in interpretation are not visible in the final dataset.

Additionally, the dataset conceals games that were never added to IGDB, games with incomplete records, and games that players consider part of the genre but that lack the relevant keywords. The dataset is bounded by what IGDB contains and how its contributors have labeled things.

## The Role of Computation

Computation was essential to this project. Without the API and automated pagination, collecting data on hundreds of games would have been impractical. The Python script allowed me to send structured queries, handle errors and rate limits, and save results in a consistent format.

At the same time, computation did not do the interpretive work. The script could retrieve fields, but it could not explain what those fields meant or why the genre boundaries are drawn where they are. Deciding that roguelike and roguelite were the right keywords to search for, understanding why certain queries returned zero results, and making sense of overlapping tags all required human judgment. Computational methods scaled the data collection, but interpretation remained a separate and necessary step.

## How Scale Shaped the Dataset

Scaling the project through the API made it possible to see patterns across a large number of games rather than just a small selection. Broad trends in release dates, platform coverage, and genre overlap became visible only because the dataset included enough games to make those patterns meaningful.

However, scale also introduced limitations. With a larger dataset, individual games become rows rather than objects of close attention. Details that might matter in a careful reading of one game's page, such as the specific way its description frames the roguelike mechanics, are lost when data is collected at scale. The dataset shows the shape of the genre across many games, but it flattens the differences between them.

## Limitations and Qualifications

Several limitations apply to this dataset. First, it depends entirely on IGDB's coverage and keyword system. Games not in IGDB, or games without the roguelike or roguelite keywords, will not appear. Second, many records have incomplete fields. Ratings, genres, themes, and developer information are missing for a portion of the dataset, which means any analysis of those fields applies only to the subset of games with complete data. Third, the keyword system reflects contributor behavior over time, which may be inconsistent. Fourth, the dataset does not include player reviews, sales figures, playtime, or any direct measure of how these games were received or experienced.

## Conclusion

This project shows that roguelike and roguelite as genre categories are not fixed or stable. They are flexible labels applied across a wide range of games, platforms, and time periods. The IGDB dataset reveals how the genre has grown over time and spread across platforms, but it also shows how much is left out when a game's identity is reduced to metadata fields.

Data can reveal patterns in culture, but it cannot capture culture completely. IGDB can turn a roguelike game into a set of keywords, ratings, and platform names, and I can turn those records into a dataset. But what makes a roguelike game meaningful to a player — the tension, the randomness, the cycle of loss and improvement — is still more complex than anything that fits in a spreadsheet.