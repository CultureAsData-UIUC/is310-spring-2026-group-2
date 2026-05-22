# Collective Principles & Documentation for Working with Gaming Culture as Data

## What Someone Should Know Before Representing Gaming Culture as Data

### Javier Martinez

Before turning gaming culture into data, someone should know that games are hard to capture with simple labels. A game is not just a title, genre, platform, or score. It can also include mechanics, mood, story, visuals, sound, marketing, and player expectations.

For my project, I worked with horror games on Steam. One thing I learned is that a tag like “Horror” does not explain the whole game. A horror game might also be Atmospheric, Psychological Horror, Survival Horror, Action, story-rich, Multiplayer, or Co-op. This showed me that genre is not fixed. It is built from overlapping tags, moods, and gameplay patterns.

Someone starting a project like this should also remember that platform data is not neutral. Steam tags and descriptions are useful because they make games searchable, but they also reflect how Steam and developers present games to players. In my case, the data showed how horror games are marketed and categorized, not exactly how they feel to play.

The biggest thing to keep in mind is that data can show patterns, but it also leaves things out. My dataset can show common horror tags, but it cannot fully capture fear, atmosphere, sound, pacing, or player reaction. That means researchers need to be careful about their claims.

For me, the main lesson was that gaming data needs both computation and interpretation. Web scraping helped me collect more data, but I still had to think about what the tags meant and what the dataset could not show. 

### Charles Cantrell
For my project, I tracked how the RPG genre has evolved from 1994 to 2023 using data from IGDB. What I learned is that genre categories are not stable over time. A game labeled "RPG" in 1995 looks and plays completely differently from a game labeled "RPG" in 2023, yet both carry the same tag. This taught me that genre is not a fixed definition but a moving target shaped by player expectations, industry trends, and platform classification systems.

One of the clearest patterns in my data was the rise of the "Action" theme. In the 1990s, none of the RPGs in my dataset had "Action" listed in their themes. By the 2020s, 80% did. This could mean RPGs genuinely became more action-focused, or it could mean the "Action" tag became a marketing term that gets applied more liberally. The data alone cannot tell you which interpretation is correct.

I also noticed that player perspective shifted dramatically over time. Classic RPGs from the 1990s used bird-view or isometric cameras. By the 2010s, third-person and first-person perspectives dominated. This is not just a technical change — it reflects a shift in how players experience RPGs, from tactical overhead views to immersive character-level cameras.

The main lesson I took away is that metadata reflects the present moment, not history. When IGDB tags Fallout 2 (1998) as "Open world," that tag was probably applied retroactively, since "Open world" was not a common marketing term in the 1990s. Databases are living documents that get edited over time, so researchers should not assume that tags accurately represent how games were described at release.

## Gaming Data Principles 

### Javier Martinez

**Principle 1: Treat genre as flexible, not fixed.**  
A genre label like “Horror” does not explain the whole game. Many horror games also fit into other categories, such as survival, action, story-rich, atmospheric, or multiplayer. Future researchers should avoid treating one genre label as the full meaning of a game.

**Principle 2: Separate platform representation from player experience.**  
Steam tags and descriptions show how games are represented on the platform, but they do not fully show what it feels like to play them. A game can be tagged as scary or psychological, but the dataset cannot fully capture fear, atmosphere, sound, pacing, or player reaction.

## Anshuman Satpute

In my project, I treated Steam’s metadata especially its genre labels, as a kind of historical record of how the platform has chosen to organize games over time. Instead of seeing genres as a timeless list of categories, I started to see them as snapshots of how Steam and developers described games in specific years. Looking at multiple years at once made it clear that some genres become more visible, some fade into the background, and new ones appear, reflecting changes in design trends, marketing language, and platform priorities.

Working with platform metadata in this way showed me that Steam is not just a store; it is also an evolving catalog that leaves behind traces of how gaming culture gets sorted, named, and discovered. For example, the rise of labels like “Indie” or “Survival” is not only about individual games; it also tells a story about what kinds of games the platform supports and how it bundles them together for players. The dataset captures these shifts indirectly through changes in the frequency and combination of genre labels across years.

## Hongli Peng

## Principle 1: Genre is a Label, Not a Fact

When you query a database for games in a specific genre, you are not retrieving a neutral list. You are retrieving a list of games that someone — an editor, a contributor, a developer, an algorithm — decided to attach a particular label to. That decision was made at a specific moment, under specific conditions, and it may have been made differently by someone else.

Before you build a dataset around a genre label, ask: Who defined this label? When? Has its meaning shifted? Are there competing labels that overlap with it? You may need more than one keyword or tag to capture the full category you are interested in.

## Principle 2: Cleaning Is Interpretation

When you clean a dataset — filling in missing values, standardizing formats, deciding which records to keep and which to drop — you are making interpretive decisions, not just technical ones. Those decisions shape what your dataset can show.

Document your cleaning decisions as carefully as you document your collection process. A dataset that looks clean may have had significant interpretive work done to it that is invisible unless you record it explicitly.

## Charles Cantrell

Metadata can reflect the present, not the past. Database entries for older games are often edited retroactively to match contemporary tagging practices. A game from 1998 might have "Open world" added to its tags in 2015 when that term became marketable. Do not assume that current tags accurately represent how games were described at release.

Survivorship bias shapes every gaming dataset. Any dataset of video games will overrepresent successful, memorable, well-documented games. The thousands of forgotten games from any era are systematically excluded. Frame your findings as applying to "notable games" rather than "all games."