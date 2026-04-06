# Esports Earnings Dataset (Audit and Augment Project)

## Overview

This project explores esports earnings and competitive gaming as a way to understand how digital entertainment becomes professionalized and monetized over time. Rather than treating earnings as simple numbers, this dataset looks at how certain games gain dominance, visibility, and long-term investment within esports culture.

This project follows an **Audit and Augment** approach. I began with an existing dataset and then added new fields to better capture cultural meaning and patterns that were not originally included.

---

## Dataset Source

The base dataset used in this project is:

https://www.kaggle.com/datasets/rankirsh/esports-earnings

This dataset includes information on esports games such as:

- total earnings
- number of players
- number of tournaments

It represents competitive gaming activity from approximately 1998 to 2023.

---

## Data Verification (Audit Step)

As part of the audit process, I traced the dataset back to its likely source and verified a sample of entries.

The dataset is derived from publicly available esports records:

https://www.esportsearnings.com/

To verify accuracy, I selected several major games, such as Dota 2, Counter-Strike, and League of Legends, and compared their total earnings, tournament counts, and player counts with the values reported on the website.

I found that most values closely matched the publicly available source data. However, there are still limitations:

- some values may be slightly outdated depending on when the dataset was compiled
- early esports data from the late 1990s and early 2000s is less complete
- smaller regional tournaments may not be fully represented

This shows that the dataset is not a perfect record, but a constructed and partial version of esports history.

---

## Augmentation Process

To move beyond basic description, I created new calculated fields and interpretive categories using Python and Pandas.

### New Fields Added

- `EarningsPerPlayer`: measures how much each player earns on average
- `EarningsPerTournament`: shows how valuable each tournament is on average
- `Tier`: groups games into different competitive levels based on total earnings
- `RegionPopularity`: identifies where the game has its strongest competitive presence
- `Notes`: adds brief context about the game’s esports significance

These additions help the dataset move beyond basic totals and toward a more meaningful analysis of esports as a professional system.

---

## Sampling Method

I created a **genre-balanced sample of 75 games** from the original dataset. Instead of only selecting the highest-earning titles, I sampled games across different genres so the dataset would better represent the variety of esports.

This was an important interpretive decision because a sample based only on top earnings would overrepresent a small number of already dominant games. A genre-balanced sample allowed me to create a more useful dataset for cultural analysis while still keeping the project manageable.

---

## Dataset Fields

| Field Name | Data Type | Description | Example |
|---|---|---|---|
| `Game` | string | Name of the game | `Dota 2` |
| `ReleaseDate` | integer | Year the game was released | `2013` |
| `Genre` | string | Genre of the game | `MOBA` |
| `TotalEarnings` | float | Total prize money earned | `300000000` |
| `TotalPlayers` | integer | Number of players in the dataset | `4000` |
| `TotalTournaments` | integer | Number of tournaments recorded | `1200` |
| `EarningsPerPlayer` | float | Average earnings per player | `75000` |
| `EarningsPerTournament` | float | Average earnings per tournament | `250000` |
| `Tier` | string | Competitive level based on earnings | `Tier 1 (Elite)` |
| `RegionPopularity` | string | Main regional popularity of the game | `Global` |
| `Notes` | string | Short cultural or competitive note | `One of the most dominant esports by prize money` |

---

## Project Focus

This project examines how esports has developed into a professional and unequal competitive system.

Rather than just tracking total earnings, this dataset focuses on how value is distributed across games, players, and tournaments. By analyzing metrics like earnings per player and earnings per tournament, this project explores:

- which games create stronger economic opportunities for players
- how wealth is concentrated in certain esports
- how competitive gaming has evolved into a structured global industry

This approach treats esports not just as entertainment, but as a cultural and economic system shaped by visibility, investment, and access.

---

## Key Observations

Working closely with the dataset revealed several patterns:

- a small number of games dominate total earnings, showing strong inequality across esports
- some games have high total earnings but much lower earnings per player, suggesting uneven distribution
- tournament value varies widely across games, showing that different esports are structured very differently
- top-tier esports maintain long-term dominance, while smaller games struggle to grow

These patterns show that esports is not just growing, but becoming stratified, with clear divisions between elite and lower-tier competitive scenes.

---

## Challenges

Several challenges came up during this process:

- the original dataset did not include much documentation about how it was compiled
- early esports history is harder to verify than recent data
- assigning regional popularity involved interpretation and simplification
- adding categories always risks flattening more complex cultural realities

These challenges reinforced the importance of transparency in data creation and reuse.

---

## Visualizations

To better understand patterns in the dataset, I created visualizations using Python and matplotlib.

The first visualization shows the top 10 esports games by total earnings, making the concentration of money in a small number of games easy to see.

The second visualization shows the top 10 games by earnings per player, which highlights inequality and shows that high total earnings do not always mean broad player benefit.

The third visualization shows the top 10 games by earnings per tournament, which helps compare the structure and scale of competitions across different esports.

These visualizations help move the dataset from raw numbers to more interpretable cultural insights.

---

## Next Steps

In the next stage of this project, I plan to expand the dataset and focus more directly on inequality and professionalization in esports.

Future work will include:

- scaling the dataset using APIs or web scraping
- comparing top-earning games to lower-tier games
- analyzing how prize pools change over time
- combining this dataset with additional sources for deeper analysis of region, genre, and publisher influence

This will help move from a small handcrafted dataset toward a broader and more interpretive analysis of esports as a cultural system.

---

## Repository Structure

```text
Initial Dataset/
│
├── Bespoke_Esports_Dataset.csv
├── GeneralEsportData.csv
├── Cleaning_initial_Esports_Data.py
├── top_10_total_earnings.png
├── top_10_earnings_per_player.png
├── top_10_earnings_per_tournament.png
└── README.md
```

---

## Reflection

This project showed me that data is not neutral. Even when starting with an existing dataset, I still had to make decisions about sampling, verification, categorization, and interpretation.

By auditing and augmenting this dataset, I learned that making data is not just a technical task. It is also an interpretive process that shapes what kinds of cultural stories the data can tell.