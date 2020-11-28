#!/bin/bash

#SBATCH --job-name=mpi_ex
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=0:05:00
#SBATCH -p parallel
#SBATCH -o ./%j.out
#SBATCH -e ./%j.err
##SBATCH --mail-type=END,FAIL
##SBATCH --mail-user=atrupe@ucdavis.edu

source activate mpi

#export I_MPI_PMI_LIBRARY=/share/apps/slurm-18.08.0/gcc7/lib/slurm/mpi_pmix_v1.so

#mpirun -bootstrap slurm -n 4 python ./mpi_test.py
srun -n 4 python ./mpi_test.py
#srun -n 4 hostname
