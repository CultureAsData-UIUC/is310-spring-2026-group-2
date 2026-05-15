### Proposed dataset

## Horror Games on Steam 

# Initial documentation

For this project, I want to build a dataset from scratch using Steam store pages for horror games. I chose this topic because it fits my group’s focus on gaming as culture and data, especially around genres, mechanics, and design patterns. I’m interested in horror because it is not just a simple genre label. Different games get called “horror” for different reasons, like survival mechanics, psychological tension, gore, helplessness, or atmosphere.

The cultural materials I am working with are public Steam store pages for horror games. Each item in my dataset will be one Steam store page. I plan to collect around 50 games and code features from each page. I'm taking the create data from scratch approach rather than auditing an existing dataset. Even though Steam already has tags and structured information, I still have to decide what to capture, how to organize it, and how to interpret the way each game presents horror.

To help with the process, I will use a spreadsheet to organize the data and keep my coding consistent. I may also use Steam search, tags, and basic digital tools to find games and compare store pages more efficiently. These tools help me gather and structure information, but they do not do the interpretive work for me. I still have to read each page and decide things like whether the game emphasizes psychological horror, survival, gore, combat, or atmosphere.

Some of the most important decisions in this dataset are about what to include, exclude, and how to categorize things. For example, I need to decide whether I only include games that are explicitly tagged as horror, or whether I also include games that feel horror-adjacent, like survival or thriller games. I also need to decide how to code overlapping features, since many horror games are also action games, puzzle games, or multiplayer games. Another decision is whether I should rely more on Steam tags, store descriptions, or both when identifying what kind of horror is being presented.

One challenge is that horror is a messy category. Some games clearly market themselves through fear, dread, or helplessness, while others mix horror with action or comedy. Another challenge is that Steam pages are designed to sell games, so the language is promotional and sometimes vague. That means some categories are easy to code, like whether multiplayer is listed, while others are more subjective, like whether the tone feels atmospheric or psychologically intense. To deal with that, I plan to keep my categories simple and write short notes for ambiguous cases.

As I started thinking through the dataset, one pattern that already stands out is that horror does not seem to be presented in just one way. Some games seem to focus on gore and violence, some on survival and resource management, and others on tension, mystery, or story. That makes me interested in how horror is framed differently depending on the kind of player experience the game is trying to promise.

## Next steps

After I finish the hand-built dataset, I would scale it by collecting many more Steam horror games using computational methods. I could use web scraping to gather store-page information like tags, descriptions, and feature labels for hundreds or thousands of games.

If I scaled the project, I would probably try to automate some of the categories, like identifying survival language, gore-related terms, multiplayer features, or recurring descriptive patterns in store pages. At the same time, some parts of the project would become harder at scale. Categories like “atmosphere,” “psychological horror,” or “helplessness” are interpretive and not easy to automate without oversimplifying them.

What would change at scale is that I would need much stricter definitions for my categories. Right now, I can make careful decisions item by item, but automation would force me to turn those judgments into rules or patterns. I would also expect technical issues like inconsistent tags, overlapping genres, duplicate entries, and vague marketing language. 