#! /bin/bash

normscripts=$(echo run_*py)
rm ../results/misclassified_samples.tsv

for normscript in $normscripts;
do
  sbatch runner.sh $normscript
done
