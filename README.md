# Tutorial for using demon.csc cluster
Example and test code for getting started on the Linux cluster at the Complexity Sciences Center, UC Davis

## Getting Started:

For information on demon.csc and how to request access, visit http://csc.ucdavis.edu/Resources.html

Once you have an account, you can log on to demon with ssh:

    $ ssh <your_username>@demon.csc.ucdavis.edu
    
Use `scp` to transfer files between your local machine and demon; use `scp -r` to transfer directories.

I recommend using `conda` to manage your python packages and environments. You can install Anaconda from terminal on demon; find instructions here: https://stackoverflow.com/questions/28852841/install-anaconda-on-ubuntu-or-linux-via-command-line

and you can find detailed documentation on conda envirnoments here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

## Running and Managing Jobs with SLURM

When you log on to demon you are placed on the "head node". The head node should only be used to dispatch and manage jobs. All code should be run on "compute nodes". 
Compute nodes are grouped together into "partitions". You can view available partitions using 

    $ sinfo
    
Most jobs on demon should be run on the "parallel" partition. 

See what jobs are currently running or queued with

    $ squeue
    
You can view the status of just your jobs with 

    $ squeue -u <your_username>

Jobs will typically be run from the head node using SLURM scripts, described in more detail below. If you would like to interactively run code on demon, you can start a SLURM session on one of the compute nodes using

    $ salloc -p parallel

After running `salloc` you should see "salloc: Grandted job allocation". You can also check this using `squeue`. You should see a line with your user ID under `USER` and "bash" under `NAME`. It will also show that you are on the parallel `PARTITION` and tell you what compute node you are on. From here, you can activate a `conda` environment and run python code, e.g. `python code.py`. You can also open an `ipython` session, etc. When you are finished, simply type

    $ exit
    
and this will relinquish your allocation. 

## SLURM Scripts and mpi4py

I recommend the following workflow for running jobs on demon. Create a directory for the project from your home directory; the project directory I created for this tutorial is called `mpi_tutorials`. Put your python and SLURM scripts that you want to run in the project directory. I also recommend creating a `conda` environment for each project. I've included an [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) file that creates an environment called `mpi`, which my example scripts use. 
