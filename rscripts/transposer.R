require(readr)

gene_expr_data <- as.data.frame(read_tsv("../../../cancerproj/project_090817/data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz"))

rownames(gene_expr_data) <- gene_expr_data$X1

gene_expr_data$X1 <- NULL

gene_expr_data <- as.data.frame(t(gene_expr_data))

gene_expr_data$Sample <- rownames(gene_expr_data)

clinical_data <- as.data.frame(read_tsv("../data/her2_Clinical_Data.tsv"))

make.true.NA <- function(x) if(is.character(x)||is.factor(x)){
                                  is.na(x) <- x%in%c("[Not Available]","[Not Evaluated]"); x} else {
                                  x}
clinical_data <- as.data.frame(lapply(clinical_data, make.true.NA))

row.names(clinical_data) <- clinical_data$X1

clinical_data$X1 <- NULL

clinical_data <- as.data.frame(t(clinical_data))

pos_her2 <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$her2_status_by_ihc == "Positive"),]))

neg_her2 <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$her2_status_by_ihc == "Negative"),]))

pos_her2_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% pos_her2),]

pos_her2_expr$her2_status_by_ihc <- "Positive"

neg_her2_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% neg_her2),]

neg_her2_expr$her2_status_by_ihc <- "Negative"

total_her2_expr <- rbind(pos_her2_expr, neg_her2_expr)

write.table(total_her2_expr, "../data/all_genes_TPM.tsv", sep = "\t", row.names = F, quote = F)
