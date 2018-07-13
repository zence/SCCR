#! /bin/bash

normscripts=$(echo run_*py)

for normscript in $normscripts;
do
  sbatch runner.sh $normscript
done
