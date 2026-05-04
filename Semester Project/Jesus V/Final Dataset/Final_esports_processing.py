from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get current folder
folder = Path(__file__).parent

# input files
general_file = folder / "GeneralEsportData.csv"
historical_file = folder / "HistoricalEsportData.csv"

# output folders
visual_folder = folder / "visualizations"
visual_folder.mkdir(exist_ok=True)

# load data
general_df = pd.read_csv(general_file)
historical_df = pd.read_csv(historical_file)

# clean date column
historical_df["Date"] = pd.to_datetime(historical_df["Date"])
historical_df["Year"] = historical_df["Date"].dt.year
historical_df["Decade"] = (historical_df["Year"] // 10) * 10

# clean missing values
general_df = general_df.dropna(subset=["Game", "Genre"]).copy()

# avoid division by zero
general_df["TotalPlayers"] = general_df["TotalPlayers"].replace(0, np.nan)
general_df["TotalTournaments"] = general_df["TotalTournaments"].replace(0, np.nan)

# new analytical columns
general_df["EarningsPerPlayer"] = general_df["TotalEarnings"] / general_df["TotalPlayers"]
general_df["EarningsPerTournament"] = general_df["TotalEarnings"] / general_df["TotalTournaments"]

general_df["EarningsPerPlayer"] = general_df["EarningsPerPlayer"].fillna(0)
general_df["EarningsPerTournament"] = general_df["EarningsPerTournament"].fillna(0)

# decade of release
general_df["ReleaseDecade"] = (general_df["ReleaseDate"] // 10) * 10

# tier based on total earnings
def assign_tier(earnings):
    if earnings >= 100000000:
        return "Tier 1 Elite"
    elif earnings >= 10000000:
        return "Tier 2 Established"
    elif earnings >= 1000000:
        return "Tier 3 Mid-Level"
    else:
        return "Tier 4 Smaller Scene"

general_df["Tier"] = general_df["TotalEarnings"].apply(assign_tier)

# game-level historical summary
historical_summary = historical_df.groupby("Game").agg(
    HistoricalTotalEarnings=("Earnings", "sum"),
    HistoricalTotalPlayers=("Players", "sum"),
    HistoricalTotalTournaments=("Tournaments", "sum"),
    FirstRecordedYear=("Year", "min"),
    LastRecordedYear=("Year", "max")
).reset_index()

historical_summary["YearsActiveInData"] = (
    historical_summary["LastRecordedYear"] - historical_summary["FirstRecordedYear"] + 1
)

# merge general and historical data
final_df = general_df.merge(historical_summary, on="Game", how="left")

# audit difference between general total and historical total
final_df["HistoricalTotalEarnings"] = final_df["HistoricalTotalEarnings"].fillna(0)
final_df["EarningsDifference"] = final_df["TotalEarnings"] - final_df["HistoricalTotalEarnings"]

# flag close matches
def audit_flag(row):
    if row["HistoricalTotalEarnings"] == 0:
        return "Missing from historical file"
    
    difference = abs(row["EarningsDifference"])
    allowed_difference = row["TotalEarnings"] * 0.05
    
    if difference <= allowed_difference:
        return "Close match"
    else:
        return "Difference needs review"

final_df["AuditFlag"] = final_df.apply(audit_flag, axis=1)

# professionalization score
# this combines earnings, tournaments, players, and years active
final_df["YearsActiveInData"] = final_df["YearsActiveInData"].fillna(0)

final_df["ProfessionalizationScore"] = (
    final_df["TotalEarnings"].rank(pct=True) +
    final_df["TotalTournaments"].rank(pct=True) +
    final_df["TotalPlayers"].rank(pct=True) +
    final_df["YearsActiveInData"].rank(pct=True)
) / 4

# inequality flag
def inequality_flag(row):
    if row["EarningsPerPlayer"] >= final_df["EarningsPerPlayer"].quantile(0.90):
        return "High earnings per player"
    elif row["EarningsPerPlayer"] <= final_df["EarningsPerPlayer"].quantile(0.25):
        return "Low earnings per player"
    else:
        return "Middle range"

final_df["InequalityFlag"] = final_df.apply(inequality_flag, axis=1)

# yearly historical dataset
yearly_df = historical_df.groupby("Year").agg(
    YearlyEarnings=("Earnings", "sum"),
    YearlyPlayers=("Players", "sum"),
    YearlyTournaments=("Tournaments", "sum")
).reset_index()

yearly_df["CumulativeEarnings"] = yearly_df["YearlyEarnings"].cumsum()

# genre summary
genre_df = final_df.groupby("Genre").agg(
    Games=("Game", "count"),
    TotalEarnings=("TotalEarnings", "sum"),
    AverageEarningsPerPlayer=("EarningsPerPlayer", "mean"),
    AverageEarningsPerTournament=("EarningsPerTournament", "mean")
).reset_index()

# save final datasets
final_df.to_csv(folder / "Final_Esports_Game_Level_Dataset.csv", index=False)
yearly_df.to_csv(folder / "Final_Esports_Historical_Yearly_Dataset.csv", index=False)
genre_df.to_csv(folder / "Final_Esports_Genre_Summary.csv", index=False)

print("final datasets created")
print("game-level rows:", len(final_df))
print("historical yearly rows:", len(yearly_df))
print("genre rows:", len(genre_df))

# -------------------------
# visualizations
# -------------------------

# top 10 games by total earnings
top_earnings = final_df.sort_values("TotalEarnings", ascending=False).head(10)

plt.figure()
plt.bar(top_earnings["Game"], top_earnings["TotalEarnings"])
plt.title("Top 10 Esports Games by Total Earnings")
plt.xlabel("Game")
plt.ylabel("Total Earnings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "top_10_total_earnings.png")
plt.show()

# top 10 games by earnings per player
top_player = final_df.sort_values("EarningsPerPlayer", ascending=False).head(10)

plt.figure()
plt.bar(top_player["Game"], top_player["EarningsPerPlayer"])
plt.title("Top 10 Games by Earnings Per Player")
plt.xlabel("Game")
plt.ylabel("Earnings Per Player")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "top_10_earnings_per_player.png")
plt.show()

# top 10 games by earnings per tournament
top_tournament = final_df.sort_values("EarningsPerTournament", ascending=False).head(10)

plt.figure()
plt.bar(top_tournament["Game"], top_tournament["EarningsPerTournament"])
plt.title("Top 10 Games by Earnings Per Tournament")
plt.xlabel("Game")
plt.ylabel("Earnings Per Tournament")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "top_10_earnings_per_tournament.png")
plt.show()

# yearly esports earnings over time
plt.figure()
plt.plot(yearly_df["Year"], yearly_df["YearlyEarnings"])
plt.title("Esports Earnings Over Time")
plt.xlabel("Year")
plt.ylabel("Yearly Earnings")
plt.tight_layout()
plt.savefig(visual_folder / "yearly_earnings_over_time.png")
plt.show()

# cumulative earnings over time
plt.figure()
plt.plot(yearly_df["Year"], yearly_df["CumulativeEarnings"])
plt.title("Cumulative Esports Earnings Over Time")
plt.xlabel("Year")
plt.ylabel("Cumulative Earnings")
plt.tight_layout()
plt.savefig(visual_folder / "cumulative_earnings_over_time.png")
plt.show()

# total earnings by genre
genre_plot = genre_df.sort_values("TotalEarnings", ascending=False).head(10)

plt.figure()
plt.bar(genre_plot["Genre"], genre_plot["TotalEarnings"])
plt.title("Top Genres by Total Esports Earnings")
plt.xlabel("Genre")
plt.ylabel("Total Earnings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "top_genres_by_earnings.png")
plt.show()

# tier distribution
tier_counts = final_df["Tier"].value_counts()

plt.figure()
plt.bar(tier_counts.index, tier_counts.values)
plt.title("Number of Games by Esports Tier")
plt.xlabel("Tier")
plt.ylabel("Number of Games")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(visual_folder / "tier_distribution.png")
plt.show()

# 8. professionalization score vs total earnings
plt.figure()
plt.scatter(final_df["ProfessionalizationScore"], final_df["TotalEarnings"])
plt.title("Professionalization Score vs Total Earnings")
plt.xlabel("Professionalization Score")
plt.ylabel("Total Earnings")
plt.tight_layout()
plt.savefig(visual_folder / "professionalization_vs_earnings.png")
plt.show()

print("visualizations saved in:", visual_folder)