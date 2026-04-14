# Individual Article Analysis

## Article Summary Information

- **Author:** Adrian Demleitner
- **Title:** Observing the Coming of Age of Video Game Graphics: Exploring the historical development of video game graphics through distant viewing, hermeneutics and image clustering
- **Venue:** Journal of Open Humanities Data
- **Year:** 2024
- **DOI:** https://doi.org/10.5334/johd.251
- **Paper:** https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.251
- **Code Repository:** https://github.com/thgie/vhs-dataset (also archived at https://doi.org/10.5281/zenodo.13349250)

---

## Part 1: AI Summary

**Prompt used:** "Summarize the article 'Observing the Coming of Age of Video Game Graphics: Exploring the historical development of video game graphics through distant viewing, hermeneutics and image clustering' by Adrian Demleitner (2024, Journal of Open Humanities Data) in 1–2 paragraphs, focusing on the data, computational methods, and main findings."

**AI-generated summary:**

This article investigates the historical development of video game graphics from the 1960s to 1990 using a distant viewing approach. The author compiled a large dataset of video game screenshots drawn from early computing platforms across multiple geographic regions, including games from the USA, Japan, and Europe. Rather than focusing on a few canonical titles, the study deliberately includes lesser-known and under-researched games to build a broader picture of how game visuals evolved. The data is processed using the computer vision model DINOv2 to generate image embeddings, which are then visualized using the dimensionality reduction technique UMAP and clustered using k-means, all implemented through the open-source toolkit FiftyOne.

The main findings suggest that the distant viewing approach can reveal large-scale patterns in video game graphics history that would be difficult to observe through traditional case-study methods, such as the gradual shift from text-based representations to pixel-based graphics and eventually 3D imagery. The study identifies meaningful clusters that correspond to different aesthetic and technical traditions across hardware platforms and regional contexts. However, the author also acknowledges significant limitations: the computer vision model struggles to recognize game-specific interface elements known as ludemes, and the static screenshot format fails to capture the temporal and animated dimensions of video game graphics. The article concludes that while this computational approach is promising, it requires further refinement, including the development of domain-specific models trained on annotated game data.

---

## Part 2: Critical Assessment

**What is the Data?**

The cultural data in this study consists of thousands of screenshots taken from video games released between approximately 1960 and 1990, spanning multiple hardware platforms such as the PC-88, Super Nintendo, and various early home computers. The screenshots were collected from existing video game archive platforms and digital preservation repositories, meaning the dataset's composition is shaped by what has already been digitized and made publicly available — not necessarily what was most culturally significant or representative at the time of release. This is a meaningful gap: games from North America and Japan are likely over-represented, while games from regions such as Eastern Europe, South America, or Australia may appear only sporadically, despite the author's stated intention to include under-researched regional contexts. Additionally, because the data consists only of static screenshots, it fundamentally cannot capture movement, animation, sound, or the interactive dimension of video game graphics — all of which are central to how players actually experience a game's visual design. The scale is large enough to enable pattern detection, but the dataset's boundaries are set by archival availability rather than principled cultural sampling.

**How is Computation Used and Why?**

The article uses computation primarily for analysis: the author applies the self-supervised vision transformer model DINOv2 to generate numerical embeddings for each screenshot, then uses UMAP for dimensionality reduction and k-means clustering to group visually similar images. The purpose is to identify large-scale aesthetic and historical patterns across the dataset that would be impossible to detect through close reading of individual games. Computation here is genuinely necessary — no human researcher could meaningfully compare thousands of screenshots manually and extract structured visual patterns at this scale. The choice to use DINOv2 rather than other models (like Inception-v3 or ResNet-101, which were tested and rejected) reflects a real methodological decision with consequences for what gets clustered together and why. However, the article is candid that the model was not trained on video game data and therefore fails to recognize ludemes — game-specific visual elements tied to rules and gameplay — which means that computationally derived clusters reflect general visual similarity rather than the culturally specific logic of how games actually look and function. The method reveals genuine patterns, but those patterns are shaped by what a general-purpose vision model is designed to see, not by what game scholars would identify as meaningful.

---

## Part 3: What AI Missed

The AI summary does a reasonable job of conveying the article's general structure: it correctly identifies the dataset, the use of DINOv2 and UMAP, and the finding that the approach reveals broad historical patterns. However, it glosses over several important methodological tensions that the article itself addresses quite honestly. Most notably, the AI treats the failure to recognize ludemes as a minor limitation rather than what it actually is — a fundamental challenge to the validity of the clustering results. If the model cannot distinguish game-specific interface elements from general visual textures, then the clusters do not necessarily map onto anything meaningful in game culture; they map onto what a vision model trained on general internet images happens to perceive as similar. The AI also does not mention that the dataset is constrained by archival availability, which quietly shapes which regional traditions appear in the analysis and which are excluded. Finally, the AI summary does not engage with the article's reflexive discussion of how different model and visualization choices (UMAP vs. t-SNE, DINOv2 vs. Inception-v3) produced radically different clusterings — a point that reveals how much the "findings" depend on technical choices that are rarely made explicit in computational humanities work. Overall, the AI captured the what but missed the stakes of the how.
