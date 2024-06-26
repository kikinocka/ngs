#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N sp4
#PBS -l nodes=1:ppn=20
#PBS -l walltime=600:00:00

workdir='/mnt/data/kika/blastocrithidia/genomes/selenoproteins/'
genome='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/p57_polished.fa'
spp='bnon'
log=$workdir$spp'_sp4.log'


eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate sp4

cd $workdir
selenoprofiles -o $workdir -t $genome -s $spp -p eukarya -log $log -ncpus 20 -genetic_code 31 \
	-output_fasta -output_gff

conda deactivate


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: sp4 done
