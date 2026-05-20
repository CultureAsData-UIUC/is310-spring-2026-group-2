import time
import requests
import pandas as pd
from datetime import datetime

CLIENT_ID = "Your CLIENT_ID"
CLIENT_SECRET = "Your CLIENT_SECRET "

def get_access_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()["access_token"]

def convert_date(timestamp):
    if not timestamp:
        return ""
    return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")

def igdb_post(url, headers, data, retries=3):
    for i in range(retries):
        try:
            response = requests.post(url, headers=headers, data=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                print("Rate limited, waiting...")
                time.sleep(2)
            else:
                print(f"Error {response.status_code}: {response.text}")
                time.sleep(1)
        except Exception as e:
            print("Request failed:", e)
            time.sleep(1)
    return []

token = get_access_token()
headers = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {token}"
}

# Confirmed keyword IDs:
# 416   = roguelike
# 17292 = roguelite

all_games = []
offset = 0
limit = 500

while True:
    query = f"""
    fields
        name,
        first_release_date,
        rating,
        genres.name,
        platforms.name,
        themes.name,
        keywords.name,
        involved_companies.company.name,
        player_perspectives.name,
        game_modes.name;

    where keywords = (416) | keywords = (17292);

    sort first_release_date desc;
    limit {limit};
    offset {offset};
    """

    games = igdb_post("https://api.igdb.com/v4/games", headers, query)

    if not games:
        break

    all_games.extend(games)
    print(f"Fetched {len(all_games)} games so far...")

    if len(games) < limit:
        break

    offset += limit
    time.sleep(0.25)

print(f"\nTotal games fetched: {len(all_games)}")

# ==========================================
# Build dataset
# ==========================================

dataset = []

for game in all_games:
    dataset.append({
        "Name":               game.get("name", ""),
        "Release Date":       convert_date(game.get("first_release_date")),
        "Rating":             round(game.get("rating", 0), 1) if game.get("rating") else "",
        "Genre(s)":           ", ".join([g["name"] for g in game.get("genres", [])]),
        "Platform(s)":        ", ".join([p["name"] for p in game.get("platforms", [])]),
        "Theme(s)":           ", ".join([t["name"] for t in game.get("themes", [])]),
        "Keyword(s)":         ", ".join([k["name"] for k in game.get("keywords", [])]),
        "Developer(s)":       ", ".join([
                                  c["company"]["name"]
                                  for c in game.get("involved_companies", [])
                                  if "company" in c
                              ]),
        "Player Perspective": ", ".join([p["name"] for p in game.get("player_perspectives", [])]),
        "Game Mode(s)":       ", ".join([m["name"] for m in game.get("game_modes", [])])
    })

df = pd.DataFrame(dataset)
csv_name = "roguelike_games_dataset.csv"
df.to_csv(csv_name, index=False)

print("\nFirst 5 rows:")
print(df.head())
print(f"\nDataset saved to: {csv_name}")
print(f"Total rows: {len(df)}")