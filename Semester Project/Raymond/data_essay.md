# Data Essay: Making "Mainstream" — A Video Game Dataset from 1978 to 2025

## How This Started

When I first thought about what kind of cultural dataset I wanted to build, I kept coming back to video games. Partly because I play them, but also because I kept wondering what it actually means for a game to be "mainstream." Like, everyone agrees that *Grand Theft Auto V* is mainstream. But what about *Undertale*? What about *Among Us*, which almost nobody was playing until suddenly everyone was? These didn't become mainstream in the same way, and I wasn't sure any existing list really captured that difference.

That question — what makes a game mainstream, and how do you turn that into data — ended up being the core problem I kept running into throughout this whole project.

## What I Made and Why

The dataset I built tracks mainstream video games from 1978 to 2025. The final version has 683 entries across 12 fields: title, release year, decade, primary genre, subgenre, platform, developer, publisher, mainstream signal, inclusion reason, and discovery source.

I started with 84 games I curated manually. These came from cross-referencing Wikipedia's best-selling games lists, Metacritic's all-time rankings, and The Game Awards' GOTY history. From there, I expanded the dataset computationally using the Steam Games Dataset from Kaggle, which added another 599 entries filtered by estimated ownership (I only pulled in games with at least 2 million estimated Steam owners).

The reason I wanted to mix these two methods is that neither one alone does a good job of capturing what "mainstream" actually means. A purely sales-based list is going to overrepresent PC and console blockbusters and miss out on titles like *Pokémon GO* or *League of Legends*, which were massive societal phenomena but don't neatly show up in boxed-unit sales. And a purely critical list is going to reflect what game journalists think matters, which isn't always the same as what a hundred million people were actually playing.

So I defined "mainstream" using four signals: best-seller status, critical canon inclusion, Game of the Year recognition, and social impact (e.g., defining a genre, becoming an esports staple, or blowing up during the pandemic). A game only needed to meet one of these to qualify.

## The Role of Computation

Computation showed up at basically every stage of this project, but in pretty different ways depending on what I was trying to do.

During the manual phase, I used Python to help normalize and structure the records. The actual selection decisions were mine — I was looking at Wikipedia lists, comparing sources, and making judgment calls about which titles belonged — but once I had a list of candidates, I used scripts to clean up inconsistent formatting, standardize genre labels, and make sure the CSV was consistent. That kind of computational work is easy to undervalue. It's not glamorous, but without it, the dataset would have been a mess of inconsistent capitalization and conflicting date formats.

The scaling phase was more clearly computational. I wrote a Python script that filtered the Kaggle Steam dataset by estimated ownership thresholds, inferred genre labels from Steam's tag system, and merged the results with my existing 84 entries while deduplicating by title. The script processed over 122,000 rows and brought the dataset from 84 to 683 entries.

But here's what I didn't fully appreciate until I was actually doing it: computation at scale doesn't just speed up the process, it also changes what kinds of decisions are even possible. While working through 84 games manually, I could think about each one individually. Is *Hades* mainstream? It won a lot of awards, it's critically beloved, but it's still an indie roguelike — so I thought about that and made a call. At 683 entries, I can't do that anymore. The genre classifications for the Steam-sourced entries are based on tag inference logic I wrote, and while I think the logic is reasonable, it's making calls I would have made differently if I'd been doing them by hand. That shift from close reading to rule-based abstraction is real, and it's worth being honest about.

## How Scale Changed Things

Mél Hogan and Tamara Shepherd, writing about data and infrastructure, argue that datasets are never neutral containers — they always reflect the conditions under which they were built. I kept thinking about that while working on the scaling phase of this project, because the Kaggle Steam dataset has a very specific set of built-in assumptions.

Steam is dominated by PC gaming. It tilts heavily toward Western markets and toward certain genres — action games, shooters, RPGs — that do well on PC storefronts. The dataset I built reflects that. My 84 manually curated games have a deliberate cross-era, cross-platform spread: arcade games from the late 1970s, console exclusives from the 1980s and 1990s, mobile phenomena, and esports titles. The 599 Steam-sourced entries are almost entirely PC games from the 2000s onward, and the decade distribution shows it clearly — 406 of those entries are from the 2010s alone.

So scaling up gave me more data, but it also narrowed the scope of what that data actually represents. A researcher looking at my full 683-entry dataset might come away thinking that the 2010s were uniquely dominant in gaming history, when really I'm just seeing the decade where Steam grew fastest. That's a distortion introduced by the source, not by the phenomenon itself.

This is something Catherine D'Ignazio and Lauren Klein discuss in *Data Feminism* — the idea that what gets counted and who does the counting shape what the data ends up saying. My manual curation tried to push against the assumption that mainstream means PC games with high Steam ownership. The scaled version pulled back in that direction, because that's what the available data supports.

## Limitations

The most honest thing I can say about this dataset is that "mainstream" is doing a lot of work that it can't quite support.

