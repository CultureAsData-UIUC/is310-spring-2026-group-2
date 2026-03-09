# Initial Dataset: Esports Earnings and Competitive Gaming

## Cultural Materials

This dataset focuses on **esports earnings and competitive gaming**. Competitive video games represent a major form of digital culture where players compete in organized tournaments for prize money. These tournaments produce records about games, players, tournaments, and total earnings.

I chose esports as my cultural focus because competitive gaming has grown into a global industry and reflects how digital entertainment becomes professionalized and monetized. Esports also generates large amounts of structured data that can be analyzed to understand patterns of competition, popularity, and economic growth in gaming.

---

## Approach

For this assignment I used the **Audit and Augment Existing Data approach**.

I began with an existing esports dataset that contains information about many games, including total earnings, number of players, and number of tournaments. Instead of simply reusing the dataset, I created a **bespoke dataset of 75 games** and augmented the data with additional interpretive metadata.

My dataset includes new fields such as:

- `RegionPopularity`
- `CompetitiveLevel`
- `Notes`

These additions help capture cultural context about the esports scene that is not included in the original dataset.

---

## Computational Tools

Several computational tools helped assist the process.

I used **Python and the Pandas library** to load and analyze the original dataset and generate a balanced sample of approximately 75 games. The code helped select entries across different genres so the dataset would not be dominated by a single type of game.

Python was also used to automatically generate some metadata fields such as `CompetitiveLevel` based on tournament counts and total earnings. However, the dataset still required interpretive decisions when categorizing games and reviewing the entries.

These tools helped organize and structure the data, but they did not replace the manual decisions involved in building the dataset.

---

## Interpretive Decisions

Creating this dataset required several interpretive choices.

First, I decided to select **75 games** from the larger dataset in order to create a manageable dataset for close analysis. I used a **genre-balanced sampling method** so that the dataset would represent a variety of esports genres rather than focusing only on the highest earning games.

Second, I introduced new interpretive categories such as `RegionPopularity` to reflect the relative importance of different games within esports culture. Games with large prize pools or many tournaments were labeled as high competitiveness, while smaller esports scenes were categorized as medium or low.

Finally, I added contextual notes for each entry to capture additional observations about the game’s esports presence.

These decisions illustrate how datasets are shaped by interpretive choices made during data creation.

---

## Challenges

One challenge was that the original dataset lacked some cultural metadata that would help interpret esports as a phenomenon. For example, the dataset did not clearly describe how important each game is within competitive gaming.

Another challenge involved determining how to classify certain games, since esports scenes can change over time and different regions may emphasize different titles.

These challenges highlight the importance of transparency when creating datasets.

---

## Observations

Working closely with the data revealed several patterns.

First, a relatively small number of genres dominate esports competition, particularly **first-person shooters, strategy games, and multiplayer online battle arena games**.

Second, the dataset shows that many successful esports titles are supported by large game publishers that actively organize tournaments and professional leagues.

Finally, the data reflects the **global nature of esports**, with strong competitive scenes across North America, Europe, and East Asia.

---

## Next Steps (Scaling Plan)

After Spring Break, I plan to scale the dataset using computational methods.

One possible approach is to merge the bespoke dataset with the larger esports dataset and automatically classify additional games using Python. This would allow the dataset to expand to several hundred or even thousands of entries.

I could also use web scraping or APIs to collect updated tournament and earnings data from esports statistics websites.

Scaling the dataset will make it possible to analyze broader trends in esports while also demonstrating how automated data collection changes the interpretive process compared to manually creating a small dataset.

---

## Repository Structure

```
Initial Dataset/
│
├── esports_games_bespoke.csv
├── GeneralEsportData.csv
├── Cleaning_initial_Esports_Data.py
└── README.md
```

This repository contains the bespoke dataset, the original dataset used for sampling, and the Python script used to generate the dataset.