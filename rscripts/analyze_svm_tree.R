require(readr)
require(C50)
require(caret)
require(ROCR)

svm_her2_expr <- as.data.frame(read_tsv("../results/svm_genes_TPM.tsv.gz"))

svm.her2_pos <- svm_her2_expr[which(svm_her2_expr$her2_status_by_ihc == "Positive"),]
svm.her2_neg <- svm_her2_expr[which(svm_her2_expr$her2_status_by_ihc == "Negative"),]
rm(svm_her2_expr)

pos_her2_data <- as.matrix(sapply(subset(svm.her2_pos, select = -c(her2_status_by_ihc, Sample, SVM_classified)), as.numeric))
target.pos_her2 <- as.factor(svm.her2_pos$SVM_classified)

colnames(pos_her2_data) <- make.names(colnames(pos_her2_data))

partition <- createDataPartition(target.pos_her2, p = 0.66, list = F)
# print(partition)

print("Pre c50")
results <- C5.0(pos_her2_data[partition, ], target.pos_her2[partition], trials = 1, rules = T)
summary(results)
predictions <- predict(results, pos_her2_data[-partition, ])
print(sum((as.numeric(predictions) - as.numeric(target.pos_her2[-partition])) == 0) / length(predictions))

predictions <- predict(results, pos_her2_data[-partition, ], type = "prob")
print(mean(predictions[,1] > predictions[,2]))

pred <- prediction(predictions[,2], target.pos_her2[-partition])
auc.tmp <- performance(pred, "auc")
auc <- as.numeric(auc.tmp@y.values)
auc

svm.tree <- C5.0(pos_her2_data[partition, ], target.pos_her2[partition], trials = 1, rules = F)
plot(svm.tree)