For the manually curated section, "mainstream" is a judgment call that reflects my familiarity with gaming history and the sources I consulted. I leaned on English-language Wikipedia lists and a US-centric awards show, which means the dataset probably underrepresents games that were mainstream in East Asian markets, or games that were huge on mobile platforms in South and Southeast Asia, or games that mattered regionally but never crossed into global visibility.

For the Steam-sourced section, "mainstream" basically means "had a lot of Steam owners," which is a much narrower definition. It excludes console-exclusive titles entirely (there's no *God of War* from Steam data, no *Halo*, no Nintendo exclusives), and it's heavily weighted toward free-to-play titles with inflated ownership numbers.

Genre classification is another real limitation. Many of the games in this dataset resist clean genre labels. *Dark Souls* is an action game, an RPG, and something so distinct it spawned its own genre name (Soulslike). I forced it into "Role-playing" because that was the closest match in my controlled vocabulary, but that label loses real information. At 84 games, these calls felt defensible because I could justify each one. At 683, I'm less confident.

Finally, the most recent entries — anything from 2023 onward — are hard to evaluate historically. *Clair Obscur: Expedition 33* is listed here because it won a GOTY award, but whether it ends up being a genuinely significant game in the medium's longer history is something nobody can know yet.

## Moral and Privacy Considerations

Because this dataset covers only commercial games and publicly available metadata (release years, developers, sales figures from published lists), there aren't major privacy matters for individual users. No personal data is collected or represented.

That said, there are subtler ethical aspects worth acknowledging. The dataset is partly built on ownership and sales data, which tend to favor large studios with the resources to market globally. Representing *Undertale* or *Hades* alongside *GTA V* or *Minecraft* treats them as equivalent data points, even though the conditions of their production and distribution were wildly different. A solo developer making a game on their own and a major corporation releasing a blockbuster shouldn't be flattened into the same row, lacking that context being visible somewhere.

I partially addressed this through the `mainstream_signal` field, which flags whether a game's inclusion was driven by sales, critical recognition, esports presence, social impact, or community acclaim. That at least lets a future user sort and filter by the type of mainstream-ness, rather than treating all 683 entries as equivalent.

## What I Learned

The thing I keep coming back to is how much the initial framing constrains everything that comes after. I defined "mainstream" early on, set the terms for what that word would mean in this dataset, and then spent the rest of the semester working within those constraints. When I expanded the dataset, I didn't really get to revisit the definition — I just had to find a way to apply it at scale, which meant accepting that the scaled version would be a rougher approximation of the original one idea.

That's probably unavoidable, but it made me understand why the assignment asked us to start small. When I was curating 84 games by hand, I understood every decision I was making. Now that there are 683 entries, I understand the logic behind the script that generated them, but I can't claim the same familiarity with the individual rows. That's a real difference, and I think it's the honest version of what "scale transforms data work" means in practice.

I also learned that cleaning data is most of the work and almost none of the credit. The genre normalization, the deduplication, the decision about whether to use initial release year or the most recent major release — none of that is visible in the final CSV, but it took more time than almost anything else in this project.

## Situating This inside Broader Scholarship

This project sits within a growing body of digital humanities and critical data studies work that takes seriously the idea that datasets are constructed objects, not neutral records of reality.

Johanna Drucker's concept of "capta" (rather than "data") is useful here — the argument that what we think of as raw data is always already interpreted, captured under particular conditions for particular purposes. Every game in this dataset is there because it met criteria I chose, appeared in sources I consulted, and fit the labels I defined. None of that is unbiased, and the dataset shouldn't be read as if it were.

The Responsible Datasets in Context project, which this assignment was modeled on, makes a similar point when it argues that data cannot be analyzed responsibly without knowing its provenance and limitations. The documentation I've tried to write for this dataset is an attempt to make those things legible — not to claim that the dataset is comprehensive or unbiased, but to be honest about what it is and how it came to be.

For a future researcher, the most useful thing I can say is probably this: the manually curated 84-entry section is a defensible interpretive sample of gaming history as I understand it, based on the sources I used. The Steam-sourced 599-entry section is a filtered slice of PC gaming from roughly 2005 to 2024, weighted toward high-ownership titles. They're both in the same CSV file, but they were generated differently and answer different kinds of questions.

---

*Dataset repository: [is310-spring-2026-group-2](https://github.com/CultureAsData-UIUC/is310-spring-2026-group-2/tree/main/Semester%20Project/Raymond)*

*Sources cited:*
- D'Ignazio, Catherine, and Lauren Klein. *Data Feminism*. MIT Press, 2020.
- Drucker, Johanna. "Humanities Approaches to Graphical Display." *Digital Humanities Quarterly* 5, no. 1 (2011).
- Hogan, Mél, and Tamara Shepherd. "Information Ownership and Materiality in an Age of Big Data Surveillance." *Journal of Information Policy* 5 (2015): 6–31.
- Responsible Datasets in Context Project. https://www.responsible-datasets-in-context.com/.
