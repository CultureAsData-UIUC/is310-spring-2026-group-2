from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder = Path(__file__).parent

manual_file = folder / "rpg_genre_dataset.csv"

visual_folder = folder / "visualizations"
visual_folder.mkdir(exist_ok=True)

df = pd.read_csv(manual_file)

print("Loaded", len(df), "games from manual dataset")
print("Columns:", list(df.columns))

df.columns = df.columns.str.replace(r"[()]", "", regex=True)
df.columns = df.columns.str.strip()

df["ReleaseDate"] = pd.to_datetime(df["Release Date"], errors="coerce")
df["ReleaseYear"] = df["ReleaseDate"].dt.year

df["Decade"] = (df["ReleaseYear"] // 10) * 10
df["DecadeLabel"] = df["Decade"].astype(str) + "s"

def count_genres(genre_str):
    if pd.isna(genre_str):
        return 0
    return len(genre_str.split(", "))

df["GenreCount"] = df["Genres"].apply(count_genres)

def has_action_theme(theme_str):
    if pd.isna(theme_str):
        return False
    return "Action" in theme_str

df["HasActionTheme"] = df["Themes"].apply(has_action_theme)

def has_open_world(theme_str):
    if pd.isna(theme_str):
        return False
    return "Open world" in theme_str

df["HasOpenWorld"] = df["Themes"].apply(has_open_world)

def has_multiplayer(mode_str):
    if pd.isna(mode_str):
        return False
    return "Multiplayer" in mode_str

df["HasMultiplayer"] = df["Game Modes"].apply(has_multiplayer)

def categorize_perspective(persp_str):
    if pd.isna(persp_str):
        return "Unknown"
    persp_str = persp_str.lower()
    if "bird" in persp_str or "isometric" in persp_str:
        return "Classic (Isometric/Bird view)"
    elif "first person" in persp_str:
        return "First Person"
    elif "third person" in persp_str:
        return "Third Person"
    else:
        return "Other"

df["PerspectiveCategory"] = df["Player Perspective"].apply(categorize_perspective)

df["DataSource"] = "Manual"

final_columns = ["Name", "Release Date", "ReleaseYear", "Decade", "DecadeLabel", "Genres", "Themes", "Platforms", "Developers", "Player Perspective", "PerspectiveCategory", "Game Modes", "Rating", "GenreCount", "HasActionTheme", "HasOpenWorld", "HasMultiplayer", "DataSource"]

final_columns = [c for c in final_columns if c in df.columns]
final_df = df[final_columns].copy()

final_df.to_csv(folder / "Final_RPG_Game_Level_Dataset.csv", index=False)
print("\nSaved Final_RPG_Game_Level_Dataset.csv with", len(final_df), "games")

decade_summary = df.groupby("Decade").agg(
    GameCount=("Name", "count"),
    AvgGenreCount=("GenreCount", "mean"),
    ActionThemePercent=("HasActionTheme", lambda x: x.mean() * 100),
    OpenWorldPercent=("HasOpenWorld", lambda x: x.mean() * 100),
    MultiplayerPercent=("HasMultiplayer", lambda x: x.mean() * 100),
    AvgRating=("Rating", "mean")
).reset_index()

decade_summary.to_csv(folder / "Final_RPG_Decade_Summary.csv", index=False)
print("Saved Final_RPG_Decade_Summary.csv")
print(decade_summary.to_string())

perspective_summary = df.groupby("PerspectiveCategory").agg(
    GameCount=("Name", "count"),
    AvgRating=("Rating", "mean"),
    ActionThemePercent=("HasActionTheme", lambda x: x.mean() * 100),
    AvgGenreCount=("GenreCount", "mean")
).reset_index()

perspective_summary.to_csv(folder / "Final_RPG_Perspective_Summary.csv", index=False)
print("\nSaved Final_RPG_Perspective_Summary.csv")
print(perspective_summary.to_string())

print("\nGenerating visualizations...")

plt.figure(figsize=(10, 6))
decade_plot = decade_summary.sort_values("Decade")
plt.bar(decade_plot["Decade"].astype(str) + "s", decade_plot["AvgGenreCount"], color="steelblue")
plt.title("RPG Genre Hybridization Over Time")
plt.xlabel("Decade")
plt.ylabel("Average Number of Genre Tags")
plt.tight_layout()
plt.savefig(visual_folder / "genre_hybridization_by_decade.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(decade_plot["Decade"].astype(str) + "s", decade_plot["ActionThemePercent"], color="indianred")
plt.title("Rise of 'Action' Theme in RPGs")
plt.xlabel("Decade")
plt.ylabel("Percent of Games with Action Theme")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(visual_folder / "action_theme_by_decade.png")
plt.close()

perspective_by_decade = df.groupby(["Decade", "PerspectiveCategory"]).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
perspective_by_decade.plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Player Perspective Distribution by Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Games")
plt.legend(title="Perspective", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig(visual_folder / "perspective_by_decade.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(decade_plot["Decade"].astype(str) + "s", decade_plot["OpenWorldPercent"], color="forestgreen")
plt.title("Emergence of 'Open World' in RPGs")
plt.xlabel("Decade")
plt.ylabel("Percent of Games with Open World Theme")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(visual_folder / "open_world_by_decade.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(decade_plot["Decade"].astype(str) + "s", decade_plot["MultiplayerPercent"], color="darkorange")
plt.title("Multiplayer Support in RPGs Over Time")
plt.xlabel("Decade")
plt.ylabel("Percent of Games with Multiplayer")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(visual_folder / "multiplayer_by_decade.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(decade_plot["Decade"].astype(str) + "s", decade_plot["AvgRating"], color="mediumpurple")
plt.title("Average RPG Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(visual_folder / "rating_by_decade.png")
plt.close()

plt.figure(figsize=(10, 6))
persp_counts = df["PerspectiveCategory"].value_counts()
plt.bar(persp_counts.index, persp_counts.values, color="teal")
plt.title("RPG Games by Player Perspective")
plt.xlabel("Perspective Type")
plt.ylabel("Number of Games")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "games_by_perspective.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.scatter(df["GenreCount"], df["Rating"], alpha=0.6, color="coral")
plt.title("Genre Hybridization vs Rating")
plt.xlabel("Number of Genre Tags")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig(visual_folder / "genre_count_vs_rating.png")
plt.close()

print("\nVisualizations saved in:", visual_folder)

print("\n" + "=" * 60)
print("SUMMARY STATISTICS FOR FINAL ESSAY")
print("=" * 60)

print(f"\nTotal games in dataset: {len(df)}")
print(f"Year range: {df['ReleaseYear'].min()} - {df['ReleaseYear'].max()}")

print("\n--- Games per Decade ---")
print(df["DecadeLabel"].value_counts().sort_index())

print("\n--- Action Theme by Decade ---")
for _, row in decade_summary.iterrows():
    print(f"  {int(row['Decade'])}s: {row['ActionThemePercent']:.1f}%")

print("\n--- Player Perspective Distribution ---")
print(df["PerspectiveCategory"].value_counts())

print("\n--- Open World by Decade ---")
for _, row in decade_summary.iterrows():
    print(f"  {int(row['Decade'])}s: {row['OpenWorldPercent']:.1f}%")

print("\n--- Average Genre Count by Decade ---")
for _, row in decade_summary.iterrows():
    print(f"  {int(row['Decade'])}s: {row['AvgGenreCount']:.2f} genres per game")

print("\n--- Multiplayer by Decade ---")
for _, row in decade_summary.iterrows():
    print(f"  {int(row['Decade'])}s: {row['MultiplayerPercent']:.1f}%")

print("\n" + "=" * 60)
print("DONE - All files created")
print("=" * 60)