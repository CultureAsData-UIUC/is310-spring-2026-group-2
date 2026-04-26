# Mainstream Video Games Dataset (1978–2025)

This folder contains my semester project submission for IS310. The project tracks mainstream video games from 1978 to 2025, examining how "mainstream" has been defined differently across eras — through sales, critical recognition, awards, and cultural impact.

## Folder Structure

```
Raymond/
├── Initial Dataset Submission/
│   ├── mainstream_video_games_dataset.csv   # original 84-entry bespoke dataset
│   ├── dataset_documentation.md            # methodology and interpretive decisions
│   └── next_steps_plan.md                  # scaling plan written before Spring Break
│
├── mainstream_video_games_dataset_expanded.csv   # final dataset (683 entries)
├── data_essay.md                                 # final data essay
└── README.md
```

## Files

### Final Submission

- `mainstream_video_games_dataset_expanded.csv`  
  The complete dataset with 683 entries. The first 84 rows are manually curated; the remaining 599 were collected computationally from the Steam Games Dataset (Kaggle), filtered by estimated ownership of 2 million or more.

- `data_essay.md`  
  A reflective essay covering how the dataset was made, how computation shaped the process, what changed at scale, limitations, ethical considerations, and how this work relates to broader digital humanities scholarship.

### Initial Dataset Submission (March)

- `Initial Dataset Submission/mainstream_video_games_dataset.csv` — original 84-entry dataset
- `Initial Dataset Submission/dataset_documentation.md` — full methodology documentation
- `Initial Dataset Submission/next_steps_plan.md` — scaling roadmap written before the computational phase

## Project Summary

The dataset defines "mainstream" using four signals: best-seller status, critical canon inclusion, Game of the Year recognition, and cultural/social impact. The final 683-entry version combines close manual curation with computational scaling via a Kaggle Steam dataset, and reflects on what gets gained and lost when cultural data moves from hand-curated to algorithmically generated.
