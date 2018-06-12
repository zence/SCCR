# SCCR

- This is where I will build my program until I have a name for it
  - EDIT 18-May-18: I deleted previous parts of this file because they were not helpful and they made me look really stupid

## 18 May, 2018

* Lime may not be the solution to what we are looking for
  * Instead, I have found this blog post that contains a simple function I can use to view the weight of each feature
    * https://medium.com/@aneesha/visualising-top-features-in-linear-svm-with-scikit-learn-and-matplotlib-3454ab18a14d

## 4 June, 2018

* The C50 package in R is neat
  * It allows for printing off used rules as well as cross-validation

## 12 June, 2018

* We have compared SVM and RandomForest classifiers in her2 positivity
  * SVM seems to have an easier time classifying her2 negative samples
  * RF struggles, but that may be because we are using Stratified K fold cross validation instead of the RF functionality

* I am now testing different groups of genes to see if we can improve accuracy

1. Just ERBB2
   * __AVG AUC:__ 0.7106403495743
2. Genes that Dr. Piccolo gave me
   * __AVG AUC:__ 0.7494731630026

* I'm going to try the same thing with SVM (just for kicks and giggles)

1. Just ERBB2
   * __AVG AUC:__ 0.7514569716776001
2. Genes that Dr. Piccolo gave me
   * __AVG AUC:__ 0.7279307783719
