#!/bin/bash
#PBS -N vsearch
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add swarm-3.0.3



# if [ $# != 1 ]; then
#     echo "You need to supply an input filename - this is your global dereplicated fasta file (not the bzip)!";
#     exit 1;
# fi

./swarm_fastidious.sh $1
