require(readr)
require(caret)
require(C50)
require(VIM)
require(ggplot2)
require(partykit)

total_her2_expr <- as.data.frame(read_tsv("../data/all_genes_TPM.tsv"))

total_her2_data <- as.matrix(sapply(subset(total_her2_expr, select = -c(her2_status_by_ihc, Sample)), as.numeric))
target.total_her2 <- as.factor(total_her2_expr$her2_status_by_ihc)

names(total_her2_data) <- make.names(names(total_her2_data))

partition <- createDataPartition(target.total_her2, p = 0.75, list = T)
print(partition)

print("Pre c50")
results <- C5.0(total_her2_data[unlist(partition), ], target.total_her2[unlist(partition), ], trials = 1, rules = F)
summary(results)
predictions <- predict(results, total_her2_data[-unlist(partition), ])
print(sum((predictions - target.total_her2[-unlist(partition), ]) == 0))

# pdf('../graphs/c50_tree.pdf')
# plot(results)
# dev.off()
