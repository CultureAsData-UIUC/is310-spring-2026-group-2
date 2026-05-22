## Initial dataset

My dataset examines the RPG (Role-Playing Game) genre, and which can be used to find changes or trends with the game genre over the years. The data I collected covers games from about a 30 year period (1994-2023). My main goal is to track how RPGs have changed with things like genre combinations, a games player perspective, themes in these games, and things like rating or platforms change over time.

I'm particularly interested in whether RPGs have become more action-focused rather than turn-based and how the genre's theme has shifted from more fantasy themes to sci-fi themes over the decades with changes in consumer taste.

This ties into my group's broader theme of video games as cultural objects — and tracking genre evolution over time reveals how player expectations and industry trends shapes a genre such as RPGs.

Maybe I can possibly find eras between years with themeing or genre combinations.

### Dataset Information
- Audit and augment approach
- I manually browsed IGDB's website, used the advance search function, and recorded information for 50 games tagged as RPGs

The dataset includes:
- Game metadata from IGDB (Genre, title, release date, platforms, developers, themes, rating, player perspective, game modes)

### Why This Topic
- I love RPGs especially the Fallout series, and I've noticed that modern RPGs feel very different from classic ones(Ex. Fallout 1 Isometric but Fallout 4 is first/third person)
- Games like Chrono Trigger and fallout 2 play nothing like Elden Ring or Cyberpunk 2077 but they're still RPGs, just from different times.
- It seems that RPGs have become "dumbed down" or "more action-focused" over time. I wanted to see if the data supports this.
- Understanding how genres evolve helps us understand how player expectations and industry trends shape game design.

### Tools
- This dataset was created manually. I browsed IGDB's website for RPGs, visited each game's page, and recorded the relevant information.
- I used a Excel spreadsheet to organize and store my data as I collected it.
- I did it manually to avoid having to make an API script for the time being.
- Took about ~4-6 minutes per game, took about 4 hours to get all 50 games.

### Challenges
- **Balancing years**: There are way more RPGs from 2013-2019 in my dataset, than from the 1990s. This partly reflects what's on IGDB and partly reflects the slight difficulty with searching on IGDB. I picked things I recognized taking the release year into account.
- **Inconsistent theme tagging**: Some games had lots of theme tags on IGDB (like "Action, Fantasy, Open world, Romance") while others only had one or two. I'm not sure if this means older games actually had fewer themes or if IGDB just has less detailed info for them.
- **Genre subjectivity**: IGDB lists multiple genres for many games, but what counts as "RPG, Shooter" vs just "RPG" seems inconsistent.
- **Rating availability**: Some older games didn't have ratings on IGDB, or had very few user ratings. This makes comparing ratings across eras tricky since newer games have way more data, and old games have less skewing there ratings.
 
### Patterns and Trends
 
From looking at my data so far, I noticed a few things:
 
- **Player perspective shift**: older games are mostly Bird view or Isometric. Starting in the mid 2000's Third person becomes dominant, and the amount of First person increases.
- **Genre hybridization**: Newer RPGs tend to have more genre tags. Classic games are often just "Role-playing (RPG)" while modern games are "Role-playing (RPG), Adventure, Shooter" or similar combinations.
- **Open world is new**: The "Open world" theme is mostly on just newer games.
- **Fantasy theme is common**: Fantasy is still a very common theme across all years.
 
### Reflection
 
- Making this dataset manually was tedious and tiring, but I got to comb through games rather than just downloading a spreadsheet.
- The shift from isometric/bird-view to third-person cameras is a definite shift.
- I wonder if the patterns will hold up with more games.
 
### Next Steps
 
- For the scaling phase, I plan to use the IGDB API to pull data for 500-1,000+ games programmatically.
- I'll write a Python script that authenticates with Twitch (IGDB is owned by Twitch) and queries their database for games tagged as RPG.
- With more data, I can do actual statistical analysis like calculating the percentage of games with "Action" theme by year, or graphing how player perspective distribution changes over time.
- I want to create visualizations to show different variables change across the decades.
- I might also try to identify "eras" in RPG history based on when certain patterns cluster together.

### Possible changes

**Genre combination Over Time**
- same question as I have stated previously.

**Player Perspective Shifts**
- Classic RPGs were often isometric or bird-view (top-down). Has this shifted toward first-person and third-person?
- When did first-person RPGs become common?

**Theme Evolution**
- Is Fantasy still the dominant RPG theme, or has Science Fiction grown?
- When did "Open world" become a common RPG theme?
- Has "Action" as a theme increased over time?