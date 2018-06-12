#! /bin/bash

#SBATCH --time=08:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=6192M   # memory per CPU core
#SBATCH -J "All_Genes_C50"   # job name

Rscript make_tree_c50.R --max-ppsize=500000
