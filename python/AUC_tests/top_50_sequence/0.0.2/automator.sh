#! /bin/bash

cd GB
rm slurm*
sbatch do_the_thing.sh
cd ../rbf_SVM
rm slurm*
sbatch do_the_thing.sh
cd ../linear_SVM
rm slurm*
sbatch do_the_thing.sh
cd ../LR
rm slurm*
sbatch do_the_thing.sh
cd ../RF
rm slurm*
sbatch do_the_thing.sh
