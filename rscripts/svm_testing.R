require(mlr)
require(readr)

total_her2_expr <- as.data.frame(read_tsv("../data/all_genes_TPM.tsv"))

rdesc <- makeResampleDesc("CV", iters = 10)

rdesc

names(total_her2_expr) <- make.names(names(total_her2_expr))

her2.task <- makeClassifTask(data = subset(total_her2_expr, select = -c(Sample)), target = "her2_status_by_ihc")

summary(her2.task)

svm.lrnr <- makeLearner("classif.svm", kernel = "radial", predict.type = "prob")

resamp <- resample(svm.lrnr, her2.task, rdesc, measures = list(mmce, acc, auc))

summary(resamp)
