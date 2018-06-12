require(readr)
require(caret)
require(C50)
require(VIM)
require(ggplot2)
require(partykit)

options(expressions = 5e5)

total_her2_expr <- as.data.frame(read_tsv("../data/all_genes_TPM.tsv"))
total_her2_data <- as.matrix(sapply(subset(total_her2_expr, select = -c(her2_status_by_ihc, Sample)), as.numeric))
target.total_her2 <- as.factor(total_her2_expr$her2_status_by_ihc)

colnames(total_her2_data) <- make.names(colnames(total_her2_data))

print("Before making results")
results <- C5.0(total_her2_data, target.total_her2, trials = 1, rules = F)
#summary(results)
print("After results")

pdf('../graphs/c50_tree.pdf')
plot(results)
dev.off()
