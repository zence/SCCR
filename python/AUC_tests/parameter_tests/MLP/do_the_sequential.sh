#! /bin/bash

#SBATCH --time=24:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=3192M   # memory per CPU core
#SBATCH -J "MLP ER top genes"   # job name

python sequentialize.py