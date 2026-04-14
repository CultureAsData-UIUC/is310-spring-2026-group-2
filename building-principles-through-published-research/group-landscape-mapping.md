## This is the folder where we will do our group portion of the assignment

### Step 1: Share Your Critical Findings

**Jesus Vazquez – Article Overview**

My article, *Video Highlight Prediction Using Audience Chat Reactions* (Fu et al., 2017), looks at how audience chat from Twitch can be used to predict highlight moments in esports matches, specifically League of Legends. The data includes full match videos and synchronized chat messages, with highlights labeled by aligning highlight videos with the full matches. One important issue is that the highlights come from a single source, which means they reflect one perspective of what is important and may not capture the full range of viewer experiences.

The computational method combines computer vision and natural language processing into a multimodal deep learning model. The model analyzes both video frames and chat messages to predict highlights. Computation plays a major role in analyzing large-scale data that would be difficult to process manually, but it also introduces limitations. For example, the way highlights are labeled and how chat is interpreted can shape the results and reinforce certain biases. Overall, the article shows that computation is useful, but it does not fully capture the complexity of cultural meaning in esports.

**Javier Martinez - Article Overview**

The article, *FAIRGAMER: Evaluating Biases in the Application of Large Language Models to Video Games* (Shi et al., 2025), looks at bias in large language models when they’re used in video games as NPCs. The data isn’t from real players, it’s built using simulated game scenarios from different games, with things like race, nationality, and roles included in the prompts. That makes it easier to test, but it also doesn’t fully reflect real gameplay or how people actually interact in games. 

Computation is used to run these scenarios through different models and measure how their decisions change across groups. The authors use a benchmark to track bias by looking at patterns in decisions, not just single responses. This works well for large-scale analysis, but the results depend a lot on how the scenarios are designed.

Overall, computation is necessary here, but it also shapes what counts as “bias” in the first place. The AI summary got the general idea right, but it missed some details and didn’t fully explain some key parts. It also didn’t really explain that the data is simulated, which is important for understanding the limits of the study.

**Anshuman Satpute - Article Overview**

Nohar’s thesis uses machine learning on a merged Steam dataset (store metadata, player counts, and Metacritic scores) to predict each game’s Metascore as a proxy for player satisfaction. After extensive feature engineering, non‑linear models like Random Forest outperform linear regression and show that factors such as average player count, game age, developer/publisher history, and price are most influential in predicting critical reception.

### Step 2: Map How Computation Is Being Used

- Analysis:
  - Main: Jesus Vazquez
  - Comments: Javier Martinez

Across both articles, computation is primarily used for analysis by identifying patterns in large-scale data. In my article, computation analyzes both video frames and Twitch chat data using a multimodal deep learning model to predict highlight moments. The model detects patterns in visual intensity and audience reactions to determine what moments are considered important. This allows researchers to process thousands of frames and chat messages that would be impossible to analyze manually.

In Javier’s article, computation is also used for analysis but in a different way. Instead of real-world data, it uses simulated scenarios to test how large language models behave across different social categories. The models are evaluated by comparing patterns in their decisions to detect bias. This shows how computation can be used not just to find patterns, but to evaluate systems and measure fairness.

Together, both articles show that computation is being used to analyze complex datasets at scale, but the type of data (real vs simulated) changes what the analysis represents. While both approaches are effective, they also depend heavily on how the data is structured, which can influence the results and limit how well they reflect real cultural experiences.  

Comments:

You’re right that both papers use computation for analysis since they’re both finding patterns in data. But I don’t think they’re doing the same kind of analysis. In Fu et al., it’s really about analyzing real data like chat and video to figure out what moments matter. The *FAIRGAMER: Evaluating Biases in the Application of Large Language Models to Video Games* article, feels more like computation is being used to test the models by creating scenarios and checking for bias, not just analyzing existing data.

### Step 3: Find Trends, Divergences, and Silences

- Trends: Jesus Vazquez 

A clear trend across both articles is the reliance on computation to analyze large-scale datasets that would be difficult or impossible to process manually. Both studies use computational models to detect patterns, whether it is identifying highlight moments in esports or measuring bias in AI systems. This shows that computation is often used as a tool to scale analysis and make sense of complex cultural or social data.

Another trend is that both articles rely on structured datasets that are either constructed or simulated. In my article, highlight labels are created through alignment methods, while in Javier’s article, the data is fully simulated through designed scenarios. This suggests that a lot of computational cultural research depends on how data is built before analysis even begins.

Overall, these trends show that while computation is powerful, it often simplifies or reshapes the data in ways that can limit how accurately it represents real-world experiences.  

- Divergences: Javier Martinez

The two articles take very different approaches, and that really affects what their results mean. Fu et al. (2017) work with real Twitch data and actual game footage, using audience chat to predict highlights and treating those reactions as a signal of what matters in a match. On the other hand, Shi et al. (2025) create a controlled setup in which LLMs serve as game characters and are tested for bias using simulated scenarios with varying demographic traits. So one paper focuses on building a system that works in the real world, while the other focuses on testing and critiquing AI behavior. What’s at stake is the tradeoff between realism and control. Fu et al. capture real human reactions but risk carrying over hidden biases from those sources, while Shi et al. can clearly measure bias but in a setup that may not reflect real gameplay. In the end, it comes down to whether you trust messy real-world data or controlled experiments to better understand these systems.

Comments:
I believe your observation regarding realism versus control is quite significant, and it also reflects in the definitions of "bias" and "importance." Fu et al. take in whatever values are already present in Twitch highlights and chat, whereas Shi et al. clearly embed their assumptions into benchmark scenarios. In both cases, the computational framework subtly determines what is considered a meaningful event or a negative outcome, indicating that part of the difference arises not only from the data source but also from who has the authority to define the problem initially.

- Silences: Anshuman Satpute

One major silence across both articles is how little they engage with the lived experiences and perspectives of actual players. Fu et al. uses chat and highlight compilations as stand-ins for excitement, but they overlook who’s chatting, whose reactions are most prominent, and how toxicity, spam, or inside jokes influence what’s considered a “highlight.” On the other hand, Shi et al. create synthetic scenarios to examine bias in LLM-driven NPCs, but these scenarios are crafted from the researchers’ perspective, rather than being co-created with players or marginalized groups who could be most impacted by in-game bias. 

### Contributions

- Jesus Vazquez:
  - Completed full individual article analysis (AI summary, critical assessment, and AI critique)
  - Wrote Step 1 article overview
  - Wrote Step 2 (Analysis section)
  - Wrote Step 3 (Trends section)

- Javier Martinez:   
    - Completed full individual article analysis (AI summary, critical assessment, and AI critique)
    - Wrote step 1 article overview
    - Wrote step 2 (Comment section)
    - Wrote step 3 (Divergences section)

- Anshuman Satpute:
    - Completed full individual article analysis (AI summary, critical assessment, and AI critique)
    - Wrote step 1 article overview
    - Wrote step 3 (Comment section)
    - Wrote step 3 (Silences section)
