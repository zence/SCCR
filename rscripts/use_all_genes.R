packages.to.install <- c()

if (!require(readr)){packages.to.install <- c(packages.to.install, "readr")}
if (!require(mlr)){packages.to.install <- c(packages.to.install, "mlr")}
if (!require(VIM)){packages.to.install <- c(packages.to.install, "VIM")}
if (!require(ggplot2)){packages.to.install <- c(packages.to.install, "ggplot2")}
if (length(packages.to.install)){install.packages(packages.to.install)}

library(readr)
library(mlr)
library(VIM)
library(ggplot2)

clinical_data <- as.data.frame(read_tsv("../data/her2_Clinical_Data.tsv"))

make.true.NA <- function(x) if(is.character(x)||is.factor(x)){
                                  is.na(x) <- x%in%c("[Not Available]","[Not Evaluated]"); x} else {
                                  x}
clinical_data <- as.data.frame(lapply(clinical_data, make.true.NA))

# aggr() shows how much is missing, and there is a lot missing
aggr(clinical_data[, 4:200 ])

row.names(clinical_data) <- clinical_data$X1

clinical_data$X1 <- NULL

clinical_data <- as.data.frame(t(clinical_data))

aggr(clinical_data)

pos_her2 <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$her2_status_by_ihc == "Positive"),]))

neg_her2 <- gsub("\\.","-", rownames(clinical_data[which(clinical_data$her2_status_by_ihc == "Negative"),]))

gene_expr_data <- as.data.frame(read_tsv("../../../cancerproj/project_090817/data/GSM1536837_06_01_15_TCGA_24.tumor_Rsubread_TPM.txt.gz"))

rownames(gene_expr_data) <- gene_expr_data$X1

gene_expr_data$X1 <- NULL

gene_expr_data <- as.data.frame(t(gene_expr_data))

gene_expr_data

ids <- rownames(gene_expr_data)

gene_expr_data <- as.data.frame(sapply(gene_expr_data, function(x){log2(x + 1)}))

rownames(gene_expr_data) <- ids

gene_expr_data

pos_her2_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% pos_her2),]

pos_her2_expr$her2_status_by_ihc <- "Positive"

neg_her2_expr <- gene_expr_data[which(rownames(gene_expr_data) %in% neg_her2),]

neg_her2_expr$her2_status_by_ihc <- "Negative"

total_her2_expr <- rbind(pos_her2_expr, neg_her2_expr)

colnames(total_her2_expr) <- make.names(colnames(total_her2_expr))

training.her2_expression <- sample(seq_len(nrow(total_her2_expr)), nrow(total_her2_expr) / 2)

training.ids <- c(sample(pos_her2, 150), sample(neg_her2, 150))

nrow(total_her2_expr[-which(row.names(total_her2_expr) %in% training.ids),])

as.numeric(total_her2_expr[training.ids, 'her2_status_by_ihc'] == "Positive")

task <- makeClassifTask(data = total_her2_expr, target = "her2_status_by_ihc")

rdesc <- makeResampleDesc("CV", iters = 10L)

discrete_ps <- makeParamSet(
  makeDiscreteParam("cost", values = c(0.5, 1.0, 1.5, 2.0, 2.5, 3.0)),
  makeDiscreteParam("kernel", values = c("linear", "polynomial", "radial"))
)

ctrl <- makeTuneControlGrid()

r <- resample(makeLearner("classif.svm", kernel = "linear", predict.type = "prob"), task, rdesc, measures = list(mmce, acc, auc))

#sink(file("all_results.txt", open = "w"), type = "output")
print(r$aggr)
#sink(type = "output")
#sink()

misclassied.ids <- c()

for (i in 1:nrow(total_her2_expr)){
  mini.predict <- r$pred$data[which(r$pred$data$id == i & r$pred$data$truth != r$pred$data$response),]
  #print(mini.predict)
  if (nrow(mini.predict) > 0){
    misclassied.ids <- c(misclassied.ids, rownames(total_her2_expr[i,]))
  }
}

print(length(misclassied.ids))

write.table(misclassied.ids, file = "../results/misclassified_ERBB2_FGFR1.tsv",  
            quote = F, sep = "\t", row.names = F, col.names = F)
