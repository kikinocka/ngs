#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N amoebae
#PBS -l nodes=1:ppn=80
#PBS -l walltime=600:00:00


cd '/home/users/kika/amoebae/'

eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate snakemake

# nohup snakemake get_ref_seqs -j 100 --use-conda &
nohup snakemake -j 100 --use-conda &

conda deactivate
