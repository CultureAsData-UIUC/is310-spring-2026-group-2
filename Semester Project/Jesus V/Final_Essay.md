## Introduction

Esports has grown from small, informal competitions into a global industry where players compete in organized tournaments for large prize pools. As competitive gaming has expanded, it has also produced large amounts of structured data, including records of earnings, players, and tournaments. This makes esports a useful case for understanding how culture can be represented and analyzed through data.

This project examines esports earnings and competitive gaming as a way to explore how digital entertainment becomes professionalized and unequal over time. Rather than treating earnings as neutral statistics, this project uses them to understand which games receive attention, investment, and long-term support within the esports ecosystem.

The main question guiding this project is: how does esports earnings data reveal patterns of professionalization and inequality in competitive gaming? By creating, auditing, and expanding datasets, this project investigates how data both represents and simplifies complex cultural systems.

## Dataset Overview

This project is based on esports earnings data collected from publicly available sources. The primary dataset used is an esports dataset from Kaggle, which includes information on total earnings, number of players, and number of tournaments for a large number of competitive games. This dataset is likely derived from publicly available esports records such as those found on Esports Earnings.

In addition to the general dataset, I also used a historical dataset that tracks esports activity over time, including yearly earnings, player participation, and tournament counts. This allowed me to analyze not only individual games, but also broader trends in esports development over time.

The final dataset combines these sources and includes both original variables and newly created fields. At the game level, the dataset includes information about earnings, players, tournaments, and genre. It also includes new analytical variables such as earnings per player, earnings per tournament, and a tier system that categorizes games based on their competitive scale.

In addition to the game-level dataset, I created a yearly dataset that tracks esports growth over time, as well as a genre-level summary dataset that compares different types of games. Together, these datasets provide multiple ways to understand esports as both an economic and cultural system.

## Initial Dataset (Bespoke Work)

The project began with the creation of a small, bespoke dataset consisting of approximately 75 esports games. Rather than working at scale immediately, this step required manually selecting, organizing, and interpreting data on a game-by-game basis. The dataset was created using a genre-balanced sampling approach to ensure that different types of esports were represented, rather than focusing only on the highest-earning games.

This process involved several interpretive decisions. I had to determine which games to include, how to categorize them, and what information would be meaningful to capture. While the original dataset included fields such as total earnings, number of players, and number of tournaments, I added additional fields to provide more context, including competitive level and short descriptive notes.

Working with a small dataset made it clear that data is not simply collected but constructed. Even basic decisions, such as how to define a “major” esports title or how to categorize genres, required judgment and simplification. This stage of the project helped highlight the limitations of datasets and the importance of transparency in how data is created.

This initial dataset served as the foundation for later computational work, allowing me to better understand the structure and meaning of the data before expanding it at a larger scale.

## Audit Process

A key part of this project was auditing the original dataset to better understand its sources, accuracy, and limitations. Rather than treating the dataset as fully reliable, I attempted to trace it back to its likely origin and verify a sample of its entries.

The dataset appears to be based on publicly available esports records, particularly those found on Esports Earnings. To audit the data, I selected several well-known games, including Dota 2, Counter-Strike, and League of Legends, and compared their reported total earnings, number of players, and tournament counts with values from the source website.

This comparison showed that the dataset is generally accurate for major games, but it also revealed several limitations. First, some values appear slightly outdated, likely reflecting when the dataset was last updated. Second, early esports data, particularly from the late 1990s and early 2000s, is less complete and more difficult to verify. Finally, smaller or regional tournaments may not be fully captured in the dataset, meaning that certain parts of esports history are underrepresented.

This audit process demonstrates that datasets are not neutral or complete representations of reality. Instead, they are constructed from available records and shaped by what is documented, preserved, and made accessible. Understanding these limitations was important before building additional analysis on top of the dataset.

## Scaling and Computational Augmentation

After creating the initial bespoke dataset, the next step was to scale the project using computational methods. While the original dataset of 75 games required manual selection and interpretation, scaling allowed me to work with a much larger set of data and identify broader patterns across esports.

