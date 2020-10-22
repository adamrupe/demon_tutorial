# add test_things.py module to path
import sys
sys.path.insert(0, "$HOME/source")

import numpy as np

from test_things import a_thing

# always include these lines of MPI code!
from mpi4py import MPI
comm = MPI.COMM_WORLD 
size = comm.Get_size() # number of MPI procs
rank = comm.Get_rank() # i.d. for local proc

run = 1

# if you have an external file with parameters as function of rank:

# params = load(param_file) # e.g. np.load(params.npy) or load from csv, etc.
# my_param = params[rank]


# if params are procedurally generated (quickly), can generate them here, e.g.
params = np.arange(1, size+1)
my_param = params[rank]

# perform local computation using local param
my_array = my_param * np.ones(5, dtype=int)

# save parameters to output file by printing 
print(a_thing(rank, size, my_param))

# save your results
save_dir = '/home/atr486/mpi_tutorial/results/result-{}/'.format(run)
save_file = 'array-{}'.format(rank)

np.save(save_dir+save_file, my_array)

# add a comm barrier so that param printing finishes first
comm.barrier()

# a simple example of cross-node computation using mpi
global_array = np.zeros(5, dtype=int)
comm.Allreduce(my_array, global_array, op=MPI.SUM)

# record the result in the output file
if rank == 0:
    print('global array sum: ', global_array)
