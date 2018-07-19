#! /bin/bash

cd RF
rm -f slurm*
./sbatcher.sh
cd ../linear_SVM
rm -f slurm*
./sbatcher.sh
cd ../SVM
rm -f slurm*
./sbatcher.sh
cd ../LR
rm -f slurm*
./sbatcher.sh
cd ../GB
rm -f slurm*
./sbatcher.sh

