#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/home/users/kika/bnon_pfr_ko/'
annotation='bnon_proteins_annotated.gff3'
bamfile='bw2_mapping/bnon_PF16_KO.bw2_sorted.bam'
output='bnon_PF16_KO.featureCounts.txt'

featureCounts -p -O -T n -a $annotation -o $output $bamfile

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
