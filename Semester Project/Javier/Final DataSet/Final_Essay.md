### Horror Games on Steam: What Tags and Descriptions Can Tell Us

## Introduction

For my final project, I created a dataset about horror games on Steam. I chose this topic because my group’s overall theme is gaming as culture and data. Our group looked at gaming as more than just entertainment or software. We were interested in how video games shape player behavior, communities, identity, meaning, genres, mechanics, reviews, and platform data. My project fits into that theme because horror games are cultural objects. They are not only played by people; they are also categorized, marketed, described, searched for, and understood through platforms like Steam.

My main research question is: How are horror games represented on Steam through tags and descriptions? I wanted to understand what Steam store pages could show about horror as a genre. At first, horror seems like a simple label, but once I started building the dataset, I realized it is much more complicated. Some horror games focus on survival, some focus on psychological fear, some are action-heavy, some are atmospheric, and others are multiplayer or co-op experiences.

My argument is that horror on Steam is not one fixed category. It is a flexible genre that overlaps with many other types of games. Steam tags and descriptions help make horror games searchable and organized, but they also simplify what horror actually means as a player experience. The dataset reveals how horror is represented on Steam, but it cannot fully capture what horror feels like during gameplay.

## Dataset Overview

For this project, I made a dataset of horror games collected from Steam store pages. Each row in the dataset represents one Steam game page. The final scaled dataset includes four main columns: title, steam_url, tags, and description.

The title column identifies the game. The URL column links back to the Steam store page. The tags column shows the labels connected to the game, such as Horror, Singleplayer, Atmospheric, Psychological Horror, Survival Horror, Action, Adventure, Gore, Puzzle, or Co-op. The description column includes the short promotional description from the Steam page.

This dataset is not just a list of games. It is a dataset about how horror games are represented on Steam. The main cultural material I studied was the Steam store page. I focused on store pages because they combine platform organization, developer marketing, and community-facing labels. Steam pages do not only describe games; they help shape how players discover and understand them.

## How I Made the Dataset

I started with the idea of building a smaller dataset manually. In my original documentation, I planned to create a dataset from scratch using Steam store pages for horror games. I wanted to collect games and code features such as survival mechanics, psychological tension, gore, helplessness, and atmosphere. This first stage helped me think about horror as something that needed interpretation, not just copying and pasting.

At the manual stage, I had to decide what counted as horror. This was not always obvious. Some games are clearly horror, but others are horror-adjacent, like survival games, thrillers, dark puzzle games, or action games with horror themes. I also had to decide whether to rely mostly on Steam tags, store descriptions, or my own judgment. These decisions mattered because they shaped what the dataset could show.

After that, I scaled the project using web scraping. I wrote a Python script using requests, BeautifulSoup, pandas, and time. The script went through Steam search result pages using the horror tag, collected the game links, visited each game page, scraped the title, description, tags, and URL, and then saved the data into a CSV file called Scaled_Horror_Games.csv.

This process allowed me to move from a small hand-built dataset to a larger dataset with hundreds of Steam horror game entries.

## What the Dataset Represents

The dataset represents horror games as they appear through Steam’s platform structure. It does not represent every horror game ever made, and it does not represent every player’s experience with horror. Instead, it represents a specific view of horror: horror as organized by Steam tags and store-page descriptions.

This is important because Steam is not a neutral space. It is a commercial platform. Store pages are designed to sell games, and tags are designed to help players search, browse, and decide what they might want to play. That means the dataset represents horror as both a cultural category and a marketplace category.

The dataset also represents horror as a mixed genre. Many games in the dataset are not only labeled horror. They also include tags related to action, adventure, survival, story, atmosphere, multiplayer, and puzzle-solving. This shows that horror is often combined with other genres and mechanics.

## What the Dataset Reveals

The dataset reveals that horror on Steam is not one simple category. Horror games are usually hybrid games. Some are survival horror games, some are psychological horror games, some are first-person exploration games, some are action games, and some are multiplayer or co-op games.

One important pattern is that horror is often connected to mood. Tags like Atmospheric, Dark, Psychological Horror, and Story Rich show that many Steam horror games are marketed through feeling and tone. These games are not only described by what the player does, but also by what the player is supposed to feel.

