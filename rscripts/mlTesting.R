#! /usr/bin/env Rscript
require(readr)

genes <- c('ACTB', 'B2M', 'GAPDH', 'GUSB', 'HPRT1', 'PGK1', 'PPIA', 'RPLP0', 'TBP', 'TFRC')
cellTypes <- c("BRCA", "COAD", "LUAD", "LUSC", "PRAD")

featureCounts <- as.data.frame(read_tsv("../../cancerproject/proj_090817/data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_FeatureCounts.txt.gz"))
#column_to_rownames(featureCounts, var = "X1")
rownames(featureCounts) <- featureCounts$X1
featureCounts$X1 <- NULL
#featureCounts$condition <- 'Tumor'
#featureCounts <- t(featureCounts)

cellStates <- data.frame(condition = rep("Tumor", ncol(featureCounts)))

normFeatureCounts <- as.data.frame(read_tsv("../../cancerproject/proj_090817/data/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FeatureCounts.txt.gz"))
rownames(normFeatureCounts) <- normFeatureCounts$X1
normFeatureCounts$X1 <- NULL
#normFeatureCounts$condition <- 'Normal'
cellStates <- rbind(cellStates, data.frame(condition = rep("Normal", ncol(normFeatureCounts))))

for (cellType in cellTypes){
  tumorIDs <- scan(paste("../../cancerproject/proj_090817/tumor_IDs/tumor", cellType, ".txt", sep = ''), character(), sep = '\t')
  tumorFC <- featureCounts[,which(colnames(featureCounts)%in%tumorIDs)]
  
  normalIDs <- scan(paste("../../cancerproject/proj_090817/normal_IDs/norm", cellType, ".txt", sep = ''), character(), sep = '\t')
  normalFC <- normFeatureCounts[,which(colnames(normFeatureCounts)%in%normalIDs)]
  
  cellStates <- data.frame(condition = rep("Tumor", ncol(tumorFC)))
  cellStates <- rbind(cellStates, data.frame(condition = rep("Normal", ncol(normalFC))))
  
  tumorFC <- as.data.frame(t(tumorFC)[,1:20])
  tumorFC$cell_state <- "Tumor"
  normalFC <- as.data.frame(t(normalFC)[,1:20])
  normalFC$cell_state <- "Normal"
  
  if (exists("totalFC")){
    totalFC <- rbind(totalFC, tumorFC, normalFC)
  }else{
    totalFC <- rbind(tumorFC, normalFC)
  }
}
