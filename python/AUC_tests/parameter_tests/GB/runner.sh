#! /bin/bash

#SBATCH --time=72:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=3192M   # memory per CPU core
#SBATCH -J "Norm Tester"   # job name

random_list="0 123 8858 10293 4839302 10 100 39203 8484 2998"
random_seeds=($random_list)

for i in $(seq 10);
do
  echo $i"th iteration"
  python norm_tester.py $1 ${random_seeds[`expr $i - 1`]}
done