Another pattern is that horror is connected to mechanics. Tags like Survival, Puzzle, First-Person, Action, Multiplayer, and Co-op show that horror can be created through different types of gameplay. A survival horror game may create fear by limiting resources. A puzzle horror game may create fear through mystery and uncertainty. A co-op horror game may turn fear into a shared social experience.

The dataset also reveals that Steam tags are useful because they show overlap. Instead of forcing every game into one genre, tags allow a game to have multiple identities at once. This fits with Starosta et al.’s argument that modern game classification is difficult because games often overlap across genres and can be classified in multiple ways.

## What the Dataset Conceals

The dataset also conceals a lot. The biggest thing it conceals is actual player experience. My dataset can show that a game is tagged as horror, psychological, survival, or atmospheric, but it cannot prove that players actually felt scared while playing it.

This matters because horror is not only a label. Horror depends on sound, visuals, pacing, gameplay, story, and player interaction. Thon’s article helped me understand this because he explains horror games through audiovisual, ludic, and narrative aesthetics. In simpler terms, horror can come from what the player sees and hears, what the player does, and how the story is structured. My dataset can capture tags and descriptions, but it cannot fully capture sound design, jump scares, lighting, player vulnerability, or the feeling of being under pressure.

The dataset also conceals differences between marketing and gameplay. A Steam page may describe a game as terrifying or atmospheric because that helps sell the game, but the actual gameplay experience might be different. Since my dataset is based on store pages, it mainly captures how games are presented, not necessarily how they play.

It also conceals the full process behind Steam tags. Tags can come from developers and users, and they reflect how games are categorized on the platform. But my dataset does not show exactly who added each tag, why certain tags appear first, or how Steam’s system affects visibility.

## The Role of Computation

Computation played a major role in my dataset because web scraping allowed me to collect data at a much larger scale than I could have done manually. Manually copying hundreds of Steam pages would have taken a long time and would have made the project harder to organize. The Python script made it possible to gather repeated information in a consistent format.

At the same time, computation did not do the whole project for me. The script could collect titles, URLs, tags, and descriptions, but it could not explain what those categories meant. It could not decide whether horror was being presented through atmosphere, survival, psychological tension, or social gameplay. That still required interpretation.

This showed me that computational methods are useful for collecting and organizing cultural data, but they do not replace human judgment. The computer helped me scale the dataset, but I still had to decide what the data meant.

## How Scale Shaped the Dataset

Scale changed the project in both positive and negative ways. On the positive side, having a larger dataset helped me see broader patterns. Instead of only looking closely at a small number of games, I could see how horror was represented across hundreds of Steam pages. This made it easier to notice repeated tags and descriptions.

However, scale also made the dataset less detailed. When I was looking at games manually, I could pay close attention to each page. I could think carefully about whether a game emphasized helplessness, gore, atmosphere, or psychological fear. But when I scraped hundreds of games, the dataset became more general. It focused on fields that could be collected consistently: title, URL, tags, and description.

This is one of the main tradeoffs I learned from the project. A larger dataset can reveal patterns, but it can also flatten details. Scale helped me see horror as a broad Steam category, but it also made it harder to capture the small differences between individual games.

## Limitations and Qualifications

There are several limitations to my dataset. First, the dataset depends on Steam’s horror tag and search system. This means it only includes games that were findable through Steam in that way. It does not include every horror game, and it may leave out games that are horror-adjacent but not tagged clearly as horror.

Second, the data is based on store pages. Store pages are promotional, so the language is not neutral. Developers and publishers want their games to sound interesting, scary, or unique. This means my dataset is better for studying how horror is marketed than for proving what horror games are actually like during play.

Third, the scraping process was not perfect. Some entries can appear as Unknown, some descriptions may be missing, and some tags may not be collected correctly. This means the dataset needs cleaning and should not be treated as perfect.

Fourth, the dataset does not include direct player reactions. It does not include reviews, playtime, sales, ratings, or interviews. Because of that, I cannot claim that a game tagged as horror actually scared players. I can only analyze how horror is represented on Steam.

## Ethics and Privacy

This project used public Steam store pages, so I did not collect private user information. I did not scrape individual player profiles, private accounts, or personal data. That made the privacy risk low.

