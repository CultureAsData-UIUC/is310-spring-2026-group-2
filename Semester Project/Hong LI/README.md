# Initial Dataset

My dataset examines the roguelike genre, and can be used to identify changes and trends in this genre over time. The data I collected covers games across roughly a 15-year period, allowing for analysis of how roguelike games have evolved in terms of genre combinations, player perspective, themes, ratings, and platforms.

My main goal is to explore how roguelike games have shifted over time—particularly whether they have become more action-oriented and accessible, compared to their traditionally turn-based and system-heavy roots. I am also interested in how themes have evolved, such as whether roguelikes have expanded beyond their traditional fantasy settings into areas like science fiction or hybrid themes.

This connects to my group’s broader theme of video games as cultural objects, as tracking the evolution of the roguelike genre helps reveal how player expectations, technological advances, and industry trends influence game design.

---

## Dataset Information

### Audit and augment approach
I manually browsed IGDB’s website, used the advanced search function, and recorded information for 50 games tagged as roguelike or roguelite.

### The dataset includes:
- Game metadata from IGDB (Genre, title, release date, platforms, developers, themes, rating, player perspective, game modes)

---

## Why This Topic

I enjoy roguelike games such as Hades, The Binding of Isaac, and Slay the Spire, and I’ve noticed that modern roguelikes feel very different from classic ones.

Early roguelikes like Rogue are very different from modern titles like Hades or Returnal, even though they are grouped under the same genre.

It seems that roguelikes have become more action-heavy, faster-paced, and visually complex, compared to older turn-based, text-heavy, or grid-based designs.

I wanted to see if the data supports the idea that roguelikes have shifted from niche, system-driven games to more mainstream and hybridized experiences.

Understanding how roguelikes evolve helps explain how player expectations and accessibility influence genre development.

---

## Tools

This dataset was created manually by browsing IGDB and recording data from individual game pages.

I used an Excel spreadsheet to organize and store the data.

I chose manual collection to avoid setting up the API initially and to better understand the data itself.

---

## Challenges

- **Balancing years:** There are more recent roguelikes in the dataset than older ones. This reflects both IGDB’s database and the fact that the genre has grown significantly in recent years.
- **Inconsistent theme tagging:** Some games have many theme tags while others have very few. It is unclear whether this reflects actual design differences or incomplete metadata for older games.
- **Genre subjectivity:** The distinction between “roguelike” and “roguelite” is not always clear, and many games include multiple genre labels (e.g., RPG, shooter, strategy).
- **Rating availability:** Older games often lack ratings or have fewer user reviews, making comparisons across time less reliable.

---

## Patterns and Trends

From my initial observations, I noticed several trends:

- **Player perspective shift:** Older roguelikes are mostly bird-view, isometric, or text-based. Newer games increasingly use side view, third-person, or even first-person perspectives.
- **Genre hybridization:** Modern roguelikes frequently combine multiple genres (e.g., RPG, shooter, deck-building, platformer), while older ones are more mechanically focused and genre-pure.
- **Rise of action elements:** Many newer roguelikes emphasize real-time combat and action mechanics, compared to the turn-based systems of earlier games.
- **Theme diversity:** While fantasy remains dominant, there is a noticeable increase in science fiction, horror, and mixed themes in newer titles.
- **Platform expansion:** Roguelikes have expanded from PC-focused releases to consoles and mobile platforms.

---

## Next Steps

For the scaling phase, I plan to use the IGDB API to collect data for 500–1,000+ roguelike games.

I will write a Python script to authenticate via Twitch and query IGDB programmatically.

With more data, I can perform statistical analysis, such as:
- Percentage of roguelikes with action elements over time
- Changes in player perspective distribution
