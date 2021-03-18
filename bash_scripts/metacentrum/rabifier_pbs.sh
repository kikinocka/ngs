#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=30:mem=80gb:scratch_local=150gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.4.2
module add samtools-1.11


/storage/brno12-cerit/home/kika/anaeramoeba/RABs