However, there are still ethical issues to think about. Public data is still shaped by platforms, algorithms, and commercial goals. Steam controls what is visible, searchable, and easy to collect. Because of that, my dataset reflects Steam’s structure as much as it reflects horror gaming culture.

There is also an ethical issue in how horror and discomfort are represented. Horror games can deal with disturbing themes, fear, anxiety, violence, and emotional discomfort. Gowler and Iacovides show that games can create discomfort through uncertainty, pressure, difficult choices, disturbing themes, and feelings like fear or anxiety. My project does not study players directly, but it still deals with a genre connected to emotional intensity. That means I should be careful not to reduce player experience to simple labels.

## Scholarly Context

My project connects most strongly to scholarship on game classification and horror game experience.

The first source I used was Starosta et al.’s “The Tangled Ways to Classify Games.” This article helped me understand why video game genres are difficult to classify. The authors explain that modern games often overlap across genres, and they suggest that Steam tags can be useful because they describe games through genre, mechanics, themes, visual properties, and other characteristics. This connects directly to my project because my dataset uses Steam tags to study horror games. The article helped me see that tags are not just random labels; they are one way platforms and communities organize games.

The second source I used was Jan-Noël Thon’s “Playing with Fear.” This article helped me understand horror as an experience, not just a tag. Thon argues that horror games create fear through a combination of audiovisual, ludic, and narrative elements. This matters because my dataset cannot fully capture those elements. It can show that a game is described as horror, but it cannot fully show how fear is created during gameplay.

The third source I considered was Gowler and Iacovides’s article on uncomfortable experiences in digital games. Their work shows that discomfort in games can come from uncertainty, pressure, disturbing themes, limited power, and difficult decisions. This supports my point that horror and discomfort are more complex than tags alone.

Together, these sources helped me place my project in a larger scholarly conversation. My dataset is not only about Steam games. It is about how games are classified, how horror is represented, and what gets lost when emotional experiences are turned into data.

## What I Learned

This project changed how I think about data. At first, I thought the main challenge would be collecting enough information. But after working on the project, I realized that the harder part was deciding what the data meant.

I learned that data is not simply found. It is made through choices. I chose Steam as my platform. I chose horror games as my topic. I chose to collect titles, URLs, tags, and descriptions. I chose to focus on representation rather than player reviews or sales numbers. All of those choices shaped the final dataset.

I also learned that computational methods are powerful but limited. Web scraping helped me collect data at scale, but it did not remove the need for interpretation. The script could gather information, but it could not understand horror as a cultural experience.

Most importantly, I learned that culture becomes data through simplification. A horror game is a full experience involving sound, visuals, mechanics, story, emotion, and player reaction. My dataset turns that experience into rows and columns. That makes patterns easier to see, but it also leaves things out.

## Conclusion

My final project shows that horror games on Steam are not represented as one simple genre. Instead, horror appears through many overlapping tags, descriptions, mechanics, and moods. Some games are survival horror, some are psychological, some are action-based, some are story-rich, and others are multiplayer or co-op experiences.

The dataset reveals how Steam organizes and markets horror games. It shows that horror is a flexible category shaped by platform tags, descriptions, and search systems. But the dataset also conceals important parts of horror, especially the actual experience of fear, atmosphere, sound, pacing, and player emotion.

In the end, this project helped me understand the main idea of culture as data. Data can help us see patterns in culture, but it does not capture culture completely. Steam can turn horror into tags and descriptions, and I can turn those tags and descriptions into a dataset. But horror as a player experience is still more complicated than what fits in a spreadsheet.

## References

Gowler, C. P. R., & Iacovides, I. (2019). “Horror, guilt and shame”—Uncomfortable experiences in digital games. Proceedings of the Annual Symposium on Computer-Human Interaction in Play, 325–337. https://doi.org/10.1145/3311350.3347179

Starosta, J., Kiszka, P., Szyszka, P. D., Starzec, S., & Strojny, P. (2024). The tangled ways to classify games: A systematic review of how games are classified in psychological research. PLOS ONE, 19(6), Article e0299819. https://doi.org/10.1371/journal.pone.0299819

Thon, J.-N. (2019). Playing with fear: The aesthetics of horror in recent indie games. Eludamos: Journal for Computer Game Culture, 10(1), 197–231. https://doi.org/10.7557/23.6179 