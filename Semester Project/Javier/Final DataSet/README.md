# Horror Games on Steam Dataset

## Project Overview

This project looks at how horror games are represented on Steam through store page tags and descriptions. My main goal was to understand how Steam organizes horror games and what those tags reveal about horror as a genre.

At first, horror seems like one simple category, but the dataset shows that horror games often overlap with many other labels, such as Atmospheric, Psychological Horror, Survival Horror, Action, Adventure, Story Rich, Multiplayer, Co-op, and Gore. Because of this, I treat horror as a flexible category instead of one fixed genre.

My original topic focused more broadly on video game genres and how they change over time. After reviewing the scope of the project, I narrowed the focus to horror games on Steam. I made this change because Steam tags gave me a clearer way to study how one platform organizes genre, mechanics, mood, and player experience. Instead of trying to study all genres across decades, I focused on one genre category, horror, and examined how it overlaps with tags like Atmospheric, Psychological Horror, Survival Horror, Action, Story Rich, Multiplayer, and Co-op.

This project still follows my original interest in genre and mechanics because it looks at how horror is built from repeated labels, moods, and gameplay patterns rather than treating horror as a fixed or natural category.

This project connects to my group’s larger theme of gaming as culture and data. Gaming is not only about playing games; it is also about how games are categorized, marketed, searched for, and understood through platforms like Steam.


## Research Question

My main research question is:

**How are horror games represented on Steam through tags and descriptions?**

I use this question to think about how Steam makes horror games searchable and organized, but also how tags can simplify what horror actually feels like as a player experience.

## Dataset Source

The data comes from public Steam store pages. I used Steam’s horror tag search page to collect games that were listed under the horror category.

The source was:

`https://store.steampowered.com/search/?tags=1667`

The tag ID `1667` is Steam’s horror tag. My web scraping script went through multiple Steam search result pages and collected links to individual game pages.

## Files Included

This folder includes the main files for my final project:

- `Scaled_Horror_Games.csv`
  The final scaled dataset of Steam horror games.

- `Steam_Horror_Scraper.py`
  The Python web scraping script used to collect the Steam horror game data.

- `Steam_Horror_Tag_Analysis.ipynb`
  A Jupyter notebook with basic analysis of the dataset, especially Steam tag counts.

- `Final_Essay.md`
  The final essay explaining how the dataset was made, what it represents, what it reveals and conceals, and how it connects to scholarly sources.

- `README.md`
  This documentation file explaining the dataset, method, files, limitations, and main takeaway.

## Dataset Structure

The final dataset is saved as:

`Scaled_Horror_Games.csv`

Each row represents one Steam horror game page. The dataset has four columns:

| Column | Description |
|---|---|
| `title` | The title of the Steam game. |
| `steam_url` | The URL for the game’s Steam store page. |
| `tags` | The Steam tags listed on the game page, separated by commas. |
| `description` | The short description/snippet from the Steam store page. |

## Methodology

I started this project with the idea of manually collecting Steam horror game pages and coding them based on features like survival, psychological horror, gore, atmosphere, and multiplayer gameplay. This helped me think about horror as something that needs interpretation, not just a simple label.

After that, I expanded the dataset using web scraping. I wrote a Python script that used:

- `requests`
- `BeautifulSoup`
- `pandas`
- `time`

The script first collected game links from Steam horror search result pages. Then it visited each game page and scraped the title, Steam URL, tags, and description. Finally, it saved the data into a CSV file.

This allowed me to move from a smaller manual idea to a larger scaled dataset.

## Manual and Computational Work

This project includes both manual and computational work.

The manual part was deciding what kind of data mattered. I had to think about what counts as horror, why Steam tags are useful, and what information from a store page could help answer my research question.

The computational part was the web scraping. The script helped me collect many more Steam horror game pages than I could have gathered manually. This made it easier to see larger patterns in the data.

However, computation did not remove the need for interpretation. The script could collect tags and descriptions, but it could not fully explain what horror means or how fear works in a game. I still had to interpret the patterns and think critically about what the dataset shows and what it leaves out.

## Analysis

In the notebook, I focused mostly on Steam tags because they are the clearest part of the dataset to compare.

The analysis includes:

### 1. Top Steam Tags

I counted the most common tags in the dataset. This helps show what labels appear most often alongside horror games.

This analysis supports the idea that horror overlaps with many other categories, such as:

