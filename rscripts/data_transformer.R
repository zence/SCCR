if (!(c("DESeq2", "readr") %in% installed.packages()[,"Package"])){
  source("https://bioconductor.org/biocLite.R")
  biocLite("DESeq2")
  install.packages('readr')
}

require(readr)
require(DESeq2)

featureCount <- as.data.frame(read_tsv("../data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_FeatureCounts.txt.gz"))

row.names(featureCount) <- featureCount$X1

featureCount$X1 <- NULL

her2.clinical <- as.data.frame(read_tsv("../data/her2_Clinical_Data.tsv"))

row.names(her2.clinical) <- her2.clinical$X1

her2.clinical$X1 <- NULL
her2.clinical$X2 <- NULL
her2.clinical$X3 <- NULL

her2.clinical <- as.data.frame(t(her2.clinical))
her2.scores <- subset(her2.clinical, her2_ihc_score == "3+" | her2_ihc_score == "0")
her2.scores <- her2.scores[order(row.names(her2.scores)), ]

featureCount <- featureCount[row.names(her2.scores)]

featureCount <- as.matrix(featureCount)

dsq.fc <- DESeqDataSetFromMatrix(countData = featureCount, colData = her2.scores, design = ~ her2_ihc_score)

vsd.fc <- vst(dsq.fc)

vsd.data <- as.data.frame(t(assay(vsd.fc)))

vsd.data <- cbind(vsd.data, her2.scores)

write.table(vsd.data, file = '../data/vsd_FeatureCounts_cleanscores.tsv', quote = F, sep = '\t', col.names = NA)

