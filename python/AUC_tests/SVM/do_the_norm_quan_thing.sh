#! /bin/bash

#SBATCH --time=48:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=3192M   # memory per CPU core
#SBATCH -J "SVM NormQuan"   # job name

python faster_sequentialize_norm_quan.py
