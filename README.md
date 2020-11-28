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
    
If you need to, you can cancel a job using the `JOBID` listed in `squeue` with 

    $ scancel <JOBID>

Jobs will typically be run from the head node using SLURM scripts, described in more detail below. If you would like to interactively run code on demon, you can start a SLURM session on one of the compute nodes using

    $ salloc -p parallel

After running `salloc` you should see "salloc: Grandted job allocation". You can also check this using `squeue`. You should see a line with your user ID under `USER` and "bash" under `NAME`. It will also show that you are on the parallel `PARTITION` and tell you what compute node you are on. From here, you can activate a `conda` environment and run python code, e.g. `python code.py`. You can also open an `ipython` session, etc. When you are finished, simply type

    $ exit
    
and this will relinquish your allocation. 

## SLURM Scripts and mpi4py

I recommend the following workflow for running jobs on demon. Create a directory for the project from your home directory; the project directory I created for this tutorial is called `mpi_tutorials`. Put your python and SLURM scripts that you want to run in the project directory. I also recommend creating a `conda` environment for each project. I've included an [environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) file that creates an environment called "mpi", which my example scripts use. 

When running parallel jobs a SLURM script is used to specify what resources you are requesting from demon and constraints on those resources (e.g. how much time to give the job) using #SBATCH commands at the top of the script (note that I have commented out the email options in my example scripts with double ##; if you would like to use the email option delete one of the # and change the email address to your own). This is used together with mpi4py to specify the various "processes" that will be run. Each "process" is a single instance of the python code being run (e.g. if you would like to do a parameter sweep then each process corresponds to one parameter value). 

When you are first getting started, you should create the "mpi" conda environment and try running `mpi_test.py` using `run_test.sl`. SLURM scripts are submitted using the `sbatch` command 

    $ sbatch run_test.sl 
    
By default, `run_test.sl` should call `srun -n 4 python ./mpi_test.py` (this should be the uncommented line at the end). When you run this code it will create an output and an error file, as specified with the `#SBATCH -o` and `#SBATCH -e` commands. When a job is run, SLURM assigns the job a job ID number, and the `%j` you see for the error and output commands assign the number to the output and error files, e.g. `4551335.out` and `4551335.err`. If there are any errors, they will be printed in the `.err` file. If there are no errors, the code output will be written to the `.out` file. For this test code you should see

    Hello, I am rank 0 of 4
    Hello, I am rank 1 of 4
    Hello, I am rank 2 of 4
    Hello, I am rank 3 of 4
    
The numbers may not be in order, but that's alright. Here, there are four different processes being run and "rank" refers to the individual ID of each process.

If you see four lines of `Hello, I am rank 0 of 1`, then mpi4py and SLURM are not communicating properly. In this case, try running with the line `mpirun -bootstrap slurm -n 4 python ./mpi_test.py` in `run_test.sl`. 

Once `mpi_test.py` and `run_test.sl` are working properly, you are ready to run your own jobs. See `mpi_example.py` and `run_example.sh` for more realistic scripts that you should be able to adapt for your purposes. 
