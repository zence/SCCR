require(readr)

gene_expr_data <- as.data.frame(read_tsv("../../../cancerproj/project_090817/data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz"))

rownames(gene_expr_data) <- gene_expr_data$X1

gene_expr_data$X1 <- NULL

gene_expr_data <- as.data.frame(t(gene_expr_data))

gene_expr_data$Sample <- rownames(gene_expr_data)

clinical_data <- as.data.frame(read_tsv("../data/er_Clinical_Data.tsv"))

make.true.NA <- function(x) if(is.character(x)||is.factor(x)){
                                  is.na(x) <- x%in%c("[Not Available]","[Not Evaluated]"); x} else {
                                  x}
clinical_data <- as.data.frame(lapply(clinical_data, make.true.NA))

row.names(clinical_data) <- clinical_data$X1

clinical_data$X1 <- NULL

clinical_data <- as.data.frame(t(clinical_data))

pos_er <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$er_status_by_ihc == "Positive"),]))

neg_er <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$er_status_by_ihc == "Negative"),]))

pos_er_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% pos_er),]

pos_er_expr$er_status_by_ihc <- "Positive"

neg_er_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% neg_er),]

neg_er_expr$er_status_by_ihc <- "Negative"

total_er_expr <- rbind(pos_er_expr, neg_er_expr)

write.table(total_er_expr, "../data/all_genes_er_Data.tsv", sep = "\t", row.names = F, quote = F)
