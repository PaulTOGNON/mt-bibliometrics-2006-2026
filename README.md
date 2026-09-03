# Replication Package: Bibliometric Analysis of Machine Translation (2006–2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Source](https://img.shields.io/badge/Data%20Source-Dimensions%20AI-blue.svg)](https://www.dimensions.ai/)

This repository provides the complete replication package, curated datasets, and analysis scripts for the study:

> **A Bibliometric Analysis of Machine Translation Systems: Trends, Evolution, and the Emergence of Voice-to-Voice Translation (2006–2026)**  
> **Authors:** TOGNON G. Jean-Paul & MOUSSE A. Mikaël  
---

## 📁 Repository Structure

```text
mt-bibliometrics-2006-2026/
├── README.md                  # Project documentation & replication guidelines
├── LICENSE                    # MIT License
├── data/
│   ├── raw/                   # Raw metadata exported from Dimensions AI (Aug 20, 2026)
│   ├── processed/             # Cleaned & validated dataset (18,588 publications)
│   │   ├── dataset_validated_final.csv
│   │   └── bibliometrix_dataset_final.RData
│   └── subcorpora/            # Specialized subcorpora (S2S, LRL, African, Tonal)
├── scripts/
│   ├── 01_data_cleaning.py    # Deduplication, Cochran sampling & Cohen's Kappa
│   ├── 02_subcorpora.py       # Subcorpus extraction & intersection matrix
│   └── 03_bibliometrix.R      # Science mapping (co-citation, coupling, Callon map)
└── thesaurus/
    ├── keywords_thesaurus.csv # Keyword normalization thesaurus
    └── institutions_ror.csv   # GRID / ROR institution disambiguation