I used Python and the Pandas library to process and expand the dataset. This included cleaning the data, merging multiple datasets, and generating new variables. For example, I calculated earnings per player and earnings per tournament to better understand how value is distributed within different games. I also created a tier system and a professionalization score to compare the relative scale and development of different esports.

Scaling the dataset changed the nature of the project. In the initial stage, I was making decisions at the level of individual games. At scale, those decisions had to be translated into rules and calculations that could be applied across hundreds of entries. This required simplifying some concepts, such as how to define competitive tiers, and relying more on patterns in the data rather than detailed knowledge of individual games.

This shift highlights an important tension in working with cultural data. While computational methods make it possible to analyze larger datasets, they also require reducing complex cultural phenomena into measurable variables. As a result, scaling introduces both new insights and new limitations, as some forms of nuance are lost in the process.

## What the Dataset Reveals

Analyzing the dataset reveals several important patterns about how esports operates as a professional and economic system.

First, the data shows a strong concentration of earnings among a small number of games. Titles such as Dota 2, Counter-Strike, and League of Legends account for a large portion of total esports prize money. This suggests that esports is not evenly distributed across games, but instead dominated by a few highly visible and well-supported titles.

Second, the dataset highlights inequality within esports through measures such as earnings per player. While some games generate very high total earnings, those earnings are not always evenly distributed among participants. In some cases, a relatively small number of top players capture a large share of prize money, while the majority earn significantly less. This reflects a broader pattern of inequality in competitive systems.

Third, differences in earnings per tournament show that esports are structured in different ways. Some games rely on a small number of high-value tournaments, while others have many smaller events. This suggests that esports is not a single unified system, but a collection of different competitive models.

The historical data also shows that esports has grown significantly over time. Earnings, player participation, and tournament counts have all increased, especially in the past decade. This supports the idea that esports has become more professionalized, with more organized infrastructure and larger financial investment.

Overall, the dataset reveals that esports is a structured and unequal system, shaped by a combination of visibility, investment, and long-term support for certain games.

## What the Dataset Conceals

While the dataset reveals important patterns, it also conceals many aspects of esports as a cultural and social phenomenon.

One major limitation is that the dataset focuses primarily on prize money, which only captures a small part of the esports ecosystem. Many players earn income through sponsorships, streaming, and content creation, which are not reflected in tournament earnings. As a result, the dataset may underestimate the financial realities of professional gaming.

The dataset also simplifies complex player experiences. It treats players as numerical entries rather than individuals with careers, identities, and varying levels of access to opportunities. This makes it difficult to understand issues such as labor conditions, burnout, or barriers to entry within esports.

Another limitation is the uneven quality of historical data. Early esports tournaments are less well documented, which means that the dataset likely underrepresents older games and early competitive scenes. This can create the impression that esports has grown more rapidly than it actually has, when part of that growth reflects better documentation rather than actual change.

Additionally, the dataset tends to emphasize the most visible and successful games. Smaller or regional esports scenes may be missing or underrepresented, which reinforces the dominance of already popular titles. This reflects a broader issue in data collection, where what gets recorded often depends on visibility and institutional support.

Finally, some of the variables introduced in this project, such as Tier or RegionPopularity, involve simplifications and assumptions. While they help organize the data, they do not fully capture the complexity of global esports communities.

Overall, the dataset provides a structured view of esports, but it cannot fully represent the cultural, social, and economic complexity of competitive gaming.

## Ethics and Limitations

Working with esports data raises several ethical and methodological considerations. Although the dataset is based on publicly available information, the way the data is organized and interpreted can shape how esports is understood.

One important issue is that the dataset simplifies complex realities into numerical values. For example, representing player success through earnings can overlook other important factors such as stability, career longevity, or access to opportunities. This risks reinforcing a narrow view of success based only on financial outcomes.