- Singleplayer
- Atmospheric
- Adventure
- Action
- First-Person
- Psychological Horror
- Dark
- Story Rich
- Survival Horror

### 2. Horror-Related Styles and Themes

I also looked at tags that are more directly connected to horror style or mood, such as:

- Atmospheric
- Psychological Horror
- Dark
- Story Rich
- Survival Horror
- Gore
- Mystery
- Survival
- Violent
- Thriller

This helped me see that many horror games on Steam are marketed through atmosphere, story, darkness, survival, and emotional experience, not only through violence or gore.

### 3. Single-Player vs. Multiplayer/Co-op Horror

I compared tags related to play style:

- Singleplayer
- Multiplayer
- Co-op
- Online Co-Op

This helped me think about how horror can be presented as both an individual experience and a shared social experience. Many horror games are single-player, but multiplayer and co-op horror also appear in the dataset.

### 4. Broader Horror Categories

I also grouped related Steam tags into broader categories to get a clearer picture of how horror games are represented. These categories were based on my interpretation of the tags, so they are not perfect or official Steam categories. However, they help summarize the main patterns in the dataset.

The broader categories included:

- Mood / Atmosphere: Atmospheric, Dark, Mystery
- Psychological / Story: Psychological Horror, Story Rich
- Survival: Survival Horror, Survival
- Action / Combat: Action, Shooter, FPS, Gore, Violent
- Social / Multiplayer: Multiplayer, Co-op, Online Co-Op

This helped me see that horror games on Steam are not represented in only one way. Many games connect to mood and atmosphere, while others connect more to action, survival, story, or multiplayer gameplay.

## What the Dataset Represents

This dataset represents horror games as they appear on Steam store pages. It shows how horror games are categorized and marketed through platform tags and short descriptions.

The dataset does not represent every horror game ever made. It also does not represent exactly how players experience these games. Instead, it represents horror as organized by Steam’s platform structure.

## What the Dataset Reveals

The dataset reveals that horror on Steam is not one simple genre. Horror games are often hybrid games that overlap with other genres, styles, and mechanics.

Some horror games are atmospheric and story-based. Others are survival-focused, action-heavy, psychological, multiplayer, or co-op. This shows that horror on Steam is flexible and layered.

The dataset also reveals that Steam tags are useful because they allow one game to have multiple identities at once. A game can be Horror, Survival Horror, Atmospheric, and Story Rich all at the same time.

## What the Dataset Conceals

The dataset also leaves out important things.

It does not show what it actually feels like to play each game. Horror depends on sound, visuals, pacing, gameplay, story, and player reaction. A Steam tag can say “Horror” or “Psychological Horror,” but it cannot fully capture fear or atmosphere.

The dataset also does not show player reviews, sales, playtime, ratings, or actual reactions from players. Because of this, I cannot claim that these games actually scared players. I can only analyze how they are represented on Steam.

## Limitations

There are several limitations to this dataset:

1. **Steam search shapes the dataset**  
   The dataset depends on Steam’s horror tag search. If a game is not visible through that search, it may not appear in the dataset.

2. **Store pages are promotional**  
   Steam descriptions are designed to sell games, so they may exaggerate or simplify what the game is actually like.

3. **Scraping is not perfect**  
   Some rows may have missing values, unknown titles, or incomplete tag information.

4. **Tags are limited**  
   Tags are useful, but they cannot fully explain gameplay, emotion, or player experience.

5. **No release dates or review data**  
   Since the dataset only includes title, URL, tags, and description, I cannot analyze trends over time or compare player ratings.

## Ethics and Privacy

This project uses public Steam store pages. I did not collect private user information, player profiles, personal data, or private reviews.

The privacy risk is low because the dataset is based on public game pages. However, it is still important to remember that public platform data is not neutral. Steam decides what is searchable, visible, and easy to collect, so the dataset reflects Steam’s structure as much as it reflects horror gaming culture.

## Conclusion

The main takeaway from this project is that horror games on Steam are not represented as one simple category. Horror overlaps with atmosphere, story, survival, action, psychological tension, multiplayer gameplay, and co-op experiences.

The broader tag categories also showed that horror games often combine mood, survival, action, story, and social gameplay instead of fitting into only one category.

Steam tags make horror games searchable and organized, but they also simplify the experience. The dataset is useful for seeing patterns in how horror games are represented, but it cannot fully capture what it feels like to actually play a horror game.