#! /bin/bash

#SBATCH --time=08:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=5192M   # memory per CPU core
#SBATCH -J "All_Genes_C50"   # job name

Rscript c50_testing.R --max-ppsize=500000
