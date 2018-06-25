# SCCR

- This branch is primarily for the use of ipython notebooks in the browser. Although it lacks a profound amount of interactivity compared to Rstudio or VSCode/PyCharm, Jupyter lab allows me to run chunks of code rather than entire scripts as well as utilize the increased amount of RAM on kumiko

## June 25, 2018

- I have tested the different sorting methods that Dr. Piccolo asked me to run
  - SVM did not work well with either VST or Quantile Normalization
    - Both showed an AUC of about .71 with just ERBB2 and then .5 afterwards
  - Random Forest did show some promise
    - Both algorithms peaked at about .78 AUC, but the average auc of Quantile Normalization was more dismal
    - All in all, both algorithms showed a decrease after about the fourth or fifth series
