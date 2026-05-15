import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {"User-Agent": "Mozilla/5.0"}

links = []

for page in range(12): 
    url = f"https://store.steampowered.com/search/?tags=1667&start={page*50}"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = soup.find_all("a", class_="search_result_row")
    
    for game in results:
        links.append(game.get("href"))
    
    time.sleep(0.5)

data = []

for link in links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    title_tag = soup.find("div", class_="apphub_AppName")
    desc_tag = soup.find("div", class_="game_description_snippet")
    tag_elements = soup.find_all("a", class_="app_tag")
    
    title = title_tag.text.strip() if title_tag else "Unknown"
    description = desc_tag.text.strip() if desc_tag else "No description"
    tags = [tag.text.strip() for tag in tag_elements]
    
    data.append({
        "title": title,
        "steam_url": link,
        "tags": ", ".join(tags),
        "description": description
    })
    
    print(title)
    time.sleep(0.5)

df = pd.DataFrame(data)
df.to_csv("scaled_horror_games.csv", index=False)

print("Done")