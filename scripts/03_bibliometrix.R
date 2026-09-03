# =================================================================
# 03_bibliometrix.R
# Science Mapping & Bibliometric Modeling with R 'bibliometrix' (v4.1.4)
# Study: Bibliometric Analysis of Machine Translation (2006-2026)
# Authors: TOGNON G. Jean-Paul & MOUSSE A. Mikael
# =================================================================

suppressPackageStartupMessages({
  library(bibliometrix)
  library(ggplot2)
  library(igraph)
})

# Load the serialised bibliometrix dataset
load("data/processed/bibliometrix_dataset_final.RData")

# 1. Main Bibliometric Overview
cat("Calculating bibliometric indicators...\n")
results <- biblioAnalysis(M, sep = ";")
summary(results, k = 10, pause = FALSE)

# 2. Bradford's Law Zones
cat("Evaluating Bradford's Law distribution...\n")
bradford_res <- bradford(M)
print(table(bradford_res$Zone))

# 3. Co-citation Network (Cited References)
cat("Generating Reference Co-citation Network...\n")
NetMatrix_CR <- biblioNetwork(M, analysis = "co-citation", network = "references", sep = ";")
net_cr <- networkPlot(NetMatrix_CR, n = 50, Title = "Co-Citation Network", type = "fruchterman",
                      labelsize = 0.7, cluster = "louvain")

# 4. Thematic Map (Callon's Centrality & Density)
cat("Building Strategic Thematic Map...\n")
thematic_map <- thematicMap(M, field = "DE", n = 250, minfreq = 10,
                            stemming = FALSE, size = 0.5, n.labels = 3, repel = TRUE)
plot(thematic_map$map)

cat("Bibliometrix analysis completed successfully.\n")
