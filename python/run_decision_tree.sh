#! /bin/bash

#SBATCH --time=05:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=3192M   # memory per CPU core
#SBATCH -J "Decision Tree"   # job name

for i in $(seq 100);
do
  echo $i
  python decision_tree.py >> output_dt.txt
done
