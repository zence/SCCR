install.packages("readr")
require(readr)

#Fill this in with file location
clinical_data <- as.data.frame(read_tsv())

#Grab rows
# Use which() on column 'X1'
# i.e. clinical_data[which(clinical_data$X1 == "(insert desired row name)"),] 
#   OR clinical_data[which(clinical_data$X1 %in% (vector of desired row names))]


#Transpose data frame
clinical_data_transposed <- as.data.frame(t(clinical_data))
