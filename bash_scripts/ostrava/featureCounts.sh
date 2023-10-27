#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N featureCounts
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/home/users/kika/bnon_pfr_ko/'
annotation='bnon_proteins_annotated.gtf'
bamfile='bw2_mapping/bnon_PF16_KO.bw2_sorted.bam'
output='bnon_PF16_KO.featureCounts.txt'

featureCounts -p -O -T 20 -a $annotation -o $output $bamfile

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: featureCounts done
