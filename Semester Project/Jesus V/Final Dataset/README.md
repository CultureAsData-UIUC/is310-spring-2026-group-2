# Final Dataset: Esports Earnings and Competitive Gaming

## Overview

This dataset explores esports earnings and competitive gaming as a way to understand how digital entertainment becomes professionalized and unequal over time. It combines both manually curated data and computationally generated data to analyze patterns in prize pools, tournaments, and player participation.

The dataset builds on an initial bespoke dataset of 75 games and expands it using larger datasets and computational methods.

---

## Data Sources

The dataset is based on two main sources:

- https://www.kaggle.com/datasets/rankirsh/esports-earnings  
- https://www.esportsearnings.com/

These sources include data on esports games, total earnings, number of players, and tournament history.

---

## Dataset Structure

This project produces three main datasets:

### 1. Game-Level Dataset
File: `Final_Esports_Game_Level_Dataset.csv`

Each row represents a game and includes:

| Field | Description |
|------|-------------|
| Game | Name of the game |
| ReleaseDate | Year the game was released |
| Genre | Genre of the game |
| TotalEarnings | Total prize money earned |
| TotalPlayers | Number of players |
| TotalTournaments | Number of tournaments |
| EarningsPerPlayer | Average earnings per player |
| EarningsPerTournament | Average earnings per tournament |
| Tier | Competitive level of the game |
| AuditFlag | Result of dataset verification |
| ProfessionalizationScore | Combined measure of esports development |
| InequalityFlag | Indicates player earning inequality |

---

### 2. Yearly Historical Dataset
File: `Final_Esports_Historical_Yearly_Dataset.csv`

Each row represents a year:

| Field | Description |
|------|-------------|
| Year | Year of esports activity |
| YearlyEarnings | Total earnings that year |
| YearlyPlayers | Total players that year |
| YearlyTournaments | Total tournaments that year |
| CumulativeEarnings | Total earnings over time |

---

### 3. Genre Summary Dataset
File: `Final_Esports_Genre_Summary.csv`

Each row represents a genre:

| Field | Description |
|------|-------------|
| Genre | Game genre |
| Games | Number of games |
| TotalEarnings | Total earnings for genre |
| AverageEarningsPerPlayer | Avg earnings per player |
| AverageEarningsPerTournament | Avg earnings per tournament |

---

## Methodology

### Initial Dataset

The project began with a manually curated dataset of 75 games selected using a genre-balanced sampling approach. This process required interpretive decisions about what to include and how to categorize games.

### Audit Process

The dataset was verified by comparing sample entries to publicly available esports records. This helped identify inconsistencies, outdated values, and missing data, especially in early esports history.

### Computational Scaling

The dataset was expanded using Python and Pandas. Additional fields were calculated, and multiple datasets were merged to create a more complete representation of esports.

---

## Analytical Features

New variables were created to better understand esports as a system:

- **EarningsPerPlayer**: shows inequality between players  
- **EarningsPerTournament**: reflects tournament value  
- **Tier**: categorizes games by scale and importance  
- **ProfessionalizationScore**: measures long-term esports development  
- **AuditFlag**: highlights data reliability  

These variables allow for deeper analysis beyond simple totals.

---

## Visualizations

The dataset includes several visualizations:

- Top games by total earnings  
- Earnings per player (inequality)  
- Earnings per tournament  
- Earnings over time  
- Genre comparisons  
- Tier distribution  

These help illustrate patterns in esports growth and structure.

---

## Limitations

- Early esports data is incomplete  
- Smaller tournaments may not be recorded  
- Some values may be outdated  
- Certain variables involve interpretation (such as Tier)  

The dataset represents a constructed view of esports rather than a complete record.

---

## Summary

This dataset demonstrates how cultural data is created, interpreted, and scaled. It shows that esports is not just growing, but becoming structured and unequal, with a small number of dominant games shaping the industry.