# Final Dataset: RPG Genre Evolution and Temporal Analysis (1994-2023)

## Overview

This dataset explores how the Role-Playing Game (RPG) genre has evolved over nearly 30 years, tracking changes in genre combinations, player perspectives, themes, and game design patterns. It combines both manually curated data and computationally generated data to analyze patterns in how RPGs are classified and how those classifications have shifted over time.

The dataset builds on an initial bespoke dataset of 50 games and expands it using the IGDB API and computational methods.

---

## Data Sources

The dataset is based on two main sources:

- https://www.igdb.com/ (Internet Games Database)
- Manual research via Steam and Wikipedia for cross-reference

IGDB is owned by Twitch/Amazon and contains metadata on video games including genres, themes, release dates, platforms, and player perspectives.

---

## Dataset Structure

This project produces three main datasets:

### 1. Game-Level Dataset
File: `Final_RPG_Game_Level_Dataset.csv`

Each row represents a game and includes:

| Field | Description |
|-------|-------------|
| Name | Name of the game |
| ReleaseDate | Date the game was released |
| ReleaseYear | Year extracted from release date |
| Decade | Decade of release (1990s, 2000s, etc.) |
| Genre(s) | Genre tags from IGDB |
| Theme(s) | Thematic tags (Fantasy, Sci-fi, etc.) |
| Platform(s) | Platforms the game released on |
| Developer(s) | Development studio |
| PlayerPerspective | Camera/view type (Isometric, Third person, etc.) |
| GameMode(s) | Single player, Multiplayer, or both |
| Rating | IGDB user rating (0-100) |
| GenreCount | Number of genre tags |
| HasActionTheme | Whether "Action" appears in themes |
| HasOpenWorld | Whether "Open world" appears in themes |
| HasMultiplayer | Whether game supports multiplayer |
| PerspectiveCategory | Simplified perspective (Classic, Modern3D, FirstPerson) |
| DataSource | Manual or API |

---

### 2. Decade Summary Dataset
File: `Final_RPG_Decade_Summary.csv`

Each row represents a decade:

| Field | Description |
|-------|-------------|
| Decade | Decade (1990, 2000, 2010, 2020) |
| GameCount | Number of games in decade |
| AvgGenreCount | Average genre tags per game |
| ActionThemePercent | Percent of games with Action theme |
| OpenWorldPercent | Percent with Open World theme |
| MultiplayerPercent | Percent with multiplayer support |
| AvgRating | Average rating for decade |

---

### 3. Perspective Summary Dataset
File: `Final_RPG_Perspective_Summary.csv`

Each row represents a player perspective type:

| Field | Description |
|-------|-------------|
| PerspectiveCategory | Classic, Modern3D, or FirstPerson |
| GameCount | Number of games |
| AvgRating | Average rating |
| ActionThemePercent | Percent with Action theme |
| AvgGenreCount | Average genre tags |

---

## Methodology

### Initial Dataset

The project began with a manually curated dataset of 50 games selected using a temporal sampling approach. Games were chosen to represent different decades (1990s through 2020s) and different RPG subgenres (JRPGs, Western RPGs, Action RPGs, CRPGs). This process required interpretive decisions about what to include and how to categorize boundary cases.

### Audit Process

The dataset was verified by comparing IGDB entries to Steam and Wikipedia classifications. This helped identify inconsistencies in genre tagging and revealed how different platforms categorize the same games differently.

### Computational Scaling

The dataset was expanded using the IGDB API and Python. The script authenticates with Twitch OAuth, queries the IGDB database for RPG-tagged games, and processes the nested JSON response into a flat CSV structure. Additional analytical fields were calculated to enable temporal analysis.

---

## Analytical Features

New variables were created to better understand RPG evolution:

- **GenreCount**: Number of genre tags per game, measuring hybridization
- **HasActionTheme**: Binary flag for Action theme, tracking action-ification
- **HasOpenWorld**: Binary flag for Open World theme
- **HasMultiplayer**: Binary flag for multiplayer support
- **PerspectiveCategory**: Simplifies perspectives into Classic (Isometric/Bird view), Modern3D (Third person), and FirstPerson
- **Decade**: Groups games for temporal analysis
- **DataSource**: Distinguishes manual vs API-collected data

These variables allow for analysis of how RPGs have changed over time.

---

## Visualizations

The dataset includes several visualizations:

- Genre count over time (hybridization trend)
- Action theme prevalence by decade
- Player perspective distribution by decade
- Open World theme emergence
- Multiplayer support over time
- Rating distribution by decade

These help illustrate patterns in RPG evolution.

---

## Limitations

- IGDB tagging may reflect marketing as much as game design
- Older games may have sparser metadata
- Dataset skews toward successful/remembered games (survivorship bias)
- Some categories involve interpretation (like PerspectiveCategory)
- Western/English-language games may be overrepresented

The dataset represents a constructed view of RPG history rather than a complete record.

---

## Summary

This dataset demonstrates how cultural data is created, interpreted, and scaled. It shows that the RPG genre is not static but has evolved significantly — becoming more action-focused, more hybrid, and shifting from classic isometric/bird-view perspectives to modern third-person and first-person cameras. The data also reveals the emergence of "Open World" as a defining RPG characteristic in the 2010s and the increasing prevalence of multiplayer features.
