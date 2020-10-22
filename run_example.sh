#!/bin/bash

#SBATCH --job-name=mpi_ex
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=0:05:00
#SBATCH -p parallel
#SBATCH -o /home/%u/mpi_tutorial/results/result-1/%j.out
#SBATCH -e /home/%u/mpi_tutorial/results/result-1/%j.err
##SBATCH --mail-type=END,FAIL
##SBATCH --mail-user=atrupe@ucdavis.edu

source activate mpi 

mpirun -bootstrap slurm -n 4 python ./mpi_example.py