There are also limitations in how certain variables were constructed. Fields such as Tier and RegionPopularity rely on interpretive decisions and generalizations. While they help organize the data, they may introduce bias or oversimplify global esports dynamics. For example, assigning a single region to a game does not fully capture the international nature of many competitive scenes.

Another concern is the uneven availability of data. Since larger and more visible esports events are better documented, the dataset may privilege well-funded games and regions while excluding smaller or emerging communities. This can reinforce existing inequalities by making dominant games appear even more central.

Finally, computational methods used in this project required translating complex cultural phenomena into measurable variables. While this allows for large-scale analysis, it also means that certain aspects of esports, such as player experiences or community dynamics, are not represented.

These limitations highlight the importance of approaching datasets critically and recognizing that data is not a complete or neutral representation of culture.

## Scholarly Context

This project connects to broader scholarly work on esports, digital labor, and the representation of culture through data. One useful framework comes from T.L. Taylor’s *Raising the Stakes*, which examines how competitive gaming has evolved into a professionalized system shaped by corporate investment, organized tournaments, and global audiences. Taylor argues that esports is not just a form of play, but a structured environment where labor, performance, and economic value are closely linked. This perspective helps frame the dataset as more than a collection of numbers, but as a representation of how professional gaming operates.

The project also relates to research on digital culture and data practices, particularly the idea that data is not neutral but constructed. Scholars in fields such as information science and media studies emphasize that datasets reflect the conditions under which they are created, including what is recorded, what is excluded, and how categories are defined. This is visible in esports data, where well-funded games and major tournaments are more likely to be documented, while smaller or regional scenes may be underrepresented.

Finally, this project connects to discussions of inequality in digital systems. The concentration of earnings among a small number of games and players reflects broader patterns seen in other cultural industries, where visibility and access are unevenly distributed. By analyzing esports through data, this project contributes to understanding how digital platforms and competitive structures shape opportunities within gaming.

Together, these scholarly perspectives help situate the dataset within a larger conversation about culture, labor, and the role of data in representing complex social systems.

## Reflection

Over the course of this project, my understanding of data changed significantly. At the beginning, I approached the dataset mainly as a collection of numbers that could be organized and analyzed. However, as I worked through the process of creating, auditing, and expanding the dataset, I realized that data is not neutral or objective. Every dataset reflects decisions about what to include, how to categorize information, and what is left out.

One of the biggest lessons for me was the importance of auditing data rather than simply trusting it. In my initial submission, I focused more on building the dataset and adding new fields, but I did not fully verify where the data came from or how accurate it was. After revising my work, I understood that tracing the dataset back to its source and identifying its limitations is a critical part of responsible data work.

I also learned that scaling data with computational tools changes how you interact with it. When working with a small dataset, I could think about each game individually and make detailed decisions. When scaling up using Python, I had to translate those decisions into rules and calculations, which required simplifying complex ideas. This showed me that while computation allows for larger analysis, it also reduces nuance.

Finally, this project helped me see how data can both reveal and hide important aspects of culture. While my dataset shows patterns of inequality and professionalization in esports, it does not fully capture the experiences of players or the social dynamics of gaming communities. This made me more aware of the limits of data and the importance of interpreting it carefully.

Overall, this project shifted my perspective from seeing data as something given to something that is created, shaped, and interpreted.

## Conclusion

This project demonstrates how esports earnings data can be used to understand the professionalization and inequality of competitive gaming. By combining manual data creation with computational scaling, the dataset reveals patterns in how certain games dominate the esports industry, how earnings are distributed among players, and how competitive structures differ across games.

At the same time, the project highlights the limitations of representing culture through data. While the dataset provides insight into economic trends and competitive systems, it cannot fully capture the experiences of players or the broader social context of esports. This reinforces the idea that data should be interpreted critically rather than taken as a complete representation of reality.

Overall, this project shows that working with culture as data involves both technical and interpretive work. It requires not only building and analyzing datasets, but also understanding how those datasets are constructed and what they leave out. By examining esports through this lens, the project contributes to a deeper understanding of how digital culture is organized, measured, and represented.