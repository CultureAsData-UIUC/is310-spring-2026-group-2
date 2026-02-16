# Instructor Feedback on Group & Individual Topic Selection

## Group Feedback

Overall, this is a strong theme that fits well with the goals of the course. Your focus on gaming as a cultural, social, and economic phenomenon—–rather than just a technical artifact—–shows thoughtful alignment with the course's emphasis on meaning-making and cultural practice. I especially appreciate how clearly you've articulated what is in scope (player behavior, communities, identity, esports, representation) versus out of scope (gambling, hardware benchmarking, tabletop games, purely technical analysis). This demonstrates that you're thinking about gaming as a site of cultural production and social interaction, which is exactly the right framing for this course. That said, there are several areas where your framing could become more conceptually precise and better grounded in game studies and information science scholarship.

1. **Conceptual Clarity**

Your description of gaming as a "cultural, social, and economic phenomenon" is a good start, but it would be helpful to unpack what you mean by these terms in the context of gaming. For example, when you say "cultural," are you referring to the ways games reflect and shape cultural norms and values? When you say "social," are you focusing on player interactions, community formation, or something else? Providing more specific definitions and examples will help clarify your focus and make it easier to connect with relevant scholarship. Overall, these are massive topics, so you might consider trying to define these terms more clearly so that you don't end up being overwhelmed by the breadth of your theme.

You might consider are you examining how game design shapes communities or how communities shape gaming culture? Or maybe even how platform infrastructures mediate both? Several of you mention economics and esports professionalization, while others focus on genres and player engagement. How do these different lenses relate to each other within your group theme?

Gaming culture is vast, and each of your individual projects seems to approach it from a different angle (competition, sales, performance metrics, genre evolution, industry growth). This diversity is valuable, but you should think collectively about what connects these approaches and what shared insights you hope to generate about gaming as culture.

1. **Engage with Platform Political Economy and Technological Infrastructure**

I'm glad you've acknowledged that gaming is not just a technical artifact, but I'd encourage you to think more explicitly about the relationship between technical infrastructure and cultural practice. The political economy of gaming has changed dramatically in the past decade alone, and these shifts fundamentally shape what you're studying. 

So you might want to at least engage somewhat with the fact that most contemporary gaming is mediated through platforms like Steam, Epic, console ecosystems, or mobile app stores. These platforms shape what games get made, how they're distributed, who profits, and how players interact. Similarly, the shift from local to streaming-based gaming changes ownership, access, preservation, and play practices; all of which has transformed gaming economics and player relationships to games.

You don't need to make this your primary focus, but being aware of these infrastructural dimensions will strengthen your analysis. Gaming culture doesn't emerge in a vacuum—–it's shaped by who owns the platforms, how visibility is determined, and what economic models sustain (or fail to sustain) different types of games and communities.

3. **Engage with Published Scholarship**

This topic sits at the intersection of game studies, media studies, platform studies, and information science, so there's substantial scholarship you can draw on. I'd encourage you to start engaging with key works early on, particularly those that examine gaming as cultural practice, community formation, and the economics of digital play.

Some starting points to consider:

- Muriel, Daniel, and Garry Crawford. *Video Games as Culture: Considering the Role and Importance of Video Games in Contemporary Society*. Routledge, 2018. (Available as an e-book through the library)
- Xue, Hanhan, Joshua I. Newman, and James Du. “Narratives, Identity and Community in Esports.” *Leisure Studies* 38, no. 6 (2019): 845–61. [https://doi.org/10.1080/02614367.2019.1640778](https://doi.org/10.1080/02614367.2019.1640778).
- Nieborg, David B., and Thomas Poell. “The Platformization of Cultural Production: Theorizing the Contingent Cultural Commodity.” *New Media & Society* 20, no. 11 (2018): 4275–92. [https://doi.org/10.1177/1461444818769694](https://doi.org/10.1177/1461444818769694).

You should also look at journals like *Games and Culture*, *Game Studies*, *Convergence*, and *New Media & Society* for more recent work on gaming communities, esports, and platform dynamics.

Given your topic, I'd strongly encourage you to reach out to faculty in the iSchool who work on gaming and digital culture. Professor Judith Pintar and Professor Dave Dubin could both provide valuable guidance as you develop your projects.

4. **Working with Existing Datasets: Verification and Augmentation**

I notice that all group members are planning to work with existing Kaggle datasets. This is a reasonable approach, but it comes with specific responsibilities for this course. Since the course requires you to either create data or meaningfully augment existing data, you'll need to think carefully about:

- Who created these datasets? How were they constructed? What was included and excluded? What biases or limitations might exist?
- Are there missing values, inconsistencies, or errors? How complete is the coverage?
- How will each of you augment these existing datasets? This could involve collecting additional datasets or integrating data from multiple sources, or enriching the data with contextual information.

Simply using an existing dataset as-is does not meet the course requirements. Each of you will need to articulate specifically what you're adding, verifying, or expanding. I'll provide individual feedback on augmentation strategies for each project.

Your collaboration plan looks solid—using Discord for communication, GitHub for organization, and maintaining individual folders within a shared repository is a sensible approach. The key will be ensuring that your individual projects inform and strengthen each other thematically, even as each of you pursues distinct analytical questions.

## Individual Feedback

### Jesus

Your focus on esports earnings and the economics of competitive gaming is a strong choice that connects well to the group's broader theme. I appreciate that you've identified a specific existing dataset (Esports Earnings from Kaggle, based on esportsearnings.com spanning 1998-2023) and that you're thinking about substantive questions like inequality between games, genre popularity, sustainability, and how cultural attention translates into financial reward. The temporal span of this dataset is particularly valuable—covering 25 years of esports development gives you substantial historical depth to examine how competitive gaming has evolved as an economic and cultural phenomenon.

I also appreciate that you've described what variables are in the dataset (game titles, prize pools, number of tournaments, number of players, total earnings). This shows you're thinking concretely about what the data contains. However, you now need to think critically about potential disconnects between how this data was collected and the analytical questions you're asking. Prize pool data might be relatively straightforward to verify, but concepts like "inequality," "genre popularity," and "cultural attention" are interpretive and will require you to make decisions about how to operationalize them from the available data.

Since you're working with an existing dataset, your first responsibility is to verify its quality and understand its construction. Fortunately, esportsearnings.com appears to still be online, which gives you an opportunity to trace the data back to its source—similar to what we did with the HathiTrust dataset in class. I'd recommend select random rows from the dataset and verify them against the current website. What has been maintained? What might have been lost or changed? Can you determine how the data was initially compiled? Was it scraped from the website, manually entered, or sourced from tournament organizers? Understanding the provenance of the data will help you assess its reliability and identify any biases or gaps. Furthermore, does the dataset include all games on the site, or was there filtering? Are certain regions, platforms, or tournament types over- or under-represented? How has data collection changed over the 1998-2023 span? Early esports tournaments may be less comprehensively documented than recent ones. Are there gaps in prize pools, player counts, or tournament information? How will you handle these? Understanding the dataset's limitations and biases will be crucial for making valid claims about inequality and sustainability in esports.

Since the course requires you to add value through augmentation, you'll need to think creatively about how to enrich this dataset to answer your research questions. Here are several possible approaches based on the questions you've outlined:

- The 1998-2023 timeframe lets you examine the early days of competitive gaming. You could augment the dataset by adding contextual information about key moments in esports history, from major sponsorship deals to the founding of professional leagues and platform launches (Twitch in 2011, for example), or even regulatory changes. This would help you understand why certain games saw prize pool growth at particular moments.
- You mention "genre popularity" as a key interest. Currently, it seems the dataset has five very basic genre categories, so you might consider adding more detailed genre classifications that might get more specific elements of esports games or players.
- You mention "inequality between games," which is an interesting angle. To meaningfully analyze this, you might augment with more detailed data on the distribution of prize pools across games. For instance, do a small number of elite players capture most earnings, or is it more evenly distributed? Also who is funding these prize pools (developers, sponsors, crowdfunding)? Similarly, "cultural attention" is a broad concept that could be operationalized in various ways. You might consider augmenting with data on viewership, media coverage, or community engagement to see how these correlate with prize pool growth.

Generally speaking, several of your key concepts—–"inequality," "genre popularity," "cultural attention," "sustainability"—–are interpretive, so I would suggest spending some time thinking about how you will define and operationalize these concepts in relation to the data. 

Similarly, Your questions are ambitious, which is good, but you'll need to narrow your scope to make this feasible. Rather than trying to capture all of esports history and all aspects of inequality and attention, you might consider focusing on a specific genre, time period, or set of games to analyze in depth. Are there turning points in esports history that you can examine closely to understand how economic dynamics shifted? Are there particular games that exemplify different trajectories of growth and sustainability that you can compare? Or will your dataset end up being a more in-depth history of EsportsEarnings.com itself, tracing how it has evolved as a source of data on competitive gaming? Lots of possibilities here, but you'll need to narrow your focus to make it manageable and meaningful.

There's growing academic work on esports that will help you frame your analysis. T.L. Taylor's *Raising the Stakes: E-Sports and the Professionalization of Computer Gaming* (MIT Press, 2012) is apparently foundational for understanding how competitive gaming became professionalized, so you might start there and then look at newer scholarship in the journals I mentioned above. Overall, I like the focus and so now it is about thinking carefully about how to verify and augment the dataset to make meaningful claims about the economics of esports. Happy to discuss further as you develop your project!

### Charles

Your focus on video game sales and ratings with attention to historical evolution is promising, and I appreciate your connection to retro gaming and how technological limitations shaped what was feasible in different eras. The temporal scope (1980-2020) gives you substantial historical depth, and your interest in how platforms, technology, and market tastes evolved over time connects well to broader questions about gaming as culture. You've also helpfully documented what's in the dataset (title, platform, release year, genre, publisher, developer, scores, ESRB rating, sales by region), which shows you're thinking concretely about the data.

Your observation that "the limitations of technology surely has affected what was feasible and thus genre/perceptions/sales of games" is exactly the kind of cultural-technical relationship this course wants you to explore. However, there are significant concerns about data provenance and verification that you need to address before proceeding.

My primary concern is that I cannot access the original source for this dataset. The Kaggle page links to a source that is no longer available, which raises serious questions about verification. How can you confirm the accuracy, completeness, and methodology of this data if you cannot trace it back to its origin? This is not a minor issue—it's fundamental to responsible data work.

Before committing to this dataset, you need to answer the following questions:

- Where did this data originally come from? Who compiled it? What was their methodology? The Kaggle page should have some documentation—read it carefully. But if you cannot find any information about the original source, you need to consider whether this dataset is reliable enough to use for your project.
- Can you spot-check specific games against other sources? VGChartz, for instance, tracks historical sales data (though it has its own reliability issues). Gaming magazines, publisher reports, or industry databases might provide verification points for at least some of the data.
- What's missing? The dataset appears to cover North America, Europe, and Japan—but what about other regions? What about digital sales (which became significant in the 2010s)? What platforms or game types might be systematically excluded?

If you cannot adequately verify this data's origins and quality, you may need to consider alternative datasets or a different approach to examining historical game sales.

You mention analyzing "regional markets" (North America, Europe, Japan), but you need to think much more carefully about what "region" means in this context and the massive confounding factors involved. More fundamentally: *who defined these regions and why?* These categories likely come from the video game industry's own sales analytics, where markets are segmented for business purposes. This is not a neutral geographic categorization—–it reflects how publishers think about profitable markets. Understanding this framing is crucial to interpreting the data.

Similarly, you correctly identify that this is sales data, but you need to think critically about what sales data is and isn't. Sales data is collected for business forecasting and investor reporting. It measures commercial success, not necessarily cultural impact or player engagement. Therefore it likely skews to physical copies sold through retail. Later datasets might include digital sales, but verification is difficult since platforms rarely release comprehensive numbers. So you need to consider what is missing: used game sales, piracy, emulation, games kept but not played, games played extensively but not purchased (shareware, demos, borrowing). Sales ≠ actual play or cultural significance. Finally, publishers inflate numbers. Platforms obfuscate data. "Shipped to retailers" ≠ "sold to consumers."

Your interest in how technological limitations shaped market taste is compelling and potentially more tractable than the regional question. Some angles to consider: What is the relationship between genres and market taste? How did technological limitations shape which genres were viable in different eras? When do certain genres appear in the data? When do they peak? When do they decline? Can you correlate this with technological shifts? Some genres thrived on specific platforms. What explains these platform-genre affinities? How do the same genres evolve differently across platforms?

Since you're working with existing data, augmentation is required. Based on your interests, you might consider exploring the following angles:

- You mention market evolution—track publisher and developer consolidation over time. You could add metadata about company mergers, acquisitions, bankruptcies, and new entrants. This would help explain shifts in genre popularity and platform focus as corporate strategy changed.
- You could also undertake a more detailed coding of platforms by their technical capabilities and release timelines. This would allow you to analyze how technological affordances shaped what games were made and sold in different eras. For example, the rise of 3D graphics enabled new genres, while mobile platforms enabled more casual gaming. Understanding these technological shifts would give you another angle on genre evolution and market trends.
- Alternatively, you could explore the consistency and evolution of genre labels over time. I will note that Javier is also interested in this topic, so you might could consider partnering together (though just a suggestion!). But generally, you might consider what would it look like to have more granular genre labels that get to your interest in market taste. What would that even look like for instance? You might consider trying to code one or two games to create a prototype and get how this aggregate data often flattens the complexity of genre. 
- You might also consider exploring what is missing from this dataset. It likely focuses on traditional console and PC sales, but what about other platforms and distribution models that became significant over time? You mention an interest in retro gaming, so are there consoles or games you know of that are missing from this dataset? You could augment by creating a dataset of those games or trying to find and verify another dataset for instance.

As some general guidance on scope, 1980-2020 is a huge timespan with massive industry and cultural shifts. So you might consider narrowing your focus to specific eras or key moments in gaming history that align with your interest in retro consoles and technological evolution. Generally, your interest in how technology shapes gaming culture is valuable, and the historical scope is ambitious in a good way. But the data quality question is serious and must be addressed first. Sales data can tell you important things about the gaming industry's evolution, but only if you understand its origins, limitations, and what it actually measures. Happy to discuss further as you develop your project!

### Anshuman

Your focus on Valorant leaderboard statistics is interesting, and I appreciate that you have a personal connection to the game as a competitive player—–this kind of insider knowledge can be valuable for understanding what the data actually represents. You've also helpfully documented what's in the dataset (over 80,000 players with ranking, rating, and in-game stats) and explained how it fits the group's competitive gaming theme. However, there are significant issues with data provenance and, more importantly, a lack of clarity about what analytical question you're actually trying to answer.

First, the verification challenge. You mention the data was "collected from a public stats tracker (e.g., tracker.gg)," but when I looked at the Kaggle page, I found that someone asked the creator three years ago where the data came from, and the response was simply "scraped from a leaderboard website." Which leaderboard website? Completely unclear. This is a serious problem.

Your first responsibility is determining the actual source of this data. Given the timeframe and structure, this is likely from tracker.gg, blitz.gg, or a similar stats aggregator. You need to figure out which one and verify that it still exists and is accessible. Then you need to start considering how this data was even created in the first place. How do these sites collect data? Do they scrape Riot's API? Do they require players to opt in? Are certain ranks or regions over-represented? Next would be figuring out how to assess accuracy. You might compare random entries from the dataset to current leaderboard information. What has changed? What has remained consistent? But also of course what is missing? Are casual players excluded? Only certain regions? Only players who linked their accounts to the tracker? Without understanding where this data came from and how it was constructed, you cannot make valid analytical claims. This verification work is essential when using an existing dataset.

Beyond data provenance, my bigger concern is that you don't have seem to a have clear research question driving your dataset to help you augment it. You state you're interested in "what distinguishes top players from the rest of the ladder," but how will you augment this existing dataset to get at this question? 

Before deciding on your question, you need to understand what this data represents. Leaderboards are not neutral reflections of skill–—they're constructed systems with specific logics. So you might consider what is being collected and whether that is actually a proxy for skill or something else. Also you might consider the broader ecosystem of competitive play and how that shapes what gets measured.  Since you're working with existing data, you must augment it to meet course requirements. Simply analyzing the leaderboard stats as-is is insufficient. Here are several possible augmentation strategies based on your interests:

- You might consider creating a custom dataset from scratch trying to datafy gameplay patterns of top players versus lower ranked ones. It would help you get at what is actually captured in the data of leaderboards versus what isn't for instance.
- If you're interested in what distinguishes top players, you might consider augmenting with data on player demographics (age, region, playtime, etc.) or background (previous competitive experience, streaming presence). This would allow you to analyze whether certain types of players are more likely to reach the top of the ladder and what factors beyond in-game stats might contribute to competitive success. However, I will caution you that demographics are often difficult to determine and so you will want to think carefully about what you can actually collect and verify. You could also look at the economics of sponsorship and streaming for top players, which would connect to the broader theme of competitive gaming as a cultural and economic phenomenon.
- As I mentioned, I'm not familiar with this game, but you might be interested in the reception of top players so you could compile social media or forum posts to look at how being the top of leaderboards or certain players are received.

These are all suggestions though. I think at it's core you need to you need to articulate why Valorant specifically is worth studying. Is it your interest in game dynamics or is it more about Valorant's role in gaming communities? Whatever your angle, connect it to broader questions about competitive gaming culture. Why does this particular game and dataset help us understand something meaningful about digital competition, skill measurement, or gaming communities? The danger here is that you treat this as a statistics exercise—running correlations, building predictive models, clustering players—without any cultural interpretation or critical engagement with what the data represents. This course requires you to think about data as culturally constructed and meaningful, not just as numbers to analyze.

Ask yourself:

- What cultural assumptions underlie leaderboard ranking systems?
- How do players experience and interpret their rank differently than the numbers suggest?
- What aspects of competitive skill are made visible vs. invisible by stat tracking?
- How does the existence of leaderboards shape how people play the game?

These are cultural questions that require you to augment quantitative data with qualitative context. Your insider knowledge of Valorant is valuable, but you need to translate that into a clear analytical project. Happy to discuss more how to turn your familiarity with the game into a meaningful cultural data project!

### Javier

Your focus on game genres and how they evolve over time is compelling, and I appreciate your conceptual sophistication in recognizing that genres are not simple labels but "built from repeated mechanics and design patterns that change over time." This shows you're thinking about genres as cultural constructs rather than natural categories, which is exactly the kind of critical perspective this course encourages. The temporal scope (1980-2023) is ambitious and could yield interesting insights about how game categorization has evolved alongside the industry itself. You've also helpfully documented what's in the dataset and how it relates to the group theme.

As with everyone in your group, your first responsibility is verifying this existing dataset. According to the Kaggle page, this data was scraped from a website called Backloggd. I checked, and the site is indeed still running, which is good news—–it means you can trace the data back to its source.

Your verification work should include seeing what's currently on the site, how it compares to the dataset, and understanding the site's purpose and user base. This will help you understand what the data actually represents and how it was constructed. Specifically, Backloggd is a social cataloging site for gamers, similar to Goodreads for books or Letterboxd for films. Users log games they've played, want to play, or are currently playing. This context matters—the data reflects what games Backloggd users care about tracking, which may skew toward certain types of games or eras. So you might consider what games are included vs. excluded? Mobile games? Flash games? Indie titles? The dataset claims to cover "popular" games, but whose definition of popular? Backloggd's user base? Sales figures? Critical acclaim? And that gets you to the big question of where do Backloggd's genre labels come from? Are they user-generated tags? Industry-standard categories? Site moderator classifications? This fundamentally affects what you can claim about genre evolution.

Additionally, you might trying using the Wayback Machine to examine Backloggd's history. When was it founded? How has its genre taxonomy changed over time? Understanding the site's own evolution will help you contextualize the dataset's construction and assess whether these labels reflect something from Backloggd or broader industry or community practices.

Since you're working with existing data, you must augment it meaningfully. Based on your interest in how genres emerge and evolve, here are some potential approaches:

- You mention that genres are built from "repeated mechanics and design patterns." You might consider trying to create a more granular coding system that gets at those mechanics and design patterns. You wouldn't have to do it for all the games (obviously) but it might help you get at what is missing from these genre labels.
- You might find or create a dataset that tracks when certain mechanics and design patterns became possible with technological shifts (e.g., 3D graphics enabling open-world games). You could then analyze how genre labels correlate with these technological affordances over time. This would help you understand genre as a product of both cultural and technical evolution.
- Consider what other genre systems exist in the gaming industry or academic literature. Are there alternative ways to categorize games that might be more useful or accurate than Backloggd's current taxonomy? You might try to compare across sites (e.g., Steam tags,  Wikipedia genre labels) to see how different platforms categorize the same games differently. This would reveal genre as a contested and constructed system rather than a fixed reality.

These are just suggestions though! I would highly recommend you think about how you plan to scope this dataset. You have an enormous timespan so do you want to focus on critical periods or deep dive into specific genres? Do you want to analyze how genre labels changed for specific games over time? Do you want to look at boundary cases that challenge genre definitions? Do you want to examine how genre labels correlate with sales, player engagement, or critical reception? There are many possible angles here, but you'll need to narrow your focus to make it manageable and meaningful.

There's substantial work in digital humanities on literary genre classification and evolution that would inform your project. Look for work using computational approaches to genre (topic modeling, clustering, network analysis) as potential methodological models. In game studies specifically, scholars have critiqued genre as a framework and examined how industry categorization shapes development and marketing, so you might look at research on indie games or regional genre differences as well.

Overall, your recognition that genres are constructed, not natural, is exactly the right starting point. Now you need to design a project that can actually demonstrate *how* and *why* they're constructed the way they are, and what that reveals about gaming as culture. What specific aspect of genre evolution can you meaningfully examine with augmented data from Backloggd? Happy to discuss further as you develop your project!

### Hongli

I appreciate your interest in the evolution of the gaming industry and esports, and your focus on metrics like player activity, tournament dynamics, technology adoption, mobile gaming, streaming services, and AR/VR is timely and relevant to the group's theme. However, I have a serious concern about your dataset choice that we need to address immediately.

The dataset you've selected explicitly describes itself as containing **"realistic, synthetically generated data"** on the Kaggle page. This means the data is entirely fabricated—–it was created through simulation rather than collected from real-world gaming activity, tournaments, or player behavior. This is a critical issue for this course.

The core problem is verification. A central requirement of this course—–especially when working with existing datasets—–is that you must verify data quality, understand its provenance, trace it back to original sources, and assess its completeness and accuracy. With synthetic data, there is nothing to verify. The data doesn't represent actual events, players, tournaments, or industry trends. It represents a simulation of what the dataset creator thought these patterns might look like.

This fundamentally undermines the course's learning goals. We're studying culture through data, which requires engaging with how real cultural phenomena are captured, measured, and represented. Synthetic data sidesteps all of these questions. You can't learn about the challenges of data collection, the politics of what gets measured, or the gaps between cultural reality and data representation when the data was simply made up.

I want to acknowledge that your research interests are strong. You want to understand:

- How the gaming industry has evolved from 2010-2025
- Long-term trends in gaming revenue, player participation, and esports development
- How mobile gaming, streaming services, and AR/VR influence industry growth
- Regional variations in gaming culture and economics

These are all excellent questions worthy of investigation. The problem isn't your interests–—it's that you've chosen a dataset that cannot answer these questions because it doesn't represent reality.

**I cannot approve the synthetic dataset for this course.** However, I want to support you in finding an appropriate alternative, so I am giving you one week to resubmit your dataset proposal with a real dataset that can be verified and meaningfully augmented. There are many real datasets available on gaming industry trends, player behavior, esports tournaments, and platform usage that could support your research questions. You just need to find one that is based on actual data rather than simulation. Please reach out if you have questions about finding alternative datasets or want to discuss your options. I want to see you succeed in this project, but that requires working with real data that you can verify, critique, and augment meaningfully.

**Deadline: One week from February 16 to resubmit your dataset proposal with a real (non-synthetic) dataset.**

### Raymond

Your focus on the relationship between game ownership and active participation is a compelling angle that gets at how people relate to games as commodities, collections, and experiences. You've also helpfully documented what's in the dataset (game titles, release dates, estimated owners, peak concurrent users, pricing, age requirements, languages, DLC counts) and explained how it connects to the group theme.

According to the Kaggle page, this dataset appears to have been collected from the Steam API, which is promising—–Steam is a major platform with substantial public data. Your first task is verifying this dataset's quality and understanding how it was constructed. Presumably, if you're interested in gaming, you have a Steam account. So you might select random games from the dataset and compare the data to what's currently visible on Steam's store pages and community hubs. What matches? What's different? What might have changed since data collection? Steam's public API provides some data freely, but not everything. What was actually accessible through the API versus what might have been estimated or scraped from other sources? The "estimated number of owners" field is particularly interesting—–how is this estimate calculated? Also you might want to consider when was this data collected and how that shapes this data? Steam's ecosystem changes constantly—–games are removed, concurrent player counts fluctuate, ownership grows. Is this a snapshot at one moment, or does it track changes over time? Finally, how much coverage does this dataset have? Steam has tens of thousands of games—–does this dataset include all of them, or only a subset? If it's a subset, how was it selected? Are certain types of games over- or under-represented? For instance, are indie games, mobile ports, or non-English titles included? Understanding the dataset's construction and limitations will be crucial for making valid claims about ownership versus engagement patterns.

Understanding the dataset's construction and limitations will be crucial for making valid claims about ownership versus engagement patterns.

Your core question—–examining the gap between games that are widely owned but rarely played versus games with smaller player bases but high activity—–is genuinely interesting. However, you need to think carefully about what "active participation" actually means in the data. The dataset includes "peak concurrent users (CCU)" as a measure of engagement, but this is a very limited metric. CCU captures how many people are playing at the same time, but it doesn't capture how long people play, how deeply they engage, or whether they return to the game over time. A game might have a high CCU on launch day due to hype and marketing but then drop off quickly. Another game might have a smaller but more dedicated player base that sustains over years. So you need to be cautious about equating CCU with "active participation."

You also state that you want to use "clear and measurable data rather than rankings or subjective evaluations," which I understand as a desire for objectivity. However, I need to push back on this framing gently. This course is fundamentally about the interpretive work of turning culture into data—–there is always subjectivity involved. For instance, even seemingly "clear and measurable" metrics require interpretation:

- What does it mean if a game has high ownership but low CCU? Is it a bad game? A single-player game with no replay value? A game bought on sale and never installed? A game completed and moved on from?
- What does "engagement" actually measure? Time played? Emotional investment? Community involvement? Player satisfaction?
- Are ownership and CCU even the right metrics for what you want to understand about player relationships to games?

You'll need to make interpretive choices about what these numbers represent and what they don't capture. Embracing this interpretive dimension will strengthen your project, not weaken it.

Since you're working with existing data, you must augment it to meet course requirements. Here are several possible approaches based on your interest in ownership versus engagement:

- You might consider either creating from scratch or finding datasets that capture other forms of engagement beyond CCU. For instance, you might scrape social media or community forums to measure discussion activity around each game. Is there any relationship between ownership and community engagement? Do games with high ownership but low CCU have active communities, or are they silent backlogs? 
- You might consider trying to augment by exploring what games get heavily marketed and how that correlates with ownership and engagement. Are there games that are widely owned due to marketing hype but fail to sustain player interest? Conversely, are there games that build strong communities and engagement without massive marketing budgets? This would connect to broader questions about the economics of attention in gaming culture.
- You might consider how changes in Steam's platform and policies over time have affected ownership and engagement patterns. For instance, the rise of digital distribution, the introduction of sales and bundles, changes in refund policies, or shifts in recommendation algorithms could all influence how people buy and play games. Analyzing these temporal dynamics would add depth to your analysis of ownership versus engagement.

The ownership versus active participation question is genuinely interesting because it highlights a tension in contemporary gaming culture: abundance creates backlogs, marketing creates impulse purchases, and actual engagement is selective. What specific aspect of this dynamic can you illuminate with augmented Steam data? Happy to discuss more how to turn this into a meaningful cultural data rather than just statistical description!