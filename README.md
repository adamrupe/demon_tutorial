# Tutorial for using Demon
Example and test code for getting started on the Linux cluster at the Complexity Sciences Center, UC Davis

## Getting Started:

For information on demon.csc and how to request access, visit http://csc.ucdavis.edu/Resources.html

Once you have an account, you can log on to demon with ssh:

    $ ssh <your_username>@demon.csc.ucdavis.edu

On demon, view the available SLURM partitions and their status with 

    $ sinfo
    
See what jobs are currently running or queued with

    $ squeue
    
You can view the status of just your jobs with 

    $ squeue -u <your_username>
